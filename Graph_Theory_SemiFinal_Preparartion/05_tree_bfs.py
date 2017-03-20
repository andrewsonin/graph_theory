# Остовное дерево поиска в ширину. Реализация на Python 3. O(N)

def read_graph_as_lists():
    vertexes, edges = tuple(map(int, input().split()))
    graph = [[] for i in range(vertexes)]
    for edge in range(edges):
        a, b = tuple(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs(graph, start, path, used=None):
    if used is None:
        used = set()
    used.add(start)
    queue = [start]
    while queue:
        vertex = queue.pop()
        for neighbour in graph[vertex]:
            if neighbour not in used:
                path.append((vertex, neighbour))
                used.add(neighbour)
                queue.append(neighbour)
    return path


def build_tree(graph):
    tree = []
    bfs(graph, 0, tree, set())
    return tree

for edge in build_tree(read_graph_as_lists()):
    print(' '.join(map(str, edge)))
