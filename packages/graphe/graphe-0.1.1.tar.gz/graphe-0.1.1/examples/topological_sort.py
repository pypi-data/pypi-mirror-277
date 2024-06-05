#!/usr/local/bin/python3

from graphe.digraph import symboldigraph
from graphe.digraph import topological
from graphe import draw

SG = symboldigraph.SymbolDigraph('../data/jobs.txt', '/')
TS = topological.Topological(SG.DG)
names = SG.node_names()

print("Order of courses")
for i, v in enumerate(TS.get_order()):
    print(f'{i} {names[v]}')

fig = draw.Draw(digraph=True)
fig.set_names(G.keys)
fig.node_attr(width='0.3', height='0.3', shape='', style='',
              color='gray', fontcolor='black', fontsize='4')
fig.draw(G.graph())
