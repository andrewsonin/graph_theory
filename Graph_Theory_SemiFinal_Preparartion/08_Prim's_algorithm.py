# Алгоритм построения минимального остовного дерева. Алгоритм Прима на неориентированном взвешенном связном графе


def read_graph_as_lists(vertex_quantity, edge_quantity):
    graph = [[] for i in range(vertex_quantity)]
    for edge in range(edge_quantity):
        link1, link2, weight = [int(x) for x in input().split()]
        graph[link1].append((link2, weight)), graph[link2].append((link1, weight))
    return graph


def prim(graph, vertex_quantity):
    spanning_edges, spanning_vertexes, full_weight = [], {0}, 0
    for i in range(vertex_quantity - 1):
        min_length = float('+inf')
        for vertex in spanning_vertexes:
            for (neighbour, weight) in graph[vertex]:
                if neighbour not in spanning_vertexes and weight < min_length:
                    min_length, current_vertex, current_edges = weight, neighbour, (vertex, neighbour)
        spanning_edges.append(current_edges), spanning_vertexes.add(current_vertex)
        full_weight += min_length
    return full_weight, spanning_edges
