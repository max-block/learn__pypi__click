import click


@click.help_option(help="Show this message and exit")
@click.command()
def cli():
    click.echo("I do nothing")


# t0 --node 1 --node 2
# your nodes is: ('1', '2')
