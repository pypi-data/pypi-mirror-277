# Description
Demonstrates how to use the rule_firing_species method in the SpeciesPatternMatcher class to get species which match the reactants of rules in the model.

# Code
```
from pysb.examples import robertson
from pysb.bng import generate_equations
from pysb.pattern import SpeciesPatternMatcher

generate_equations(robertson.model)

        >>> from pysb.bng import generate_equations
        >>> model = robertson.model
        >>> generate_equations(model)
        >>> spm = SpeciesPatternMatcher(model)

        Get a list of species which fire each rule:

        >>> spm.rule_firing_species() \
                #doctest: +NORMALIZE_WHITESPACE
        OrderedDict([(Rule('A_to_B', A() >> B(), k1), [[A()]]),
         (Rule('BB_to_BC', B() + B() >> B() + C(), k2), [[B()], [B()]]),

```
