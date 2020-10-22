from typing import List

import click


@click.command()
@click.argument("command", nargs=-1)
def cli(command: List[str]):
    click.echo(f"your command is: {command}")
