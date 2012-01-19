#!/usr/bin/python3
try:
    import traceback
    import sys
    import csv

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)


class Database(object):

    def __init__(self, name):
        self.name = name

    def _getDialect(self, file):
        dialect = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)
        return dialect

    def _getReader(self, file, dialect):
        reader = csv.reader(file, dialect)
        return reader

    def _getWriter(self, file, dialect):
        writer = csv.writer(file, dialect)
        return writer

    def loadRecords(self):
        with open(self.name, "r", newline="") as file:
            reader = self._getReader(file, self._getDialect(file))
            return [row for row in reader]

    def saveRecords(self, records):
        with open(self.name, "r", newline="") as file:
            dialect = self._getDialect(file)

        with open(self.name, "w", newline="") as file:
            writer = self._getWriter(file, dialect)
            writer.writerows(records)

    def loadRecordByName(self, name):
        for record in self.loadRecords():
            if record[0] == name:
                return record
