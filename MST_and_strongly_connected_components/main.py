from graph import Vertex, VertexColor, Graph, Edge


def find_strongly_connected_components(graph):
    graph.DFS()
    transposed = graph.transpose()

    transposed.DFS_component(graph.finished)
    print("Strongly connected components in the graph:")
    for comp_list in transposed.components:
        print(f"{comp_list}")
    print()


if __name__ == '__main__':
    vertices = ["a", "b", "c", "d", "e", "f", "g", "h"]

    g = Graph()

    for i, name in enumerate(vertices):
        g.add_vertex(Vertex(name, i))

    edges = [Edge("a", "b", 4),
             Edge("b", "f", 8),
             Edge("b", "c", 8),
             Edge("b", "e", 11),
             Edge("c", "d", 7),
             Edge("c", "g", 2),
             Edge("d", "c", 6),
             Edge("d", "h", 1),
             Edge("e", "a", 2),
             Edge("e", "f", 4),
             Edge("f", "g", 9),
             Edge("g", "f", 14),
             Edge("g", "h", 10),
             Edge("h", "h", 10)]

    g.set_edge_list(edges)
    g.make_adj_matrix(False)
    g.print_adj_matrix()

    g.make_adj_list(False)
    g.print_adj_list()
    print()

    find_strongly_connected_components(g)

    # za Prim i Kruskala staviti da je graf neusmeren
    # tj. kada se prave adj list i matrix staviti True

    # # MST Prim
    # print("\nMST - Prim:")
    # mst = g.mst_prim(g.v['a'])
    # print(mst)
    #
    # # MST Kruskal
    # print("\nMST - Kruskal:")
    # mst = g.mst_kruskal()
    # print(mst)
