


## Trapping Rain Water (LeetCode #42)

https://leetcode.com/problems/trapping-rain-water/description/



### Problem Statement

Given an array `height` of non-negative integers representing the elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

#### Example:

**Input:**

```plaintext
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

**Output:**

```plaintext
6
```

**Explanation:** The elevation map `height` is visualized as follows:

```
    # 
    #     #
#   # ##  ###
################
 0  1 0 2 1 0 1 3 2 1 2 1
```

The water trapped is represented as empty spaces filled between the bars.

---

### Key Observations

To trap water above a bar at index `i`, the water level depends on:

1. The **maximum height to the left** of the bar.
2. The **maximum height to the right** of the bar.

The trapped water at index `i` can be calculated as:

water[i]=max⁡(0,min⁡(left_max[i],right_max[i])−height[i])\text{water[i]} = \max(0, \min(\text{left\_max[i]}, \text{right\_max[i]}) - \text{height[i]})

---

own brute force: ( not worked)

fails at {"input": [4,2,3], "expected": 1},


```python


def findFirstDecIndex(ary:List):
    for i in range(1,len(ary)):
        if(ary[i]<ary[i-1]):
            return i-1
    return -1

def trimmedAry(ary):
    firstIndex = findFirstDecIndex(ary)
    if(firstIndex == -1):
        return []
    lastFirstIndex =  findFirstDecIndex(ary[::-1])
    if(lastFirstIndex == -1):
        return []
    lastIndex = len(ary) - lastFirstIndex - 1
    if( lastIndex == firstIndex):
         return []
    return ary[firstIndex: lastIndex+1]

def value_find(ary5, need_trim = True):
    trimAry = trimmedAry(ary5) if need_trim else ary5
    print(trimAry)
    if(len(trimAry) == 0):
        return 0
    max = trimAry[0]
    items_inc_after_max = []
    ans = 0
    for i in range(1,len(trimAry)):
        val = trimAry[i]
        if(val < max):
            items_inc_after_max.append(max- val)
        else:
            ans += sum(items_inc_after_max)
            items_inc_after_max = []
            max = val

    if(not items_inc_after_max):
        return ans
    else:
        return ans + value_find(trimAry[len(trimAry)-len(items_inc_after_max):], False)


```


---


### Approach 1: Brute Force (Time Complexity: O(n2)O(n^2))

For each index ii, calculate the maximum height to the left and right of ii and use it to determine the trapped water.

#### Code:

```python
def trap(height):
    n = len(height)
    if n == 0:
        return 0

    water_trapped = 0

    for i in range(n):
        left_max = max(height[:i+1])  # Max height to the left of index i
        right_max = max(height[i:])  # Max height to the right of index i

        # Calculate water trapped at index i
        water_trapped += max(0, min(left_max, right_max) - height[i])

    return water_trapped
```

#### Complexity:

- **Time Complexity**: O(n2)O(n^2), because finding `left_max` and `right_max` for each index takes O(n)O(n).
- **Space Complexity**: O(1)O(1), no additional data structures are used.

---

### Approach 2: Precompute Arrays (Time Complexity: O(n)O(n))

Instead of recomputing `left_max` and `right_max` for each index, we can precompute them using two arrays:

1. `left_max[i]`: Maximum height to the left of index ii.
2. `right_max[i]`: Maximum height to the right of index ii.

#### Steps:

1. Populate the `left_max` array by scanning from left to right.
2. Populate the `right_max` array by scanning from right to left.
3. Calculate trapped water using: water[i]=max⁡(0,min⁡(left_max[i],right_max[i])−height[i])\text{water[i]} = \max(0, \min(\text{left\_max[i]}, \text{right\_max[i]}) - \text{height[i]})

#### Code:

```python
def trap(height):
    n = len(height)
    if n == 0:
        return 0

    # Initialize arrays
    left_max = [0] * n
    right_max = [0] * n

    # Compute left_max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Compute right_max array
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Calculate trapped water
    water_trapped = 0
    for i in range(n):
        water_trapped += max(0, min(left_max[i], right_max[i]) - height[i])

    return water_trapped
