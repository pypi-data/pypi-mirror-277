# Description
Test introspection functions to check if components are correctly tagged with the function names where they are defined.

# Code
```
copy
pysb.testing import *
pysb.core import *
functools import partial
nose.tools import assert_raises
operator

@with_model
def test_function_introspection():
    # Case 1: Component defined inside function
    Monomer('A')
    assert A._function == 'test_function_introspection'

    # Case 2: Component defined inside nested function
    def define_monomer_b():
        Monomer('B')
    define_monomer_b()
    assert B._function == 'define_monomer_b'

    # Case 3: Component defined by macro
    from pysb.macros import equilibrate
    equilibrate(A(), B(), [1, 1])

    assert model.rules['equilibrate_A_to_B']._function == 'equilibrate'

    # Case 4: Component defined by macro inside function
    def define_macro_inside_function():
        Monomer('C')
        equilibrate(A(), C(), [2, 2])
    define_macro_inside_function()

```
