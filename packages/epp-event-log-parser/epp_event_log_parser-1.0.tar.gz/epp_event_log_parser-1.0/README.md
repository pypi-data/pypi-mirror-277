A library to parse .event files from Eggplant Performance test results.

```python
from epp_event_log_parser import EventLogReader
elr = EventLogReader(
    path=r'path to a .event file'
)

while elr.read(logEntry := EventLogEntry(), 0):
    print(logEntry.getShortText())

```