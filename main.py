#!/usr/bin/env python3
"""Entrypoint for the news-image-20261126 entry.

The repository ships its finished front page as ``entry.png`` beside
this file. Running the program delivers those exact bytes to the
output directory the harness names: ``MAKEFUN_OUTPUT_DIR`` when that
variable is set, otherwise ``/output``. Nothing is drawn or fetched
here, so every run writes identical bytes.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def target_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    src = source_path()
    if not os.path.isfile(src):
        print(f"missing image: {src}", file=sys.stderr)
        return 1
    out_dir = target_dir()
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    # The copy only counts as delivered whole if its size matches the
    # source exactly; anything shorter means the run failed.
    if os.path.getsize(dst) != os.path.getsize(src):
        print(f"short copy: {dst}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
