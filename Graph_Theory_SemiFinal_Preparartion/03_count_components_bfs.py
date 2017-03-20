# Подсчёт компонент связности поиском в ширину. Реализация на Python 3.


def read_graph_as_lists():
    vertexes, edges = tuple(map(int, input().split()))
    graph = [[] for i in range(vertexes)]
    for edge in range(edges):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs(graph, start, used=None):
    if used is None:
        used = set()
    queue = list()
    queue.append(start)
    used.add(start)
    while queue:
        current = queue.pop()
        for neighbour in graph[current]:
            if neighbour not in used:
                used.add(neighbour)
                queue.append(neighbour)


def count_components(graph):
    used = set()
    number_of_components = 0
    for vertex in range(len(graph)):
        if vertex not in used:
            bfs(graph, vertex, used)
            number_of_components += 1
    return number_of_components

print(count_components(read_graph_as_lists()))
