from dataclasses import dataclass, field
import tosholi
from pathlib import Path


SERVERCTL_DIR = Path.home() / ".serverctl"
SERVERCTL_DIR.mkdir(exist_ok=True, parents=True)


@dataclass
class Git:
    url: str
    branch: str | None = None
    gh: bool = False
    recursive: bool = False


@dataclass
class Server:
    git: str | Git
    run: str
    cwd: str | None = None
    env: dict[str, str] = field(default_factory=dict)
    build: str | None = None
    clean: str | None = None


@dataclass
class Config:
    server: dict[str, Server] = field(default_factory=dict)

    @staticmethod
    def load():
        if not (SERVERCTL_DIR / "config.toml").exists():
            return Config()
        with open(SERVERCTL_DIR / "config.toml", "rb") as f:
            config = tosholi.load(Config, f)  # type: ignore
        return config


CONFIG = Config.load()
