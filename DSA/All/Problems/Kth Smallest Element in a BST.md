

https://www.youtube.com/watch?v=5LUXSvjmGCw


The problem "Kth Smallest Element in a BST" (Leetcode #230) asks us to find the k-th smallest element in a Binary Search Tree (BST). Below are Python solutions to this problem, including different approaches.

---

### **Approach 1: In-order Traversal**

The in-order traversal of a BST gives the elements in sorted order. We can use this property to extract the k-th smallest element.

#### **Code**

```python

def getKthSmallest(root: TreeNode, k:int)-> int:

    def traverseInOrder(head: Optional[TreeNode])-> List[int]:
        if(head is None):
            return []
        return traverseInOrder(head.left) + [head.val] + traverseInOrder(head.right);

    sorted_list:List[int] = traverseInOrder(root)

    return sorted_list[k-1]
```

#### **Time Complexity**

- **Traversal**: O(n)O(n), where nn is the number of nodes in the tree.
- **Space Complexity**: O(n)O(n), for storing the traversal.

---

### **Approach 2: In-order Traversal with Early Termination**

Instead of traversing the entire tree, we can terminate once we reach the k-th smallest element.

#### **Code**

```python

def getKthSmallest(root: TreeNode, k:int)-> int:

    value:Optional[int] = None
    k_count = 0
    def traverseInOrderAndFindK(head: Optional[TreeNode])-> None:
        nonlocal value, k_count
        if(head is None or value is not None):
            return

        traverseInOrderAndFindK(head.left)
        k_count += 1
        if(k_count == k):
            value = head.val
            return

        traverseInOrderAndFindK(head.right)

    traverseInOrderAndFindK(root)

    if value is None:
        raise ValueError("k is out of bounds.")

    return value


```

#### **Time Complexity**

- **Traversal**: O(k)O(k) in the best case (when the k-th smallest element is early in the traversal).
- **Space Complexity**: O(h)O(h), where hh is the height of the tree (for the recursion stack).

---

### **Approach 3: Iterative In-order Traversal**

An iterative approach using a stack can also efficiently find the k-th smallest element.

#### **Code**

```python

def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    current = root
    count = 0

    while stack or current:
        # take all left
        while current:
            stack.append(current)
            current = current.left
		
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        
		# recursively take all right
        current = current.right
```

#### **Time Complexity**

- **Traversal**: O(k)O(k), as we only process up to k elements.
- **Space Complexity**: O(h)O(h), where hh is the height of the tree.

---

### **Test Cases**


```python
from typing import Optional, Callable, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def test_kthSmallest(func: Callable[[TreeNode, int], int]) -> None:
    def insert_into_bst(root: Optional[TreeNode], val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    def build_bst(values: List[int]) -> Optional[TreeNode]:
        root = None
        for val in values:
            root = insert_into_bst(root, val)
        return root

    test_cases = [
        # Test Case 1: Simple BST
        {
            "tree": build_bst([3, 1, 4, 2]),
            "k": 1,
            "expected": 1,
        },
        # Test Case 2: Larger BST
        {
            "tree": build_bst([5, 3, 6, 2, 4, 1]),
            "k": 3,
            "expected": 3,
        },
        # Test Case 3: BST with only two nodes
        {
            "tree": build_bst([2, 1]),
            "k": 2,
            "expected": 2,
        },
        # Test Case 4: BST with duplicates (don't do special logic for duplicates')
        {
            "tree": build_bst([5, 3, 6, 2, 4, 4, 1]),
            "k": 5,
            "expected": 4,
        },
        # Test Case 5: Single node tree
        {
            "tree": build_bst([1]),
            "k": 1,
            "expected": 1,
        },
        # Test Case 6: Right-skewed BST
        {
            "tree": build_bst([1, 2, 3, 4, 5]),
            "k": 4,
            "expected": 4,
        },
        # Test Case 7: Left-skewed BST
        {
            "tree": build_bst([5, 4, 3, 2, 1]),
            "k": 2,
            "expected": 2,
        },
        # Test Case 8: Large BST
        {
            "tree": build_bst([15, 10, 20, 8, 12, 17, 25]),
            "k": 5,
            "expected": 17,
        },
        # Test Case 9: Tree with no left subtree
        {
            "tree": build_bst([10, 15, 20]),
            "k": 1,
            "expected": 10,
        },
        # Test Case 10: Tree with no right subtree
        {
            "tree": build_bst([10, 5, 2]),
            "k": 3,
            "expected": 10,
        },
    ]

    for i, case in enumerate(test_cases):
        result = func(case["tree"], case["k"])
        assert result == case["expected"], (
            f"Test case {i + 1} failed: k={case['k']}, Expected={case['expected']}, "
            f"but got {result}"
        )
    print("All test cases passed!")

```

---

These solutions provide different trade-offs between simplicity and efficiency. Use the one that best fits your constraints and problem requirements.





### 9. **Kth Smallest Element in a BST**

**Problem:** Given a binary search tree (BST), find the kth smallest element.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
```


OThers:

Memory: 18.7mb

python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr

                temp = curr
                curr = curr.left
                temp.left = None

            
    
```




Runtime: 3ms

python 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        def explorer(node):
            if len(heap) >= k:
                if node.val > heap[0]:
                    heapq.heappush(heap, -node.val)
                    heapq.heappop(heap)
            else:
                heapq.heappush(heap, -node.val)

            if node.left:
                explorer(node.left)
            if node.right:
                explorer(node.right)

        explorer(root)

        return -heap[0]
```

