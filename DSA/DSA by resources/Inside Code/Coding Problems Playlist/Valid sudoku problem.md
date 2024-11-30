
[Valid sudoku problem (LeetCode #36) - Inside code](https://youtu.be/HKEhqxznPjk?si=AUm0tv24pb6HaJ3j)



### Problem Explanation:

The goal of the **Valid Sudoku** problem is to determine whether a given 9x9 Sudoku board is valid. The board is valid if:
1. Each row contains the digits 1-9 without repetition.
2. Each column contains the digits 1-9 without repetition.
3. Each 3x3 sub-grid (or square) contains the digits 1-9 without repetition.

We are not required to solve the Sudoku, only to verify its current state.


Apologies for missing the brute force explanation earlier. Let’s go over that part in detail now, contrasting the brute force approach with the optimized one we’ve already covered.

### Brute Force Approach:

In the brute force method, the goal is still to check if the Sudoku board is valid by ensuring that:
1. There are no duplicate numbers in any row.
2. There are no duplicate numbers in any column.
3. There are no duplicate numbers in any 3x3 sub-grid.

#### How Brute Force Works:
- For each non-empty cell in the grid, you need to **check all other cells** in its corresponding row, column, and 3x3 sub-grid to ensure there are no duplicates.
  
1. **Check Rows**: For each filled cell in a given row, check all other cells in the same row to see if they contain the same value.
2. **Check Columns**: For each filled cell in a given column, check all other cells in the same column to see if they contain the same value.
3. **Check 3x3 Sub-Grids**: For each filled cell in a 3x3 sub-grid, check all other cells in that sub-grid to see if they contain the same value.

#### Time Complexity of Brute Force:
- **O(n³)** where `n = 9` (for a 9x9 grid).
- Here's the reasoning:
  - There are **n² cells** in total (81 cells for a 9x9 grid).
  - For each cell, you need to check **n** cells in its row, **n** cells in its column, and **n** cells in its sub-grid (essentially 3n checks per cell).
  - This results in **n² × 3n = O(n³)** total checks.
  
Since **n** is small (9 in a typical Sudoku), brute force could still work in practice, but it’s inefficient compared to the optimized set-based approach.

#### Brute Force Code (for clarity):
```python
def is_valid_sudoku_brute_force(grid):
    n = 9  # Size of the Sudoku grid

    # Check rows for duplicates
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                continue
            for k in range(n):
                if k != j and grid[i][k] == grid[i][j]:
                    return False  # Duplicate in the row

    # Check columns for duplicates
    for j in range(n):
        for i in range(n):
            if grid[i][j] == '.':
                continue
            for k in range(n):
                if k != i and grid[k][j] == grid[i][j]:
                    return False  # Duplicate in the column

    # Check 3x3 sub-grids for duplicates
    for block_row in range(0, n, 3):
        for block_col in range(0, n, 3):
            for i in range(3):
                for j in range(3):
                    cell_value = grid[block_row + i][block_col + j]
                    if cell_value == '.':
                        continue
                    for x in range(3):
                        for y in range(3):
                            if (x != i or y != j) and grid[block_row + x][block_col + y] == cell_value:
                                return False  # Duplicate in the 3x3 sub-grid
    return True
```

#### Breakdown of Brute Force Approach:
- **Row Check**:  
  For each cell in a row, compare it with every other cell in that row. This requires nested loops, making it O(n²) for rows alone.

- **Column Check**:  
  Similarly, for each cell in a column, compare it with every other cell in that column, adding another O(n²) check.

- **Sub-Grid Check**:  
  Each 3x3 sub-grid is checked cell-by-cell to ensure there are no duplicates. This also adds another layer of nested loops, O(n²).

---

### Why the Optimized Approach is Better:
- The brute force approach, as described, is inefficient due to the O(n³) complexity. For each non-empty cell, it redundantly checks all other cells in the row, column, and sub-grid, which leads to unnecessary repetition.
  
- In contrast, the **optimized approach** (using sets) processes each cell **only once**. It tracks the values in each row, column, and sub-grid in real-time, ensuring that every value is unique as we traverse the grid. This reduces the time complexity to **O(n²)**, a significant improvement, especially for larger grids.

---

### Optimized vs. Brute Force Comparison:

| Metric              | Brute Force                         | Optimized (Set-based)                |
|---------------------|-------------------------------------|--------------------------------------|
| **Time Complexity**  | O(n³)                               | O(n²)                               |
| **Space Complexity** | O(1) (no extra space)               | O(n²) (for rows, columns, squares)   |
| **Efficiency**       | Checks each cell multiple times     | Checks each cell only once           |
| **Use Case**         | Simple, straightforward but slow    | Efficient, handles larger grids well |

---

### Conclusion:

The brute force approach is conceptually simpler but highly inefficient, especially as the grid size grows. By using sets to track the numbers seen in rows, columns, and sub-grids, we can drastically reduce the time complexity from O(n³) to O(n²), making the solution much more scalable and faster for practical use.

---

### Optimized Solution Using Sets:

We use sets to keep track of the digits seen so far in each row, each column, and each 3x3 sub-grid. For each digit in the grid, we:
- Check if it already exists in its corresponding row, column, or square set.
- If it does, the grid is invalid. If not, add it to the corresponding sets and continue.

The benefit of using sets is that lookups and insertions are done in **O(1)** time on average, making the algorithm efficient.

---

### Approach:

1. **Data Structures**:
   - We need 9 sets for rows, 9 sets for columns, and 9 sets for the 3x3 sub-grids.
   - Each set will store the digits we’ve encountered so far in that specific row, column, or square.

2. **Nested Loops**:
   - We iterate over every cell in the grid using two nested loops (i.e., one for rows and one for columns).
   
3. **Skip Empty Cells**:
   - If the cell is empty (represented by '.'), we simply skip to the next cell.

4. **Check for Duplicates**:
   - For each digit, check if it already exists in the corresponding row, column, or 3x3 sub-grid set.
   - If it exists, the grid is invalid, and we return `False`.
   - If it doesn’t exist, add the digit to the respective sets (row, column, and square).

5. **Square Index Calculation**:
   - To map each cell to the correct 3x3 sub-grid, use the formula:  
     `square_index = (i // 3) * 3 + (j // 3)`  
     where `i` is the row index and `j` is the column index.

6. **Time Complexity**:
   - **O(n²)** where `n = 9`, because we traverse all 81 cells in the grid, and lookups in sets are done in **O(1)** on average.

---

### Code with Detailed Comments:

```python
def is_valid_sudoku(grid):
    # Create 9 sets for rows, columns, and 3x3 sub-grids (squares)
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]  # There are 9 squares in a 9x9 grid
    
    # Iterate over every cell in the grid
    for i in range(9):  # 'i' is the row index
        for j in range(9):  # 'j' is the column index
            # Current cell value
            value = grid[i][j]
            
            # Skip empty cells (denoted by '.')
            if value == '.':
                continue
            
            # Calculate which 3x3 square this cell belongs to
            square_index = (i // 3) * 3 + (j // 3)
            
            # Check if the value already exists in the corresponding row, column, or square
            if value in rows[i] or value in cols[j] or value in squares[square_index]:
                # If the value is found, the board is invalid
                return False
            
            # Add the value to the respective row, column, and square sets
            rows[i].add(value)
            cols[j].add(value)
            squares[square_index].add(value)
    
    # If no duplicates are found, the board is valid
    return True
```




```js

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const len = board.length;

    // Validate columns
    for (let col = 0; col < len; col++) {
        const colMap = new Map();
        for (let row = 0; row < len; row++) {
            const num = board[row][col];
            if (num !== ".") {
                if (colMap.has(num)) {
                    return false; // Duplicate found in the column
                }
                colMap.set(num, 1);
            }
        }
    }

    // Validate rows
    for (let row = 0; row < len; row++) {
        const rowMap = new Map();
        for (let col = 0; col < len; col++) {
            const num = board[row][col];
            if (num !== ".") {
                if (rowMap.has(num)) {
                    return false; // Duplicate found in the row
                }
                rowMap.set(num, 1);
            }
        }
    }

    // Validate 3x3 subgrids
    for (let boxRow = 0; boxRow < 3; boxRow++) {
        for (let boxCol = 0; boxCol < 3; boxCol++) {
            const boxMap = new Map();
            for (let i = 0; i < 3; i++) {
                for (let j = 0; j < 3; j++) {
                    const num = board[boxRow * 3 + i][boxCol * 3 + j];
                    if (num !== ".") {
                        if (boxMap.has(num)) {
                            return false; // Duplicate found in the 3x3 subgrid
                        }
                        boxMap.set(num, 1);
                    }
                }
            }
        }
    }

    return true; // The Sudoku board is valid
};



```

```js

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    // Validate each row
    for (let r = 0; r < 9; r++) {
        let seen = new Set();
        for (let i = 0; i < 9; i++) {
            const cell = board[r][i];
            if (cell === ".") continue; // Skip empty cells
            if (seen.has(cell)) return false; // Duplicate found in the row
            seen.add(cell);
        }
    }

    // Validate each column
    for (let c = 0; c < 9; c++) {
        let seen = new Set();
        for (let i = 0; i < 9; i++) {
            const cell = board[i][c];
            if (cell === ".") continue; // Skip empty cells
            if (seen.has(cell)) return false; // Duplicate found in the column
            seen.add(cell);
        }
    }

    // Validate each 3x3 subgrid
    for (let r = 0; r < 9; r += 3) {
        for (let c = 0; c < 9; c += 3) {
            let seen = new Set();
            for (let row = r; row < r + 3; row++) {
                for (let col = c; col < c + 3; col++) {
                    const cell = board[row][col];
                    if (cell === ".") continue; // Skip empty cells
                    if (seen.has(cell)) return false; // Duplicate found in the subgrid
                    seen.add(cell);
                }
            }
        }
    }

    return true; // The Sudoku board is valid
};

```

---

### Breakdown of Key Points:

1. **Data Structures**:
   - `rows`: Tracks values in each row (9 sets).
   - `cols`: Tracks values in each column (9 sets).
   - `squares`: Tracks values in each 3x3 sub-grid (9 sets).

2. **Square Calculation**:
   - We use `(i // 3) * 3 + (j // 3)` to determine which 3x3 sub-grid a cell belongs to. This is because the grid is divided into nine 3x3 sub-grids.

3. **Condition to Skip Empty Cells**:
   - `if value == '.': continue` skips cells that are empty.

4. **Duplicate Check**:
   - The `if` statement checks if the current value exists in the respective row, column, or sub-grid. If a duplicate is found, the function immediately returns `False`.

5. **Return True**:
   - If no duplicate values are found after iterating through the entire grid, the function returns `True`, meaning the Sudoku board is valid.

---

```javascript
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {

    let rowItems = new Set()

    let colItemsArray = []
    for (let k = 0; k < 9; k++) {
        colItemsArray.push(new Set())
    }

    let gridItemsArray;

    for (let i = 0; i < 9; i++) {

        rowItems = new Set()
        if (i % 3 == 0) {
            gridItemsArray = [new Set(), new Set(), new Set()]
        }

        for (let j = 0; j < 9; j++) {

            const cellValue = board[i][j]
            console.log(i, j, cellValue)

            // filter empty cells
            if (cellValue === '.') {
                continue
            }


            // check row's uniqueness
            if (rowItems.has(cellValue)) {
                return false
            } else {
                rowItems.add(cellValue)
            }


            // check col's uniquness
            const colItems = colItemsArray[j]
            if (colItems.has(cellValue)) {
                console.log('colItems', colItems, 'cellValue', cellValue)
                return false
            } else {
                colItems.add(cellValue)
            }

            // check grid's uniqueness
            const gridItems = gridItemsArray[Math.floor(j / 3)]
            if (gridItems.has(cellValue)) {
                return false
            } else {
                gridItems.add(cellValue)
            }
        }
    }


    return true
};

```


---

### Time and Space Complexity:

- **Time Complexity**:  
  - **O(n²)** (i.e., O(81) = O(1)) since we check every cell in the 9x9 grid, and each operation (lookup and insert into a set) is done in **O(1)** time on average.

- **Space Complexity**:  
  - **O(n²)** because we maintain three separate sets (for rows, columns, and squares), each capable of holding up to `n` (9) elements.

---

### Conclusion:

This solution efficiently checks whether a given Sudoku grid is valid by leveraging sets to track seen values and ensures that all checks are done in **O(1)** time per cell. The overall time complexity is **O(n²)**, which is optimal for this problem size, and the space complexity is also manageable.


