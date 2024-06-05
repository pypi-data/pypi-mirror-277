# Description
Defines the `show_species` function which prints the table of species including their initial values, synthesis rates, and degradation rates (similar to supporting text S3, Table S2 from Gaudet et al).

# Code
```
from pysb import *
import pysb.bng
import pysb.examples.earm_1_0
Model(base=pysb.examples.earm_1_0.model)

pysb.bng.generate_equations(model)
all_species = list(model.species)

def show_species():
    """Print a table of species like Table S2"""
    print('   | %-12s %8s %20s %10s' %
          ('species', 'initial', 'synth rate', 'deg rate'))
    print('-' * (5 + 12 + 1 + 8 + 1 + 20 + 1 + 10))
    for i, species in enumerate(all_species, 1):
        mp_names = [mp.monomer.name for mp in species.monomer_patterns]
        name = '_'.join(mp_names)
        display_name = ':'.join(mp_names)
        ks = model.parameters.get('ks_' + name)
        kdeg = model.parameters.get('kdeg_' + name)
        ic = model.parameters.get(name + '_0')
        if ic is not None:
            ic_value = ic.value
        else:
            ic_value = 0
        if ks.value != 0 and kdeg.value != 0:
            ic_calc = round(ks.value/kdeg.value/syn_base)
            ks_expr = '%4.2f*kdeg*%7d' % (syn_base, ic_calc)
        else:
            ks_expr = '0'
        values = (i, display_name, ic_value, ks_expr, kdeg.value)

```
