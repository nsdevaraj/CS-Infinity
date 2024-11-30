

[Course schedule - YT(InsideCode) ](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=2994s) 




# Course Schedule Problem

## Problem Statement

You are given **n** courses labeled from `0` to `n-1`. Some courses have prerequisites, meaning you must take one course before another. The prerequisites are represented by a list where `prerequisites[i] = [a, b]`, meaning **to take course `a`, you must first take course `b`**. Your task is to determine whether it's possible to complete all courses given these prerequisites.

### Input:
- An integer `n` representing the number of courses.
- A list `prerequisites` where each element is a pair `[a, b]` meaning `b` is a prerequisite for `a`.

### Output:
- Return `True` if it's possible to finish all the courses, otherwise return `False`.

### Example 1:
```
Input: 
n = 4
prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]

Output: 
False

Explanation:
To take course 3, you must take course 2. 
To take course 2, you must take course 1.
To take course 1, you must take course 3.
Hence, there is a cycle, and it's impossible to complete all courses.
```

### Example 2:
```
Input:
n = 6
prerequisites = [[1, 0], [2, 1], [3, 1], [4, 3], [5, 4]]

Output:
True

Explanation:
You can take the courses in the following order: 0 -> 1 -> 2 -> 3 -> 4 -> 5.
There are no circular dependencies, so it is possible to complete all the courses.
```

---

## Solution Approaches


we are not able to use just visited set, since a node can be visited by 2 paths and in dfs we may already finished exploration of node before, pushing in visited set can't help whether its already visited or visited in the current driven path!

### 1. **Depth-First Search (DFS) with Cycle Detection**

The key observation is that this problem can be represented as a **directed graph**:
- Each course is a **node**.
- A directed edge from course `b` to course `a` means **b is a prerequisite for a**.

To check whether all courses can be completed, we need to ensure there is no cycle in the graph. A **cycle** implies that the courses have circular dependencies, making it impossible to complete all.

We can use **DFS** to detect cycles by tracking the current path and detecting if we revisit a node already in the path.

#### Algorithm:
1. **Graph Representation**: Use an adjacency list to represent the graph.
2. **Cycle Detection**: Perform DFS for each unvisited node. If we encounter a node already in the current DFS path, we have found a cycle.
3. **Return Result**: If a cycle is detected, return `False`. If no cycles are found after checking all nodes, return `True`.

#### Code:

```python
from typing import List, Set

def dfs(graph: List[List[int]], vertex: int, path: Set[int], order: List[int], visited: Set[int]) -> bool:
    path.add(vertex)  # Add vertex to the current DFS path
    for neighbor in graph[vertex]:
        if neighbor in path:  # Cycle detected
            return False
        if neighbor not in visited:  # Visit unvisited neighbors
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False
    path.remove(vertex)  # Remove from current path after visiting
    order.append(vertex)  # Add to topological order after all neighbors are visited
    return True

def can_finish_dfs(n: int, prerequisites: List[List[int]]) -> bool:
    # Build the adjacency list
    graph = [[] for _ in range(n)]
    for a, b in prerequisites:
        graph[b].append(a)  # Edge b -> a (b is a prerequisite of a)
    
    visited = set()
    path = set()  # Tracks the current DFS path to detect cycles
    order = []    # Topological ordering
    
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False  # If a cycle is detected
    return True  # No cycles found, all courses can be completed
```

#### Time Complexity:
- Building the graph takes **O(m)**, where `m` is the number of prerequisites.
- The DFS traversal takes **O(n + m)** where `n` is the number of nodes (courses) and `m` is the number of edges (prerequisites).

Overall time complexity: **O(n + m)**.

#### Space Complexity:
- Adjacency list takes **O(n + m)** space.
- The recursion stack in the worst case takes **O(n)** space.
- Additional space for the visited and path sets.

Overall space complexity: **O(n + m)**.

---


**Topological sort** gives a linear ordering of vertices such that for every directed edge `U -> V`, vertex `U` comes before `V` in the ordering. If the graph contains a cycle, a topological sort is impossible.


### 2. **Topological Sort Using DFS**

