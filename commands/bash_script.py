import argparse
import sys
import subprocess
from pathlib import Path

def setup(subparsers: argparse._SubParsersAction):
    # NOTE: This command parses the args in the subprocess. Do nothing here
    cmd = subparsers.add_parser("bash", help="run the bash script")
    cmd.set_defaults(run=bash)
    

def bash(_):
    path_to_exe = Path("./commands/bash_script")
    temp = [path_to_exe] + sys.argv[1:]
    subprocess.run(temp)

