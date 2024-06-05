# Description
Defines the `show_rates` function which prints a table of rate parameters including forward, reverse, and catalytic rates (similar to supporting text S3, Table S4 from Gaudet et al).

# Code
```
from pysb import *
import pysb.bng
import pysb.examples.earm_1_0
Model(base=pysb.examples.earm_1_0.model)

pysb.bng.generate_equations(model)
all_species = list(model.species)

def show_rates():
    """Print a table of rate parameters like Table S4"""
    # FIXME kf14-kf21 need to be un-scaled by v to make the table look right
    print(("%-20s        " * 3) % ('forward', 'reverse', 'catalytic'))
    print('-' * (9 + 11 + 7) * 3)
    for i in list(range(1,29)) + [31]:
        for t in ('f', 'r', 'c'):
            n = 'k%s%d' % (t,i)
            p = model.parameters.get(n)
            if p is not None:
                print("%-9s%11g       " % (p.name, p.value), end=' ')

```
