import math
import heapq
import json

# Load coordinates used by A* heuristic
with open("data/bengaluru_coordinates.json", "r") as file:
    COORDS = json.load(file)

def heuristic(node, destination):
    """
    Euclidean Distance Heuristic: sqrt((x1-x2)^2 + (y1-y2)^2)
    """
    if node not in COORDS or destination not in COORDS:
        return 0

    x1, y1 = COORDS[node]
    x2, y2 = COORDS[destination]
    
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def astar(graph, start, destination):
    """
    A* Shortest Path Algorithm
    """
    open_set = [(0, start)]
    came_from = {}
    
    # Initialize scores
    g_score = {node: float("inf") for node in graph.get_nodes()}
    g_score[start] = 0
    
    f_score = {node: float("inf") for node in graph.get_nodes()}
    f_score[start] = heuristic(start, destination)
    
    visited_count = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        visited_count += 1

        if current == destination:
            return (
                reconstruct_path(came_from, current),
                g_score[destination],
                visited_count
            )

        for neighbor, weight in graph.get_neighbors(current):
            tentative_g_score = g_score[current] + weight
            
            if tentative_g_score < g_score[neighbor]:
                # Record path
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, destination)
                
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, float("inf"), visited_count