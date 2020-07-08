import heapq
from enum import Enum
from math import inf


class VertexColor(Enum):
    WHITE = 255
    GREY = 127
    BLACK = 0


class Vertex:

    def __init__(self, name, index):
        self.name = name
        self.p = None
        self.d = None
        self.f = None
        self.color = VertexColor.WHITE
        self.index = index

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.d < other.d

    def __le__(self, other):
        return self.d <= other.d

    def __eq__(self, other):
        return self.d == other.d


class Edge:

    def __init__(self, first, second, w):
        self.first = first
        self.second = second
        self.w = w

    def __repr__(self):
        return f"({self.first}, {self.second}, {self.w})"


def find_set(set_list, vertex):
    for s in set_list:
        if vertex in s:
            return s


class Graph:

    def __init__(self):
        self.v = {}
        self.adj_matrix = None
        self.n = 0
        self.edge_list = None
        self.adj_list = None
        self.indices = {}
        self.time = 0
        self.finished = []
        self.components = []

    def set_edge_list(self, edges):
        self.edge_list = edges

    def add_vertex(self, vtx):
        if vtx.name not in self.v.keys():
            self.v[vtx.name] = vtx
            self.n += 1
            self.indices[vtx.index] = vtx.name

    def make_adj_matrix(self, undirected=False):
        edges = self.edge_list
        n = self.n
        self.adj_matrix = [0] * (n ** 2)
        for edge in edges:
            self.adj_matrix[self.v[edge.first].index * n + self.v[edge.second].index] = edge.w
            if undirected:
                self.adj_matrix[self.v[edge.second].index * n + self.v[edge.first].index] = edge.w

    def make_adj_list(self, undirected=False):
        adj_list = []
        for i in range(self.n):
            adj_list.append([])
        for edge in self.edge_list:
            first = self.v[edge.first]
            second = self.v[edge.second]
            adj_list[first.index].append([second, edge.w])
            if undirected:
                adj_list[second.index].append([first, edge.w])
        self.adj_list = adj_list

    def DFS_visit(self, u, comp=False, comp_list=None):
        if comp:
            comp_list.append(u)
        self.time += 1
        u.d = self.time
        u.color = VertexColor.GREY
        for edge in self.adj_list[u.index]:
            v = edge[0]
            if v.color == VertexColor.WHITE:
                v.p = u
                self.DFS_visit(v, comp, comp_list)
        u.color = VertexColor.BLACK
        self.finished.append(u)
        self.time += 1
        u.f = self.time

    def DFS(self):
        for u in self.v.values():
            u.color = VertexColor.WHITE
            u.p = None
        self.time = 0
        for u in self.v.values():
            if u.color == VertexColor.WHITE:
                self.DFS_visit(u)
        self.finished.reverse()
        return self.finished

    def DFS_component(self, finished):
        for u in self.v.values():
            u.color = VertexColor.WHITE
            u.p = None
        self.time = 0
        for vertex in finished:
            u = self.v[vertex.name]
            if u.color == VertexColor.WHITE:
                comp_list = list()
                self.DFS_visit(u, True, comp_list)
                self.components.append(comp_list)

    def mst_prim(self, source):
        Q = []
        for u in self.v.values():
            u.d = inf
            u.p = None
            heapq.heappush(Q, u)
        source.d = 0
        heapq.heapify(Q)
        mst = []
        while len(Q) != 0:
            u = heapq.heappop(Q)
            if u != source:
                mst.append((u, u.p, u.d))
            for v in self.adj_list[u.index]:
                if v[0] in Q and v[1] < v[0].d:
                    v[0].p = u
                    v[0].d = v[1]
            heapq.heapify(Q)
        return mst

    def mst_kruskal(self):
        A = set()
        temp = []
        for v in self.v.values():
            s = {v}
            temp.append(s)
        self.edge_list.sort(key=lambda edge: edge.w)
        for edge in self.edge_list:
            src = self.v[edge.first]
            dst = self.v[edge.second]
            src_set = find_set(temp, src)
            dst_set = find_set(temp, dst)
            if src_set != dst_set:
                A.add(edge)
                u_set = src_set.union(dst_set)
                temp.remove(dst_set)
                temp.remove(src_set)
                temp.append(u_set)
        return A

    def transpose(self):
        transposed = Graph()
        transposed.n = self.n

        for name, vertex in self.v.items():
            transposed.v[name] = Vertex(name, vertex.index)
            transposed.indices[vertex.index] = name

        edge_list = []
        for edge in self.edge_list:
            edge_list.append(Edge(edge.second, edge.first, edge.w))
        transposed.set_edge_list(edge_list)
        transposed.make_adj_list(undirected=False)
        transposed.make_adj_matrix()

        return transposed

    def print_adj_list(self):
        for i, lst in enumerate(self.adj_list):
            print(f"{self.indices[i]}: {lst}")

    def print_adj_matrix(self):
        disp = "    "
        for i in range(self.n):
            disp += f"{self.indices[i]:4}"
        disp += "\n"
        for i in range(self.n):
            disp += f"{self.indices[i]}"
            for j in range(self.n):
                disp += f"{self.adj_matrix[i * self.n + j]:4}"
            disp += "\n"
        print(disp)
