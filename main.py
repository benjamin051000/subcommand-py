import argparse
from glob import glob
from importlib import import_module


def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands")

    for filename in glob("commands/*.py"):
        module_name = filename.replace('/', '.').rstrip(".py")
        module = import_module(module_name)
        # The rule is that each module has a method called setup.
        module.setup(subparsers)

    args = parser.parse_args()

    # Run the relevant command with its subparser.
    try:
        args.run(args)
    except AttributeError:
        parser.print_help()


if __name__ == "__main__":
    main()
