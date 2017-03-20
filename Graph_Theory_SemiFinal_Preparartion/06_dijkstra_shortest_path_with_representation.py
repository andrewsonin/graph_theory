# Алгоритм Дейкстры с восстановлением кратчайшего пути. Реализация на Python 3. Реализация для связного графа.
# Иначе просто пробегаем по компоненте связности, которую можно получить при помощи dfs или bfs. O(N^3)


def read_graph_as_lists(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    for edge in range(edge_number):
        link1, link2, weight = [int(x) for x in input().split()]
        graph[link2].append((link1, weight)), graph[link1].append((link2, weight))
    return graph


def dijkstra(graph, start, vertex_quantity, used_vertexes=set()):
    path_length = [float('+inf')] * vertex_quantity
    path_length[start] = 0
    for i in range(vertex_quantity):
        min_distance = float('+inf')
        for vertex in range(vertex_quantity):
            if path_length[vertex] < min_distance and vertex not in used_vertexes:
                current = vertex
                min_distance = path_length[vertex]
        for neighbour in graph[current]:
            length = path_length[current] + neighbour[1]
            if length < path_length[neighbour[0]]:
                path_length[neighbour[0]] = length
        used_vertexes.add(current)
    return path_length


vertex_number, edge_quantity, start_vertex, end_vertex = tuple(map(int, input().split()))
print(dijkstra(read_graph_as_lists(vertex_number, edge_quantity), start_vertex, vertex_number)[end_vertex])
