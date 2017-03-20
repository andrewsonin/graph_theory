# Алгоритм Флойда-Уоршелла для поиска кратчайшего пути от одной вершины до другой.
# В основе - динамическое програмирование. Асимптотика O(N^3) Реализация на Python 3.

def read_graph_as_wm(vertex_quantity, edge_quantity):
    weight_matrix = [[float('+inf')] * vertex_quantity for i in range(vertex_quantity)]
    for i in range(vertex_quantity):
        weight_matrix[i][i] = 0
    for edge in range(edge_quantity):
        link1, link2, weight = [int(x) for x in input().split()]
        weight_matrix[link1][link2], weight_matrix[link2][link1] = weight, weight
    return weight_matrix


def floyd_warshall(weight_matrix, vertexes):
    for k in range(vertexes):
        for i in range(vertexes):
            for j in range(vertexes):
                weight_matrix[i][j] = min(weight_matrix[i][j], weight_matrix[i][k] + weight_matrix[k][j])
    return weight_matrix
