# Остовное дерево поиска в глубину. Реализация на Python 3. O(N)


def read_graph_as_lists():
    vertexes, edges = tuple(map(int, input().split()))
    graph = [[] for i in range(vertexes)]
    for edge in range(edges):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    return graph


def dfs(graph, start, path, used=None):
    if used is None:
        used = set()
    used.add(start)
    for vertex in graph[start]:
        if vertex not in used:
            path.append((start, vertex))
            dfs(graph, vertex, path, used)


def build_tree(graph):
    tree = []
    dfs(graph, 0, tree, set())
    return tree

for edge in build_tree(read_graph_as_lists()):
    print(' '.join(map(str, edge)))
