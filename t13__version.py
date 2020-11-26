import click


@click.version_option("v0.1.2")
@click.command()
def cli():
    click.echo("I do nothing")


# t13 --version
# t13, version v0.1.2
