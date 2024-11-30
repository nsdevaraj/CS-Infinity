

## Maximum Depth of Binary Tree



 [LeetCode #104 - Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree).


## Problem: Maximum Depth of Binary Tree

### Problem Statement
Given the `root` of a binary tree, return its **maximum depth**.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example 1:
```plaintext
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3
```
Explanation: The depth of the tree with root 3 is 3, as the longest path is 3 -> 20 -> 7.

### Example 2:
```plaintext
Input: root = [1, null, 2]
Output: 2
```
Explanation: The depth of the tree with root 1 is 2, as the longest path is 1 -> 2.

### Constraints:
- The number of nodes in the tree is in the range [0, 10⁴].
- `-100 <= Node.val <= 100`

---

## Approaches to Solve the Problem

### Approach 1: Recursive DFS (Depth-First Search)
This approach uses recursion to explore the depth of both the left and right subtrees for each node. The depth of the current node is calculated as the maximum depth of its left and right subtree plus one.

#### Algorithm:
1. If the node is `None`, return `0` (base case for leaf nodes).
2. Recursively calculate the depth of the left and right subtrees.
3. The maximum depth at any node will be `1 + max(left depth, right depth)`.

#### Code:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

#### Time Complexity:
- **Time**: \( O(N) \), where \( N \) is the number of nodes in the tree. Each node is visited once.
- **Space**: \( O(H) \), where \( H \) is the height of the tree. This is the space required for the recursion stack.

### Approach 2: Iterative BFS (Breadth-First Search)
In this approach, we use a queue to traverse the tree level by level. We increment the depth at each level until we finish traversing all levels.

#### Algorithm:
1. Use a queue to keep track of nodes at each level.
2. For each level, process all the nodes at that level and add their children to the queue.
3. Continue this process until the queue is empty, and return the number of levels traversed.

#### Code:
```python
from collections import deque

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth
```

#### Time Complexity:
- **Time**: \( O(N) \), where \( N \) is the number of nodes in the tree.
- **Space**: \( O(N) \) in the worst case where the queue holds all the nodes of the last level.

---

## Comparison of Approaches

| Approach              | Time Complexity | Space Complexity | Description |
|-----------------------|-----------------|------------------|-------------|
| **Recursive DFS**      | \( O(N) \)      | \( O(H) \)       | Simpler and concise, uses recursion. Best for smaller trees. |
| **Iterative BFS**      | \( O(N) \)      | \( O(N) \)       | Uses queue to traverse level by level. Avoids recursion depth issues in large trees. |

---

## Test Function

Here’s a test function for the **Maximum Depth of Binary Tree** problem:

```python
def test_max_depth(func):
    print(f"Testing function: {func.__name__}")

    test_cases = [
        # Case 1: General tree with multiple levels
        {
            "name": "General Case with Multiple Levels",
            "input": TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            "expected": 3,
        },
        # Case 2: Tree with only one node
        {
            "name": "Single Node Tree",
            "input": TreeNode(1),
            "expected": 1,
        },
        # Case 3: Empty tree
        {
            "name": "Empty Tree",
            "input": None,
            "expected": 0,
        },
        # Case 4: Right-skewed tree
        {
            "name": "Right-Skewed Tree",
            "input": TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
            "expected": 3,
        },
        # Case 5: Left-skewed tree
        {
            "name": "Left-Skewed Tree",
            "input": TreeNode(1, TreeNode(2, TreeNode(3))),
            "expected": 3,
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert result == expected_output, f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")

# Run the test function
test_max_depth(maxDepth)
```




## Minimum Depth of Binary Tree

[LeetCode #111](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

## 111. Minimum Depth of Binary Tree


## Description

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note**: A leaf is a node with no children.

## Examples

### Example 1:

**Input**:
```plaintext
root = [3,9,20,null,null,15,7]
```

**Output**:
```plaintext
2
```

**Explanation**: The minimum depth is 2, with the path: 3 -> 20 -> 7.

### Example 2:

**Input**:
```plaintext
root = [2,null,3,null,4,null,5,null,6]
```

**Output**:
```plaintext
5
```

**Explanation**: The minimum depth is 5, with the path: 2 -> 3 -> 4 -> 5 -> 6.

## Constraints

- The number of nodes in the tree is in the range `[0, 10^5]`.
- `-1000 <= Node.val <= 1000`

---

## Solutions

### **Approach 1: Recursive DFS (Depth-First Search)**

In this approach, we perform a depth-first traversal of the tree. For each node, we compute the depth of the left and right subtrees recursively. The minimum depth is the smallest of the two, unless one of them is `null`, in which case the other subtree defines the depth.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    # If there is no left subtree, recurse through right subtree
    if not root.left:
        return minDepth(root.right) + 1
    
    # If there is no right subtree, recurse through left subtree
    if not root.right:
        return minDepth(root.left) + 1

    # Recursively calculate the depth of both left and right subtrees
    return min(minDepth(root.left), minDepth(root.right)) + 1
```

### **Time Complexity**:  
\( O(n) \), where \( n \) is the number of nodes in the tree. Every node is visited once.

### **Space Complexity**:  
\( O(h) \), where \( h \) is the height of the tree (due to recursion stack).

---

### **Approach 2: BFS (Breadth-First Search)**

A more optimal approach to find the minimum depth is to use BFS. We traverse level by level, and the first time we encounter a leaf node, we return the current depth because BFS ensures we visit nodes level-wise.

```python
from collections import deque

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    queue = deque([(root, 1)])  # Start with root at depth 1
    
    while queue:
        node, depth = queue.popleft()
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            return depth
        
        # Add the left and right children to the queue with incremented depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
```

### **Time Complexity**:  
\( O(n) \), where \( n \) is the number of nodes in the tree. Every node is visited once in a level-wise manner.

### **Space Complexity**:  
\( O(n) \), where \( n \) is the number of nodes in the queue at the widest level (in the worst case, half the tree’s nodes could be in the queue).

---

### **Approach 3: Iterative DFS Using a Stack**

This approach uses a stack to simulate the recursive depth-first search process iteratively. We push the root node and its depth into the stack, and we keep processing nodes until we reach a leaf node, at which point we return the minimum depth.

```python
def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    stack = [(root, 1)]  # Start with the root node at depth 1
    min_depth = float('inf')
    
    while stack:
        node, depth = stack.pop()
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            min_depth = min(min_depth, depth)
        
        # Push the left and right children into the stack with incremented depth
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
    
    return min_depth
```

### **Time Complexity**:  
\( O(n) \), where \( n \) is the number of nodes in the tree. Every node is visited once.

### **Space Complexity**:  
\( O(h) \), where \( h \) is the height of the tree (due to stack space).

---

### Summary of Approaches:

| **Approach**          | **Time Complexity** | **Space Complexity** | **Details**                                                        |
|-----------------------|---------------------|----------------------|--------------------------------------------------------------------|
| **Recursive DFS**      | \( O(n) \)          | \( O(h) \)           | Elegant but uses recursive stack memory.                           |
| **BFS (Level Order)**  | \( O(n) \)          | \( O(n) \)           | Best approach for finding the minimum depth, especially for large trees. |
| **Iterative DFS**      | \( O(n) \)          | \( O(h) \)           | Iterative, avoids recursion, but uses a stack.                     |

---

### Tests

```python
def test_min_depth(func):
    print(f"Testing function: {func.__name__}")

    test_cases = [
        # Example 1: Simple case with min depth 2
        {
            "name": "Simple case",
            "input": TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            "expected": 2,
        },
        # Example 2: Right-skewed tree with min depth 5
        {
            "name": "Right-skewed tree",
            "input": TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))),
            "expected": 5,
        },
        # Example 3: Empty tree
        {
            "name": "Empty tree",
            "input": None,
            "expected": 0,
        },
        # Example 4: Single node tree
        {
            "name": "Single node tree",
            "input": TreeNode(1),
            "expected": 1,
        },
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert result == expected_output, f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")
```

You can implement the test function to verify all your approaches.





to be continued:

```python
from collections import deque
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val:int=0, left:'Optional[TreeNode]'=None, right:'Optional[TreeNode]'=None):
        self.val = val          # Value of the node
        self.left = left      # Pointer to the left child
        self.right = right    # Pointer to the right child


