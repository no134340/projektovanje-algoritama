def topological_sort(G):
    G.DFS()
    return G.t

if __name__ == '__main__':
    from graph import Graph, Vertex, VertexColor, Data

    # ------------------------ Zadatak 1.1 ------------------------
    print("Zadatak 1, graf 1:\n")

    g1 = Graph()
    v = []
    for i in range(0, 5):
        v.append(Vertex(Data(i + 1), VertexColor.BLACK))
    v[0].set_adj([v[1], v[4]])
    v[1].set_adj([v[0], v[4], v[2], v[3]])
    v[2].set_adj([v[1], v[3]])
    v[3].set_adj([v[1], v[4], v[2]])
    v[4].set_adj([v[3], v[0], v[1]])

    for vtx in v:
        g1.insert(vtx)

    for u in g1.v:
        u.print_adj()
    print()
    for u in g1.v:
        u.print_edges()

    print()

    # ------------------------ Zadatak 1.2 ------------------------
    print("Zadatak 1, graf 2:\n")
    g2 = Graph()
    v = []
    for i in range(0, 6):
        v.append(Vertex(Data(i + 1), VertexColor.BLACK))
    v[0].set_adj([v[1], v[3]])
    v[1].set_adj([v[4]])
    v[2].set_adj([v[5], v[4]])
    v[3].set_adj([v[1]])
    v[4].set_adj([v[3]])
    v[5].set_adj([v[5]])

    for vtx in v:
        g2.insert(vtx)

    for u in g2.v:
        u.print_adj()
    print()
    for u in g2.v:
        u.print_edges()

    print()

    # ------------------------ Zadatak 2 ------------------------
    print("Zadatak 2")

    gb = Graph()
    v = []
    for i in range(0, 8):
        v.append(Vertex(Data(i), VertexColor.WHITE))

    v[0].data.name = "v"
    v[1].data.name = "r"
    v[2].data.name = "s"
    v[3].data.name = "w"
    v[4].data.name = "x"
    v[5].data.name = "y"
    v[6].data.name = "u"
    v[7].data.name = "t"

    v[0].set_adj([v[1]])
    v[1].set_adj([v[0], v[2]])
    v[2].set_adj([v[1], v[3]])
    v[3].set_adj([v[2], v[4], v[7]])
    v[4].set_adj([v[3], v[7], v[5], v[6]])
    v[5].set_adj([v[4], v[6]])
    v[6].set_adj([v[4], v[5], v[7]])
    v[7].set_adj([v[3], v[4], v[6]])

    for vtx in v:
        gb.insert(vtx)

    for u in gb.v:
        u.print_adj()
    print()

    gb.BFS(gb.v[2])

    print(f"Putanja od {gb.v[2]} do {gb.v[5]}:")
    gb.print_path(gb.v[2], gb.v[5])
    print("\n")

    # ------------------------ Zadatak 3 ------------------------
    print("Zadatak 3\n")

    gd = Graph()
    v = []
    for i in range(0, 6):
        v.append(Vertex(Data(i), VertexColor.WHITE))

    v[0].data.name = "u"
    v[1].data.name = "v"
    v[2].data.name = "x"
    v[3].data.name = "y"
    v[4].data.name = "w"
    v[5].data.name = "z"

    v[0].set_adj([v[1], v[2]])
    v[1].set_adj([v[3]])
    v[2].set_adj([v[1]])
    v[3].set_adj([v[2]])
    v[4].set_adj([v[3], v[5]])
    v[5].set_adj([v[5]])

    for vtx in v:
        gd.insert(vtx)

    for u in gd.v:
        u.print_adj()
    print()

    gd.DFS()

    print("DFS vremena: posećen|završen")
    for u in gd.v:
        print(f"Čvor {u}: {u.d}|{u.f}")
    print()

    # Zadatak 4

    print("Zadatak 4\n")

    gt = Graph()
    v = []
    for i in range(0, 9):
        v.append(Vertex(Data(i), VertexColor.WHITE))

    v[0].data.name = "shirt"
    v[1].data.name = "tie"
    v[2].data.name = "jacket"
    v[3].data.name = "watch"
    v[4].data.name = "undershorts"
    v[5].data.name = "pants"
    v[6].data.name = "belt"
    v[7].data.name = "shoes"
    v[8].data.name = "socks"

    v[0].set_adj([v[1], v[6]])
    v[1].set_adj([v[2]])
    # v[2].set_adj([])
    # v[3].set_adj([])
    v[4].set_adj([v[5],  v[7]])
    v[5].set_adj([v[6], v[7]])
    # v[7].set_adj([])
    v[8].set_adj([v[7]])

    for vtx in v:
        gt.insert(vtx)

    t_sorted = topological_sort(gt)

    print("DFS vremena: posećen|završen")
    for u in gt.v:
        print(f"Čvor {u}: {u.d}|{u.f}")

    print(f"\nLista čvorova nakon topološkog sortiranja: {[u for u in t_sorted]}")
