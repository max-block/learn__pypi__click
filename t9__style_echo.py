import click


@click.command()
def cli():
    click.secho("some error message!", fg="red")
    click.secho("bla bla", fg="green")
