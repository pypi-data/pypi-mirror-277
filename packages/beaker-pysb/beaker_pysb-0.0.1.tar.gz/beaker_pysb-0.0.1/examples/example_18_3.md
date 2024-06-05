# Description
Changes the rate constants of different reactions in the `EARM 1.3` model.

# Code
```
from pysb import *
import pysb.bng
import pysb.examples.earm_1_0

kr1.value = 1e-6
kc1.value = 1e-2
kf3.value = 1e-7
kf6.value = 1e-7
kf7.value = 1e-7
kr9.value = 0.001
kc9.value = 20
kr13.value = 1
kf14.value = 1e-6 / v
kf15.value = 1e-6 * 2 / v
kf16.value = 1e-6 / v
kf17.value = 1e-6 * 2 / v
kf18.value = 1e-6 / v
kf19.value = 1e-6 / v
kf20.value = 2e-6 / v
kf21.value = 2e-6 / v
kf22.value = 1

```
