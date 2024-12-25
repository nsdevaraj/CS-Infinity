
## [LeetCode #46 - Permutations](https://leetcode.com/problems/permutations/)

## Problem Statement

Given an array of distinct integers `nums`, return **all possible permutations** of the array in any order.

---

### Example 1:

```
Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

### Example 2:

```
Input: nums = [0, 1]
Output: [[0, 1], [1, 0]]
```

### Example 3:

```
Input: nums = [1]
Output: [[1]]
```

---

## Approach 1: Backtracking

### Explanation

The backtracking approach is a powerful way to generate all possible permutations of an array by swapping elements recursively.  
Each element takes turns being in the current position, and recursive calls ensure that all possible positions are tried.

---

### Steps:

1. Start from the first position and swap it with every other position, including itself.
2. Recursively call the function for the next position until a complete permutation is formed.
3. Once a valid permutation is formed, save it in the result list.
4. Backtrack by restoring the array to its original state, allowing other permutations to form.

---

### Code


```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_len = len(nums)

        if nums_len == 1 :
            return [nums[:]]
        
        for i in range(nums_len):
            first_item = nums.pop(0)

            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(first_item)
            
            result.extend(permutations)
            nums.append(first_item)

        return result
        
```



```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(start: int):
        # If all positions are filled, we have a valid permutation
        if start == len(nums):
            result.append(nums[:])  # Append a copy of the current permutation
            return
        
        for i in range(start, len(nums)):
            # Swap the current position with index i
            nums[start], nums[i] = nums[i], nums[start]
            # Recursively call for the next position
            backtrack(start + 1)
            # Backtrack to restore original array order
            nums[start], nums[i] = nums[i], nums[start]
    
    result = []
    backtrack(0)
    return result
```

---

### Time Complexity

- **Time complexity:** O(n×n!)O(n \times n!)
    - There are n!n! permutations, and each permutation takes O(n)O(n) to form.
- **Space complexity:** O(n)O(n)
    - The recursion stack depth is O(n)O(n), where nn is the size of the input.

---

### Approach 2: Iterative

### Explanation

This approach uses an iterative method to build permutations step by step. Starting with an empty list, it adds one number at a time in all possible positions.

---

### Code

```python
from typing import List

def permute_iterative(nums: List[int]) -> List[List[int]]:
    result = [[]]
    
    for num in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                # Insert the current number into every possible position
                new_result.append(perm[:i] + [num] + perm[i:])
        result = new_result
    
    return result
```

---

### Time Complexity

- **Time complexity:** O(n×n!)O(n \times n!), as each number is inserted in all permutations.
- **Space complexity:** O(n×n!)O(n \times n!), as the number of permutations grows exponentially.

---

## Summary of Approaches

|Approach|Time Complexity|Space Complexity|Explanation|
|---|---|---|---|
|Backtracking|O(n×n!)O(n \times n!)|O(n)O(n)|Recursively generate permutations with swapping.|
|Iterative|O(n×n!)O(n \times n!)|O(n×n!)O(n \times n!)|Build permutations iteratively.|

---

### Test Function

```python
def test_permute(func):
    test_cases = [
        {
            "name": "General Case",
            "input": [1, 2, 3],
            "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        },
        {
            "name": "Two Elements",
            "input": [0, 1],
            "expected": [[0, 1], [1, 0]],
        },
        {
            "name": "Single Element",
            "input": [1],
            "expected": [[1]],
        },
        {
            "name": "Empty Array",
            "input": [],
            "expected": [],
        },
    ]
    
    for i, case in enumerate(test_cases):
        input_data = case["input"]
        expected_output = sorted(case["expected"])
        result = sorted(func(input_data))
        
        assert result == expected_output, f"Test case {i + 1} failed: Input {input_data}, Expected {expected_output}, Got {result}"
    
    print("All test cases passed!")
```

---

### Examples

1. **Input:** `[1, 2, 3]`  
    **Output:** `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`
    
2. **Input:** `[0, 1]`  
    **Output:** `[[0, 1], [1, 0]]`
    
3. **Input:** `[1]`  
    **Output:** `[[1]]`
    
4. **Input:** `[]`  
    **Output:** `[]`
    

---

## Notes

Permutations are different from combinations:

- Permutations consider the order of elements, while combinations do not.
- The total number of permutations for an array of size nn is n!n!.

This problem is often used in interview scenarios to test recursion and backtracking skills.


---

### 7. **Permutations**

**Problem:** Given a collection of distinct integers, return all possible permutations.

```python
def permute(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result
```



Runtime: 0ms

python

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms
        
```


Runtime: 1ms

python

```python
from collections import defaultdict

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = [defaultdict(None)] # (path, start)
        while stack:
            path = stack.pop()

            if len(path) == len(nums):
                result.append(list(path.keys()))
                continue

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                stack.append(path | {nums[i]: None})
        return result
```


Memory: 16.2mb

python

```python
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        if n == 1:
            permutations.append(nums)
            return permutations
        permutations = list(itertools.permutations(nums))
        return permutations
```


Memory: 16.6mb

python

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            temp = []
            for prem in res:
                for i in range(len(prem) + 1):
                    temp.append(prem[:i] + [n] + prem[i:])
            res = temp
        
        return res
```



referred {

https://www.youtube.com/watch?v=s7AvT7cGdSo

https://www.youtube.com/shorts/Hcnmv5Cs0QA

}


to check {
https://www.youtube.com/watch?v=YK78FU5Ffjw

https://www.youtube.com/watch?v=f2ic2Rsc9pU


}