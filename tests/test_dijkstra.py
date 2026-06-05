from src.graph.graph import Graph
from src.graph.dijkstra import dijkstra


def test_shortest_path():

    graph = Graph()

    graph.add_edge("A", "B", 5)

    graph.add_edge("B", "C", 2)

    graph.add_edge("A", "C", 20)

    distances, _ = dijkstra(
        graph,
        "A"
    )

    assert distances["C"] == 7