def read_graph_as_edges(vertex_quantity, edge_quantity):
    edges = []
    for edge in range(edge_quantity):
        link1, link2, weight = [int(x) for x in input().split()]
        edges.append((link1, link2, weight))
    return edges


def kruscal(edges, vertex_quantity):
    edges = sorted(edges, key=lambda x: x[2])
    tree, pieces, full_weight = [], {i: 0 for i in range(vertex_quantity)}, 0
    i = 0
    for v1, v2, weight in edges:
        to_add = True
        if pieces[v1] == 0 == pieces[v2]:
            pieces[v1] = {i}
            pieces[v2] = pieces[v1]
            i += 1
        elif pieces[v1] == 0:
            pieces[v1] = pieces[v2]
        elif pieces[v2] == 0:
            pieces[v2] = pieces[v1]
        elif pieces[v1] != pieces[v2]:
            pieces[v2].update(pieces[v1])
            pieces[v1].update(pieces[v2])
        else:
            to_add = False
        if to_add:
            tree.append((v1, v2))
            full_weight += weight
    return tree, full_weight

vertex_number, edge_number = tuple(map(int, input().split()))
print(kruscal(read_graph_as_edges(vertex_number, edge_number), vertex_number))
