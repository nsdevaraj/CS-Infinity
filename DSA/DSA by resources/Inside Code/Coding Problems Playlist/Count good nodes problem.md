

[Count good nodes problem (LeetCode #1448) - Inside code](https://youtu.be/3e3Sf8rMo34?si=_MB-7eZKGLoLIRUK)



### Problem: Count Good Nodes in Binary Tree (LeetCode #1448)

You are given the root of a binary tree, and your task is to count the number of **good nodes**.

A node **N** is considered a **good node** if, along the path from the root to **N**, **no other nodes** have a value **greater than** that of **N**.

#### Problem Statement

**Input**:  
- `root`: the root node of a binary tree.

**Output**:  
- Return the number of **good nodes** in the tree.

#### Example

```plaintext
Input:
    3
   / \
  1   4
 /   / \
3   1   5

Output: 4

Explanation:
- The good nodes are: 3 (root), 3 (left child of 1), 4 (right child of 3), and 5 (right child of 4).
```

### Solution with Time Complexity of O(nh)

In this solution, we follow the intuitive but **less efficient** approach. For each node, we will traverse back to the root to check if any node on the path is greater than the current node. This approach results in a time complexity of **O(nh)**, where **n** is the number of nodes and **h** is the height of the tree.

#### Approach

1. **Check Node**: For each node, we traverse all the way back to the root, checking if any node in the path has a value greater than the current node.
2. **Traverse the Tree**: This check is performed for every node in the tree, leading to a higher time complexity because of the repeated work done in each recursive call.

#### Code Implementation (Inefficient Approach)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def is_good_node(node: TreeNode, current: TreeNode) -> bool:
    """
    Check if the current node is a good node by comparing its value to all nodes on the path to the root.
    
    :param node: the current node in the tree
    :param current: the node we are checking if it is good
    :return: True if the current node is good, False otherwise
    """
    while node is not None:
        if node.val > current.val:
            return False  # If any node on the path has a value greater, it's not a good node
        node = node.parent  # Move upwards in the tree
    return True  # If no greater node found, it's a good node

def count_good_nodes(root: Optional[TreeNode]) -> int:
    """
    Count good nodes by traversing the tree and checking each node by looking at the path from the root.
    
    :param root: the root node of the tree
    :return: the number of good nodes
    """
    if root is None:
        return 0  # Base case: empty subtree

    good_node_count = 1 if is_good_node(root, root) else 0  # Check if root is good
    
    # Traverse the left and right subtrees and sum the number of good nodes
    if root.left is not None:
        good_node_count += count_good_nodes(root.left)
    if root.right is not None:
        good_node_count += count_good_nodes(root.right)
    
    return good_node_count
```

### Time Complexity Analysis

- **Time Complexity**: In this solution, for each node, we traverse the path back to the root (which takes **O(h)** where **h** is the height of the tree).
- Since we repeat this for each node, the total time complexity becomes **O(nh)**, where **n** is the total number of nodes and **h** is the height of the tree.

$$
\text{Time Complexity} = O(nh)
$$

#### Explanation:

- **n**: We visit each of the **n** nodes in the tree.
- **h**: For each node, we potentially traverse up to **h** nodes (the height of the tree) back to the root to check the path.

### Space Complexity Analysis

- **Space Complexity**: The space complexity is determined by the maximum depth of the recursion, which is **O(h)**, where **h** is the height of the tree.

$$
\text{Space Complexity} = O(h)
$$

#### Conclusion:
This solution is **inefficient** due to repeated traversal up to the root for each node, which leads to a time complexity of **O(nh)**. It can serve as a basic approach to understanding the problem but is not ideal for large trees.



### Approach: Recursive Depth-First Search (DFS)

We can solve this problem by recursively traversing the tree and keeping track of the **maximum value** encountered so far along the path. A node is **good** if its value is greater than or equal to this maximum.

#### Key Steps:
1. **Initialize**: Start from the root and initialize the maximum value encountered so far to negative infinity ($-\infty$).
2. **Check Node**: For each node, check if its value is greater than or equal to the current maximum. If true, it is a **good node**.
3. **Update Maximum**: Update the maximum value as you move down the tree.
4. **Recur**: Traverse both the left and right subtrees, passing the updated maximum value.

#### Code Implementation (with comments)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root: Optional[TreeNode], max_node: int = float('-inf')) -> int:
    """
    Count the number of good nodes in the binary tree.
    
    :param root: the root node of the binary tree
    :param max_node: the maximum value seen so far on the path from the root to the current node
    :return: the number of good nodes in the binary tree
    """
    if root is None:
        return 0  # Base case: empty subtree

    # Check if the current node is good
    is_good = root.val >= max_node

    # Update the maximum value for the next nodes in the path
    new_max = max(max_node, root.val)
    
    # Recursively count good nodes in the left and right subtrees
    left_count = good_nodes(root.left, new_max)
    right_count = good_nodes(root.right, new_max)
    
    # Return the total count: current node (1 if good), left subtree, and right subtree
    return int(is_good) + left_count + right_count
```

### Time and Space Complexity Analysis

#### Time Complexity:
- We traverse the entire tree once, visiting each node exactly once.
- Let **n** be the number of nodes in the tree.
- The time complexity is:

$$
\text{Time Complexity} = O(n)
$$

#### Space Complexity:
- The space complexity is determined by the maximum depth of the recursion, which corresponds to the height of the tree **h**.
- In the worst case (a skewed tree), the recursion depth could be **n** (the total number of nodes), while in the best case (a balanced tree), it would be **O(\log n)**.
- Therefore, the space complexity is:

$$
\text{Space Complexity} = O(h)
$$

where **h** is the height of the tree.

### Conclusion

This recursive approach efficiently solves the "Count Good Nodes" problem by traversing the tree once and maintaining the maximum value encountered on the path. By comparing each node's value to the maximum so far, we can determine if it's a good node in constant time.

### Key Insights:
- The problem can be solved in linear time **O(n)**, where **n** is the number of nodes.
- The space complexity depends on the height of the tree, making it **O(h)**.


