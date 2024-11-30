
[Spiral matrix problem - Inside code](https://youtu.be/nHklvujUWp8)

[LeetCode #54](https://leetcode.com/problems/spiral-matrix/description/)

### Problem: Spiral Matrix (LeetCode #54)

Given an `n x m` matrix, return **all elements of the matrix in spiral order**.

#### Example 1:

**Input:**
```text
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output:**
```text
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

#### Example 2:

**Input:**
```text
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
```

**Output:**
```text
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```

### Approach 1: Simulation using Direction Change (Flood Fill Style)

#### Explanation:
We traverse the matrix in a spiral order by continuously moving in four possible directions: **right, down, left, and up**. As soon as we hit the boundary or a previously visited cell, we switch directions. To handle direction changes, we can define a `direction_map` that tells us which direction to turn next. We keep track of visited cells by marking them as `None`.

#### Code:

```python
from typing import List, Tuple

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Dimensions of the matrix
        n, m = len(matrix), len(matrix[0])
        # Starting position at top-left (0,0)
        i, j = 0, 0
        # Initial direction is towards the right (0, 1)
        delta: Tuple[int, int] = (0, 1)
        # Define direction transitions: right -> down -> left -> up
        direction_map = {
            (0, 1): (1, 0),  # right to down
            (1, 0): (0, -1), # down to left
            (0, -1): (-1, 0),# left to up
            (-1, 0): (0, 1)  # up to right
        }
        # Result array storing elements in spiral order
        spiral: List[int] = [matrix[i][j]]
        # Mark the first cell as visited
        matrix[i][j] = None
        
        while len(spiral) < n * m:
            # Calculate the next cell's position
            next_i, next_j = i + delta[0], j + delta[1]
            
            # Check if next cell is out of bounds or visited
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m or matrix[next_i][next_j] is None:
                # Change direction
                delta = direction_map[delta]
            else:
                # Move to the next cell
                i, j = next_i, next_j
                # Add the current value to the result
                spiral.append(matrix[i][j])
                # Mark the current cell as visited
                matrix[i][j] = None
        
        return spiral
```

#### Time Complexity:
- The time complexity is $O(n \times m)$ because we visit every element of the matrix exactly once.

#### Space Complexity:
- The space complexity is $O(n \times m)$ due to the storage required to hold the matrix and mark visited cells.

---

### Approach 2: Boundary Management

#### Explanation:
Instead of keeping track of visited cells, we can maintain boundaries to know when to switch direction. These boundaries will initially be at the outermost rows and columns, and as we spiral inward, we will adjust the boundaries to shrink inward.

#### Code:

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        # Defining the initial boundaries
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        result: List[int] = []
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1  # Move the top boundary down
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move the right boundary left
            
            if top <= bottom:
                # Traverse from right to left along the bottom boundary
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1  # Move the bottom boundary up
            
            if left <= right:
                # Traverse from bottom to top along the left boundary
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move the left boundary right
        
        return result
```

#### Time Complexity:
- The time complexity is $O(n \times m)$ because each element is visited exactly once.

#### Space Complexity:
- The space complexity is $O(1)$ if we don't consider the space used for the output list.

---

### Summary of Approaches

| Approach                        | Time Complexity       | Space Complexity | Explanation                                                             |
|----------------------------------|-----------------------|------------------|-------------------------------------------------------------------------|
| **Simulation (Direction Change)**| $O(n \times m)$        | $O(n \times m)$  | Traversing with direction changes, marking visited cells                |
| **Boundary Management**          | $O(n \times m)$        | $O(1)$           | Maintaining dynamic boundaries that shrink as we spiral inward           |

These two approaches offer different styles of traversal, with the second one being slightly more space efficient as it doesn't need to modify the matrix for visited cells.


