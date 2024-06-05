# Description
Creating a PySB logger adapter that prepends a model's name to log entries.

# Code
```
import logging

class PySBModelLoggerAdapter(logging.LoggerAdapter):
    """ A logging adapter to prepend a model's name to log entries """
    def process(self, msg, kwargs):

```
