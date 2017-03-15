class inser_text:
    pass
'''
Кузнечик находится на Бирже, которая является числовой прямой, в клетке №1 и собирается заработать денег.
В каждой клетке числовой прямой, которую он посещает, он вынужден заключить сделку со всеми имеющимися средствами.
При этом он может получить как прибыль, так и убыток. Прибыльность каждой клетки задана процентами со знаком.
Если знак положительный — сделка увеличивает сумму денег Кузнечика на указанный процент от его текущей суммы.
Если отрицательный — сделка уменьшает сумму денег Кузнечика на указанный процент.
В самой клетке №1 никакой сделки не заключается.
Вывести на экран путь, максимизирующий сумму, которую сможет заработать Кузнечик на бирже,
 если он может совершать прыжки на клетку с номером +2 и +3 от текущей, но не может прыгнуть на соседнюю клетку.
Обратите внимание, что Кузнечик не обязан останавливаться в точке последней возможной сделки!
Более того, если совершение сделок окажется убыточным, Кузнечик имеет право остаться в клетке №1 с исходным капиталом.
Формат входных данных
В первой строке записано целое число — стартовый капитал Кузнечика.
Во второй строке записаны целые числа — проценты со знаком + или -. Доходность не превышает 1000%, а убыточность -100%.
Отрицательный баланс у Кузнечика недопустим. Максимальный номер клетки задаётся количеством чисел в строке ввода.
Формат выходных данных
Клетки, по которым должен пройти Кузнечик, чтобы получить максимальную выгоду.
'''
init_money = int(input())
row = list(map(int, input().split()))
G = {i:{} for i in range(len(row))}
for i in range(len(row)-2):
    G[i][i+2] = 1 + 0.01 * row[i+2]
    if i+3 < len(row):
        G[i][i+3] = 1 + 0.01 * row[i+3]

def dijkstra(G,start):
    global init_money
    d = {v: -1 for v in G}
    d[start] = init_money
    ways = {v: [] for v in G}
    ways[start].append(start)
    used = set()
    for i in range (len(d)):
        max_d = -1
        for v in d:
            if d[v] > max_d and v not in used:
                current = v
                max_d = d[v]
        for neighbour in G[current]:
            l = d[current] * G[current][neighbour]
            if l > d[neighbour]:
                d[neighbour] = l
                ways[neighbour] = ways[current] + [neighbour]
        used.add(current)
    return ways, d
result = dijkstra(G,0)
print(*[i+1 for i in result[0][max(result[1].items(), key= lambda x: x[1])[0]]])