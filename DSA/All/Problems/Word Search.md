



### Problem Statement: Word Search

In a Word Search puzzle, you are given a grid of letters and a list of words. Your task is to find each word in the grid. Words can be placed in any direction: horizontally (left to right or right to left), vertically (top to bottom or bottom to top), or diagonally (in any of the four diagonal directions). 

#### Input:
1. A grid of characters (m x n) where `m` is the number of rows and `n` is the number of columns.
2. A list of words to search for within the grid.

#### Output:
- A list of words found in the grid. Each word should be reported once, regardless of how many times it appears in the grid.

#### Examples:

**Example 1:**

- **Input:**
  ```
  Grid:
  [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  
  Words: ["ABCCED", "SEE", "ABCB"]
  ```

- **Output:**
  ```
  ["ABCCED", "SEE"]
  ```

**Example 2:**

- **Input:**
  ```
  Grid:
  [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]
  
  Words: ["ABCCED", "ASDF", "SEE", "CDE"]
  ```

- **Output:**
  ```
  ["ABCCED", "SEE", "CDE"]
  ```

**Example 3:**

- **Input:**
  ```
  Grid:
  [
    ['X', 'Y', 'Z', 'A'],
    ['B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I']
  ]
  
  Words: ["XYZ", "BCE", "HIG", "DAB"]
  ```

- **Output:**
  ```
  ["XYZ", "BCE", "HIG"]
  ```

### Notes:
- The grid may contain duplicate letters, and the same letter can be used to form multiple words, provided that they are formed without reusing the same letter position in a single word.
- Words that cannot be formed should not be included in the output list.





to try {

single word have or not with dfs
multiple word - cache results and find somehow
use trie -> left , right, top, bottom.. 

}

```python
from typing import List

test_cases = [
    {
        "name": "Word Found Horizontally",
        "grid": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "input": "ABC",
        "expected": True,
        # The word "ABC" is present in the first row horizontally.
    },
    {
        "name": "Word Found Vertically",
        "grid": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "input": "SEE",
        "expected": True,
        # The word "SEE" is present vertically in the last column.
    },
    {
        "name": "Word Found Diagonally",
        "grid": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "input": "FAC",
        "expected": False,
        # The word "FAC" is not present.
    },
    {
        "name": "Word Not Found",
        "grid": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "input": "XYZ",
        "expected": False,
        # The word "XYZ" does not exist in the grid.
    },
    {
        "name": "Word Found Backwards",
        "grid": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "input": "CBA",
        "expected": True,
        # The word "CBA" can be found backwards starting from (0,2).
    },
    {
        "name": "Single Letter Word Found",
        "grid": [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        "input": "A",
        "expected": True,
        # The letter "A" is present multiple times in the grid.
    },
    {
        "name": "Word Found at Edge",
        "grid": [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P']
        ],
        "input": "ABCD",
        "expected": True,
        # The word "ABCD" is found horizontally in the first row.
    },
    {
        "name": "Long Word Not Found",
        "grid": [
            ['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'],
            ['I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P']
        ],
        "input": "ABCDEFGHIJK",
        "expected": False,
        # The word "ABCDEFGHIJK" is too long to fit in the grid.
    },
    {
        "name": "Word with Repeating Letters",
        "grid": [
            ['A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A']
        ],
        "input": "AAA",
        "expected": True,
        # The word "AAA" can be found in multiple ways in the grid.
    },
    {
        "name": "Disconnected Grid",
        "grid": [
            ['A', 'B'],
            ['C', 'D'],
            ['E', 'F']
        ],
        "input": "AE",
        "expected": False,
        # The letters "A" and "E" are in rows in which have middle row.
    },
    {
        "name": "Zig Zag letter words",
        "grid": [
            ['B', 'N','I','O'],
            ['G', 'O','R','D'],
            ['E', 'F','O','D']
        ],
        "input": "BOORING",
        "expected": True,
        # The letters "A" and "E" are in rows in which have middle row.
    },  {
        "name": "Zig Zag letter words [ but not needed repetations ]",
        "grid": [
            ['B', 'N','I','O'],
            ['G', 'O','R','D'],
            ['E', 'F','O','D']
        ],
        "input": "BOOORING",
        "expected": False,
        # we don't have 3 O's adjacent
    },
]

def run_test_for_func(word_search_func):
    print(f"Testing function: {word_search_func.__name__}")
    for case in test_cases:
        grid = case["grid"]
        input = case["input"]
        expected = case["expected"]
        result = word_search_func(grid, input)
        assert result == expected, f"Test case '{case['name']}' failed: expected {expected}, got {result}"
    print("All test cases completed!")


def word_search(grid:List[List[int]], word:str)-> bool:
    row_len = len(grid)
    if(not row_len):
        return False
    col_len = len(grid[0])
    if(not col_len):
        return False
    word_len = len(word)
    if((row_len*col_len) < word_len):
        return False

    def check_equality(r_idx:int, c_idx:int, letter_idx:int = 0, idx_set = set()):
        def is_valid_neighbour(rIdx:int, cIdx:int)->bool:
            return -1 < rIdx < row_len and -1 < cIdx < col_len and (rIdx,cIdx) not in idx_set
        remain_word_len = word_len - letter_idx - 1
        if(row_len * col_len < remain_word_len):
            return False
        elif(grid[r_idx][c_idx] == word[letter_idx]):
            idx_set.add((r_idx, c_idx))
            if(remain_word_len == 0):
                return True
            next_letter_idx = letter_idx + 1
            neighbours = [
                # North, East, South, West
                [r_idx-1, c_idx],[r_idx, c_idx+1],[r_idx-1, c_idx],[r_idx, c_idx-1],
                # NorthEast, SouthEast,SouthWest, NorthWest
                [r_idx-1,c_idx+1], [r_idx+1,c_idx+1],[r_idx+1,c_idx-1], [r_idx-1,c_idx-1]
            ]

            for neighbour in neighbours:
                if(is_valid_neighbour(neighbour[0], neighbour[1])):
                    if(check_equality(neighbour[0], neighbour[1], next_letter_idx, set(idx_set))):
                        return True
            else:
                return False
        else:
            return False

    for i in range(row_len):
        for j in range(col_len):
            if(check_equality(i,j)):
                return True
    else:
        return False


run_test_for_func(word_search)

```



