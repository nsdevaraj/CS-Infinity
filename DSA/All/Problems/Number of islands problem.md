
[Number of islands problem (LeetCode #200) - Inside code](https://youtu.be/O-6Z4Yj1sFY?si=kw0J3BakYDveQVtS)



### Problem: Number of Islands (LeetCode #200)

Given a 2D grid where:
- Each cell contains either `'1'` (land) or `'0'` (water),
- An **island** is defined as a group of adjacent land cells (horizontally or vertically connected), surrounded by water or the grid boundary,

Your task is to **count the number of distinct islands** in the grid.

#### Problem Statement

**Input**:
- `grid`: a 2D list of size $n \times m$ consisting of `'1'` (land) and `'0'` (water).

**Output**:
- Return the number of islands (distinct connected components of land cells).

#### Example

```plaintext
Input:
[
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "1"],
  ["0", "0", "0", "1", "1"],
  ["0", "0", "0", "0", "0"],
  ["1", "0", "1", "1", "1"]
]

Output: 4
Explanation: The grid contains 4 distinct islands.
```

### Approach: Breadth-First Search (BFS) with Flood Fill Algo

To solve this problem, we use the **Flood Fill** algorithm (similar to the one used for filling connected regions in images). Every time we encounter an unvisited land cell, we trigger a flood fill (or BFS) to explore the entire connected component (island) and mark all its cells as visited.

#### Algorithm Steps:
1. **Initialize**: Start by initializing a counter for islands.
2. **Grid Traversal**: Loop over each cell in the grid.
   - If the cell is land (`'1'`) and unvisited, increment the island counter and trigger a **BFS** to mark all connected land cells as visited.
3. **BFS for Flood Fill**: For each cell, we explore its neighbors (up, down, left, right) to mark all land cells of the island.
4. **Return the Island Count**: Once all cells are processed, return the total number of islands.

### Code Implementation (with comments)

```python
from typing import List
from queue import Queue

def flood_fill(grid: List[List[str]], i: int, j: int, new_color: str) -> None:
    """
    Perform BFS to mark all connected land cells as visited.
    
    :param grid: 2D grid of '1' (land) and '0' (water)
    :param i: current row index
    :param j: current column index
    :param new_color: character used to mark visited cells (e.g., '2')
    """
    n, m = len(grid), len(grid[0])
    old_color = grid[i][j]  # Original value ('1')
    
    # BFS queue initialization
    queue = Queue()
    queue.put((i, j))
    grid[i][j] = new_color  # Mark the starting cell as visited

    # Explore in 4 directions (right, left, down, up)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while not queue.empty():
        x, y = queue.get()
        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            # Check bounds and if it's unvisited land ('1')
            if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] == old_color:
                grid[next_x][next_y] = new_color  # Mark as visited
                queue.put((next_x, next_y))  # Add the new cell to the queue

def nb_islands(grid: List[List[str]]) -> int:
    """
    Count the number of islands in the given 2D grid.
    
    :param grid: 2D grid of '1' (land) and '0' (water)
    :return: number of distinct islands
    """
    if not grid:
        return 0
    
    n, m = len(grid), len(grid[0])
    island_count = 0  # To store the number of islands
    
    # Traverse every cell in the grid
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':  # Found unvisited land (new island)
                island_count += 1
                flood_fill(grid, i, j, '2')  # Mark all connected land cells as visited
    
    return island_count
```

### Time and Space Complexity

#### Time Complexity:
- **Grid Traversal**: We visit each cell exactly once, and the BFS flood fill explores all the connected cells of an island.
- The BFS exploration for one island costs **O(k)**, where **k** is the number of cells in the island. Since the total number of cells in the grid is $n \times m$, the overall time complexity is:

$$
\text{Time Complexity} = O(n \times m)
$$

#### Space Complexity:
- **Auxiliary Space**: The maximum space required by the BFS queue is proportional to the number of cells in the largest island, which can be at most $n \times m$. Hence, the space complexity is:

$$
\text{Space Complexity} = O(n \times m)
$$

### Conclusion

The BFS-based flood fill solution for the "Number of Islands" problem efficiently counts islands by marking all cells of an island as visited once detected. This approach ensures that each land cell is processed only once, providing an optimal time complexity of **O(n \* m)**.

#### Key Insights:
- **Flood Fill** is an essential algorithm for connected-component problems.
- Both the time and space complexities are linear with respect to the grid size, making this approach scalable for large grids.





---


## Number of islands

 [LeetCode #200 - Number of Islands](https://leetcode.com/problems/number-of-islands/)


#### Problem Statement:

Given a 2D grid map of `'1'`s (land) and `'0'`s (water), the goal is to count the number of distinct islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

##### Example:

```plaintext
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

---

### Approach 1: Depth-First Search (DFS)

#### Key Idea:
The basic idea is to traverse through the grid and count the number of distinct islands using DFS. When we encounter a land cell (`'1'`), we mark it as visited by changing its value to `'0'` (water) to avoid revisiting it. Then, we explore all its neighboring land cells (up, down, left, right) recursively.

#### Steps:
1. Initialize the number of islands as 0.
2. Traverse the grid, and when a land cell is encountered (`'1'`), perform a DFS to mark all the connected land cells as water (`'0'`).
3. Each time DFS is initiated, increment the count of islands.

#### DFS Code Implementation:

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(r, c):
            # If out of bounds or the cell is water ('0'), return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            # Mark this cell as visited by setting it to '0'
            grid[r][c] = '0'
            
            # Explore all 4 possible directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found an island
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
```


```python

```

#### Time Complexity:
- $O(\text{rows} \times \text{cols})$: Every cell is visited once.
  
#### Space Complexity:
- $O(\text{rows} \times \text{cols})$: Space used by the recursion stack.

---

### Approach 2: Breadth-First Search (BFS)

#### Key Idea:
The BFS approach is similar to DFS but uses a queue to explore neighboring cells level by level. Starting from a land cell (`'1'`), we enqueue it, mark it as visited by changing it to `'0'`, and then explore its neighbors iteratively.

#### BFS Code Implementation:

```python
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = '0'  # Mark as visited
            
            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'  # Mark as visited
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    bfs(r, c)
        
        return num_islands
```


```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define movement directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        # Depth-First Search (DFS) to mark visited parts of the island
        def dfs(r: int, c: int):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
                return
            
            # Mark current cell as visited by changing '1' to '0'
            grid[r][c] = '0'

            # Explore all four directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through the grid and start DFS when '1' is found (new island)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)
        
        return island_count

```


#### Time Complexity:
- $O(\text{rows} \times \text{cols})$: Every cell is visited once.
  
#### Space Complexity:
- $O(\min(\text{rows}, \text{cols}))$: The queue can grow up to the size of the smaller dimension of the grid.

---

### Approach 3: Union-Find (Disjoint Set)

#### Key Idea:
We treat each land cell (`'1'`) as a separate component and union the cells that are adjacent. At the end, the number of distinct sets will give us the number of islands.

#### Union-Find Code Implementation:

```python
from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
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
            self.count -= 1

    def set_count(self, num):
        self.count = num

    def get_count(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)
        num_islands = 0
        
        def index(r, c):
            return r * cols + c
        
        # Initial count of islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
        
        uf.set_count(num_islands)
        
        directions = [(0, 1), (1, 0)]  # Only right and down to avoid double counting
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            uf.union(index(r, c), index(nr, nc))
        
        return uf.get_count()
```

#### Time Complexity:
- $O(\text{rows} \times \text{cols})$: The grid is traversed once, and union-find operations are near constant time, thanks to path compression.

#### Space Complexity:
- $O(\text{rows} \times \text{cols})$: Space used by the Union-Find data structure.

---

### Section 2: Approaches Comparison and Test Function

#### Approaches Comparison Table

| Approach           | Time Complexity                 | Space Complexity              | Key Idea                                             |
|--------------------|----------------------------------|-------------------------------|------------------------------------------------------|
| **DFS (Recursive)** | $O(\text{rows} \times \text{cols})$ | $O(\text{rows} \times \text{cols})$ | Traverse grid and use recursion to mark visited cells.|
| **BFS (Queue)**     | $O(\text{rows} \times \text{cols})$ | $O(\min(\text{rows}, \text{cols}))$ | Uses a queue to explore level by level.               |
| **Union-Find**      | $O(\text{rows} \times \text{cols})$ | $O(\text{rows} \times \text{cols})$ | Treats each cell as a separate component and unions adjacent ones.|

---


Here is the test function with distinct test cases, checking a variety of scenarios:

```python
def test_num_islands(solution):
    test_cases = [
        {
            "grid": [
              ["1", "1", "1", "1", "0"],
              ["1", "1", "0", "1", "0"],
              ["1", "1", "0", "0", "0"],
              ["0", "0", "0", "0", "0"]
            ],
            "expected": 1
        },
        {
            "grid": [
              ["1", "1", "0", "0", "0"],
              ["1", "1", "0", "0", "0"],
              ["0", "0", "1", "0", "0"],
              ["0", "0", "0", "1", "1"]
            ],
            "expected": 3
        },
        {
            "grid": [
              ["1", "0", "0", "1", "0"],
              ["0", "0", "1", "0", "0"],
              ["1", "1", "0", "1", "1"],
              ["0", "0", "0", "0", "0"]
            ],
            "expected": 4
        },
        {
            "grid": [
              ["0", "0", "0", "0"],
              ["0", "1", "0", "0"],
              ["0", "0", "0", "0"]
            ],
            "expected": 1
        },
        {
            "grid": [
              ["0", "0", "0", "0"],
              ["0", "0", "0", "0"],
              ["0", "0", "0", "0"]
            ],
            "expected": 0
        },
        {
            "grid": [
              ["1", "0", "1", "0", "1"],
              ["0", "1", "0", "1", "0"],
              ["1", "0", "1", "0", "1"]
            ],
            "expected": 9
        },
        {
            "grid": [
              ["1", "1", "0", "1", "1"],
              ["1", "1", "0", "1", "1"],
              ["0", "0", "0", "0", "0"],
              ["1", "1", "0", "1", "1"],
              ["1", "1", "0", "1", "1"]
            ],
            "expected": 4
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        grid = test_case["grid"]
        expected = test_case["expected"]
        result = solution.numIslands(grid)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed!")
```

