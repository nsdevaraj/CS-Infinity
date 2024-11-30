

[? Maximum Subarray @LeetCode#53](https://leetcode.com/problems/maximum-subarray/)

Referred :
https://www.youtube.com/watch?v=5WZl3MMT0Eg




# 53. Maximum Subarray


## Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
A **subarray** is a contiguous **non-empty** sequence of elements within an array.
## Examples

### Example 1

**Input:** 


```plaintext
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

**Output:** 
```plaintext
6
```
**Explanation:** The subarray `[4, -1, 2, 1]` has the largest sum `6`.

### Example 2

**Input:** 
```plaintext
nums = [1]
```

**Output:** 
```plaintext
1
```
**Explanation:** The subarray `[1]` has the largest sum `1`.

### Example 3

**Input:** 
```plaintext
nums = [5, 4, -1, 7, 8]
```

**Output:** 
```plaintext
23
```
**Explanation:** The subarray `[5, 4, -1, 7, 8]` has the largest sum `23`.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`




```python

'''
sub-array : contiguous elements of an array

when all are only +ve numbers, the max subArray must be the whole array
when all are only -ve numbers, the max subArray must be the largest number

'''

```


```python

'''
Approach: Brute Force Iteration
- find all possible subarrays and calculate the sum of each subarray
- keep track of the maximum sum found so far, and return it at the end
- Time complexity: O(n^3) since we have two nested loops and inside sum function is also O(n)
- Space complexity: O(1) since we are not using any extra space
'''
def max_subarray1(nums):
    max_value = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub_array_sum = sum(nums[i : j + 1])
            if sub_array_sum > max_value:
                max_value = sub_array_sum
    return max_value


```




```python

'''
Approach: Brute Force Iteration (Optimized)
- Instead of calculating the sum of each subarray from scratch, we can reuse the sum of the previous subarray
- This way, we can calculate the sum of the current subarray by adding the new element to the previous sum
- Time complexity: O(n^2) since we have two nested loops, but the inner loop is optimized
- Space complexity: O(1) since we are not using any extra space
'''
def max_subarray2(nums):
    max_value = float('-inf')
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_value = max(max_value, current_sum)
    return max_value

```



```python


def max_subarray3(nums):
    # recusive apporach (divide and conqueror)
    # ToDo: implement this from readme file
    return -1


```



```python

'''
Approach: Kadane's Algorithm
# to find the max sum of subarray with current element,
# we consider max sum of subarray ending at previous element and add current element to it
# i.e extending the new element to the previous subarray or starting a new subarray with current element

- take 1st element as max_value and current_max_value
- iterate over the array from 2nd element and find taking element or just that element gives max sum
- check new max sum with the max_value and update max_value if new max sum is greater
- Time complexity: O(n) since we are iterating over the array once
- Space complexity: O(1) since we are using only two variables
'''

def max_subarray4(nums):
    if not nums:
        return float('-inf')
    max_value = nums[0]
    current_max_value = nums[0]
    for num in nums[1:]:
        current_max_value = max(current_max_value + num, num)
        max_value = max(max_value, current_max_value)
    return max_value

```


Yes, you can solve the maximum subarray problem using recursion. One common recursive approach is to use the **divide and conquer** technique. Here’s how it works:


### Divide and Conquer Approach

1. **Divide**: Split the array into two halves.
2. **Conquer**: Recursively find the maximum subarray sum in the left half, the right half,
and the maximum subarray that crosses the midpoint.
3. **Combine**: The result is the maximum of these three values.

### Implementation

Here's a Python implementation of this approach:

```python
def max_crossing_sum(nums, left, mid, right):
    # Include elements on the left of mid
    left_sum = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += nums[i]
        left_sum = max(left_sum, current_sum)

    # Include elements on the right of mid
    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += nums[i]
        right_sum = max(right_sum, current_sum)

    # Return sum of elements on left and right of mid
    return left_sum + right_sum

def max_subarray_recursive(nums, left, right):
    if left == right:  # Base case: only one element
        return nums[left]

    mid = (left + right) // 2

    # Find maximum subarray sum in left half, right half, and crossing subarray
    left_max = max_subarray_recursive(nums, left, mid)
    right_max = max_subarray_recursive(nums, mid + 1, right)
    crossing_max = max_crossing_sum(nums, left, mid, right)

    return max(left_max, right_max, crossing_max)

def max_subarray(nums):
    if not nums:
        return float('-inf')  # Handle empty array case
    return max_subarray_recursive(nums, 0, len(nums) - 1)
```

### Time Complexity

The time complexity of this recursive approach is \( O(n \log n) \):

- The array is split into two halves, which gives a logarithmic depth of recursion (\( \log n \)).
- Each level of recursion requires \( O(n) \) time to calculate the maximum crossing sum.

### Space Complexity

The space complexity is \( O(\log n) \) due to the recursion stack. However, if you want to avoid this stack overhead, you could implement this iteratively, but that would lose the recursive aspect.
'''


The **maximum subarray problem** involves finding a contiguous subarray within a one-dimensional array of numbers (both positive and negative) that has the largest sum. Several approaches can be used to solve this problem, each with varying time complexities. Here are different solutions:

### 1. **Brute Force (O(n²))**
The brute-force method checks all possible subarrays, computes their sums, and keeps track of the maximum sum found.

#### Algorithm:
- Iterate over each possible starting point of a subarray.
- For each starting point, iterate over each possible ending point.
- Calculate the sum for each subarray and update the maximum sum.

```python
def max_subarray_bruteforce(arr):
    max_sum = float('-inf')
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum
```

### 2. **Kadane's Algorithm (O(n))**
Kadane's algorithm efficiently finds the maximum sum by keeping track of the current subarray sum and the global maximum sum.

#### Algorithm:
- Initialize two variables: `max_current` for the current subarray and `max_global` for the maximum found so far.
- Iterate through the array, updating `max_current` with the maximum of the current element or the sum of the current element and the previous subarray.
- Update `max_global` whenever `max_current` exceeds it.

```python
def max_subarray_kadane(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)
    return max_global
```



```python
from typing import List

def max_sub_array(nums: List[int]) -> int:
    # Initialize current maximum sum and overall maximum sum
    current_sum = nums[0]
    max_sum = nums[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Update current sum to be the maximum of the current element or 
        # the current element plus the previous sum
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update overall maximum sum if current sum is greater
        max_sum = max(current_sum, max_sum)

    return max_sum  # Return the overall maximum sum

```


```python
from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    # Initialize the best sum ending at the first element and the best overall sum
    current_sum = nums[0]
    max_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # If current sum is negative, start a new subarray from the current number
        if current_sum < 0:
            current_sum = num
        else:
            # Otherwise, add the current number to the current sum
            current_sum += num
        
        # Update the maximum sum found so far
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

```




```python
from typing import List

def max_sub_ary(nums: List[int]) -> float:
    """
    Find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

    Args:
    nums (List[int]): A list of integers.

    Returns:
    float: The maximum sum of the subarray. Returns negative infinity if the list is empty.
    """
    
    # Edge case: if the input list is empty, return negative infinity
    if not nums:
        return float('-inf')

    # Initialize max_sum and current_sum with the first element of the array
    max_sum = nums[0]
    current_sum = nums[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Current element to consider
        current_element = nums[i]

        # Calculate the potential new current_sum by including the current element
        included_current_sum = current_sum + current_element

        # Update current_sum: either include the current element or start a new subarray
        if included_current_sum > current_element:
            current_sum = included_current_sum
        else:
            current_sum = current_element

        # Update max_sum if the current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

```

### 3. **Divide and Conquer (O(n log n))**
This method is based on divide-and-conquer principles, similar to merge sort. The idea is to divide the array into two halves, recursively find the maximum subarray sum for both halves, and then find the maximum subarray that crosses the middle of the array.

#### Algorithm:
- Divide the array into two halves.
- Recursively compute the maximum subarray sum in the left half, the right half, and the subarray that crosses the middle.
- The result is the maximum of the three values.

```python
def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left-1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total

    right_sum = float('-inf')
    total = 0
    for i in range(mid+1, right+1):
        total += arr[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum

def max_subarray_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2
    left_max = max_subarray_divide_conquer(arr, left, mid)
    right_max = max_subarray_divide_conquer(arr, mid+1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)

def max_subarray(arr):
    return max_subarray_divide_conquer(arr, 0, len(arr)-1)
```


```typescript

function maxSubArrayCrossing(nums: number[], start: number, mid: number, end: number): number {
    let leftSum = -Infinity;
    let rightSum = -Infinity;

    // Calculate left max sum
    let total = 0;
    for (let i = mid; i >= start; i--) {
        total += nums[i];
        leftSum = Math.max(leftSum, total);
    }

    // Calculate right max sum
    total = 0;
    for (let j = mid + 1; j <= end; j++) {
        total += nums[j];
        rightSum = Math.max(rightSum, total);
    }

    return leftSum + rightSum;
}

function maxSubArrayBetweenIndices(nums: number[], start: number, end: number): number {
    if (start === end) {
        return nums[start];
    }

    const mid = Math.floor((start + end) / 2);

    return Math.max(
        maxSubArrayBetweenIndices(nums, start, mid),
        maxSubArrayBetweenIndices(nums, mid + 1, end),
        maxSubArrayCrossing(nums, start, mid, end)
    );
}

function maxSubArray(nums: number[]): number {
    if (nums.length === 0) return 0;
    return maxSubArrayBetweenIndices(nums, 0, nums.length - 1);
}

// Example usage
console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])); // Output: 6


```



### 4. **Dynamic Programming (O(n))**
This is similar to Kadane's algorithm but explicitly uses an array to store the maximum subarray sum ending at each index.

#### Algorithm:
- Create a `dp` array where `dp[i]` stores the maximum subarray sum ending at index `i`.
- At each index, update `dp[i]` as the maximum of `arr[i]` or `arr[i] + dp[i-1]`.
- Track the maximum value in the `dp` array.

```python
def max_subarray_dp(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    max_sum = dp[0]

    for i in range(1, len(arr)):
        dp[i] = max(arr[i], arr[i] + dp[i-1])
        max_sum = max(max_sum, dp[i])

    return max_sum
```

### 5. **Prefix Sum Approach (O(n²))**
In this approach, we compute prefix sums and use them to find subarray sums more efficiently than a brute force approach.

#### Algorithm:
- Compute a prefix sum array where each element at index `i` is the sum of the elements from `arr[0]` to `arr[i]`.
- For each subarray starting at `i` and ending at `j`, the subarray sum can be computed as `prefix[j] - prefix[i-1]`.

```python
def max_subarray_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    max_sum = float('-inf')
    for i in range(1, len(prefix)):
        for j in range(i, len(prefix)):
            max_sum = max(max_sum, prefix[j] - prefix[i - 1])

    return max_sum
```

### Summary
- **Brute Force (O(n²))**: Simple but slow.
- **Kadane's Algorithm (O(n))**: Fastest and most efficient for this problem.
- **Divide and Conquer (O(n log n))**: Slower than Kadane but good for understanding the problem recursively.
- **Dynamic Programming (O(n))**: A variation of Kadane’s that stores intermediate results.
- **Prefix Sum (O(n²))**: Faster than brute force, but still not optimal.

For most use cases, **Kadane’s Algorithm** is the best solution due to its optimal time complexity and simplicity.



### Test

```python

max_subarray_test_cases = [
    # Case 1: General case with mixed positive and negative numbers
    {
        "name": "General Case with Mixed Values",
        "input": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        "expected": 6,
    }, # max subarray is [4, -1, 2, 1]
    # Case 2: All negative numbers
    {
        "name": "All Negative Numbers",
        "input": [-1, -2, -3, -4],
        "expected": -1,
    },  # max subarray is [-1]
    # Case 3: All positive numbers
    {
        "name": "All Positive Numbers",
        "input": [1, 2, 3, 4],
        "expected": 10,
    },  # max subarray is [1, 2, 3, 4]
    # Case 4: Single positive element
    {
        "name": "Single Positive Element",
        "input": [5],
        "expected": 5,
    },  # max subarray is [5]
    # Case 5: Single negative element
    {
        "name": "Single Negative Element",
        "input": [-3],
        "expected": -3,
    },  # max subarray is [-3]
    # Case 6: Subarray within negatives
    {
        "name": "Subarray in Middle of Negatives",
        "input": [2, -1, 2, 3, -4],
        "expected": 6,
    },  # max subarray is [2, -1, 2, 3]
    # Case 7: Large array with all negatives except one positive
    {
        "name": "Negatives with One Positive",
        "input": [-1, -2, -3, -4, 5],
        "expected": 5,
    },  # max subarray is [5]
    # Case 8: Array with alternating positive and negative values
    {
        "name": "Alternating Positive and Negative Values",
        "input": [-1, 2, -3, 4, -5, 6],
        "expected": 6,
    },  # max subarray is [4, -5, 6]
    # Case 9: Includes zero values
    {
        "name": "Includes Zero Values",
        "input": [0, -2, 3, 0, 4, -1],
        "expected": 7,
    },  # max subarray is [3, 0, 4]
    # Case 10: Long array with maximum subarray at the start
    {
        "name": "Max Subarray at Start",
        "input": [6, -1, -8, 4, 3],
        "expected": 7,
    },  # max subarray is [4,3]
    # Case 11: Large array with alternating positive and negative values
    {
        "name": "Large Alternating Values",
        "input": [3, -1, 2, 1, -3, 4, -2, 5, -1, 2],
        "expected": 10,
    },  # max subarray is [3, -1, 2, 1, -3, 4, -2, 5, -1, 2]
    # Case 12: Empty array
    {
        "name": "Empty Array",
        "input": [],
        "expected": float('-inf'),
    }, # max subarray is []
    # Case 13: Large array with all positive values
    {
        "name": "Large Array of All Positive Values",
        "input": list(range(1, 1001)),
        "expected": 500500,
    }, # max subarray is [1, 2, 3, ..., 1000]
    # Case 14: Large array with all negative values
    {
        "name": "Large Array of All Negative Values",
        "input": [-i for i in range(1, 1001)],
        "expected": -1,
    },  # max subarray is [-1]
    # Case 15: Large mixed array with large positive and negative values
    {
        "name": "Large Mixed Values",
        "input": [1000, -500, 200, -100, 300, -200, 400],
        "expected": 1100,
    },  # max subarray is [1000, -500, 200, -100, 300, -200, 400]
    # Case 16: Large array where maximum subarray is at the end
    {
        "name": "Max Subarray at End",
        "input": [-1] * 500 + [2, 3, 4, 5],
        "expected": 14,
    },  # max subarray is [2, 3, 4, 5]
    # Case 17: Large array with fluctuating values
    {
        "name": "Fluctuating Values",
        "input": [i % 10 - 5 for i in range(100)],
        "expected": 10,
    },  # max subarray is [1,2,3,4]
    # Case 18: Very large input to test performance
    {
        "name": "Very Large Input for Performance Testing",
        "input": [i for i in range(-500, 500)],
        "expected": 124750,
    }, # max subarray is [0, 1, 2, ..., 499]
]


def test_max_subarray(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        max_subarray_test_cases, 1
    ):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert (
            result == expected_output
        ), f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")

```




looks Similar but really not similar : [[Maximum Product subArray]]



