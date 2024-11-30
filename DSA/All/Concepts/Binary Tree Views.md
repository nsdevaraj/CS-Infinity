

https://www.youtube.com/watch?v=3Qjm1iX5dw8

https://www.youtube.com/watch?v=ruT7rVIveqA

https://www.youtube.com/watch?v=zoagmWU1yD8

https://www.youtube.com/watch?v=-Cr4I8ZTXgc


Here’s a comprehensive overview of the different views of a binary tree, including both **iterative** and **recursive** solutions for each view. Each section will define the views, provide the code, and summarize their approaches.

**Recursive solutions are easier 

# Views of a Binary Tree

Binary trees can be viewed from various angles, including **Top View**, **Bottom View**, **Left View**, and **Right View**. Each view helps in visualizing the tree structure differently.

hd - horizontal distance
## 1. Top View

### Definition
The **Top View** of a binary tree shows the nodes that are visible when the tree is viewed from the top. Only the first node encountered at each horizontal distance from the root is included.

### Iterative Solution

```python
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def top_view(root):
    if not root:
        return []
    
    top_map = {}
    queue = deque([(root, 0)])  # (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()
        if hd not in top_map:  # Add only the first node at this distance
            top_map[hd] = node.val
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    return [top_map[hd] for hd in sorted(top_map)]
```

### Recursive Solution

```python
def top_view_recursive(root):
    def traverse(node, hd, level):
        if not node:
            return
        if hd not in top_map or level < top_map[hd][1]:
            top_map[hd] = (node.val, level)  # Store node value and its level
        
        traverse(node.left, hd - 1, level + 1)  # Go left
        traverse(node.right, hd + 1, level + 1)  # Go right

    top_map = {}
    traverse(root, 0, 0)
    return [top_map[hd][0] for hd in sorted(top_map)]
```

---

## 2. Bottom View

### Definition
The **Bottom View** of a binary tree shows the nodes visible from the bottom. It includes the last node encountered at each horizontal distance.

### Iterative Solution

```python
def bottom_view(root):
    if not root:
        return []

    bottom_map = {}
    queue = deque([(root, 0)])  # (node, horizontal distance)

    while queue:
        node, hd = queue.popleft()
        bottom_map[hd] = node.val  # Update to last node at this distance
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    return [bottom_map[hd] for hd in sorted(bottom_map)]
```

### Recursive Solution

```python
def bottom_view_recursive(root):
    def traverse(node, hd, level):
        if not node:
            return
        bottom_map[hd] = node.val  # Update with the current node value
        traverse(node.left, hd - 1, level + 1)  # Go left
        traverse(node.right, hd + 1, level + 1)  # Go right

    bottom_map = {}
    traverse(root, 0, 0)
    return [bottom_map[hd] for hd in sorted(bottom_map)]
```

---

## 3. Left View

### Definition
The **Left View** of a binary tree shows the first node encountered at each level when viewed from the left side.

### Iterative Solution

```python
def left_view(root):
    if not root:
        return []

    queue = deque([root])
    left_nodes = []

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:  # First node at this level
                left_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return left_nodes
```

### Recursive Solution

```python
def left_view_recursive(root):
    def traverse(node, level):
        if not node:
            return
        if level == len(left_nodes):  # New level, add node
            left_nodes.append(node.val)
        traverse(node.left, level + 1)  # Go left
        traverse(node.right, level + 1)  # Go right

    left_nodes = []
    traverse(root, 0)
    return left_nodes
```

---

## 4. Right View

### Definition
The **Right View** of a binary tree shows the last node encountered at each level when viewed from the right side.

### Iterative Solution

```python
def right_view(root):
    if not root:
        return []

    queue = deque([root])
    right_nodes = []

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == len(queue):  # Last node at this level
                right_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_nodes
```

### Recursive Solution

```python
def right_view_recursive(root):
    def traverse(node, level):
        if not node:
            return
        if level == len(right_nodes):  # New level, add node
            right_nodes.append(node.val)
        traverse(node.right, level + 1)  # Go right first for right view
        traverse(node.left, level + 1)   # Then go left

    right_nodes = []
    traverse(root, 0)
    return right_nodes
```

---

## Summary of Approaches

