# Description
Testing the rules_using_parameter() function from pysb.util to find rules that use a specific parameter.

# Code
```
pysb.core import Initial, Monomer, Parameter, Rule
pysb.util import rules_using_parameter

@with_model
def test_rules_using_parameter():
    """
    Tests for rules_using_parameter() in pysb.util
    """
    Monomer('m1')
    Monomer('m2')
    Monomer('m3')

    ka1 = Parameter('ka1', 2e-5)
    keff = Parameter('keff', 1e5)

    Initial(m2(), Parameter('m2_0', 10000))

    Rule('R1', None >> m1(), ka1)
    Rule('R2', m1() + m2() >> m1() + m3(), keff)

    components = rules_using_parameter(model, 'keff')
    assert R2 in components

    # Get rules by supplying Parameter object directly
    components = rules_using_parameter(model, keff)

```
