
[LeetCode #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)


### 1. **Remove Duplicates from Sorted Array**
- **Problem**: Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and return the new array.
- **Example**:
  - Input: `nums = [1, 1, 2]`
  - Output:  `[1, 2]`



```markdown
## Example 1

**Input:** 
```python
nums = [1, 1, 2]
```

**Output:** 
```python
2, nums = [1, 2, _]
```
**Explanation:** Return `k = 2`; the first two elements are `1` and `2`. The rest can be ignored.

---

## Example 2

**Input:** 
```python
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
```

**Output:** 
```python
5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
```
**Explanation:** Return `k = 5`; the first five elements are `0`, `1`, `2`, `3`, and `4`. The rest can be ignored.


Custom Judge:

The judge will test your solution with the following code:
```python


int[] nums = [...]; // Input array

int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;

for (int i = 0; i < k; i++) {

assert nums[i] == expectedNums[i];

}
```
If all assertions pass, then your solution will be accepted.


  Here are a few different approaches to solve the problem of removing duplicates from a sorted array, each with a distinct technique:

  ### 1. **Two-pointer Approach (Efficient In-place Method)**
  This is the approach we discussed earlier, using two pointers to traverse and overwrite duplicates in the original array.

  #### Steps:
  1. Initialize two pointers: `index` to track the position of unique elements and `i` to traverse the array.
  2. If `arr[i]` is different from `arr[index]`, move `index` forward and assign `arr[i]` to `arr[index]`.
  3. Finally, slice the array up to `index + 1` to get the array without duplicates.


```python

def remove_duplicates2(nums):
    checked_index = 0
    for j in range(1, len(nums)):
        if nums[j-1] != nums[j]:
            checked_index += 1
            nums[checked_index] = nums[j]

    return nums[:checked_index+1]


```


```python

def remove_duplicates(nums):
    index = 0
    for i in range(1, len(nums)):
        if(nums[index]!= nums[i]):
            index += 1
            nums[index] = nums[i]
    return nums[:index+1]


```


```python
from typing import List

def remove_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0  # Return 0 if the list is empty

    # Initialize the slow pointer
    slow: int = 1

    # Iterate with the fast pointer
    for fast in range(1, len(nums)):
        # If the current element is not a duplicate
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]  # Update the position of the slow pointer
            slow += 1  # Move the slow pointer forward

    return slow  # Return the new length of the array

# Example usage
nums = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(nums)
print(f"Length of array after removing duplicates: {new_length}")
print(f"Array after duplicates removed: {nums[:new_length]}")  # Print the modified array

```


  #### Complexity:
  - **Time**: O(n)
  - **Space**: O(1)

  ---

  ### 2. **Set-based Approach**
  You can convert the list into a set, which automatically removes duplicates, and then convert it back into a sorted list.

  #### Steps:
  1. Convert the array to a `set`.
  2. Convert the set back to a `sorted` list, since sets are unordered.

  #### Code:
  ```python
  def remove_duplicates(arr):
      return sorted(set(arr))
  ```

  #### Complexity:
  - **Time**: O(n log n) (due to sorting)
  - **Space**: O(n)

  **Pros**: Simple and elegant, especially for unsorted arrays.
  **Cons**: This approach doesn't maintain the original order unless you sort the result.

  ---

  ### 3. **Iterative Approach (Using Extra Array)**
  Instead of modifying the input array in place, create a new array to store unique elements by iterating through the input array.

  #### Steps:
  1. Create a new list `result`.
  2. Iterate through the input array and add an element to `result` only if it’s not the same as the last element added to `result`.

  #### Code:
  ```python
  def remove_duplicates(arr):
      if not arr:
          return arr

      result = [arr[0]]

      for i in range(1, len(arr)):
          if arr[i] != arr[i-1]:
              result.append(arr[i])

      return result
  ```


```python

def remove_duplicates1(nums):
    visited_set = set()
    nums_len = len(nums)
    for i in range(nums_len):
        if nums[i] not in visited_set:
            visited_set.add(nums[i])
            visited_set_length = len(visited_set)
            nums[visited_set_length - 1] = nums[i]

    return nums[:len(visited_set)]


