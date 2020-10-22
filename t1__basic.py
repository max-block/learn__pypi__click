from typing import List

import click


@click.command()
@click.option("-n", "--name", help="bla bla name")
@click.option("-a", "--addresses", multiple=True)
@click.argument("command", type=click.Choice(["cmd1", "cmd2"]))
def cli(name: str, addresses: List[str], command: str):
    click.echo(f"your command is: {command}")
    click.echo(f"your name is: {name}")
    click.echo(f"addresses: {addresses}")
