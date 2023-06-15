n = int(input())

for _ in range(n):
    edges = input().split()
    graph = {}
    edge_count = 0

    for edge in edges:
        x, y = [int(i) for i in edge.split(',')]
        if x == 0 and y == 0:
            break

        if x not in graph:
            graph[x] = []

        if y not in graph:
            graph[y] = []

        graph[x].append(y)
        graph[y].append(x)
        edge_count += 1


    nodes = list(graph.keys())

    if len(nodes) == 0:
        print(0)
        continue

    if edge_count != len(nodes) - 1:
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

    if len(visited) != len(nodes):
        print('F')
        continue


    leaves = []
    for node in graph:
        if len(graph[node]) == 1:
            leaves.append(node)

    print(len(leaves) - 1)


