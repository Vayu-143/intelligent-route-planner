def dfs(graph, start):

    visited = set()

    result = []

    def helper(node):

        visited.add(node)

        result.append(node)

        for neighbor, _ in graph.get_neighbors(node):

            if neighbor not in visited:

                helper(neighbor)

    helper(start)

    return result