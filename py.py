def orientation(p, q, r):
    """
    Вычисляет ориентацию тройки точек p, q, r.
    Возвращает 0, если точки коллинеарны, 1, если образуют
    положительный поворот, и -1 в противном случае.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def jarvis(points):
    """
    Принимает на вход список координат точек в формате [(x1, y1), (x2, y2), ...].
    Возвращает список координат точек выпуклой оболочки в формате [(x1, y1), (x2, y2), ...].
    """
    n = len(points)
    if n < 3:
        return []
    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == -1:
                q = i
        p = q
        if p == l:
            break
    return hull
points = [(0, 0), (223, 464), (0, 749)]
hull = jarvis(points)
print(hull)