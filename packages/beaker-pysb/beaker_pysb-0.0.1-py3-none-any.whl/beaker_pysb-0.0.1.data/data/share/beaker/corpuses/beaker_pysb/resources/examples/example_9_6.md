# Description
Usage examples of the RulePatternMatcher class, including pattern matching using Monomer, MonomerPattern, ComplexPattern, and ReactionPattern.

# Code
```
from pysb.examples.earm_1_0 import model

    Create a PatternMatcher for the EARM 1.0 model

    >>> from pysb.examples.earm_1_0 import model
    >>> from pysb.pattern import RulePatternMatcher
    >>> rpm = RulePatternMatcher(model)

    Assign some monomers to variables (only needed when importing a model
    instead of defining one interactively)

    >>> AMito, mCytoC, mSmac, cSmac = [model.monomers[m] for m in \
        ('AMito', 'mCytoC', 'mSmac', 'cSmac')]

    Search using a Monomer

    >>> rpm.match_reactants(AMito) # doctest:+NORMALIZE_WHITESPACE
    [Rule('bind_mCytoC_AMito', AMito(b=None) + mCytoC(b=None) |
        AMito(b=1) % mCytoC(b=1), kf20, kr20),
    Rule('produce_ACytoC_via_AMito', AMito(b=1) % mCytoC(b=1) >>
        AMito(b=None) + ACytoC(b=None), kc20),
    Rule('bind_mSmac_AMito', AMito(b=None) + mSmac(b=None) |
        AMito(b=1) % mSmac(b=1), kf21, kr21),
    Rule('produce_ASmac_via_AMito', AMito(b=1) % mSmac(b=1) >>
        AMito(b=None) + ASmac(b=None), kc21)]

    >>> rpm.match_products(mSmac) # doctest:+NORMALIZE_WHITESPACE
    [Rule('bind_mSmac_AMito', AMito(b=None) + mSmac(b=None) |
        AMito(b=1) % mSmac(b=1), kf21, kr21)]

    Search using a MonomerPattern

    >>> rpm.match_reactants(AMito(b=1)) # doctest:+NORMALIZE_WHITESPACE
    [Rule('produce_ACytoC_via_AMito', AMito(b=1) % mCytoC(b=1) >>
        AMito(b=None) + ACytoC(b=None), kc20),
    Rule('produce_ASmac_via_AMito', AMito(b=1) % mSmac(b=1) >>
        AMito(b=None) + ASmac(b=None), kc21)]

    >>> rpm.match_rules(cSmac(b=1)) # doctest:+NORMALIZE_WHITESPACE
    [Rule('inhibit_cSmac_by_XIAP', cSmac(b=None) + XIAP(b=None) |
        cSmac(b=1) % XIAP(b=1), kf28, kr28)]

    Search using a ComplexPattern

    >>> rpm.match_reactants(AMito() % mSmac()) # doctest:+NORMALIZE_WHITESPACE
    [Rule('produce_ASmac_via_AMito', AMito(b=1) % mSmac(b=1) >>
        AMito(b=None) + ASmac(b=None), kc21)]

    >>> rpm.match_rules(AMito(b=1) % mCytoC(b=1)) \
        # doctest:+NORMALIZE_WHITESPACE
    [Rule('bind_mCytoC_AMito', AMito(b=None) + mCytoC(b=None) |
        AMito(b=1) % mCytoC(b=1), kf20, kr20),
    Rule('produce_ACytoC_via_AMito', AMito(b=1) % mCytoC(b=1) >>
        AMito(b=None) + ACytoC(b=None), kc20)]

    Search using a ReactionPattern

    >>> rpm.match_reactants(mCytoC() + mSmac())
    []

    >>> rpm.match_reactants(AMito() + mCytoC()) # doctest:+NORMALIZE_WHITESPACE
    [Rule('bind_mCytoC_AMito', AMito(b=None) + mCytoC(b=None) |

```
