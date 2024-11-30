


### Problem Statement: Sudoku Solver

You are given a 9x9 Sudoku board filled with digits and some empty cells (represented by `'.'`). Write a function to solve the Sudoku by filling the empty cells.

The rules for Sudoku are as follows:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits `1-9` without repetition.

The Sudoku puzzle is guaranteed to have a single solution.

You must modify the given board in-place and the function should not return anything.

### Solution

The solution uses **backtracking** to recursively try filling the board, checking if each guess is valid and undoing the guess if it leads to an invalid state. Here's the code with improved structure and concise comments.

### Optimized Code:

```python
from itertools import product
from typing import List

class Solution:
    SHAPE = 9
    GRID = 3
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, SHAPE + 1)])  # Set of digits '1' to '9'

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle in-place.
        
        Args:
            board (List[List[str]]): 9x9 Sudoku board with empty cells ('.').
        """
        self.search(board)
    
    def is_valid_state(self, board):
        """
        Checks if the current board is a valid solution.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        # Validate rows, columns, and 3x3 grids
        for row in self.get_rows(board):
            if set(row) != self.DIGITS:
                return False
        for col in self.get_cols(board):
            if set(col) != self.DIGITS:
                return False
        for grid in self.get_grids(board):
            if set(grid) != self.DIGITS:
                return False
        return True

    def get_candidates(self, board, row, col):
        """
        Returns valid candidates for the current empty cell.
        
        Args:
            board (List[List[str]]): Current state of the Sudoku board.
            row (int): Row index of the empty cell.
            col (int): Column index of the empty cell.

        Returns:
            set: Set of valid digits that can be placed in the cell.
        """
        # Collect digits used in the same row, column, and 3x3 grid
        used_digits = set(self.get_kth_row(board, row))
        used_digits.update(self.get_kth_col(board, col))
        used_digits.update(self.get_grid_at_row_col(board, row, col))
        used_digits -= {self.EMPTY}  # Remove placeholder for empty cells
        return self.DIGITS - used_digits  # Return valid candidates

    def search(self, board):
        """
        Recursively tries to solve the board using backtracking.
        
        Args:
            board (List[List[str]]): Current state of the board.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        # Base case: check if the board is fully valid
        if self.is_valid_state(board):
            return True  # Solution found

        # Search for the next empty spot ('.')
        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell == self.EMPTY:
                    # Try all valid candidates
                    for candidate in self.get_candidates(board, row_idx, col_idx):
                        board[row_idx][col_idx] = candidate  # Place candidate
                        if self.search(board):  # Recurse
                            return True  # Solution found
                        board[row_idx][col_idx] = self.EMPTY  # Undo the guess (backtrack)
                    return False  # No valid candidate, puzzle unsolvable from this state
        return True  # Puzzle solved (no empty spots)

    # Helper functions for rows, columns, and grids
    def get_kth_row(self, board, k):
        return board[k]  # Return the k-th row

    def get_rows(self, board):
        for i in range(self.SHAPE):
            yield board[i]  # Yield all rows
    
    def get_kth_col(self, board, k):
        return [board[row][k] for row in range(self.SHAPE)]  # Return the k-th column

    def get_cols(self, board):
        for col in range(self.SHAPE):
            yield [board[row][col] for row in range(self.SHAPE)]  # Yield all columns

    def get_grid_at_row_col(self, board, row, col):
        row = (row // self.GRID) * self.GRID  # Find top-left row of the 3x3 grid
        col = (col // self.GRID) * self.GRID  # Find top-left column of the 3x3 grid
        return [
            board[r][c] for r, c in 
            product(range(row, row + self.GRID), range(col, col + self.GRID))
        ]  # Return all elements in the 3x3 grid containing (row, col)

    def get_grids(self, board):
        for row in range(0, self.SHAPE, self.GRID):
            for col in range(0, self.SHAPE, self.GRID):
                yield [
                    board[r][c] for r, c in 
                    product(range(row, row + self.GRID), range(col, col + self.GRID))
                ]  # Yield all 3x3 grids
```

### Key Changes:

- **Concise Comments**: Added clear, concise comments explaining each function and critical steps in the algorithm.
- **Backtracking Logic**: Each empty cell is recursively filled with valid candidates, and backtracking occurs if the current guess doesn't lead to a solution.
- **Helper Functions**: Functions like `get_kth_row`, `get_kth_col`, and `get_grid_at_row_col` are used to retrieve specific rows, columns, and 3x3 sub-grids.
  
