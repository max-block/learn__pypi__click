import click


@click.version_option("v0.1.2")
@click.command()
def cli():
    click.echo("I do nothing")


# t0 --node 1 --node 2
# your nodes is: ('1', '2')
