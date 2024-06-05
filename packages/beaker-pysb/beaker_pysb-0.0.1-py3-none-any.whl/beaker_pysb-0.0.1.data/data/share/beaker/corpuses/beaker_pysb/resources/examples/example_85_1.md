# Description
Render the reactions produced by a model into the 'dot' graph format and include species as expression rates.

# Code
```
import pysb
import pysb.bng
import re
import sys
import os
try:
    import pygraphviz
except ImportError:
    pygraphviz = None

def run(model, include_rate_species=False):
    if pygraphviz is None:
        raise ImportError('pygraphviz library is required to run this function')
    pysb.bng.generate_equations(model)
    strict = True
    if include_rate_species:
        strict = False
    graph = pygraphviz.AGraph(directed=True, rankdir='LR', strict=strict)
    ic_species = [ic.pattern for ic in model.initials]
    for i, cp in enumerate(model.species):
        species_node = 's%d' % i
        slabel = re.sub(r'% ', r'%\\l', str(cp))
        slabel += '\\l'
        color = '#ccffcc'
        if len([s for s in ic_species if s.is_equivalent_to(cp)]):
            color = '#aaffff'
        graph.add_node(species_node,
                       label=slabel,
                       shape='Mrecord',
                       fillcolor=color, style='filled', color='transparent',
                       fontsize='12',
                       margin='0.06,0')
    for i, reaction in enumerate(model.reactions_bidirectional):
        reaction_node = 'r%d' % i
        graph.add_node(reaction_node,
                       label=reaction_node,
                       shape='circle',
                       fillcolor='lightgray', style='filled', color='transparent',
                       fontsize='12',
                       width='.3', height='.3', margin='0.06,0')
        reactants = set(reaction['reactants'])
        products = set(reaction['products'])
        modifiers = reactants & products
        reactants = reactants - modifiers
        products = products - modifiers
        attr_reversible = {'dir': 'both', 'arrowtail': 'empty'} if reaction['reversible'] else {}
        rule = model.rules.get(reaction['rule'][0])
        if include_rate_species:
            sps_forward = set()
            if isinstance(rule.rate_forward, pysb.core.Expression):
                sps_forward = sp_from_expression(rule.rate_forward)
                for s in sps_forward:
                    r_link(graph, s, i, **{'style': 'dashed'})
            if isinstance(rule.rate_reverse, pysb.core.Expression):
                sps_reverse = sp_from_expression(rule.rate_reverse)
                sps_reverse = sps_reverse - sps_forward
                for s in sps_reverse:
                    r_link(graph, s, i, **{'style': 'dashed'})
        for s in reactants:
            r_link(graph, s, i, **attr_reversible)
        for s in products:
            r_link(graph, s, i, _flip=True, **attr_reversible)
        for s in modifiers:
            r_link(graph, s, i, arrowhead='odiamond')
    return graph.string()

def r_link(graph, s, r, **attrs):
    nodes = ('s%d' % s, 'r%d' % r)
    if attrs.get('_flip'):
        del attrs['_flip']
        nodes = reversed(nodes)
    attrs.setdefault('arrowhead', 'normal')
    graph.add_edge(*nodes, **attrs)

def sp_from_expression(expression):
    expr_sps = []
    for a in expression.expr.atoms():
        if isinstance(a, pysb.core.Observable):
            sps = a.species
            expr_sps += sps


```
