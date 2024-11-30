

### Problem Statement: Shortest Path in a Graph

**Description:**
Given a weighted or unweighted graph, find the shortest path between two vertices. The graph may be directed or undirected. The shortest path is defined as the path that minimizes the total weight of the edges traveled.

**Input:**
- A graph represented as an adjacency list or adjacency matrix.
- Two vertices \(u\) and \(v\) for which the shortest path needs to be found.

**Output:**
- The length of the shortest path between the two vertices.
- The actual path taken, if required.

**Constraints:**
- The graph may contain cycles.
- The graph may be disconnected; if no path exists, return an indication (e.g., `null` or `Infinity`).
- The number of vertices \(V\) and edges \(E\) must be within reasonable limits (e.g., \(1 ≤ V ≤ 10^5\) and \(1 ≤ E ≤ 10^6\)).

### Example 1: Unweighted Graph

**Input:**
- Graph: 
```
   A -- B
   |    |
   C -- D
```
- Edges: `A-B`, `A-C`, `B-D`, `C-D`
- Start vertex: `A`
- End vertex: `D`

**Output:**
- Shortest Path Length: `2`
- Path: `A -> B -> D` or `A -> C -> D`

---

### Example 2: Weighted Graph

**Input:**
- Graph: 
```
   (1)
 A ---- B
 | \    |
(4)| (2)| (3)
 |   \  |
 C ---- D
```
- Edges: `A-B (1)`, `A-C (4)`, `B-D (2)`, `C-D (3)`
- Start vertex: `A`
- End vertex: `D`

**Output:**
- Shortest Path Length: `3`
- Path: `A -> B -> D`

---

### Example 3: Disconnected Graph

**Input:**
- Graph: 
```
   A -- B

   C -- D
```
- Edges: `A-B`, `C-D`
- Start vertex: `A`
- End vertex: `C`

**Output:**
- Shortest Path Length: `Infinity`
- Path: `null` (no path exists)

---

### Example 4: Graph with Negative Weights (Using Bellman-Ford)

**Input:**
- Graph: 
```
   A -- B
   |   /
 (2) (3)
   | /
   C
   |
 (5)
   |
   D
```
- Edges: `A-B (1)`, `A-C (2)`, `B-C (3)`, `C-D (5)`
- Start vertex: `A`
- End vertex: `D`

**Output:**
- Shortest Path Length: `7`
- Path: `A -> C -> D`

---

### Notes:
- For unweighted graphs, Breadth-First Search (BFS) can be used.
- For weighted graphs, Dijkstra's algorithm is suitable, but it requires non-negative weights.
- For graphs with negative weights, the Bellman-Ford algorithm can be used.
- If the graph is directed, indicate the direction in the adjacency representation. 

This problem is fundamental in computer science and has applications in routing, navigation systems, and network design.




## Soln

```ts
// by DFS
const shortPathFromSrcToDest1 = (
  graph: Graph,
  src: string,
  dest: string,
  needPathWeight: boolean = false,
): string[] | null | [string[] | null, number | null] => {
  if (src == dest) return needPathWeight ? [[], 0] : [];

  const pathsFromSrc = graph[src];
  const interNodeKeys = Object.keys(pathsFromSrc).filter(
    (node) => node !== src,
  );

  if (interNodeKeys.includes(dest)) {
    return needPathWeight ? [[src, dest], pathsFromSrc[dest]] : [src, dest];
  } else {
    let minPath: string[] | null = null;
    let minWeight: number | null = null;

    interNodeKeys.forEach((interNode) => {
      const [interPath, interPathWeight] = shortPathFromSrcToDest1(
        graph,
        interNode,
        dest,
        true,
      ) as [string[] | null, number | null];

      if (interPath !== null && interPathWeight !== null) {
        if (!minPath || !minWeight || minWeight > interPathWeight) {
          minPath = interPath;
          minWeight = interPathWeight;
        }
      }
    });

    if (minPath !== null && minWeight !== null) {
      const fullPath = [src, ...minPath];
      const fullPathWeight = pathsFromSrc[minPath[0]] + minWeight;
      return needPathWeight ? [fullPath, fullPathWeight] : fullPath;
    } else {
      return needPathWeight ? [null, null] : null;
    }
  }
};

```



## Types of graph

The types of graphs can be classified based on various characteristics. Here are some of the common types:

### 1. **Directed vs. Undirected Graphs**
- **Directed Graph (Digraph):** A graph where edges have a direction. Each edge is an ordered pair of vertices (e.g., \(A \to B\)).
- **Undirected Graph:** A graph where edges do not have a direction. The edge \(A-B\) implies a connection from \(A\) to \(B\) and vice versa.

### 2. **Weighted vs. Unweighted Graphs**
- **Weighted Graph:** A graph where edges have weights (costs, distances, etc.). Each edge is associated with a numerical value.
- **Unweighted Graph:** A graph where all edges are treated equally, with no weights.

