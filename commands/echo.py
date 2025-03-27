import click


@click.command()
@click.option("--double", is_flag=True, help="print it twice")
@click.argument("text")
def echo(double: bool, text: str):
    """Print TEXT to the screen."""

    print(text)

    if double:
        print(text)
