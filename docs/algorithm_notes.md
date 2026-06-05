# Algorithm Notes

## Breadth First Search (BFS)

### Purpose

Traverses all reachable nodes level-by-level.

### Time Complexity

```text
O(V + E)
```

### Space Complexity

```text
O(V)
```

### Use Cases

- Graph traversal
- Connectivity checking
- Level-order exploration

---

## Depth First Search (DFS)

### Purpose

Traverses graph depth-wise before backtracking.

### Time Complexity

```text
O(V + E)
```

### Space Complexity

```text
O(V)
```

### Use Cases

- Graph exploration
- Path discovery
- Cycle detection

---

## Dijkstra Algorithm

### Purpose

Finds the shortest path in a weighted graph with non-negative edge weights.

### Data Structure Used

```text
Priority Queue (Min Heap)
```

### Time Complexity

```text
O((V + E) log V)
```

### Space Complexity

```text
O(V)
```

### Advantages

- Guarantees optimal shortest path
- Works on weighted graphs
- Widely used in routing systems

### Disadvantages

- Explores more nodes
- Can be slower on large graphs

---

## A* Search Algorithm

### Purpose

Finds the shortest path using a heuristic function.

### Evaluation Function

```text
f(n) = g(n) + h(n)
```

Where:

```text
g(n) = Actual path cost from source
h(n) = Estimated cost to destination
```

### Heuristic Used

```text
Euclidean Distance
```

### Time Complexity

```text
O((V + E) log V)
```

### Space Complexity

```text
O(V)
```

### Advantages

- Faster than Dijkstra
- Visits fewer nodes
- Suitable for navigation systems

### Disadvantages

- Requires coordinates
- Depends on heuristic quality

---

## Algorithm Comparison

| Feature | Dijkstra | A* |
|----------|----------|-----|
| Shortest Path | Yes | Yes |
| Uses Heuristic | No | Yes |
| Faster Search | No | Yes |
| Optimal Result | Yes | Yes |
| Real Navigation Systems | Sometimes | Yes |

---

## Algorithms Used in Project

### Traversal Algorithms

- Breadth First Search (BFS)
- Depth First Search (DFS)

### Shortest Path Algorithms

- Dijkstra Algorithm
- A* Search Algorithm

---

## Conclusion

The Intelligent Route Planner uses graph traversal and shortest path algorithms to efficiently determine optimal routes across multiple city datasets. Dijkstra guarantees the shortest path, while A* improves efficiency through heuristic-based search.