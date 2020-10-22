import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("version")
@click.pass_context
def cmd1(ctx, version):
    ctx.forward(c1)
    ctx.forward(c2)


@cli.command()
@click.argument("version")
@click.pass_context
def cmd2(ctx, version):
    ctx.invoke(c1, version=777)
    ctx.invoke(c2, version=999)


@cli.command()
@click.argument("version")
def c1(version):
    click.echo(f"c1({version})")


@cli.command()
@click.argument("version")
def c2(version):
    click.echo(f"c2({version})")
