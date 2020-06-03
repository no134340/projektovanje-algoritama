from enum import Enum
from math import inf
import heapq

class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255


class Vertex():

    def __init__(self, name):
        self.p = None
        self.d = 0
        self.name = name
        self.c = VertexColor.WHITE
        self.adj = []
        self.indgr = 0
        self.outdgr = 0

    def __repr__(self):
        return self.name

    def add_edge(self, edge, n):
        if edge.src != self.name:
            return False
        for a in self.adj:
            if a[1].dst == edge.dst:
                a[1].w = edge.w
                return
        self.adj.append((n, edge))
        self.outdgr += 1
        n.indgr += 1

    def print_adj(self):
        ret = f"Susedi cvora {self} su: "
        for _, v in self.adj:
            ret += f"{v} "
        return ret.rstrip()

    def __le__(self, other):
        return self.d <= other.d

    def __lt__(self, other):
        return self.d < other.d

    def __eq__(self, other):
        return self.d == other.d


class Edge():

    def __init__(self, src, dst, w):
        self.src = src
        self.dst = dst
        self.w = w

    def __repr__(self):
        return f"({self.src}, {self.dst}, {self.w})"


class Graph:

    def __init__(self):
        self.v = {}
        self.vnames = []
        self.e = []

    def insert(self, vertex):
        if vertex.name not in self.v.keys():
            self.vnames.append(vertex.name)
            self.v[vertex.name] = vertex

    def add_edge(self, edge):
        if edge.src in self.v.keys() and edge.dst in self.v.keys():
            self.e.append(edge)
            return self.v[edge.src].add_edge(edge, self.v[edge.dst])
        else:
            return False

    def GetOutDegrees(self):
        out_degrees = []
        for vname in self.vnames:
            out_degrees.append(self.v[vname].outdgr)
        return out_degrees

    def GetInDegrees(self):
        in_degrees = []
        for vname in self.vnames:
            in_degrees.append(self.v[vname].indgr)
        return in_degrees

    def initialize_single_source(self, s):
        for v in self.v.values():
            v.d = inf
            v.p = None
        s.d = 0

    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def dijkstra(self, src):
        self.initialize_single_source(src)
        s = []
        Q = list(self.v.values())
        heapq.heapify(Q)
        while len(Q) > 0:
            u = heapq.heappop(Q)
            s.append(u)
            for v, e in u.adj:
                self.relax(u, v, e.w)
            heapq.heapify(Q)

    def bellman_ford(self, src):
        self.initialize_single_source(src)
        for i in range(len(self.v) - 1):
            for e in self.e:
                self.relax(self.v[e.src], self.v[e.dst], e.w)
        for e in self.e:
            if self.v[e.dst].d > self.v[e.src].d + e.w:
                print("Uočen negativan ciklus!")
                return False
        return True
