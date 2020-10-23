import click


@click.command()
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=False)
def cli(password: str):
    click.secho(f"your password: {password}")
