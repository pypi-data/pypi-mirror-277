import click
import os
import subprocess

@click.group()
def cli():
    pass

@cli.command()
def comando1():
    click.echo('Executando comando 1')

@cli.command()
def comando2():
    click.echo('Executando comando 2')

@cli.command()
def atualizar():
    click.echo('Atualizando meu-cli...')
    subprocess.run([os.sys.executable, '-m', 'pip', 'install', '--upgrade', 'meu-cli'])
    click.echo('Atualização concluída.')

if __name__ == '__main__':
    cli()
