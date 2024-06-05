# Description
Adds synthesis and degradation rules and parameters for all species in the model and iterates over them to set up the corresponding reactions.

# Code
```
from pysb import *
import pysb.bng
import pysb.examples.earm_1_0
Model(base=pysb.examples.earm_1_0.model)

pysb.bng.generate_equations(model)
all_species = list(model.species)
model.reset_equations()

def synthesize(name, species, ks):
    """Synthesize species with rate ks"""
    Rule(name, None >> species, ks)

def degrade(name, species, kdeg):
    """Degrade species with rate kdeg"""

# almost all degradation rates use this one value
kdeg_generic = 2.9e-6
# and these are the three exceptions
Parameter('kdeg_Mcl1', 0.0001)
Parameter('kdeg_AMito', 0.0001)
Parameter('kdeg_C3_U', 0)
# fraction by which synthesis rates should be scaled (to mimic the effects of
# treating HeLa cells wth 2.5 ug/ml of cycloheximide as per Table S2, Note 2)
syn_base = 0.15
# synthesis rates are all syn_base*kdeg*IC, except for L which is 0
Parameter('ks_L', 0)

# Even though the degradation of AMito is counted as a degradation reaction, it
# is different from the others in that the reactant species is not destroyed but
# rather converted to another species. So we have to declare this one
# explicitly.
Rule('AMito_deg', AMito(b=None) >> Mito(b=None), kdeg_AMito)

# loop over all species and create associated synthesis and degradation rates
# and reactions
for species in all_species:
    species_name = '_'.join(mp.monomer.name for mp in species.monomer_patterns)
    ks_name = 'ks_' + species_name
    kdeg_name = 'kdeg_' + species_name
    syn_rule_name = species_name + '_syn'
    deg_rule_name = species_name + '_deg'
    ic_name = species_name + '_0'
    ks = model.parameters.get(ks_name)
    kdeg = model.parameters.get(kdeg_name)
    syn_rule = model.rules.get(syn_rule_name)
    deg_rule = model.rules.get(deg_rule_name)
    ic = model.parameters.get(ic_name)
    if kdeg is None:
        kdeg = Parameter(kdeg_name, kdeg_generic)
    if ks is None:
        ks_value = 0
        if ic is not None:
            ks_value = syn_base * kdeg.value * ic.value
        ks = Parameter(ks_name, ks_value)
    if syn_rule is None:
        synthesize(syn_rule_name, species, ks)
    if deg_rule is None:

```
