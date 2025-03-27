import click
from glob import glob
from importlib import import_module


@click.group()
def cli():
    pass


def main():
    for filename in glob("commands/*.py"):
        module_name = filename.replace("/", ".").rstrip(".py")
        module = import_module(module_name)

        # The rule is that each module has a click.command with the same name.
        _, command_name = module_name.split(".")
        command = getattr(module, command_name)
        cli.add_command(command)

    cli()


if __name__ == "__main__":
    main()
