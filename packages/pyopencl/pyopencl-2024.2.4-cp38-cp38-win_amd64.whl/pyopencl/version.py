from importlib import metadata
VERSION_TEXT = metadata.version("pyopencl")

import re
_match = re.match("^([0-9.]+)([a-z0-9]*?)$", VERSION_TEXT)
VERSION_STATUS = _match.group(2)
VERSION = tuple(int(nr) for nr in _match.group(1).split("."))