### Time Complexity:
- **O(9^m)** where `m` is the number of empty cells. Since for each empty cell, there are 9 possible choices, the worst-case scenario involves trying every combination of digits for each empty cell.

### Space Complexity:
- **O(9^2)**, due to the recursive call stack and storing the board itself (since it's a 9x9 grid).



---


### Section 1: LeetCode Link, Problem Statement, Examples, and Approaches

[LeetCode #37 - Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

---

#### Problem Statement:

You are given a 9x9 Sudoku board (partially filled) where empty cells are represented by `'.'`. The task is to fill the empty cells such that each row, column, and each of the nine 3x3 sub-boxes contains digits from `1` to `9` with the following constraints:
1. Each digit must appear exactly once in each row.
2. Each digit must appear exactly once in each column.
3. Each digit must appear exactly once in each of the nine 3x3 sub-boxes.

You are required to modify the board in-place to solve the Sudoku puzzle.

#### Example:
```plaintext
Input:
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

Output: The board is solved as follows:
[
  ["5","3","4","6","7","8","9","1","2"],
  ["6","7","2","1","9","5","3","4","8"],
  ["1","9","8","3","4","2","5","6","7"],
  ["8","5","9","7","6","1","4","2","3"],
  ["4","2","6","8","5","3","7","9","1"],
  ["7","1","3","9","2","4","8","5","6"],
  ["9","6","1","5","3","7","2","8","4"],
  ["2","8","7","4","1","9","6","3","5"],
  ["3","4","5","2","8","6","1","7","9"]
]
```

---

### Approach 1: Backtracking

The main approach to solving Sudoku is **backtracking**, where we try to fill each empty cell with a valid number (from 1 to 9) while adhering to the Sudoku rules.

#### Steps:
1. **Find Empty Cell**: First, locate an empty cell in the Sudoku board.
2. **Place a Valid Number**: For each empty cell, try placing digits from `1` to `9`. Check whether placing a specific number in that cell is valid (i.e., does not violate the row, column, or 3x3 sub-box constraints).
3. **Recur**: Move to the next empty cell and try the same process.
4. **Backtrack**: If placing a number leads to an invalid configuration, backtrack by removing the number and trying a different number in the previous step.

The algorithm continues until all cells are filled with valid numbers, and the Sudoku board is solved.

#### Code:

```python
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying the board in-place.
        """

        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            # Check if the number is not in the current row, column, or 3x3 sub-box.
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
                
                box_row = 3 * (row // 3) + i // 3
                box_col = 3 * (col // 3) + i % 3
                if board[box_row][box_col] == num:
                    return False

            return True

        def backtrack() -> bool:
            # Find the next empty spot
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        # Try placing digits from '1' to '9'
                        for num in '123456789':
                            if is_valid(board, row, col, num):
                                board[row][col] = num  # Place the number

                                if backtrack():
                                    return True

                                board[row][col] = '.'  # Undo the placement (backtrack)
                        return False
            return True

        backtrack()
```

#### Time Complexity:
The time complexity of this solution is **exponential** in the worst case due to the nature of backtracking, approximately $O(9^{(N^2)})$, where $N = 9$ is the board size. In the worst case, each empty cell might need to check 9 possibilities.

#### Space Complexity:
The space complexity is **$O(1)$** since we modify the board in-place and only use a constant amount of extra space for checking the validity.

---

### Section 2: Approaches Comparison and Test Function

---

#### Approaches Comparison

| Approach              | Time Complexity      | Space Complexity     | Description                                                                       |
|-----------------------|----------------------|----------------------|-----------------------------------------------------------------------------------|
| **Backtracking**       | $O(9^{N^2})$         | $O(1)$               | Tries placing digits one by one, using backtracking when conflicts arise.          |

---

#### Test Function


```python

def test_sudoku_solver():
    solution = Solution()

    # Test Case 1: Standard partially filled Sudoku puzzle
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solution.solveSudoku(board1)
    expected1 = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    assert board1 == expected1, "Test Case 1 Failed"

    # Test Case 2: Almost completed Sudoku puzzle (only one cell empty)
    board2 = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","."],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    solution.solveSudoku(board2)
    expected2 = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    assert board2 == expected2, "Test Case 2 Failed"

    # Test Case 3: Already solved Sudoku puzzle
    board3 = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    solution.solveSudoku(board3)
    expected3 = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    assert board3 == expected3, "Test Case 3 Failed"

    print("All test cases passed!")

# Run the test function
test_sudoku_solver()


```


