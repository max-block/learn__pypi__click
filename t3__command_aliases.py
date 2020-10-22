import click
from click_aliases import ClickAliasedGroup


@click.group(cls=ClickAliasedGroup)
def cli():
    pass


@cli.command(aliases=["i", "inst"])
def install():
    click.echo("install")


@cli.command(aliases=["d", "uninstall", "remove"])
def delete():
    click.echo("delete")
