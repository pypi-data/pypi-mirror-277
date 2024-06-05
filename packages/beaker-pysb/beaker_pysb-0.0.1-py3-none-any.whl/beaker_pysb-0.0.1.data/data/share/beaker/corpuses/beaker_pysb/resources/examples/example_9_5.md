# Description
Demonstrates how to use the species_fired_by_reactant_pattern method in the SpeciesPatternMatcher class to get a list of species matching a reactant pattern.

# Code
```
from pysb.examples import bax_pore
from pysb.bng import generate_equations
from pysb.pattern import SpeciesPatternMatcher

generate_equations(bax_pore.model)

        >>> from pysb.examples import bax_pore
        >>> from pysb.bng import generate_equations
        >>> model = bax_pore.model
        >>> generate_equations(model)
        >>> spm = SpeciesPatternMatcher(model)

        Get a list of species which fire each rule:

        >>> rxn_pat = model.rules['bax_dim'].reactant_pattern
        >>> print(rxn_pat)
        BAX(t1=None, t2=None) + BAX(t1=None, t2=None)

        >>> spm.species_fired_by_reactant_pattern(rxn_pat) \
                #doctest: +NORMALIZE_WHITESPACE
        [[BAX(t1=None, t2=None, inh=None),
          BAX(t1=None, t2=None, inh=1) % MCL1(b=1)],
         [BAX(t1=None, t2=None, inh=None),

```
