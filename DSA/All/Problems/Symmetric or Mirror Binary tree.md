

[Symmetric binary tree - YT(InsideCode)](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=1178s) 

[ ? LeetCode #101](https://leetcode.com/problems/symmetric-tree/)
[ ? Symmetric binary Tree @GFG](https://www.geeksforgeeks.org/problems/symmetric-tree/1)


[Mirror Binary Tree @GFG](https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/)




---

## Problem Statement: "Symmetric Tree"

Given the root of a binary tree, determine whether the tree is **symmetric** around its center, meaning it is a mirror reflection of itself.

### Example 1:
```text
Input: 
        1
       / \
      2   2
     / \ / \
    3  4 4  3
Output: True
```

### Example 2:
```text
Input:
        1
       / \
      2   2
       \   \
        3   3
Output: False
```

---

## Approach 1: Recursive Solution

### Idea:
To check if a binary tree is symmetric, we need to determine if its left subtree is a **mirror reflection** of its right subtree. In other words:
- The root values must be the same.
- The left subtree of the root must be a mirror of the right subtree.

This can be implemented recursively by checking the following for two subtrees:
1. Both subtrees are empty (symmetric).
2. One subtree is empty while the other is not (not symmetric).
3. Both subtrees have the same root value, and their left and right subtrees are symmetric to each other.

### Code:
```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_symmetric(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    # Both trees are empty
    if root1 is None and root2 is None:
        return True
    # One tree is empty, or the values don't match
    if root1 is None or root2 is None or root1.val != root2.val:
        return False
    # Check if left subtree of root1 is symmetric to right subtree of root2
    # and right subtree of root1 is symmetric to left subtree of root2
    return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)

def is_symmetric(root: Optional[TreeNode]) -> bool:
    # An empty tree is symmetric
    if root is None:
        return True
    # Check if the left and right subtrees are symmetric
    return are_symmetric(root.left, root.right)
```


```python

#User function Template for python3

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        
        def isSymmetric(node1, node2):
            
            if(node1 is None and node2 is None):
                return True
            
            if(node1 is None and node2 is not None):
                return False
            
            if(node1 is not None and node2 is None):
                return False
            
            if(node1.data != node2.data):
                return False
            
            return isSymmetric(node1.left, node2.right) and isSymmetric(node1.right, node2.left)
        
        
        if(root is None):
            return True
        
        return isSymmetric(root.left, root.right)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        if ob.isSymmetric(root):
            print("True")
        else:
            print("False")
        
        

        print("~")
# } Driver Code Ends

```


```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to check if two subtrees are mirror images
        def is_mirror(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            # Both nodes are None, this is symmetric
            if not n1 and not n2:
                return True
            # One of the nodes is None, this is not symmetric
            if not n1 or not n2:
                return False
            # Check if current nodes are equal and their subtrees are mirror images
            return (n1.val == n2.val 
                    and is_mirror(n1.left, n2.right) 
                    and is_mirror(n1.right, n2.left))
        
        # Start the recursive mirror check on the left and right children of the root
        return is_mirror(root.left, root.right)

```
### Time Complexity:
- Each node is visited exactly once, so the time complexity is $O(n)$, where `n` is the number of nodes in the tree.

### Space Complexity:
- The space complexity is determined by the recursion depth, which depends on the height of the tree. For a balanced tree, the height is $O(\log n)$, giving a space complexity of $O(\log n)$. For a skewed tree, the height could be $O(n)$.

---

## Approach 2: Iterative Solution Using a Queue

### Idea:
Instead of using recursion, we can solve the problem iteratively by simulating the recursive stack with a queue (BFS-like approach). We compare nodes level by level:
- Start with the left and right children of the root.
- Push corresponding nodes (left-left with right-right, left-right with right-left) onto the queue.
- Continue until the queue is empty or we find a mismatch.

### Code:
```python
from collections import deque
from typing import Optional

def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:
    # An empty tree is symmetric
    if root is None:
        return True

    # Initialize queue with root's children
    queue = deque([(root.left, root.right)])

    while queue:
        node1, node2 = queue.popleft()

        # Both nodes are None, move to the next pair
        if node1 is None and node2 is None:
            continue

        # One is None, or values don't match
        if node1 is None or node2 is None or node1.val != node2.val:
            return False

        # Enqueue children in the mirror order
        queue.append((node1.left, node2.right))
        queue.append((node1.right, node2.left))

    return True
```

### Time Complexity:
- Each node is processed once, resulting in $O(n)$ time complexity, where `n` is the number of nodes in the tree.

### Space Complexity:
- The space complexity is $O(n)$ in the worst case because we are storing nodes in the queue.

---
## Stack

```python
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, it is symmetric
        if root is None:
            return True

        # Initialize two stacks to compare nodes on the left and right sides
        stack1, stack2 = [root.left], [root.right]

        # Process until both stacks are empty
        while stack1 and stack2:
            # Pop nodes from each stack for comparison
            node1, node2 = stack1.pop(), stack2.pop()

            # If both nodes are None, continue to next pair of nodes
            if node1 is None and node2 is None:
                continue

            # If only one of the nodes is None or their values are different, the tree is not symmetric
            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            # Add the children in opposite order for mirror comparison
            stack1.append(node1.left)
            stack2.append(node2.right)
            
            stack1.append(node1.right)
            stack2.append(node2.left)

        # If both stacks are empty, the tree is symmetric; otherwise, it's not
        return not stack1 and not stack2

```


---



## Summary of Approaches

| Approach              | Time Complexity | Space Complexity      | Explanation                                                     |
| --------------------- | --------------- | --------------------- | --------------------------------------------------------------- |
| **Recursive**         | $O(n)$          | $O(\log n)$ or $O(n)$ | Simple recursive DFS approach, efficient for balanced trees.    |
| **Iterative (Queue)** | $O(n)$          | $O(n)$                | Simulates BFS using a queue, good for handling iterative logic. |

---




### Conclusion:

The recursive and iterative solutions both have the same time complexity. The recursive approach is more intuitive but may cause stack overflow for very deep trees. The iterative approach using a queue avoids this issue but requires more memory for the queue.



to check {

https://leetcode.com/problems/path-sum/description/


}

