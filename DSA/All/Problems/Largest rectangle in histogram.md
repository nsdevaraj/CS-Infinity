

Certainly! Here's the first section for **Largest Rectangle in Histogram**.

---

### Largest Rectangle in Histogram

**LeetCode Problem**: [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

---

### Problem Statement

Given an array of integers `heights` representing the heights of bars in a histogram, find the largest rectangle that can be formed in the histogram. The width of each bar is `1`.

**Examples:**

1. **Input**: `heights = [2, 1, 5, 6, 2, 3]`
   - **Output**: `10`
   - **Explanation**: The largest rectangle has height `5` and width `2`, covering indices `[2, 3]`.
  
2. **Input**: `heights = [2, 4]`
   - **Output**: `4`
   - **Explanation**: The largest rectangle has height `4` and width `1`, covering index `[1]`.

---

### Approaches

There are multiple approaches to solving this problem, each with different levels of efficiency.

---

#### Approach 1: Brute Force with All Pairs

The brute force approach considers every pair of bars as potential boundaries of a rectangle. For each pair, we compute the minimum height between them and then calculate the rectangle area.

1. **Steps**:
   - Iterate through all pairs of bars to determine possible rectangles.
   - For each pair `(i, j)`, calculate the minimum height from `i` to `j` and then the area of the rectangle using this height and the width `(j - i + 1)`.
   - Track the maximum area across all possible rectangles.

2. **Code**:

   ```python
   from typing import List

   def largestRectangleAreaBruteForce(heights: List[int]) -> int:
       max_area = 0
       n = len(heights)
       
       for i in range(n):
           min_height = heights[i]
           for j in range(i, n):
               min_height = min(min_height, heights[j])
               area = min_height * (j - i + 1)
               max_area = max(max_area, area)
       
       return max_area
   ```

3. **Complexity Analysis**:
   - **Time Complexity**: \(O(n^3)\) due to the nested loops and minimum calculation.
   - **Space Complexity**: \(O(1)\), as we are only storing integers for the minimum height and max area.

---

#### Approach 2: Optimized Brute Force (Single Loop for Minimum Heights)

We can improve upon the previous approach by avoiding the re-computation of the minimum height for each pair of indices.

1. **Steps**:
   - For each bar at index `i`, treat it as the smallest bar in a rectangle.
   - Extend the rectangle to the left and right as long as the heights are greater than or equal to `heights[i]`.
   - Calculate the area using this width and update the maximum area found.

2. **Code**:

   ```python
   def largestRectangleAreaOptimizedBruteForce(heights: List[int]) -> int:
       max_area = 0
       n = len(heights)
       
       for i in range(n):
           height = heights[i]
           left = i
           right = i
           
           while left >= 0 and heights[left] >= height:
               left -= 1
           while right < n and heights[right] >= height:
               right += 1
           
           width = right - left - 1
           area = height * width
           max_area = max(max_area, area)
       
       return max_area
   ```


3. **Complexity Analysis**:
   - **Time Complexity**: \(O(n^2)\), as the inner loops left and right still depend on `n`.
   - **Space Complexity**: \(O(1)\).

---

#### Approach 3: Using a Stack (Optimal Solution)

Using a stack is an efficient solution to this problem. The idea is to find the "next smaller" and "previous smaller" bars for each bar in the histogram, which helps in calculating the largest rectangle for each bar efficiently.

1. **Steps**:
   - Traverse each bar in `heights`.
   - Use a stack to keep track of bars that are increasing in height.
   - For each bar, if the current bar height is less than the bar height at the top of the stack, calculate the area of the rectangle formed with the bar at the top of the stack as the smallest bar.
   - Repeat until the stack is empty or the top of the stack is less than the current bar.
   - Push the current bar index onto the stack and continue to the next bar.
   - Finally, calculate the area for remaining bars in the stack.

2. **Code**:

   ```python
   def largestRectangleAreaStack(heights: List[int]) -> int:
       max_area = 0
       stack = []
       heights.append(0)  # Append a sentinel value for easier computation
       
       for i, h in enumerate(heights):
           while stack and heights[stack[-1]] > h:
               height = heights[stack.pop()]
               width = i if not stack else i - stack[-1] - 1
               max_area = max(max_area, height * width)
           stack.append(i)
       
       heights.pop()  # Remove the sentinel value
       return max_area
   ```

3. **Complexity Analysis**:
   - **Time Complexity**: \(O(n)\), since each element is pushed and popped from the stack only once.
   - **Space Complexity**: \(O(n)\), due to the stack.

---

### Summary of Section 1

We explored three approaches for solving the Largest Rectangle in Histogram problem:

1. **Brute Force** – Simple but highly inefficient with \(O(n^3)\) time complexity.
2. **Optimized Brute Force** – Improves upon brute force by reducing duplicate minimum calculations, achieving \(O(n^2)\) time complexity.
3. **Stack-Based Solution** – The optimal approach with \(O(n)\) time complexity using a stack to efficiently calculate the maximum area.

Let me know if you'd like Section 2, which will include a detailed comparison of these approaches along with test cases for each.


### Section 2: Comparison of Approaches and Test Function with Distinct Test Cases

---

#### Comparison of Approaches

The following table compares each approach discussed in terms of complexity and performance:

| Approach                   | Description                                           | Time Complexity   | Space Complexity | Efficiency                    |
|----------------------------|-------------------------------------------------------|-------------------|------------------|--------------------------------|
| Brute Force                | Checks all rectangles, using each pair of indices as boundaries | \(O(n^3)\)        | \(O(1)\)         | Inefficient for large inputs |
| Optimized Brute Force      | Uses each bar as the smallest and extends left and right to maximize width | \(O(n^2)\) | \(O(1)\)         | Slightly better than brute force |
| Stack-Based Solution       | Finds largest rectangle by leveraging "next smaller" and "previous smaller" properties | \(O(n)\)          | \(O(n)\)         | Most efficient solution       |

The stack-based solution is optimal and commonly used for the "Largest Rectangle in Histogram" problem due to its linear time complexity.

---

#### Test Function and Distinct Test Cases

Here is a `test_largestRectangleArea` function that runs multiple test cases using each of the different approaches for comparison.

```python
from typing import List, Callable

def test_largestRectangleArea(func: Callable[[List[int]], int]) -> None:
    """
    Test function for validating the largestRectangleArea implementations.
    
    Args:
    func: Function to test that calculates the largest rectangle in a histogram.
    """

      test_cases = [
        # Basic case with mixed heights
        {"input": [2, 1, 5, 6, 2, 3], "expected": 10},  # Largest area is from height 5, width 2

        # Uniform height bars
        {"input": [2, 2, 2, 2], "expected": 8},         # Rectangle using entire histogram

        # Single bar (smallest case)
        {"input": [3], "expected": 3},                  # Only one bar, area is 3

        # Full
        {"input": [2, 4, 6, 5, 4, 2], "expected": 16},  # Largest rectangle covers [2, 4, 6, 5, 4, 2]

        # Decreasing heights
        {"input": [6, 5, 4, 3, 2, 1], "expected": 12},  # Using height 3, spanning 4 bars

        # Smallest rectangle scenario
        {"input": [1, 1, 1, 1, 1, 1], "expected": 6},   # All bars can be used for largest area

        # Sparse bars with 0s
        {"input": [0, 3, 0, 3, 0], "expected": 3},      # Rectangle only from the height-3 bars

        #
        {"input": [5, 6, 1, 6, 5], "expected": 10},     # Using heights [5, 6]

        # Multiple valleys and peaks
        {"input": [2, 1, 4, 5, 1, 3, 3], "expected": 8}, # Rectangle from heights 4 and 5

        # All zeros
        {"input": [0, 0, 0, 0], "expected": 0},         # No height, so area is 0
    ]

    for i, test in enumerate(test_cases):
        input_data = test["input"]
        expected = test["expected"]
        result = func(input_data)
        assert result == expected, f"Test case {i+1} failed: Input {input_data} Expected {expected}, but got {result}"
    print("All test cases passed!")

```


---

[Largest rectangle in histogram @InsideCode](https://www.youtube.com/watch?v=o3DUXPRyvT8&t=6459s)


Inside code : flow


## Brute force


```python

'''
BruteForce Approach:
    * take one candle, and check neighbours heigh accoumodate its height and expand.
Time: O(n**2) since n for looping each candle and n for expanding both sides
Space: O(1)
'''
# LeetCode : 87 / 99 testcases passed
def largestRectangleArea(heights:List[int])->int:
    max_area = 0
    heights_len = len(heights)

    for i in range(heights_len):
        left = i
        right = i
        cur_height = heights[i]

        while(left-1 > -1 and heights[left-1] >= cur_height):
            left -= 1

        while(right+1 < heights_len and heights[right+1] >= cur_height):
            right += 1

        width = right - left + 1
        area = cur_height * width

        max_area = max(area, max_area)

    return max_area

```



## Divide and Conquer


```python


'''
Divide and Conquer
* like merge sort, same here
* find min =>
        * min maybe largest area - min's height and whole width [all heights are same]
        * min's left may be largest area - now take min's left array
        * min's right may be largest area - now take min's right array

'''
def largestRectangleArea2(heights:List[int], left = 0, right = None, )-> int:

    heights_len = len(heights)

    if(right == None):
        right = heights_len - 1

    # increasing left can lead to above right
    if(left > right):
        return 0
    # decreasing right can lead to equal to left
    if(left == right):
        return heights[left]

    sub_array = heights[left:right+1]
    min_value = min(sub_array)
    # suport index for find index is important for handling duplicates
    min_index = heights.index(min_value, left, right+1)

    # current
    cur_max_area = min_value * len(sub_array)
    # in left subarray
    left_max_area = largestRectangleArea2(heights, left, min_index-1)
    # in right subarray
    right_max_area = largestRectangleArea2(heights, min_index+1, right)

    return max(cur_max_area, left_max_area, right_max_area)


```


Time: still `O(n^2)` since reducing N and finding min N...
but finding min N maybe made to O(logN) using segment tree.. 
so it can be reduced to O(NlogN)
n => reducing
n + logN => build tree + search 
build once + reduce and search => n + n (longN) => nLogn



## Stack 

Brute force approach => but expanding left and right is the things that we can get rid of..  instead of expanding everytime, have track of visited items in stack .. 


iterate and find for each index, grow left index
iterate and find for each index, grow right index
iterate each index and find area for each with grow left and right value saved!


```python
# time - x times O(n) => O(n)
# space - x times O(n) => O(n)
def largestRectangleArea3(heights):

    # expanding for logic bounds
    temp_heights = [-1] + heights + [-1]
    temp_heights_len = len(temp_heights)

    # next sorted bar for left
    from_left = [0]*temp_heights_len

    # allow bound logic -1 presence in stack always
    # present indices representing as ordered ones
    stack = [0]

    i = 1
    while(i<temp_heights_len-1):
        # maintain order by popup out bigger values
        while(temp_heights[i] <= temp_heights[stack[-1]]):
            stack.pop()

        # maintain left next sorted of current
        from_left[i] = stack[-1]
        # push current to sorted
        stack.append(i)
        i += 1

    from_right = [0]*temp_heights_len

    stack = [temp_heights_len-1]
    i = temp_heights_len-2
    while(i>0):
        # maintain order by popup out bigger values
        while(temp_heights[i]  <=temp_heights[stack[-1]]):
            stack.pop()

        # maintain right next sorted of current
        from_right[i] = stack[-1]
        stack.append(i)
        i -= 1

    max_area = 0
    for i in range(1, temp_heights_len-1):
        # -1 for not counting extra bounds for width here
        width = from_right[i] - from_left[i] - 1
        area = temp_heights[i] * width
        max_area = max(area, max_area)

    return max_area

```



## Stack optimized

while popup out, calculate area from current before to poping out items.
while pushing , also push heights and upto poped index for next poping area clac...


```python


# Time - O(n) - revolving
# Space - O(n) - stack 
def largestRectangeArea4(heights:List[int])-> int:
    # adding for logic bounds
    heights = [-1]+ heights + [-1]
    max_area = 0
    # string both index and height
    stack =  [(0,-1)]

    heights_len = len(heights)

    # not revolving the bounds
    for i in range(1, heights_len-1):
        start = i
        while(stack[-1][1] > heights[i]):
            top_index, top_height = stack.pop()
            # calc area of poping items
            max_area = max(max_area, top_height * ( i - top_index))
            # maintain start last poped items's index
            start = top_index
        
        stack.append((start, heights[i]))
    
    # Process remaining elements in the stack
    for i, height in stack[1:]:
        max_area = max(max_area, height * (heights_len - i - 1))
    
    return max_area
```


Leet code others soln:

Runtime: 59ms

python

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Adding a zero avoids ending with incomplete rects
        heights.append(0)
        # profile[i] = (h, s) -> A rectangle of height h can start as far back as index s. Sorted by height
        profile = []
        largest_area = 0
        prev_h = 0
        for i, height in enumerate(heights):
            if height == prev_h:
                continue
            prev_h = height
            current_height_start = i
            while profile:
                h, start = profile[-1]
                if h <= height:
                    break
                profile.pop()
                area = (i - start) * h
                current_height_start = start
                if area > largest_area:
                    largest_area = area
            if not profile or profile[-1][0] != height:
                profile.append((height, current_height_start))
        return largest_area
```


python

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: list[int] = [-1]
        max_area: int = 0
        N = len(heights)

        for i in range(N):
            
            # While we're not at the end of stack and the top's height is greater than the current height visted
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]  # Height of the top element and remove index from array
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)
        
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack [-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area
```


chat gpt soln:

```python

def largestRectangleArea21(heights):
    stack = []
    max_area = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)

            i += 1
        else:
            top_index = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, width * heights[top_index])
    while stack:
        top_index = stack.pop()
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, width * heights[top_index])
    return max_area


```



### 7. **Largest Rectangle in Histogram**

**Problem:** Given an array of integers representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Add a zero height to pop out remaining bars
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```



