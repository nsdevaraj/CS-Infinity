
[Virus spread problem - Inside code](https://youtu.be/viv6_a_epjs?si=0AD6wxasnllz2keo)


### Problem: Virus Spread in a Grid

**Problem Statement:**

You are given a 2D grid of cells, where each cell is either infected (`1`) or uninfected (`0`). Every night, the virus spreads from infected cells to their 4-directionally adjacent uninfected cells. To stop the virus from spreading, you can place walls between infected and uninfected cells, but you can only surround one infected area (a connected group of infected cells) per day. The goal is to surround the most dangerous area—the one that will infect the most uninfected cells in the next day—and count the total number of walls used to completely stop the spread of the virus.

**Input:**
- A grid of size `n x m` with values `1` (infected) and `0` (uninfected).

**Output:**
- The total number of walls used to completely stop the virus.

**Example:**

```text
Grid:
[[0, 1, 0, 0, 0, 0],
 [1, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 1]]

Output: 50 walls
```

---

### Approaches

#### 1. **Flood Fill to Detect Infected Areas**

This approach treats infected areas like islands (as in the "Number of Islands" problem). We perform a flood-fill (either BFS or DFS) to find all connected infected cells and treat each group as a separate infected area.

- **Steps**:
  1. Traverse the grid, and every time we find an unvisited infected cell (`1`), we perform flood-fill to find the entire infected area.
  2. Mark cells as visited (`2`).
  3. Return a list of infected areas, where each area is a list of infected cell coordinates.

- **Code**:

```python
from queue import Queue
from typing import List, Tuple

def flood_fill(grid: List[List[int]], i: int, j: int, areas: List[List[Tuple[int, int]]]) -> None:
    """Flood-fill to find all infected areas."""
    n, m = len(grid), len(grid[0])
    areas.append([(i, j)])  # Add a new area
    queue = Queue()
    queue.put((i, j))
    grid[i][j] = 2  # Mark visited
    
    while not queue.empty():
        i, j = queue.get()
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 1:
                areas[-1].append((next_i, next_j))
                grid[next_i][next_j] = 2  # Mark visited
                queue.put((next_i, next_j))

def get_areas(grid: List[List[int]]) -> List[List[Tuple[int, int]]]:
    """Returns a list of infected areas."""
    n, m = len(grid), len(grid[0])
    areas = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                flood_fill(grid, i, j, areas)
    
    # Reset visited cells (2) back to infected (1)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 1
    
    return areas
```

- **Time Complexity**: $O(n \times m)$, since we traverse each cell at most once.
- **Space Complexity**: $O(n \times m)$, for storing areas and the grid itself.

---

#### 2. **Calculate Danger of Each Infected Area**

The "danger" of an infected area is defined as the number of uninfected cells it can spread to in the next day. For each cell in the infected area, check its 4 neighbors, and count how many of them are uninfected (`0`).

- **Steps**:
  1. For each infected area, count the number of adjacent uninfected cells.
  2. Return the count as the "danger" of the area.

- **Code**:

```python
def danger(grid: List[List[int]], area: List[Tuple[int, int]], walls: set) -> int:
    """Calculates the danger of an infected area based on how many cells it can infect next."""
    n, m = len(grid), len(grid[0])
    affected = set()  # To avoid duplicates
    
    for cell in area:
        i, j = cell
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 0:
                affected.add((next_i, next_j))
    
    return len(affected)
```

- **Time Complexity**: $O(n \times m)$, since we check the neighbors of each infected cell.
- **Space Complexity**: $O(n \times m)$, for storing the affected cells.

---

#### 3. **Surround the Most Dangerous Area with Walls**

Once we identify the most dangerous area, we need to place walls around its uninfected neighbors to stop the spread. Walls are placed on the boundary between infected and uninfected cells.

- **Code**:

```python
def put_walls(grid: List[List[int]], area: List[Tuple[int, int]], walls: set) -> None:
    """Place walls around an infected area to stop the virus spread."""
    n, m = len(grid), len(grid[0])
    for cell in area:
        i, j = cell
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 0:
                walls.add(((i, j), (next_i, next_j)))  # Add wall between infected and uninfected
```

- **Time Complexity**: $O(n \times m)$, similar to calculating danger.
- **Space Complexity**: $O(n \times m)$, for storing walls.

---

#### 4. **Spread the Virus**

After placing walls, we simulate the spread of the virus by infecting adjacent uninfected cells if there's no wall between them.

- **Code**:

```python
def spread(grid: List[List[int]], walls: set, areas: List[List[Tuple[int, int]]]) -> bool:
    """Simulate virus spread and return whether the grid changed."""
    n, m = len(grid), len(grid[0])
    changed = False
    for area in areas:
        for i, j in area:
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 0:
                    if ((i, j), (next_i, next_j)) not in walls:
                        grid[next_i][next_j] = 1
                        changed = True
    return changed
```

- **Time Complexity**: $O(n \times m)$.
- **Space Complexity**: $O(1)$, no additional space beyond the grid.

---

#### 5. **Final Solution: Counting the Walls**

This function combines the previous parts to repeatedly find the most dangerous area, surround it with walls, and spread the virus until the spread stops.

- **Code**:

```python
def nbwalls(grid: List[List[int]]) -> int:
    """Returns the number of walls needed to contain the virus spread."""
    walls = set()
    spreading = True
    total_walls = 0
    
    while spreading:
        areas = get_areas(grid)
        if not areas:
            break
        most_dangerous = max(areas, key=lambda area: danger(grid, area, walls))
        put_walls(grid, most_dangerous, walls)
        total_walls += len(walls)  # Update the total number of walls
        spreading = spread(grid, walls, areas)
    
    return total_walls
```

- **Time Complexity**: $O(n \times m \times d)$, where `d` is the number of days the virus spreads.
- **Space Complexity**: $O(n \times m)$.

---


```python
from queue import Queue

def flood_fill(grid, i, j, areas):
    n, m = len(grid), len(grid[0])
    areas.append([(i, j)])
    queue = Queue()
    queue.put((i, j))
    grid[i][j] = 2
    while not queue.empty():
        i, j = queue.get()
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 1:
                areas[-1].append((next_i, next_j))
                grid[next_i][next_j] = 2
                queue.put((next_i, next_j))


def get_areas(grid):
    n, m = len(grid), len(grid[0])
    areas = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                flood_fill(grid, i, j, areas)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 1
    return areas


def spread(grid, walls, areas):
    n, m = len(grid), len(grid[0])
    changed = False
    for area in areas:
        for cell in area:
            i, j = cell
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i, next_j = i+direction[0], j+direction[1]
                if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 0 and ((i, j), (next_i, next_j)) not in walls:
                    grid[next_i][next_j] = 1
                    changed = True
    return changed


def put_walls(grid, area, walls):
    n, m = len(grid), len(grid[0])
    for cell in area:
        i, j = cell
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = i+direction[0], j+direction[1]
            if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 0 and ((i, j), (next_i, next_j)) not in walls:
                walls.add(((i, j), (next_i, next_j)))

                
def danger(grid, area, walls):
    n, m = len(grid), len(grid[0])
    affected = set()
    for cell in area:
        i, j = cell
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i, next_j = i+direction[0], j+direction[1]
            if 0 <= next_i < n and 0 <= next_j < m and grid[next_i][next_j] == 0 and ((i, j), (next_i, next_j)) not in walls:
                affected.add((next_i, next_j))
    return len(affected)


def nbwalls(grid):
    walls = set()
    spreading = True
    while spreading:
        areas = get_areas(grid)
        most_dangerous = max(areas, key=lambda area: danger(grid, area, walls), default=[])
        put_walls(grid, most_dangerous, walls)
        spreading = spread(grid, walls, areas)
    return len(walls)

```
### Summary of Approaches

| Approach                          | Time Complexity         | Space Complexity |
|------------------------------------|-------------------------|------------------|
| Flood Fill (Infected Areas)        | $O(n \times m)$          | $O(n \times m)$  |
| Danger Calculation                 | $O(n \times m)$          | $O(n \times m)$  |
| Placing Walls Around the Area      | $O(n \times m)$          | $O(n \times m)$  |
| Virus Spread Simulation            | $O(n \times m)$          | $O(1)$           |
| Total Solution (Iterative Process) | $O(n \times m \times d)$ | $O(n \times m)$  |

Where:
- \( n \times m \) represents the dimensions of the grid.
- \( d \) represents the number of days until the virus spread is stopped.

---

### Final Thoughts

The key to solving this problem is repeatedly identifying the most dangerous infected area (i.e., the area that will infect the most uninfected cells), surrounding it with walls, and then simulating the virus spread for the remaining infected areas. This process continues until the virus can no longer spread, with the total number of walls used being the final answer.

By optimizing the flood-fill and wall placement process, this approach efficiently handles large grids while ensuring that all necessary walls are counted.





