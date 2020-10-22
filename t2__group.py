import click


@click.group()
def cli():
    pass


@cli.command()
def cmd1():
    click.echo("cmd1")


@cli.command()
def cmd2():
    click.echo("cmd2")
