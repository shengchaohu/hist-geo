import click

import backend


@click.command()
def entry_point() -> None:
    click.echo(backend.__version__)


if __name__ == "__main__":
    entry_point()
