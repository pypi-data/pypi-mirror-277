# hello_world/cli.py
import click
from hello1 import hello

@click.command()
def greet():
    """Simple program that greets the user."""
    click.echo(hello())

if __name__ == '__main__':
    greet()
