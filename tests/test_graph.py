from src.graph.graph import Graph


def test_add_edge():

    graph = Graph()

    graph.add_edge(
        "A",
        "B",
        10
    )

    assert len(
        graph.get_neighbors("A")
    ) == 1