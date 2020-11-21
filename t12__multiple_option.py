from typing import List

import click


@click.command()
@click.option("--node", multiple=True)
def cli(node: List[str]):
    click.echo(f"your nodes is: {node}")


# t0 --node 1 --node 2
# your nodes is: ('1', '2')
