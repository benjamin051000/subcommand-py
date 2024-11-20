import argparse

def setup(subparsers: argparse._SubParsersAction):
    cmd = subparsers.add_parser("echo", help="print to the screen")
    cmd.add_argument("--double", action="store_true", help="print it twice")
    cmd.add_argument("text", help="text to print")
    cmd.set_defaults(run=echo)
    

def echo(args):
    """Prints text to the screen."""
    msg = f"{args.text}"

    print(msg)

    if args.double:
        print(msg)

