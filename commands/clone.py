import argparse

def setup(subparsers: argparse._SubParsersAction):
    cmd = subparsers.add_parser("clone", help="clone a repository.")
    cmd.add_argument("url", help="HTTPS URL of the repository.")
    cmd.set_defaults(run=clone)

def clone(args):
    """Clones a git repo"""
    print(args)
    print(f"cloning from {args.url}...")
    print("done.")

