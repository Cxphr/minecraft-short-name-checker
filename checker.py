#!/usr/bin/env python3
"""Filter candidate Minecraft usernames to those shorter than four characters."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Filter names to usernames 1–3 characters long.")
    parser.add_argument("names", nargs="*", help="Candidate usernames; if omitted, read one per line from stdin.")
    args = parser.parse_args()

    if args.names:
        names = args.names
    else:
        import sys
        names = sys.stdin.read().splitlines()

    matches = [name.strip() for name in names if 1 <= len(name.strip()) < 4]
    print("\n".join(matches))


if __name__ == "__main__":
    main()
