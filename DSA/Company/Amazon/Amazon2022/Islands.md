



```markdown
# Number of Islands

## Problem Statement

Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

## Examples

### Example 1

**Input:**

```plaintext
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```

**Output:**

```plaintext
1
```

### Example 2

**Input:**

```plaintext
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

**Output:**

```plaintext
3
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is '0' or '1'.


### Soln



```sudolang
FUNCTION islands_1(board):
    INITIALIZE visited_pts AS empty set
    INITIALIZE island_count AS 0
    SET row_limit TO number of rows in board
    SET col_limit TO number of columns in board

    FUNCTION visit_neighbours(pt):
        UNPACK pt INTO p1, p2

        IF p1 or p2 is out of bounds OR board[p1][p2] is '0' OR pt is in visited_pts THEN
            RETURN

        ADD pt to visited_pts

        DEFINE neighbours AS list of adjacent coordinates:
            (p1 - 1, p2)  // Up
            (p1, p2 + 1)  // Right
            (p1 + 1, p2)  // Down
            (p1, p2 - 1)  // Left

        FOR each neighbour IN neighbours DO
            CALL visit_neighbours(neighbour)

    FOR i FROM 0 TO row_limit - 1 DO
        FOR j FROM 0 TO col_limit - 1 DO
            SET pt TO (i, j)
            SET pt_value TO board[i][j]

            IF pt is in visited_pts THEN
                CONTINUE

            IF pt_value is '1' THEN
                INCREMENT island_count
                CALL visit_neighbours(pt)

    RETURN island_count


```


![[islands.py]]

{
to check
from chatGPT


Here are several different approaches to solve the "Number of Islands" problem:

### 1. Depth-First Search (DFS)

**Description**: Use DFS to explore each land cell and mark all connected land cells as visited.

**Implementation Steps**:
- Iterate through each cell in the grid.
- When a '1' (land) is found, increment the island count and start a DFS from that cell to mark all connected land cells (change '1's to '0's).
- Continue until all cells have been processed.

**Complexity**:
- Time: O(m * n), where m is the number of rows and n is the number of columns.
- Space: O(m * n) in the worst case for the recursion stack.

### 2. Breadth-First Search (BFS)

**Description**: Similar to DFS, but using BFS to explore the grid iteratively using a queue.

**Implementation Steps**:
- Iterate through the grid and start a BFS when a '1' is found.
- Use a queue to explore all connected land cells, marking them as visited.
- Count the islands as you perform the BFS.

**Complexity**:
- Time: O(m * n).
- Space: O(min(m, n)) for the queue.

### 3. Union-Find (Disjoint Set Union)

**Description**: Use the Union-Find data structure to keep track of connected components in the grid.

**Implementation Steps**:
- Treat each cell as a node in a graph.
- For each '1' in the grid, connect it to its neighboring land cells using the union operation.
- At the end, count the number of unique roots to determine the number of islands.

**Complexity**:
- Time: O(m * n * α(m * n)), where α is the inverse Ackermann function (very slow-growing).
- Space: O(m * n) for the parent and rank arrays.

### 4. Iterative Flood Fill

**Description**: Implement a flood fill algorithm iteratively, similar to how it is done in paint bucket tools in graphics applications.

**Implementation Steps**:
- For each cell, if it's a '1', perform an iterative flood fill using a stack or queue to mark all connected land cells.
- Increment the island count each time a new flood fill starts.

**Complexity**:
- Time: O(m * n).
- Space: O(min(m, n)) for the stack/queue.

### 5. Matrix Traversal with Directions

**Description**: Use an explicit stack or queue to handle traversal and visit neighboring cells in a predefined order.

**Implementation Steps**:
- Define possible movements (up, down, left, right).
- For each unvisited '1', use a stack/queue to traverse and mark all connected cells.

**Complexity**:
- Time: O(m * n).
- Space: O(m * n) in the worst case for the stack/queue.

### 6. Recursive Backtracking

**Description**: Use backtracking to explore each land cell and its neighbors.

**Implementation Steps**:
- Start from a '1', recursively visit all connected '1's, and backtrack to mark them as visited.

**Complexity**:
- Time: O(m * n).
- Space: O(m * n) for the recursion stack.

### Summary

- **DFS and BFS** are the most common approaches, offering a straightforward implementation and clear logic.
- **Union-Find** is efficient for larger grids and provides a different perspective on connectivity.
- **Flood fill** is useful for visualizing the problem and can be efficient with the right data structure.
- The choice of approach may depend on the specific constraints and requirements of the problem (e.g., memory limitations, maximum grid size).


soln:

Here are implementations for each of the approaches to solve the "Number of Islands" problem in Python:

### 1. Depth-First Search (DFS)

```python
def numIslandsDFS(grid):
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark as visited
        # Explore all directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count
```

### 2. Breadth-First Search (BFS)

```python
from collections import deque

def numIslandsBFS(grid):
    if not grid:
        return 0

    def bfs(i, j):
        queue = deque([(i, j)])
        grid[i][j] = '0'  # Mark as visited
        while queue:
            x, y = queue.popleft()
            # Explore all directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'  # Mark as visited
                    queue.append((nx, ny))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                bfs(i, j)

    return count
```

### 3. Union-Find (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def numIslandsUnionFind(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    uf = UnionFind(rows * cols)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                if i > 0 and grid[i - 1][j] == '1':
                    uf.union(i * cols + j, (i - 1) * cols + j)
                if j > 0 and grid[i][j - 1] == '1':
                    uf.union(i * cols + j, i * cols + (j - 1))

    islands = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                islands.add(uf.find(i * cols + j))

    return len(islands)
```

### 4. Iterative Flood Fill

```python
def numIslandsFloodFill(grid):
    if not grid:
        return 0

    def flood_fill(i, j):
        stack = [(i, j)]
        grid[i][j] = '0'  # Mark as visited
        while stack:
            x, y = stack.pop()
            # Explore all directions
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'  # Mark as visited
                    stack.append((nx, ny))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                flood_fill(i, j)

    return count
```

### 5. Matrix Traversal with Directions

```python
def numIslandsDirections(grid):
    if not grid:
        return 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def traverse(i, j):
        stack = [(i, j)]
        grid[i][j] = '0'  # Mark as visited
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'  # Mark as visited
                    stack.append((nx, ny))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                traverse(i, j)

    return count
```

### 6. Recursive Backtracking

```python
def numIslandsBacktracking(grid):
    if not grid:
        return 0

    def backtrack(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark as visited
        # Explore all directions
        backtrack(i + 1, j)
        backtrack(i - 1, j)
        backtrack(i, j + 1)
        backtrack(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                backtrack(i, j)

    return count
```

### Summary
- Each approach effectively counts the number of islands in the grid.
- You can choose the one that best fits your needs based on readability, performance, and ease of implementation. The DFS and BFS methods are often the most straightforward and efficient for this problem.



}



for more: check 

Islands: https://leetcode.com/problems/number-of-islands/description/








