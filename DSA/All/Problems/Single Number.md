
[LeetCode #136](https://leetcode.com/problems/single-number/description/)


Here’s the problem statement for "Single Number" in Markdown format:


# 136. Single Number

**Easy**

## Description

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Examples

### Example 1

**Input:** 
```plaintext
nums = [2, 2, 1]
```

**Output:** 
```plaintext
1
```

### Example 2

**Input:** 
```plaintext
nums = [4, 1, 2, 1, 2]
```

**Output:** 
```plaintext
4
```

### Example 3

**Input:** 
```plaintext
nums = [1]
```

**Output:** 
```plaintext
1
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.


## Answers

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

```

```python
from functools import reduce

def single_num(nums):
    return reduce(lambda x, y: x ^ y, nums)

# Example usage
print(single_num([2, 2, 1]))  # Output: 1

```


Here are three different approaches to solve the "Single Number" problem, each with TypeScript code, comments, and type annotations.

### Approach 1: XOR Operation

This approach leverages the property of XOR. When you XOR two identical numbers, the result is `0`. Thus, XORing all numbers in the array will leave only the unique number.

```typescript
function singleNumberXOR(nums: number[]): number {
    let result: number = 0;

    // XOR all numbers in the array
    for (let num of nums) {
        result ^= num; // Same numbers cancel each other out
    }

    return result; // The remaining number is the unique one
}

// Example usage
console.log(singleNumberXOR([2, 2, 1])); // Output: 1
```

### Approach 2: Hash Map

This approach uses a hash map to count the occurrences of each number. The unique number will have a count of `1`.

```typescript
function singleNumberHashMap(nums: number[]): number {
    const countMap: { [key: number]: number } = {};

    // Count occurrences of each number
    for (let num of nums) {
        countMap[num] = (countMap[num] || 0) + 1;
    }

    // Find the number that appears only once
    for (let num in countMap) {
        if (countMap[num] === 1) {
            return Number(num); // Return as number
        }
    }

    return -1; // Fallback (should not reach here based on problem constraints)
}

// Example usage
console.log(singleNumberHashMap([4, 1, 2, 1, 2])); // Output: 4
```

### Approach 3: Array Sorting

This approach sorts the array first. After sorting, the unique number will be next to duplicates, making it easy to find.

```typescript
function singleNumberSorting(nums: number[]): number {
    // Sort the array first
    nums.sort((a, b) => a - b);

    // Traverse the sorted array to find the unique number
    for (let i = 0; i < nums.length; i += 2) {
        // If we reach the last element or the current is not equal to the next, return it
        if (i === nums.length - 1 || nums[i] !== nums[i + 1]) {
            return nums[i];
        }
    }

    return -1; // Fallback (should not reach here based on problem constraints)
}

// Example usage
console.log(singleNumberSorting([1, 1, 2, 2, 3, 3, 4, 4, 5])); // Output: 5
```

### Summary of Approaches:

1. **XOR Operation**:
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1)
   - **Pros**: Optimal in both time and space.

2. **Hash Map**:
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)
   - **Pros**: Intuitive and straightforward.

3. **Array Sorting**:
   - **Time Complexity**: O(n log n)
   - **Space Complexity**: O(1) (in-place sort)
   - **Pros**: Simple, but less efficient due to sorting.

Each approach has its trade-offs, and the XOR method is typically the most efficient solution for this problem given the constraints.







### Tests

```python

def test_single_number(func):
    print(f"Testing function: {func.__name__}")

    single_number_test_cases = [
        # Case 1: General case with positive numbers
        {
            "name": "General Case with Positive Numbers",
            "input": [2, 2, 1],
            "expected": 1,
        },
        # Case 2: General case with mixed positive and negative numbers
        {
            "name": "Mixed Positive and Negative Numbers",
            "input": [4, 1, 2, 1, 2],
            "expected": 4,
        },
        # Case 3: Single element
        {
            "name": "Single Element",
            "input": [1],
            "expected": 1,
        },
        # Case 4: Larger input with one unique number
        {
            "name": "Larger Input with One Unique Number",
            "input": [1, 1, 2, 2, 3, 3, 4, 4, 5],
            "expected": 5,
        },
        # Case 5: Multiple pairs and one unique number
        {
            "name": "Multiple Pairs and One Unique",
            "input": [10, 10, 20, 20, 30, 30, 40],
            "expected": 40,
        },
        # Case 6: All negative numbers with one unique
        {
            "name": "All Negative Numbers with One Unique",
            "input": [-1, -2, -2, -3, -3],
            "expected": -1,
        },
        # Case 7: Larger array with many duplicates
        {
            "name": "Larger Array with Duplicates",
            "input": [5] * 999 + [10, 10, 15, 15],
            "expected": 5,
        },
        # Case 8: Array with only the unique number
        {
            "name": "Array with Only Unique Number",
            "input": [0, 0, 1, 1, 2],
            "expected": 2,
        },
        # Case 9: Large mixed numbers
        {
            "name": "Large Mixed Values",
            "input": [1000, 2000, 1000, 3000, 2000],
            "expected": 3000,
        },
    ]

    for i, test_case in enumerate(single_number_test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert result == expected_output, f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")

```