# Description
Rendering species from a PySB model into the 'dot' graph format and generating a PDF visualization using Graphviz tools.

# Code
```
import os
import re
import sys
try:
    import pygraphviz
except ImportError:
    pygraphviz = None
import pysb.bng
def run(model):
    pysb.bng.generate_equations(model)
    return render_species_as_dot(model.species, model.name)
def render_species_as_dot(species_list, graph_name=""):
    if pygraphviz is None:
        raise ImportError('pygraphviz library is required to run this function')
    graph = pygraphviz.AGraph(name="%s species" % graph_name, rankdir="LR", fontname='Arial')
    graph.edge_attr.update(fontname='Arial', fontsize=8)
    for si, cp in enumerate(species_list):
        sgraph_name = 'cluster_s%d' % si
        cp_label = re.sub(r'% ', '%<br align="left"/>', str(cp)) + '<br align="left"/>'
        sgraph_label = '<<font point-size="10" color="blue">s%d</font>' +
                       '<br align="left"/>' +
                       '<font face="Consolas" point-size="6">%s</font>>' % (si, cp_label)
        sgraph = graph.add_subgraph(name=sgraph_name, label=sgraph_label, color="gray75", sortv=sgraph_name)
        bonds = {}
        for mi, mp in enumerate(cp.monomer_patterns):
            monomer_node = '%s_%d' % (sgraph_name, mi)
            monomer_label = '<<table border="0" cellborder="1" cellspacing="0">'
            monomer_label += '<tr><td bgcolor="#a0ffa0"><b>%s</b></td></tr>' % mp.monomer.name
            for site in mp.monomer.sites:
                site_state = None
                cond = mp.site_conditions[site]
                if isinstance(cond, str):
                    site_state = cond
                elif isinstance(cond, tuple):
                    site_state = cond[0]
                site_label = site
                if site_state is not None:
                    site_label += '=<font color="purple">%s</font>' % site_state
                monomer_label += '<tr><td port="%s">%s</td></tr>' % (site, site_label)
            for site, value in mp.site_conditions.items():
                site_bonds = []  # list of bond numbers
                if isinstance(value, int):
                    site_bonds.append(value)
                elif isinstance(value, tuple):
                    site_bonds.append(value[1])
                elif isinstance(value, list):
                    site_bonds += value
                for b in site_bonds:
                    bonds.setdefault(b, []).append((monomer_node, site))
            monomer_label += '</table>>'
            sgraph.add_node(monomer_node, label=monomer_label, shape="none", fontname="Arial", fontsize=8)
        for bi, sites in bonds.items():
            node_names, port_names = list(zip(*sites))
            sgraph.add_edge(node_names, tailport=port_names[0], headport=port_names[1], label=str(bi))

Usage: ``python -m pysb.tools.render_species mymodel.py > mymodel.dot``

Renders the species from a model into the "dot" graph format which can be
visualized with Graphviz.

To create a PDF from the .dot file, use the Graphviz tools in the following
command pipeline::

    ccomps -x mymodel.dot | dot | gvpack -m0 | neato -n2 -T pdf -o mymodel.pdf

You can also change the "dot" command to "circo" or "sfdp" for a different type
of layout. Note that you can pipe the output of render_species straight into a
Graphviz command pipeline without creating an intermediate .dot file, which is
especially helpful if you are making continuous changes to the model and need to
visualize your changes repeatedly::

    python -m pysb.tools.render_species mymodel.py | ccomps -x | dot |
      gvpack -m0 | neato -n2 -T pdf -o mymodel.pdf

Note that some PDF viewers will auto-reload a changed PDF, so you may not even

```
