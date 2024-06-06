import os
import sys
from typing import Dict, Optional
import subprocess


def exec(
    prog: str | os.PathLike,
    *args: str | os.PathLike | None,
    cwd: str | os.PathLike = ".",
    env: Optional[Dict[str, str]] = None,
    check: bool = False,
    dump: bool = False,
):
    """Run a command and return the status."""
    cmd: list[str] = [str(prog), *(str(arg) for arg in args if arg is not None)]
    result = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE if not dump else None,
        stderr=subprocess.PIPE if not dump else None,
    )
    if check and result.returncode:
        sys.stderr.buffer.write(result.stderr)
        sys.stderr.buffer.flush()
        sys.exit(result.returncode)
    return result.returncode
