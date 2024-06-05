#!/usr/local/bin/python3

import sys
from graphe.graph import graph
from graphe.graph import cc
from graphe import draw

infile = "../data/mediumGCut.txt"

G = graph.Graph(infile)

mycc = cc.CC(G)

res = mycc.ccomps()

print(f'Connected components: {len(res)}')
print(f'{res}')

names = [str(x) for x in range(G.V)]
fig = draw.Draw()
fig.set_names(names)
#fig.node_attr(label='')
fig.draw(G)
