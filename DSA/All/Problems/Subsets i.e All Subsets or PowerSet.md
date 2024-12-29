
### Powerset

- A **powerset** is the set of all subsets of a given set.


referred {

https://www.youtube.com/watch?v=Y85dfkCSlP8


}

# [LeetCode #78 - Subsets](https://leetcode.com/problems/subsets/)

## Problem Statement

Given an integer array `nums` of **unique elements**, return **all possible subsets** (the power set).

The solution set must not contain duplicate subsets. Return the solution in **any order**.

---

### Example 1:

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
```

### Example 2:

```
Input: nums = [0]
Output: [[],[0]]
```

---

## Approach 1: Backtracking

### Explanation

The backtracking approach systematically explores all subsets by including or excluding each element at every recursive step.  
It builds the subsets incrementally and explores all possibilities.

---

### Steps:

1. Start with an empty subset.
2. For each element in the array, make two recursive calls:
    - One where the element is included in the current subset.
    - One where it is excluded.
3. Once the recursion reaches the end of the array, save the subset.

---

Recursive: take item or skip item recursively



```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def findSubsets(subset = [], i=0):
            if i == len(nums):
                # copy is optional here, don't affect any logic flow.. 
                subsets.append(subset.copy())
            else:
                findSubsets(subset, i+1)
                findSubsets(subset+[nums[i]], i+1)
        
        findSubsets()

        return subsets
```




----


### Code

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(start: int, current: List[int]):
        # Add the current subset to the result
        result.append(current[:])
        
        # Try including each number in the current subset
        for i in range(start, len(nums)):
            current.append(nums[i])  # Include nums[i]
            backtrack(i + 1, current)  # Recurse
            current.pop()  # Exclude nums[i] (backtrack)
    
    result = []
    backtrack(0, [])
    return result
```

---

### Time Complexity:

- **Time complexity:** O(n×2n)O(n \times 2^n)
    - 2n2^n subsets are generated for an array of size nn.
    - Each subset takes O(n)O(n) to construct.
- **Space complexity:** O(n)O(n)
    - Maximum depth of recursion is O(n)O(n).

---

## Approach 2: Iterative

### Explanation

The iterative approach generates subsets by starting with an empty subset and iteratively adding elements to all existing subsets.

---

### Steps:

1. Start with an empty subset (`[[]]`).
2. For each number in the array, add it to every existing subset.
3. Continue this process for all elements in the array.

---

### Code

```python
from typing import List

def subsets_iterative(nums: List[int]) -> List[List[int]]:
    result = [[]]
    
    for num in nums:
        # Add the current number to all existing subsets
        result += [curr + [num] for curr in result]
    
    return result
```

---

### Time Complexity:

- **Time complexity:** O(n×2n)O(n \times 2^n), as there are 2n2^n subsets, and each subset takes O(n)O(n) to construct.
- **Space complexity:** O(n×2n)O(n \times 2^n), as the result list contains all subsets.

---

## Approach 3: Bitmasking

### Explanation

Using bitmasking, we can represent each subset as a binary number.  
For example, for `nums = [1, 2, 3]`:

- The bitmask `000` represents the empty subset `[]`.
- The bitmask `101` represents the subset `[1, 3]`.

---

### Steps:

1. Use a loop to iterate through all possible bitmasks from `0` to 2n−12^n - 1.
2. For each bitmask, include elements where the corresponding bit is `1`.

---

### Code

```python
from typing import List

def subsets_bitmask(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []
    
    for mask in range(1 << n):  # Iterate through all 2^n combinations
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    
    return result
```

---

### Time Complexity:

- **Time complexity:** O(n×2n)O(n \times 2^n), as there are 2n2^n subsets, and each subset takes O(n)O(n) to construct.
- **Space complexity:** O(n×2n)O(n \times 2^n), for storing the result.

---

## Summary of Approaches

|Approach|Time Complexity|Space Complexity|Explanation|
|---|---|---|---|
|Backtracking|O(n×2n)O(n \times 2^n)|O(n)O(n)|Recursively build subsets by including/excluding elements.|
|Iterative|O(n×2n)O(n \times 2^n)|O(n×2n)O(n \times 2^n)|Build subsets iteratively by adding elements to existing subsets.|
|Bitmasking|O(n×2n)O(n \times 2^n)|O(n×2n)O(n \times 2^n)|Use binary representation to generate subsets.|

---

### Test Function

