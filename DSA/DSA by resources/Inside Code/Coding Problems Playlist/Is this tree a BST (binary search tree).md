

[# Is this tree a BST (binary search tree)? - Inside code](https://youtu.be/uc2mxZLDRi4?si=ELZzWiDUepFK3VRQ)


### Problem Definition:
Given a binary tree, determine if it qualifies as a Binary Search Tree (BST):
- **BST Definition**: Every node's value is greater than all nodes in its left subtree and smaller than all nodes in its right subtree.
### Problem Example:
Consider the following binary tree:
```
    5
   / \
  2   8
     / \
    6   10
```
- **Explanation**:
  - For the root node `5`, its left subtree (nodes `2`) should be smaller and its right subtree (nodes `8`, `6`, `10`) should be greater.
  - Node `5` should be greater than all nodes in its left subtree (`2`), and smaller than all nodes in its right subtree (`8`, `6`, `10`).

### Solution Approaches:

1. **Recursive Range Check (Optimal Approach)**
   - **Approach Explanation**:
     - Use recursive traversal with parameters `minval` and `maxval` to enforce the BST property dynamically.
     - Ensure each node's value falls within its valid range (`minval` to `maxval`).
   - **Base Cases**:
     - Return `True` if the tree is empty (`root is None`).
     - Return `False` if the current node's value violates the BST property (`not minval < root.val < maxval`).
   - **Recursive Cases**:
     - Recursively check the left subtree, updating `maxval` to `root.val` (upper limit).
     - Recursively check the right subtree, updating `minval` to `root.val` (lower limit).

   ```python
   def is_bst(root, minval=float('-inf'), maxval=float('inf')):
       if root is None:
           return True
       elif not minval < root.val < maxval:
           return False
       else:
           return is_bst(root.left, minval, root.val) and is_bst(root.right, root.val, maxval)
   ```

   - **Time Complexity**: \( O(n) \) where \( n \) is the number of nodes (each node is visited once).
   - **Space Complexity**: \( O(h) \) due to recursive calls, where \( h \) is the height of the tree.

2. **Inorder Traversal with Array Check**
   - **Approach Explanation**:
     - Perform an inorder traversal of the tree, storing node values in an array (`vals`).
     - Check if the resulting array is strictly increasing, which ensures the BST property.
   - **Inorder Traversal**:
     - Traverse left subtree.
     - Process current node (append value to `vals`).
     - Traverse right subtree.
   - **Check Array**:
     - Iterate through `vals` to verify if each element is greater than the previous one.

   ```python
   def is_bst(root):
       vals = []
       def inorder(root, vals):
           if root is None:
               return
           inorder(root.left, vals)
           vals.append(root.val)
           inorder(root.right, vals)
       inorder(root, vals)
       for i in range(1, len(vals)):
           if vals[i] <= vals[i-1]:
               return False
       return True
   ```

   - **Time Complexity**: \( O(n) \) where \( n \) is the number of nodes (each node is visited once during traversal).
   - **Space Complexity**: \( O(n) \) due to the array `vals` storing node values.


### Conclusion:
These methods offer two distinct approaches to determine if a binary tree satisfies the BST property, catering to different preferences for traversal and validation strategies. Each method ensures efficiency in checking the tree structure against the BST criteria.


