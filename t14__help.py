import click


@click.help_option(help="Show this message and exit")
@click.command()
def cli():
    click.echo("I do nothing")
