#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2023-2024 Robin Jarry

"""
Display process statistics: CPU/NUMA affinity, context switches (voluntary and
non-voluntary) and thread names.
"""

import argparse
import os
import pathlib
import re
import sys

from . import bits, irqstat, table


# ------------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-r",
        "--root",
        default="/",
        help="""
        Root dir used to determine path to /proc (default /).
        """,
    )
    parser.add_argument(
        "-e",
        "--exact",
        action="store_true",
        help="""
        Display exact stats values.
        """,
    )
    parser.add_argument(
        "pids",
        metavar="PID",
        nargs="+",
        type=int,
        help="""
        Process ID for which to display statistics.
        """,
    )
    args = parser.parse_args()

    try:
        os.chdir(args.root)
        pids = {}
        for pid in args.pids:
            for thread in pathlib.Path(f"proc/{pid}").glob("task/*/status"):
                status = parse_status(thread)
                pids[status["pid"]] = status

        if set(args.pids) - pids.keys():
            raise ValueError(f"no such PIDs: {set(args.pids) - pids.keys()}")

    except Exception as e:
        sys.stderr.write(f"error: {e}\n")
        sys.stderr.flush()
        return 1

    if args.exact:
        num_format = str
    else:
        num_format = irqstat.human_readable

    t = table.Table()
    t.add_column("PID")
    t.add_column("CPUs", convert=bits.bit_list)
    t.add_column("NUMAs", convert=bits.bit_list)
    t.add_column("NONVOL_CTX_SW", align=">", convert=num_format)
    t.add_column("VOL_CTX_SW", align=">", convert=num_format)
    t.add_column("COMM")

    for pid, p in sorted(pids.items()):
        t.add_row(
            [
                pid,
                p["cpu_affinity"],
                p["mem_affinity"],
                p["nonvoluntary_ctxt_switches"],
                p["voluntary_ctxt_switches"],
                p["name"],
            ]
        )

    t.print(sys.stdout)

    return 0


# ------------------------------------------------------------------------------
STATUS_LINE_RE = re.compile(r"^([^:]+):\s+(.*)$", re.MULTILINE)


def parse_status(path: pathlib.Path) -> dict:
    raw = {}
    for match in STATUS_LINE_RE.finditer(path.read_text(encoding="ascii")):
        raw[match.group(1)] = match.group(2).strip()
    return {
        "name": raw["Name"],
        "pid": int(raw["Pid"]),
        "cpu_affinity": bits.mask_or_list(raw["Cpus_allowed_list"]),
        "mem_affinity": bits.mask_or_list(raw["Mems_allowed_list"]),
        "voluntary_ctxt_switches": int(raw["voluntary_ctxt_switches"]),
        "nonvoluntary_ctxt_switches": int(raw["nonvoluntary_ctxt_switches"]),
    }


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
