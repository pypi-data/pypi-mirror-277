#!/usr/local/bin/python3

import sys
from graphe.digraph import digraph
from graphe.digraph import digraphdfs
from graphe import draw

DG = digraph.Digraph('../data/mediumG.txt')
print(DG.to_string())

dfs = digraphdfs.DirectedDFSearch(DG, 0)
for i in range(1, 200):
    if dfs.has_path_to(i):
        print(f'0 has path to {i}')
dfpath = dfs.path_to(197)

fig = draw.Draw(digraph=True)
fig.node_attr(label='')
fig.edge_attr(color='gray', arrowsize='0.2', penwidth='0.75')
fig.draw(DG, dfpath)
