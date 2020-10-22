import click


@click.command()
@click.option("--shout/--no-shout", default=False)
def cli(shout):
    click.echo(f"shout flag value: {shout}")
