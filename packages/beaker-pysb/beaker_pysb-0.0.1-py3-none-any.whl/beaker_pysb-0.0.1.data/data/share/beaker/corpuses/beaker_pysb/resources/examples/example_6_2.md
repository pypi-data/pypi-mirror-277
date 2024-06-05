# Description
Running static analysis using KaSa to generate contact and influence maps of a model. It provides options to clean up generated files and output verbose logs.

# Code
```
import pysb.pathfinder as pf
from pysb.generator.kappa import KappaGenerator
import os
import subprocess
import tempfile
shutil
import warnings
from collections import namedtuple
from pysb.util import read_dot
import pysb.logging

logger = pysb.logging.get_logger(__name__)


def run_static_analysis(model, influence_map=False, contact_map=False,
                        cleanup=True, output_prefix=None, output_dir=None,
                        verbose=False):
    """Run static analysis (KaSa) on to get the contact and influence maps.

    If neither influence_map nor contact_map are set to True, then a ValueError
    is raised.

    Parameters
    ----------
    model : pysb.core.Model
        The model to simulate/analyze using KaSa.
    influence_map : boolean
        Whether to compute the influence map.
    contact_map : boolean
        Whether to compute the contact map.
    cleanup : boolean
        Specifies whether output files produced by KaSa should be deleted
        after execution is completed. Default value is True.
    output_prefix: str
        Prefix of the temporary directory name. Default is
        'tmpKappa_<model name>_'.
    output_dir : string
        The directory in which to create the temporary directory for
        the .ka and other output files. Defaults to the system temporary file
        directory (e.g. /tmp). If the specified directory does not exist,
        an Exception is thrown.
    verbose : boolean
        Whether to pass the output of KaSa through to stdout/stderr.

    Returns
    -------
    StaticAnalysisResult, a namedtuple with two fields, `contact_map` and
    `influence_map`, each containing the respective result as an instance
    of a networkx MultiGraph. If the either the contact_map or influence_map
    argument to the function is False, the corresponding entry in the
    StaticAnalysisResult returned by the function will be None.

    Notes
    -----
    To view a networkx file graphically, use `draw_network`::

        import networkx as nx
        nx.draw_networkx(g, with_labels=True)

    You can use `graphviz_layout` to use graphviz for layout (requires pydot
    library)::

        import networkx as nx
        pos = nx.drawing.nx_pydot.graphviz_layout(g, prog='dot')
        nx.draw_networkx(g, pos, with_labels=True)

    For further information, see the networkx documentation on visualization:
    https://networkx.github.io/documentation/latest/reference/drawing.html
    """

    # Make sure the user has asked for an output!
    if not influence_map and not contact_map:
        raise ValueError('Either contact_map or influence_map (or both) must '
                         'be set to True in order to perform static analysis.')

    gen = KappaGenerator(model, _warn_no_ic=False)

    if output_prefix is None:
        output_prefix = 'tmpKappa_%s_' % model.name

    base_directory = tempfile.mkdtemp(prefix=output_prefix, dir=output_dir)

    base_filename = os.path.join(base_directory, str(model.name))
    kappa_filename = base_filename + '.ka'
    im_filename = base_filename + '_im.dot'
    cm_filename = base_filename + '_cm.dot'

    # NOTE: in the args passed to KaSa, the directory for the .dot files is
    # specified by the --output_directory option, and the output_contact_map
    # and output_influence_map should only be the base filenames (without
    # a directory prefix).
    # Contact map args:
    if contact_map:
        cm_args = ['--compute-contact-map', '--output-contact-map',
                   os.path.basename(cm_filename),
                   '--output-contact-map-directory', base_directory]
    else:
        cm_args = ['--no-compute-contact-map']
    # Influence map args:
    if influence_map:
        im_args = ['--compute-influence-map', '--output-influence-map',
                   os.path.basename(im_filename),
                   '--output-influence-map-directory', base_directory]
    else:
        im_args = ['--no-compute-influence-map']
    # Full arg list
    args = [kappa_filename] + cm_args + im_args

    # Generate the Kappa model code from the PySB model and write it to
    # the Kappa file:
    with open(kappa_filename, 'w') as kappa_file:
        file_data = gen.get_content()
        logger.debug('Kappa file contents:\n\n' + file_data)
        kappa_file.write(file_data)

    # Run KaSa using the given args
    kasa_path = pf.get_path('kasa')
    p = subprocess.Popen([kasa_path] + args,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         cwd=base_directory)
    if verbose:
        for line in iter(p.stdout.readline, b''):
            print('@@', line, end='')
    (p_out, p_err) = p.communicate()

    if p.returncode:
        raise KasaInterfaceError(
            p_out.decode('utf8') + '\n' + p_err.decode('utf8'))

    # Try to create the graphviz objects from the .dot files created
    try:
        # Convert the contact map to a Graph
        cmap = read_dot(cm_filename) if contact_map else None
        imap = read_dot(im_filename) if influence_map else None
    except ImportError:
        if cleanup:
            raise
        else:
            warnings.warn(
                    "The pydot library could not be "
                    "imported, so no MultiGraph "
                    "object returned (returning None); "
                    "contact/influence maps available at %s" %
                    base_directory)
            cmap = None
            imap = None

    # Clean up the temp directory if desired
    if cleanup:
        shutil.rmtree(base_directory)


```
