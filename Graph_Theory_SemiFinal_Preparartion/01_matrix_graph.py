# Считывание матрицы смежности орграфа и вывод списков смежности. Начальный граф задан списком ребер,
# с изначальным заданием их числа и числа вершин


def read_graph_as_matrix():
    vertexes, edges = tuple(map(int, input().split()))
    graph = [[0] * vertexes for i in range(vertexes)]
    for edge in range(edges):
        a, b = tuple(map(int, input().split()))
        graph[a][b] = 1
    return graph


def print_graph_as_lists(graph_as_matrix):
    graph_len = len(graph_as_matrix)
    graph_as_lists = [[] for i in range(graph_len)]
    for vertex1 in range(graph_len):
        for vertex2 in range(graph_len):
            if graph_as_matrix[vertex1][vertex2] == 1:
                graph_as_lists[vertex1].append(vertex2)
    for i in range(graph_len):
        if graph_as_lists[i]:
            print(str(i) + ':', ' '.join(map(str, graph_as_lists[i])))

print_graph_as_lists(read_graph_as_matrix())
