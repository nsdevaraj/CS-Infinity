



[How to solve (almost) any binary tree coding problem](https://youtu.be/s2Yyk3qdy3o?si=n1G_czJa_4J4T3Pk)





Binary Tree:
 * non linear data structure, so not easy like liner datastructure like array or linkedList
 * fact - subtree of nodes are also considered as tree, so by recursion we can solve easily


```python
from typing import Optional

class TreeNode:
    def __init__(self, value: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.value = value
        self.left = left
        self.right = right

# 1. Sum of Tree Elements
def sum_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

# 2. Finding the Maximum Value
def max_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return float('-inf')  # Return negative infinity for empty nodes
    return max(root.value, max_tree(root.left), max_tree(root.right))

# 3. Calculating the Height of the Tree
def height_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(height_tree(root.left), height_tree(root.right))

# 4. Reversing (Inverting) the Tree
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# 5. Checking if a Value Exists in the Tree
def exists_in_tree(root: Optional[TreeNode], value: int) -> bool:
    if root is None:
        return False
    if root.value == value:
        return True
    return exists_in_tree(root.left, value) or exists_in_tree(root.right, value)

```



### The Trick: Treat Subtrees as Trees

One of the most useful properties of binary trees is that each subtree of a node is, by definition, a binary tree. This simple observation allows us to use the same function on both the left and right subtrees of any node, meaning we can solve many problems recursively. Here’s a classic example: calculating the sum of all elements in a binary tree.

To calculate the sum of elements in a binary tree, we need to:

1. Add the value of the root node.
2. Add the sum of the elements in the left subtree.
3. Add the sum of the elements in the right subtree.

But here’s where recursion comes in. To compute the sum of the elements in the left or right subtree, we can use the same function that we use for the entire tree. This continues recursively until we reach a null node, which is our base case. At this point, the recursion starts to unwind, and the results propagate back up the tree to give us the total sum.

### Breaking It Down

This recursive process can be expressed in just a few lines of code. The function needs to handle two main cases:

1. **Base Case:** If the root is null, we return 0.
2. **Recursive Case:** For any other node, we return the sum of the root’s value, the sum of the left subtree, and the sum of the right subtree.

Here’s a simplified version of the code for calculating the sum of elements in a binary tree:

```python
def sum_tree(root):
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)
```

### A Generalized Process for Binary Tree Problems

The beauty of this recursive approach is that it can be generalized to solve many binary tree problems by following these four steps:

1. **Identify the Base Case:** Find the condition where the recursion should stop, typically when the node is `null`.
2. **Recur on the Left Subtree:** Apply the same function to the left child.
3. **Recur on the Right Subtree:** Apply the function to the right child.
4. **Combine the Results:** Merge the results from the left and right subtrees, often by adding, comparing, or swapping.

Let’s apply this process to a few more problems:

- **Finding the Maximum Value in a Binary Tree:**
  To find the maximum value, recursively get the maximum of the left subtree, the maximum of the right subtree, and compare them with the root node’s value.

  ```python
  def max_tree(root):
      if root is None:
          return float('-inf')  # Use negative infinity as a placeholder for null nodes
      return max(root.value, max_tree(root.left), max_tree(root.right))
  ```

- **Calculating the Height of a Binary Tree:**
  To find the height, recursively calculate the height of both subtrees and return 1 plus the maximum of the two heights.

  ```python
  def height_tree(root):
      if root is None:
          return 0
      return 1 + max(height_tree(root.left), height_tree(root.right))
  ```

- **Checking if a Value Exists in the Tree:**
  To check if a value exists, recursively check the root, then check if the value exists in either the left or right subtree.

  ```python
  def search_tree(root, target):
      if root is None:
          return False
      if root.value == target:
          return True
      return search_tree(root.left, target) or search_tree(root.right, target)
  ```

- **Reversing a Binary Tree (Inverting it):**
  To reverse (or invert) a binary tree, recursively swap the left and right subtrees for every node.

  ```python
  def invert_tree(root):
      if root is None:
          return None
      root.left, root.right = invert_tree(root.right), invert_tree(root.left)
      return root
  ```

### The Recursion Mindset

The key takeaway is that recursion is a powerful tool for binary tree problems. By breaking the problem into smaller subproblems (i.e., left and right subtrees), you can build up the solution incrementally. This recursive pattern—dealing with subtrees, applying the same logic, and merging results—can solve a wide range of binary tree problems.

Whenever you face a binary tree coding challenge, try thinking in terms of recursion. Consider the base case, how you can divide the problem into subproblems, and how to combine the results. While this approach may not solve every problem, it will be effective in a majority of cases.

By mastering this recursive trick, you'll find that solving binary tree problems becomes much more intuitive and manageable!


- **Binary Tree Complexity for Beginners**  
  - Binary trees are non-linear data structures, unlike arrays or linked lists.
  - Traversing a binary tree is different from linear structures, requiring new strategies.

- **Key Insight: Treat Subtrees as Trees**  
  - Each subtree in a binary tree is also a binary tree.
  - This allows you to apply the same function recursively on subtrees.
  
- **Example: Calculating the Sum of Elements in a Binary Tree**  
  - To calculate the sum of elements:
    - Add the root's value.
    - Add the sum of the left subtree.
    - Add the sum of the right subtree.
  - The same function is applied recursively to the subtrees until a `null` node is reached (base case).
  - When the recursion unwinds, the total sum is calculated as the results propagate back to the root.

- **Steps for Recursion**  
  1. **Base Case:** Identify when recursion should stop, usually at `null`.
  2. **Recur on Left Subtree:** Call the function on the left child.
  3. **Recur on Right Subtree:** Call the function on the right child.
  4. **Combine Results:** Merge results from the left and right subtrees.

- **Code Example: Sum of Tree Elements**
  ```python
  def sum_tree(root):
      if root is None:
          return 0
      return root.value + sum_tree(root.left) + sum_tree(root.right)
  ```

- **General Approach to Binary Tree Problems**  
  - **Finding the Maximum Value:**  
    - Recursively find the maximum in the left and right subtrees.
    - Compare them with the root’s value.
    ```python
    def max_tree(root):
        if root is None:
            return float('-inf')
        return max(root.value, max_tree(root.left), max_tree(root.right))
    ```

  - **Calculating the Height of the Tree:**  
    - Recursively compute the height of both subtrees.
    - Return 1 plus the maximum height.
    ```python
    def height_tree(root):
        if root is None:
            return 0
        return 1 + max(height_tree(root.left), height_tree(root.right))
    ```

  - **Checking if a Value Exists in the Tree:**  
    - Check the root’s value.
    - Recursively check both subtrees for the target value.
    ```python
    def search_tree(root, target):
        if root is None:
            return False
        if root.value == target:
            return True
        return search_tree(root.left, target) or search_tree(root.right)
    ```

  - **Reversing (Inverting) a Binary Tree:**  
    - Recursively reverse the left and right subtrees.
    - Swap the left and right nodes at each step.
    ```python
    def invert_tree(root):
        if root is None:
            return None
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root
    ```

- **The Power of Recursion**  
  - Recursion simplifies solving many binary tree problems.
  - It works by breaking problems into smaller subproblems, working on subtrees.
  - Common pattern: base case, recursive calls on subtrees, combine results.





to check. {

```python 

from typing import Optional, List

class TreeNode:
    def __init__(self, value: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.value = value
        self.left = left
        self.right = right

# Helper function to build a binary tree from a list (level-order)
def build_tree_from_list(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]
    return nodes[0]


# 1. Sum of Tree Elements
def sum_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

# 2. Finding the Maximum Value
def max_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return float('-inf')  # Return negative infinity for empty nodes
    return max(root.value, max_tree(root.left), max_tree(root.right))

# 3. Calculating the Height of the Tree
def height_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(height_tree(root.left), height_tree(root.right))

# 4. Reversing (Inverting) the Tree
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# 5. Checking if a Value Exists in the Tree
def exists_in_tree(root: Optional[TreeNode], value: int) -> bool:
    if root is None:
        return False
    if root.value == value:
        return True
    return exists_in_tree(root.left, value) or exists_in_tree(root.right, value)




# Helper function to convert binary tree to list (level-order traversal)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Trim the trailing Nones for a cleaner list
    while result and result[-1] is None:
        result.pop()

    return result


def run_test_for_tree_cases():
    print("Running binary tree test cases...\n")

    test_cases = [
        {
            "name": "Basic Tree",
            "root": [1, 2, 3],
            "expected_sum": 6,  # 1 + 2 + 3
            "expected_max": 3,
            "expected_height": 2,
            "expected_inverted": [1, 3, 2],  # Tree inverted
        },
        {
            "name": "Tree with Nulls",
            "root": [1, None, 2, None, None, 3],
            "expected_sum": 6,  # 1 + 2 + 3
            "expected_max": 3,
            "expected_height": 3,
            "expected_inverted": [1, 2, None, 3],  # Inverted
        },
        {
            "name": "Negative Values Tree",
            "root": [-5, 4, -3],
            "expected_sum": -4,  # -5 + 4 + (-3)
            "expected_max": 4,
            "expected_height": 2,
            "expected_inverted": [-5, -3, 4],  # Tree inverted
        },
        {
            "name": "Empty Tree",
            "root": [],
            "expected_sum": 0,
            "expected_max": float('-inf'),
            "expected_height": 0,
            "expected_inverted": [],  # No tree to invert
        },
        {
            "name": "Balanced Tree",
            "root": [4, 2, 6, 1, 3, 5, 7],
            "expected_sum": 28,  # 4 + 2 + 6 + 1 + 3 + 5 + 7
            "expected_max": 7,
            "expected_height": 3,
            "expected_inverted": [4, 6, 2, 7, 5, 3, 1],  # Inverted
        },
        {
            "name": "Single Node Tree",
            "root": [10],
            "expected_sum": 10,  # 10
            "expected_max": 10,
            "expected_height": 1,
            "expected_inverted": [10],  # No change
        },
        {
            "name": "Right-Skewed Tree",
            "root": [1, None, 2, None, 3],
            "expected_sum": 6,  # 1 + 2 + 3
            "expected_max": 3,
            "expected_height": 3,
            "expected_inverted": [1, 2, None, 3],  # Inverted
        },
        {
            "name": "Left-Skewed Tree",
            "root": [1, 2, None, 3],
            "expected_sum": 6,  # 1 + 2 + 3
            "expected_max": 3,
            "expected_height": 3,
            "expected_inverted": [1, None, 2, None, 3],  # Inverted
        },
        {
            "name": "Complex Tree",
            "root": [5, 3, 8, 2, 4, 7, 9],
            "expected_sum": 38,  # 5 + 3 + 8 + 2 + 4 + 7 + 9
            "expected_max": 9,
            "expected_height": 3,
            "expected_inverted": [5, 8, 3, 9, 7, 4, 2],  # Inverted
        },
        {
            "name": "Tree with Duplicate Values",
            "root": [1, 1, 1],
            "expected_sum": 3,  # 1 + 1 + 1
            "expected_max": 1,
            "expected_height": 2,
            "expected_inverted": [1, 1, 1],  # No change
        },
        {
            "name": "Wide Tree",
            "root": [1, 2, 3, 4, 5],
            "expected_sum": 15,  # 1 + 2 + 3 + 4 + 5
            "expected_max": 5,
            "expected_height": 3,
            "expected_inverted": [1, 3, 2, 5, 4],  # Inverted
        },
        {
            "name": "Tree with Negative and Positive Values",
            "root": [0, -1, 1, -2, 2],
            "expected_sum": 0,  # 0 + (-1) + 1 + (-2) + 2
            "expected_max": 2,
            "expected_height": 3,
            "expected_inverted": [0, 1, -1, 2, -2],  # Inverted
        },
    ]


    for case in test_cases:
        root = build_tree_from_list(case["root"])

        # Run each function
        tree_sum = sum_tree(root)
        max_value = max_tree(root)
        height = height_tree(root)
        inverted_root = invert_tree(build_tree_from_list(case["root"]))  # Build the tree again for invert test

        inverted_list = tree_to_list(inverted_root)  # Helper function to convert tree back to list for comparison

        # Assert and print results
        assert tree_sum == case["expected_sum"], f"Failed {case['name']} on sum_tree"
        assert max_value == case["expected_max"], f"Failed {case['name']} on max_tree"
        assert height == case["expected_height"], f"Failed {case['name']} on height_tree"
        assert inverted_list == case["expected_inverted"], f"Failed {case['name']} on invert_tree"

        print(f"Test case '{case['name']}' passed!")

    print("\nAll test cases completed!")

```

}
