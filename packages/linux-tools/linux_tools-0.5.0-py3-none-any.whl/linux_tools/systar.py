#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2023-2024 Robin Jarry

"""
Create gzipped tar archives of sysfs devfs folders. Properly handling file sizes without
errors.
"""

import argparse
import io
import os
import sys
import tarfile


# ------------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="""
        Print files and dirs on stderr as they are included in the archive.
        """,
    )
    parser.add_argument(
        "-f",
        "--file",
        help="""
        Output file to create. By default, gzipped tar archive is written to stdout.
        """,
    )
    parser.add_argument(
        "paths",
        metavar="PATH",
        nargs="+",
        help="""
        Path to include into archive (folder contents are included recursively).
        """,
    )
    args = parser.parse_args()

    try:
        if args.file is not None:
            fileobj = open(args.file, "wb")  # pylint: disable=consider-using-with
        else:
            fileobj = sys.stdout.buffer

        with tarfile.TarFile.gzopen(None, fileobj=fileobj, mode="w") as tar:
            for p in args.paths:
                if os.path.isdir(p):
                    for root, dirs, files in os.walk(p):
                        for d in dirs:
                            add_member(tar, os.path.join(root, d), args.verbose)
                        for f in files:
                            add_member(tar, os.path.join(root, f), args.verbose)
                else:
                    add_member(tar, p, args.verbose)

        if args.file is not None:
            fileobj.close()
    except Exception as e:
        sys.stderr.write(f"error: {e}\n")
        sys.stderr.flush()
        return 1

    return 0


def add_member(tar: tarfile.TarFile, path: str, verbose: bool = False):
    if verbose:
        print(path, file=sys.stderr)
    info = tar.gettarinfo(path)
    fileobj = None
    if info.type == tarfile.REGTYPE:
        # Regular files reported size is invalid in sysfs and devfs.
        # Read the file in # memory and use that as file object to get the correct size.
        with open(path, "rb") as f:
            buf = f.read()
        info.size = len(buf)
        fileobj = io.BytesIO(buf)
    tar.addfile(info, fileobj)


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
