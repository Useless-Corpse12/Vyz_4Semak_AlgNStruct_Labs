def floyd_path(cnt, rts, start, end, directed=True):
    start = int(start)
    end = int(end)
    if not (0 <= start < cnt and 0 <= end < cnt):
        raise ValueError("Вершины start и end должны быть в диапазоне [0, cnt-1]")

    INF = 10**9
    dist = [[INF] * cnt for _ in range(cnt)]
    next_node = [[None] * cnt for _ in range(cnt)]

    # Диагональ: расстояние до себя = 0
    for i in range(cnt):
        dist[i][i] = 0
        next_node[i][i] = i

    for u, v, w in rts:
        if w < dist[u][v]:
            dist[u][v] = w
            next_node[u][v] = v
        if not directed:  # для неориентированного — симметрично
            if w < dist[v][u]:
                dist[v][u] = w
                next_node[v][u] = u

    for k in range(cnt):
        for i in range(cnt):
            # Оптимизация: если i→k недостижимо, дальше нет смысла
            if dist[i][k] == INF:
                continue
            for j in range(cnt):
                if dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    if next_node[start][end] is None or dist[start][end] == INF:
        return None  # пути не существует

    path = []
    curr = start
    while curr != end:
        path.append(curr)
        curr = next_node[curr][end]
        if curr is None:  # защита от зацикливания
            return None
    path.append(end)

    return "-".join(map(str, path))

def dijkstra_path(cnt, rts, a, b, directed=True):
    a= int(a)
    b= int(b)
    # 0. Быстрая проверка входных данных
    if not (0 <= a < cnt and 0 <= b < cnt):
        raise ValueError("Вершины a и b должны быть в диапазоне [0, cnt-1]")

    # 1. Строим список смежности из rts
    adj = [[] for _ in range(cnt)]
    for u, v, w in rts:
        adj[u].append((v, w))          # ребро u -> v с весом w
        if not directed:               # если граф неориентированный
            adj[v].append((u, w))      # добавляем обратное ребро

    # 2. Инициализация массивов
    INF = float('inf')
    dist = [INF] * cnt      # кратчайшие расстояния от a
    prev = [-1] * cnt       # предыдущая вершина в пути
    visited = [False] * cnt # флаг обработки
    dist[a] = 0             # расстояние до старта = 0

    # 3. Основной цикл Дейкстры
    for _ in range(cnt):
        # а) Ищем непосещённую вершину с минимальным dist
        u = -1
        for v in range(cnt):
            if not visited[v] and (u == -1 or dist[v] < dist[u]):
                u = v

        # Если все достижимые вершины обработаны или попали в изоляцию
        if u == -1 or dist[u] == INF:
            break

        visited[u] = True  # фиксируем вершину
        if u == b:         # оптимизация: дошли до цели
            break

        # б) "Расслабляем" соседей
        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u  # запоминаем, откуда пришли

    # 4. Восстановление пути
    if dist[b] == INF:
        return None, []  # пути не существует

    path = []
    curr = b
    while curr != -1:
        path.append(curr)
        if curr == a:
            break
        curr = prev[curr]

    return dist[b], path[::-1]  # длина, путь в прямом порядке