Topological sort is a linear ordering of vertices in a directed graph, where for every directed edge `U -> V`, vertex `U` comes before `V` in the ordering. In the **Course Schedule** problem, if the graph (representing the courses and prerequisites) has a valid topological sort, it means there's no cycle, and all courses can be completed.

#### Key Idea:
We can use **DFS** to generate a topological ordering of the courses. If we can generate such an ordering, then there is no cycle, and the courses can be completed. If a cycle is detected during the DFS traversal, it indicates that the course schedule is not possible.

#### Algorithm:
1. **Graph Representation**: Use an adjacency list to represent the graph, where each course is a node, and a directed edge from course `b` to course `a` means **b is a prerequisite of a**.
2. **Topological Sorting with DFS**: Perform a DFS for each unvisited node. While performing DFS, add the nodes to the result in post-order (after visiting all its neighbors). This ensures that all dependencies are visited before adding a course to the final order.
3. **Cycle Detection**: Use an additional visited status (`-1`, `0`, `1`) for nodes:
   - `0`: Not visited.
   - `-1`: Visiting (currently in the recursion stack, used to detect cycles).
   - `1`: Fully processed.
4. **Result**: If a cycle is detected (i.e., visiting a node that is already in the current DFS path), return `False`. If no cycles are detected, return `True`.

#### Code:

#### easy one

```python
from typing import List

def dfs_topological(graph: List[List[int]], course: int, visited: List[int], stack: List[int]) -> bool:
    # Mark the course as being visited (in the current recursion path)
    visited[course] = -1
    
    # Visit all the prerequisites (neighbors) of this course
    for neighbor in graph[course]:
        if visited[neighbor] == -1:  # Cycle detected
            return False
        if visited[neighbor] == 0:   # Not visited yet, so recurse
            if not dfs_topological(graph, neighbor, visited, stack):
                return False
    
    # Mark the course as fully processed and add to the topological order stack
    visited[course] = 1
    stack.append(course)
    return True

def can_finish_topological_sort_dfs(n: int, prerequisites: List[List[int]]) -> bool:
    # Build the adjacency list
    graph = [[] for _ in range(n)]
    for a, b in prerequisites:
        graph[b].append(a)  # Edge b -> a (b is a prerequisite of a)
    
    visited = [0] * n  # 0: Not visited, -1: Visiting, 1: Fully processed
    stack = []         # Stack to store topological order
    
    # Perform DFS from each unvisited node
    for course in range(n):
        if visited[course] == 0:
            if not dfs_topological(graph, course, visited, stack):
                return False  # If a cycle is detected, return False
    
    # If no cycle is detected, return True (courses can be finished)
    return True
```

#### Explanation:
- We first build the **graph** (adjacency list) representing the course dependencies.
- Then, we initialize the `visited` array and `stack` for storing the topological order.
- For each course that has not been visited, we call the `dfs_topological` function.
- In the DFS function, we mark the node as being processed (`-1`), visit all its neighbors, and after processing, we add the course to the topological order stack.
- If we find a cycle during DFS (a course being visited again while still in the recursion stack), we return `False`, indicating that it's not possible to finish all courses.
- If no cycles are found, we return `True`.

#### Time Complexity:
- **Graph construction** takes **O(m)**, where `m` is the number of prerequisites.
- **DFS traversal** takes **O(n + m)**, where `n` is the number of courses and `m` is the number of prerequisites.

Overall time complexity: **O(n + m)**.

#### Space Complexity:
- **Graph** (adjacency list) takes **O(n + m)** space.
- **Visited array** takes **O(n)** space.
- **Recursion stack** in DFS takes **O(n)** space in the worst case.

Overall space complexity: **O(n + m)**.


#### Conclusion:
The **Topological Sort using DFS** approach is a popular and efficient method for solving the **Course Schedule** problem. It gives a linear ordering of the courses if there are no cycles and works in **O(n + m)** time complexity, just like other efficient algorithms like **Kahn's Algorithm (BFS)**.


### 3. **Kahn's Algorithm (BFS / Topological Sort)**


