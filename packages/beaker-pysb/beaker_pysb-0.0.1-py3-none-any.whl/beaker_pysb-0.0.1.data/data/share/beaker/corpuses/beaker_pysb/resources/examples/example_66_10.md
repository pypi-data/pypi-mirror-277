# Description
Test NFSim with total rate enabled for a rule in the `pysb` library.

# Code
```
from pysb import *

@with_model
def test_nfsim_total_rate():
    Monomer('A', ['a'])
    Monomer('B', ['b'])

    Parameter('ksynthA', 100)
    Parameter('ksynthB', 100)
    Parameter('kbindAB', 10)

    Parameter('A_init', 20)
    Parameter('B_init', 30)

    Initial(A(a=None), A_init)
    Initial(B(b=None), B_init)

    Observable("A_free", A(a=None))
    Observable("B_free", B(b=None))
    Observable("AB_complex", A(a=1) % B(b=1))

    Rule('A_synth', None >> A(a=None), ksynthA)
    Rule('B_synth', None >> B(b=None), ksynthB)
    Rule('AB_bind', A(a=None) + B(b=None) >> A(a=1) % B(b=1), kbindAB)

    with BngFileInterface(model) as bng:
        bng.action('simulate', method='nf', t_end=1000, n_steps=100)
        bng.execute()
        res = bng.read_simulation_results()
        assert res.dtype.names == ('time', 'A_free', 'B_free', 'AB_complex')
        no_total_rate_ab_complex = res['AB_complex'][-1]

    # Set total rate of last AB_bind reaction to be constant and independent
    # of A and B concentration. In this case, the number of AB complex molecules
    # should be less than the non total rate case.
    model.rules[-1].total_rate = True

    # check that generate network does not fail when total rate is set to be true
    # generate_network just ignores this setting
    ok_(generate_network(model))

    with BngFileInterface(model) as bng:
        bng.action('simulate', method='nf', t_end=1000, n_steps=100)
        bng.execute()
        res = bng.read_simulation_results()
        assert res.dtype.names == ('time', 'A_free', 'B_free', 'AB_complex')
        total_rate_ab_complex = res['AB_complex'][-1]


```
