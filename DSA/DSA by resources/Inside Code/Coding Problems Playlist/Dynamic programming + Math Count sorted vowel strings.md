


[Dynamic programming + Math: Count sorted vowel strings (LeetCode #1641) [3 solutions]](https://youtu.be/_SgsB1ZhcIQ?si=0IrzBruruWDVm0WP)


### Dynamic Programming + Math: Count Sorted Vowel Strings (LeetCode #1641)

Algorithmic problems can often be solved in multiple ways, showcasing the versatility of computer science. In this discussion, we will explore three distinct methods to solve the "Count Sorted Vowel Strings" problem: using **backtracking**, **dynamic programming**, and **mathematics**.

#### Problem Overview:
The problem statement is as follows: Given an integer `n`, return the number of strings of length `n` that consist only of vowels (`a, e, i, o, u`) and are lexicographically sorted.

lexicographically ~ alphabetically 

A string is considered lexicographically sorted if for every pair of consecutive characters, the first is less than or equal to the second, i.e., `a ≤ e ≤ i ≤ o ≤ u`. 

For example, `"aeeiu"` is a valid sorted vowel string because the order of vowels from left to right follows their natural order.

Let's walk through the three solutions, each employing a unique approach.

---

### Solution 1: Backtracking

This solution explores all possible vowel strings and counts those that are sorted. We leverage **backtracking** to avoid generating combinations that violate the lexicographical order.

#### Intuition:
- We attempt to build strings character by character.
- If adding a character violates the lexicographical order, we stop that recursion path.
- The function recursively adds a vowel as long as the condition is met, eventually reaching the base case where the string's length equals `n`.

#### Time Complexity:
- The time complexity is **O(n^5)**. The recursive calls expand based on vowel combinations, but with pruning (backtracking), the time is polynomial rather than exponential.

#### Code:

```python
# Backtracking solution
# Time complexity: O(n^5)
# Space complexity: O(n) (due to the call stack size)
def count(n, last=''):
    if n == 0:
        return 1
    else:
        nb = 0
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            if last <= vowel:
                nb += count(n-1, vowel)
        return nb
```

---

### Solution 2: Dynamic Programming

The dynamic programming approach aims to solve the problem by **breaking it down into subproblems**, computing smaller subproblems first and building up to the solution for `n`.

#### Intuition:
- We define a 2D array `dp` where `dp[i][j]` represents the number of valid strings of length `i` that start with the vowel `j`.
- By filling this table using a bottom-up approach, we leverage previously computed results to quickly build larger strings.

#### Time Complexity:
- **O(n)**. The DP solution builds the table row by row, leading to a linear complexity.

#### Code:

```python
# Dynamic programming solution
# Time complexity: O(n)
# Space complexity: O(n)
def count(n):
    NB_VOWELS = 5
    dp = [[0]*NB_VOWELS for i in range(n)]
    dp[0] = [1]*NB_VOWELS  # Base case: Strings of length 1, 1 possibility per vowel
    for i in range(1, len(dp)):
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]
        dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]
        dp[i][2] = dp[i-1][2] + dp[i-1][3] + dp[i-1][4]
        dp[i][3] = dp[i-1][3] + dp[i-1][4]
        dp[i][4] = dp[i-1][4]
    return sum(dp[-1])
```

#### Bonus: Space-Optimized DP
- By observing that we only need the last and current row to compute results, we can reduce the space complexity to **O(1)**.

```python
# Space-optimized DP solution
# Time complexity: O(n)
# Space complexity: O(1)
def count(n):
    NB_VOWELS = 5
    prev = [1]*NB_VOWELS
    curr = [0]*NB_VOWELS
    for i in range(1, n):
        curr[0] = sum(prev)
        curr[1] = sum(prev[1:])
        curr[2] = sum(prev[2:])
        curr[3] = sum(prev[3:])
        curr[4] = prev[4]
        prev = curr[:]
    return sum(prev)
```

---

### Solution 3: Mathematical Approach

This is a direct **combinatorial solution** using mathematics. The problem of counting sorted vowel strings can be modeled as finding the **combinations with repetition**.

#### Combinatorial Formula:
- We are selecting `n` vowels (with repetition allowed) from 5 possible vowels.
- The formula to compute combinations with repetition is:

$$
C(n+4, 4) = \frac{(n+4)!}{n! \cdot 4!}
$$

After simplifying, the result can be expressed as:

$$
\frac{(n+4)(n+3)(n+2)(n+1)}{24}
$$


#### Time Complexity:
- The time complexity of this solution is **O(1)** as we are just using a formula to calculate the result directly.

#### Code:

```python
# Mathematical solution
# Time complexity: O(1)
# Space complexity: O(1)
def count(n):
    return (n+4)*(n+3)*(n+2)*(n+1)//24
```

---

### Summary:
- **Backtracking**: An intuitive but inefficient solution with time complexity **O(n^5)**.
- **Dynamic Programming**: A more optimized approach with **O(n)** time and space complexity.
- **Mathematical Solution**: The most efficient with **O(1)** time complexity using combinatorics.

Each approach offers a unique perspective, from brute-force exploration to elegant mathematical formulation.





