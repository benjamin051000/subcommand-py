import click
import subprocess
from pathlib import Path

# See https://click.palletsprojects.com/en/stable/advanced/#forwarding-unknown-options
@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument("bash_args", nargs=-1, type=click.UNPROCESSED)
def bash(bash_args: tuple[str, ...]) -> None:
    """Run a bash subprocess."""
    path_to_exe = Path("./commands/bash_script")
    temp = [path_to_exe] + list(bash_args)
    subprocess.run(temp)
