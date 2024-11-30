

[LeetCode #33 - Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem Statement
You are given an integer array `nums` sorted in ascending order, which is then rotated at some unknown pivot index. You are also given an integer `target`. Your task is to determine if `target` exists in the array `nums`. If it does, return its index. Otherwise, return `-1`.

You must write an algorithm with a time complexity of $O(\log n)$.

### Example
**Input:**
```plaintext
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```
**Output:**
```plaintext
4
```
**Explanation:** The target `0` is found at index `4`.

---

**Input:**
```plaintext
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
```
**Output:**
```plaintext
-1
```
**Explanation:** The target `3` is not found in the array.

---

## Approaches

### Approach 1: Modified Binary Search

The most efficient way to solve this problem is to use a modified binary search. Here’s how it works:

1. **Initialization**: Start with two pointers, `left` at the beginning (0) and `right` at the end (length of array - 1).
2. **Loop until left pointer is less than or equal to the right pointer**:
   - Calculate the mid-point: `mid = left + (right - left) // 2`.
   - **Check if the mid-point is the target**: If `nums[mid]` is equal to `target`, return `mid`.
   - **Determine which side is sorted**:
     - If the left side is sorted (`nums[left] <= nums[mid]`):
       - Check if the target is within the range of the left side. If so, move the right pointer to `mid - 1`, otherwise move the left pointer to `mid + 1`.
     - If the right side is sorted (`nums[mid] <= nums[right]`):
       - Check if the target is within the range of the right side. If so, move the left pointer to `mid + 1`, otherwise move the right pointer to `mid - 1`.
3. If the target is not found, return `-1`.

#### Time Complexity
The time complexity for this approach is $O(\log n)$ due to the halving of the search space with each iteration.

#### Space Complexity
The space complexity is $O(1)$ as we are using only a few extra variables.

### Code Implementation
```python
from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Determine which side is sorted 
        # ( note condition check by left/right vs mid)
        # left is less or equal to mid
        if nums[left] <= nums[mid]:  # Left side is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target is in the left side
            else:
                left = mid + 1  # Target is in the right side
        else:  # Right side is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Target is in the right side
            # it don't work, since it means different
            #if(nums[right] >= target > nums[mid]):
            #    left = mid +1    
            else:
                right = mid - 1  # Target is in the left side

    return -1  # Target not found
```


to check {

| Condition | Interpretation | Search Focus |
| --------- | -------------- | ------------ |

|                                     |                                                          |       |
| ----------------------------------- | -------------------------------------------------------- | ----- |
| `nums[right] >= target > nums[mid]` | Target is strictly between `nums[mid]` and `nums[right]` | Right |

|                                     |                                                                                    |       |
| ----------------------------------- | ---------------------------------------------------------------------------------- | ----- |
| `nums[mid] < target <= nums[right]` | Target is within the range from `nums[mid]` to `nums[right]`, inclusive of `right` | Right |


}

### Approach 2: Linear Search (Less Efficient)

A straightforward approach is to perform a linear search. This is less efficient and not recommended for large arrays but can be useful for understanding the problem.

1. Loop through each element in the array and check if it is equal to the target.
2. If found, return the index; if not found by the end of the loop, return `-1`.

#### Time Complexity
The time complexity for this approach is $O(n)$ as it checks each element once.

#### Space Complexity
The space complexity is $O(1)$, using no additional space.

### Code Implementation
```python
def linear_search(nums: List[int], target: int) -> int:
    for index, num in enumerate(nums):
        if num == target:
            return index
    return -1  # Target not found
```

### Summary of Approaches
| Approach                    | Time Complexity | Space Complexity | Description                                             |
|-----------------------------|------------------|------------------|---------------------------------------------------------|
| Modified Binary Search      | $O(\log n)$      | $O(1)$           | Efficiently searches using a modified binary search.    |
| Linear Search               | $O(n)$           | $O(1)$           | Simple but inefficient search through all elements.     |



```python
from typing import List, Callable

def test_search_function(search_func: Callable[[List[int], int], int]):
    """Tests the search function with various test cases."""
    test_cases = [
        {
            "name": "General Case 1",
            "input": ([4, 5, 6, 7, 0, 1, 2], 0),
            "expected": 4  # The target 0 is found at index 4.
        },
        {
            "name": "General Case 2",
            "input": ([4, 5, 6, 7, 0, 1, 2], 3),
            "expected": -1  # The target 3 is not present in the array.
        },
        {
            "name": "Single Element Present",
            "input": ([1], 1),
            "expected": 0  # The target 1 is the only element, found at index 0.
        },
        {
            "name": "Single Element Absent",
            "input": ([1], 0),
            "expected": -1  # The target 0 is not present in the array.
        },
        {
            "name": "Empty Array",
            "input": ([], 1),
            "expected": -1  # The array is empty, so the target cannot be found.
        },
        {
            "name": "Target is the Pivot",
            "input": ([2, 3, 4, 5, 1], 1),
            "expected": 4  # The target 1 is at index 4, which is the pivot point.
        },
        {
            "name": "Target in Rotated Array",
            "input": ([6, 7, 0, 1, 2, 4, 5], 0),
            "expected": 2  # The target 0 is found at index 2.
        },
        {
            "name": "Target Not in Rotated Array",
            "input": ([6, 7, 0, 1, 2, 4, 5], 3),
            "expected": -1  # The target 3 is not present in the array.
        },
        {
            "name": "Duplicates Present",
            "input": ([1, 0, 1, 1, 1], 0),
            "expected": 1  # The target 0 is found at index 1.
        },
        {
            "name": "Duplicates Not Present",
            "input": ([1, 1, 1, 1], 0),
            "expected": -1  # The target 0 is not present in the array.
        },
    ]

    for case in test_cases:
        result = search_func(*case["input"])
        assert result == case["expected"], f"Test failed for {case['name']}: expected {case['expected']}, got {result}"
    print("All tests passed!")


```



Similar: [[Find min in rotated sorted array]]