def test_min_depth(func):
    print(f"Testing function: {func.__name__}")

    test_cases = [
        # # Example 1: Simple case with min depth 2
        # {
        #     "name": "Simple case",
        #     "input": TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        #     "expected": 2,
        # },
        # Example 2: Right-skewed tree with min depth 5
        {
            "name": "Right-skewed tree",
            "input": TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))),
            "expected": 5,
        },
        # # Example 3: Empty tree
        # {
        #     "name": "Empty tree",
        #     "input": None,
        #     "expected": 0,
        # },
        # # Example 4: Single node tree
        # {
        #     "name": "Single node tree",
        #     "input": TreeNode(1),
        #     "expected": 1,
        # },
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert result == expected_output, f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")



def min_depth(root:Optional[TreeNode])->int:
    if(not root):
        return 0

    min_depth = 10**9
    queue: deque[Tuple[Optional[TreeNode], int]] = deque([(root, 1)])


    while(queue):
        print('!Q ', [(x[0].val if x[0] is not None else None) for x in queue])
        (current, current_depth) = queue.popleft()

        print(current.val if current else None, current_depth)

        if(not current):
            # not consider last null
            original_depth = current_depth - 1
            if(original_depth < min_depth):
                min_depth = original_depth
        else:
            queue.append((current.left, current_depth +1 ))
            queue.append((current.right, current_depth +1) )


    return min_depth


test_min_depth(min_depth)

```






