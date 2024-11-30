

[Capture surrounded regions problem](https://youtu.be/WAdqmywK_Ms)

[LeetCode 130](https://leetcode.com/problems/surrounded-regions/description/)


### Problem: Capture Surrounded Regions (LeetCode #130)

Given an `n x m` matrix `board` containing 'X' and 'O', capture all regions that are surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region. A region is 4-directionally surrounded if no 'O' in that region touches the border.

### Problem Statement:
- **Input:** A 2D matrix `board` where:
  - 'X' represents water.
  - 'O' represents land.
- **Output:** Modify the matrix in place to capture all surrounded regions (convert 'O' cells to 'X' if they are fully surrounded by 'X').

### Example:

#### Input:
```python
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
```

#### Output:
```python
# The matrix after capturing surrounded regions
[
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X']
]
```

### Approach 1: Flood Fill (First Attempt - Not Efficient Enough)
The first approach is inspired by the "Number of Islands" problem, where we use flood fill (BFS/DFS) to identify regions. Here, we mark regions as surrounded or not using a hash map, but this approach turns out to be inefficient for large boards.

#### Key Idea:
1. Traverse the entire board.
2. Identify land cells ('O') and perform a flood fill to mark whether the region is surrounded.
3. Capture the surrounded regions by converting 'O's to 'X's.
4. Reset non-surrounded regions back to 'O'.


#### Time Complexity:
- **Time:** $O(n \times m)$, as we traverse all cells in the matrix.
- **Space:** $O(n \times m)$ for flood fill.

This approach isn't optimal for larger matrices as it requires multiple passes over the board.

#### Code (Initial Attempt):
```python
from typing import List
from queue import Queue

def flood_fill(board: List[List[str]], i: int, j: int):
    """Perform BFS flood fill to mark the region starting from (i, j)."""
    n, m = len(board), len(board[0])
    queue = Queue()
    queue.put((i, j))
    board[i][j] = '-'  # Mark as visited with a special character
    while not queue.empty():
        x, y = queue.get()
        for adj_x, adj_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= adj_x < n and 0 <= adj_y < m and board[adj_x][adj_y] == 'O':
                queue.put((adj_x, adj_y))
                board[adj_x][adj_y] = '-'

def capture_surrounded(board: List[List[str]]):
    n, m = len(board), len(board[0])
    # Traverse the borders first
    for j in range(m):
        if board[0][j] == 'O': flood_fill(board, 0, j)   # First row
        if board[n-1][j] == 'O': flood_fill(board, n-1, j)  # Last row
    for i in range(1, n-1):
        if board[i][0] == 'O': flood_fill(board, i, 0)   # First column
        if board[i][m-1] == 'O': flood_fill(board, i, m-1)  # Last column
    
    # Convert the board
    for i in range(n):
        for j in range(m):
            if board[i][j] == '-':  # Restore un-captured regions
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'  # Capture surrounded regions

# Example board
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
capture_surrounded(board)
print(*board, sep='\n')
```

### Approach 2: Optimized Solution (BFS from Borders)
To improve the time complexity, we shift our focus. Instead of searching for surrounded regions, we focus on identifying non-surrounded regions from the border. By doing this, we can optimize the number of cells we traverse.

#### Key Idea:
1. **Flood fill from the borders:** Start from all 'O's on the borders and mark them as part of non-surrounded regions.
2. **Capture remaining regions:** After marking the border-connected regions, any 'O' left in the matrix must be fully surrounded, so we flip it to 'X'.

#### Time Complexity:
- **Time:** $O(n \times m)$, as we visit each cell at most once.
- **Space:** $O(n \times m)$, due to the space required by BFS (queue).

This approach ensures that we minimize the number of cells we process, focusing only on the border regions first.

#### Code (Optimized BFS Solution):
```python
from typing import List
from queue import Queue

def flood_fill(board: List[List[str]], i: int, j: int):
    """Flood fill from (i, j) to mark non-surrounded regions."""
    n, m = len(board)
    queue = Queue()
    queue.put((i, j))
    board[i][j] = '-'  # Mark with special character to indicate non-surrounded region
    while not queue.empty():
        x, y = queue.get()
        for adj_x, adj_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= adj_x < n and 0 <= adj_y < m and board[adj_x][adj_y] == 'O':
                queue.put((adj_x, adj_y))
                board[adj_x][adj_y] = '-'

def capture_surrounded(board: List[List[str]]):
    n, m = len(board)
    # Step 1: Flood fill from border 'O' cells
    for j in range(m):
        if board[0][j] == 'O': flood_fill(board, 0, j)  # First row
        if board[n-1][j] == 'O': flood_fill(board, n-1, j)  # Last row
    for i in range(1, n-1):
        if board[i][0] == 'O': flood_fill(board, i, 0)  # First column
        if board[i][m-1] == 'O': flood_fill(board, i, m-1)  # Last column
    
    # Step 2: Convert captured and non-captured regions
    for i in range(n):
        for j in range(m):
            if board[i][j] == '-':  # Restore non-surrounded regions
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'  # Capture surrounded regions

# Example board
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
capture_surrounded(board)
print(*board, sep='\n')
```

### Summary of Approaches:

| Approach                | Time Complexity     | Space Complexity  | Notes                                                    |
|-------------------------|---------------------|-------------------|----------------------------------------------------------|
| Flood Fill (Initial)     | $O(n \times m)$     | $O(n \times m)$   | Traverses all regions and marks surrounded regions.       |
| BFS from Borders (Optimized) | $O(n \times m)$     | $O(n \times m)$   | Starts from border and identifies non-surrounded regions. |

The optimized approach is more efficient for larger matrices, as it minimizes unnecessary checks in the middle of the board, focusing only on regions that connect to the border.

### Time and Space Complexity (Final Solution):
- **Time Complexity:** $O(n \times m)$, where $n$ is the number of rows and $m$ is the number of columns, because each cell is processed at most once.
- **Space Complexity:** $O(n \times m)$, for storing the queue used in BFS.

The optimized solution leverages the fact that any region touching the border cannot be surrounded, thus only needing to traverse border regions initially.