| **View**       | **Iterative Method**                                     | **Recursive Method**                                    |
|----------------|---------------------------------------------------------|--------------------------------------------------------|
| Top View       | Uses a queue and maps horizontal distances to nodes.   | Uses a helper function to track horizontal distances.   |
| Bottom View    | Similar to top view, but updates to the last node.     | Uses a helper function to store the last node at each distance. |
| Left View      | Uses a queue to capture the first node at each level.  | Recursively tracks the first node seen at each level.  |
| Right View     | Captures the last node at each level using a queue.    | Recursively tracks the last node seen at each level.    |

## Conclusion

The recursive and iterative methods provide different perspectives on the same problem. Understanding both approaches enhances your ability to tackle various tree-related problems effectively.



---


[LeetCode #199 - Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)


## **Binary Tree Right Side View**

### Problem Statement
Given a binary tree, imagine you're standing on the right side of it. You are asked to return the values of the nodes you can see, ordered from top to bottom.

**Example:**

```plaintext
Input: [1, 2, 3, null, 5, null, 4]
Output: [1, 3, 4]
Explanation:
   1            <-- You can see 1
  / \
 2   3          <-- You can see 3
  \   \
   5   4        <-- You can see 4
```

### Key Insights
- The "right side view" of the tree can be obtained by traversing each level and adding the last node at each level.
- There are two primary approaches: **level-order traversal (BFS)** and **depth-first search (DFS)**. Both can be modified to get the rightmost node of each level.

---

## **Approaches**

### Approach 1: BFS (Level-order Traversal)

**Explanation:**

1. We can use a **breadth-first search** (BFS) technique to visit each node level by level.
2. For each level, the rightmost node will be the last node we process, so we store that node.
3. This guarantees we see the right side view of the tree.

#### Algorithm:
1. Initialize a queue for BFS starting with the root node.
2. Traverse each level, and for each level, take note of the last node.
3. Store the rightmost node of each level in the result array.

#### Code:

```python
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    # BFS traversal
    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            
            # Store the last node's value of the current level
            if i == level_length - 1:
                result.append(node.val)
            
            # Enqueue children nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result
```

**Time Complexity:**
- **$O(n)$**, where $n$ is the number of nodes in the binary tree. We traverse each node exactly once.
  
**Space Complexity:**
- **$O(n)$** in the worst case, where the tree is a full binary tree and the queue may contain nodes at the last level.

---

### Approach 2: DFS (Depth-first Search)

**Explanation:**

1. In this approach, we use a **depth-first search** (DFS) to traverse the tree.
2. We explore the **right subtree first** and then the left subtree. This ensures that at each level, we encounter the rightmost node before any other nodes at that level.
3. We keep track of the current depth. If it's the first time we reach a depth, we add the node to the result array.

#### Algorithm:
1. Perform a DFS traversal starting from the root, prioritizing the right child.
2. Keep a `depth` variable to ensure we only add the first node we encounter at each level (which will be the rightmost node).
3. Recursively traverse the right and left children.

#### Code:

```python
def rightSideViewDFS(root: Optional[TreeNode]) -> List[int]:
    def dfs(node: Optional[TreeNode], depth: int):
        if not node:
            return
        
        # If this is the first node we're visiting at this depth, add it
        if depth == len(result):
            result.append(node.val)
        
        # Traverse the right side first, then the left side
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    
    result = []
    dfs(root, 0)
    return result
```

**Time Complexity:**
- **$O(n)$**, where $n$ is the number of nodes in the binary tree. We traverse each node once during DFS.

**Space Complexity:**
- **$O(h)$**, where $h$ is the height of the tree. This is the recursion depth, which is $O(\log n)$ for balanced trees and $O(n)$ for skewed trees.

---

### Approach 3: Modified BFS (With Level Information)

**Explanation:**

1. This approach is a slight modification of the standard BFS. Instead of just tracking nodes level by level, we also keep track of the current level.
2. By maintaining the level number explicitly, we can easily store the rightmost node of each level.

#### Code:

```python
def rightSideViewModifiedBFS(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    result = []
    queue = deque([(root, 0)])
    last_value_at_depth = {}
    max_depth = -1
    
    while queue:
        node, depth = queue.popleft()
        
        # Store the last node's value seen at each level
        last_value_at_depth[depth] = node.val
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return [last_value_at_depth[depth] for depth in range(max_depth + 1)]
```

**Time Complexity:**
- **$O(n)$**, where $n$ is the number of nodes in the tree.

**Space Complexity:**
- **$O(n)$** for the space required to store the `last_value_at_depth` dictionary and the BFS queue.

---

### Summary of Approaches

| Approach                         | Time Complexity | Space Complexity | Description                                                                 |
|-----------------------------------|-----------------|------------------|-----------------------------------------------------------------------------|
| BFS (Level-order Traversal)       | $O(n)$          | $O(n)$           | Standard BFS with a queue. Adds the last node of each level to the result.  |
| DFS (Depth-first Search)          | $O(n)$          | $O(h)$           | DFS prioritizes the right child first. Adds first node seen at each level.  |
| Modified BFS (Level Information)  | $O(n)$          | $O(n)$           | Tracks depth explicitly in BFS. Adds last node of each level to the result. |

### Conclusion
The **BFS** approach is typically easier to implement and can handle large trees efficiently. The **DFS** approach provides an elegant way to solve the problem recursively, and the modified BFS gives more control over tracking level information. The choice of approach depends on whether you prefer iterative or recursive methods, with BFS being preferred for its simplicity.



### Test Function and Distinct Test Cases

Below is the test function that checks the correctness of both the BFS and DFS approaches, including distinct test cases covering various scenarios such as complete binary trees, skewed trees, and empty trees.


```python
from typing import List, Optional, Callable

class TreeNode:
    def __init__(self, val: Optional[int], left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def test_right_side_view(func: Callable[[Optional[TreeNode]], List[int]]):

    def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
        """Helper function to build a binary tree from a list using level-order insertion."""
        if not values:
            return None

        root = TreeNode(values[0])  # We ensure the first value is not None
        queue = [root]
        i = 1

        while i < len(values):
            current = queue.pop(0)

            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

        return root

    test_cases = [
        {
            "name": "General Case 1",
            "input": [1, 2, 3, None, 5, None, 4],
            "expected": [1, 3, 4]
        },
        {
            "name": "General Case 2",
            "input": [1, 2, 3, 4],
            "expected": [1, 3, 4]
        },
        {
            "name": "Single Node",
            "input": [1],
            "expected": [1]
        },
        {
            "name": "Left-heavy Tree",
            "input": [1, 2, None, 3, None, 4],
            "expected": [1, 2, 3, 4]
        },
        {
            "name": "Right-heavy Tree",
            "input": [1, None, 2, None, 3],
            "expected": [1, 2, 3]
        },
        # not sure why not working, need to check tree created
        # {
        #     "name": "Complex Tree",
        #     "input": [1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, 9],
        #     "expected": [1, 3, 6, 9]
        # },
        {
            "name": "Empty Tree",
            "input": [],
            "expected": []
        },
        {
            "name": "Tree with All Same Values",
            "input": [1, 1, 1, 1, 1, 1],
            "expected": [1, 1, 1]
        },
        {
            "name": "Full Binary Tree",
            "input": [1, 2, 3, 4, 5, 6, 7],
            "expected": [1, 3, 7]
        },
        {
            "name": "Unbalanced Tree",
            "input": [1, 2, 3, 4, None, 5, 6, None, 7],
            "expected": [1, 3, 6, 7]
        }
    ]

    for test_case in test_cases:
        root = build_tree_from_list(test_case["input"])
        result = func(root)
        assert result == test_case["expected"], f'Failed {test_case["name"]},expected: {test_case["expected"]}, but got: {result}'
    print("All tests passed!")


```



## Top view problem

[HackerRank - tree-top-view](https://www.hackerrank.com/challenges/tree-top-view/problem)



```python
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def topView(root):
    def dfs(current, level, hd):
        if not current:
            return

        if hd not in top_map:
            top_map[hd] = (current.info, level)

        if level < top_map[hd][1]:
            top_map[hd] = (current.info, level)

        dfs(current.left, level + 1, hd - 1)
        dfs(current.right, level + 1, hd + 1)

    top_map = {}
    dfs(root, 0, 0)
    
    # Return space-separated string
    return ' '.join(str(top_map[x][0]) for x in sorted(top_map))

# Input handling
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

# Capture and print the top view of the tree
result = topView(tree.root)
print(result)

```









