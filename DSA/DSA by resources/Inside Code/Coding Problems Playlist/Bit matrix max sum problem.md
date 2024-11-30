

[Bit matrix max sum problem - Inside code](https://youtu.be/N4vQn9zj7J0?si=C5cQx2fMPo6Q9VoS)



### Problem Statement

Given a binary matrix where each row represents a binary number, your task is to maximize the sum of the binary numbers after potentially toggling (flipping) any number of rows and columns. A toggle on a row or column flips all `1`s to `0`s and vice versa. The goal is to maximize the sum of the decimal values of the rows.

### Approach Explanation

1. **Row Toggling Strategy**:
   - The most significant bit (leftmost) of a binary number determines its value more than other bits. Therefore, for any row that starts with `0`, toggle it so that the leftmost bit becomes `1`, maximizing its value.
   
2. **Column Toggling Strategy**:
   - Once the rows are adjusted, focus on columns. For each column, count the number of `1`s and `0`s. If a column has more `0`s than `1`s, toggle it to maximize the number of `1`s in the column.
   
3. **Sum Calculation**:
   - After toggling necessary rows and columns, convert each row (now representing a binary number) to its decimal equivalent, sum them up, and return the result.

### Example

**Input**:
```
[
  [0, 1, 1, 0, 1],
  [1, 0, 0, 1, 0],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 0]
]
```

**Output**:
```
Resulting sum: 87
```

### Explanation:
1. Initially, toggle the first and third rows (because they start with `0`).
2. Then toggle the second, third, and fourth columns (because they have more `0`s than `1`s).
3. After toggling, calculate the sum of the binary numbers and return the result.

### Code Implementation

```python
from typing import List

# Function to toggle a specific row by flipping all bits
def toggleRow(matrix: List[List[int]], row: int) -> None:
    m = len(matrix[0])  # Number of columns
    for i in range(m):
        matrix[row][i] ^= 1  # XOR with 1 to flip the bit

# Function to check if a column has more zeroes than ones
def hasLessOnesThanZeroes(matrix: List[List[int]], column: int) -> bool:
    n = len(matrix)  # Number of rows
    nbZeroes, nbOnes = 0, 0
    for i in range(n):
        if matrix[i][column] == 1:
            nbOnes += 1
        else:
            nbZeroes += 1
    return nbOnes < nbZeroes

# Function to toggle a specific column by flipping all bits
def toggleColumn(matrix: List[List[int]], column: int) -> None:
    n = len(matrix)  # Number of rows
    for i in range(n):
        matrix[i][column] ^= 1  # XOR with 1 to flip the bit

# Function to get the maximum sum by toggling necessary rows and columns
def bitMatrixMaxSum(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])  # n rows and m columns
    
    # Step 1: Toggle rows if the first element is 0
    for i in range(n):
        if matrix[i][0] == 0:
            toggleRow(matrix, i)
    
    # Step 2: Toggle columns if the column has more zeroes than ones
    for i in range(m):
        if hasLessOnesThanZeroes(matrix, i):
            toggleColumn(matrix, i)
    
    # Step 3: Calculate the sum of the binary numbers after toggling
    total_sum = 0
    for row in matrix:
        total_sum += int("".join(map(str, row)), 2)  # Convert binary row to decimal
    
    return total_sum
```

### Optimizations & Complexity

-Here’s the time complexity explanation with LaTeX formatting:

Here’s the corrected time complexity explanation with proper LaTeX formatting:

- **Time Complexity**:
  - Toggling rows and columns involves traversing the entire matrix, so both steps (row and column toggling) cost \( O(n \times m) \).
  - Summing up the binary numbers also requires traversing the matrix, contributing another \( O(n \times m) \).
  - Overall, the time complexity is \( O(n \times m) \).

 where \( n \) is the number of rows and \( m \) is the number of columns.

### Time Complexity

- **Time Complexity**:
  - Toggling rows and columns involves traversing the entire matrix, so both steps (row and column toggling) cost 
  $$
  O(n \times m)
  $$
  - Summing up the binary numbers also requires traversing the matrix, contributing another 
  $$
  O(n \times m)
  $$
  - Overall, the time complexity is 
  $$
  O(n \times m)
  $$


- **Space Complexity**:
  - The space complexity is **O(1)** since we are using only a few extra variables, and the matrix is modified in-place.

### Conclusion

This algorithm effectively maximizes the sum by using toggles strategically, focusing on the most significant bits in the rows and then optimizing the ones in the columns. The time complexity of \( O(n \cdot m) \) ensures that it scales efficiently with matrix size.






