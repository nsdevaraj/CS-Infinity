

[An interesting dynamic programming problem (Triangle problem) - Inside code](https://youtu.be/adHbfFYKCNs?si=DQJcDRX-TgIQ9Vwa)

## Solving the Triangle Problem with Recursion and Dynamic Programming

### Problem Statement:
Given a triangle represented by a 2D array, find the minimum path sum from the top to the bottom. Each step you may move to adjacent numbers on the row below. 

#### Example:
Consider the following triangle:
```
     2
    3 4
   6 5 7
  4 1 8 3
```
The minimum path sum is `11`, which we can achieve by taking the path: `2 → 3 → 5 → 1`.

### Explanation:

A path in this problem is defined as a series of adjacent cells starting from the top row and moving to the bottom. We want to find the path that yields the smallest sum of values from the top to the bottom of the triangle.

#### 1. Greedy Approach (Why it Fails)
A greedy approach would try to take the smaller of the two adjacent cells at each step. For example:
```
At 2 → take 3 (smaller than 4) 
At 3 → take 6 (smaller than 5) 
At 6 → take 4 (smaller than 1)
```
But this would lead to a total sum of `2 + 3 + 6 + 4 = 15`, which is not the minimum sum (`11`).

#### The reason this approach fails is that choosing the local minimum at each step doesn't guarantee the global minimum, as smaller choices might lead to larger sums later. Therefore, we need a more robust method.

---

### Recursive Solution

In the recursive approach, we explore all possible paths and choose the one with the minimum sum.

#### Recursive Logic:
At each cell `triangle[i][j]`, you can move to the two adjacent cells in the next row: `triangle[i+1][j]` or `triangle[i+1][j+1]`. Therefore, the minimum path sum at any cell is the value of the current cell plus the minimum path sum of its two children.

#### Base Case:
When you reach the last row, there are no more cells to move to, so you just return the value of the current cell.

#### Code:

```python
from typing import List

# Recursive solution to find minimum path sum
def minPathSumRec(triangle: List[List[int]], i: int = 0, j: int = 0) -> int:
    # Base case: last row, return the value of the current cell
    if i == len(triangle) - 1:
        return triangle[i][j]
    # Recursive case: take the current value and add the minimum path sum from the next row
    else:
        return triangle[i][j] + min(
            minPathSumRec(triangle, i + 1, j), 
            minPathSumRec(triangle, i + 1, j + 1)
        )
```

#### Time Complexity:
- Each recursive call splits into two, so the time complexity is exponential: $O(2^n)$, where $n$ is the number of rows.

#### Space Complexity:
- Since we are storing one recursive call for each row in the call stack, the space complexity is $O(n)$.

---

### Dynamic Programming Solution (2D Array)

The dynamic programming approach avoids recalculating overlapping subproblems by storing the minimum path sum for each cell in a 2D array.

#### DP Logic:
We start by filling the base case (last row), where the minimum path sum is just the value of each cell. Then, we move upwards, filling each cell by taking the value of the cell plus the minimum of its two adjacent cells from the row below.

#### Code:

```python
from typing import List

# DP solution using a 2D array
def minPathSumDP(triangle: List[List[int]]) -> int:
    # Create a dp array with the same dimensions as the triangle
    dp = [[0] * len(row) for row in triangle]
    
    # Initialize the last row of dp with the last row of the triangle
    for j in range(len(triangle[-1])):
        dp[-1][j] = triangle[-1][j]
    
    # Bottom-up calculation of the minimum path sum
    for i in range(len(triangle) - 2, -1, -1):  # Start from the second last row
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
    
    # The result will be in the top cell
    return dp[0][0]
```

#### Time Complexity:
- We visit every cell once, and there are $n(n+1)/2$ cells, where $n$ is the number of rows. Hence, the time complexity is $O(n^2)$.

#### Space Complexity:
- We use a 2D array to store the results, so the space complexity is also $O(n^2)$.

---

### Space-Optimized Dynamic Programming Solution (1D Array)

In the space-optimized DP approach, we observe that we only need to keep track of the current row and the row below it, rather than maintaining the entire triangle.

#### Space-Optimized DP Logic:
We maintain two arrays: one for the current row (`dp`) and one for the previous row (`prevDp`). We update these arrays as we move upwards through the triangle, calculating the minimum path sum row by row.

#### Code:

```python
from typing import List

# Space-optimized DP solution
def minPathSumOptimized(triangle: List[List[int]]) -> int:
    # Initialize dp as the last row of the triangle
    dp = triangle[-1][:]
    
    # Traverse the triangle from the second last row to the top
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Update dp[j] to store the minimum path sum for the current cell
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    
    # The result will be the minimum path sum from the top
    return dp[0]
```

#### Time Complexity:
- Like the 2D DP solution, we visit every cell once, so the time complexity remains $O(n^2)$.

#### Space Complexity:
- We now only store two rows (current and previous), reducing the space complexity to $O(n)$.

---

### Summary of Solutions:
1. **Recursive Solution:**
   - Time Complexity: $O(2^n)$
   - Space Complexity: $O(n)$

2. **Dynamic Programming (2D Array):**
   - Time Complexity: $O(n^2)$
   - Space Complexity: $O(n^2)$

3. **Space-Optimized DP (1D Array):**
   - Time Complexity: $O(n^2)$
   - Space Complexity: $O(n)$

Each approach provides insight into how we can improve performance by optimizing time and space. The space-optimized DP solution is the most efficient for this problem.

---

If you enjoyed this breakdown of the "Triangle" problem, make sure to subscribe to the channel, leave a comment, and check out the links for more problem-solving guides!





