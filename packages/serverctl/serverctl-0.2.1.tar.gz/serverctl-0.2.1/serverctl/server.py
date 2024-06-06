import os
from pathlib import Path
import subprocess
from .util import exec
from .config import CONFIG, Server, SERVERCTL_DIR, Git


def global_init():
    # Create serverctl directory
    SERVERCTL_DIR.mkdir(exist_ok=True, parents=True)
    (SERVERCTL_DIR / "servers").mkdir(exist_ok=True, parents=True)
    (SERVERCTL_DIR / "logs").mkdir(exist_ok=True, parents=True)
    # Copy template service file
    service_file = Path(__file__).parent.parent / "serverctl@.service"
    service_file_dest = SERVERCTL_DIR / "serverctl@.service"
    if not service_file_dest.exists():
        service_file_dest.write_text(service_file.read_text())


global_init()


def cleanup_servers(log=True):
    # Get all running servers
    result = subprocess.check_output(
        ["systemctl", "--user", "list-units", "--type=service"]
    )
    lines = [l.strip() for l in result.decode().splitlines()]
    servers = [l.split()[0] for l in lines if l.startswith("serverctl@")]
    server_names = [s.split("@")[1].split(".service")[0] for s in servers]
    # Stop all running servers that are not in the config
    for name in server_names:
        if name not in CONFIG.server:
            try:
                exec("systemctl", "--user", "stop", f"serverctl@{name}", check=True)
                exec("systemctl", "--user", "disable", f"serverctl@{name}", check=True)
            except Exception as e:
                print(f"❌ Failed to stop server {name}: {e}")
            try:
                # Remove git repo
                exec("rm", "-rf", SERVERCTL_DIR / "servers" / name, check=True)
            except Exception as e:
                print(f"❌ Failed to delete server {name}: {e}")
            if log:
                print(f"✅ Removed server: {name}")


def init_server(name: str, server: Server):
    git = server.git if not isinstance(server.git, str) else Git(url=server.git)
    if not git:
        # No git repo to clone
        return
    if not (SERVERCTL_DIR / "servers" / name).exists():
        rec_args = ["--recursive"] if git.recursive else []
        branch_args = ["--branch", git.branch] if git.branch else []
        cwd = SERVERCTL_DIR / "servers"
        gitflags = [*branch_args, *rec_args]
        exec("git", "clone", git.url, name, *gitflags, cwd=cwd, check=True, dump=True)
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
        exec("systemctl", "--user", "stop", f"serverctl@{name}", check=False)
        # 2. Clone repo if not exists
        init_server(name, server)
        # 3. Clean server
        if clean:
            clean_server(name, server)
        # 4. Update server
        if update and server.git:
            exec("git", "pull", cwd=SERVERCTL_DIR / "servers" / name, check=True)
        # 5. Build if needed
        if server.build:
            build_server(name, server)
        # 6. Start service
        service_file = SERVERCTL_DIR / f"serverctl@.service"
        exec("systemctl", "--user", "link", service_file, check=True)
        exec("systemctl", "--user", "daemon-reload", check=True)
        # exec("systemctl", "--user", "start", f"serverctl@{name}.service", check=True)
        exec("systemctl", "--user", "restart", f"serverctl@{name}", check=True)
        exec("systemctl", "--user", "enable", f"serverctl@{name}", check=True)
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
        exec("systemctl", "--user", "stop", f"serverctl@{name}", check=True)
        exec("systemctl", "--user", "disable", f"serverctl@{name}", check=True)
    except Exception as e:
        exit(f"❌ Error stopping server {name}: {e}")
    print(f"✅ Server {name} stopped")


def restart_server(name: str):
    exec("systemctl", "--user", "restart", f"serverctl@{name}", check=True)
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
        if not server.git:
            exec("git", "pull", cwd=SERVERCTL_DIR / "servers" / name, check=True)
        start_server(name, clean=True, update=False, log=False)
    except Exception as e:
        exit(f"❌ Error updating server {name}: {e}")
    print(f"✅ Server {name} updated")


def show_server_status(name: str):
    exec("systemctl", "--user", "status", f"serverctl@{name}", dump=True)


def run_server(name: str):
    server = CONFIG.server.get(name)
    if server is None:
        exit(f"❌ Server {name} not found in config")
    try:
        print(f"🟢 Starting server {name} ...")
        env = os.environ.copy()
        env.update(server.env)
        env = {k: v for k, v in env.items() if v is not None}
        exec(
            "bash",
            "-l",
            "-c",
            server.run,
            cwd=server.cwd or (SERVERCTL_DIR / "servers" / name),
            env=env,
            dump=True,
            check=True,
        )
    except Exception as e:
        exit(f"❌ Error running server {name}: {e}")
