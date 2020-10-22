import click


@click.command()
@click.option("--id", "id_", default=777)
def cli(id_):
    click.echo(f"id: {id_}")
