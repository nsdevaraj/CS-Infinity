


[Binary Tree Traversals Recursive](https://www.hackerrank.com/topics/tree-traversals)

[Preorder BinaryTree TreeTraversal -HackerRank](https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?isFullScreen=true)
[LeetCode #102 - Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal).

[HackerRank Trees ](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=trees)
[Binary Tree Traversals - LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/1860290/tree-traversals-preorder-inorder-and-postorder-traverse-algorithms-all-in-one/)





## Recursive logics: ( basically DFS)


```python
def inOrder(root, result = [], display = True):
	if(root):
		inOrder(root.left, result, False)
		result.append(root.info)
		inOrder(root.right, result, False)
	if(display):
		print(' '.join(str(x) for x in result))
```


```python
def preOrder(root):
	def traverse(node):
		if(not node):
			return
		result.append(node.info)
		traverse(node.left)
		traverse(node.right)
	
	result = []
	traverse(root)
```


```python
def postOrder(root):
	result = []

	def traverse(node):
		if(node):
			traverse(node.left)
			traverse(node.right)
			result.append(node.info)
	
	traverse(root)	
	print(' '.join(map(str,result)))
```



```python
# in-order
traverse(node.left)
res.append(node.val)
traverse(node.right)

# pre-order
res.append(node.val)
traverse(node.left)
traverse(node.right)


# post-order
traverse(node.left)
traverse(node.right)
res.append(node.val)
```


```python
def levelOrder(root):

	result = []
	
	def traverse(node = root, level = 0):
		if(len(result) == level):
			result.append([])
		
		if(node):
			result[level].append(node.info)
			
			traverse(node.left, level + 1)
			traverse(node.right, level + 1)
	
	traverse()
	
	print(' '.join(map(str,[y for x in result for y in x])))
```


## Iterative logic

**trick - imitate recursive stack soln

Here’s how you can implement the `inorder`, `preorder`, and `postorder` traversal in an iterative way similar to the preorder function you've shared:

### Inorder Traversal:
```python
def inorder(root):
    if not root:
        return []

    result = []
    stack = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right

    return result
```

### Preorder Traversal (Already provided):
```python
def preorder(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        cur = stack.pop()
        result.append(cur.val)

        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return result
```

### Postorder Traversal:
```python
def postorder(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        cur = stack.pop()
        result.append(cur.val)

        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

    return result[::-1]  # Reverse the result to get the correct postorder
```


```python

def postorder(root):
  res = []
  if (not root):
      return res

  stack = [root]
  while (stack):
    cur = stack.pop()
    # not optimal one to insert at first
    res.insert(0, cur.data)

    if (cur.left):
        stack.append(cur.left)
    if (cur.right):
        stack.append(cur.right)

  return res

```

### Summary:
- **Inorder**: Traverse left subtree, root, then right subtree.
- **Preorder**: Traverse root, then left subtree, and finally right subtree.
- **Postorder**: Traverse left subtree, right subtree, and then root.


---


[Inorder traversal @NeetCode](https://youtu.be/g_S5WuasWUE)


inroder:

```python
 def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        cur = root
        stack = []
        while(cur or stack):
            # dig in direction atmost
            while(cur):
                # push items found in direction
                stack.append(cur)
                cur = cur.left
            
            # get item and explore 
            cur = stack.pop()
            result.append(cur.val)
            # if left complted, switch right's left
            cur = cur.right
        
        return result
```





```python 
# inorder alterations of the same


def inorder(root):
    result = []
    cur = root
    stack = []
    while(cur or stack):
        while(cur):
            stack.append(cur)
            cur = cur.left 
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    
    return result


def inorder(root):
    curr, stack = root, []
    res = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr)
            curr = curr.right
    return res

        
def inorder(root):
    cur = root
    stack = []
    res = []
    while True:
        if cur:
            stack.append(cur)
            cur = cur.left
        elif stack:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        else:
            return res
            
```



preorder:

[Preorder (iterative) @NeetCode](https://youtu.be/afTpieEZXck)


```python

def preorderTraversal(root) -> List[int]:
        result = []
        cur = root
        stack = []
        while(cur or stack):
            while(cur):
                result.append(cur.val)
                stack.append(cur.right)
                cur = cur.left 
            cur = stack.pop()
        
        return result
        
 
```


postorder

[Postorder (iterative) @NeetCode](https://youtu.be/QhszUQhGGlA)


```python

def postorder(root):
    result = []
    visited = [False]
    stack = [root]
    
    while(stack):
        cur, v = stack.pop(), visited.pop()
        if(cur):
            if v:
                result.append(cur.val)
            else:
                stack.append(cur)
                visited.append(True)
                stack.append(cur.right)
                visited.append(False)
                stack.append(cur.left)
                visited.append(False)
    return result
    
```



---
---



```python
class Node:  
    def __init__(self, key):  
        self.left = None  
        self.right = None  
        self.val = keydef insert(root, key):  
    if root is None:  
        return Node(key)    # Use a queue to do level order traversal until we find an empty place  
    queue = []  
    queue.append(root)    while queue:  
        temp = queue.pop(0)        if not temp.left:  
            temp.left = Node(key)  
            break  
        else:  
            queue.append(temp.left)        if not temp.right:  
            temp.right = Node(key)  
            break  
        else:  
            queue.append(temp.right)  
    return root# Function to print level order traversal of the tree  
def printLevelOrder(root):  
    if root is None:  
        return    queue = []  
    queue.append(root)    while queue:  
        node = queue.pop(0)  
        print(node.val, end=" ")        if node.left:  
            queue.append(node.left)  
        if node.right:  
            queue.append(node.right)# Example usage  
root = Node(1)  
insert(root, 2)  
insert(root, 3)  
insert(root, 4)  
insert(root, 5)print("Level order traversal of binary tree is -")  
printLevelOrder(root)

```

## Binary Tree Level Order Traversal

### Problem Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### Example

- **Example 1:**
  - **Input:** `root = [3,9,20,null,null,15,7]`
  - **Output:** `[[3],[9,20],[15,7]]`

- **Example 2:**
  - **Input:** `root = [1]`
  - **Output:** `[[1]]`

- **Example 3:**
  - **Input:** `root = []`
  - **Output:** `[]`

### Constraints
- The number of nodes in the tree is in the range $[0, 10^4]$.
- $-100 \leq \text{Node.val} \leq 100$

### Solution Approaches

The level order traversal of a binary tree can be achieved using different approaches. Here are some common methods:

#### 1. Breadth-First Search (BFS) Using Queue

**Algorithm Steps:**
1. Initialize an empty list to store the result.
2. Use a queue to perform BFS starting from the root node.
3. For each level, traverse nodes from left to right and store their values in a temporary list.
4. Append the temporary list to the result list.
5. Repeat until the queue is empty.

**Time Complexity:** $O(n)$, where \( n \) is the number of nodes in the tree.  
**Space Complexity:** $O(m)$, where \( m \) is the maximum number of nodes at any level (in the worst case, $m$ could be $n/2$).

**Python Code:**
```python
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])  # Initialize the queue with the root node

    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()  # Dequeue the front node
            level_nodes.append(node.val)  # Store the value
            
            # Enqueue the left and right children if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)  # Add the current level's values to the result

    return result
```


```python

def get_level_order(root:Optional[TreeNode])-> List[List[int]]:
    values:List[List[int]] = []

    if(not root):
        return values

    queue = deque([(root, 0)])

    while(queue):
        node, level = queue.popleft()

        if len(values) == level:
            values.append([])

        values[level].append(node.val)

        if(node.left):
            queue.append((node.left, level+1))
        if(node.right):
            queue.append((node.right, level+1))

    return values

```


#### 2. DFS (Depth-First Search) Using Recursion

**Algorithm Steps:**
1. Initialize an empty list to store the result.
2. Define a recursive function that takes the current node and its level as parameters.
3. If the current level is equal to the size of the result list, append an empty list to the result.
4. Add the current node's value to the corresponding level in the result.
5. Recursively call the function for the left and right children.

**Time Complexity:** $O(n)$, where \( n \) is the number of nodes in the tree.  
**Space Complexity:** $O(h)$, where \( h \) is the height of the tree due to the recursion stack.

**Python Code:**
```python
def levelOrderDFS(root: Optional[TreeNode]) -> List[List[int]]:
    result = []

    def dfs(node: Optional[TreeNode], level: int):
        if not node:
            return
        
        if level == len(result):
            result.append([])  # Create a new level
        result[level].append(node.val)  # Add the node's value to the current level
        
        # Recur for left and right children
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)  # Start DFS from level 0
    return result
```

### Summary of Approaches

| Approach                     | Time Complexity | Space Complexity | Description                                  |
|------------------------------|------------------|------------------|----------------------------------------------|
| Breadth-First Search (BFS)   | $O(n)$           | $O(m)$           | Use a queue to traverse nodes level by level. |
| Depth-First Search (DFS)     | $O(n)$           | $O(h)$           | Use recursion to visit nodes and store values level-wise. |

### Conclusion
Both the BFS and DFS approaches effectively achieve level order traversal of a binary tree. BFS is typically preferred for its straightforward approach using queues, while DFS can be a good alternative if a recursive solution is favored.

----

```python
```python
    def preorder_iterative(self):
        """
        Display data of nodes in a binary tree, iteratively traversing in pre-order
        :return: None
        """
        cur_node = self
        stack, preorder = [], []
        while cur_node or stack:
            if cur_node:    # visit the root first then following left child
                preorder.append(cur_node.data)
                stack.append(cur_node)
                cur_node = cur_node.l_child
            else:           # then right child
                cur_node = stack.pop()
                cur_node = cur_node.r_child
        return preorder

    def inorder_iterative(self):
        """
        Display data of nodes in a binary tree, iteratively traversing in in-order
        :return: None
        """
        cur_node = self
        stack, inorder = [], []
        while cur_node or stack:
            if cur_node:        # visit left child first
                stack.append(cur_node)
                cur_node = cur_node.l_child
            else:               # following root node and then the right child
                cur_node = stack.pop()
                inorder.append(cur_node.data)
                cur_node = cur_node.r_child
        return inorder

    def postorder_iterative(self):
        """
        Display data of nodes in a binary tree, iteratively traversing in post-order
        :return:
        """
        cur_node = self
        stack, postorder = [], []
        while cur_node or stack:
            if cur_node:        # visit left child first
                stack.append((cur_node, 1))
                cur_node = cur_node.l_child
            else:               # then back to the root node
                cur_node, visited = stack.pop()
                if visited == 2:    # if the root is visited twice, which means the left and right child have been visited
                    postorder.append(cur_node.data)
                    cur_node = None
                else:               # otherwise, visit its right child and marking the indicator to 2
                    stack.append((cur_node, 2))
                    cur_node = cur_node.r_child
        return postorder

    def preorder_recursive(self):
        def _preorder(node, order):
            if not node: return None
            order.append(node.data)
            _preorder(node.l_child, order)
            _preorder(node.r_child, order)

        if not self: return None
        preorder = []
        _preorder(self, preorder)
        return preorder

    def inorder_recursive(self):
        def _inorder(node, order):
            if not node: return None
            _inorder(node.l_child, order)
            order.append(node.data)
            _inorder(node.r_child, order)

        if not self: return None
        inorder = []
        _inorder(self, inorder)
        return inorder

    def postorder_recursive(self):
        def _postorder(node, order):
            if not node: return None
            _postorder(node.l_child, order)
            _postorder(node.r_child, order)
            order.append(node.data)

        if not self: return None
        postorder = []
        _postorder(self, postorder)
        return postorder
```


to check {


height of binary tre

bst or not 
}
\

to check {

https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/4381521/one-line-solution/


moris traversals

}
