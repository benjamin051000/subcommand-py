import click
import sys
import subprocess
from pathlib import Path

@click.command
def bash():
    """Run a bash subprocess."""
    path_to_exe = Path("./commands/bash_script")
    temp = [path_to_exe] + sys.argv[1:]
    breakpoint()
    subprocess.run(temp)

