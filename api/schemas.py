from pydantic import BaseModel


class RouteRequest(BaseModel):

    city: str

    source: str

    destination: str


class RouteResponse(BaseModel):

    city: str

    algorithm: str

    source: str

    destination: str

    path: list

    distance: float

    visited_nodes: int

    execution_time: float