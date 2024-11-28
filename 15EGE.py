# # Граф в виде списка смежности
# graph = {
#     "А": ["Б", "В", "Г"],
#     "Б": ["В", "Д"],
#     "В": ["Д", "Е", "Ж"],
#     "Г": ["В", "Ж"],
#     "Д": ["И"],
#     "Е": ["Л", "К"],
#     "Ж": ["К"],
#     "И": ["Л"],
#     "Л": [],
#     "К": ["Л"]
# }

# # Функция для нахождения топологического порядка
# def topological_sort(graph):
#     visited = set()
#     order = []

#     def dfs(node):
#         if node not in visited:
#             visited.add(node)
#             for neighbor in graph[node]:
#                 dfs(neighbor)
#             order.append(node)

#     for node in graph:
#         dfs(node)

#     return order[::-1]  # Разворачиваем порядок

# # Получаем топологический порядок узлов
# order = topological_sort(graph)

# # Инициализация массива для хранения количества путей
# dp = {node: 0 for node in graph}
# dp["А"] = 1  # Начинаем с одного пути из города А

# # Обход графа для подсчёта путей
# for node in order:
#     for neighbor in graph[node]:
#         dp[neighbor] += dp[node]

# # Вывод количества путей в конечный узел
# print(f"Количество различных путей из А в Л: {dp['Л']}")
graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["F"],
    "D": ["C", "F"],
    "E": ["G"],
    "F": ["G"],
    "G": []
}

# Функция для топологической сортировки
def topological_sort(graph):
    visited = set()
    order = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            order.append(node)

    for node in graph:
        dfs(node)

    return order[::-1]

# Топологический порядок
order = topological_sort(graph)

# Инициализация dp
dp = {node: 0 for node in graph}
dp["A"] = 1

# Обход графа
for node in order:
    for neighbor in graph[node]:
        dp[neighbor] += dp[node]

print(f"Количество различных путей из A в G: {dp['G']}")
