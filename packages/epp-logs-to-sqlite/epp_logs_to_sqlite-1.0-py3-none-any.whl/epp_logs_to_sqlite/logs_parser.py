import os
import datetime
from glob import glob
import re
from epp_event_log_parser import EventLogReader, EventLogEntry


class EventLogEntryExtraData(EventLogEntry):
    def __init__(self):
        super().__init__()
        self.data = {}

    def addFileld(self, name, value):
        self.data[name] = value


class EventLogEntryNode(EventLogEntryExtraData):
    def __init__(self):
        super().__init__()
        self._parent = None
        self.children = []

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def addChild(self, child):
        self.children.append(child)
        child.parent = self


def create_db(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE logs (
            id number NOT NULL,
            time text NOT NULL,
            description text NOT NULL,
            logId text NULL,
            info text NULL,
            groupName text NOT NULL,
            groupUserId number NOT NULL,
            timeSeconds number NOT NULL

        );"""
    )

    cursor.execute("""CREATE UNIQUE INDEX idx_logs ON logs (id);""")


def add_column_to_table(cursor, table, columName):
    cursor.execute(f"ALTER TABLE {table} ADD COLUMN {columName} text NULL;")


def insert_rows(cursor, table, columns, values):
    cursor.execute(
        "insert into {} ({}) values ({})".format(
            table, ", ".join(columns), ", ".join("?" for c in columns)
        ),
        tuple(values),
    )


def write(logEntries, cursor, startDbId=1):
    rowsNames = (
        "id time description logId info groupName groupUserId timeSeconds".split(" ")
    )
    for idx, logEntry in enumerate(logEntries):
        rowsValues = [
            startDbId + idx,
            str(logEntry.time),
            logEntry.getDescription(),
            logEntry.id,
            logEntry.info,
            logEntry.groupName,
            logEntry.groupUserId,
            logEntry.time.total_seconds(),
        ]

        extra = [(k, v) for k, v in logEntry.data.items()]

        insert_rows(
            cursor,
            "logs",
            rowsNames + [e[0] for e in extra],
            rowsValues + [e[1] for e in extra],
        )


openTags = {
    EventLogEntry.START,
    EventLogEntry.START_ACTIVITY,
    EventLogEntry.CURRENT_SCRIPT,
    EventLogEntry.START_TRANSACTION,
}

closeTags = {
    EventLogEntry.END,
    EventLogEntry.END_ACTIVITY,
    EventLogEntry.END_TRANSACTION,
    EventLogEntry.FAIL_TRANSACTION,
}


def add_scope(logEntries):
    currentUser = None
    currentParent = None

    for logEntry in logEntries:
        if currentUser != (logEntry.groupName, logEntry.groupUserId):
            currentUser = (logEntry.groupName, logEntry.groupUserId)
            currentParent = logEntry
        else:
            while (
                logEntry.tag == EventLogEntry.CURRENT_SCRIPT
                and currentParent.tag != EventLogEntry.START_ACTIVITY
            ):
                currentParent = currentParent.parent

            currentParent.addChild(logEntry)

            if logEntry.tag in openTags:
                currentParent = logEntry
            elif logEntry.tag in closeTags:
                currentParent = currentParent.parent

    return logEntries


def parse_entries_file(fpath: str) -> list[EventLogEntryNode]:
    groupName = fpath.split("\\")[-2]
    groupUserId = fpath.split("\\")[-1].replace(".event", "")

    events = []
    elr = EventLogReader(fpath)
    while elr.read(logEntry := EventLogEntryNode(), 0):
        logEntry.time = datetime.timedelta(milliseconds=logEntry.time)
        logEntry.groupName = groupName
        logEntry.groupUserId = groupUserId
        events.append(logEntry)

    return events


def parse_entries_files(dirpath):
    entries = []

    def group_info(fpath):
        group, userId = fpath.split("\\")[-2:]
        return group, int(userId.replace(".event", ""))

    files = sorted(
        glob(os.path.join(dirpath, r"**\*.event"), recursive=True), key=group_info
    )
    tfiles = len(files)

    for i, fpath in enumerate(files):
        group, userId = group_info(fpath)
        print(f"{userId} of {group} ({i + 1}/{tfiles})")
        entries.extend(parse_entries_file(fpath))

    return entries


def parse_value(logEntries, fieldName, infoRegexp, tag=None, logId=None):
    def entryFilter(entry):
        if tag is not None and entry.tag != tag:
            return False
        if logId is not None and entry.id != logId:
            return False
        return True

    for logEntry in filter(entryFilter, logEntries):
        if m := re.search(infoRegexp, logEntry.dumpData(), re.DOTALL | re.MULTILINE):
            logEntry.addFileld(fieldName, m.group(1))
