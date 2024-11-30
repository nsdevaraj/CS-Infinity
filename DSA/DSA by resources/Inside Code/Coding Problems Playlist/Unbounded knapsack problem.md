
[Unbounded knapsack problem - Inside code](https://youtu.be/jlCJqgSgXI4?si=hO5UwpQip5oIoHGr)



### Unbounded Knapsack Problem

#### Problem Statement:
Given $n$ items, each with a value $v[i]$ and a weight $w[i]$, and a knapsack with a capacity $k$. You are tasked to find the maximum value that can be obtained by selecting items such that the total weight does not exceed $k$. Unlike the 0-1 knapsack problem, in this case, you can take an item multiple times. This is the key difference: you can take any item $i$ as many times as you want (including 0), i.e., $x[i] \geq 0$.

The goal is to maximize the total value without exceeding the weight capacity.

### Objective:
Maximize the total value by selecting items such that:

$$
\sum_{i=1}^{n} v[i] \cdot x[i]
$$

subject to:

$$
\sum_{i=1}^{n} w[i] \cdot x[i] \leq k
$$

Where $x[i] \geq 0$ can be any non-negative integer (as you can take items multiple times).

### Approach 1: Recursive Solution (Backtracking)

1. **Concept**: This approach is similar to the 0-1 knapsack problem. At each step, we decide to either take an item (and remain at the current item) or move on to the next one.



Here is the code for the Unbounded Knapsack problem with comments:

```python
def knapsack(values: list[int], weights: list[int], k: int, i: int = 0) -> int:
    # If the remaining capacity is less than 0, this path is not feasible
    if k < 0:
        return float('-inf')  # Return negative infinity to indicate an invalid solution
    
    # If we have considered all items, return 0 as no more items can be added
    if i == len(values):
        return 0
    
    # Recursively explore two possibilities:
    # 1. Exclude the current item and move to the next one
    # 2. Include the current item (unbounded, so we don't move to the next item, we can take it again)
    return max(
        knapsack(values, weights, k, i + 1),  # Exclude the current item
        values[i] + knapsack(values, weights, k - weights[i], i)  # Include the current item
    )
```

### Explanation:
1. **Base Case 1**: If the remaining capacity `k` becomes negative, the solution is invalid, so we return negative infinity.
2. **Base Case 2**: If we've exhausted all items (i.e., `i == len(values)`), we return 0 as no more items can be added.
3. **Recursive Case**: At each item, we either exclude it or include it:
   - Exclude: Call the function for the next item.
   - Include: Add the value of the current item and reduce the capacity by its weight. The current item can still be included again (unbounded nature), so we call the function without moving to the next item.

### Time Complexity:
- \(O(n \times k)\), where \(n\) is the number of items and \(k\) is the capacity.

### Space Complexity:
- \(O(k)\) due to the recursive call stack.




1. **Modification**: Unlike 0-1, where we move to the next item after including one, in unbounded knapsack, after taking an item, we don’t move to the next item immediately but stay on the same item to take it again if desired.

#### Code:
```python
from typing import List

def knapsack_recursive(values: List[int], weights: List[int], k: int) -> int:
    # Base case: no capacity left
    if k == 0:
        return 0
    
    max_value = 0
    for i in range(len(values)):
        # If the item can fit in the knapsack
        if weights[i] <= k:
            # Calculate the value if we take the item
            max_value = max(max_value, values[i] + knapsack_recursive(values, weights, k - weights[i]))
    
    return max_value
```

**Explanation**:
- This is a simple recursive solution that tries to take every item as many times as possible without exceeding the capacity.
- For each item, we recursively calculate the maximum value for the remaining capacity.

**Time Complexity**: 
- In this approach, the number of subproblems is exponential, making the time complexity $O(2^k)$ where $k$ is the capacity of the knapsack.

**Space Complexity**: 
- $O(k)$ because of the recursive stack.

---

### Approach 2: Dynamic Programming with Memoization

1. **Concept**: To optimize the recursive approach, we can store the results of subproblems in a table (memoization). This way, we avoid recalculating values for the same capacity multiple times, reducing redundant work.
2. **Optimization**: Use a dictionary `lookup` to store the best possible value for a given remaining capacity.

#### Code:
```python
from typing import List, Dict

def knapsack_memoization(values: List[int], weights: List[int], k: int, lookup: Dict[int, int] = None) -> int:
    if lookup is None:
        lookup = {}
    
    # If the solution is already computed
    if k in lookup:
        return lookup[k]
    
    max_value = 0
    for i in range(len(values)):
        if weights[i] <= k:
            max_value = max(max_value, values[i] + knapsack_memoization(values, weights, k - weights[i], lookup))
    
    # Save the result for this capacity
    lookup[k] = max_value
    return max_value
```

**Explanation**:
- This solution is similar to the recursive approach but stores the results of previously solved subproblems in a dictionary `lookup`.
- Before calculating the value for a given capacity, we first check if we already know the result for that capacity.

**Time Complexity**: 
- The time complexity is $O(n \cdot k)$, where $n$ is the number of items and $k$ is the capacity of the knapsack, as we solve each subproblem once.

**Space Complexity**: 
- $O(k)$ due to memoization storage.

---

### Approach 3: Bottom-Up Dynamic Programming (Tabulation)

1. **Concept**: A more intuitive way to solve this problem is by iterating over each item and solving the problem for increasing capacities from $0$ to $k$. This avoids recursion altogether.
2. **Optimization**: Use a 1D DP array where `dp[j]` stores the maximum value we can achieve with a knapsack capacity $j$.

#### Code:
```python
from typing import List

def knapsack_tabulation(values: List[int], weights: List[int], k: int) -> int:
    # Create a dp array of size k+1 initialized to 0
    dp = [0] * (k + 1)
    
    # For each item, update dp array for all capacities
    for i in range(len(values)):
        for capacity in range(weights[i], k + 1):
            dp[capacity] = max(dp[capacity], values[i] + dp[capacity - weights[i]])
    
    return dp[k]
```

**Explanation**:
- We iterate over each item and update the `dp` array for capacities from the item's weight up to the maximum capacity.
- This allows us to calculate the best value we can get for each capacity up to $k$.

**Time Complexity**: 
- $O(n \cdot k)$ where $n$ is the number of items and $k$ is the capacity of the knapsack.

**Space Complexity**: 
- $O(k)$ since we only use a 1D DP array of size $k+1$.

---

### Summary of Approaches:

| Approach                           | Time Complexity    | Space Complexity | Explanation                                                                 |
|------------------------------------|--------------------|------------------|-----------------------------------------------------------------------------|
| Recursive (Backtracking)            | $O(2^k)$           | $O(k)$           | Explore all possible ways to take items, exponential time.                   |
| Memoization (Top-Down DP)           | $O(n \cdot k)$     | $O(k)$           | Optimize recursion by storing subproblem results.                           |
| Tabulation (Bottom-Up DP)           | $O(n \cdot k)$     | $O(k)$           | Iteratively solve the problem using a DP array for capacities.              |

This concludes the explanation of the **Unbounded Knapsack Problem**.




