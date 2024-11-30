

[LeetCode #208 - Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

---

### Problem Statement:
Implement a Trie (Prefix Tree) with the following operations:
- **`insert(word)`**: Inserts a word into the trie.
- **`search(word)`**: Returns `true` if the word is in the trie (i.e., it was inserted previously), and `false` otherwise.
- **`startsWith(prefix)`**: Returns `true` if there is any word in the trie that starts with the given prefix, and `false` otherwise.

---

### Example:

**Example 1**:

```text
Input:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
```

---

### Constraints:
- All inputs consist of lowercase English letters.
- All inputs are non-empty strings.
- Methods `insert`, `search`, and `startsWith` will be called at most $3 \times 10^4$ times.

---

### Approaches:

#### 1. **Trie Node Implementation**

A Trie is a tree-like data structure where each node represents a single character of the inserted word. Every word is a path in this tree. Each node has:
1. A boolean flag `isEnd` to indicate if a word ends at this node.
2. A dictionary `children` that maps a character to another Trie node.

We can perform the following operations:

- **`insert(word)`**: Traverse the trie and insert the word character by character. If a character does not exist, create a new node. Mark the last node as the end of a word.
- **`search(word)`**: Traverse the trie, character by character. If the word exists and the last node is marked as the end of the word, return `true`.
- **`startsWith(prefix)`**: Traverse the trie up to the length of the prefix. If all characters in the prefix exist, return `true`.

Here’s how the methods work:

- **`insert(word)`**:
  - Starting at the root node, check each character of the word.
  - If the character does not exist as a child, create a new TrieNode.
  - Move to the next node and repeat until the entire word is inserted.
  - Mark the last node as the end of the word.

- **`search(word)`**:
  - Traverse each character of the word in the trie.
  - If the character is not found at any point, return `false`.
  - If all characters are found and the last node marks the end of the word, return `true`.

- **`startsWith(prefix)`**:
  - Similar to `search(word)`, but we don’t need to check if the last node marks the end of a word.

---

### Code Implementation:

```python
class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes for each character
        self.children = {}
        # Boolean to mark the end of a word
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        # Initialize the root node of the trie
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Insert a word into the trie
        node = self.root
        for char in word:
            # If the character is not in the children, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of the word
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        # Search for a word in the trie
        node = self.root
        for char in word:
            # If character is not in the children, return False
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True if it's the end of the word, else False
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        # Search for a prefix in the trie
        node = self.root
        for char in prefix:
            # If character is not in the children, return False
            if char not in node.children:
                return False
            node = node.children[char]
        # Return True as long as the prefix is found
        return True
```

---

### Explanation:

- **TrieNode Class**:
  - `children`: A dictionary to store the mapping of characters to their corresponding child TrieNode.
  - `isEndOfWord`: A boolean that indicates if the node marks the end of a word.

- **Trie Class**:
  - `insert(word)`: Iterates through the word, creates nodes as needed, and marks the end of the word.
  - `search(word)`: Follows the nodes according to the word characters. Returns `true` if the word exists and ends correctly.
  - `startsWith(prefix)`: Similar to `search`, but returns `true` as long as the prefix is found.



### Section 2: Approaches Comparison and Test Function

---

#### Approaches Comparison

| Approach              | Time Complexity                             | Space Complexity                             | Description                                                                 |
|-----------------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------|
| **Trie (Prefix Tree)** | $O(m)$ per operation, where $m$ is the length of the word/prefix | $O(n \cdot k)$ where $n$ is the number of words, and $k$ is the average length of the word | Efficient approach for storing and searching words and prefixes using Trie. Each insert, search, or startsWith operation takes time proportional to the length of the word/prefix. |

- **Time Complexity**:
  - **Insert**: Inserting a word of length $m$ requires iterating over all $m$ characters. Thus, it takes $O(m)$ for insertion.
  - **Search**: Searching for a word of length $m$ takes $O(m)$, as we iterate over each character.
  - **StartsWith**: Similar to `search`, it takes $O(m)$, where $m$ is the length of the prefix.
  
- **Space Complexity**:
  - Space is proportional to the total number of nodes in the trie. In the worst case, each node has $26$ children (for each letter in the alphabet), and we might need $O(n \cdot k)$ space for storing $n$ words with average length $k$.

---

#### Test Function

To validate the `Trie` implementation, we can write a test function that checks the distinct operations and covers a variety of test cases:

```python
def test_trie():
    # Initialize the trie
    trie = Trie()
    
    # Test case 1: Insert and search
    trie.insert("apple")
    assert trie.search("apple") == True, "Test Case 1 Failed"
    assert trie.search("app") == False, "Test Case 1 Failed"
    assert trie.startsWith("app") == True, "Test Case 1 Failed"
    
    # Test case 2: Insert and recheck
    trie.insert("app")
    assert trie.search("app") == True, "Test Case 2 Failed"
    
    # Test case 3: Insert more words
    trie.insert("banana")
    assert trie.search("banana") == True, "Test Case 3 Failed"
    assert trie.startsWith("ban") == True, "Test Case 3 Failed"
    assert trie.search("band") == False, "Test Case 3 Failed"
    
    # Test case 4: Edge case for prefix
    trie.insert("car")
    trie.insert("card")
    assert trie.startsWith("ca") == True, "Test Case 4 Failed"
    assert trie.search("car") == True, "Test Case 4 Failed"
    assert trie.search("card") == True, "Test Case 4 Failed"
    
    # Test case 5: No match
    assert trie.search("cat") == False, "Test Case 5 Failed"
    assert trie.startsWith("cat") == False, "Test Case 5 Failed"
    
    print("All test cases passed!")

# Run the test function
test_trie()
```

---