---


### LeetCode Problem: [79. Word Search](https://leetcode.com/problems/word-search/)

---

### Problem Statement:

Given an `m x n` grid of characters `board` and a string `word`, return `true` if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same cell may not be used more than once.

---

### Examples:

#### Example 1:

Input:

```plaintext
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
```

Output:

```plaintext
true
```

#### Example 2:

Input:

```plaintext
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
```

Output:

```plaintext
true
```

#### Example 3:

Input:

```plaintext
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
```

Output:

```plaintext
false
```

---

### Constraints:

1. `m == board.length`
2. `n == board[i].length`
3. `1 <= m, n <= 6`
4. `1 <= word.length <= 15`
5. `board` and `word` consist only of lowercase and uppercase English letters.

---

### Approach: Backtracking

**Key Idea:**

- Start at each cell of the grid and attempt to match the first character of the word.
- Use Depth First Search (DFS) to explore all possible paths in the grid.
- Mark visited cells to avoid reusing them in the same word construction.

**Algorithm:**

1. Iterate through each cell in the grid.
2. Start DFS from each cell, checking adjacent cells recursively.
3. If all characters in the word are found, return `true`.
4. Restore the state of visited cells after exploring.

---

### Code in Python:

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(row, col, index):
            # Base cases: word fully matched or out of bounds
            if index == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]:
                return False
            
            # Mark cell as visited
            temp, board[row][col] = board[row][col], "#"
            
            # Explore neighbors
            found = (backtrack(row + 1, col, index + 1) or
                     backtrack(row - 1, col, index + 1) or
                     backtrack(row, col + 1, index + 1) or
                     backtrack(row, col - 1, index + 1))
            
            # Restore cell state
            board[row][col] = temp
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False
```

---

### Code in Rust:

```rust
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut board = board;
        let rows = board.len();
        let cols = board[0].len();
        let word_chars: Vec<char> = word.chars().collect();

        fn backtrack(board: &mut Vec<Vec<char>>, word: &[char], index: usize, row: usize, col: usize) -> bool {
            if index == word.len() {
                return true;
            }
            if row >= board.len() || col >= board[0].len() || board[row][col] != word[index] {
                return false;
            }

            let temp = board[row][col];
            board[row][col] = '#'; // Mark as visited

            let found = 
                (row > 0 && backtrack(board, word, index + 1, row - 1, col)) ||
                (row + 1 < board.len() && backtrack(board, word, index + 1, row + 1, col)) ||
                (col > 0 && backtrack(board, word, index + 1, row, col - 1)) ||
                (col + 1 < board[0].len() && backtrack(board, word, index + 1, row, col + 1));

            board[row][col] = temp; // Restore the state
            found
        }

        for r in 0..rows {
            for c in 0..cols {
                if backtrack(&mut board, &word_chars, 0, r, c) {
                    return true;
                }
            }
        }

        false
    }
}
```



```rust
fn ans_func(mut board: Vec<Vec<char>>, word: String) -> bool {
        let word_chars: Vec<char> = word.chars().collect();
        let row_len = board.len();
        let col_len = board[0].len();

        // Define the recursive backtracking function with necessary parameters passed
        fn backtrack_board(
            board: &mut Vec<Vec<char>>,
            i: usize,
            j: usize,
            word_chars: &Vec<char>,
            char_index: usize,
            row_len: usize,
            col_len: usize,
        ) -> bool {
            // Check if the current cell doesn't match the current character in the word
            if board[i][j] != word_chars[char_index] {
                return false;
            }

            // Mark the cell as visited
            let backup_char = board[i][j];
            board[i][j] = '#';

            let next_char_index = char_index + 1;

            // If we've found all characters in the word
            if next_char_index == word_chars.len() {
                return true;
            }

            // Explore all 4 possible directions safely
            let found_inner = (i > 0
                && backtrack_board(
                    board,
                    i - 1,
                    j,
                    word_chars,
                    next_char_index,
                    row_len,
                    col_len,
                ))
                || (i + 1 < row_len
                    && backtrack_board(
                        board,
                        i + 1,
                        j,
                        word_chars,
                        next_char_index,
                        row_len,
                        col_len,
                    ))
                || (j > 0
                    && backtrack_board(
                        board,
                        i,
                        j - 1,
                        word_chars,
                        next_char_index,
                        row_len,
                        col_len,
                    ))
                || (j + 1 < col_len
                    && backtrack_board(
                        board,
                        i,
                        j + 1,
                        word_chars,
                        next_char_index,
                        row_len,
                        col_len,
                    ));

            // Restore the cell (backtrack)
            board[i][j] = backup_char;

            found_inner
        }

        // Iterate over each cell in the board
        for i in 0..row_len {
            for j in 0..col_len {
                if backtrack_board(&mut board, i, j, &word_chars, 0, row_len, col_len) {
                    return true;
                }
            }
        }

        false
    }
