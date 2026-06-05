from fastapi import FastAPI, HTTPException

from src.utils.data_loader import load_graph
from src.route_planner import RoutePlanner

from src.visualization.visualizer import (
    draw_shortest_path
)

from src.reports.pdf_generator import (
    generate_pdf_report
)

from src.reports.report_generator import (
    generate_text_report
)

from api.schemas import RouteRequest

app = FastAPI(
    title="Intelligent Route Planner API",
    version="3.0.0",
    description="Multi-City Route Optimization API"
)

# --------------------------------------------------
# CONFIG & HELPERS
# --------------------------------------------------

CITY_DATASETS = {
    "Sample City": "data/city_graph.json",
    "Bengaluru": "data/bengaluru_graph.json"
}


def get_planner(city: str):

    if city not in CITY_DATASETS:

        raise HTTPException(
            status_code=400,
            detail=f"City '{city}' not found"
        )

    graph = load_graph(
        CITY_DATASETS[city]
    )

    return RoutePlanner(graph), graph


def execute_and_report(
        planner,
        graph,
        request,
        algorithm_type
):

    # Validate nodes

    if (
        request.source not in graph.get_nodes()
        or
        request.destination not in graph.get_nodes()
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid source or destination"
        )

    # Run selected algorithm

    method = getattr(
        planner,
        f"shortest_path_{algorithm_type}"
    )

    result = method(
        request.source,
        request.destination
    )

    # ------------------------------------------
    # Generate Outputs
    # ------------------------------------------

    draw_shortest_path(
        graph,
        result.path,
        "outputs/optimized_route.png"
    )

    generate_text_report(
        result,
        "outputs/route_report.txt"
    )

    generate_pdf_report(
        result,
        "outputs/route_report.pdf"
    )

    # ------------------------------------------
    # API Response
    # ------------------------------------------

    return {

        "city":
        request.city,

        "algorithm":
        result.algorithm,

        "source":
        result.source,

        "destination":
        result.destination,

        "path":
        result.path,

        "distance":
        result.distance,

        "visited_nodes":
        result.visited_nodes,

        "execution_time":
        result.execution_time
    }


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():

    return {

        "message":
        "Intelligent Route Planner API Running",

        "version":
        "3.0.0"
    }


# --------------------------------------------------
# CITIES
# --------------------------------------------------

@app.get("/cities")
def cities():

    return {

        "cities":
        list(CITY_DATASETS.keys())
    }


# --------------------------------------------------
# BACKWARD COMPATIBILITY
# --------------------------------------------------

@app.get("/locations")
def default_locations():

    graph = load_graph(
        "data/city_graph.json"
    )

    return {

        "locations":
        graph.get_nodes()
    }


# --------------------------------------------------
# LOCATIONS BY CITY
# --------------------------------------------------

@app.get("/locations/{city}")
def locations(city: str):

    _, graph = get_planner(city)

    return {

        "city":
        city,

        "locations":
        graph.get_nodes()
    }


# --------------------------------------------------
# DIJKSTRA
# --------------------------------------------------

@app.post("/dijkstra")
def dijkstra_route(
        request: RouteRequest
):

    planner, graph = get_planner(
        request.city
    )

    return execute_and_report(
        planner,
        graph,
        request,
        "dijkstra"
    )


# --------------------------------------------------
# A*
# --------------------------------------------------

@app.post("/astar")
def astar_route(
        request: RouteRequest
):

    planner, graph = get_planner(
        request.city
    )

    return execute_and_report(
        planner,
        graph,
        request,
        "astar"
    )


# --------------------------------------------------
# HEALTH
# --------------------------------------------------

@app.get("/health")
def health():

    return {

        "status":
        "healthy",

        "service":
        "Route Planner API"
    }