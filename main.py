#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence, at most 200 characters, pitching a bizarre
startup idea that sounds absurd until the business logic lands.
Deterministic: the same pitch on every run, stdlib only, no network.
"""

import os

PITCH = (
    "Hire a professional rival: a trained athlete who trash-talks you "
    "and beats your personal best by one percent, because gym members pay "
    "more to beat a person than to beat a clock."
)


def main() -> None:
    if not 1 <= len(PITCH) <= 200:
        raise SystemExit("pitch must be 1-200 characters, got %d" % len(PITCH))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
