#!/usr/bin/env python3
import os
import sys

import output
from data import Event
from util import load_json

if __name__ == "__main__":
    try:
        path, old_file, old_hex, old_mode, new_file, new_hex, new_mode = sys.argv[1:8]
        remaining_args = sys.argv[8:]
    except ValueError:
        try:
            old_file, new_file = sys.argv[1:3]
            remaining_args = sys.argv[3:]
        except ValueError:
            print("Usage:")
            print("difftool.py <path> <old_file> <old_hex> <old_mode> <new_file> <new_hex> <new_mode>")
            print("or difftool.py <old_file> <new_file>")
            sys.exit(1)

    old_event = Event.from_json(load_json(old_file))
    new_event = Event.from_json(load_json(new_file))

    if (
        "--both" in remaining_args
        or "--reg" in remaining_args
        and "--event" in remaining_args
        or os.environ.get("CDEDIFF_BOTH_VIEW")
        or os.environ.get("CDEDIFF_VIEW", "").lower() == "both"
    ):
        output.print_event_diff(old_event, new_event)

        print()
        print("=" * 80)
        print()

        output.print_event_registrations_diff(old_event, new_event)
    elif "--reg" in remaining_args or os.environ.get("CDEDIFF_REG_VIEW") or os.environ.get("CDEDIFF_VIEW", "").lower() == "reg":
        output.print_event_registrations_diff(old_event, new_event)
    elif (
        "--event" in remaining_args
        or os.environ.get("CDEDIFF_EVENT_VIEW")
        or os.environ.get("CDEDIFF_VIEW", "").lower() == "event"
    ):
        output.print_event_diff(old_event, new_event)
    else:
        # Default to reg.
        output.print_event_registrations_diff(old_event, new_event)
