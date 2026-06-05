from dataclasses import dataclass
from typing import List


@dataclass
class RouteResult:
    """
    Stores route planning results.
    """

    source: str

    destination: str

    path: List[str]

    distance: float

    algorithm: str

    visited_nodes: int

    execution_time: float = 0.0