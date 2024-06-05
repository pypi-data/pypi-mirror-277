# Description
Changes the initial condition values of various components in the model.

# Code
```
from pysb import *
import pysb.bng
import pysb.examples.earm_1_0

pR_0.value = 1000
flip_0.value = 2000
pC8_0.value = 10000
Bid_0.value = 60000
Bax_0.value = 80000

```
