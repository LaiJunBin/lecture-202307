n = int(input())

for _ in range(n):
    edges = input().split()
    graph = {}

    for edge in edges:
        x, y = [int(i) for i in edge.split(',')]

        if x not in graph:
            graph[x] = []

        if y not in graph:
            graph[y] = []

        graph[x].append(y)
        graph[y].append(x)

    nodes = list(graph.keys())

    if len(nodes) - 1 != len(edges):
        print('F')
        continue

    visited = set()
    stack = [nodes[0]]

    while stack:
        node = stack.pop()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    if len(visited) == len(nodes):
        print('T')
    else:
        print('F')
        
