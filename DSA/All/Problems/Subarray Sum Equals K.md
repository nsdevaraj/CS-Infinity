



referred {

https://youtu.be/HbbYPQc-Oo4?si=9wlXbIojHa0fJ9DF


}

# Problem: 560. Subarray Sum Equals K

[**LeetCode Link**](https://leetcode.com/problems/subarray-sum-equals-k/)

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of **continuous subarrays** whose sum equals `k`.

---

### Example 1:

```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: There are two subarrays [1,1] with sum = 2.
```

### Example 2:

```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: Subarrays are [1,2] and [3].
```

### Constraints:

- 1≤nums.length≤2×1041 \leq nums.length \leq 2 \times 10^4
- −104≤nums[i]≤104-10^4 \leq nums[i] \leq 10^4
- −107≤k≤107-10^7 \leq k \leq 10^7

---


Code

Python3

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        sum_map = {}
        target_count = 0
        for num in nums:
            running_sum += num
            remain = running_sum - k

            if running_sum == k:
                target_count += 1

            if remain in sum_map:
                target_count += sum_map[remain]
            
            if running_sum in sum_map:
                sum_map[running_sum] += 1
            else:
                sum_map[running_sum]  = 1
        
        return target_count



```


---


## Approach 1: Brute Force

### Explanation:

1. Iterate through all possible subarrays using two nested loops.
2. Compute the sum of each subarray.
3. Increment the count if the sum equals kk.

### Code:

```python
from typing import List

def subarray_sum_brute_force(nums: List[int], k: int) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1
    return count
```

### Complexity:

- **Time Complexity:** O(n2)O(n^2), because of the nested loops iterating through all subarrays.
- **Space Complexity:** O(1)O(1), as no extra space is used.

---

## Approach 2: Prefix Sum with Hash Map (Optimal)

### Explanation:

This approach uses a hash map to store the frequency of **prefix sums** and checks for the required subarrays in O(1)O(1).

1. Maintain a running sum of the array (`prefix_sum`).
2. For each element:
    - Check if `prefix_sum - k` exists in the hash map. If it does, it means there's a subarray with a sum equal to kk.
    - Update the hash map to include the current `prefix_sum`.

### Code:

```python
from typing import List
from collections import defaultdict

def subarray_sum(nums: List[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 1  # Initialize with a prefix sum of 0

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] += 1

    return count
```

### Complexity:

- **Time Complexity:** O(n)O(n), as we traverse the array once.
- **Space Complexity:** O(n)O(n), to store the hash map.

---

## Approach 3: Sliding Window (For Non-Negative Integers)

### Explanation:

If all numbers are non-negative, we can use the sliding window technique:

1. Use two pointers (`start` and `end`) to define a window.
2. Expand the window by moving `end` and add to the sum.
3. Shrink the window by moving `start` if the sum exceeds kk.

### Code:

```python
def subarray_sum_sliding_window(nums: List[int], k: int) -> int:
    count = 0
    start = 0
    current_sum = 0

    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum > k and start <= end:
            current_sum -= nums[start]
            start += 1
        if current_sum == k:
            count += 1
    return count
```

### Complexity:

- **Time Complexity:** O(n)O(n), but only works for non-negative arrays.
- **Space Complexity:** O(1)O(1).

---

## Test Cases

```python
def test_subarray_sum(func):
    test_cases = [
        {"nums": [1, 1, 1], "k": 2, "expected": 2},
        {"nums": [1, 2, 3], "k": 3, "expected": 2},
        {"nums": [1, -1, 0], "k": 0, "expected": 3},  # Subarrays: [1, -1], [0], [1, -1, 0]
        {"nums": [0, 0, 0, 0], "k": 0, "expected": 10},  # All subarrays of zeros
        {"nums": [-1, -1, 1], "k": 0, "expected": 1},  # Subarray: [-1, -1, 1]
        {"nums": [3, 4, 7, 2, -3, 1, 4, 2], "k": 7, "expected": 4},  # Multiple subarrays
        {"nums": [1], "k": 1, "expected": 1},
        {"nums": [1], "k": 0, "expected": 0},
        {"nums": [10, 2, -2, -20, 10], "k": -10, "expected": 3},  # Includes negative numbers
        {"nums": [1000] * 20000, "k": 1000, "expected": 20000},  # Large input with simple subarrays
    ]
    for i, test in enumerate(test_cases):
        result = func(test["nums"], test["k"])
        assert result == test["expected"], f"Test case {i + 1} failed: Expected {test['expected']}, got {result}"
    print("All test cases passed!")
```

### Run Tests

```python
test_subarray_sum(subarray_sum)
```

---

## Summary of Approaches

|Approach|Time Complexity|Space Complexity|Explanation|
|---|---|---|---|
|Brute Force|O(n2)O(n^2)|O(1)O(1)|Check all subarrays using nested loops.|
|Prefix Sum with Hash Map|O(n)O(n)|O(n)O(n)|Use a hash map to track prefix sums.|
|Sliding Window|O(n)O(n)|O(1)O(1)|Only works for non-negative arrays.|

---

### Key Insights:

1. The **hash map with prefix sum** is the most efficient solution for all inputs.
2. The **sliding window** method is limited to non-negative numbers but is faster with lower space requirements.
3. The brute force approach should only be used for small arrays or conceptual understanding.



---


others:

Runtime: 11ms

python

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        subarraySums = {0 : 1}
        prefixSum = 0
        for num in nums:
            prefixSum += num
            subarrays += subarraySums.get(prefixSum - k, 0)
            subarraySums[prefixSum] = subarraySums.get(prefixSum, 0) + 1
        return subarrays
```



Runtime: 47ms

python

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        d=defaultdict(int)
        d[0]=1
        s=0
        for i in nums:
            s+=i
            c+=d[s-k]
            d[s]+=1
        return c
        
```


Memory: 18.9mb

python

```python
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = collections.Counter()
        counts[nums[0]] += 1
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            counts[nums[i]] += 1
        total = counts[k]
        for n in nums:
            counts[n] -= 1
            total += counts[k + n]
        return total
```



Memory: 19.4mb

python

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        count = 0
        d = {0: 1}

        for i in nums:
            if i-k in d:
                count+=d[i-k]
            d[i] = d.get(i,0)+1
            
        return count
        
```


Memory: 21.1mb

python

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        array = [0 for _ in nums]
        array[0] = nums[0]
        counter = 0
        if array[0] == k:
                counter+=1
        
        umap = {array[0]:1}
        for i in range(1, len(nums)):
            array[i] = nums[i]+array[i-1]
            if array[i] == k:
                counter+=1
            if array[i]-k in umap:
                counter += umap[array[i]-k]
            umap[array[i]] = umap.get(array[i],0) + 1
             
        return counter
```


### **6. Subarray Sum Equals K**

**Problem**: Count the number of subarrays that sum to `k`.

**Code**:

```python
def subarray_sum(nums, k):
    count = prefix_sum = 0
    prefix_sums = {0: 1}
    for num in nums:
        prefix_sum += num
        count += prefix_sums.get(prefix_sum - k, 0)
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
    return count

# Example
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Output: 2
```
