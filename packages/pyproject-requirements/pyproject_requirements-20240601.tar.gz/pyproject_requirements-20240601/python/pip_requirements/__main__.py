#!/bin/env python
"""

Note: https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
PIP does not have a fucking Python API 😐
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import cast

import toml

DESCRIPTION = """
Install dependencies from a pyproject file.

Example:

pip-requirements install [--pip path/to/pip] --all pyproject.toml
"""


def get_argument_parser():
    found_pip = shutil.which("pip")

    if found_pip is None:
        found_pip = ""

    root_parser = argparse.ArgumentParser(
        prog="pip-requirements",
        description=DESCRIPTION,
    )

    subparsers = root_parser.add_subparsers(
        dest='command',
        title="commands",
        description="Valid commands",
        help="Commands you may enter.",
        required=True,
    )

    parser = subparsers.add_parser("install")
    parser.add_argument("pyproject_toml", help="pyproject.toml")
    parser.add_argument(
        "--all",
        default=False,
        action="store_true",
        help="Install dependencies from all known sections (required and optional).",
    )
    parser.add_argument(
        "--required",
        default=False,
        action="store_true",
        help="Install required dependencies.",
    )
    parser.add_argument(
        "--optional",
        nargs="*",
        default=[],
        help="Optional dependency to install. May be specified multiple times.",
    )
    parser.add_argument(
        "--pip",
        default=found_pip,
        required=False if found_pip else True,
        help=f"Pip tool to use. Autodetected. Default: {found_pip}",
    )
    parser.add_argument(
        "--dry",
        help="Dry run",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--target",
        default=None,
        help="Install requirements to target path specified. Ignores already installed dependencies.",
    )


    parser = subparsers.add_parser(
        "txt",
        description="Generate a requirements.txt files for compatibility.",
    )
    parser.add_argument("pyproject_toml", help="pyproject.toml")
    parser.add_argument(
        "output_file",
        nargs="?",
        default=None,
        help="path to a file to output. stdout otherwise.",
    )
    parser.add_argument(
        "--all",
        default=False,
        action="store_true",
        help="Include dependencies from all known sections (required and optional)."
    )
    parser.add_argument(
        "--required",
        default=False,
        action="store_true",
        help="Include required dependencies.",
    )
    parser.add_argument(
        "--optional",
        nargs="*",
        default=[],
        help="Include optional dependency. May be specified multiple times."
    )

    return root_parser


def pip_install(deps: list[str], pip_tool: Path, args: list[str]):
    arg = [pip_tool.as_posix(), "install"] + args + deps
    print("Running:", " ".join(arg))
    result = subprocess.run(arg)
    if result.returncode != 0:
        print("Error installing packages with pip:")
        print(result.stderr)
        sys.exit(-1)


def get_packages_to_install(pyproject_toml: Path, all=False, required=True, optional=False):
    install_list = []
    with pyproject_toml.open("r") as f:
        d = toml.load(f)

        project = d.get("project", None)

        if project is None:
            return install_list

        if all or required:
            install_list += project.get("dependencies", [])

        if all:
            for category, deps in project.get("optional-dependencies", {}).items():
                install_list += deps
        else:
            for optional_name in optional:
                optional = project.get("optional-dependencies").get(optional_name, None)
                if optional is None:
                    print(f"No optional dependency section: {optional_name}")
                    sys.exit(-1)

                install_list += optional
    return install_list


def open_toml_file(pyproject_toml):
    tomlfile = Path(pyproject_toml).expanduser().resolve()
    if not tomlfile.exists():
        print(f"pyproject.toml does not exist at {pyproject_toml}")
        sys.exit(-1)
    return tomlfile


def main_generate_txt(args, extra_args):

    if args.output_file:
        output = Path(args.output_file).expanduser()
        if not output.parent.exists():
            print(f"Parent directory of output file {output} doesn't exist.")
            sys.exit(-1)

        output = output.open("w")
    else:
        output = sys.stdout

    tomlfile = open_toml_file(args.pyproject_toml)

    if not tomlfile.exists():
        print(f"pyproject.toml does not exist at {args.pyproject_toml}")
        sys.exit(-1)

    install_list = get_packages_to_install(
        tomlfile,
        all=args.all,
        required=args.required,
        optional=args.optional,
    )

    if not install_list:
        sys.exit(0)

    for line in install_list:
        print(line, file=output)


def main_install(args, extra_args):
    tomlfile = open_toml_file(args.pyproject_toml)

    pip_tool = Path(args.pip).expanduser()

    if pip_tool.exists() is False:
        print(f"Error: pip executable does not exist at {pip_tool}")
        sys.exit(-1)

    if os.access(pip_tool, os.X_OK) is False:
        print(f"Error: pip is not executable at {pip_tool}")
        sys.exit(-1)

    print("Reading pyproject file: ", tomlfile)
    install_list = get_packages_to_install(
        tomlfile,
        all=args.all,
        required=args.required,
        optional=args.optional,
    )

    if not install_list:
        print("Nothing found to install.")
        sys.exit(-1)
    print("Installing required packages: ", install_list)

    if args.target:
        extra_args += ["--target", Path(args.target).expanduser().resolve(strict=False).as_posix()]

    if not args.dry:
        pip_install(install_list, pip_tool, extra_args)


def main():

    values = cast(list, sys.argv)
    try:
        dash_index = values.index("--")
        extra_args = values[dash_index + 1:]
        args = values[1:dash_index]
    except ValueError:
        args = values[1:]
        extra_args = []

    parser = get_argument_parser()
    args = parser.parse_args(args)

    if args.command == "install":
        main_install(args, extra_args)
    elif args.command == "txt":
        main_generate_txt(args, extra_args)


if __name__ == "__main__":
    main()
