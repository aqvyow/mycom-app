"""Tiny CLI used to give the pipeline something real to build, test and ship."""

from __future__ import annotations

import argparse
import json
import sys

from mycom_app import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mycom-app", description="Lab CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    greet = sub.add_parser("greet", help="print a greeting")
    greet.add_argument("--name", default="world")

    sub.add_parser("version", help="print the installed version")

    return parser


def run(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "version":
        print(json.dumps({"name": "mycom-app", "version": __version__()}))
        return 0
    if args.command == "greet":
        print(f"hello, {args.name}")
        return 0
    return 2


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
