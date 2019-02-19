"""
run.py
Run commands with ease.

For usage:
python run.py --help
"""
from cli import Cli
import argparse
import inspect
from pprint import pprint


def get_valid_commands():
    """Dynamically generate valid cli commands"""
    members = inspect.getmembers(Cli)
    return [x[0] for _, x in enumerate(members) if '__' not in x[0] and not x[0].startswith('_')]


def get_args():
    parser = argparse.ArgumentParser(description=("Run commands."))
    parser.add_argument('command', metavar='COMMAND',
            choices=get_valid_commands(), help="Valid commands: {}".format(get_valid_commands()))
    parser.add_argument('args', nargs=argparse.REMAINDER, help="Args to pass to COMMAND")
    return parser.parse_args()


def main():
    args = get_args()
    cmd = Cli()
    result = getattr(cmd, args.command)(*args.args)
    pprint(result)


if __name__ == "__main__":
    main()
