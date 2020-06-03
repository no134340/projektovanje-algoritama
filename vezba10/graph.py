from enum import Enum
from math import inf
import heapq


class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255


class Vertex:

    def __init__(self, name, color=VertexColor.WHITE, pred=None, d=None):
        self.name = name
        self.c = color
        self.p = pred
        self.d = d
        # susedi se čuvaju uz odgovarajuću ivicu, koja sadrži informaciju o težini te ivice
        # elementi liste su torke (susedni čvor, odgovarajuća ivica)
        self.adj = []

    def print_adj(self):
        print(f"Susedi čvora {self}: {self.adj}")

    def print_edges(self):
        ret = f"Ivice od čvora {self} ka susednim čvorovima: "
        for p in self.adj:
            ret += f"{p[1]}, "
        print(ret.rstrip(" ,"))

    def __repr__(self):
        return self.name

    def add_edge(self, edge, v):
        if edge.dst == self.name:
            return False
        for a in self.adj:
            if a[1].dst == edge.dst:
                # print("Dupla ivica.")
                return False
        if edge.src == self.name:
            self.adj.append((v, edge))
            return True

    def __lt__(self, other):
        return self.d < other.d

    def __le__(self, other):
        return self.d <= other.d

    def __eq__(self, other):
        return self.d == other.d

class Edge:

    def __init__(self, src, dst, w):
        self.src = src
        self.dst = dst
        self.w = w

    def __repr__(self):
        return f"({self.src}, {self.dst}, {self.w})"


class Graph:

    def __init__(self):
        self.v = {}
        self.e = []

    def print_v(self):
        ret = ""
        for v in self.v:
            ret += f"{v.name} "
        print(ret.rstrip())

    def insert(self, vertex):
        if vertex.name not in self.v.keys():
            self.v[vertex.name] = vertex

    def print_path(self, s, v):
        if v == s:
            print(s)
        elif not v.p:
            print(f"Ne postoji putanja od {s} do {v}.")
        else:
            self.print_path(s, v.p)
            print(v)

    def add_edge(self, edge):
        if edge.src in self.v.keys() and edge.dst in self.v.keys():
            return self.v[edge.src].add_edge(edge, self.v[edge.dst])
        else:
            print(f"Jedan ili oba čvora ne postoje u grafu!")
            return False

    def initialize_single_source(self, src):
        for _, vtx in self.v.items():
            vtx.d = inf
            vtx.p = None
        self.v[src].d = 0

    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def dijkstra(self, src):
        self.initialize_single_source(src)
        s = []
        Q = []
        for vtx in self.v.values():
            heapq.heappush(Q, vtx)
        while len(Q) != 0:
            u = heapq.heappop(Q)
            s.append(u)
            for v in u.adj:
                self.relax(u, v[0], v[1].w)
            heapq.heapify(Q)
