# Description
Test saving and loading of SimulationResult

# Code
```
pysb.simulator import ScipyOdeSimulator, BngSimulator
pysb.simulator.base import SimulationResult
numpy as np
tempfile
copy
warnings
pysb.examples import tyson_oscillator, robertson, expression_observables

def test_save_load():
    tspan = np.linspace(0, 100, 101)
    # Make a copy of model so other tests etc. don't see the changed name.
    model = copy.deepcopy(tyson_oscillator.model)
    test_unicode_name = u'Hello \u2603 and \U0001f4a9!'
    model.name = test_unicode_name
    sim = ScipyOdeSimulator(model, integrator='lsoda')
    simres = sim.run(tspan=tspan, param_values={'k6': 1.0})

    sim_rob = ScipyOdeSimulator(robertson.model, integrator='lsoda')
    simres_rob = sim_rob.run(tspan=tspan)

    # Reset equations from any previous network generation
    robertson.model.reset_equations()
    A = robertson.model.monomers['A']

    # NFsim without expressions
    nfsim1 = BngSimulator(robertson.model)
    nfres1 = nfsim1.run(n_runs=2, method='nf', tspan=np.linspace(0, 1))
    # Test attribute saving (text, float, list)
    nfres1.custom_attrs['note'] = 'NFsim without expressions'
    nfres1.custom_attrs['pi'] = 3.14
    nfres1.custom_attrs['some_list'] = [1, 2, 3]

    # NFsim with expressions
    nfsim2 = BngSimulator(expression_observables.model)
    nfres2 = nfsim2.run(n_runs=1, method='nf', tspan=np.linspace(0, 100, 11))

    with tempfile.NamedTemporaryFile() as tf:
        # Cannot have two file handles on Windows
        tf.close()

        simres.save(tf.name, dataset_name='test', append=True)

        # Try to reload when file contains only one dataset and group
        SimulationResult.load(tf.name)

        simres.save(tf.name, append=True)

        # Trying to overwrite an existing dataset gives a ValueError
        assert_raises(ValueError, simres.save, tf.name, append=True)

        # Trying to write to an existing file without append gives an IOError
        assert_raises(IOError, simres.save, tf.name)

        # Trying to write a SimulationResult to the same group with a
        # different model name results in a ValueError
        assert_raises(ValueError, simres_rob.save, tf.name,
                      dataset_name='robertson', group_name=model.name,
                      append=True)

        simres_rob.save(tf.name, append=True)

        # Trying to load from a file with more than one group without
        # specifying group_name should raise a ValueError
        assert_raises(ValueError, SimulationResult.load, tf.name)

        # Trying to load from a group with more than one dataset without
        # specifying a dataset_name should raise a ValueError
        assert_raises(ValueError, SimulationResult.load, tf.name,
                      group_name=model.name)

        # Load should succeed when specifying group_name and dataset_name
        simres_load = SimulationResult.load(tf.name, group_name=model.name,
                                            dataset_name='test')
        assert simres_load._model.name == test_unicode_name

        # Saving network free results requires include_obs_exprs=True,
        # otherwise a warning should be raised
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always", UserWarning)
            nfres1.save(tf.name, dataset_name='nfsim_no_obs', append=True)
            assert len(w) == 1

        nfres1.save(tf.name, include_obs_exprs=True,
                    dataset_name='nfsim test', append=True)

        # NFsim load
        nfres1_load = SimulationResult.load(tf.name,
                                            group_name=nfres1._model.name,
                                            dataset_name='nfsim test')

        # NFsim with expression
        nfres2.save(tf.name, include_obs_exprs=True, append=True)
        nfres2_load = SimulationResult.load(tf.name,
                                            group_name=nfres2._model.name)

    _check_resultsets_equal(simres, simres_load)
    _check_resultsets_equal(nfres1, nfres1_load)

```