```


  #### Complexity:
  - **Time**: O(n)
  - **Space**: O(n)

  **Pros**: Keeps the original array intact. Useful if you need a new array without changing the input.
  **Cons**: Uses extra space to store the result.

  ---

  ### 4. **Recursive Approach**
  You can also solve this problem recursively, where you compare each element with the previous one and build the result list.

  #### Steps:
  1. Base case: If the array is empty or has only one element, return it as is.
  2. Recursively process the remaining elements and only append the element if it's different from the previous one.

  #### Code:
  ```python
  def remove_duplicates(arr):
      if len(arr) <= 1:
          return arr

      # Recursively call the function for the rest of the array
      rest = remove_duplicates(arr[1:])

      # Add the first element only if it's different from the next one
      if arr[0] == rest[0]:
          return rest
      else:
          return [arr[0]] + rest
  ```

  #### Complexity:
  - **Time**: O(n)
  - **Space**: O(n) (due to the recursive call stack and the new array creation)

  **Pros**: Provides an interesting functional approach.
  **Cons**: Not as efficient due to recursion and additional space overhead.

  ---

  ### 5. **Hash Map Counting Approach (for Unsorted Arrays)**
  This approach is not necessary for a sorted array but can be used for unsorted arrays. A hash map (dictionary) is used to track the frequency of elements.

  #### Steps:
  1. Create a hash map (or dictionary) to count occurrences of each element.
  2. Iterate through the array and add elements to the result array only if they haven’t been added before.

  #### Code:
  ```python
  def remove_duplicates(arr):
      seen = {}
      result = []

      for num in arr:
          if num not in seen:
              seen[num] = True
              result.append(num)

      return result
  ```

  #### Complexity:
  - **Time**: O(n)
  - **Space**: O(n)

  **Pros**: Works well for unsorted arrays.
  **Cons**: Extra space needed for the hash map.

  ---

  ### Summary of Approaches:
  1. **Two-pointer**: Best for in-place removal with O(1) space complexity.
  2. **Set-based**: Simple and elegant, but requires sorting and O(n) space.
  3. **Iterative (with extra array)**: Keeps original array intact, but uses extra space.
  4. **Recursive**: Functional but less efficient due to recursion depth and extra space.
  5. **Hash Map Counting**: Useful for unsorted arrays, but adds overhead of a hash map.

  Each approach has its trade-offs depending on the input and the specific requirements (e.g., in-place modification, preserving order, etc.).




#### Tests

```python

def test_remove_duplicates(func):
    print(f"Testing function: {func.__name__}")

    remove_duplicates_test_cases = [
        # Case 1: General case with duplicates
        {
            "name": "General Case",
            "input": [1, 1, 2],
            "expected_array": [1, 2],
        },

        # Case 2: All unique elements
        {
            "name": "All Unique",
            "input": [1, 2, 3, 4, 5],
            "expected_array": [1, 2, 3, 4, 5],
        },

        # Case 3: All elements are the same
        {
            "name": "All Duplicates",
            "input": [2, 2, 2, 2, 2],
            "expected_array": [2],
        },

        # Case 4: Empty array
        {
            "name": "Empty Array",
            "input": [],
            "expected_array": [],
        },

        # Case 5: Single element array
        {
            "name": "Single Element",
            "input": [5],
            "expected_array": [5],
        },

        # Case 6: Larger input with consecutive duplicates
        {
            "name": "Larger Input with Duplicates",
            "input": [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7],
            "expected_array": [1, 2, 3, 4, 5, 6, 7],
        },

        # Case 7: Alternating duplicates
        {
            "name": "Alternating Duplicates",
            "input": [1, 2, 2, 3, 4, 4, 5],
            "expected_array": [1, 2, 3, 4, 5],
        },
    ]

    for i, test_case in enumerate(remove_duplicates_test_cases, 1):
        input_data = test_case["input"]
        expected_array = test_case["expected_array"]
        case_name = test_case["name"]

        # Clone input to avoid modifying test cases' original input
        input_clone = input_data[:]

        result_array = func(input_clone)

        # Check if the returned array matches the expected array
        assert (
            result_array == expected_array
        ), f"Test case {i} ({case_name}) failed: expected array {expected_array}, got {result_array}"

    print("All test cases passed!")


```
