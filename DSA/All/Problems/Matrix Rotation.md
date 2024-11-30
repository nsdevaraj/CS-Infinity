



### Rotate Matrix Problem (All Types of Rotation)

In this problem, we are asked to rotate a given matrix in different directions and degrees: 90°, 180°, and 270°, both clockwise and anticlockwise. The matrix is typically a 2D list (or array), and we need to transform it by rearranging the elements according to the specified rotation.

### Problem Statement

Given an $n \times n$ 2D matrix, rotate the matrix in place (without using extra space for another matrix) by 90°, 180°, or 270°, either clockwise or anticlockwise.

### Key Matrix Transformations:
1. **90° Clockwise**: Transpose the matrix, then reverse each row.
2. **90° Anticlockwise**: Transpose the matrix, then reverse each column.
3. **180° Clockwise/Anticlockwise**: Reverse both rows and columns of the matrix.
4. **270° Clockwise**: Rotate the matrix 90° anticlockwise.
5. **270° Anticlockwise**: Rotate the matrix 90° clockwise.

---

### 1. Rotate Matrix by 90° Clockwise

**Approach**:
1. **Transpose** the matrix: swap the matrix element at $i,j$ with the one at $j,i$.
2. **Reverse each row** of the matrix.

#### Code:
```python
def rotate_90_clockwise(matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

### 2. Rotate Matrix by 90° Anticlockwise

**Approach**:
1. **Transpose** the matrix.
2. **Reverse each column** of the matrix (instead of rows).

#### Code:
```python
def rotate_90_anticlockwise(matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each column
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
```

### 3. Rotate Matrix by 180° Clockwise/Anticlockwise

**Approach**:
- You can reverse both the rows and columns to rotate by 180°.

#### Code:
```python
def rotate_180(matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

    # Reverse the entire matrix
    matrix.reverse()
```

### 4. Rotate Matrix by 270° Clockwise

**Approach**:
- Equivalent to rotating the matrix by 90° anticlockwise.

#### Code:
```python
def rotate_270_clockwise(matrix: List[List[int]]) -> None:
    rotate_90_anticlockwise(matrix)
```

### 5. Rotate Matrix by 270° Anticlockwise

**Approach**:
- Equivalent to rotating the matrix by 90° clockwise.

#### Code:
```python
def rotate_270_anticlockwise(matrix: List[List[int]]) -> None:
    rotate_90_clockwise(matrix)
```

---

### Time and Space Complexity:
- **Time Complexity**: $O(n^2)$ for all rotations, as we need to visit each element of the matrix at least once.
- **Space Complexity**: $O(1)$ (in-place rotation).

---

### Summary of Rotations:

| Rotation                      | Transformation Steps                                      | Code Function                   |
|--------------------------------|-----------------------------------------------------------|----------------------------------|
| 90° Clockwise                  | Transpose, reverse each row                               | `rotate_90_clockwise`            |
| 90° Anticlockwise              | Transpose, reverse each column                            | `rotate_90_anticlockwise`        |
| 180° Clockwise/Anticlockwise    | Reverse rows, reverse entire matrix                       | `rotate_180`                     |
| 270° Clockwise                 | Equivalent to 90° Anticlockwise                           | `rotate_270_clockwise`           |
| 270° Anticlockwise             | Equivalent to 90° Clockwise                               | `rotate_270_anticlockwise`       |

Now, you can confidently apply any type of rotation to a matrix for coding interviews!



---


### Alternative Approaches for Rotating a Matrix

#### 1. Using an Extra Matrix

This approach involves creating a new matrix to store the rotated version of the original matrix. This is a straightforward method but requires additional space.

**90° Clockwise Rotation**:
```python
def rotate_90_clockwise_extra(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_matrix[j][n - 1 - i] = matrix[i][j]
    
    return new_matrix
```

**90° Anticlockwise Rotation**:
```python
def rotate_90_anticlockwise_extra(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_matrix[n - 1 - j][i] = matrix[i][j]
    
    return new_matrix
```

**180° Rotation**:
```python
def rotate_180_extra(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            new_matrix[n - 1 - i][n - 1 - j] = matrix[i][j]
    
    return new_matrix
```

**270° Clockwise**:
```python
def rotate_270_clockwise_extra(matrix: List[List[int]]) -> List[List[int]]:
    return rotate_90_anticlockwise_extra(matrix)
```

**270° Anticlockwise**:
```python
def rotate_270_anticlockwise_extra(matrix: List[List[int]]) -> List[List[int]]:
    return rotate_90_clockwise_extra(matrix)
```

### 2. Using NumPy Library

If you're allowed to use external libraries, NumPy provides convenient functions to rotate matrices easily. This method is efficient and concise.

**Example**:
```python
import numpy as np

def rotate_with_numpy(matrix: List[List[int]], degrees: int) -> List[List[int]]:
    np_matrix = np.array(matrix)

    if degrees == 90:
        return np.rot90(np_matrix, k=-1).tolist()  # Clockwise
    elif degrees == -90:
        return np.rot90(np_matrix, k=1).tolist()   # Anticlockwise
    elif degrees == 180:
        return np.rot90(np_matrix, k=2).tolist()   # 180 degrees
    elif degrees == 270:
        return np.rot90(np_matrix, k=3).tolist()   # Clockwise
    elif degrees == -270:
        return np.rot90(np_matrix, k=-3).tolist()  # Anticlockwise
    else:
        return matrix  # No rotation
```

### 3. Layer-by-Layer Rotation (for 90°)

This method involves rotating the matrix layer by layer. It is an in-place method and works well, especially for larger matrices.

**90° Clockwise Layer-by-Layer Rotation**:
```python
def rotate_layer_by_layer(matrix: List[List[int]]) -> None:
    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        for i in range(first, last):
            top = matrix[first][i]  # save top
            
            # left -> top
            matrix[first][i] = matrix[last - (i - first)][first]
            
            # bottom -> left
            matrix[last - (i - first)][first] = matrix[last][last - (i - first)]
            
            # right -> bottom
            matrix[last][last - (i - first)] = matrix[i][last]
            
            # top -> right
            matrix[i][last] = top  # saved top
```

### Summary of Approaches

| Approach                        | Method                                     | Space Complexity |
|---------------------------------|--------------------------------------------|------------------|
| In-Place (Transpose + Reverse)  | Efficient for rotation                      | O(1)             |
| Extra Matrix                    | Create a new matrix for rotation           | O(n^2)           |
| NumPy Library                   | Use NumPy for rotation                      | O(n^2) (NumPy handles internally) |
| Layer-by-Layer                  | Rotate in layers (only 90° clockwise)     | O(1)             |

### Conclusion

The choice of approach often depends on the constraints of the coding interview (e.g., whether you can use additional space) and the size of the matrix. Using in-place algorithms is generally preferred to reduce space complexity, but extra matrix solutions are straightforward and can be easier to implement.



---

# Rotate Image or Rotate Matrix


[LeetCode #48 - Rotate Image](https://leetcode.com/problems/rotate-image)

[Rotate Matrix 90 clockwise - Techdose](https://youtu.be/EaPuzeW7M0w?si=Cnz8OEuxUJrU3gcR)



## Problem Statement

You are given an $n \times n$ 2D matrix representing an image. Rotate the image by 90 degrees (clockwise) **in-place**. This means you cannot use any additional 2D array or significant extra space.

### Example

**Input:**
```python
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

**Output:**
```python
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

### Constraints
- The matrix must be rotated in-place, meaning no additional memory should be used beyond a few extra variables.
- Matrix dimensions: $n \times n$ (square matrix).
- $1 \leq n \leq 20$

---

## Approach Overview

We can solve this problem using two main approaches:
1. **Transpose and Reverse** - the most common and efficient approach.
2. **In-place Rotation by Layer** - an alternative that rotates the matrix layer by layer without needing to transpose first.

---

## non inplace soln


```python
from typing import List

def rotate_matrix_90(matrix:List[List[int]]):
    n = len(matrix)
    copy_matrix = []

    for i in range(n):
        for j in range(n):
            if(len(copy_matrix) != i+1):
                copy_matrix.append([])
            if(len(copy_matrix[i]) != j+1):
                copy_matrix[i].append([])
            copy_matrix[i][j] = matrix[i][j]

    for i in range(n):
        copy_j = n - i -1
        for j in range(n):
            copy_i = j
            copy_matrix[copy_i][copy_j] = matrix[i][j]

    return (copy_matrix)

```


```python

```python
from typing import List

def rotate_matrix_90(matrix:List[List[int]]):
    n = len(matrix)
    copy_matrix = []

    for i in range(n):
        for j in range(n):
            if(len(copy_matrix) != i+1):
                copy_matrix.append([])
            if(len(copy_matrix[i]) != j+1):
                copy_matrix[i].append([])
            copy_matrix[i][j] = matrix[i][j]

    for i in range(n):
        copy_j = n - i -1
        for j in range(n):
            copy_i = j
            copy_matrix[copy_i][copy_j] = matrix[i][j]

    return (copy_matrix)


```



---



## Approach 1: Transpose and Reverse

### Explanation

To rotate the matrix 90 degrees clockwise, we can break the process into two main steps:

1. **Transpose the matrix**: Swap rows with columns, i.e., matrix[i][j] becomes matrix[j][i]. This converts all rows into columns.
   
   After transposing, the matrix looks like:
   ```
   [
     [1, 4, 7],
     [2, 5, 8],
     [3, 6, 9]
   ]
   ```

2. **Reverse each row**: Reverse the elements in every row, which gives us the desired 90-degree rotation.
   
   After reversing each row, the matrix becomes:
   ```
   [
     [7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]
   ]
   ```

### Code

```python
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

### Time Complexity

- **Transpose operation**: We swap elements in the upper triangle of the matrix, which takes $O(n^2)$ time.
- **Reverse operation**: Each row reversal takes $O(n)$ time, so $O(n^2)$ in total.

Thus, the time complexity is **$O(n^2)$**.

### Space Complexity

- We only use a few extra variables, so the space complexity is **$O(1)$** (in-place).

---

## Approach 2: In-Place Rotation by Layer

### Explanation

In this approach, we rotate the matrix layer by layer. For an $n \times n$ matrix, there are $\frac{n}{2}$ layers.

1. For each layer, we rotate four elements at a time. The top row becomes the right column, the right column becomes the bottom row, and so on.

2. We repeat this process for all layers, working from the outermost layer to the innermost.

For example, consider a 4x4 matrix:
```
[
  [ 1,  2,  3,  4],
  [ 5,  6,  7,  8],
  [ 9, 10, 11, 12],
  [13, 14, 15, 16]
]
```

We rotate the outermost layer by shifting four elements at a time:
```
[
  [13,  9,  5,  1],
  [14, 10,  6,  2],
  [15, 11,  7,  3],
  [16, 12,  8,  4]
]
```

### Code

```python
def rotate_layer(matrix: List[List[int]]) -> None:
    n = len(matrix)
    
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  # Save top element
            
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Assign top to right
            matrix[i][last] = top
```

### Time Complexity

- **Layer rotation**: For each layer, we rotate $4 \times (n - 2 \times \text{layer})$ elements, and there are $\frac{n}{2}$ layers. Hence, the time complexity is **$O(n^2)$**.

### Space Complexity

- Since the rotation is done in-place, the space complexity is **$O(1)$**.

---

## Test Cases

We will use several test cases to check the correctness of the program, including general cases, edge cases, and variations in matrix sizes.

```python
def test_rotate():
    test_cases = [
        {
            "name": "General Case 3x3",
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        },
        {
            "name": "General Case 4x4",
            "input": [[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12], [13, 14, 15, 16]],
            "expected": [[13,  9,  5,  1], [14, 10,  6,  2], [15, 11,  7,  3], [16, 12,  8,  4]]
        },
        {
            "name": "Edge Case 1x1",
            "input": [[1]],
            "expected": [[1]]
        },
        {
            "name": "Edge Case 2x2",
            "input": [[1, 2], [3, 4]],
            "expected": [[3, 1], [4, 2]]
        },
        {
            "name": "All Same Elements",
            "input": [[5, 5], [5, 5]],
            "expected": [[5, 5], [5, 5]]
        },
        {
            "name": "Negative Values",
            "input": [[-1, -2], [-3, -4]],
            "expected": [[-3, -1], [-4, -2]]
        },
        {
            "name": "Larger 5x5 Matrix",
            "input": [[ 1,  2,  3,  4,  5],
                      [ 6,  7,  8,  9, 10],
                      [11, 12, 13, 14, 15],
                      [16, 17, 18, 19, 20],
                      [21, 22, 23, 24, 25]],
            "expected": [[21, 16, 11,  6,  1],
                         [22, 17, 12,  7,  2],
                         [23, 18, 13,  8,  3],
                         [24, 19, 14,  9,  4],
                         [25, 20, 15, 10,  5]]
        }
    ]

    for i, test_case in enumerate(test_cases):
        input_data = [row[:] for row in test_case["input"]]
        rotate(input_data)
        assert input_data == test_case["expected"], f"Test {test_case['name']} failed: expected {test_case['expected']}, got {input_data}"

    print("All tests passed.")
```

---

## Summary of Approaches
## Non-In-Place Solution: Using Extra Space

If we were not restricted to an in-place solution, we could easily solve the problem by creating a new matrix and directly placing the rotated values into the appropriate positions. This approach allows us to avoid the in-place constraints but does require additional space.

### Explanation

The idea behind this approach is simple:

1. Create a new matrix of the same size as the input matrix.
2. For each element in the original matrix, place it in the correct position in the new matrix according to a 90-degree rotation. For example, the element at position `(i, j)` in the original matrix will be placed at position `(j, n - 1 - i)` in the new matrix.
3. Finally, replace the original matrix with the newly created matrix.

### Code

```python
from typing import List

def rotate_non_inplace(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]  # Create a new empty matrix
    
    for i in range(n):
        for j in range(n):
            new_matrix[j][n - 1 - i] = matrix[i][j]  # Rotate by 90 degrees
    
    return new_matrix
```

### Time Complexity

- **Matrix traversal**: We iterate over all elements of the matrix, which takes $O(n^2)$ time, where $n$ is the dimension of the matrix.

Thus, the time complexity is **$O(n^2)$**.

### Space Complexity

- We use an additional matrix of size $n \times n$, so the space complexity is **$O(n^2)$**.

### Test Cases

Let's modify the test function to include this new approach:

```python
def test_rotate_non_inplace():
    test_cases = [
        {
            "name": "General Case 3x3",
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        },
        {
            "name": "General Case 4x4",
            "input": [[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12], [13, 14, 15, 16]],
            "expected": [[13,  9,  5,  1], [14, 10,  6,  2], [15, 11,  7,  3], [16, 12,  8,  4]]
        },
        {
            "name": "Edge Case 1x1",
            "input": [[1]],
            "expected": [[1]]
        },
        {
            "name": "Edge Case 2x2",
            "input": [[1, 2], [3, 4]],
            "expected": [[3, 1], [4, 2]]
        },
        {
            "name": "All Same Elements",
            "input": [[5, 5], [5, 5]],
            "expected": [[5, 5], [5, 5]]
        },
        {
            "name": "Negative Values",
            "input": [[-1, -2], [-3, -4]],
            "expected": [[-3, -1], [-4, -2]]
        },
        {
            "name": "Larger 5x5 Matrix",
            "input": [[ 1,  2,  3,  4,  5],
                      [ 6,  7,  8,  9, 10],
                      [11, 12, 13, 14, 15],
                      [16, 17, 18, 19, 20],
                      [21, 22, 23, 24, 25]],
            "expected": [[21, 16, 11,  6,  1],
                         [22, 17, 12,  7,  2],
                         [23, 18, 13,  8,  3],
                         [24, 19, 14,  9,  4],
                         [25, 20, 15, 10,  5]]
        }
    ]

    for i, test_case in enumerate(test_cases):
        input_data = [row[:] for row in test_case["input"]]
        result = rotate_non_inplace(input_data)
        assert result == test_case["expected"], f"Test {test_case['name']} failed: expected {test_case['expected']}, got {result}"

    print("All tests passed.")
```

---

## Summary of Approaches

| Approach                    | Time Complexity | Space Complexity | Explanation                                                                   |
| --------------------------- | --------------- | ---------------- | ----------------------------------------------------------------------------- |
| **Transpose and Reverse**   | $O(n^2)$        | $O(1)$           | Transpose the matrix and reverse each row for in-place 90-degree rotation.    |
| **In-place Layer Rotation** | $O(n^2)$        | $O(1)$           | Rotate each layer of the matrix element by element without using extra space. |
| **Non-In-Place Rotation**   | $O(n^2)$        | $O(n^2)$         | Use extra matrix to directly rotate by placing elements in correct positions. |

The **non-in-place approach** is simpler to understand but requires extra space, making it less optimal in terms of space complexity.


