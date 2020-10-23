import click


@click.command()
@click.option("--shout/--no-shout", default=False)
@click.option("--flag", is_flag=True)
def cli(shout: bool, flag: bool):
    click.echo(f"shout: {shout}, flag: {flag}")
