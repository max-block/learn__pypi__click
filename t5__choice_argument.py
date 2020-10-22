from typing import List

import click


@click.command()
@click.argument("command", type=click.Choice(["cmd1", "cmd2"]))
def cli(command: str):
    click.echo(f"your command is: {command}")