```

#### Complexity:

- **Time Complexity**: O(n)O(n), because we traverse the array three times (to populate `left_max`, `right_max`, and compute trapped water).
- **Space Complexity**: O(n)O(n), for the `left_max` and `right_max` arrays.

---

### Approach 3: Two Pointers (Time Complexity: O(n)O(n), Space Complexity: O(1)O(1))

Instead of using arrays to store `left_max` and `right_max`, we use two pointers:

1. A **left pointer** that moves from the left end of the array.
2. A **right pointer** that moves from the right end of the array.

#### Key Idea:

- Keep track of `left_max` and `right_max` while traversing the array.
- Water trapped is determined by the smaller of the two maximums at the pointers.

#### Steps:

1. Initialize `left` to 0 and `right` to n−1n - 1.
2. While left<rightleft < right:
    - If `height[left] < height[right]`, calculate water trapped at `left` and move `left` pointer.
    - Otherwise, calculate water trapped at `right` and move `right` pointer.

#### Code:

```python
def trap(height):
    n = len(height)
    if n == 0:
        return 0

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            # Update left_max and calculate water trapped
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
            left += 1
        else:
            # Update right_max and calculate water trapped
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])
            right -= 1

    return water_trapped
```


```python

class Solution:
    def trap(self, height: List[int]) -> int:
        if (not height):
            return 0
        
        left,right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        water = 0

        while (left < right):
            if (left_max < right_max):
                left += 1
                new_left_val = height[left]
                left_max = max(new_left_val, left_max)
                water += left_max - new_left_val
            else:
                right -= 1
                new_right_val = height[right]
                right_max = max(new_right_val, right_max)
                water += right_max - new_right_val
        
        return water


```

#### Complexity:

- **Time Complexity**: O(n)O(n), as we traverse the array once.
- **Space Complexity**: O(1)O(1), no additional data structures are used.

---

### Comparison of Approaches

|Approach|Time Complexity|Space Complexity|Notes|
|---|---|---|---|
|**Brute Force**|O(n2)O(n^2)|O(1)O(1)|Slow for large inputs due to repeated calculations.|
|**Precompute**|O(n)O(n)|O(n)O(n)|Efficient, but requires extra space.|
|**Two Pointers**|O(n)O(n)|O(1)O(1)|Most efficient in terms of time and space.|

---

### Test Cases

```python
def test_trap(func):
    print(f"Testing function: {func.__name__}")

	test_cases = [
        {"input": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], "expected": 6},
        {"input": [4, 2, 0, 3, 2, 5], "expected": 9},
        {"input": [], "expected": 0},
        {"input": [1, 0, 1], "expected": 1},
        {"input": [2, 0, 2], "expected": 2},
        {"input": [3, 0, 2, 0, 4], "expected": 7},
        {"input": [4,2,3], "expected": 1},
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]

        result = func(input_data)
        assert result == expected_output, \
            f"Test case {i} failed: expected {expected_output}, got {result}"

    print("All test cases passed!")

# Example usage:
test_trap(trap)  # Replace 'trap' with the function being tested
```

---

### Summary

- The **Two Pointers** approach is the most efficient, with O(n)O(n) time and O(1)O(1) space complexity.
- The **Precompute Arrays** approach is also efficient but uses more space.
- Avoid the **Brute Force** approach for large inputs.

Understanding and implementing the **Two Pointers** approach is essential for mastering this problem, as it strikes the perfect balance between simplicity and efficiency.






referred {

https://www.youtube.com/watch?v=8cqpkCreiwM

}

Others code:

Runtime: 0ms

python

```python
class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        total_snow = 0
        left_max = right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_snow += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_snow += right_max - height[right]
                right -= 1

        return total_snow
```


Memory: 17.7mb

python

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
```

