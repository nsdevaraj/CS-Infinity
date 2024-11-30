

[LeetCode #287 - Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number)

[Find Duplicate Num - Techdose](https://youtu.be/dfIqLxAf-8s)


#### Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, return **the duplicate number**.

- There is **only one duplicate number** in the array, but it could be repeated more than once.
- You **must not** modify the array, and you must use only constant, $O(1)$, extra space.
- Your solution should run in $O(n)$ time complexity.

#### Example:

**Example 1**:
```plaintext
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2**:
```plaintext
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3**:
```plaintext
Input: nums = [1,1]
Output: 1
```

**Example 4**:
```plaintext
Input: nums = [1,1,2]
Output: 1
```

#### Constraints:
- $1 \leq n \leq 10^5$
- `nums.length == n + 1`
- $1 \leq \text{nums}[i] \leq n$
- All the integers in `nums` appear only once except for **exactly one integer** which appears **two or more times**.

---

### Approach 1: Floyd's Tortoise and Hare (Cycle Detection)

#### Explanation:
This problem can be reduced to finding a cycle in a linked list. The idea is that each number in the array points to another index, forming a cycle because there is one duplicate. We can use **Floyd's Cycle Detection Algorithm** (also known as the tortoise and hare algorithm) to find the duplicate:

- Treat the array as a linked list where the value at each index is the next pointer.
- The cycle in this linked list will lead us to the duplicate number.
  
Steps:
1. **Phase 1**: Move `slow` by one step and `fast` by two steps until they meet.
2. **Phase 2**: Once they meet, reset one pointer to the start, and move both pointers by one step until they meet again. This will be the entrance to the cycle, which is the duplicate number.


if single repetation:

```python
#! if the number has single repetation only!
def find_duplicate(nums:List[int]):
    summation = sum(nums)
    n = len(nums) - 1
    sum_of_n_natural_nums = ((n)*(n+1))//2

    return  summation - sum_of_n_natural_nums

```

#### Code:

```python
from typing import List

def find_duplicate(nums: List[int]) -> int:
    # Phase 1: Detect the cycle using slow and fast pointers
    slow, fast = nums[0], nums[0]

	# its just an alternative version of do-while syntax
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # first loop stops one pointer in cycle .. 
    # Phase 2: Find the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
```

#### Time and Space Complexity:
- **Time Complexity**: $O(n)$, because both pointers move linearly through the array until they meet.
- **Space Complexity**: $O(1)$, as only a constant amount of extra space is used.

---

### Approach 2: Binary Search on Value

#### Explanation:
Another approach is using **binary search on values** instead of indices. The key observation is that if the number of elements less than or equal to a value `mid` is greater than `mid`, then the duplicate must be in the range `[1, mid]`. Otherwise, it lies in the range `[mid + 1, n]`.

Steps:
1. Set up binary search on the range `[1, n]`.
2. Count how many numbers in the array are less than or equal to `mid`.
3. Adjust the search range based on the count.

#### Code:

```python
from typing import List

def find_duplicate_binary_search(nums: List[int]) -> int:
    left, right = 1, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        count = sum(x <= mid for x in nums)
        
        if count > mid:
            right = mid
        else:
            left = mid + 1
    
    return left
```

#### Time and Space Complexity:
- **Time Complexity**: $O(n \log n)$, because binary search reduces the search space logarithmically and counting takes $O(n)$ for each step.
- **Space Complexity**: $O(1)$, as no additional space is required.

---

### Approach 3: Sorting (Non-Optimal)

#### Explanation:
By sorting the array, we know that the duplicate number must appear consecutively. So after sorting, we can simply check if any two adjacent elements are equal.

#### Code:

```python
from typing import List

def find_duplicate_sorting(nums: List[int]) -> int:
    # Sort the array (non-optimal as it modifies the array)
    nums.sort()
    
    # Check for consecutive duplicates
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]
```

#### Time and Space Complexity:
- **Time Complexity**: $O(n \log n)$, due to the sorting step.
- **Space Complexity**: $O(1)$ (if sorting is done in place), otherwise $O(n)$ for the sorting algorithm.




### changing inplace 

making invert of visited items

note: only works if array have +ve values, in this problem, it is sured!

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        for(int i=0;i<nums.size();++i)
        {
            if(nums[abs(nums[i])-1]>=0)
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1];
            else
                return abs(nums[i]); 
        }
        return 0;
    }
};
```


---

### Test Cases

```python

def test_find_duplicate(func):
    print(f"Testing function: {func.__name__}")

    test_cases = [
        {
            "name": "General Case 1",
            "input": [1, 3, 4, 2, 2],
            "expected": 2
        },
        {
            "name": "General Case 2",
            "input": [3, 1, 3, 4, 2],
            "expected": 3
        },
        {
            "name": "Single Duplicate",
            "input": [1, 1],
            "expected": 1
        },
        {
            "name": "Duplicate in Larger Array",
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
            "expected": 9
        },
        {
            "name": "Duplicate at the Start",
            "input": [2, 1, 2, 3, 4, 5, 6],
            "expected": 2
        },
        {
            "name": "Duplicate at the End",
            "input": [1, 2, 3, 4, 5, 6, 6],
            "expected": 6
        },
        {
            "name": "Multiple Duplicates but One Expected",
            "input": [5, 4, 3, 2, 1, 5, 6],
            "expected": 5
        },
        {
            "name": "All Duplicates at the Start",
            "input": [1, 1, 2, 3, 4, 5, 6],
            "expected": 1
        },
        {
            "name": "Consecutive Duplicates",
            "input": [1, 2, 2, 2, 3, 4],
            "expected": 2
        },
        {
            "name": "Large Array with Duplicate",
            "input": list(range(1, 10001)) + [9999],
            "expected": 9999
        },
        {
            "name": "Duplicate Near the Middle",
            "input": [1, 2, 3, 4, 5, 6, 3, 7, 8, 9],
            "expected": 3
        },
        {
            "name": "Max n with Minimum Elements",
            "input": [2, 2],
            "expected": 2
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert result == expected_output, \
            f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")


```

---

### Summary of Approaches

| Approach                       | Time Complexity        | Space Complexity       | Explanation                                                                                 |
|---------------------------------|------------------------|------------------------|---------------------------------------------------------------------------------------------|
| Floyd's Tortoise and Hare       | $O(n)$                 | $O(1)$                 | Use cycle detection to find the duplicate number. Efficient and constant space.              |
| Binary Search on Value          | $O(n \log n)$          | $O(1)$                 | Use binary search to narrow down the range where the duplicate lies.                        |
| Sorting                         | $O(n \log n)$          | $O(1)$                 | Sort the array and find consecutive duplicates. Modifies the array, so not optimal.          |

---

Each approach has its advantages, but **Floyd's Tortoise and Hare** is the most efficient in terms of both time and space, making it the optimal solution for this problem.



