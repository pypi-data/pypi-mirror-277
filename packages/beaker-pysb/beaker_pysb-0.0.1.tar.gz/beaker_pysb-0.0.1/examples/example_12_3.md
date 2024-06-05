# Description
Read a Graphviz DOT file and convert it to a NetworkX MultiGraph using pydot.

# Code
```
import networkx as nx

def read_dot(filename):
    """ Read a graphviz dot file using pydot

    Parameters
    ----------
    filename: str
        A DOT (graphviz) filename

    Returns
    -------
    MultiGraph
        A networkx MultiGraph file
    """
    try:
        import pydot
        pydot_graph = pydot.graph_from_dot_file(filename)[0]

```
