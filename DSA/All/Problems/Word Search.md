


## Problem

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
