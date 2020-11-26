import click


@click.version_option("v0.1.2", help="Show the version and exit")
@click.command()
def cli():
    click.echo("I do nothing")


# t13 --version
# t13, version v0.1.2
