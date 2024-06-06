import os
import sys

import argparse

from repository_setup.Controller import Controller

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path of the directory in which the repository shall be created")
    parser.add_argument("--name", "-n", type=str, required=True, help="Name of the new repository")
    args = parser.parse_args()

    repositoryDir = os.path.join(args.path, args.name)

    c = Controller()

    c.printHeader(args.path, args.name)
    c.createRepo(repositoryDir, args.name.replace("-", "_"))


if __name__ == "__main__":
    sys.exit(main())
