# Description
Running a simulation of a given model using KaSim and returning the parsed results. The function handles various parameters such as time, points, flux maps, and perturbations, and it provides a deprecated notice recommending newer PySB simulation tools.

# Code
```
import pysb.pathfinder as pf
from pysb.generator.kappa import KappaGenerator
import os
import subprocess
import warnings
import numpy as np
tempfile
shutil
from collections import namedtuple
from pysb.util import read_dot
import pysb.logging


def run_simulation(model, time=10000, points=200, cleanup=True,
                   output_prefix=None, output_dir=None, flux_map=False,
                   perturbation=None, seed=None, verbose=False):
    """Runs the given model using KaSim and returns the parsed results.

    .. deprecated:: 1.10

    Use :func:`pysb.simulator.KappaSimulator` instead

    Parameters
    ----------
    model : pysb.core.Model
        The model to simulate/analyze using KaSim.
    time : number
        The amount of time (in arbitrary units) to run a simulation.
        Identical to the -u time -l argument when using KaSim at the command
        line.
        Default value is 10000. If set to 0, no simulation will be run.
    points : integer
        The number of data points to collect for plotting.
        Note that this is not identical to the -p argument of KaSim when
        called from the command line, which denotes plot period (time interval
        between points in plot).
        Default value is 200. Note that the number of points actually returned
        by the simulator will be points + 1 (including the 0 point).
    cleanup : boolean
        Specifies whether output files produced by KaSim should be deleted
        after execution is completed. Default value is True.
    output_prefix: str
        Prefix of the temporary directory name. Default is
        'tmpKappa_<model name>_'.
    output_dir : string
        The directory in which to create the temporary directory for
        the .ka and other output files. Defaults to the system temporary file
        directory (e.g. /tmp). If the specified directory does not exist,
        an Exception is thrown.
    flux_map: boolean
        Specifies whether or not to produce the flux map (generated over the
        full duration of the simulation). Default value is False.
    perturbation : string or None
        Optional perturbation language syntax to be appended to the Kappa file.
        See KaSim manual for more details. Default value is None (no
        perturbation).
    seed : integer
        A seed integer for KaSim random number generator. Set to None to
        allow KaSim to use a random seed (default) or supply a seed for
        deterministic behaviour (e.g. for testing)
    verbose : boolean
        Whether to pass the output of KaSim through to stdout/stderr.

    Returns
    -------
    If flux_map is False, returns the kasim simulation data as a Numpy ndarray.
    Data is accessed using the syntax::

            results[index_name]

    The index 'time' gives the time coordinates of the simulation. Data for the
    observables can be accessed by indexing the array with the names of the
    observables. Each entry in the ndarray has length points + 1, due to the
    inclusion of both the zero point and the final timepoint.

    If flux_map is True, returns an instance of SimulationResult, a namedtuple
    with two members, `timecourse` and `flux_map`. The `timecourse` field
    contains the simulation ndarray, and the `flux_map` field is an instance of
    a networkx MultiGraph containing the flux map. For details on viewing
    the flux map graphically see :func:`run_static_analysis` (notes section).
    """
    warnings.warn(
        'run_simulation will be removed in a future version of PySB. '
        'Use pysb.simulator.KappaSimulator instead.',
        DeprecationWarning
    )

    gen = KappaGenerator(model)

    if output_prefix is None:
        output_prefix = 'tmpKappa_%s_' % model.name

    base_directory = tempfile.mkdtemp(prefix=output_prefix, dir=output_dir)

    base_filename = os.path.join(base_directory, model.name)
    kappa_filename = base_filename + '.ka'
    fm_filename = base_filename + '_fm.dot'
    out_filename = base_filename + '.out'

    if points == 0:
        raise ValueError('The number of data points cannot be zero.')
    plot_period = (float(time) / points) if time > 0 else 1.0

    args = ['-i', kappa_filename, '-u', 'time', '-l', str(time),
            '-p', '%.5f' % plot_period, '-o', out_filename]

    if seed:
        args.extend(['-seed', str(seed)])

    # Generate the Kappa model code from the PySB model and write it to
    # the Kappa file:
    with open(kappa_filename, 'w') as kappa_file:
        file_data = gen.get_content()
        # If desired, add instructions to the kappa file to generate the
        # flux map:
        if flux_map:
            file_data += '%%mod: [true] do $DIN "%s" [true];\n' % fm_filename

        # If any perturbation language code has been passed in, add it to
        # the Kappa file:
        if perturbation:
            file_data += '\n%s\n' % perturbation

        logger.debug('Kappa file contents:\n\n' + file_data)
        kappa_file.write(file_data)

    # Run KaSim
    kasim_path = pf.get_path('kasim')
    p = subprocess.Popen([kasim_path] + args,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         cwd=base_directory)
    if verbose:
        for line in iter(p.stdout.readline, b''):
            print('@@', line, end='')
    (p_out, p_err) = p.communicate()

    if p.returncode:
        raise KasimInterfaceError(
            p_out.decode('utf8') + '\n' + p_err.decode('utf8'))

    # The simulation data, as a numpy array
    data = _parse_kasim_outfile(out_filename)

    if flux_map:
        try:
            flux_graph = read_dot(fm_filename)
        except ImportError:
            if cleanup:
                raise
            else:
                warnings.warn(
                        "The pydot library could not be "
                        "imported, so no MultiGraph "
                        "object returned (returning None); flux map "
                        "dot file available at %s" % fm_filename)
                flux_graph = None

    if cleanup:
        shutil.rmtree(base_directory)

    # If a flux map was generated, return both the simulation output and the
    # flux map as a networkx multigraph
    if flux_map:
        return SimulationResult(data, flux_graph)
    # If no flux map was requested, return only the simulation data
    else:

```