### 3. **Cyclic vs. Acyclic Graphs**
- **Cyclic Graph:** A graph that contains at least one cycle (a path where the starting and ending vertices are the same).
- **Acyclic Graph:** A graph that does not contain any cycles. 

### 4. **Connected vs. Disconnected Graphs**
- **Connected Graph:** In an undirected graph, there is a path between every pair of vertices.
- **Disconnected Graph:** A graph where at least two vertices do not have a path connecting them.

### 5. **Complete Graph**
- A graph in which every pair of vertices is connected by a unique edge. In a complete graph with \(n\) vertices, there are \(\frac{n(n-1)}{2}\) edges.

### 6. **Tree**
- A special type of acyclic graph that is connected and has \(n-1\) edges, where \(n\) is the number of vertices. Trees have a hierarchical structure.

### 7. **Forest**
- A disjoint set of trees. It is an acyclic graph that can consist of one or more trees.

### 8. **Bipartite Graph**
- A graph whose vertices can be divided into two disjoint sets such that no two graph vertices within the same set are adjacent.

### 9. **Planar Graph**
- A graph that can be drawn on a plane without any edges crossing.

### 10. **Multigraph**
- A graph that can have multiple edges connecting the same pair of vertices.

### Conclusion
When discussing graphs in algorithms (like shortest path algorithms), it’s important to know the type of graph you're working with, as it influences the choice of algorithms and data structures used for graph traversal and pathfinding. For example, Dijkstra’s algorithm works on graphs with non-negative weights, while the Bellman-Ford algorithm can handle graphs with negative weights.




#### test

```ts
type Graph = {
  [key: string]: {
    [key: string]: number; // edge weight
  };
};

const testCases = [
  {
    name: "Unweighted Graph with Direct Path",
    graph: {
      A: { B: 1, C: 1 },
      B: { D: 1 },
      C: { D: 1 },
      D: {},
    },
    start: "A",
    end: "D",
    expected: ["A", "B", "D"],
  },
  {
    name: "Weighted Graph with Direct Path",
    graph: {
      A: { B: 1, C: 4 },
      B: { D: 2 },
      C: { D: 3 },
      D: {},
    },
    start: "A",
    end: "D",
    expected: ["A", "B", "D"],
  },
  {
    name: "Disconnected Graph",
    graph: {
      A: { B: 1 },
      B: {},
      C: { D: 1 },
      D: {},
    },
    start: "A",
    end: "C",
    expected: null,
  },
  {
    name: "Graph with Negative Weights",
    graph: {
      A: { B: 1, C: 2 },
      B: { D: 3 },
      C: { D: -1 },
      D: {},
    },
    start: "A",
    end: "D",
    expected: ["A", "C", "D"],
  },
  {
    name: "Cycle in Graph",
    graph: {
      A: { B: 1 },
      B: { C: 1 },
      C: { A: 1, D: 1 },
      D: {},
    },
    start: "A",
    end: "D",
    expected: ["A", "B", "C", "D"],
  },
  {
    name: "Single Node Graph",
    graph: {
      A: {},
    },
    start: "A",
    end: "A",
    expected: [],
  },
  {
    name: "Multiple Paths with Different Weights",
    graph: {
      A: { B: 2, C: 1 },
      B: { D: 1 },
      C: { D: 5 },
      D: {},
    },
    start: "A",
    end: "D",
    expected: ["A", "B", "D"],
  },
  {
    name: "Multiple Paths with Same Start and End",
    graph: {
      A: { B: 1, C: 2 },
      B: { D: 2 },
      C: { D: 1 },
      D: {},
    },
    start: "A",
    end: "D",
    expected: ["A", "C", "D"],
  },
  {
    name: "Long Path with Multiple Nodes",
    graph: {
      A: { B: 2 },
      B: { C: 2 },
      C: { D: 2 },
      D: { E: 2 },
      E: {},
    },
    start: "A",
    end: "E",
    expected: ["A", "B", "C", "D", "E"],
  },
  {
    name: "Graph with All Nodes Connected",
    graph: {
      A: { B: 1, C: 1 },
      B: { D: 1 },
      C: { D: 1 },
      D: { E: 1 },
      E: { F: 1 },
      F: {},
    },
    start: "A",
    end: "F",
    expected: ["A", "B", "D", "E", "F"], // or A -> C -> D -> E -> F
  },
  {
    name: "Graph with Isolated Node",
    graph: {
      A: { B: 1 },
      B: { C: 1 },
      C: {},
      D: {},
    },
    start: "A",
    end: "D",
    expected: null,
  },
];

const runTestForFunc = (graphFunc: Function) => {
  console.log(`Testing func: ${graphFunc.name}`);
  testCases.forEach(({ name, graph, start, end, expected }) => {
    const path = graphFunc(graph, start, end);
    console.assert(
      JSON.stringify(path) === JSON.stringify(expected),
      `Test case '${name}' failed: expected ${JSON.stringify(expected)}, got ${JSON.stringify(path)}`,
    );
  });
  console.log("All test cases completed!");
};

```