**Kahn's Algorithm** uses **BFS** to perform topological sorting:
- Track the **in-degree** (number of incoming edges) of each node.
- Start with nodes that have **0 in-degree** (no prerequisites).
- Gradually remove these nodes and reduce the in-degree of their neighbors.
- If all nodes can be ordered, there are no cycles.

#### Algorithm:
1. **Graph Representation**: Build the adjacency list and compute in-degrees of all vertices.
2. **Queue Initialization**: Add all nodes with `0` in-degree to the queue.
3. **BFS Traversal**: Remove nodes from the queue and reduce the in-degree of their neighbors.
4. **Cycle Detection**: If all nodes are processed, return `True`. Otherwise, return `False` (cycle exists).

#### Code:

#### **optimal:

```python
from collections import deque
from typing import List

def can_finish_bfs(n: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(n)]
    indegree = [0] * n  # Track in-degree of each node
    
    # Build the graph and compute in-degrees
    for a, b in prerequisites:
        graph[b].append(a)  # Edge b -> a (b is a prerequisite of a)
        indegree[a] += 1
    
    # Initialize the queue with courses having 0 in-degree (no prerequisites)
    queue = deque([i for i in range(n) if indegree[i] == 0])
    count = 0  # Track number of courses processed
    
    while queue:
        course = queue.popleft()
        count += 1  # Process this course
        for neighbor in graph[course]:
            indegree[neighbor] -= 1  # Reduce in-degree of neighbors
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == n  # If we processed all courses, return True, else False
```

if need order, track order:

```python
from collections import deque
from typing import List

def can_finish_courses(num_courses: int, prerequisites: List[List[int]]) -> bool:
    # Initialize a graph and incoming edge count
    adj_list = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    # Build the adjacency list and in-degree count
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1

    # Initialize the queue with courses that have no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    
    completed_courses = []

    # Process the courses in the queue
    while queue:
        current_course = queue.popleft()
        completed_courses.append(current_course)

        # Decrease in-degree for neighbors and add to queue if no more prerequisites
        for next_course in adj_list[current_course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # Check if all courses can be completed
    return len(completed_courses) == num_courses

```

#### Time Complexity:
- Building the graph and computing in-degrees takes **O(m)**.
- BFS traversal takes **O(n + m)**.

Overall time complexity: **O(n + m)**.

#### Space Complexity:
- Adjacency list takes **O(n + m)** space.
- Queue and indegree array take **O(n)** space.

Overall space complexity: **O(n + m)**.

---

### 4. **Backtracking Approach (Less Efficient)**

Although this is not commonly used for this type of problem, a backtracking approach can explore all paths to detect cycles. However, it's inefficient due to repeated state exploration and is typically not preferred.

---
## Summary of Approaches

| Approach                     | Time Complexity | Space Complexity | Description                                        |
| ---------------------------- | --------------- | ---------------- | -------------------------------------------------- |
| **DFS with Cycle Detection** | $O(n + m)$      | $O(n + m)$       | Uses DFS to detect cycles in the graph.            |
| **Topological Sort (DFS)**   | $O(n + m)$      | $O(n + m)$       | DFS-based topological sort with cycle detection.   |
| **Kahn's Algorithm (BFS)**   | $O(n + m)$      | $O(n + m)$       | Uses BFS for topological sort and cycle detection. |
| **Backtracking**             | Exponential     | $O(n)$           | Less efficient due to repeated state exploration.  |

### Legend:
- **n**: Number of courses (vertices).
- **m**: Number of prerequisites (edges).



----



### Section 1: Course Schedule Problem (LeetCode #207)

