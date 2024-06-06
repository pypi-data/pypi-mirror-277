from dataclasses import dataclass, field
import tosholi
from pathlib import Path


CONFIG_DIR = Path.home() / ".config" / "serverctl"
CONFIG_FILE = CONFIG_DIR / "config.toml"


SERVERS_DIR = Path.home() / ".local" / "share" / "serverctl" / "servers"
LOGS_DIR = Path.home() / ".local" / "share" / "serverctl" / "logs"

SERVICE_FILE = Path(__file__).parent.parent / "serverctl@.service"

CONFIG_DIR.mkdir(exist_ok=True, parents=True)
SERVERS_DIR.mkdir(exist_ok=True, parents=True)
LOGS_DIR.mkdir(exist_ok=True, parents=True)

if not CONFIG_FILE.exists():
    CONFIG_FILE.write_text(
        (Path(__file__).parent.parent / "config.template.toml").read_text()
    )


@dataclass
class Git:
    url: str
    branch: str | None = None
    recursive: bool = False


@dataclass
class Server:
    run: str
    cwd: str | None = None
    git: str | Git | None = None
    env: dict[str, str] = field(default_factory=dict)
    build: str | None = None
    clean: str | None = None


@dataclass
class Config:
    server: dict[str, Server] = field(default_factory=dict)

    @staticmethod
    def load():
        if not CONFIG_FILE.exists():
            return Config()
        with open(CONFIG_FILE, "rb") as f:
            config = tosholi.load(Config, f)  # type: ignore
        return config


CONFIG = Config.load()
