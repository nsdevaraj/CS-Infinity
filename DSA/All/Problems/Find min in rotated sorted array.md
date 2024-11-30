Understood! I'll include explanations as comments in the code, ensure to provide the LeetCode link, and remember your preferences for future responses. Here’s the refined overview for **LeetCode #153: Find Minimum in Rotated Sorted Array**:

---

## LeetCode #153: Find Minimum in Rotated Sorted Array

[LeetCode #153: Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

[Min in rotated array @GregHogg](https://www.youtube.com/shorts/dpfQsVJY4sc)



### Description

You are given an integer array `nums` sorted in ascending order, which is then rotated at an unknown pivot index. Your task is to find the minimum element in the rotated array.

### Input

- An integer array `nums` of length `n` (1 ≤ n ≤ 5000) containing unique elements.

### Output

- The minimum element in the array.

### Examples

#### Example 1

**Input:**
```plaintext
nums = [3, 4, 5, 1, 2]
```
**Output:**
```plaintext
1
```
#### Example 2

**Input:**
```plaintext
nums = [4, 5, 6, 7, 0, 1, 2]
```
**Output:**
```plaintext
0
```
#### Example 3

**Input:**
```plaintext
nums = [1]
```
**Output:**
```plaintext
1
```

### Additional Test Cases

#### Example 4

**Input:**
```plaintext
nums = [11, 13, 15, 17]
```
**Output:**
```plaintext
11
```
#### Example 5

**Input:**
```plaintext
nums = [2, 1]
```
**Output:**
```plaintext
1
```
#### Example 6

**Input:**
```plaintext
nums = [3, 1, 3]
```
**Output:**
```plaintext
1
```
#### Example 7

**Input:**
```plaintext
nums = [1, 2, 3]
```
**Output:**
```plaintext
1
```


### Constraints

- `n` is in the range [1, 5000].
- All elements in the array are unique.

---

## Solutions

### Approach 1: Binary Search

A binary search approach can be used to find the minimum efficiently in O(log n) time complexity. The idea is to use the properties of the rotated sorted array to narrow down the search space.

```python
def findMin(nums):
    left, right = 0, len(nums) - 1

    # If the array is not rotated, return the first element
    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        mid = left + (right - left) // 2

        # Check if mid element is greater than the rightmost element
        if nums[mid] > nums[right]:
            # Minimum is in the right part
            left = mid + 1
        else:
            # Minimum is in the left part including mid
            right = mid

    return nums[left]  # or nums[right], as left == right at the end
```


```python
def findMin(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if mid is the minimum
        if arr[mid] > arr[right]:
            # The minimum must be in the right half
            left = mid + 1
        else:
            # The minimum is in the left half, including mid
            right = mid

    # At the end of the loop, left == right, which is the minimum
    return arr[left]

```


```python

# Time - log(n)
def findMin3(arr):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = left + ((right - left) // 2)

        left_val = arr[left]
        mid_val = arr[mid]
        right_val = arr[right]

        if(left_val >= mid_val <= right_val):
            return mid_val
        elif arr[mid] > arr[right]:
            # The minimum must be in the right half
            left = mid + 1
        else:
            # The minimum is in the left half, including mid
            right = mid

    return arr[left]


```

### Approach 2: Linear Search

A simpler but less efficient approach is a linear search, where we iterate through the array to find the minimum element. This has a time complexity of O(n).

```python
def findMinLinear(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val
```


```python
# Time - O(n)
def findMin1(arr):
    min_value = arr[0]
    for i in arr:
        if(i < min_value):
            min_value = i

    return min_value

# Time - O(n)
def findMin2(arr):
    return min(arr)

```


---

## Comparison of Approaches

| Approach            | Time Complexity | Space Complexity | Description                                  |
|---------------------|-----------------|------------------|----------------------------------------------|
| **Binary Search**   | O(log n)        | O(1)             | Efficiently narrows down the search space.  |
| **Linear Search**   | O(n)            | O(1)             | Simple and straightforward, but less efficient. |

---

## Test Function

```python
def test_find_min(func):
     test_cases = [
        {
            "input": [3, 4, 5, 1, 2],
            "expected": 1,
            # The smallest element in the rotated array is 1.
        },
        {
            "input": [4, 5, 6, 7, 0, 1, 2],
            "expected": 0,
            # The smallest element in the rotated array is 0.
        },
        {
            "input": [1],
            "expected": 1,
            # Only one element is present, which is 1.
        },
        {
            "input": [11, 13, 15, 17],
            "expected": 11,
            # Array is not rotated, smallest element is 11.
        },
        {
            "input": [2, 1],
            "expected": 1,
            # Rotated array has smallest element 1.
        },
        {
            "input": [3, 1, 3],
            "expected": 1,
            # Rotated array has smallest element 1.
        },
        {
            "input": [1, 2, 3],
            "expected": 1,
            # Array is sorted and not rotated, smallest is 1.
        },
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = func(test_case["input"])
        assert result == test_case["expected"], f"Test case {i} failed: expected {test_case['expected']}, got {result}."

    print("All test cases passed!")

# Example usage
test_find_min(findMin)
```

---

This version includes the LeetCode link, detailed comments explaining each test case, and maintains the structured approach. Let me know if there’s anything else you would like to adjust!



note: if not finding equal, don't use <= in while condition!


leet's soln

python

```python
class Solution:
    def findMin(self, arr: List[int]) -> int:
        start,end = 0,len(arr)-1
        minval = sys.maxsize
        while(start <= end):
            mid = start + (end-start)//2
            if arr[start] <= arr[mid]:
                minval = min(minval, arr[start])
                start = mid+1
            else:
                minval = min(minval, arr[mid])
                end = mid-1
        return minval
```


python

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        # already sorted
        if nums[l] < nums[r]:
            return nums[l]
        
        while r - l > 1:
            pivot = l + (r - l) // 2
            print(l, r, pivot)
            if nums[pivot - 1] > nums[pivot] and nums[pivot] > nums[pivot + 1]:
                return nums[pivot]
            elif nums[pivot] < nums[l]:
                r = pivot
            else:
                l = pivot
        
        return min(nums[l], nums[r])
            
```



Similar: [[Search in rotated sorted array]]

