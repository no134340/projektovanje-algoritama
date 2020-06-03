from graph import Graph, VertexColor, Vertex, Edge
from math import inf


def MakeGraph():
    g = Graph()
    for v in vertices:
        g.insert(v)

    g.add_edge(Edge("a", "c", 6))
    g.add_edge(Edge("a", "b", 8))
    g.add_edge(Edge("b", "d", 10))
    g.add_edge(Edge("c", "d", 15))
    g.add_edge(Edge("c", "e", 9))
    g.add_edge(Edge("d", "e", 14))
    g.add_edge(Edge("d", "f", 4))
    g.add_edge(Edge("e", "f", 13))
    g.add_edge(Edge("e", "g", 17))
    g.add_edge(Edge("f", "g", 7))

    return g


def GetInDegrees(g):
    return g.GetInDegrees()


def GetOutDegrees(g):
    return g.GetOutDegrees()


def ShortestPath(g, nodeA, nodeB):
    g.dijkstra(nodeA)
    path = []
    curr = nodeB
    while curr:
        path.append(curr)
        curr = curr.p
    path.reverse()
    return path, nodeB.d


def UpdateEdge(g, nodeA, nodeB, w):
    g.add_edge(Edge(nodeA.name, nodeB.name, w))


def NewShortestPath():
    if g.bellman_ford(vertices[0]):
        path = []
        curr = vertices[6]
        while curr:
            path.append(curr)
            curr = curr.p
        path.reverse()
        return path, vertices[6].d
    else:
        return [], inf


if __name__ == '__main__':
    # Zadatak 1

    vertices = [Vertex("a"), Vertex("b"), Vertex("c"), Vertex("d"), Vertex("e"), Vertex("f"), Vertex("g")]
    g = MakeGraph()

    for vtx in g.v.values():
        print(vtx.print_adj())

    # Zadatak 2
    in_degrees = GetInDegrees(g)
    out_degrees = GetOutDegrees(g)

    print("Ulazni stepeni cvorova: ")
    ret = ""
    for i, d in enumerate(in_degrees):
        ret += f"{vertices[i]} : {d}, "
    print(ret.rstrip(" ,") + "\n")
    print("Izlazni stepeni cvorova: ")
    ret = ""
    for i, d in enumerate(out_degrees):
        ret += f"{vertices[i]} : {d}, "
    print(ret.rstrip(" ,") + "\n")

    # Zadatak 3
    src, dst = vertices[0], vertices[6]
    path, dist = ShortestPath(g, src, dst)

    print(f"Putanja od {src} do {dst}:")
    if len(path) == 1:
        print(f"Putanja od {src} do {dst} ne postoji.")
    else:
        ret = ""
        for v in path:
            ret += f"{v} -> "
        print(ret.rstrip(" ->"))
    print(f"Duzina putanje: {dist}\n")

    # Zadatak 4
    s = vertices[1]
    d = vertices[2]
    new_w = -4
    print(f"Dodavanje ivice od {s} do {d} sa tezinom {new_w}:")
    UpdateEdge(g, s, d, new_w)

    for vtx in g.v.values():
        print(vtx.print_adj())

    print()
    # Zadatak 5
    path, dist = NewShortestPath()

    src, dst = vertices[0], vertices[6]

    print(f"Putanja od {src} do {dst}:")
    if len(path) == 0:
        print(f"Putanja od {src} do {dst} ne postoji.")
    else:
        ret = ""
        for v in path:
            ret += f"{v} -> "
        print(ret.rstrip(" ->"))
    print(f"Duzina putanje: {dist}")
