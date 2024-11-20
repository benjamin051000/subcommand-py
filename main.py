import argparse
import commands


def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands")

    # Get all the subcommands and set their subparsers up.
    for module_name in commands.command_names:
        module = getattr(commands, module_name)
        module.setup(subparsers)

    args = parser.parse_args()

    # Run the relevant command with its subparser.
    try:
        args.run(args)
    except AttributeError:
        parser.print_help()


if __name__ == "__main__":
    main()
