#!/usr/bin/env python3
import argparse
import pathlib
import subprocess
import sys

parser = argparse.ArgumentParser()

parser.add_argument(
    "event_keeper_dir",
    action="store",
    default=pathlib.Path.cwd(),
    type=pathlib.Path,
    help="The path to the event keeper repository to set up. Alternatively run this script from that directory.",
)

view = parser.add_mutually_exclusive_group()
view.add_argument("--event", action="store_true", help="If given, use the event view by default.")
view.add_argument("--reg", action="store_true", help="If given, use the registration view by default.")
view.add_argument("--remove", action="store_true", help="If given, remove all diff handling.")

args = parser.parse_args()

if args.event:
    diff = "event"
elif args.reg:
    diff = "reg"
elif args.remove:
    diff = "remove"
else:
    diff = "event"

cdediff_path = pathlib.Path(__file__).parent.resolve()
python_executable = sys.executable
difftool_path = cdediff_path / "difftool.py"
requirements_path = cdediff_path / "requirements.txt"

subprocess.check_call(
    [  # noqa: S607
        "git",
        "config",
        "diff.event.command",
        f'FORCE_COLOR=1 CDEDIFF_VIEW=event "{python_executable}" "{difftool_path}"',
    ],
    cwd=args.event_keeper_dir,
    shell=False,  # noqa: S603
)
subprocess.check_call(
    [  # noqa: S607
        "git",
        "config",
        "diff.reg.command",
        f'FORCE_COLOR=1 CDEDIFF_VIEW=reg "{python_executable}" "{difftool_path}"',
    ],
    cwd=args.event_keeper_dir,
    shell=False,  # noqa: S603
)

(args.event_keeper_dir / ".gitattributes").write_text("" if args.remove else f"*.json diff={diff}\n")

subprocess.check_call(
    [
        python_executable,
        "-m",
        "pip",
        "install",
        "-r",
        requirements_path,
    ],
    cwd=cdediff_path,
    shell=False,  # noqa: S603
    stdout=subprocess.DEVNULL,
)

if args.remove:
    print("Removed diff handling from event keeper repository.")
else:
    print(f"Configured event keeper repository to use {diff}-based diff view.")
