# Description
Usage examples of the SpeciesPatternMatcher class, including pattern matching using Monomer, MonomerPattern, and ComplexPattern.

# Code
```
from pysb.examples.earm_1_0 import model
from pysb.bng import generate_equations
from pysb.pattern import SpeciesPatternMatcher
from pysb import ANY, WILD, Model, Monomer, as_complex_pattern


    Create a PatternMatcher for the EARM 1.0 model

    >>> from pysb.examples.earm_1_0 import model
    >>> from pysb.bng import generate_equations
    >>> from pysb.pattern import SpeciesPatternMatcher
    >>> from pysb import ANY, WILD, Model, Monomer, as_complex_pattern
    >>> generate_equations(model)
    >>> spm = SpeciesPatternMatcher(model)

    Assign two monomers to variables (only needed when importing a model
    instead of defining one interactively)

    >>> Bax4 = model.monomers['Bax4']
    >>> Bcl2 = model.monomers['Bcl2']

    Search using a Monomer

    >>> spm.match(Bax4)
    [Bax4(b=None), Bax4(b=1) % Bcl2(b=1), Bax4(b=1) % Mito(b=1)]
    >>> spm.match(Bcl2) # doctest:+NORMALIZE_WHITESPACE
    [Bax2(b=1) % Bcl2(b=1),
    Bax4(b=1) % Bcl2(b=1),
    Bcl2(b=None),
    Bcl2(b=1) % MBax(b=1)]

    Search using a MonomerPattern (ANY and WILD keywords can be used)

    >>> spm.match(Bax4(b=WILD))
    [Bax4(b=None), Bax4(b=1) % Bcl2(b=1), Bax4(b=1) % Mito(b=1)]
    >>> spm.match(Bcl2(b=ANY))
    [Bax2(b=1) % Bcl2(b=1), Bax4(b=1) % Bcl2(b=1), Bcl2(b=1) % MBax(b=1)]

    Search using a ComplexPattern

    >>> spm.match(Bax4(b=1) % Bcl2(b=1))
    [Bax4(b=1) % Bcl2(b=1)]
    >>> spm.match(Bax4() % Bcl2())
    [Bax4(b=1) % Bcl2(b=1)]

    Contrived example to test a site with both a bond and state defined

    >>> model = Model(_export=False)
    >>> A = Monomer('A', ['a'], {'a': ['u', 'p']}, _export=False)
    >>> model.add_component(A)
    >>> species = [                                                     \
            A(a='u'),                                                   \
            A(a=1) % A(a=1),                                            \
            A(a=('u', 1)) % A(a=('u', 1)),                              \
            A(a=('p', 1)) % A(a=('p', 1))                               \
        ]
    >>> model.species = [as_complex_pattern(sp) for sp in species]
    >>> spm2 = SpeciesPatternMatcher(model)
    >>> spm2.match(A()) # doctest:+NORMALIZE_WHITESPACE
    [A(a='u'), A(a=1) % A(a=1), A(a=('u', 1)) % A(a=('u', 1)),
     A(a=('p', 1)) % A(a=('p', 1))]
    >>> spm2.match(A(a='u'))
    [A(a='u')]
    >>> spm2.match(A(a=('u', ANY)))
    [A(a=('u', 1)) % A(a=('u', 1))]
    >>> spm2.match(A(a=('u', WILD)))

```
