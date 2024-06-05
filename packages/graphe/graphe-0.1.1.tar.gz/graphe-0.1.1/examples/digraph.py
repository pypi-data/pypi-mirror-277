#!/usr/bin/env python3

from graphe.digraph import digraph
from graphe import draw

DG = digraph.Digraph('../data/tinyDG.txt')
print(DG.to_string())
print(DG.G)

fig = draw.Draw(digraph=True)
fig.node_attr(fontsize='8')
fig.draw(DG, [11, 12, 9, 11])
