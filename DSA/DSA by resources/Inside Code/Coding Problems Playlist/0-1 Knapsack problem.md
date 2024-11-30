
[0-1 Knapsack problem - Inside code](https://youtu.be/Q2vDTam9qMQ?si=RnwwXiIlYf5zJmqD)


## Problem Statement: 0-1 Knapsack Problem

You are given a set of items, each with a weight and a value. Your goal is to determine the maximum value you can accumulate in a knapsack with a limited weight capacity. The catch is, you can only include an item either once (1) or not at all (0) in the knapsack, which is why it's called the **0-1 Knapsack Problem**.

### Given:
- `n` items, where each item $i$ has:
  - Value: $v[i]$
  - Weight: $w[i]$
- A knapsack with a maximum capacity of $k$.

### Objective:
Find the combination of items that maximizes the total value without exceeding the weight capacity $k$.

Mathematically, you want to maximize the sum:

$$
\sum_{i=1}^{n} v[i] \cdot x[i]
$$

subject to:

$$
\sum_{i=1}^{n} w[i] \cdot x[i] \leq k
$$

where $x[i]$ can be either 0 or 1 (indicating whether to include the item or not).

### Example:
Consider 5 items with the following weights and values:

| Item  | Value | Weight |
|-------|-------|--------|
| 1     | 20    | 6      |
| 2     | 30    | 10     |
| 3     | 50    | 12     |
| 4     | 10    | 5      |
| 5     | 15    | 8      |

Knapsack capacity = 20.

The best solution is to take items 1, 4, and 5, which gives a total value of **55** and a total weight of 19 (which is within the capacity).

---

## Approach 1: Brute Force (Recursive)


{
take all combinations 
}

The brute force approach explores all possible combinations of items. For each item, we have two options:
1. Include the item in the knapsack.
2. Exclude the item from the knapsack.

We then recursively evaluate both possibilities for every item and choose the one that gives the maximum value without exceeding the weight capacity.

### Recurrence Relation:
$$
\text{knapsack}(i, k) = 
\begin{cases} 
0 & \text{if } i = n \text{ (no items left)} \\
-\infty & \text{if } k < 0 \text{ (capacity exceeded)} \\
\max(\text{knapsack}(i+1, k), v[i] + \text{knapsack}(i+1, k-w[i])) & \text{otherwise}
\end{cases}
$$

### Code (Brute Force):
```python
def knapsack_brute_force(v: list[int], w: list[int], k: int, i: int = 0) -> int:
    # Base cases
    if i == len(v):  # No items left
        return 0
    if k < 0:  # Capacity exceeded
        return float('-inf')

    # If the current item exceeds the knapsack's capacity, skip it
    if w[i] > k:
        return knapsack_brute_force(v, w, k, i + 1)
    
    # Recursively choose the maximum between taking or not taking the current item
    return max(v[i] + knapsack_brute_force(v, w, k - w[i], i + 1),
               knapsack_brute_force(v, w, k, i + 1))
```

### Time Complexity:
- **Time**: $O(2^n)$ since each item has two possibilities (include or exclude), and we explore all combinations.
- **Space**: $O(n)$ due to the recursion stack.

---

## Approach 2: Dynamic Programming (Top-Down with Memoization)

The brute force approach has a lot of redundant calculations. For example, two different paths in the recursion might solve the same subproblem multiple times. To avoid this, we use **dynamic programming** by storing the results of already computed subproblems in a lookup table (memoization).

### Optimized Recurrence Relation:
We use the same recurrence relation as above but add a lookup table (`lookup`) to store intermediate results.

### Code (Top-Down with Memoization): (best for this prob)
```python
def knapsack_top_down(v: list[int], w: list[int], k: int, i: int = 0, lookup: dict = None) -> int:
    lookup = {} if lookup is None else lookup
    
    # Check if the subproblem has already been solved
    if (i, k) in lookup:
        return lookup[(i, k)]
    
    # Base cases
    if i == len(v):  # No items left
        return 0
    if k < 0:  # Capacity exceeded
        return float('-inf')

    # If the current item exceeds the knapsack's capacity, skip it
    if w[i] > k:
        result = knapsack_top_down(v, w, k, i + 1, lookup)
    else:
        # Recursively choose the maximum between taking or not taking the current item
        result = max(v[i] + knapsack_top_down(v, w, k - w[i], i + 1, lookup),
                     knapsack_top_down(v, w, k, i + 1, lookup))
    
    # Store the result in the lookup table
    lookup[(i, k)] = result
    return result
```

### Time Complexity:
- **Time**: $O(n \cdot k)$ because we solve each subproblem only once and there are $n \times k$ unique subproblems.
- **Space**: $O(n \cdot k)$ for the lookup table and recursion stack.

---

## Approach 3: Dynamic Programming (Bottom-Up)

In the **bottom-up** approach, we build a table iteratively where the rows represent items and the columns represent the possible capacities. This approach ensures that all subproblems are solved, but it may solve subproblems we don’t need.

### Code (Bottom-Up):
```python
def knapsack_bottom_up(v: list[int], w: list[int], k: int) -> int:
    n = len(v)
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(v[i - 1] + dp[i - 1][j - w[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][k]
```

### Time Complexity:
- **Time**: $O(n \cdot k)$ as we iterate over every item and capacity combination.
- **Space**: $O(n \cdot k)$ for the 2D table.

---

## Summary of Approaches

| Approach                        | Time Complexity  | Space Complexity | Explanation                                                    |
|----------------------------------|------------------|------------------|----------------------------------------------------------------|
| **Brute Force**                  | $O(2^n)$         | $O(n)$           | Recursively evaluates all possible combinations.                |
| **Top-Down (Memoization)**       | $O(n \cdot k)$   | $O(n \cdot k)$   | Uses recursion with memoization to store intermediate results.  |
| **Bottom-Up (DP Table)**         | $O(n \cdot k)$   | $O(n \cdot k)$   | Iteratively builds a table of results for all subproblems.      |

This concludes the explanation of the **0-1 Knapsack problem** with multiple approaches, their implementations, and time/space complexity analyses.

---

This version correctly encloses all mathematical expressions in dollar signs for proper rendering in Obsidian.


