import struct


class EventLogEntry:
    NULL_EVENT = 0
    CONNECT = 1
    END_ACTIVITY = 2
    ERROR = 3
    WARNING = 4
    TIMEOUT = 5
    START_TRANSACTION = 6
    END_TRANSACTION = 7
    SYNC = 8
    FAIL_TRANSACTION = 9
    EXIT = 10
    START = 11
    END = 12
    MESSAGE = 13
    START_ACTIVITY = 14
    PASS = 15
    FAIL = 16
    START_TIMING = 17
    END_TIMING = 18
    FAIL_TIMING = 19
    SUSPEND_TRANSACTION = 20
    RESUME_TRANSACTION = 21
    CURRENT_SCRIPT = 22
    METRIC = 23
    START_REQUEST = 24
    END_REQUEST = 25
    RECORD_TRANSACTION = 26
    #  Make sure that the following exceeds the highest event number by one
    MAX_TAG = 27

    dataSeparator = '\t'

    descriptions = [
        'None',
        'Connect',
        'End activity',
        'Error',
        'Warning',
        'Timeout',
        'Start transaction',
        'End transaction',
        'Sync',
        'Fail transaction',
        'Exit',
        'Start',
        'End',
        'Message',
        'Start activity',
        'Pass',
        'Fail',
        'Start timing',
        'End timing',
        'Fail timing',
        'Suspend transaction',
        'Resume transaction',
        'Current script',
        'Metric',
        'Start Request',
        'End Request',
        'Transaction',
    ]

    def getDescription(self):
        return EventLogEntry.descriptions[self.tag]

    def formatVUId(self, injector=None, engine=None, group=None, vu=0):
        return '%s.%s.%s.%04d' % (injector, engine, group, vu)

    def __init__(self):
        self.tag = EventLogEntry.NULL_EVENT
        self.time = -1
        self.id = ''
        self.info = ''

    def dumpData(self, injector=None, engine=None, group=None, vu=0):
        return (
            self.formatVUId(injector, engine, group, vu)
            + EventLogEntry.dataSeparator
            + str(self.time)
            + EventLogEntry.dataSeparator
            + self.getDescription()
            + EventLogEntry.dataSeparator
            + self.id
            + EventLogEntry.dataSeparator
            + self.info
        )

    def getText(self):
        return (
            self.formatVUId()
            + ', '
            + str(self.time)
            + EventLogEntry.dataSeparator
            + self.getDescription()
            + EventLogEntry.dataSeparator
            + self.id
            + EventLogEntry.dataSeparator
            + self.info
        )

    def getShortText(self):
        return self.getDescription() + EventLogEntry.dataSeparator + self.id + EventLogEntry.dataSeparator + self.info


class EventLogReader:
    A = 1
    B = 2

    def __init__(self, path=None):
        self.inError = 0
        self.processingWarnings = 0
        self.warnings = []
        self.errors = []
        self.path = path
        self.eventCount = 0
        if path is not None:
            self.open(path)
        else:
            self.file = None

    def open(self, path):
        self.file = open(path, 'rb')
        self.inError = 0
        self.processingWarnings = 0

        if struct.unpack('!H', self.file.read(2))[0] == 0xFF02:
            self.version = EventLogReader.B
        else:
            self.version = EventLogReader.A
            self.file.seek(0)

    def close(self):
        if self.file is not None:
            self.file.close()

    def printContents(self, out, vu):
        logEntry = EventLogEntry()
        while self.read(logEntry, 0):
            out.write(logEntry.getText())
            out.write('\n')
        if self.error():
            out.write('Error(s): ' + str(self.errors) + '\n')

    def error(self):
        return self.inError

    def getProcessingWarningsCount(self):
        return self.processingWarnings

    def getProcessingWarnings(self):
        return self.warnings

    def getProcessingErrors(self):
        return self.errors

    #  Return true if more to read
    def read(self, entry, timeOffset=0):
        self.eventCount += 1
        #  read and check tag
        s = self.file.read(1)
        if len(s) == 0:
            self.eof = 1
            return 0
        else:
            entry.tag = struct.unpack('b', s)[0]

        if entry.tag < EventLogEntry.NULL_EVENT or entry.tag >= EventLogEntry.MAX_TAG:
            self.inError = 1
            self.errors.append('invalid entry :: tag=' + str(entry.tag) + ' @ event:' + str(self.eventCount))
            return 0

        #  read and check time
        s = self.file.read(4)
        if len(s) < 4:
            self.eof = True
            return 0
        else:
            entry.time = struct.unpack('!I', s)[0]

        if entry.time < 0:
            self.inError = True
            self.errors.append('invalid time: ' + entry.time + ' @ event:' + self.eventCount)
        else:
            entry.time += timeOffset

        #  read and check id
        eid = []
        while 1:
            s = self.file.read(1)
            if len(s) == 0:
                self.eof = True
                return 0
            else:
                char = struct.unpack('c', s)[0]
            if char == b'\x00':
                break
            else:
                eid.append(char)

        eid = b''.join(eid).decode('ascii')

        entry.id = ''.join(eid)

        info = []
        while 1:
            s = self.file.read(1)
            if len(s) == 0:
                self.eof = True
                return 0
            else:
                char = struct.unpack('c', s)[0]
            if char == b'\x00':
                break
            else:
                info.append(char)

        entry.info = b''.join(info).decode('utf-8')

        if self.version == EventLogReader.B:
            struct.unpack('!I', self.file.read(4))[0]

        return 1
