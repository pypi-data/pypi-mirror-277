# Description
Configure the `pysb` logger to use the `DEBUG` level and disable console output to avoid duplication.

# Code
```
import logging

from pysb.logging import get_logger
import logging

# Nosetests adds its own logging handler - console_output=False avoids
# duplication

```
