import os
from .util import exec
from .config import CONFIG, Server, SERVERCTL_DIR, Git
import textwrap


def get_service_config(name: str, cmd: str, env: dict[str, str]) -> str:
    env_str = " ".join(f"{key}={value}" for key, value in env.items())
    env_str = f"Environment={env_str}" if env_str else ""
    config = f"""
        [Unit]
        Description=serverctl-{name}
        After=network.target

        [Service]
        Type=simple
        Restart=on-failure
        WorkingDirectory=%h/.serverctl/servers/{name}
        ExecStart=/bin/bash -l -c 'exec "$@"' _  {cmd}
        StandardOutput=file:%h/.serverctl/logs/{name}.log
        {env_str}

        [Install]
        WantedBy=default.target
    """
    return textwrap.dedent(config).strip()


def init_server(name: str, server: Server):
    git = server.git if not isinstance(server.git, str) else Git(url=server.git)
    if not (SERVERCTL_DIR / "servers" / name).exists():
        (SERVERCTL_DIR / "servers").mkdir(exist_ok=True, parents=True)
        rec_args = ["--recursive"] if git.recursive else []
        branch_args = ["--branch", git.branch] if git.branch else []
        cwd = SERVERCTL_DIR / "servers"
        gitflags = [*branch_args, *rec_args]
        if git.gh:
            exec(
                "gh",
                "repo",
                "clone",
                git.url,
                name,
                *gitflags,
                cwd=cwd,
                check=True,
                dump=True,
            )
        else:
            exec(
                "git", "clone", git.url, name, *gitflags, cwd=cwd, check=True, dump=True
            )
    exec("git", "fetch", cwd=SERVERCTL_DIR / "servers" / name, check=True)
    if git.branch:
        exec(
            "git",
            "checkout",
            git.branch,
            cwd=SERVERCTL_DIR / "servers" / name,
            check=True,
        )
    if not (SERVERCTL_DIR / "servers" / name).exists():
        exit(f"❌ Error cloning repository {name}")


def clean_server(name: str, config: Server):
    try:
        if not config.clean:
            return
        exec(
            "bash",
            "--login",
            "-c",
            config.clean,
            cwd=SERVERCTL_DIR / "servers" / name,
            check=True,
            dump=True,
        )
    except Exception as e:
        exit(f"❌ Error cleaning server {name}: {e}")


def build_server(name: str, config: Server):
    try:
        if not config.build:
            return
        exec(
            "bash",
            "--login",
            "-c",
            config.build,
            cwd=SERVERCTL_DIR / "servers" / name,
            check=True,
            dump=True,
        )
    except Exception as e:
        exit(f"❌ Error building server {name}: {e}")


def start_server(name: str, clean: bool, update: bool, log=True):
    server = CONFIG.server.get(name)
    if server is None:
        exit(f"❌ Server {name} not found in config")
    try:
        # 1. Stop server if running
        exec("systemctl", "--user", "stop", f"serverctl-{name}", check=False)
        # 2. Clone repo if not exists
        init_server(name, server)
        # 3. Clean server
        if clean:
            clean_server(name, server)
        # 4. Update server
        if update:
            exec("git", "pull", cwd=SERVERCTL_DIR / "servers" / name, check=True)
        # 5. Build if needed
        if server.build:
            build_server(name, server)
        # 6. Start service
        service_file = SERVERCTL_DIR / "services" / f"serverctl-{name}.service"
        service_file.parent.mkdir(exist_ok=True, parents=True)
        (SERVERCTL_DIR / "logs").mkdir(exist_ok=True, parents=True)
        service_file.write_text(get_service_config(name, server.run, server.env))
        exec("systemctl", "--user", "link", service_file, check=True)
        exec("systemctl", "--user", "daemon-reload", check=True)
        exec("systemctl", "--user", "restart", f"serverctl-{name}", check=True)
        exec("systemctl", "--user", "enable", f"serverctl-{name}", check=True)
        exec("loginctl", "enable-linger", os.getlogin(), check=True)
    except Exception as e:
        exit(f"❌ Error starting server {name}: {e}")
    if log:
        print(f"✅ Server {name} started")


def stop_server(name: str):
    server = CONFIG.server.get(name)
    if server is None:
        exit(f"❌ Server {name} not found in config")
    try:
        exec("systemctl", "--user", "stop", f"serverctl-{name}", check=True)
        exec("systemctl", "--user", "disable", f"serverctl-{name}", check=True)
    except Exception as e:
        exit(f"❌ Error stopping server {name}: {e}")
    print(f"✅ Server {name} stopped")


def restart_server(name: str):
    exec("systemctl", "--user", "restart", f"serverctl-{name}", check=True)
    print(f"✅ Server {name} restarted")


def start_all_servers(clean: bool, update: bool):
    for name in CONFIG.server:
        start_server(name, clean, update)


def stop_all_servers():
    for name in CONFIG.server:
        stop_server(name)


def update_server(name: str):
    server = CONFIG.server.get(name)
    print(f"Updating server {name}...")
    if server is None:
        exit(f"❌ Server {name} not found in config")
    try:
        exec("git", "pull", cwd=SERVERCTL_DIR / "servers" / name, check=True)
        start_server(name, clean=True, update=False, log=False)
    except Exception as e:
        exit(f"❌ Error updating server {name}: {e}")
    print(f"✅ Server {name} updated")


def show_server_status(name: str):
    exec("systemctl", "--user", "status", f"serverctl-{name}", dump=True)
