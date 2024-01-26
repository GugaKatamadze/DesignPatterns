import typer

from pos.pos import POS

cli = typer.Typer()


@cli.command(name="list")
def pos_list() -> None:
    POS.list()


@cli.command(name="simulate")
def pos_simulate() -> None:
    POS.simulate()


@cli.command(name="setup")
def pos_setup() -> None:
    POS.setup()


@cli.command(name="report")
def pos_report() -> None:
    POS.report()


if __name__ == "__main__":
    cli()
