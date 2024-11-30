
[How to clone a graph (LeetCode #133) - Inside code](https://youtu.be/zjkHN0zNgn4?si=GVbsOe3uK3REtQhB)

[Leetcode - Clone Graph ](https://leetcode.com/problems/clone-graph/)


### Cloning a Graph (LeetCode #133)

#### Problem Statement
We are given a connected **undirected graph** represented by a **reference node**. Each node has a unique integer value and a list of its **neighbors**. Our task is to create a **deep copy** of the graph where the nodes have the same values and the same connections, but all nodes must be newly created (no references to the original nodes).

##### Example:
```plaintext
Input: Graph represented by node 1

    1
   / \
  2   4
 /     \
3-------5

Output: Deep copy of the graph with the same structure.
```

#### Approach 1: Recursive Depth-First Search (DFS)

To solve this problem, we can use **DFS** to traverse the graph. The key is that we need to create each node only **once**. Whenever we encounter a node for the first time, we create its clone and store it in a **hash map**. If we encounter the node again, we simply use the stored clone to avoid creating multiple copies of the same node.

##### Steps:
1. **DFS Traversal**:
   - Start at the input node.
   - For each node, check if it already has a clone (using a `node_map`). If not, create a new node, and recursively clone all of its neighbors.
   - Return the clone at the end.
   
2. **Hash Map**:
   - Use a dictionary (`node_map`) to map from original nodes (by their values) to their cloned versions.

#### Code Implementation (Recursive DFS):
```python
from typing import Dict

class Node:
    def __init__(self, val: int = 0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def dfs(node: Node, node_map: Dict[int, Node]) -> Node:
    # Create a clone of the current node
    clone = Node(node.val)
    node_map[node.val] = clone
    
    # Traverse all neighbors of the current node
    for neighbor in node.neighbors:
        if neighbor.val not in node_map:
            # If neighbor is not cloned yet, recursively clone it
            dfs(neighbor, node_map)
        # Append the clone of the neighbor to the neighbors of the current clone
        clone.neighbors.append(node_map[neighbor.val])
    
    return clone

def clone_graph(node: Node) -> Node:
    if node is None:
        return None
    # Hash map to store the original node to clone mapping
    node_map = {}
    # Start DFS from the given node
    return dfs(node, node_map)
```

##### Explanation:
- We initialize the cloning process from the input node.
- For each node, we create its clone (if it doesn't already exist), then recursively clone all its neighbors.
- The `node_map` ensures that no node is cloned more than once.

##### Time Complexity:
- **O(V + E)**, where \( V \) is the number of vertices (nodes) and \( E \) is the number of edges in the graph. This is because we visit every node once and traverse all edges during the DFS traversal.

##### Space Complexity:
- **O(V + E)**, since we store a clone for each node and replicate the connections (edges) between nodes in the new graph.

#### Approach 2: Iterative Depth-First Search (Using a Stack)

We can also implement DFS **iteratively** using a **stack** instead of recursion. This is useful when the recursion depth might become too large and lead to a stack overflow.

##### Steps:
1. Use a stack to maintain nodes for which neighbors need to be cloned.
2. Initialize the clone for the starting node and push the original node to the stack.
3. Process nodes from the stack, cloning each neighbor if it hasn't been cloned yet.

#### Code Implementation (Iterative DFS):
```python
def clone_graph_iterative(node: Node) -> Node:
    if node is None:
        return None
    
    # Hash map to store the original node to clone mapping
    node_map = {}
    
    # Initialize the clone for the starting node
    node_map[node.val] = Node(node.val)
    
    # Stack to perform DFS
    stack = [node]
    
    while stack:
        curr_node = stack.pop()
        
        # Iterate over all neighbors of the current node
        for neighbor in curr_node.neighbors:
            if neighbor.val not in node_map:
                # Clone the neighbor if it hasn't been cloned yet
                node_map[neighbor.val] = Node(neighbor.val)
                # Push the neighbor to stack for DFS
                stack.append(neighbor)
            # Add the cloned neighbor to the current clone's neighbors
            node_map[curr_node.val].neighbors.append(node_map[neighbor.val])
    
    return node_map[node.val]
```

##### Time Complexity:
- Same as recursive DFS, **O(V + E)**.

##### Space Complexity:
- **O(V + E)**, due to the stack and hash map usage.

#### Approach Summary (Tabular Comparison)

| Approach               | Description                                   | Time Complexity  | Space Complexity |
|------------------------|-----------------------------------------------|------------------|------------------|
| **Recursive DFS**       | Traverse the graph recursively, clone nodes on the fly | O(V + E)          | O(V + E)          |
| **Iterative DFS**       | Use an explicit stack to clone the graph iteratively | O(V + E)          | O(V + E)          |

#### Conclusion:
Both the recursive and iterative DFS approaches work well for cloning a graph, ensuring we create a **deep copy** without duplicating nodes unnecessarily.


### Cloning a Tree

Cloning a tree is simpler than cloning a graph due to the absence of cycles and shared neighbors. Trees are structured hierarchically, where each node has a parent and a set of children, but no two nodes share a child node. The key observation here is that every node will be visited only once in a depth-first or breadth-first traversal, which makes cloning the tree straightforward.

The algorithm to clone a tree is a recursive approach where we:

1. Create a new node with the same value as the original.
2. Recursively clone each child of the original node and assign the cloned child to the clone.
3. Return the root of the cloned tree.

### Code for Cloning a Tree

```python
class TreeNode:
    def __init__(self, val: int, children=None):
        self.val = val
        self.children = children if children is not None else []

def clone_tree(node: TreeNode) -> TreeNode:
    if node is None:
        return None
    # Create the clone node
    cloned_node = TreeNode(node.val)
    
    # Recursively clone each child and append to cloned node's children
    for child in node.children:
        cloned_node.children.append(clone_tree(child))
    
    return cloned_node
```

### Why Cloning a Tree is Simpler than Cloning a Graph

The main reason cloning a tree differs from cloning a graph is the lack of shared neighbors and cycles in trees. In a tree:

- **No Cycles**: Nodes are never revisited, which means we don't have to worry about infinite recursion or duplicated nodes.
- **Unique Children**: Every child node has a unique parent. This means each node will be cloned exactly once.

However, when it comes to a **graph**, nodes may have multiple parents or be connected in cycles. Without proper handling, we might end up cloning the same node multiple times, leading to incorrect results. This is why we must store references to already cloned nodes in the graph cloning approach (using a hash map) to ensure that each node is cloned only once, and we correctly maintain the relationships between nodes.

In summary:

| Problem       | Key Differences                                 | Complexity                                    | Approach                           |
|---------------|-------------------------------------------------|-----------------------------------------------|------------------------------------|
| **Clone Tree**| Simple hierarchical structure, no cycles.       | Time: $O(n)$, Space: $O(n)$, where $n$ is the number of nodes. | Depth-first search (DFS) with recursion.|
| **Clone Graph**| Nodes can have multiple parents or cycles.      | Time: $O(V + E)$, Space: $O(V + E)$, where $V$ is vertices and $E$ is edges. | DFS/BFS with a hash map to avoid revisiting nodes.|

This shows why cloning a graph is more complex than cloning a tree—graphs require additional checks to avoid duplicate nodes or cycles, while trees do not.


