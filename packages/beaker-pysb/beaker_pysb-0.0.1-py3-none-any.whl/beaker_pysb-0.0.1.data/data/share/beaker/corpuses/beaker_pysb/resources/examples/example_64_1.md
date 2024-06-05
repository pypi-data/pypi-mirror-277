# Description
Example of creating and using a test suite to check properties of a PySB model.

# Code
```
import pysb
from pysb.core import SelfExporter
from pysb.pattern import SpeciesPatternMatcher, ReactionPatternMatcher, \
    RulePatternMatcher
from pysb.testing.modeltests import TestSuite, SpeciesExists, SpeciesDoesNotExist
from pysb.bng import generate_equations

    >>> from pysb.testing.modeltests import TestSuite, SpeciesExists, \
        SpeciesDoesNotExist
    >>> from pysb.bng import generate_equations
    >>> from pysb.examples.earm_1_0 import model
    >>> ts = TestSuite(model)

    Create variables for model components (not needed for models defined
    interactively):

    >>> AMito, mCytoC, mSmac, cSmac, L, CPARP = [model.monomers[m] for m in \
                                       ('AMito', 'mCytoC', 'mSmac', 'cSmac', \
                                        'L', 'CPARP')]

    Add some assertions:

    Check that AMito(b=1) % mSmac(b=1) exists in the species graph (note this
    doesn't guarantee the species will actually be producted/consumed/change
    in concentration; that depends on the rate constants):

    >>> ts.add(SpeciesExists(AMito(b=1) % mSmac(b=1)))

    This is the opposite check, that the complex above doesn't exist,
    which should of course fail:

    >>> ts.add(SpeciesDoesNotExist(AMito(b=1) % mSmac(b=1)))

    We can also specify that species matching a pattern should never exist
    in a model. For example, we shouldn't ever be producing unbound
    ligand in the EARM 1.0 model:

    >>> ts.add(SpeciesNeverProduct(L(b=None)))

    We could also have used SpeciesOnlyReactant. The difference is the
    latter checks for an appearance as a reactant, whereas
    SpeciesNeverProduct would pass whether the species appeared as a
    reactant or not.

    >>> ts.add(SpeciesOnlyReactant(L(b=None)))

    CPARP is an output in this model, so it should appear as a product but
    never as a reactant:

    >>> ts.add(SpeciesOnlyProduct(CPARP()))

    When we're ready, we can generate the reactions and check the assertions:

    >>> generate_equations(model)
    >>> ts.check_all()  # doctest:+ELLIPSIS
    SpeciesExists(AMito() % mSmac())...OK...
    SpeciesDoesNotExist(AMito() % mSmac())...FAIL...
      [AMito(b=1) % mSmac(b=1)]...
    SpeciesExists(AMito(b=1) % mCytoC(b=1))...OK...
    SpeciesNeverProduct(L(b=None))...OK...
    SpeciesOnlyProduct(CPARP())...OK...

    We can also execute any test immediately without adding it to the test
    suite (note that some tests require a reaction network to be generated):

    >>> ts.check(SpeciesExists(L(b=None)))

```
