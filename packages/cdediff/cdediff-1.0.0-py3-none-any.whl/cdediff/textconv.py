#!/usr/bin/env python3
import sys

import output
from data import Event
from util import load_json

if __name__ == "__main__":
    if len(sys.argv) > 1:
        event = Event.from_json(load_json(sys.argv[1]))
        # output.print_event(event)
        output.print_registrations(event)
    else:
        print("Usage: textconv.py <json file>")
