import click

@click.group()
def cli():
    pass

@cli.command()
def comando1():
    click.echo('Executando comando 1')

@cli.command()
def comando2():
    click.echo('Executando comando 2')

if __name__ == '__main__':
    cli()
