#!/usr/bin/env python3
"""Require a Doxygen file comment in each public plugin header."""

from __future__ import annotations

import re
import sys

from check_text import ROOT, repository_files

FILE_COMMENT = re.compile(r"(?:@file|\\file)\b")


def public_headers():
    return [
        path
        for path in repository_files()
        if path.is_file() and path.suffix.lower() in {".h", ".hpp"} and "Public" in path.relative_to(ROOT).parts
    ]


def main() -> int:
    headers = public_headers()
    missing = []
    for path in headers:
        source = path.read_text(encoding="utf-8-sig")
        if not FILE_COMMENT.search(source):
            missing.append(path.relative_to(ROOT).as_posix())
    for path in missing:
        print(f"{path}: missing Doxygen @file comment", file=sys.stderr)
    print(f"Checked {len(headers)} public headers; {len(missing)} issue(s).")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
