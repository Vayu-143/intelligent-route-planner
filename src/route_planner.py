from src.graph.dijkstra import dijkstra
from src.graph.astar import astar

from src.models.route_result import RouteResult

from src.analytics.route_analytics import (
    RouteAnalytics
)


class RoutePlanner:

    def __init__(self, graph):

        self.graph = graph

    def reconstruct_path(
        self,
        previous,
        destination
    ):
        """
        Reconstruct path from Dijkstra parent map.
        """

        path = []

        current = destination

        while current:

            path.append(current)

            current = previous[current]

        path.reverse()

        return path

    def shortest_path_dijkstra(
        self,
        source,
        destination
    ):
        """
        Find shortest route using Dijkstra.
        """

        analytics = RouteAnalytics()

        analytics.start()

        (
            distances,
            previous,
            visited
        ) = dijkstra(
            self.graph,
            source
        )

        analytics.stop()

        execution_time = (
            analytics.execution_time()
        )

        path = self.reconstruct_path(
            previous,
            destination
        )

        print(
            f"\n[Dijkstra Runtime] "
            f"{execution_time} µs"
        )

        return RouteResult(
            source=source,
            destination=destination,
            path=path,
            distance=distances[destination],
            algorithm="Dijkstra",
            visited_nodes=visited,
            execution_time=execution_time
        )

    def shortest_path_astar(
        self,
        source,
        destination
    ):
        """
        Find shortest route using A*.
        """

        analytics = RouteAnalytics()

        analytics.start()

        (
            path,
            distance,
            visited
        ) = astar(
            self.graph,
            source,
            destination
        )

        analytics.stop()

        execution_time = (
            analytics.execution_time()
        )

        print(
            f"\n[A* Runtime] "
            f"{execution_time} µs"
        )

        return RouteResult(
            source=source,
            destination=destination,
            path=path,
            distance=distance,
            algorithm="A*",
            visited_nodes=visited,
            execution_time=execution_time
        )