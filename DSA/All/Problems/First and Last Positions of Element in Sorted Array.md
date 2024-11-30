

[LeetCode #34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

[first and last positions in sorted array @GFG](https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/)


Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.


**Example 1:**

**Input:** nums = [5,7,7,8,8,10], target = 8
**Output:** [3,4]

**Example 2:**

**Input:** nums = [5,7,7,8,8,10], target = 6
**Output:** [-1,-1]

**Example 3:**

**Input:** nums = [], target = 0
**Output:** [-1,-1]


### Linear Search


```python

# if unsorted array given , do sorting on your own

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    # Edge case: if nums is empty or target is not in nums, return [-1, -1]
    if not nums or target not in nums:
        return [-1, -1]
    
    # Sort nums to handle the case where positions should be found in sorted order
    nums.sort()  # Note: Sorting could change the original indices
    positions = [-1, -1]  # Initialize result list

    # Find the first occurrence of the target
    # nums.index(x)
    for i in range(len(nums)):
        if nums[i] == target:
            positions[0] = i  # Set the first position
            break
    
    # Find the last occurrence of the target
    # nums[::-1].index(x)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            positions[1] = i  # Set the last position
            break

    return positions

# Time Complexity: O(n log n) due to sorting (where n is the length of nums).
# Space Complexity: O(1) if sorting can be done in-place, else O(n) for additional sorting storage.

```




```python
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]  # Initialize result for start and end positions

    # Find the first occurrence of target
    for start in range(len(nums)):
        if nums[start] == target:
            result[0] = start  # Update start position

            # Find the last occurrence of target from the end of the list
            end = len(nums) - 1
            while end > start:
                if nums[end] == target:
                    break
                end -= 1

            result[1] = end  # Update end position
            break  # Exit after finding both positions

    return result
```


```python
def searchRange(self, nums: List[int], target: int) -> List[int]:
	first,last = -1,-1
	for i in range(len(nums)):
	
		if nums[i]==target:
			
			if first==-1:
				first=i
			
			last=i
			
	return [first,last]
```



- **Time Complexity**: \(O(n)\)
  - The outer loop iterates through the list up to finding the first occurrence of `target`, which could take \(O(n)\) in the worst case.
  - The inner `while` loop then searches backwards to find the last occurrence, adding up to \(O(n)\) overall.
  
- **Space Complexity**: \(O(1)\)
  - Only a fixed-size list (`result`) is used, so the space complexity is constant.


### Binary Search


Here’s the refactored Java code with simplified comments, clearer variable names, and precise complexity analysis:

```ts
function searchRange(nums: number[], target: number): number[] {
    // Find the left and right bounds of the target in the array
    const left = findLeftBound(nums, target);
    const right = findRightBound(nums, target);
    return [left, right];
}

function findLeftBound(nums: number[], target: number): number {
    let index = -1;
    let low = 0, high = nums.length - 1;

    // Binary search to find the leftmost (first) occurrence of target
    while (low <= high) {
        const mid = low + Math.floor((high - low) / 2);

        if (nums[mid] === target) {
            index = mid;      // Potential left bound found
            high = mid - 1;   // Move left to find earlier occurrence
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return index;
}

function findRightBound(nums: number[], target: number): number {
    let index = -1;
    let low = 0, high = nums.length - 1;

    // Binary search to find the rightmost (last) occurrence of target
    while (low <= high) {
        const mid = low + Math.floor((high - low) / 2);

        if (nums[mid] === target) {
            index = mid;      // Potential right bound found
            low = mid + 1;    // Move right to find later occurrence
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return index;
}
```

### Time and Space Complexity Analysis

- **Time Complexity**: \(O(\log n)\)
  - Each binary search (`findLeftBound` and `findRightBound`) runs in \(O(\log n)\), making the overall time complexity \(O(\log n)\).
  
- **Space Complexity**: \(O(1)\)
  - The algorithm uses a constant amount of extra space for variables and no additional data structures, so the space complexity is constant.



```python
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    # Helper function to perform binary search for target's left or right boundary
    def binary_search(start: int = 0, find_left_bound: bool = True) -> int:
        left, right = start, len(nums) - 1
        position = -1  # Initialize as -1 in case target is not found

        while left <= right:
            mid = left + (right - left) // 2  # Calculate mid-point
            if nums[mid] == target:
                position = mid  # Target found, store position
                # Narrow search to find the exact boundary
                if find_left_bound:
                    right = mid - 1  # Search left side for leftmost position
                else:
                    left = mid + 1   # Search right side for rightmost position
            elif nums[mid] > target:
                right = mid - 1  # Target is in left half
            else:
                left = mid + 1   # Target is in right half

        return position

    # Find leftmost and rightmost positions of target
    left_pos = binary_search(find_left_bound=True)
    right_pos = -1 if left_pos == -1 else binary_search(left_pos, find_left_bound=False)

    return [left_pos, right_pos]


# Time Complexity: O(log n) for each binary search, so O(log n) in total, as we perform two binary searches.
# Space Complexity: O(1), as we only use a constant amount of extra space.
```



```python

from typing import List

def find_start(arr: List[int], target: int) -> int:
    # If target is at the beginning of the array
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    
    # Binary search for the starting index of the target
    while left <= right:
        mid = (left + right) // 2
        # Check if mid is the first occurrence of target
        if arr[mid] == target and arr[mid - 1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Move right if target is larger
        else:
            right = mid - 1  # Move left if target is smaller
    
    return -1  # Return -1 if target not found

def find_end(arr: List[int], target: int) -> int:
    # If target is at the end of the array
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    
    # Binary search for the ending index of the target
    while left <= right:
        mid = (left + right) // 2
        # Check if mid is the last occurrence of target
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid - 1  # Move left if target is smaller
        else:
            left = mid + 1  # Move right if target is larger
    
    return -1  # Return -1 if target not found

def first_and_last(arr: List[int], target: int) -> List[int]:
    # Edge case: check if array is empty or target is out of range
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    
    # Find starting and ending positions of target
    start = find_start(arr, target)
    end = find_end(arr, target)
    
    return [start, end]  # Return result as [start, end]


```

---


[First and last index in sorted array - YT(InsideCode)](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=298s)

[LeetCode #34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)


### Problem Statement: First and Last Position in a Sorted Array

Given a **sorted** array of integers `arr` and an integer `target`, find the **first** and **last** positions of the `target` in the array. If the `target` cannot be found, return `[-1, -1]`.

#### Example:
**Input:**
```plaintext
arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9], target = 5
```

**Output:**
```plaintext
[2, 6]
```
Explanation: The first occurrence of `5` is at index `2`, and the last occurrence is at index `6`.

---

### Approach 1: Linear Search

We start by traversing the array to find the first occurrence of the target. Once we find it, we continue scanning the array to find the last occurrence. This is simple, but it can be improved given the array is sorted.

#### Code Implementation:

```python
def first_and_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i + 1] == target:
                i += 1
            return [start, i]
    return [-1, -1]

```

```python
from typing import List

def find_first_and_last_linear(arr: List[int], target: int) -> List[int]:
    n = len(arr)
    start, end = -1, -1
    
    # Linear traversal to find the first and last positions
    for i in range(n):
        if arr[i] == target:
            if start == -1:
                start = i  # First occurrence
            end = i  # Keep updating for last occurrence
    
    return [start, end]
```


```python

from typing import List

def find_first_and_last_linear(arr: List[int], target: int) -> List[int]:
    n = len(arr)
    start, end = -1, -1

    # Linear traversal to find the first and last positions
    for i in range(n):
        if arr[i] == target:
            if start == -1:
                start = i  # First occurrence
            end = i  # Keep updating for last occurrence
        else:
            if(end != i):
                return [start, end]

    return [start, end]

```


#### Time Complexity: 
- In the **worst case**, we traverse all the elements in the array, which gives us $O(n)$ time complexity.

#### Space Complexity:
- Since we only use a few variables, the space complexity is $O(1)$.

---

### Approach 2: Binary Search for Optimized Search

Since the array is sorted, we can use **binary search** to efficiently find the first and last positions. The binary search will reduce the search space by half at every step.


```python


def find_first_last_index  (arr:List[int], target:int)-> List[int]:
    arrLen = len(arr)

    # binary search
    [left,right] = [0,arrLen-1]
    found_idx = -1
    while(left<=right):
        mid = (left + right) // 2
        midElm = arr[mid]

        if(target == midElm):
            found_idx = mid
            break
        elif(target < midElm):
            right = mid -1
        else:
            left = mid+1

    [start_idx, end_idx] = [-1,-1]

    # handle duplicates
    if(found_idx != -1):
        [start_idx, end_idx] = [found_idx, found_idx]
        while(start_idx > -1 and arr[start_idx] == target):
            start_idx -= 1
        start_idx += 1

        while(end_idx < arrLen and arr[end_idx] == target):
            end_idx += 1
        end_idx -= 1


    return [start_idx, end_idx]



```


when the whole array contains only targets with more duplicates, then the finding first / last index by iteration is not a good move... 


```python
def find_start(arr, target):
    left, right = 0, len(arr) - 1
    start = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            start = mid
            right = mid - 1  # Keep searching to the left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return start

def find_end(arr, target):
    left, right = 0, len(arr) - 1
    end = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            end = mid
            left = mid + 1  # Keep searching to the right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return end

def first_and_last(arr, target):
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]

# Example usage:
arr = [5, 7, 7, 8, 8, 10]
target = 8
print(first_and_last(arr, target))  # Output: [3, 4]

```

#### Finding the First Occurrence
In this step, we use binary search to find the first occurrence of the target. We add an extra condition to ensure that the element to the left of the found element (if it exists) is smaller than the target.

#### Finding the Last Occurrence
Similarly, we use binary search again to find the last occurrence. Here, we ensure the element to the right of the found element is greater than the target.

#### Early Exit

An even more efficient version can include early exit conditions to handle specific edge cases like:
1. If the array is empty.
2. If the `target` is smaller than the first element or larger than the last.


#### Code Implementation:
```python
def find_start(arr, target):
    # Check if the first element is the target
    if arr[0] == target:
        return 0
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        # Check if we found the target and it's the first occurrence
        if arr[mid] == target and (mid == 0 or arr[mid - 1] < target):
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Target not found

def find_end(arr, target):
    # Check if the last element is the target
    if arr[-1] == target:
        return len(arr) - 1
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        # Check if we found the target and it's the last occurrence
        if arr[mid] == target and (mid == len(arr) - 1 or arr[mid + 1] > target):
            return mid
        elif arr[mid] > target:
            right = mid - 1  # Search in the left half
        else:
            left = mid + 1  # Search in the right half
            
    return -1  # Target not found

def first_and_last(arr, target):
    # Check for edge cases: empty array or target out of range
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    
    # Find the start and end indices of the target
    start = find_start(arr, target)
    end = find_end(arr, target)
    
    return [start, end]  # Return the start and end indices

# Example usage:
arr = [5, 7, 7, 8, 8, 10]
target = 8
print(first_and_last(arr, target))  # Output: [3, 4]

```

#### Time Complexity:
- Binary search reduces the time complexity to $O(\log n)$, as it divides the search space by half at each step.
- Since we run two binary searches (one for the first occurrence and one for the last), the total complexity is $2 \times O(\log n) = O(\log n)$.

#### Space Complexity:
- We use a constant amount of space, so the space complexity is $O(1)$.


---

### Summary of Approaches

| Approach               | Time Complexity | Space Complexity | Explanation                                                                                         |
|------------------------|-----------------|------------------|-----------------------------------------------------------------------------------------------------|
| **Linear Search**       | $O(n)$          | $O(1)$           | Traverse the entire array to find the first and last occurrence.                                      |
| **Binary Search**       | $O(\log n)$     | $O(1)$           | Use binary search twice to find the first and last occurrence in a more optimized way.                |