```
---

### Complexity Analysis:

1. **Time Complexity**:
    
    - In the worst case, the algorithm explores every cell and every path, leading to $O(N \cdot 3^L)$, where:
        - $N$ is the number of cells in the board ($m \times n$).
        - $L$ is the length of the word.
        - Each cell has at most 3 unvisited neighbors to explore.
2. **Space Complexity**:
    
    - $O(L)$ for the recursion stack, where $L$ is the length of the word.

---

### Test Cases:

```rust
fn test_func(ans_func: fn(Vec<Vec<char>>, String) -> bool) {
	let cases = vec![
		// Test Case 1: Word Found Horizontally
		(
			vec![
				vec!['A', 'B', 'C', 'E'],
				vec!['S', 'F', 'C', 'S'],
				vec!['A', 'D', 'E', 'E'],
			],
			String::from("ABC"),
			true,
		),
		// Test Case 2: Word Found Vertically
		(
			vec![
				vec!['A', 'B', 'C', 'E'],
				vec!['S', 'F', 'C', 'S'],
				vec!['A', 'D', 'E', 'E'],
			],
			String::from("SEE"),
			true,
		),
		// Test Case 3: Word Found Diagonally
		(
			vec![
				vec!['A', 'B', 'C', 'E'],
				vec!['S', 'F', 'C', 'S'],
				vec!['A', 'D', 'E', 'E'],
			],
			String::from("FAC"),
			false,
		),
		// Test Case 4: Word Not Found
		(
			vec![
				vec!['A', 'B', 'C', 'E'],
				vec!['S', 'F', 'C', 'S'],
				vec!['A', 'D', 'E', 'E'],
			],
			String::from("XYZ"),
			false,
		),
		// Test Case 5: Word Found Backwards
		(
			vec![
				vec!['A', 'B', 'C', 'E'],
				vec!['S', 'F', 'C', 'S'],
				vec!['A', 'D', 'E', 'E'],
			],
			String::from("CBA"),
			true,
		),
		// Test Case 6: Single Letter Word Found
		(
			vec![
				vec!['A', 'B', 'C', 'E'],
				vec!['S', 'F', 'C', 'S'],
				vec!['A', 'D', 'E', 'E'],
			],
			String::from("A"),
			true,
		),
		// Test Case 7: Word Found at Edge
		(
			vec![
				vec!['A', 'B', 'C', 'D'],
				vec!['E', 'F', 'G', 'H'],
				vec!['I', 'J', 'K', 'L'],
				vec!['M', 'N', 'O', 'P'],
			],
			String::from("ABCD"),
			true,
		),
		// Test Case 8: Long Word Not Found
		(
			vec![
				vec!['A', 'B', 'C', 'D'],
				vec!['E', 'F', 'G', 'H'],
				vec!['I', 'J', 'K', 'L'],
				vec!['M', 'N', 'O', 'P'],
			],
			String::from("ABCDEFGHIJK"),
			false,
		),
		// Test Case 9: Word with Repeating Letters
		(
			vec![
				vec!['A', 'A', 'A', 'A'],
				vec!['A', 'A', 'A', 'A'],
				vec!['A', 'A', 'A', 'A'],
				vec!['A', 'A', 'A', 'A'],
			],
			String::from("AAA"),
			true,
		),
		// Test Case 10: Disconnected Grid
		(
			vec![vec!['A', 'B'], vec!['C', 'D'], vec!['E', 'F']],
			String::from("AE"),
			false,
		),
		// Test Case 11: Zig-Zag letter words (true / false)
		(
			vec![
				vec!['B', 'N', 'I', 'O'],
				vec!['G', 'O', 'R', 'D'],
				vec!['E', 'F', 'O', 'D'],
			],
			String::from("BOORING"),
			// true,
			false,
		),
		// Test Case 12: Zig-Zag letter words with unnecessary repetitions
		(
			vec![
				vec!['B', 'N', 'I', 'O'],
				vec!['G', 'O', 'R', 'D'],
				vec!['E', 'F', 'O', 'D'],
			],
			String::from("BOOORING"),
			false,
		),
	];

	for (i, (board, word, expected)) in cases.iter().enumerate() {
		let result = ans_func(board.clone(), word.clone());
		assert_eq!(result, *expected, "Test case {} failed", i + 1);
	}
	println!("All test cases passed!");
}
```

---

### Summary of Approaches:

1. **Backtracking**: Core algorithm for solving this problem.
2. **Optimizations**: Use early exits or pre-checks to skip unnecessary computations.
3. **Implementation Tips**: Carefully handle grid boundaries and visited cells.

---


to refer {

https://www.youtube.com/shorts/7rLxa6eQi4M

https://www.youtube.com/watch?v=MEnQZUw5Wyg

https://www.youtube.com/watch?v=2mul77j6vVo


https://www.youtube.com/watch?v=z6OQBsorLV0

https://www.youtube.com/watch?v=pfiQ_PS1g8E


}

further word problems. {

https://www.youtube.com/watch?v=asbcE9mZz_U

https://www.youtube.com/watch?v=YTQjsPiMtRk


}


others code:



Runtime: 0ms

rust

```rust
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut counter = std::collections::HashMap::new();
        for letter in word.chars() {
            *counter.entry(letter).or_insert(0) += 1;
        }

        let word_chars: Vec<char> =
            if counter[&word.chars().next().unwrap()] >= counter[&word.chars().last().unwrap()] {
                word.chars().rev().collect()
            } else {
                word.chars().collect()
            };
        let word_length = word_chars.len();
        let m = board.len();
        let n = board[0].len();
        let mut visited = vec![vec![false; n]; m];
        for i in 0..m {
            for j in 0..n {
                if board[i][j] != word_chars[0] {
                    continue;
                }
                let mut path = vec![(i, j, 0)];
                while !path.is_empty() {
                    let path_length = path.len();
                    if path_length == word_length {
                        return true;
                    }
                    let (x, y, status) = path[path_length - 1];
                    let next_char = word_chars[path_length];
                    if status == 0 {
                        visited[x][y] = true;
                        if x > 0 && board[x - 1][y] == next_char && !visited[x - 1][y] {
                            path[path_length - 1].2 = 1;
                            path.push((x - 1, y, 0));
                        } else if x < m - 1 && board[x + 1][y] == next_char && !visited[x + 1][y] {
                            path[path_length - 1].2 = 2;
                            path.push((x + 1, y, 0));
                        } else if y > 0 && board[x][y - 1] == next_char && !visited[x][y - 1] {
                            path[path_length - 1].2 = 3;
                            path.push((x, y - 1, 0));
                        } else if y < n - 1 && board[x][y + 1] == next_char && !visited[x][y + 1] {
                            path[path_length - 1].2 = 4;
                            path.push((x, y + 1, 0));
                        } else {
                            visited[x][y] = false;
                            path.pop();
                        }
                    }
                    if status == 1 {
                        if x < m - 1 && board[x + 1][y] == next_char && !visited[x + 1][y] {
                            path[path_length - 1].2 = 2;
                            path.push((x + 1, y, 0));
                        } else if y > 0 && board[x][y - 1] == next_char && !visited[x][y - 1] {
                            path[path_length - 1].2 = 3;
                            path.push((x, y - 1, 0));
                        } else if y < n - 1 && board[x][y + 1] == next_char && !visited[x][y + 1] {
                            path[path_length - 1].2 = 4;
                            path.push((x, y + 1, 0));
                        } else {
                            visited[x][y] = false;
                            path.pop();
                        }
                    }
                    if status == 2 {
                        if y > 0 && board[x][y - 1] == next_char && !visited[x][y - 1] {
                            path[path_length - 1].2 = 3;
                            path.push((x, y - 1, 0));
                        } else if y < n - 1 && board[x][y + 1] == next_char && !visited[x][y + 1] {
                            path[path_length - 1].2 = 4;
                            path.push((x, y + 1, 0));
                        } else {
                            visited[x][y] = false;
                            path.pop();
                        }
                    }
                    if status == 3 {
                        if y < n - 1 && board[x][y + 1] == next_char && !visited[x][y + 1] {
                            path[path_length - 1].2 = 4;
                            path.push((x, y + 1, 0));
                        } else {
                            visited[x][y] = false;
                            path.pop();
                        }
                    }
                    if status == 4 {
                        visited[x][y] = false;
                        path.pop();
                    }
                }
            }
        }
        false
    }
}
```


Memory: 2.1mb

rust

```rust
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let (n, m) = (board.len(), board[0].len());
        let mut board = board;
        let words = word.chars().collect::<Vec<char>>();
        for i in 0..n {
            for j in 0..m {
                if Self::exist_sub(&mut board, i, j, &words, 0) {
                    return true;
                }
            }
        }
        false
    }

    fn exist_sub(board: &mut [Vec<char>], i: usize, j: usize, word: &[char], k: usize) -> bool {
        if k == word.len() {
            return true;
        }
        if i >= board.len() || j >= board[0].len() || board[i][j] != word[k] {
            return false;
        }
        let rec = board[i][j];
        board[i][j] = '\0';
        let mut res = false;
        if i > 0 {
            res = res || Self::exist_sub(board, i - 1, j, word, k + 1);
        }
        res = res || Self::exist_sub(board, i + 1, j, word, k + 1);
        if j > 0 {
            res = res || Self::exist_sub(board, i, j - 1, word, k + 1);
        }
        res = res || Self::exist_sub(board, i, j + 1, word, k + 1);
        board[i][j] = rec;
        res
    }
}
```


Runtime: 110ms

rust

```rust
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut visited = vec![vec![false; board[0].len()]; board.len()];
        let word: Vec<_> = word.chars().collect();
        for r in 0..board.len() as i32 {
            for c in 0..board[0].len() as i32 {
                if exist(r, c, &board, &mut visited, &word) {
                    return true;
                }
            }
        }
        false
    }
}
fn exist(
    r: i32, 
    c: i32,
    board: &Vec<Vec<char>>, 
    visited: &mut Vec<Vec<bool>>, 
    word: &[char]
) -> bool {
    if word.is_empty() {
        return true;
    }
    if r < 0 || r >= board.len() as i32 || c < 0 || c >= board[0].len() as i32 {
        return false;
    }
    if board[r as usize][c as usize] != word[0] {
        return false;
    }
    if visited[r as usize][c as usize] {
        return false;
    }
    visited[r as usize][c as usize] = true;
    for (dx, dy) in &[(1, 0), (-1, 0), (0, 1), (0, -1)] {
        if exist(r + dx, c + dy, board, visited, &word[1..]) {
            return true;
        }
    }
    visited[r as usize][c as usize] = false;
    false
}
```



