#!/usr/local/bin/python3


from graphe.digraph import symboldigraph
from graphe.digraph import digraph
from graphe.digraph import cycle
from graphe.digraph import ddfo


class Topological:
    def __init__(self, G):
        assert isinstance(G, digraph.Digraph)
        self.G = G
        self.rank = [-1 for i in range(self.G.V)]

        cyc = cycle.DirectedCycle(self.G)
        if cyc.has_cycle():
            print('Topological sort not possible - graph has cycle')
            raise Exception('G has cycle')

        dfo = ddfo.DepthFirstOrder(self.G)
        self.order = dfo.get_reverse_post()

        for i, v in enumerate(self.order):
            self.rank[v] = i

    def get_order(self):
        return self.order


if __name__ == '__main__':

    SG = symboldigraph.SymbolDigraph('../../../data/jobs.txt', '/')

    TS = Topological(SG.DG)
    names = SG.node_names()
    for v in TS.get_order():
        print(f'{v} {names[v]}')
