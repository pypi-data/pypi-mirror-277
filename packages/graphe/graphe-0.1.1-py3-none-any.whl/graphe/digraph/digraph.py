#!/usr/local/bin/python3

import sys


class Digraph:
    def __init__(self, arg):
        self.E = 0
        if type(arg) is int:
            self.V = arg
            self.G = [[] for i in range(self.V)]
            return

        infile = arg  # assume string
        with open(infile) as f:
            self.V = int(f.readline())
            E = int(f.readline())
            self.G = [[] for i in range(self.V)]
            for line in f:
                From, To = line.strip().split()
                self.add_edge(int(From), int(To))
        assert self.E == E
        f.close()

    def add_edge(self, v, w):
        assert v < self.V
        assert w < self.V
        self.G[v].append(w)
        self.E += 1
        return

    def adj(self, v):
        assert v < self.V
        return self.G[v]

    def reverse(self):
        DG = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj(v):
                DG.add_edge(w, v)
        return DG

    def to_string(self):
        s = f'G: {self.V} vertices, {self.E} edges'
        return s
