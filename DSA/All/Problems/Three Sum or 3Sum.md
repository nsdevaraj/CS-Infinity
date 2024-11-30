
 [LeetCode #15 - 3Sum](https://leetcode.com/problems/3sum)

[3 sum - AlgoEngine](https://www.youtube.com/watch?v=IIxoo93bmPQ)


## Problem Statement

Given an integer array `nums`, return **all the triplets** `[nums[i], nums[j], nums[k]]` such that:
- \( i \neq j \neq k \)
- \( nums[i] + nums[j] + nums[k] = 0 \)

The solution set must not contain duplicate triplets.

### Example 1:
```
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

### Example 2:
```
Input: nums = []
Output: []
```

### Example 3:
```
Input: nums = [0]
Output: []
```

---

## Approach 1: Brute Force

### Explanation
The most naive approach is to check all combinations of triplets in the array and determine if their sum equals 0. This requires iterating through every combination of three elements, which leads to a time complexity of \( O(n^3) \).

### Steps:
1. Iterate over every triplet \( (i, j, k) \) where \( i < j < k \).
2. Check if \( nums[i] + nums[j] + nums[k] = 0 \).
3. If true, add the triplet to the result set, ensuring no duplicates.

### Code
```python
from typing import List

def three_sum_brute_force(nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)
    
    # Check all combinations of triplets
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                        result.append(triplet)
    
    return result
```

### Time Complexity:
- **Time complexity:** \( O(n^3) \), because we are checking every combination of three numbers.
- **Space complexity:** \( O(n) \), to store the result.

---

## Approach 2: Two Pointer Technique ( optimal)

### Explanation
A more efficient way to solve this is to use sorting and the two-pointer technique. This reduces the time complexity to \( O(n^2) \).

### Steps:
1. Sort the array.
2. Iterate through the array. For each number, use two pointers: one starting from the left and one from the right of the current number to find the sum that equals zero.
3. Skip duplicate values to avoid duplicate triplets in the result.

### Code
```python
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array first
    result = []
    n = len(nums)
    
    for i in range(n - 2):
	    # since sorted, first value can't be above zero , since consec value also be above zero, then their sum never be zero
	    if nums[i] > 0:
		    continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate values
        
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

### Time Complexity:
- **Time complexity:** \( O(n^2) \), where \( n \) is the number of elements in the array. Sorting takes \( O(n \log n) \) and the two-pointer traversal takes \( O(n^2) \).
- **Space complexity:** \( O(1) \), as we are only using constant extra space for pointers.

---

## Approach 3: Hashing (Avoid Duplicate Triplets)

### Explanation
This approach uses a hash set to track elements that have been seen so far and avoids duplicates using a combination of hashing and sorting.

### Steps:
1. Use a hash set to store the complement of the current two elements.
2. Check if the complement is already in the hash set. If yes, return the triplet.
3. Ensure that no duplicate triplets are added to the result.

### Code
```python
def three_sum_hashing(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to make triplet checking easier
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        
        seen = set()
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], nums[j], complement])
                
                # Skip duplicates for j
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
    
    return result
```

### Time Complexity:
- **Time complexity:** \( O(n^2) \). Sorting takes \( O(n \log n) \), and the rest takes \( O(n^2) \) due to the two-pointer traversal.
- **Space complexity:** \( O(n) \), due to the usage of the hash set.

---



## Summary of Approaches:

| Approach               | Time Complexity | Space Complexity | Explanation                                           |
|------------------------|-----------------|------------------|-------------------------------------------------------|
| Brute Force             | \( O(n^3) \)    | \( O(n) \)       | Check all triplets using three nested loops            |
| Two Pointers            | \( O(n^2) \)    | \( O(1) \)       | Sort the array and use two pointers to find the triplet|
| Hashing                 | \( O(n^2) \)    | \( O(n) \)       | Use hash set to find the complement of two elements    |

---

## Test Function

```python
def test_three_sum(func):
    test_cases = [
        {
            "name": "General Case 1",
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]],
        },
        {
            "name": "No Triplets",
            "input": [1, 2, 3],
            "expected": [],
        },
        {
            "name": "All Zeros",
            "input": [0, 0, 0, 0],
            "expected": [[0, 0, 0]],
        },
	    {
	        "name": "General Case 1",
	        "input": [-1, 0, 1, 2, -1, -4],
	        "expected": [[-1, -1, 2], [-1, 0, 1]],
	    },
	    {
	        "name": "No Triplets",
	        "input": [1, 2, 3],
	        "expected": [],
	    },
	    {
	        "name": "All Zeros",
	        "input": [0, 0, 0, 0],
	        "expected": [[0, 0, 0]],
	    },
	    {
	        "name": "Mixed Positives and Negatives",
	        "input": [-2, -1, 0, 1, 2],
	        "expected": [[-2, 0, 2], [-1, 0, 1]],
	    },
	    {
	        "name": "All Positive Numbers",
	        "input": [1, 2, 3, 4, 5],
	        "expected": [],
	    },
	    {
	        "name": "All Negative Numbers",
	        "input": [-5, -4, -3, -2, -1],
	        "expected": [],
	    },
	    {
	        "name": "Repeating Triplets",
	        "input": [-2, -2, 0, 0, 2, 2],
	        "expected": [[-2, 0, 2]],
	    },
	    {
	        "name": "Large Input with Triplets",
	        "input": [-10, -7, -3, -2, 0, 1, 2, 5, 8],
	        "expected": [[-10, 2, 8], [-7, -3, 10], [-2, 0, 2]],
	    },
	    {
	        "name": "Multiple Zero Elements",
	        "input": [0, 0, 0, 0],
	        "expected": [[0, 0, 0]],
	    },
	    {
	        "name": "Triplet in Large Range",
	        "input": [-1000, -500, 0, 500, 1000],
	        "expected": [[-1000, 0, 1000], [-500, 0, 500]],
	    },
    ]
    
    for i, test_case in enumerate(test_cases):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        
        result = func(input_data)
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected_output])
        
        assert result_sorted == expected_sorted, f"Test case {i + 1} failed: expected {expected_sorted}, got {result_sorted}"
    
    print("All test cases passed!")
```



Similar :
[[Two Sum or 2sum]]

few diffs of 3 sum from 2 sum:
- 3 vallues to 0
- return array values, not indices
- can have mulitple soln, give all ( excluding duplicates )

note: order not matter.. 

if only one unique soln is fine:

fix outer index and give 2 sum ..

```python

for i in range(len(nums)):
	complement = target - i
	# implement 2 sum of the complement

```



to check {


https://www.youtube.com/watch?v=EYeR-_1NRlQ


}


