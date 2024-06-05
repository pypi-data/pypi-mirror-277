import typer
from . import server

app = typer.Typer(pretty_exceptions_enable=False, add_completion=False)


@app.command(help="Start a server")
def start(name: str, clean: bool = False, update: bool = False):
    server.start_server(name, clean, update)


@app.command(help="Stop a server")
def stop(name: str):
    server.stop_server(name)


@app.command(help="Restart a server without cleaning, rebuilding or updating")
def restart(name: str):
    server.restart_server(name)


@app.command(help="Start all servers")
def start_all(clean: bool = False, update: bool = False):
    server.start_all_servers(clean, update)


@app.command(help="Stop all servers")
def stop_all():
    server.stop_all_servers()


@app.command(help="Update a server")
def update(name: str):
    server.update_server(name)


@app.command(help="Get the status of a server")
def status(name: str):
    server.show_server_status(name)


def main():
    app()
