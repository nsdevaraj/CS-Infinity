

 [LeetCode #54 - Spiral Matrix](https://leetcode.com/problems/spiral-matrix)

[Trick for spiral matrix traversal](https://www.youtube.com/watch?v=1ZGJzvkcLsA)



# Spiral Matrix

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in spiral order.

### Example

**Input:**

```plaintext
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output:** 

```plaintext
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

## Approaches to Solve the Problem

We will explore two main approaches to solve the Spiral Matrix problem: the iterative approach and the recursive approach.

### Approach 1: Iterative Method

The iterative method involves keeping track of the boundaries of the spiral. We'll start from the outermost layer and progressively move inward.

#### Steps:
1. Define four boundaries: `top`, `bottom`, `left`, and `right`.
2. While the boundaries are valid:
   - Traverse from left to right along the `top` boundary, then increment `top`.
   - Traverse from top to bottom along the `right` boundary, then decrement `right`.
   - If `top` is still less than or equal to `bottom`, traverse from right to left along the `bottom` boundary, then decrement `bottom`.
   - If `left` is still less than or equal to `right`, traverse from bottom to top along the `left` boundary, then increment `left`.

#### Complexity Analysis
- **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns.
- **Space Complexity:** $O(1)$, since we are using a constant amount of space for the output.

#### Code Implementation

```python
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
```

### Approach 2: Recursive Method

The recursive approach breaks the problem into smaller sub-problems. We can define a function that handles the traversal for a specific layer and call it recursively.

#### Steps:
1. Define a recursive function that takes the current boundaries as parameters.
2. Add the elements in the current layer to the result, adjusting the boundaries accordingly.
3. Call the recursive function for the next inner layer.

#### Complexity Analysis
- **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns.
- **Space Complexity:** $O(m \cdot n)$ for the recursion stack, which may be less efficient than the iterative method.

#### Code Implementation

```python
from typing import List

def spiralOrderRecursive(matrix: List[List[int]]) -> List[int]:
    def helper(top, bottom, left, right):
        if top > bottom or left > right:
            return []

        result = []

        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        
        # Traverse from top to bottom
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])
        
        if top < bottom:
            # Traverse from right to left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][i])
        
        if left < right:
            # Traverse from bottom to top
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])
        
        # Recur for the inner matrix
        return result + helper(top + 1, bottom - 1, left + 1, right - 1)

    return helper(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
```

## Summary of Approaches

| Approach              | Time Complexity     | Space Complexity     | Description                                         |
|-----------------------|---------------------|----------------------|-----------------------------------------------------|
| Iterative             | $O(m \cdot n)$      | $O(1)$               | Traverse the matrix using defined boundaries.       |
| Recursive             | $O(m \cdot n)$      | $O(m \cdot n)$       | Recurse for each layer of the matrix.              |


### Test Function and Distinct Test Cases

Below is the test function that checks the correctness of both the iterative and recursive approaches. It includes distinct test cases to cover different edge scenarios.

```python
def test_spiral_order():
    test_cases = [
        {
            "name": "General Case 1",
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
        },
        {
            "name": "Single Row",
            "matrix": [[1, 2, 3, 4]],
            "expected": [1, 2, 3, 4],
        },
        {
            "name": "Single Column",
            "matrix": [[1], [2], [3], [4]],
            "expected": [1, 2, 3, 4],
        },
        {
            "name": "Empty Matrix",
            "matrix": [],
            "expected": [],
        },
        {
            "name": "1x1 Matrix",
            "matrix": [[1]],
            "expected": [1],
        },
        {
            "name": "Rectangular Matrix",
            "matrix": [[1, 2], [3, 4], [5, 6]],
            "expected": [1, 2, 4, 6, 5, 3],
        },
        {
            "name": "Larger Square Matrix",
            "matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            "expected": [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
        },
        {
            "name": "Non-rectangular Matrix",
            "matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        }
    ]
    
    for case in test_cases:
        matrix = case["matrix"]
        expected = case["expected"]

        # Test Iterative Approach
        result_iterative = spiralOrder(matrix)
        assert result_iterative == expected, f"Test failed for {case['name']} with iterative approach"
        
        # Test Recursive Approach
        result_recursive = spiralOrderRecursive(matrix)
        assert result_recursive == expected, f"Test failed for {case['name']} with recursive approach"
    
    print("All test cases passed!")

# Run the test function
test_spiral_order()
```


### Comparison of Approaches

| Approach             | Time Complexity     | Space Complexity     | Description                                                   |
|----------------------|---------------------|----------------------|---------------------------------------------------------------|
| Iterative            | $O(m \cdot n)$      | $O(1)$               | Iterates through the matrix using four boundary variables. Most efficient for space. |
| Recursive            | $O(m \cdot n)$      | $O(m \cdot n)$       | Uses recursion to process layers of the matrix. Can be less efficient due to recursion stack. |

### Time and Space Complexities (Explanation)

- **Iterative Approach:** 
  - **Time Complexity:** Since we visit each element of the matrix once, the time complexity is $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns.
  - **Space Complexity:** The space complexity is $O(1)$ because the only additional space used is for the result array and a few variables to track boundaries.

- **Recursive Approach:** 
  - **Time Complexity:** Similar to the iterative approach, the time complexity is $O(m \cdot n)$ because we visit each element exactly once.
  - **Space Complexity:** The space complexity is $O(m \cdot n)$ due to the recursion stack that holds states for each layer of the matrix.

The recursive approach may lead to more memory overhead due to recursion, especially in large matrices.




```python 

# tried this and ended without success

from typing import List


def test_spiral_order(func):
    test_cases = [
        {
            "name": "General Case 1",
            "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
        },
        {
            "name": "Single Row",
            "matrix": [[1, 2, 3, 4]],
            "expected": [1, 2, 3, 4],
        },
        {
            "name": "Single Column",
            "matrix": [[1], [2], [3], [4]],
            "expected": [1, 2, 3, 4],
        },
        {
            "name": "Empty Matrix",
            "matrix": [],
            "expected": [],
        },
        {
            "name": "1x1 Matrix",
            "matrix": [[1]],
            "expected": [1],
        },
        {
            "name": "Rectangular Matrix",
            "matrix": [[1, 2], [3, 4], [5, 6]],
            "expected": [1, 2, 4, 6, 5, 3],
        },
        {
            "name": "Larger Square Matrix",
            "matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            "expected": [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
        },
        {
            "name": "Non-rectangular Matrix",
            "matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        }
    ]

    for case in test_cases:
        matrix = case["matrix"]
        expected = case["expected"]
        result = func(matrix)
        assert result == expected, f"Test failed for {case['name']} with recursive approach"

    print("All test cases passed!")


'''
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
'''
def give_spiral(matrix:List[List[int]])-> List[int]:
    result = []

    '''
    3X3 matrix

    00,01,02 => (0,1)
    12,22 => (1,0)
    21,20 => (0,-1)
    20,10 => (-1,0)
    11 => (0,1)
    '''



    x = 0
    y = -1
    dir = (0,1)
    dir_map = {
        (0,1): (1,0),
        (1,0):(0,-1),
        (0,-1):(-1,0),
        (-1,0):(0,1),
    }

    row_len = len(matrix)
    col_len = len(matrix[0])

    do = [0]

    print(matrix)
    while(row_len > 0 or col_len > 0):
        print('res ',result, row_len, col_len)
        for t in do:
            if(t == 0):
                i = col_len
                row_len -= 1
            else:
                i = row_len
                col_len -= 1

            for j in range(i):
                first, second = dir
                x += first
                y += second
                result.append(matrix[x][y])
            dir = dir_map[(dir)]


    do = [1,0]

    print('res ',result)
    return result


# give_spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# give_spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

give_spiral( [[1], [2], [3], [4]])


```