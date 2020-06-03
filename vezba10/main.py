from graph import Edge, VertexColor, Vertex, Graph
from random import randint


# za Zadatak 3
def make_random_graph():
    graph = Graph()
    vn = randint(4, 7)
    vertices = [str(x) for x in range(vn)]
    print(f"Broj čvorova: {len(vertices)}")

    for v in vertices:
        graph.insert(Vertex(v))

    # broj ivica da se kreće od broja čvorova do kompletnog grafa
    en = randint(vn, vn * (vn - 1) / 2)
    print(f"Broj ivica: {en}\n")

    for i in range(en):
        src = vertices[randint(0, vn - 1)]
        dst = src
        added = False
        while not added:
            dst = vertices[randint(0, vn - 1)]
            added = graph.add_edge(Edge(src, dst, randint(1, 15)))

    # for debug:
    # for v in graph.v.values():
    #     v.print_edges()
    # print()

    source = vertices[randint(0, vn - 1)]

    graph.dijkstra(source)

    print(f"Rezultat primene Dijsktra algoritma sa čvorom {source} kao izvorom:")
    for v in graph.v.values():
        print(f"Putanja od {source} do {v}: ")
        graph.print_path(graph.v[source], v)
        print(f"Dužina putanje: {v.d}\n")



if __name__ == '__main__':


    # Zadatak 1
    g = Graph()

    vertices = ["s", "t", "y", "x", "y", "z"]
    for v in vertices:
        g.insert(Vertex(v))

    g.add_edge(Edge("s", "t", 10))
    g.add_edge(Edge("s", "y", 5))
    g.add_edge(Edge("t", "y", 2))
    g.add_edge(Edge("t", "x", 1))
    g.add_edge(Edge("y", "t", 3))
    g.add_edge(Edge("y", "x", 9))
    g.add_edge(Edge("y", "z", 2))
    g.add_edge(Edge("x", "z", 4))
    g.add_edge(Edge("z", "x", 6))
    g.add_edge(Edge("z", "s", 7))

    # Ispis ivica grafa:
    print("Ivice čvorova grafa (sa težinama):")
    for v in g.v.values():
        v.print_edges()
    print()


    # Zadatak 2
    source = "s"
    g.dijkstra(source)

    print(f"Rezultat primene Dijsktra algoritma sa čvorom {source} kao izvorom:")
    for v in g.v.values():
        print(f"Putanja od {source} do {v}: ")
        g.print_path(g.v[source], v)
        print(f"Dužina putanje: {v.d}\n")
    print()

    # Zadatak 3

    make_random_graph()