from . import clone
from . import echo
from . import bash_script

command_names = [ s for s in dir() if not s.startswith("__") and not s.endswith("__") ]

