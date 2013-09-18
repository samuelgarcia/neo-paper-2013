# encoding: utf-8
"""
This file drives an UML representation of NEO classes based on the file /neo/description.py

It requires graphviz, dot and pydot:
$ sudo apt-get install graphviz
$ pip install pydot
$ pip install pyparsing

Usage (at the moment inside neo folder):
$ python neo2dot.py | dot -Tsvg -o graph.svg
"""

import pydot
from neo import description

# initialize graph
graph = pydot.Dot( graph_type='digraph' ) # rankType='same'

# node list
nodes = {}
# creating a node for each neo class
for c in description.class_by_name: #sorted(
    # get necessary attrs in dot format
    if description.classes_necessary_attributes[c]:
        necessary_attrs = '\l'.join([i[0] for i in description.classes_necessary_attributes[c]])
    # get recommended attrs in dot format
    if description.classes_recommended_attributes[c]:
        recommended_attrs = '\l'.join([i[0] for i in description.classes_recommended_attributes[c]])
    # build record
    label = "{%s | %s | %s}" % (c, necessary_attrs+'\l', recommended_attrs+'\l')
    # create the node
    nodes[c] = pydot.Node( c, shape="Mrecord", label=label )
    #, style='filled', fillcolor='lightgrey' )
    # add the node to graph
    graph.add_node( nodes[c] )

# create one to many edges
# (many_to_one_relationship reverses the graph)
for c,rel in description.one_to_many_relationship.items(): 
    for r in rel:
        graph.add_edge( pydot.Edge( nodes[c], nodes[r], style='solid' ) ) # cyan

# create many to many edges
for c,rel in description.many_to_many_relationship.items():
    for r in rel:
        graph.add_edge( pydot.Edge( nodes[c], nodes[r], style='dashed', label='many to many' ) ) # magenta

# create property edges
for c,rel in description.property_relationship.items():
    for r in rel:
        graph.add_edge( pydot.Edge( nodes[c], nodes[r], style='dotted', label='property' ) ) # yellow

# write the graph
graph.write_svg('neo_graph.svg')
graph.write_png('neo_graph.png')
