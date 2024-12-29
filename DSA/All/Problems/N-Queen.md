


[N Queen @InsideCode](https://www.youtube.com/watch?v=KTygpUDUJ6Q)





### Problem Statement: N-Queens Problem

The N-Queens problem involves placing **n** queens on an **n x n** chessboard such that no two queens attack each other. A queen can attack another if they share the same row, column, or diagonal.

The goal is to find all the distinct solutions for placing **n** queens on the board where none of them can attack each other. The output should be a list of solutions, where each solution is represented as an **n-length array of strings**. In these strings, the character 'Q' represents a queen and '.' represents an empty space.

### Example:

For **n = 4**, there are two distinct solutions:

```
[ [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."] ]
```

### Solution:

Here’s the corrected and refined code to solve the N-Queens problem:

```python
from typing import List, Set

class Solution:
    """
    Solves the N-Queens problem: placing n queens on an n x n chessboard 
    such that no two queens attack each other.
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        # Start recursive search with an empty board state
        self.search([], solutions, n)
        return solutions

    def is_valid_state(self, state: List[int], n: int) -> bool:
        # A valid solution is found when the number of queens equals n
        return len(state) == n

    def get_candidates(self, state: List[int], n: int) -> Set[int]:
        # Get valid column positions for the next queen
        if not state:
            return set(range(n))  # All columns are valid for the first queen

        # Current row we are filling with a queen
        current_row = len(state)
        candidates = set(range(n))  # Start with all columns as candidates

        # Remove columns that are under attack from previous queens
        for row, col in enumerate(state):
            candidates.discard(col)  # Same column attack
            distance = current_row - row
            candidates.discard(col + distance)  # Diagonal attack (bottom right)
            candidates.discard(col - distance)  # Diagonal attack (bottom left)
        
        return candidates

    def search(self, state: List[int], solutions: List[List[str]], n: int):
        # If a valid solution is found, format it and store it
        if self.is_valid_state(state, n):
            solutions.append(self.state_to_string(state, n))
            return

        # Try placing a queen in each valid column
        for candidate in self.get_candidates(state, n):
            state.append(candidate)  # Place queen
            self.search(state, solutions, n)  # Recurse to the next row
            state.pop()  # Backtrack to try the next candidate

    def state_to_string(self, state: List[int], n: int) -> List[str]:
        # Convert the state (list of column indices) to a list of board strings
        board = []
        for col in state:
            row_string = '.' * col + 'Q' + '.' * (n - col - 1)
            board.append(row_string)
        return board
```

### Key Fix:
1. In the `get_candidates()` function, the `range(n)` was explicitly converted to `set(range(n))` to ensure that set operations like `discard()` work correctly.

### Solution Explanation:

1. **solveNQueens**: This is the main function that initializes the recursive search to find solutions.
2. **is_valid_state**: Checks if the current state (queen positions) is valid by verifying that it contains **n** queens.
3. **get_candidates**: This function returns valid column positions for placing a queen in the current row. It eliminates columns under attack by previous queens based on their row, column, and diagonal positions.

### Context:
In the N-Queens problem, a queen can attack another queen if they share the same:
1. **Column**
2. **Row** (but we're not concerned about rows since each queen is placed in a different row)
3. **Diagonal** (both left and right diagonals)

### Code Breakdown:

```python
for row, col in enumerate(state):
    candidates.discard(col)  # Same column attack
    distance = current_row - row
    candidates.discard(col + distance)  # Diagonal attack (bottom right)
    candidates.discard(col - distance)  # Diagonal attack (bottom left)
```

#### Variables:
- **`state`**: This is a list where each element represents the column position of a queen in a specific row. The index of the list represents the row number.
    - Example: `state = [1, 3, 0]` means:
        - Row 0: Queen at column 1
        - Row 1: Queen at column 3
        - Row 2: Queen at column 0
- **`current_row`**: This is the row where we are trying to place the next queen.
- **`candidates`**: This is a set containing all the valid column indices where we can place a queen in the current row. We want to discard any columns that are under attack from queens placed in previous rows.

#### Loop Breakdown:

1. **`for row, col in enumerate(state):`**
   - The loop iterates over all the previously placed queens, where `row` is the row index and `col` is the column index of the queen placed in that row.

2. **`candidates.discard(col)`**
   - This removes the column `col` from the set of candidates because a queen already occupies this column in row `row`. No other queen can be placed in this column.
   - **Why?** Queens in the same column can attack each other, so this column is invalid for the current row.

3. **`distance = current_row - row`**
   - This calculates the "distance" between the current row (where we are trying to place a new queen) and a previous row (`row`), where a queen has already been placed. This helps in identifying diagonal attacks.

4. **`candidates.discard(col + distance)`**
   - This removes `col + distance` from the set of candidates. This represents the diagonal attack on the **right diagonal** (i.e., bottom-right).
   - **Why?** Queens on a diagonal line have the same difference between their row and column indices. For instance:
     - If there is a queen at (row 1, col 1), then no other queen can be placed at (row 2, col 2), (row 3, col 3), etc., because they lie on the same diagonal line.
   - The `col + distance` checks for this kind of diagonal attack.

5. **`candidates.discard(col - distance)`**
   - This removes `col - distance` from the set of candidates. This represents the diagonal attack on the **left diagonal** (i.e., bottom-left).
   - **Why?** Similar to the right diagonal, queens on the left diagonal also follow the same pattern. The `col - distance` checks for this diagonal attack.
   - Example:
     - If there is a queen at (row 1, col 3), no other queen can be placed at (row 2, col 2), (row 3, col 1), etc., because they lie on the same left diagonal line.

   
4. **search**: Recursively places queens in valid positions and backtracks when necessary to explore all possible configurations.
5. **state_to_string**: Converts the current state (list of column positions) into the board's string representation to format the output.

### Example Usage:

```python
solution = Solution()
n = 4
result = solution.solveNQueens(n)
print(result)
```

### Output for `n = 4`:
```
[['.Q..', '...Q', 'Q...', '..Q.'],
 ['..Q.', 'Q...', '...Q', '.Q..']]
``` 

This solution efficiently explores all valid queen placements using backtracking.



#### Tags

`Backtracking`, `Hard`, `N Queen`


---

[N Queen problem - Inside Code](https://youtu.be/KTygpUDUJ6Q?si=4jGu_siAe9028VoW)



## N-Queens Problem

### Problem Statement

The N-Queens problem involves placing \(n\) queens on an \(n \times n\) chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal. The task is to find all possible ways to place \(n\) queens on the board that satisfy this condition.

For example, the 8-Queens problem is a specific case of the N-Queens problem where \(n = 8\). The goal is to place 8 queens on an 8x8 board without any two queens threatening each other.

### Example
For \(n = 4\), one valid solution looks like this (with 'Q' representing a queen):

```
. Q . .
. . . Q
Q . . .
. . Q .
```

This is one of two possible solutions for \(n = 4\).

---


```python

def solveNQueens(n: int) -> List[List[str]]:

        board = [[0]*n for _ in range(n)]
        results = []


        def is_safe(r_idx, c_idx):

            dep_r_idx = r_idx
            while dep_r_idx > -1:
                # check unique in col i.e horizontally
                if board[dep_r_idx][c_idx] == 1:
                    return False

                # check row diagnols
                dig_diff = r_idx - dep_r_idx
                dig_bef = c_idx - dig_diff
                dig_aft = c_idx + dig_diff
                if dig_bef > -1:
                    if board[dep_r_idx][dig_bef] == 1:
                        return False
                if dig_aft < len(board):
                    if board[dep_r_idx][dig_aft] == 1:
                        return False

                dep_r_idx -= 1

            return True

        def convert_board():
            values = []
            for r in board:
                val = ''
                for c in range(len(r)):
                    if(r[c] == 1):
                        val += 'Q'
                    else:
                        val += '.'

                values.append(val)
            return values


        def rec(r_id):
            if r_id == n:
                results.append(convert_board())
                return
            else:
                sols = []
                for c_id in range(n):
                    if is_safe(r_id, c_id):
                        board[r_id][c_id] = 1
                        rec(r_id + 1)
                        board[r_id][c_id] = 0

                return sols


        rec(0)
        print(n, results)
        return results

```

### Approach 1: Backtracking

**Explanation:**

The backtracking approach is a recursive algorithm that explores all possible placements of queens on the chessboard row by row. If a queen can be placed safely in a row (i.e., it doesn't threaten any already-placed queens), the algorithm proceeds to place the next queen. If no safe placement is possible in a row, the algorithm backtracks to the previous row and tries a different placement.

The key concept is to check whether a cell is safe by ensuring no queen is placed in the same column or on either diagonal.

**Algorithm Steps:**
1. Place a queen in the first row.
2. For each subsequent row, try to place a queen in any column that is safe.
3. Use recursion to place queens in the next rows.
4. If you reach a row where no column is safe, backtrack by removing the queen from the previous row and trying the next column.
5. Repeat until all queens are placed.

**Code:**

```python
from typing import List

def is_safe(board: List[List[int]], i: int, j: int) -> bool:
    """Check if it's safe to place a queen at board[i][j]."""
    n = len(board)
    j_left = j
    j_right = j
    while i >= 0:
        # Check the current column, left diagonal, and right diagonal
        if (j_left >= 0 and board[i][j_left] == 1) or board[i][j] == 1 or (j_right < n and board[i][j_right] == 1):
            return False
        i -= 1
        j_left -= 1
        j_right += 1
    return True

def rec(board: List[List[int]], i: int) -> int:
    """Recursively place queens and count solutions."""
    n = len(board)
    if i == n:
        return 1  # Found a valid solution
    else:
        nb_solutions = 0
        for j in range(n):
            if is_safe(board, i, j):
                board[i][j] = 1  # Place queen
                nb_solutions += rec(board, i + 1)
                board[i][j] = 0  # Backtrack
        return nb_solutions

def n_queens(n: int) -> int:
    """Return the number of solutions for the N-Queens problem."""
    board = [[0] * n for _ in range(n)]
    return rec(board, 0)

print(n_queens(8))  # Output: 92
```

**Time Complexity:**

- The time complexity of this approach is \(O(n^2 \cdot n!)\), as we are recursively checking placements for each row and backtracking if needed.
- For each row, we try placing the queen in every column and then recursively proceed to the next row.

**Space Complexity:**

- The space complexity is \(O(n^2)\) for storing the chessboard.

---

### Approach 2: Optimized Backtracking with Column and Diagonal Tracking

**Explanation:**

Instead of checking the entire board for threats every time a queen is placed, we can optimize the backtracking approach by using additional arrays to track which columns and diagonals are already occupied. This eliminates the need to traverse the board to check for conflicts, reducing the time spent in the `is_safe` function.

We maintain three arrays:
- `cols`: To track which columns are occupied.
- `diagonals_1`: To track the main diagonals (from top-left to bottom-right).
- `diagonals_2`: To track the anti-diagonals (from top-right to bottom-left).

**Code:**

```python
def n_queens_optimized(n: int) -> int:
    """Return the number of solutions using an optimized backtracking approach."""
    def backtrack(row: int) -> int:
        if row == n:
            return 1
        solutions = 0
        for col in range(n):
            if cols[col] or diagonals_1[row - col] or diagonals_2[row + col]:
                continue
            # Place the queen
            cols[col] = diagonals_1[row - col] = diagonals_2[row + col] = True
            solutions += backtrack(row + 1)
            # Remove the queen (backtrack)
            cols[col] = diagonals_1[row - col] = diagonals_2[row + col] = False
        return solutions

    # Initialize column and diagonal tracking arrays
    cols = [False] * n
    diagonals_1 = [False] * (2 * n - 1)
    diagonals_2 = [False] * (2 * n - 1)
    
    return backtrack(0)

print(n_queens_optimized(8))  # Output: 92
```

**Time Complexity:**

- The time complexity is improved to \(O(n!)\) since checking for conflicts is now constant time for each queen placement.

**Space Complexity:**

- The space complexity is \(O(n)\), as we only need to store the state of columns and diagonals.

---

### Summary of Approaches

| Approach                                  | Time Complexity     | Space Complexity   | Explanation                                                                                                                                     |
|-------------------------------------------|---------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Backtracking                              | \(O(n^2 \cdot n!)\) | \(O(n^2)\)         | Simple backtracking, checks the board for safe placements and backtracks if a conflict is found.                                                 |
| Optimized Backtracking with Column and Diagonal Tracking | \(O(n!)\)           | \(O(n)\)           | Uses arrays to track columns and diagonals, reducing the time spent checking for conflicts during queen placement.                                |

---

Both approaches solve the N-Queens problem, but the optimized approach is faster and more efficient, especially for larger values of \(n\).




----


### Section 1: LeetCode Link, Problem Statement, Examples, and Approaches

[LeetCode #51 - N-Queens](https://leetcode.com/problems/n-queens/)

---

#### Problem Statement

The **N-Queens** problem involves placing $N$ queens on an $N \times N$ chessboard in such a way that no two queens threaten each other. This means:
- No two queens can be in the same row.
- No two queens can be in the same column.
- No two queens can be on the same diagonal.

Your task is to return all possible distinct solutions to the N-Queens problem, where each solution represents a valid placement of queens on the board. Each solution must be a list of strings where `"Q"` represents a queen and `"."` represents an empty space.

#### Example 1:
```plaintext
Input: n = 4
Output: 
[
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]
```

#### Example 2:
```plaintext
Input: n = 1
Output: [["Q"]]
```

---

### Approach 1: Backtracking

Backtracking is the most common and intuitive approach to solving the N-Queens problem. The key idea is to place queens on the board row by row and backtrack if an invalid placement occurs.

We use three arrays to track conflicts:
1. **columns**: To ensure no two queens are placed in the same column.
2. **diagonals1**: To track the queens on the “/” diagonals (sum of row and column is constant).
3. **diagonals2**: To track the queens on the “\” diagonals (difference between row and column is constant).

#### Algorithm Steps:
1. Start from row 0 and try to place a queen in each column.
2. For each valid placement, move to the next row and repeat.
3. If an invalid placement occurs (column or diagonal conflict), backtrack and try another column.
4. Once you successfully place queens in all rows, add the solution to the result.
5. Repeat this process for all possible placements.

#### Code:

Note: convert to matrix with 0 and 1 and solve and return result in required form!


```python
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                board = ["".join(row) for row in current_board]
                results.append(board)
                return

            for col in range(n):
                if col in columns or (row + col) in diagonals1 or (row - col) in diagonals2:
                    continue

                # Place the queen
                current_board[row][col] = 'Q'
                columns.add(col)
                diagonals1.add(row + col)
                diagonals2.add(row - col)

                # Recur to the next row
                backtrack(row + 1)

                # Backtrack and remove the queen
                current_board[row][col] = '.'
                columns.remove(col)
                diagonals1.remove(row + col)
                diagonals2.remove(row - col)

        results = []
        current_board = [["."] * n for _ in range(n)]
        columns, diagonals1, diagonals2 = set(), set(), set()

        backtrack(0)
        return results
```

#### Time Complexity:
The time complexity of the backtracking approach is approximately $O(N!)$, as the algorithm places $N$ queens one at a time, exploring all potential configurations.

#### Space Complexity:
The space complexity is $O(N^2)$ because we use a board of size $N \times N$, and we also use extra sets for columns, diagonals1, and diagonals2.

---

### Section 2: Approaches Comparison and Test Function

---

#### Approaches Comparison

| Approach              | Time Complexity      | Space Complexity     | Description                                                                       |
|-----------------------|----------------------|----------------------|-----------------------------------------------------------------------------------|
| **Backtracking**       | $O(N!)$              | $O(N^2)$              | The most common and intuitive solution for N-Queens, exploring all valid placements. |


---

#### Test Function

```python
from typing import List

def test_nqueens(func):
    # Test case 1: Standard case for N = 4

    assert func(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."]
    ], "Test Case 1 Failed"

    # Test case 2: Single queen (N = 1)
    assert func(1) == [["Q"]], "Test Case 2 Failed"

    # Test case 3: N = 5
    assert func(5) == [['Q....', '..Q..', '....Q', '.Q...', '...Q.'], ['Q....', '...Q.', '.Q...', '....Q', '..Q..'], ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'], ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'], ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'], ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'], ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'], ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'], ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'], ['....Q', '..Q..', 'Q....', '...Q.', '.Q...']], "Test Case 3 Failed"

    # Test case 4: N = 2 (no solutions)
    assert func(2) == [], "Test Case 4 Failed"

    # Test case 5: N = 3 (no solutions)
    assert func(3) == [], "Test Case 5 Failed"

    print("All test cases passed!")


```

---

By running these test cases, we ensure that the N-Queens algorithm works correctly across a variety of board sizes and configurations.


---

others:


### 4. **N-Queens Problem**

**Problem:** The N-Queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. Write a program to solve the N-Queens problem.

```python
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def solve(board, row):
        if row == n:
            result.append(["." * i + "Q" + "." * (n - i - 1) for i in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    result = []
    solve([-1] * n, 0)
    return result
```

---
