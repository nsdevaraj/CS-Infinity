

### Problem Link  
[27. Remove Element - LeetCode](https://leetcode.com/problems/remove-element/)

---

### Problem Statement  
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The relative order of the elements may be changed. After removing the elements, return the number of elements left in the array that are not equal to `val`.

**Constraints:**  
- $0 \leq nums.length \leq 100$
- $0 \leq nums[i] \leq 50$
- $0 \leq val \leq 100$

---

### Examples  

**Example 1:**  
- **Input:** `nums = [3,2,2,3], val = 3`
- **Output:** `2, nums = [2,2]`  
- **Explanation:** After removing `3`, the array is `[2,2]`.

**Example 2:**  
- **Input:** `nums = [0,1,2,2,3,0,4,2], val = 2`
- **Output:** `5, nums = [0,1,3,0,4]`  
- **Explanation:** After removing `2`, the array is `[0,1,3,0,4]`.

---

### Approaches

#### Approach 1: Two Pointers (Read and Write)
Use two pointers:  
- **Read pointer:** Iterate over the array to check each element.  
- **Write pointer:** Keep track of the position to overwrite elements that are not equal to `val`.  

This approach is simple and performs the operation in-place.

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of 'val' in nums in-place.
        
        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(1) - Constant extra space.
        """
        write_ptr = 0  # Index to write non-val elements
        for read_ptr in range(len(nums)):
            if nums[read_ptr] != val:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1  # Move write pointer
        
        return write_ptr
```

---

#### Approach 2: Optimized Swap with Two Pointers  
Instead of overwriting, you can swap `val` elements with elements at the end of the array. This minimizes writes to the array.  

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of 'val' by swapping with the last element.
        
        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(1) - Constant extra space.
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]  # Swap with the last element
                n -= 1  # Reduce the effective size of the array
            else:
                i += 1  # Move to the next element
        
        return n
```

---

### Summary of Approaches

| Approach                  | Time Complexity | Space Complexity | Description                          |
|---------------------------|-----------------|------------------|--------------------------------------|
| Two Pointers (Read-Write) | $O(n)$          | $O(1)$           | Iterate over the array once, writing non-`val` elements in place. |
| Optimized Swap            | $O(n)$          | $O(1)$           | Swaps `val` elements with elements at the end of the array.        |

---

### Test Function

```python
def test_removeElement(func):
    """
    Test function for removeElement implementations.
    """
    test_cases = [
        {"input": ([3,2,2,3], 3), "expected": (2, [2,2])},
        {"input": ([0,1,2,2,3,0,4,2], 2), "expected": (5, [0,1,3,0,4])},
        {"input": ([2,2,2], 2), "expected": (0, [])},  # All elements removed
        {"input": ([1,2,3], 4), "expected": (3, [1,2,3])},  # No elements removed
        {"input": ([], 0), "expected": (0, [])},  # Empty array
        {"input": ([1,2,2,3], 2), "expected": (2, [1,3])},
        {"input": ([4,4,4,4,4], 4), "expected": (0, [])},  # All elements are 'val'
        {"input": ([0], 1), "expected": (1, [0])},  # Single element not equal to 'val'
        {"input": ([1], 1), "expected": (0, [])},  # Single element equal to 'val'
        {"input": ([1,1,1,2,2,2,3,3,3], 1), "expected": (6, [2,2,2,3,3,3])},
    ]
    
    for i, test in enumerate(test_cases):
        nums, val = test["input"]
        expected_len, expected_nums = test["expected"]
        result_len = func(nums, val)
        assert result_len == expected_len and nums[:result_len] == expected_nums, \
            f"Test case {i + 1} failed: Expected {test['expected']}, got {(result_len, nums[:result_len])}"

# Example usage:
# test_removeElement(Solution().removeElement)
```

