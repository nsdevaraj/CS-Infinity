

[Fractional knapsack problem - Inside code](https://youtu.be/DGOwuk55xa0?si=YUyVd-K5x9SVN5jw)


## Problem Statement: Fractional Knapsack Problem

Given a set of \( n \) items, each with a value \( v_i \) and weight \( w_i \), and a knapsack with a maximum capacity \( W \), the goal is to determine the maximum value you can fit in the knapsack. Unlike the 0/1 Knapsack Problem, you are allowed to take fractions of an item.

### Objective:
Maximize the total value without exceeding the weight capacity \( W \). Mathematically, the goal is to maximize:

$$
\sum_{i=1}^{n} v_i \cdot x_i
$$

subject to:

$$
\sum_{i=1}^{n} w_i \cdot x_i \leq W
$$

where \( x_i \) is the fraction of item \( i \) taken, and \( 0 \leq x_i \leq 1 \).

---

## Example:

Consider the following items and knapsack capacity:

| Item | Value (\( v_i \)) | Weight (\( w_i \)) |
|------|-------------------|-------------------|
| 1    | 20                | 6                 |
| 2    | 18                | 7                 |
| 3    | 15                | 5                 |
| 4    | 25                | 10                |
| 5    | 10                | 3                 |

**Knapsack Capacity**: \( W = 15 \)

---

## Greedy Approach Explanation:

The greedy solution involves calculating the ratio of value to weight for each item, sorting the items based on this ratio in decreasing order, and then taking items from the sorted list until the knapsack is full or a fraction of the next item needs to be taken.

### Step-by-Step Explanation:

1. **Calculate Ratios**:

   $$
   \frac{v_1}{w_1} = \frac{20}{6} \approx 3.33, \quad
   \frac{v_2}{w_2} = \frac{18}{7} \approx 2.57, \quad
   \frac{v_3}{w_3} = \frac{15}{5} = 3, \quad
   \frac{v_4}{w_4} = \frac{25}{10} = 2.5, \quad
   \frac{v_5}{w_5} = \frac{10}{3} \approx 3.33
   $$

2. **Sort by Ratios**: The items are sorted in descending order of value-to-weight ratio.

3. **Pick Items**:

   - **Item 1**: Take fully. Remaining capacity = \( 15 - 6 = 9 \).
   - **Item 3**: Take fully. Remaining capacity = \( 9 - 5 = 4 \).
   - **Item 5**: Take fully. Remaining capacity = \( 4 - 3 = 1 \).
   -  **Item 2**: Take a fraction. Fraction taken = $\frac{1}{7}$, value added = $18 \times \frac{1}{7} = 2.57$.

   Total value:

   $$
   20 + 15 + 10 + 2.57 = 47.57
   $$

---

## Code Implementation (Greedy Solution)

```python
from typing import List

def fractional_knapsack(values: List[float], weights: List[float], capacity: float) -> float:
    # Create a list of item indices sorted by their value-to-weight ratio in decreasing order
    items = list(range(len(values)))
    items.sort(key=lambda i: values[i] / weights[i], reverse=True)

    total_value = 0.0  # Total value collected in the knapsack
    
    # Traverse sorted items
    for i in items:
        if weights[i] <= capacity:
            # If item can fully fit in the remaining capacity, take it
            total_value += values[i]
            capacity -= weights[i]
        else:
            # Take a fraction of the item
            fraction = capacity / weights[i]
            total_value += values[i] * fraction
            break  # Knapsack is full after taking fraction
    
    return total_value

# Example usage
values = [20, 18, 15, 25, 10]
weights = [6, 7, 5, 10, 3]
capacity = 15
print(fractional_knapsack(values, weights, capacity))  # Output: approximately 47.57
```

---

## Time Complexity:

1. **Sorting** the items by their value-to-weight ratio takes \( O(n \log n) \).
2. **Traversing** the sorted items takes \( O(n) \).

Thus, the overall time complexity is \( O(n \log n) \).

## Space Complexity:

- The space complexity is \( O(n) \), primarily for storing the list of item indices.

---

## Why the Greedy Algorithm Works for Fractional Knapsack:

The greedy algorithm is optimal for the fractional knapsack problem because we can always take the most valuable fraction of an item, ensuring no capacity is wasted. This leads to the maximum possible value without needing to explore all combinations.

---

## Comparison with 0/1 Knapsack:

| Feature                     | 0/1 Knapsack        | Fractional Knapsack |
| --------------------------- | ------------------- | ------------------- |
| Can take fractions?         | No                  | Yes                 |
| Optimal Solution Approach   | Dynamic Programming | Greedy Algorithm    |
| Time Complexity (Optimal)   | \( O(nW) \)         | $( O(n \log n) )$   |
| Space Complexity            | \( O(nW) \)         | $( O(n) )$          |
| Greedy Algorithm Optimality | Not always optimal  | Always optimal      |

---

## Summary of Approaches:

| Approach                  | Time Complexity     | Space Complexity | Optimal Solution?               |
|---------------------------|---------------------|------------------|---------------------------------|
| Greedy (Fractional)        | \( O(n \log n) \)   | \( O(n) \)       | Yes, for fractional knapsack    |
| Dynamic Programming (0/1)  | \( O(nW) \)         | \( O(nW) \)      | Yes, for 0/1 knapsack           |

---

Now, the content should render correctly in Obsidian with the equations wrapped in dollar signs for LaTeX.

