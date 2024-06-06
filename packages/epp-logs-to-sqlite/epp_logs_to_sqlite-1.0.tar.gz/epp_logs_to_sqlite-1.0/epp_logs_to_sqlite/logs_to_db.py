import time
import os
from contextlib import contextmanager, suppress
import sqlite3
import sys

from .logs_parser import (
    parse_entries_files,
    add_scope,
    create_db,
    add_column_to_table,
    write,
)


@contextmanager
def time_it(msg, *args, **kwds):
    start = time.monotonic()
    print(f"{msg} - Start")
    try:
        yield None
    finally:
        print(f"{msg} - Took {time.monotonic() - start:.1f}\n")


def logs_to_db(resultsPath, extra_fn=[]):
    start = time.monotonic()

    with time_it("parse files"):
        entries = parse_entries_files(resultsPath)

    with time_it("add scope"):
        add_scope(entries)

    for fn in extra_fn:
        fn(entries)

    with time_it("save"):
        dbPath = os.path.join(resultsPath, "results.db")

        with suppress(FileNotFoundError):
            os.remove(dbPath)

        conn = sqlite3.connect(dbPath)
        create_db(conn)
        cur = conn.cursor()

        extraColumns = set()
        for entry in entries:
            for c in entry.data:
                extraColumns.add(c)
        for c in extraColumns:
            add_column_to_table(cur, "logs", c)

        write(entries, cur, startDbId=0)

        conn.commit()

    print(f"The total execution took {time.monotonic() - start:.1f} seconds")
