import json
import pathlib
import sys
from typing import Any


def load_json(path: str) -> dict[str, Any]:
    try:
        return json.loads(pathlib.Path(path).read_text())
    except json.decoder.JSONDecodeError:
        print(f"Could not decode JSON file {path!r}.")
    except FileNotFoundError:
        print(f"File {path!r} not found.")
    except PermissionError:
        print(f"Could not open file {path!r}.")
    sys.exit()
