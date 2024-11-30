
### Problem Link

[338. Counting Bits - LeetCode](https://leetcode.com/problems/counting-bits/)

---

### Problem Statement

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` ($0 \leq i \leq n$), `ans[i]` is the **number of `1`'s** in the binary representation of `i`.

---

### Examples

**Example 1:**

- **Input:** `n = 2`
- **Output:** `[0, 1, 1]`
- **Explanation:**
    - `0` in binary is `0` (0 ones).
    - `1` in binary is `1` (1 one).
    - `2` in binary is `10` (1 one).

**Example 2:**

- **Input:** `n = 5`
- **Output:** `[0, 1, 1, 2, 1, 2]`
- **Explanation:**
    - `0` in binary is `0` (0 ones).
    - `1` in binary is `1` (1 one).
    - `2` in binary is `10` (1 one).
    - `3` in binary is `11` (2 ones).
    - `4` in binary is `100` (1 one).
    - `5` in binary is `101` (2 ones).

---

### Approaches

---

#### Approach 1: Brute Force Using Bit Count

For each number $i$ from $0$ to $n$, calculate the number of `1`s in its binary representation by converting it to binary and counting.

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Brute force approach: Compute number of 1's in binary for each number.
        
        Time Complexity: O(n \cdot \text{bits}) - Counting bits for each number.
        Space Complexity: O(n) - To store the result array.
        """
        return [bin(i).count('1') for i in range(n + 1)]
```

---

```python
'''
Time - O(n logN) => n - all iterate , logN - bits iterate (The number of bits in `num` is proportional to the logarithm of the number) 
Space - O(1)
'''
def countBits(n: int) -> List[int]:
    def countBitsOfNum(num:int):
        count = 0
        while (num):
            count += num & 1
            num = num >> 1
        return count

    bits_ary = []
    for i in range(n+1):
        bits_ary.append(countBitsOfNum(i))
    return bits_ary

```


---


#### Approach 2: Dynamic Programming with Odd/Even

The binary representation of a number can be analyzed as follows:

- **Even number:** The number of `1`s is the same as the number of `1`s in `i // 2` (right shift by 1). ( last significant bit is 0, we can remove it )
- **Odd number:** The number of `1`s is one more than the number of `1`s in `i - 1` (because the least significant bit is `1`).

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Dynamic Programming using Odd/Even property.
        
        Time Complexity: O(n) - Single iteration from 0 to n.
        Space Complexity: O(n) - To store the result array.
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
```

---

#### Approach 3: Dynamic Programming with Lowest Bit

The **lowest bit** of a number `i` can be removed using `i & (i - 1)`. The count of `1`s in `i` is then `1` plus the count of `1`s in `i & (i - 1)`.


Ylet's break it down in a clear and crisp way!

### Goal:

The goal is to efficiently count the number of `1` bits (also called the **Hamming weight**) in a number `i` using a well-known bit manipulation technique.

### Key Concepts:

1. **Lowest Set Bit**:
    
    - The **lowest set bit** (the rightmost `1` bit) of a number `i` can be isolated and removed using the operation `i & (i - 1)`.
    - Here's how it works:
        - In binary, the number `i - 1` flips all the bits to the right of the rightmost `1` bit of `i`, and also flips the rightmost `1` bit itself to `0`.
        - By performing `i & (i - 1)`, we clear (set to `0`) the rightmost `1` bit of `i`.
    
    **Example**: Let's say `i = 12`, which is `1100` in binary:
    
    - `i = 12` → `1100` (in binary)
    - `i - 1 = 11` → `1011` (in binary)
    - Now, `i & (i - 1) = 1100 & 1011 = 1000` (in binary), which is `8`.
    
    The result `i & (i - 1)` removes the lowest set bit (`2^0` or the rightmost `1` bit).
    
2. **Counting the Number of `1` Bits**:
    
    - The basic idea is that if you remove the lowest set bit of `i` (using `i & (i - 1)`), the number of `1` bits in `i` will be the same as the number of `1` bits in `i & (i - 1)`, plus 1 (since you removed exactly one `1` bit).
    
    **How the process works**:
    
    - You can repeatedly remove the lowest set bit from `i` and count how many times this operation occurs until `i` becomes `0`. Each time, you are effectively "counting" one `1` bit that was removed.
    - Since each removal clears one bit, the number of iterations is equal to the number of `1` bits in `i`.

### Example Walkthrough:

Let’s take an example with `i = 12` (which is `1100` in binary):

1. **Step 1**: `i = 12` → `1100`
    
    - `i & (i - 1) = 12 & 11 = 8` → `1000`
    - So, `countBits(12) = 1 + countBits(8)`
2. **Step 2**: `i = 8` → `1000`
    
    - `i & (i - 1) = 8 & 7 = 0` → `0000`
    - So, `countBits(8) = 1 + countBits(0)`
3. **Step 3**: `i = 0`
    
    - Base case: `countBits(0) = 0`
4. **Final Calculation**:
    
    - `countBits(12) = 1 + countBits(8) = 1 + (1 + countBits(0)) = 1 + 1 + 0 = 2`

So, `12` (which is `1100` in binary) has **2 `1` bits**.

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Dynamic Programming using Lowest Bit Removal.
        
        Time Complexity: O(n) - Single iteration from 0 to n.
        Space Complexity: O(n) - To store the result array.
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp
```

---

### Summary of Approaches

|Approach|Time Complexity|Space Complexity|Description|
|---|---|---|---|
|**Brute Force (Bit Count)**|$O(n \cdot \text{bits})$|$O(n)$|Count bits for each number using `bin`.|
|**Dynamic Programming (Odd/Even)**|$O(n)$|$O(n)$|Use the relation based on odd/even properties.|
|**Dynamic Programming (Lowest Bit)**|$O(n)$|$O(n)$|Use the lowest bit removal property.|

---
## other solns:

to check :

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [sum(list(map(int, list(bin(i).replace("0b",""))))) for i in range(n+1)]
        return ans
```


```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        i = 0

        while i < n:
            temp = []
            for j in ans:
                temp.append(j+1)
                i += 1
                if i >= n:
                    break
            ans += temp

        return ans


        ### good
        # dp = [0] * (n+1)
        # dp[0] = 0
        # if n == 0:
        #     return dp
        # dp[1] = 1
        # if n == 1:
        #     return dp
        # p = 1
        # curr = 2**p
        # while curr <= n:
        #     # print(curr, n)
        #     for i in range(curr):
        #         curr = 2**p + i
        #         # print(2**p, curr, i)
        #         if curr <= n:
        #             dp[curr] = 1 + dp[i]
        #         else:
        #             break
        #     p += 1
        #     curr = 2**p
        # return dp
```

---


### Test Function

```python
def test_countBits(func):
    """
    Test function for countBits implementations.
    """
    test_cases = [
        {"input": 2, "expected": [0, 1, 1]},
        {"input": 5, "expected": [0, 1, 1, 2, 1, 2]},
        {"input": 0, "expected": [0]},
        {"input": 1, "expected": [0, 1]},
        {"input": 10, "expected": [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]},
        {"input": 15, "expected": [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]},
        {"input": 20, "expected": [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]},
        {"input": 32, "expected": [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1]},
    ]

    for i, test in enumerate(test_cases):
        result = func(test["input"])
        assert result == test["expected"], f"Test case {i + 1} failed: Input {test['input']} Expected {test['expected']}, got {result}"

# Example usage:
# test_countBits(Solution().countBits)
```


