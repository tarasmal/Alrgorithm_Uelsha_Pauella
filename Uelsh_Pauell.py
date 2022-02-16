n, v = list(map(int, input().split()))
vertexes = list(range(1, n + 1))
edges = []
colored = []
fired = []
for _ in range(v): edges.append(tuple(map(int, input().split())))
for v in range(1, v + 1):
    dntColor = []
    for tuple_ in edges:
        if v in tuple_:
            for vertex in tuple_:
                if vertex != v: dntColor.append(vertex)
    a = [vertex for vertex in vertexes if vertex not in dntColor and vertex not in fired]
    if len(a) > 0: colored.append(a)
    fired.extend(colored[-1])
result = {}
for index in range(len(colored)):
    result[index + 1] = colored[index]

print(result)