```python
def test_subsets(func):
    test_cases = [
        {
            "name": "General Case",
            "input": [1, 2, 3],
            "expected": [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
        },
        {
            "name": "Single Element",
            "input": [0],
            "expected": [[], [0]],
        },
        {
            "name": "Empty Array",
            "input": [],
            "expected": [[]],
        },
    ]
    
    for i, case in enumerate(test_cases):
        input_data = case["input"]
        expected_output = sorted([sorted(subset) for subset in case["expected"]])
        result = sorted([sorted(subset) for subset in func(input_data)])
        
        assert result == expected_output, f"Test case {i + 1} failed: Input {input_data}, Expected {expected_output}, Got {result}"
    
    print("All test cases passed!")
```

---

### Examples

1. **Input:** `[1, 2, 3]`  
    **Output:** `[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]`
    
2. **Input:** `[0]`  
    **Output:** `[[], [0]]`
    
3. **Input:** `[]`  
    **Output:** `[[]]`
    

---

## Notes

- Subsets (or the power set) are a fundamental problem in combinatorics and recursion.
- This problem is often used in interview scenarios to test recursion, iterative thinking, and binary representation skills.
- In subsets, the order of elements in the subset does not matter, unlike permutations.


---


### 10. **Subsets**

**Problem:** Given a set of distinct integers, return all possible subsets (the power set).

```python
def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

---




more {

subset vs combination


Yes, **subsets** are conceptually the same as **combinations** in combinatorics. Both involve selecting elements from a set without considering their order, but there are subtle differences in how they are framed in different contexts:

---

### **Subset**

- A subset includes **all possible selections**, including:
    - The empty set `[]`.
    - The full set `[1, 2, ..., n]`.
- A subset can range from size 00 (empty subset) to size nn (all elements in the set).
- **Example**: For `nums = [1, 2]`, the subsets are `[[], [1], [2], [1, 2]]`.

---

### **Combination**

- A combination generally refers to selecting a specific **fixed number** of elements kk from a set of nn elements.
- **Example**: For `nums = [1, 2, 3]`:
    - k=2k = 2: The combinations are `[[1, 2], [1, 3], [2, 3]]`.
- A combination does **not** include the empty set or the full set unless specifically calculated for k=0k = 0 or k=nk = n.

---

### **Key Difference**

- **Subset**: Encompasses all possible combinations for all sizes kk, from 00 to nn.
- **Combination**: Refers to a specific subset size kk.

---

### **Mathematical Representation**

1. Subsets:
    
    - All subsets of a set of size nn can be represented using 2n2^n, as each element can either be included or excluded.
2. Combinations:
    
    - The number of combinations for a fixed size kk is given by: C(n,k)=(nk)=n!k!(n−k)!C(n, k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}

---

### Summary Table

|Feature|Subsets|Combinations|
|---|---|---|
|Order of Elements|Does not matter|Does not matter|
|Size|All sizes 00 to nn|Fixed size kk|
|Includes Empty Set?|Yes|Only if k=0k = 0|
|Includes Full Set?|Yes|Only if k=nk = n|

---

If you’re solving for **subsets**, think of it as finding all possible combinations for all possible sizes. If solving for **combinations**, focus only on selecting a specific number of elements.



}

---

other codes {


Memory: 16.4mb

python

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result, sol = [], []

        def backtrack(i):
            if i == n:
                result.append(sol[:])
                return
            
            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return result
```



Memory: 16.5mb

python

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # contains all possible subsets for nums[0:i] at current iter i
        dp = []

        if not nums:
            return dp
        
        dp.append([])

        for num in nums:
            # Iterate nums. For each num, add it to all previous elements of dp
            print(num)
            
            prev_len = len(dp)
            for i in range(prev_len):
                copy = dp[i][:]
                copy.append(num)
                dp.append(copy)
            
        
        return dp
```



Memory: 17.3mb

python

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bt(si, curr_set):
            ans.append(curr_set[:])

            for i in range(si, len(nums)):
                curr_set.append(nums[i])
                bt(i + 1, curr_set)
                curr_set.pop()
        
        ans = []
        bt(0, [])
        return ans
    
```



Runtime: 1ms

python

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_sets = [[]]
        dp = {(): [[]]}

        def rec(arr):
            if arr in dp: return dp[arr]
            included = []
            not_included = rec(arr[1:])
            for x in not_included:
                included.append([arr[0]] + x)
            dp[arr] = included + not_included
            return dp[arr]
        
        return rec(tuple(nums))
```


}




similar: [[Subset]]
