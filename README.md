# subcommand-pattern
Testing various subcommand patterns.

> [!TIP]
> Each structure has its own git tag.
> Open them to see the differences:
> - [argparse](https://github.com/benjamin051000/subcommand-py/tree/argparse-1.0)
> - [click](https://github.com/benjamin051000/subcommand-py/tree/click-1.0)

# Structure
```
./
├── commands/
│   ├── __init__.py
│   ├── bash_script
│   ├── bash_script.py
│   ├── clone.py
│   └── echo.py
└── main.py
```

## `main.py`
Entrypoint.

Registers all subcommands and does the actual parsing.

## `commands/__init__.py`
Imports all subcommands beneath it.

# Subcommand Structure
A subcommand must have a `setup` function with the following signature:
```python
def setup(subparsers: argparse._SubParsersAction) -> None:
    cmd = subparsers.add_parser(...)
    cmd.set_defaults(run=...)
```

