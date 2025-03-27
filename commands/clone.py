import click


@click.command()
@click.argument("url")
def clone(url: str):
    """Clones a git repo from URL (not actually)."""
    print(url)
    print(f"cloning from {url}...")
    print("done.")
