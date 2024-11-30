


[How to solve binary tree path-related problems - Inside code](https://youtu.be/c1g6leyUuPM?si=Q24vsN-5FkMl0aKe)

solving binary tree path-related problems, including getting paths, finding the kth ancestor, finding the lowest common ancestor (LCA), and retrieving root-to-leaf paths. Each function is accompanied by comments explaining its purpose and approach, as well as the time and space complexities where applicable.

### Depth First Search (DFS) with Path Tracking

```python
# DFS to print nodes and track path
def dfs(root, path):
    if root is None:
        return
    else:
        print(root.val)  # Process the current node (print as an example)
        path.append(root)  # Add current node to the path
        dfs(root.left, path)  # Recur for left subtree
        dfs(root.right, path)  # Recur for right subtree
        path.pop()  # Remove current node from path during backtracking
```

### Get Path from Root to a Node

```python
# Function to find path from root to a specific node value
def get_path_from_root(root, val):
    def dfs(root, val, path):
        if root is None:
            return False
        else:
            path.append(root)
            if root.val == val or dfs(root.left, val, path) or dfs(root.right, val, path):
                return True
            path.pop()
            return False
    
    path = []
    dfs(root, val, path)
    return path
```

### Find Kth Ancestor of a Node

```python
# Function to find kth ancestor of a node
def kth_ancestor(root, val, k):
    path = get_path_from_root(root, val)
    if k >= len(path):
        return None
    else:
        return path[len(path) - k - 1]
```

### Lowest Common Ancestor (LCA) of Two Nodes

```python
# Function to find lowest common ancestor (LCA) of two nodes
def lca(root, val1, val2):
    path1 = get_path_from_root(root, val1)
    path2 = get_path_from_root(root, val2)
    last_common = None
    i = j = 0
    while i < len(path1) and j < len(path2):
        if path1[i] == path2[j]:
            last_common = path1[i]
            i += 1
            j += 1
        else:
            break
    return last_common
```

### Root to Leaf Paths

```python
# Function to get all root to leaf paths
def get_root_to_leaf_paths(root):
    def dfs(root, path, paths):
        if root is None:
            return
        else:
            path.append(root)
            if root.left is None and root.right is None:
                paths.append(path.copy())  # Add a copy of path when reaching leaf
            dfs(root.left, path, paths)  # Recur for left subtree
            dfs(root.right, path, paths)  # Recur for right subtree
            path.pop()  # Remove current node during backtracking

    paths = []
    path = []
    dfs(root, path, paths)
    return paths
```

### Explanation

- **DFS with Path Tracking:** Utilizes recursion to traverse the tree while maintaining a path list that tracks visited nodes.
  
- **Get Path from Root:** Uses DFS to find the path from the root to a specific node value, returning the list of nodes encountered.

- **Kth Ancestor:** Retrieves the kth ancestor of a node by using the path obtained from `get_path_from_root`.

- **Lowest Common Ancestor (LCA):** Determines the LCA of two nodes by comparing their paths obtained from `get_path_from_root`.

- **Root to Leaf Paths:** Collects all paths from the root to each leaf node using DFS, storing each complete path in a list.

### Time and Space Complexities

- **Time Complexity:** Each function involves a single traversal of the tree using DFS, resulting in O(n) time complexity, where n is the number of nodes in the tree.
  
- **Space Complexity:** Space complexity varies:
  - **DFS Path Tracking:** O(h) due to recursion stack depth, where h is the height of the tree.
  - **Path Storage:** Additional space is used to store paths, contributing to the overall space complexity.

These implementations provide a foundation for solving various tree-related problems efficiently using path tracking and DFS traversal.