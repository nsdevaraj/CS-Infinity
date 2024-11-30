

[Shopping offers problem - Inside code](https://youtu.be/HzhUQPA-3J0?si=uAKXXlMa5J_u9ceu)
[LeetCode #638](https://leetcode.com/problems/shopping-offers/description/)




### Problem Statement: Shopping Offers (LeetCode #638)

You are given:
- `n` items, each with a **price**.
- A **needs** array representing the quantity of each item you need to buy.
- A list of **special offers**, where each offer gives a discounted price for certain quantities of items.

Your goal is to determine the minimum price required to satisfy your needs, either by purchasing items individually or by using the special offers (or a combination of both). Each offer can be used multiple times, but you cannot buy more items than you need.

#### Example:
```plaintext
Price list: [10, 5, 7]  # Prices for items 0, 1, and 2 respectively
Needs: [2, 4, 1]  # You need 2 of item 0, 4 of item 1, and 1 of item 2
Special offers:
  Offer 1: [1, 1, 0, 12]  # 1 of item 0, 1 of item 1, total price = $12
  Offer 2: [0, 2, 1, 10]  # 2 of item 1, 1 of item 2, total price = $10

Minimum cost = 41
```

**Explanation:**
- Take Offer 1 twice: 2 \* 12 = 24
- Buy 2 units of item 1 at the full price: 2 \* 5 = 10
- Buy 1 unit of item 2 at the full price: 1 \* 7 = 7
- Total = 24 + 10 + 7 = 41

### Key Concepts:
This problem resembles the **Unbounded Knapsack Problem**, where:
- We can choose any offer any number of times, but only if it doesn't exceed our needs.
- We use recursion to evaluate all combinations of offers and individual purchases to find the minimal total cost.

### Approach 1: Recursive Backtracking with Memoization

We'll use recursion to explore all possible combinations of offers. For each recursive call:
1. If our needs are fully met, return the current total cost.
2. For each offer, check if we can apply it (i.e., if we still need enough of each item).
3. Apply the offer and recursively calculate the cost for the remaining needs.
4. Memoize the result to avoid recomputation of the same subproblem (i.e., the same `needs` state).

#### Code Implementation:

```python
from typing import List, Dict

def shopping_offers(price: List[int], special: List[List[int]], needs: List[int], lookup: Dict[str, int] = None) -> int:
    lookup = {} if lookup is None else lookup
    # Memoization: Return if the result for current 'needs' is already calculated
    if str(needs) in lookup:
        return lookup[str(needs)]
    
    # Cost without any offers: buy all items individually
    min_price = sum([needs[i] * price[i] for i in range(len(needs))])
    
    # Try each special offer
    for offer in special:
        # Check if the offer can be applied (i.e., we still need enough of each item)
        if all(offer[i] <= needs[i] for i in range(len(needs))):
            # Calculate new needs after applying the offer
            new_needs = [needs[i] - offer[i] for i in range(len(needs))]
            # Recursively calculate the cost with the offer applied
            min_price = min(min_price, offer[-1] + shopping_offers(price, special, new_needs, lookup))
    
    # Store the computed result for current 'needs'
    lookup[str(needs)] = min_price
    return min_price

# Example
price = [2, 3, 4]
special = [[1, 1, 0, 4], [2, 2, 1, 9]]
needs = [1, 2, 1]
print(shopping_offers(price, special, needs))  # Output: 11
```

### Approach 2: Dynamic Programming (Bottom-Up)
While the problem can naturally be solved using top-down recursion, another potential approach is to convert it into a **bottom-up dynamic programming** problem. However, this approach may not always be the most efficient in this case due to the multidimensional nature of the problem (tracking all items and combinations of offers).

**Time Complexity:**
- The time complexity of this recursive approach with memoization is difficult to express precisely because it depends on the number of valid states (subproblems) based on the needs. However, it avoids recomputation by memoizing previously solved states, making it much more efficient than pure recursion.

**Space Complexity:**
- Space complexity is $O(m \times n)$, where $m$ is the number of items and $n$ is the number of different needs states we compute.

### Summary of Approaches

| Approach                          | Time Complexity                      | Space Complexity  | Notes                                                                 |
|------------------------------------|--------------------------------------|------------------|-----------------------------------------------------------------------|
| Recursive Backtracking with Memoization | Depends on the number of unique needs states, but avoids recomputation | $O(m \times n)$ | Efficient for small to medium-sized inputs due to memoization         |
| Dynamic Programming (Bottom-Up)    | Hard to express due to problem complexity | Higher than top-down | Can be converted but not generally recommended due to multidimensional nature |

By using recursion and memoization, we can solve the problem efficiently without exploring redundant subproblems. The logic behind the solution closely follows the pattern seen in the **Unbounded Knapsack Problem**.


## Compare with unbounded kanpsack


### Problem Statement: Shopping Offers (LeetCode #638)

Imagine you need to buy `n` items, each with a specific **price**, and you know exactly how many of each you need (represented by the **needs** array). However, before purchasing them individually, you are presented with **special offers**—each offer allows you to buy a specific combination of items at a discounted price. Your task is to determine the minimum total cost to fulfill your shopping list, either by taking advantage of the special offers, buying items individually, or both.

This problem is a great opportunity to apply dynamic programming techniques, particularly those used to solve the **Unbounded Knapsack Problem**.

### Unbounded Knapsack Problem Recap

In the **Unbounded Knapsack Problem**, you are given a set of items, each with a weight and a value, and you are tasked with finding the maximum value you can obtain while ensuring the total weight does not exceed a given capacity. You can take an item multiple times, hence the name *unbounded*.

- In knapsack problems, we choose items such that their combined weight doesn't exceed a capacity.
- Here, we choose special offers such that the number of items bought doesn’t exceed what we need.

Both problems involve selecting from multiple options and using recursion to explore all possibilities. The key difference is that in the shopping offers problem, our goal is to minimize the total price, whereas in the knapsack problem, we aim to maximize the total value.

---

### Similarities to Unbounded Knapsack

1. **Choice and Recursion**: In both problems, you are faced with multiple choices (items in knapsack, offers in shopping). Recursion is used to explore all possible choices and compute the optimal result.
   
2. **Multiple Uses of an Option**: Just like in unbounded knapsack, where you can take the same item multiple times, in this problem, you can take the same offer multiple times—this introduces the possibility of solving it using dynamic programming.

3. **Constraint Check**: In unbounded knapsack, we check if the item's weight fits within the remaining capacity before selecting it. In this problem, we check if the special offer can be applied by verifying that the number of items in the offer does not exceed what we still need.

4. **Recursive Subproblems**: Both problems solve overlapping subproblems. After choosing an item (or offer), the problem reduces to a similar, smaller version, where the remaining weight (or needs) is recalculated.

---

### Approach: Recursive Backtracking with Memoization

In the shopping offers problem, the goal is to **minimize** the total price. We start by considering two main cases:
1. **No special offers used**: This is the base case, where we calculate the cost of buying all items at their full price.
2. **Using special offers**: For each special offer, we check if it can be applied (i.e., it does not exceed the remaining needs). If so, we calculate the total price after applying that offer and explore the remaining items recursively.

To optimize this, we use **memoization** to avoid recomputation of the same subproblem. This is crucial since we often end up in the same "state" of needs by following different paths.

#### Code Implementation:

```python
from typing import List, Dict

def shopping_offers(price: List[int], special: List[List[int]], needs: List[int], lookup: Dict[str, int] = None) -> int:
    lookup = {} if lookup is None else lookup
    
    # If the current needs have been solved, return the cached result
    if str(needs) in lookup:
        return lookup[str(needs)]
    
    # Base case: buying everything without any offers
    min_price = sum(needs[i] * price[i] for i in range(len(needs)))
    
    # Try applying each special offer
    for offer in special:
        # Check if the offer can be applied (doesn't exceed the needs)
        if all(offer[i] <= needs[i] for i in range(len(needs))):
            # Calculate new needs after applying the offer
            new_needs = [needs[i] - offer[i] for i in range(len(needs))]
            # Recursively calculate the total cost with this offer applied
            min_price = min(min_price, offer[-1] + shopping_offers(price, special, new_needs, lookup))
    
    # Store the result for current needs in the memoization table
    lookup[str(needs)] = min_price
    return min_price

# Example Usage:
price = [2, 3, 4]
special = [[1, 1, 0, 4], [2, 2, 1, 9]]
needs = [1, 2, 1]
print(shopping_offers(price, special, needs))  # Output: 11
```

### Explanation

- **Initial Case (No Offers)**: The simplest case is where we don't take any offers and buy all the items at their full price. This is like initializing the knapsack problem with no items, where the value is zero. The formula for this is:

  \[
  \text{min\_price} = \sum_{i=0}^{n-1} \text{needs}[i] \times \text{price}[i]
  \]

- **Applying Offers**: For each offer, we first check if it can be applied. This corresponds to checking if the weight of an item is less than or equal to the remaining capacity in the knapsack problem. We do this by ensuring:

  \[
  \text{offer}[i] \leq \text{needs}[i], \quad \text{for all } i
  \]

  If the offer is valid, we reduce the number of items in the needs array accordingly and recursively calculate the new minimum price for the remaining items.

- **Memoization**: Since this problem has overlapping subproblems (the same state of needs can be reached via different paths), we store each result in a dictionary to avoid redundant calculations.

### Time and Space Complexity

**Time Complexity**:  
The time complexity depends on the number of different states of `needs`. Since each item can be reduced to 0, the total number of states is:

\[
O(\prod_{i=0}^{n-1} \text{needs}[i])
\]

However, due to memoization, we ensure that each state is computed only once, making the algorithm efficient.

**Space Complexity**:  
The space complexity is proportional to the number of states stored in the memoization table:

\[
O(\prod_{i=0}^{n-1} \text{needs}[i])
\]

---

### Summary of Approaches

| Approach                              | Time Complexity                                            | Space Complexity     | Notes                                                                                         |
|----------------------------------------|------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------|
| **Recursive Backtracking with Memoization** | $O(\prod_{i=0}^{n-1} \text{needs}[i])$ (due to memoization) | $O(\prod_{i=0}^{n-1} \text{needs}[i])$ | Efficient for solving the problem by eliminating redundant calculations using memoization.     |
| **Dynamic Programming (Bottom-Up)**    | Not practical for this problem due to high-dimensional needs array | Higher than top-down  | Difficult to implement efficiently due to multidimensional nature of the problem.              |

In conclusion, this problem follows the same pattern as the **Unbounded Knapsack Problem**, but instead of maximizing the value, we aim to minimize the total price. By using recursion and memoization, we can solve it efficiently. The key insight is recognizing that each offer can be taken multiple times, just like taking items in the knapsack problem, but we are constrained by the maximum quantity needed for each item.




### Problem Statement: Shopping Offers (LeetCode #638)

You need to buy `n` items, each with a specific **price**, and you have special offers that allow you to buy a combination of items at a discounted rate. Your task is to find the minimum total cost to fulfill your shopping list, either by using the offers, buying items individually, or both.

### Comparison with Unbounded Knapsack

In the **Unbounded Knapsack Problem**, you aim to **maximize** value within a given capacity. In contrast, in the **Shopping Offers** problem, your goal is to **minimize** cost by selecting offers that do not exceed the required item counts.

**Similarities:**
- **Choice and Recursion**: Both problems involve recursive decision-making. In the knapsack, you decide whether to include an item. In shopping offers, you decide whether to use a special offer.
- **Multiple Uses**: Just like you can take the same item multiple times in the unbounded knapsack, you can use the same special offer multiple times in the shopping offers.
- **Subproblem Optimization**: Both problems solve smaller subproblems after making a decision, and memoization can be applied to avoid recomputation.

### Unbounded Knapsack Solution
```python
def knapsack(values, weights, k):
    max_value = 0
    for i in range(len(values)):
        if weights[i] <= k:
            max_value = max(max_value, values[i] + knapsack(values, weights, k - weights[i]))
    return max_value
```

### Shopping Offers Solution
```python
def shopping_offers(price, special, needs):
    min_price = sum([needs[i] * price[i] for i in range(len(needs))])
    for offer in special:
        if all([offer[i] <= needs[i] for i in range(len(needs))]):
            new_needs = [needs[i] - offer[i] for i in range(len(needs))]
            min_price = min(min_price, offer[-1] + shopping_offers(price, special, new_needs))
    return min_price
```

### Key Differences:
- **Objective**: Unbounded knapsack **maximizes** value, while shopping offers **minimizes** cost.
- **Constraints**: In the knapsack problem, capacity limits the selection of items, whereas in shopping offers, the remaining needs of items constrain the use of special offers.

### Time and Space Complexity
Both problems rely on the recursive exploration of states and can benefit from memoization to avoid repeated calculations of the same subproblem.

- **Time Complexity**: $O(\prod \text{needs}[i])$ due to exploring all possible states.
- **Space Complexity**: $O(\prod \text{needs}[i])$ for the memoization table.

By utilizing recursion and memoization effectively, both problems can be solved efficiently, though the difference in objectives (maximize vs. minimize) changes how we approach their solutions.







