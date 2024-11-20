# subcommand-pattern
Testing various subcommand patterns.

# Structure
```
./
├── commands/
│   ├── __init__.py
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

