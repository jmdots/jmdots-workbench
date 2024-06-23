import click
from workbench.clipboard import Clipboard

@click.command()
@click.argument('output', required=False)
@click.option('--file', '-f', 'is_file', is_flag=True, help="Indicate the output is a filename")
def paste(output, is_file):
    """Paste text from clipboard to stdout or file."""
    wb = Clipboard()
    text = wb.paste()
    if is_file:
        if output:
            with open(output, 'w') as file:
                file.write(text)
        else:
            click.echo("No file provided to paste.")
    else:
        click.echo(text)
