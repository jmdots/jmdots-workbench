import click
from workbench.clipboard import Clipboard
import sys

@click.command()
@click.argument('text', required=False)
@click.option('--file', '-f', 'is_file', is_flag=True, help="Indicate the input is a filename")
def copy(text, is_file):
    """Copy text to clipboard from input text, file, or stdin."""
    wb = Clipboard()
    if is_file:
        if text:
            try:
                with open(text, 'r') as file:
                    text = file.read()
                    wb.copy(text)
            except FileNotFoundError:
                click.echo(f"File not found: {text}")
        else:
            click.echo("No file provided to copy.")
    else:
        if text:
            wb.copy(text)
        elif not sys.stdin.isatty():
            text = sys.stdin.read()
            wb.copy(text)
        else:
            click.echo("No text provided to copy.")
