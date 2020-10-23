import click


@click.command()
def cli():
    password = click.prompt("Enter password", hide_input=True)
    click.echo(f"your password: {password}")
