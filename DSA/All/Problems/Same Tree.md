

[LeetCode #100: Same Tree](https://leetcode.com/problems/same-tree/)

## Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same values.

## Examples

### Example 1

**Input:**
```plaintext
p = [1,2,3], q = [1,2,3]
```
**Output:**
```plaintext
true
```

### Example 2

**Input:**
```plaintext
p = [1,2], q = [1,null,2]
```
**Output:**
```plaintext
false
```

### Example 3

**Input:**
```plaintext
p = [1,2,1], q = [1,1,2]
```
**Output:**
```plaintext
false
```

## Constraints
- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

---

## Solutions

### Approach 1: Recursive DFS

A recursive depth-first search (DFS) is a simple approach to solve this problem. The base cases for recursion are when one or both nodes are `None`. If both are `None`, they are considered the same; otherwise, they are not.

If both nodes are present, we compare their values. If the values are the same, we proceed to recursively check the left and right subtrees.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Base cases
    if not p and not q:
        return True  # Both are None
    if not p or not q:
        return False  # One is None and the other isn't
    
    # Compare current node values and recurse for left and right children
    return (p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

### Time Complexity
- **O(n)** where `n` is the number of nodes in the trees. We visit every node once.

### Space Complexity
- **O(h)** where `h` is the height of the tree due to recursion. The worst case is `O(n)` for a completely unbalanced tree.

---

### Approach 2: Iterative DFS (Using Stack)

In the iterative version, we simulate the recursion using a stack (or explicit DFS). We traverse the trees iteratively by pushing pairs of nodes from both trees onto the stack. We compare the node values and push their children in pairs (left, right).

```python
from collections import deque

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    stack = deque([(p, q)])

    while stack:
        node1, node2 = stack.pop()

        if not node1 and not node2:
            continue  # Both are None, continue with next pair
        if not node1 or not node2:
            return False  # One is None, the other isn't
        if node1.val != node2.val:
            return False  # Values don't match
        
        # Push children in pairs (left, right)
        stack.append((node1.left, node2.left))
        stack.append((node1.right, node2.right))
    
    return True  # All nodes matched
```

### Time Complexity
- **O(n)** where `n` is the number of nodes in the trees. We visit every node once.

### Space Complexity
- **O(h)** where `h` is the height of the tree, due to the stack. The worst case is `O(n)` for a completely unbalanced tree.

---

### Approach 3: Iterative BFS (Using Queue)

Instead of using a stack (DFS), we can use a queue (BFS) to traverse both trees level by level, comparing nodes at each level.

```python
from collections import deque

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue = deque([(p, q)])

    while queue:
        node1, node2 = queue.popleft()

        if not node1 and not node2:
            continue  # Both are None, continue with next pair
        if not node1 or not node2:
            return False  # One is None, the other isn't
        if node1.val != node2.val:
            return False  # Values don't match

        # Enqueue children in pairs (left, right)
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))

    return True  # All nodes matched
```

### Time Complexity
- **O(n)** where `n` is the number of nodes in the trees. We visit every node once.

### Space Complexity
- **O(h)** where `h` is the height of the tree due to the queue. The worst case is `O(n)` for a completely unbalanced tree.

---

## Summary of Approaches

| Approach             | Time Complexity | Space Complexity |
|----------------------|-----------------|------------------|
| **Recursive DFS**     | O(n)            | O(h)             |
| **Iterative DFS**     | O(n)            | O(h)             |
| **Iterative BFS**     | O(n)            | O(h)             |

---

## Test Cases

```python

from typing import Optional, List


class TreeNode:
    def __init__(self, val:int=0, left:'Optional[TreeNode]'=None, right:'Optional[TreeNode]'=None):
        self.val = val          # Value of the node
        self.left = left      # Pointer to the left child
        self.right = right    # Pointer to the right child



def test_isSameTree(func):
    # Helper function to create trees from list
    def create_tree(lst: List[Optional[int]]):
        if not lst:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in lst]
        for i in range(len(lst)):
            if nodes[i]:
                if 2*i+1 < len(lst):
                    nodes[i].left = nodes[2*i+1]
                if 2*i+2 < len(lst):
                    nodes[i].right = nodes[2*i+2]
        return nodes[0]

    test_cases = [
        # Case 1: Identical trees
        {
            "name": "Identical Trees",
            "p": create_tree([1, 2, 3]),
            "q": create_tree([1, 2, 3]),
            "expected": True,
        },
        # Case 2: Trees with different structure
        {
            "name": "Different Structure",
            "p": create_tree([1, 2]),
            "q": create_tree([1, None, 2]),
            "expected": False,
        },
        # Case 3: Trees with different values
        {
            "name": "Different Values",
            "p": create_tree([1, 2, 1]),
            "q": create_tree([1, 1, 2]),
            "expected": False,
        },
        # Case 4: Both trees are empty
        {
            "name": "Both Empty",
            "p": None,
            "q": None,
            "expected": True,
        },
        # Case 5: One tree is empty
        {
            "name": "One Empty",
            "p": create_tree([1]),
            "q": None,
            "expected": False,
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = func(test_case['p'], test_case['q'])
        assert result == test_case['expected'], f"Test case {i} ({test_case['name']}) failed: expected {test_case['expected']}, got {result}"

    print("All test cases passed!")



```



// to be continued!


```python

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val:int=0, left:'Optional[TreeNode]'=None, right:'Optional[TreeNode]'=None):
        self.val = val
        self.left = left
        self.right = right



def test_isSameTree(func):
    # Helper function to create trees from list
    def create_tree(lst: List[Optional[int]]):
        if not lst:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in lst]
        for i in range(len(lst)):
            if nodes[i]:
                if 2*i+1 < len(lst):
                    nodes[i].left = nodes[2*i+1]
                if 2*i+2 < len(lst):
                    nodes[i].right = nodes[2*i+2]
        return nodes[0]

    test_cases = [
        # Case 1: Identical trees
        {
            "name": "Identical Trees",
            "p": create_tree([1, 2, 3]),
            "q": create_tree([1, 2, 3]),
            "expected": True,
        },
        # Case 2: Trees with different structure
        {
            "name": "Different Structure",
            "p": create_tree([1, 2]),
            "q": create_tree([1, None, 2]),
            "expected": False,
        },
        # Case 3: Trees with different values
        {
            "name": "Different Values",
            "p": create_tree([1, 2, 1]),
            "q": create_tree([1, 1, 2]),
            "expected": False,
        },
        # Case 4: Both trees are empty
        {
            "name": "Both Empty",
            "p": None,
            "q": None,
            "expected": True,
        },
        # Case 5: One tree is empty
        {
            "name": "One Empty",
            "p": create_tree([1]),
            "q": None,
            "expected": False,
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = func(test_case['p'], test_case['q'])
        assert result == test_case['expected'], f"Test case {i} ({test_case['name']}) failed: expected {test_case['expected']}, got {result}"

    print("All test cases passed!")



def is_same_tree(tree1_root:Optional[TreeNode], tree2_root:Optional[TreeNode]):

    if(tree1_root != tree2_root and tree1_root.val != tree2_root.val):
        print('if', tree1_root.val, tree2_root.val, )
        return False

    queue1 = deque([tree1_root])
    queue2 = deque([tree2_root])

    while(queue1):
        one = queue1.popleft()
        two = queue2.popleft()

        if(
            (one.left != two.left and one.left.val != two.left.val)
            or (one.right != two.right and  one.right.val != two.right.val)
        ):
            return False

        if(one.left):
            queue1.append(one.left)
            queue2.append(two.left)

        if(one.right):
            queue1.append(one.right)
            queue2.append(two.right)

    return True


test_isSameTree(is_same_tree)


```
