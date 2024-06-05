# Description
Usage examples of the ReactionPatternMatcher class, including pattern matching using Monomer, MonomerPattern, and ComplexPattern.

# Code
```
from pysb.examples.earm_1_0 import model
from pysb.bng import generate_equations
from pysb.pattern import ReactionPatternMatcher


    Create a PatternMatcher for the EARM 1.0 model

    >>> from pysb.examples.earm_1_0 import model
    >>> from pysb.bng import generate_equations
    >>> from pysb.pattern import ReactionPatternMatcher
    >>> generate_equations(model)
    >>> rpm = ReactionPatternMatcher(model)

    Assign some monomers to variables (only needed when importing a model
    instead of defining one interactively)

    >>> AMito, mCytoC, mSmac, cSmac = [model.monomers[m] for m in \
                                       ('AMito', 'mCytoC', 'mSmac', 'cSmac')]

    Search using a Monomer

    >>> rpm.match_products(mSmac) # doctest:+NORMALIZE_WHITESPACE
    [Rxn (reversible):
        Reactants: {'__s15': mSmac(b=None), '__s45': AMito(b=None)}
        Products: {'__s47': AMito(b=1) % mSmac(b=1)}
        Rate: kf21*__s15*__s45 - kr21*__s47
        Rules: [Rule('bind_mSmac_AMito', AMito(b=None) + mSmac(b=None) |
                AMito(b=1) % mSmac(b=1), kf21, kr21)]]

    Search using a MonomerPattern

    >>> rpm.match_reactants(AMito(b=ANY)) # doctest:+NORMALIZE_WHITESPACE
    [Rxn (one-way):
        Reactants: {'__s46': AMito(b=1) % mCytoC(b=1)}
        Products: {'__s45': AMito(b=None), '__s48': ACytoC(b=None)}
        Rate: kc20*__s46
        Rules: [Rule('produce_ACytoC_via_AMito', AMito(b=1) % mCytoC(b=1) >>
                AMito(b=None) + ACytoC(b=None), kc20)],
     Rxn (one-way):
        Reactants: {'__s47': AMito(b=1) % mSmac(b=1)}
        Products: {'__s45': AMito(b=None), '__s49': ASmac(b=None)}
        Rate: kc21*__s47
        Rules: [Rule('produce_ASmac_via_AMito', AMito(b=1) % mSmac(b=1) >>
                AMito(b=None) + ASmac(b=None), kc21)]]

    >>> rpm.match_products(cSmac(b=ANY)) # doctest:+NORMALIZE_WHITESPACE
    [Rxn (reversible):
        Reactants: {'__s7': XIAP(b=None), '__s51': cSmac(b=None)}
        Products: {'__s53': XIAP(b=1) % cSmac(b=1)}
        Rate: kf28*__s51*__s7 - kr28*__s53
        Rules: [Rule('inhibit_cSmac_by_XIAP', cSmac(b=None) + XIAP(b=None) |
                cSmac(b=1) % XIAP(b=1), kf28, kr28)]]

    Search using a ComplexPattern

    >>> rpm.match_reactants(AMito() % mSmac()) # doctest:+NORMALIZE_WHITESPACE
    [Rxn (one-way):
        Reactants: {'__s47': AMito(b=1) % mSmac(b=1)}
        Products: {'__s45': AMito(b=None), '__s49': ASmac(b=None)}
        Rate: kc21*__s47
        Rules: [Rule('produce_ASmac_via_AMito', AMito(b=1) % mSmac(b=1) >>
                AMito(b=None) + ASmac(b=None), kc21)]]

    >>> rpm.match_reactions(AMito(b=3) % mCytoC(b=3)) \
    # doctest:+NORMALIZE_WHITESPACE
    [Rxn (reversible):
        Reactants: {'__s14': mCytoC(b=None), '__s45': AMito(b=None)}
        Products: {'__s46': AMito(b=1) % mCytoC(b=1)}
        Rate: kf20*__s14*__s45 - kr20*__s46
        Rules: [Rule('bind_mCytoC_AMito', AMito(b=None) + mCytoC(b=None) |
                AMito(b=1) % mCytoC(b=1), kf20, kr20)],
     Rxn (one-way):
        Reactants: {'__s46': AMito(b=1) % mCytoC(b=1)}
        Products: {'__s45': AMito(b=None), '__s48': ACytoC(b=None)}
        Rate: kc20*__s46
        Rules: [Rule('produce_ACytoC_via_AMito', AMito(b=1) % mCytoC(b=1) >>

```
