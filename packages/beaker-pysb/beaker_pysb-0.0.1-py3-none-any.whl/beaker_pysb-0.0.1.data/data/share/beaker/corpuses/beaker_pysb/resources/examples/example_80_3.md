# Description
Example of running the CupSodaSimulator with default arguments while catching warnings.

# Code
```
import numpy as np
import warnings
from pysb.examples.tyson_oscillator import model

def test_arguments(self):
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', "Neither 'param_values' nor "
                                          "'initials' were supplied.")

```
