8.	Move Zeroes
•	Problem: Given an array nums, write a function to move all 0's to the end while maintaining the relative order of the non-zero elements.
•	Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]



The problem of moving zeroes to the end while maintaining the relative order of non-zero elements can be solved using various approaches with different time and space complexities. Here are a few common approaches:

### 1. **Brute Force with Extra Space (O(n) Time, O(n) Space)**

- **Idea**: Create a new array, place all the non-zero elements in order, then append zeros to the rest.
- **Time Complexity**: O(n), where n is the number of elements in the array.
- **Space Complexity**: O(n), because of the extra array.

```python
def moveZeroes(nums):
    result = []

    # Append all non-zero elements to result
    for num in nums:
        if num != 0:
            result.append(num)

    # Append zeroes at the end
    result.extend([0] * (len(nums) - len(result)))

    # Copy the result back to the original array
    for i in range(len(nums)):
        nums[i] = result[i]

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

### 2. **Two-Pointer Approach (O(n) Time, O(1) Space)**

- **Idea**: Use two pointers. One pointer (`last_non_zero_found_at`) keeps track of the index of the last non-zero element, while the other pointer (`current`) traverses the array. When a non-zero is found, swap it with the element at `last_non_zero_found_at`, then increment both pointers.
- **Time Complexity**: O(n), because we pass through the array once.
- **Space Complexity**: O(1), since we modify the array in place.

```python
def moveZeroes(nums):
    last_non_zero_found_at = 0

    # Move all non-zero elements forward
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero_found_at], nums[current] = nums[current], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

### 3. **Shift Non-Zero Elements First, Then Fill Zeroes (O(n) Time, O(1) Space)**

- **Idea**: Traverse the array and move all non-zero elements to the front, then fill the remaining positions with zeroes.
- **Time Complexity**: O(n).
- **Space Complexity**: O(1), because the operation is done in place without using additional data structures.

```python
def moveZeroes(nums):
    # First pass: Move all non-zero elements to the front
    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1

    # Second pass: Fill the rest of the array with zeroes
    for i in range(index, len(nums)):
        nums[i] = 0

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

### 4. **Optimal Approach: One-Pass In-Place (O(n) Time, O(1) Space)**

- **Idea**: Similar to the two-pointer approach, but instead of swapping, the non-zero element is moved to its correct position immediately, and the rest of the array is filled with zeroes in the same pass.
- **Time Complexity**: O(n), since the array is traversed once.
- **Space Complexity**: O(1), as no additional memory is used.

```python
def moveZeroes(nums):
    index = 0

    # Move all non-zero elements to the front
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1

    # Fill remaining positions with zeroes
    while index < len(nums):
        nums[index] = 0
        index += 1

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

### Summary of Approaches:
1. **Brute Force**: Easiest to implement but uses extra space.
2. **Two-Pointer Approach**: Efficient, in-place solution that maintains order.
3. **Shift Non-Zero, Fill Zeroes**: Separate the process into two passes; first pass moves non-zeroes, second pass fills zeroes.
4. **Optimal Approach**: Combines shifting and zero-filling into a single pass.

The most efficient and recommended solution is the two-pointer approach due to its time and space efficiency (O(n) and O(1), respectively).
