# Алгоритм Дейкстры с восстановлением кратчайшего пути. Реализация на Python 3. Реализация для связного графа.
# Иначе просто пробегаем по компоненте связности, которую можно получить при помощи dfs или bfs. O(N^3)


def read_graph_as_lists(vertex_number, edge_number):
    graph = [[] for i in range(vertex_number)]
    for edge in range(edge_number):
        link1, link2, weight = [int(x) for x in input().split()]
        graph[link2].append((link1, weight)), graph[link1].append((link2, weight))
    return graph


def dijkstra(graph, start, vertex_quantity):
    used = set()
    ways = {i: [] for i in range(vertex_quantity)}
    path_length = [float('+inf')] * vertex_quantity
    ways[start] = [start]
    path_length[start] = 0
    for i in range(vertex_quantity - 1):
        min_distance = float('+inf')
        for vertex in range(vertex_quantity):
            if vertex not in used and path_length[vertex] < min_distance:
                current = vertex
                min_distance = path_length[vertex]
        for neighbour in graph[current]:
            length = path_length[current] + neighbour[1]
            if length < path_length[neighbour[0]]:
                path_length[neighbour[0]] = length
                ways[neighbour[0]] = ways[current] + [neighbour[0]]
        used.add(current)
    return path_length, ways


vertex_number, edge_quantity, start_vertex, end_vertex = tuple(map(int, input().split()))
print(dijkstra(read_graph_as_lists(vertex_number, edge_quantity), start_vertex, vertex_number))
