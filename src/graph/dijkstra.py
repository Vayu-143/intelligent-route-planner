import heapq


def dijkstra(graph, start):

    distances = {
        node: float("inf")
        for node in graph.get_nodes()
    }

    previous = {
        node: None
        for node in graph.get_nodes()
    }

    distances[start] = 0

    pq = [(0, start)]

    visited_count = 0

    while pq:

        current_distance, current_node = (
            heapq.heappop(pq)
        )

        visited_count += 1

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get_neighbors(
            current_node
        ):

            new_distance = (
                current_distance + weight
            )

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

                previous[neighbor] = current_node

                heapq.heappush(
                    pq,
                    (
                        new_distance,
                        neighbor
                    )
                )

    return (
        distances,
        previous,
        visited_count
    )