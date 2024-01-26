from __future__ import annotations

import typer
import uvicorn

from pos.runner.setup import setup_for_production

cli = typer.Typer(no_args_is_help=True, add_completion=False)


@cli.command(name="run")
def run(
    host: str = "127.0.0.1", port: int = 8000, database_name: str = "pos.db"
) -> None:
    uvicorn.run(host=host, port=port, app=setup_for_production(database_name))
