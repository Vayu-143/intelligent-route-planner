# Intelligent Route Planner Architecture

## Overview

The Intelligent Route Planner is a graph-based route optimization system that finds the shortest path between locations using Dijkstra and A* algorithms.

The project follows a modular architecture with separate layers for:

- Data Management
- Graph Algorithms
- Route Planning
- API Services
- User Interface
- Visualization
- Reporting

---

## System Architecture

```text
Streamlit UI
      |
      v
 FastAPI Backend
      |
      v
 Route Planner
      |
      +------------------+
      |                  |
      v                  v
 Dijkstra            A*
      |
      v
 Graph Structure
      |
      v
 JSON Dataset
```

---

## Project Structure

```text
Intelligent-Route-Planner
│
├── api/
│   ├── app.py
│   └── schemas.py
│
├── data/
│   ├── city_graph.json
│   ├── bengaluru_graph.json
│   ├── bengaluru_coordinates.json
│   └── sample_coordinates.json
│
├── src/
│   ├── analytics/
│   ├── graph/
│   ├── models/
│   ├── reports/
│   ├── utils/
│   └── visualization/
│
├── outputs/
│
├── tests/
│
├── app.py
│
└── main.py
```

---

## Components

### Graph Layer

Responsible for:

- Node storage
- Edge storage
- Neighbor lookup

File:

```text
src/graph/graph.py
```

---

### Algorithm Layer

Implements:

- BFS
- DFS
- Dijkstra
- A*

Files:

```text
src/graph/
```

---

### Route Planner

Acts as the central controller.

Responsibilities:

- Route calculation
- Runtime measurement
- Result generation

File:

```text
src/route_planner.py
```

---

### FastAPI Backend

Provides REST APIs.

Endpoints:

```text
GET /cities
GET /locations/{city}
POST /dijkstra
POST /astar
GET /health
```

---

### Streamlit Frontend

Provides:

- Dataset selection
- Route search
- Analytics dashboard
- Route visualization
- PDF download

---

### Reporting

Generates:

- PDF reports
- Text reports

---

## Future Enhancements

- Traffic simulation
- Real-time maps
- GPS integration
- Cloud deployment
- User authentication

---

## Conclusion

The Intelligent Route Planner combines graph theory, shortest path algorithms, API development, and interactive visualization into a complete route optimization platform.