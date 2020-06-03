from enum import Enum
from math import inf
from collections import deque


class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255


class Data:

    def __init__(self, num, name=""):
        self.num = num
        self.name = name


class Vertex:

    def __init__(self, data, color, pred=None, d=None):
        self.data = data
        self.c = color
        self.p = pred
        self.d = d
        self.adj = None
        self.f = None

    def print_adj(self):
        print(f"Susedi čvora {self}: {self.adj}")

    def print_edges(self):
        ret = f"Veze čvora {self} sa susednim čvorovima: "
        for v in self.adj:
            ret += f"({self}, {v}), "
        print(ret.rstrip(" ,"))

    def set_adj(self, adj):
        self.adj = adj

    def __repr__(self):
        if self.data.name != "":
            return self.data.name
        else:
            return str(self.data.num)


class Graph:

    def __init__(self):
        self.v = []
        self.time = None
        self.t = []

    def print_v(self):
        ret = ""
        for v in self.v:
            if v.data.name != "":
                ret += f"{v.data.name} "
            else:
                ret += f"{v.data.num} "
        print(ret.rstrip())

    def insert(self, vertex):
        self.v.append(vertex)

    def BFS(self, s):
        for u in self.v:
            if u == s:
                continue
            u.c = VertexColor.WHITE
            u.d = inf
            u.p = None
        s.c = VertexColor.GRAY
        s.d = 0
        s.p = None
        Q = deque()
        Q.append(s)
        while len(Q) > 0:
            u = Q.popleft()
            for v in u.adj:
                if v.c == VertexColor.WHITE:
                    v.c = VertexColor.GRAY
                    v.d = u.d + 1
                    v.p = u
                    Q.append(v)
            u.c = VertexColor.BLACK

    def print_path(self, s, v):
        if v == s:
            print(s)
        elif v.p == None:
            print(f"Ne postoji putanja od {s} do {v}.")
        else:
            self.print_path(s, v.p)
            print(v)

    def DFS(self):
        for u in self.v:
            u.c = VertexColor.WHITE
            u.p = None
        self.time = 0
        for u in self.v:
            if u.c == VertexColor.WHITE:
                self.DFS_visit(u)

    def DFS_visit(self, u):
        self.time += 1
        u.d = self.time
        u.c = VertexColor.GRAY
        if u.adj:
            for v in u.adj:
                if v.c == VertexColor.WHITE:
                    v.p = u
                    self.DFS_visit(v)
        u.c = VertexColor.BLACK
        self.time += 1
        u.f = self.time
        self.t.append(u)