[LeetCode #207 - Course Schedule](https://leetcode.com/problems/course-schedule/)

[Course Schedule I and II - YT(takeUForward)](https://www.youtube.com/watch?v=WAOfKpxYHR8)



---

### Problem Statement

You are given a total of `numCourses` courses to take, labeled from `0` to `numCourses-1`. You are also given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must complete course `b` before course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

#### Constraints:
- The input `numCourses` is an integer between 1 and 2000.
- The input `prerequisites` is an array of pairs where each element is a pair `[a, b]`.
- Prerequisites contain no duplicate pairs.

#### Example 1:

```plaintext
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Explanation: You can complete course 0 first and then take course 1.
```

#### Example 2:

```plaintext
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
Explanation: There is a cycle between course 0 and course 1, so it's impossible to complete all courses.
```

---


```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(node: int, visited: List[bool], recStack: List[bool], graph: List[List[int]]) -> bool:
            # Mark the current node as visited and part of the recursion stack
            visited[node] = True
            recStack[node] = True

            # Visit all the neighbors
            for neighbor in graph[node]:
                # If neighbor is not visited, visit it
                if not visited[neighbor]:
                    if dfs(neighbor, visited, recStack, graph):
                        return True
                # If neighbor is in the recursion stack, a cycle is detected
                elif recStack[neighbor]:
                    return True

            # Remove the node from the recursion stack after processing all its neighbors
            recStack[node] = False
            return False

        # Create the adjacency list for the graph
        graph = {x: [] for x in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # To keep track of visited nodes and nodes in the recursion stack
        visited = [False] * numCourses
        recStack = [False] * numCourses

        # Perform DFS for all unvisited nodes
        for course in range(numCourses):
            if not visited[course]:
                if dfs(course, visited, recStack, graph):
                    return False  # Cycle detected

        # If no cycles are detected, all courses can be finished
        return True


```


```python
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list and indegree array
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build the graph and calculate indegrees
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course] += 1

        # Queue to store nodes with 0 indegree
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        topo_sort = []  # List to store topological sort

        # Process the nodes in BFS manner
        while queue:
            node = queue.popleft()
            topo_sort.append(node)  # This node is in the topological order

            # Reduce the indegree of the neighbors
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If we are able to process all nodes, return True (no cycle detected)
        return len(topo_sort) == numCourses

```



#### easy soln:

```python
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list to represent the graph
        graph = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Visited set with 3 possible states:
        # 0: unvisited, 1: visiting (on current DFS path), 2: fully visited
        visited = [0] * numCourses

        # DFS function to detect cycles
        def dfs(node: int) -> bool:
            if visited[node] == 1:
                # Cycle detected
                return False
            if visited[node] == 2:
                # Already fully visited (no cycle)
                return True

            # Mark the current node as being visited
            visited[node] = 1

            # Recur for all neighbors (courses dependent on this course)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # Mark the current node as fully visited after exploring all its neighbors
            visited[node] = 2
            return True

        # Check each course using DFS
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


```



### Approaches

#### 1. **Topological Sorting (Kahn’s Algorithm - BFS)**

**Explanation**: 
This approach is based on the concept of topological sorting, which is useful when solving dependency problems. We can think of the course schedule as a Directed Acyclic Graph (DAG). If we can perform a topological sort of all the nodes (courses), then it’s possible to complete all courses; otherwise, there’s a cycle, meaning it's impossible.

**Steps**:
1. Represent the courses and prerequisites as a directed graph.
2. Use an array `in_degree` to track the number of prerequisites (incoming edges) each course has.
3. Start with the nodes (courses) that have zero prerequisites (in-degree 0).
4. For each node, reduce the in-degree of its neighbors (courses that depend on it). If a neighbor’s in-degree becomes 0, add it to the queue.
5. If all courses are processed, return `true`; otherwise, there’s a cycle, so return `false`.

```python
from collections import deque
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Create an adjacency list and an array to store in-degrees
    adj_list = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses
    
    # Build the graph and fill in-degrees
    for course, pre in prerequisites:
        adj_list[pre].append(course)
        in_degree[course] += 1
    
    # Queue to process courses with zero prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    processed_courses = 0
    
    # Process the queue
    while queue:
        course = queue.popleft()
        processed_courses += 1
        
        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If all courses are processed, return True
    return processed_courses == numCourses
```

**Time Complexity**: 
- Constructing the adjacency list takes $O(P)$ where $P$ is the number of prerequisites.
- BFS traversal takes $O(C + P)$, where $C$ is the number of courses and $P$ is the number of prerequisites.
- **Total**: $O(C + P)$

**Space Complexity**: 
- Adjacency list takes $O(C + P)$, in-degree array takes $O(C)$.
- **Total**: $O(C + P)$

---

#### 2. **DFS-based Cycle Detection**

**Explanation**:
Another way to solve the problem is by using Depth First Search (DFS). We check for cycles in the directed graph formed by the courses. A cycle in the graph means we cannot complete all courses.

**Steps**:
1. Build a graph using an adjacency list.
2. For each unvisited course, perform a DFS to detect cycles.
3. Use a `visited` array where:
   - `0` means the node has not been visited yet.
   - `1` means the node is currently being visited (part of the current path).
   - `2` means the node has already been fully processed and doesn’t have a cycle.
4. If a cycle is detected during the DFS, return `false`; otherwise, return `true`.

```python
def canFinishDFS(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj_list = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        adj_list[pre].append(course)
    
    visited = [0] * numCourses

    def has_cycle(course: int) -> bool:
        if visited[course] == 1:  # cycle detected
            return True
        if visited[course] == 2:  # already processed node
            return False
        
        visited[course] = 1  # mark as visiting
        for neighbor in adj_list[course]:
            if has_cycle(neighbor):
                return True
        
        visited[course] = 2  # mark as processed
        return False
    
    for course in range(numCourses):
        if has_cycle(course):
            return False
    
    return True
```

**Time Complexity**:
- DFS traversal takes $O(C + P)$.
- **Total**: $O(C + P)$

**Space Complexity**:
- Adjacency list and visited array take $O(C + P)$ and $O(C)$, respectively.
- **Total**: $O(C + P)$

---

### Example Walkthrough

#### Example 1:
```plaintext
Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: true
Explanation: The correct order to complete the courses is 0 → 1 → 2 → 3.
```

#### Example 2:
```plaintext
Input: numCourses = 3, prerequisites = [[0, 1], [1, 2], [2, 0]]
Output: false
Explanation: There is a cycle between courses 0, 1, and 2, so it's impossible to complete all courses.
```

---

### Summary of Approaches

| Approach                          | Time Complexity | Space Complexity | Key Idea                                                    |
|------------------------------------|-----------------|------------------|-------------------------------------------------------------|
| Topological Sort (BFS - Kahn's)    | $O(C + P)$      | $O(C + P)$       | Use in-degree to track dependencies and process zero in-degrees iteratively. |
| DFS-based Cycle Detection          | $O(C + P)$      | $O(C + P)$       | Use DFS to detect cycles by marking nodes as visited and visiting.           |

---

Let me know when you want **Section 2** with the test function and comparisons!


### Section 2: Comparison of Approaches and Test Function

#### Comparison of Approaches

| **Approach**            | **Time Complexity**        | **Space Complexity**       | **Explanation** |
|-------------------------|----------------------------|----------------------------|-----------------|
| **DFS (Depth-First Search)**    | $O(V + E)$, where $V$ is the number of courses (vertices) and $E$ is the number of prerequisites (edges). | $O(V + E)$ for storing the graph and visited states. | We visit each node and edge once during the DFS. |
| **BFS (Kahn's Algorithm)**      | $O(V + E)$ | $O(V + E)$ | Similar to DFS but processes nodes in topological order by using BFS and a queue to ensure no cycles. |
| **DFS with Cycle Detection** | $O(V + E)$ | $O(V + E)$ | A modified DFS that checks for cycles by tracking recursion stack nodes. This ensures that no courses have cyclic dependencies. |

#### Test Function

Here’s the test function to check multiple cases of the `canFinish()` function (based on both DFS and BFS implementations):

```python
from typing import List, Callable

def test_can_finish(func: Callable[[int, List[List[int]]], bool]) -> None:
    test_cases = [
        {
            "name": "Test Case 1: Simple Acyclic Graph",
            "num_courses": 2,
            "prerequisites": [[1, 0]],
            "expected": True
        },
        {
            "name": "Test Case 2: Cyclic Graph",
            "num_courses": 2,
            "prerequisites": [[1, 0], [0, 1]],
            "expected": False
        },
        {
            "name": "Test Case 3: Multiple Acyclic Dependencies",
            "num_courses": 4,
            "prerequisites": [[1, 0], [2, 1], [3, 2]],
            "expected": True
        },
        {
            "name": "Test Case 4: Larger Cyclic Dependency",
            "num_courses": 4,
            "prerequisites": [[0, 1], [1, 2], [2, 3], [3, 0]],
            "expected": False
        },
        {
            "name": "Test Case 5: No Prerequisites",
            "num_courses": 3,
            "prerequisites": [],
            "expected": True
        },
        {
            "name": "Test Case 6: Disconnected Acyclic Graph",
            "num_courses": 5,
            "prerequisites": [[1, 0], [3, 2], [4, 3]],
            "expected": True
        },
        {
            "name": "Test Case 7: Single Course",
            "num_courses": 1,
            "prerequisites": [],
            "expected": True
        },
        {
            "name": "Test Case 8: All Courses Independent",
            "num_courses": 4,
            "prerequisites": [],
            "expected": True
        },
        {
            "name": "Test Case 9: Larger Acyclic Graph",
            "num_courses": 6,
            "prerequisites": [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]],
            "expected": True
        },
        {
            "name": "Test Case 10: Larger Cyclic Graph",
            "num_courses": 6,
            "prerequisites": [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]],
            "expected": False
        },
    ]

    for case in test_cases:
        result = func(case["num_courses"], case["prerequisites"])
        assert result == case["expected"], f'{case["name"]} failed: expected {case["expected"]}, got {result}'
        print(f'{case["name"]} passed.')

# You can now pass the DFS or BFS version of canFinish to test it
# test_can_finish(canFinish_dfs)
# test_can_finish(canFinish_bfs)
```

This test function will ensure that the `canFinish` function is tested for multiple edge cases, including basic acyclic graphs, cyclic graphs, and larger dependency chains. The function accepts either the DFS or BFS implementation for `canFinish`.




----

Node: Topological Sort - directed acyclic graph

when u vertex comes before v vertex

[Topological sort - YT(InsideCode)](https://www.youtube.com/watch?v=GYmq98CVm2c)


Here’s a crisper and more structured explanation of **Topological Sort**, with additional details that might enhance understanding. I'll also break down the key components and concepts clearly:

---

### Topological Sort

**Problem Context:**
You run a YouTube channel covering algorithms and data structures. Each topic may have prerequisites, meaning you need to know the correct order to present them. For example:
- Before Dijkstra's Algorithm, you should cover **Graphs** and **Priority Queues**.
- Before **Priority Queues**, you need to discuss **Queues** and **Binary Heaps**.

This situation can be modeled as a **Directed Acyclic Graph (DAG)**, where topics are nodes, and an edge from topic A to topic B indicates that topic A is a prerequisite of topic B. The goal is to find an order in which all topics can be covered while respecting the prerequisites.

**Topological Sort** solves this problem. It orders the nodes (topics) of a DAG such that for every directed edge \( U \rightarrow V \), \( U \) comes before \( V \) in the ordering.

---

### Key Concepts

- **Directed Acyclic Graph (DAG)**: A graph that has directed edges and no cycles. A cycle means you cannot create a valid topological sort because of circular dependencies.
- **Topological Order**: A linear ordering of vertices such that for every directed edge \( U \rightarrow V \), vertex \( U \) appears before \( V \) in the ordering.

---

### Steps for Topological Sort Using Depth-First Search (DFS)

1. **Initialize**:
   - Create an empty stack to store the vertices in reverse topological order.
   - Keep track of visited nodes to avoid processing the same node multiple times.

2. **DFS Traversal**:
   - For each unvisited node, perform a **DFS**.
   - After exploring all its neighbors, push the current node onto the stack.

3. **Backtrack**:
   - During backtracking, ensure the current node is pushed only after all its prerequisites (neighbors) have been processed.

4. **Construct Ordering**:
   - Once all nodes are visited, popping from the stack gives a valid topological order.

---

### Code Implementation

```python
from typing import Dict, List, Set

# Depth-First Search helper function for topological sort
def dfs(graph: Dict[str, List[str]], vertex: str, stack: List[str], visited: Set[str]) -> None:
    visited.add(vertex)  # Mark the current node as visited
    for neighbor in graph[vertex]:  # Explore each neighbor of the current node
        if neighbor not in visited:
            dfs(graph, neighbor, stack, visited)  # Recursively perform DFS on unvisited neighbors
    stack.append(vertex)  # Once all neighbors are visited, push the node to the stack

# Topological Sort function
def topological_sort(graph: Dict[str, List[str]]) -> List[str]:
    stack = []  # Stack to store the reverse topological order
    visited = set()  # Set to keep track of visited nodes

    # Perform DFS for every unvisited vertex in the graph
    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, stack, visited)

    # Pop elements from the stack to get the topological order
    ordering = []
    while stack:
        ordering.append(stack.pop())

    return ordering

# Example Usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Running the topological sort function
order = topological_sort(graph)
print("Topological Order:", order)
```

### Explanation of the Code:

- **DFS Function**:
  - The DFS function explores all neighbors of the current node. Once all neighbors are visited, the node is pushed onto the stack.
  - This ensures that the current node is placed after all nodes it depends on.

- **Topological Sort Function**:
  - The function initializes an empty stack and visited set. It iterates through all nodes in the graph and calls the DFS function for each unvisited node.
  - After the DFS completes, popping from the stack gives the topological order.

---

### Time and Space Complexity

- **Time Complexity**: \( O(V + E) \)
  - Each vertex is processed once (through DFS), and each edge is explored once, leading to a time complexity of \( O(V + E) \), where \( V \) is the number of vertices and \( E \) is the number of edges.
  
- **Space Complexity**: \( O(V) \)
  - The algorithm requires space to store the visited set, the stack, and the call stack (in case of recursion). All of these scale linearly with the number of vertices, leading to \( O(V) \) space complexity.

---

### Key Points to Remember:

1. **Only for DAGs**: Topological sorting is only possible for Directed Acyclic Graphs. If there is a cycle, topological sort cannot be applied (because there is no valid ordering).
2. **Multiple Valid Orders**: There can be multiple valid topological orders depending on the structure of the graph. The specific order may vary depending on the starting point of the DFS.
3. **Prerequisite Tracking**: This algorithm is ideal for solving problems like course prerequisites, build systems, or any situation where you need to ensure tasks are performed in a valid order.
4. **Alternative Algorithms**: There are other algorithms for topological sort, such as **Kahn's Algorithm** (which uses in-degrees of vertices), but DFS is the most common method due to its simplicity and efficiency.

---

### Comparison with Kahn’s Algorithm

| **Approach**         | **Method**        | **Time Complexity** | **Space Complexity** | **Use Case**                    |
|----------------------|-------------------|---------------------|----------------------|----------------------------------|
| DFS-based Topological Sort | Depth-First Search | \( O(V + E) \)        | \( O(V) \)            | General, easy to implement       |
| Kahn’s Algorithm     | In-degree counting | \( O(V + E) \)        | \( O(V) \)            | When explicit in-degree tracking is needed |

---

### Conclusion

Topological sort helps in scenarios where dependencies must be respected. Whether you're managing video topics for a YouTube channel or solving a programming problem, topological sorting ensures that prerequisites are always covered before their dependent topics or tasks.




---



### Section 1: Course Schedule Problem (LeetCode #207)

[LeetCode #207 - Course Schedule](https://leetcode.com/problems/course-schedule/)

---

### Problem Statement

You are given a total of `numCourses` courses to take, labeled from `0` to `numCourses-1`. You are also given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must complete course `b` before course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

#### Constraints:
- The input `numCourses` is an integer between 1 and 2000.
- The input `prerequisites` is an array of pairs where each element is a pair `[a, b]`.
- Prerequisites contain no duplicate pairs.

#### Example 1:

```plaintext
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Explanation: You can complete course 0 first and then take course 1.
```

#### Example 2:

```plaintext
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
Explanation: There is a cycle between course 0 and course 1, so it's impossible to complete all courses.
```

---

### Approaches

#### 1. **Topological Sorting (Kahn’s Algorithm - BFS)**

**Explanation**: 
This approach is based on the concept of topological sorting, which is useful when solving dependency problems. We can think of the course schedule as a Directed Acyclic Graph (DAG). If we can perform a topological sort of all the nodes (courses), then it’s possible to complete all courses; otherwise, there’s a cycle, meaning it's impossible.

**Steps**:
1. Represent the courses and prerequisites as a directed graph.
2. Use an array `in_degree` to track the number of prerequisites (incoming edges) each course has.
3. Start with the nodes (courses) that have zero prerequisites (in-degree 0).
4. For each node, reduce the in-degree of its neighbors (courses that depend on it). If a neighbor’s in-degree becomes 0, add it to the queue.
5. If all courses are processed, return `true`; otherwise, there’s a cycle, so return `false`.

```python
from collections import deque
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Create an adjacency list and an array to store in-degrees
    adj_list = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses
    
    # Build the graph and fill in-degrees
    for course, pre in prerequisites:
        adj_list[pre].append(course)
        in_degree[course] += 1
    
    # Queue to process courses with zero prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    processed_courses = 0
    
    # Process the queue
    while queue:
        course = queue.popleft()
        processed_courses += 1
        
        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If all courses are processed, return True
    return processed_courses == numCourses
```

**Time Complexity**: 
- Constructing the adjacency list takes $O(P)$ where $P$ is the number of prerequisites.
- BFS traversal takes $O(C + P)$, where $C$ is the number of courses and $P$ is the number of prerequisites.
- **Total**: $O(C + P)$

**Space Complexity**: 
- Adjacency list takes $O(C + P)$, in-degree array takes $O(C)$.
- **Total**: $O(C + P)$

---

#### 2. **DFS-based Cycle Detection**

**Explanation**:
Another way to solve the problem is by using Depth First Search (DFS). We check for cycles in the directed graph formed by the courses. A cycle in the graph means we cannot complete all courses.

**Steps**:
1. Build a graph using an adjacency list.
2. For each unvisited course, perform a DFS to detect cycles.
3. Use a `visited` array where:
   - `0` means the node has not been visited yet.
   - `1` means the node is currently being visited (part of the current path).
   - `2` means the node has already been fully processed and doesn’t have a cycle.
4. If a cycle is detected during the DFS, return `false`; otherwise, return `true`.

```python
def canFinishDFS(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj_list = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        adj_list[pre].append(course)
    
    visited = [0] * numCourses

    def has_cycle(course: int) -> bool:
        if visited[course] == 1:  # cycle detected
            return True
        if visited[course] == 2:  # already processed node
            return False
        
        visited[course] = 1  # mark as visiting
        for neighbor in adj_list[course]:
            if has_cycle(neighbor):
                return True
        
        visited[course] = 2  # mark as processed
        return False
    
    for course in range(numCourses):
        if has_cycle(course):
            return False
    
    return True
```

**Time Complexity**:
- DFS traversal takes $O(C + P)$.
- **Total**: $O(C + P)$

**Space Complexity**:
- Adjacency list and visited array take $O(C + P)$ and $O(C)$, respectively.
- **Total**: $O(C + P)$

---

### Example Walkthrough

#### Example 1:
```plaintext
Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: true
Explanation: The correct order to complete the courses is 0 → 1 → 2 → 3.
```

#### Example 2:
```plaintext
Input: numCourses = 3, prerequisites = [[0, 1], [1, 2], [2, 0]]
Output: false
Explanation: There is a cycle between courses 0, 1, and 2, so it's impossible to complete all courses.
```

---

### Summary of Approaches

| Approach                          | Time Complexity | Space Complexity | Key Idea                                                    |
|------------------------------------|-----------------|------------------|-------------------------------------------------------------|
| Topological Sort (BFS - Kahn's)    | $O(C + P)$      | $O(C + P)$       | Use in-degree to track dependencies and process zero in-degrees iteratively. |
| DFS-based Cycle Detection          | $O(C + P)$      | $O(C + P)$       | Use DFS to detect cycles by marking nodes as visited and visiting.           |

---



to check {

https://www.geeksforgeeks.org/problems/course-schedule/1

}





