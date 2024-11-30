

[Alphabet board path problem (LeetCode #1138) - Inside code](https://youtu.be/gQGCiMPrnaY?si=4NGSS4VzJsqMc1TZ)


### Problem Statement

You are given a fixed alphabet board represented as follows:

```
a b c d e
f g h i j
k l m n o
p q r s t
u v w x y
z
```

You start at the top-left corner (position (0, 0)) and are given a target string. Your task is to determine the sequence of moves required to spell out the target string on the board. The allowed moves are:
- **U**: up
- **D**: down
- **L**: left
- **R**: right
- **!**: write the letter at your current position

You cannot move outside the boundaries of the board.

### Input
- A string `target` (1 <= |target| <= 100) containing lowercase letters.

### Output
- A string representing the sequence of moves to write the target string.

### Example

**Input:**
```
target = "leet"
```

**Output:**
```
"DDRR!UU!R!DD!"
```

### Solution

1. **Mapping Letters to Positions:**
   Create a dictionary that maps each letter to its corresponding board coordinates. For example, 'a' is at (0, 0), 'b' is at (0, 1), ..., 'z' is at (5, 0).

2. **Initialize Position:**
   Start at the top-left cell (0, 0).

3. **Iterate through Target String:**
   For each letter in the target string:
   - Retrieve its coordinates (next_i, next_j) from the mapping.
   - Move from the current position (i, j) to (next_i, next_j) using vertical and horizontal moves.
   - If moving horizontally first results in out-of-bounds issues (especially when at 'z'), adjust the starting position temporarily.

4. **Construct Moves:**
   Append the corresponding move characters (U, D, L, R) to a list and add an exclamation mark after reaching each letter's position.

5. **Output the Result:**
   Join the list of moves into a single string and return it.

### Python Implementation

```python
def alphabet_board_path(target):
    # Create a mapping of letters to their positions
    pos = {chr(i + ord('a')): (i // 5, i % 5) for i in range(26)}
    moves = []
    i, j = 0, 0  # Start at the top-left corner (0, 0)

    for char in target:
        next_i, next_j = pos[char]
        
        # Handle 'z' edge case
        if i == 5 and j == 0 and char != 'z':
            moves.append('U')
            i -= 1  # Move up temporarily
        
        # Move vertically ( vertical first based on z edge case)
        while i < next_i:
            moves.append('D')
            i += 1
        while i > next_i:
            moves.append('U')
            i -= 1
        
        # Move horizontally
        while j < next_j:
            moves.append('R')
            j += 1
        while j > next_j:
            moves.append('L')
            j -= 1
        
        # Write the letter
        moves.append('!')
    
    return ''.join(moves)

# Example usage
target = "leet"
print(alphabet_board_path(target))  # Output: "DDRR!UU!R!DD!"
```


```python
def alphabet_board(target):
    letters_map = {}
    for i in range(26):
        letter = chr(ord('a') + i)
        letters_map[letter] = (i//5, i%5)
    moves = []
    i, j = 0, 0
    for letter in target:
        next_i, next_j = letters_map[letter]
        if (i, j) == letters_map['z'] and letter != 'z':
            moves.append('U')
            i -= 1
        while j != next_j:
            if j < next_j:
                moves.append('R')
                j += 1
            else:
                moves.append('L')
                j -= 1
        while i != next_i:
            if i < next_i:
                moves.append('D')
                i += 1
            else:
                moves.append('U')
                i -= 1
        moves.append('!')
    return ''.join(moves)
```

* adding char to string create new string in py, so we are making array and at last we are converting into string
### Complexity Analysis
- **Time Complexity:** O(n), where n is the length of the target string. Each letter requires at most a constant number of moves.
- **Space Complexity:** O(n) for storing the moves.






