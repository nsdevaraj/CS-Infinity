
Problem: Find the Shortest Path in an Unweighted Graph
You are given an unweighted, undirected graph represented as an adjacency list. Write a function to find the shortest path from a starting node to a target node using Breadth-First Search (BFS).

Problem Statement:
Given a graph represented by an adjacency list, find the shortest path from node start to node target. Return the path as a list of nodes. If there is no path, return an empty list.



to check all solutions :

```python
type Graph = {
  [key: string]: string[]; // edge weight
};

const testCases: {
  name: string;
  graph: Graph;
  start: string;
  end: string;
  expected: string[][];
}[] = [
  {
    name: "Direct Path",
    graph: {
      A: ["B", "C"],
      B: ["D"],
      C: ["D"],
      D: [],
    },
    start: "A",
    end: "D",
    expected: [
      ["A", "B", "D"],
      ["A", "C", "D"],
    ], // two shortest paths
  },
  {
    name: "No Path",
    graph: {
      A: ["B"],
      B: [],
      C: ["D"],
      D: [],
    },
    start: "A",
    end: "C",
    expected: [], // no path exists
  },
  {
    name: "Cycle in Graph",
    graph: {
      A: ["B"],
      B: ["C"],
      C: ["A", "D"],
      D: [],
    },
    start: "A",
    end: "D",
    expected: [["A", "B", "C", "D"]], // only one shortest path
  },
  {
    name: "Self Loop",
    graph: {
      A: ["A"],
      B: [],
    },
    start: "A",
    end: "A",
    expected: [["A"]], // self-loop is a valid path
  },
  {
    name: "Graph with Isolated Node",
    graph: {
      A: ["B"],
      B: ["C"],
      C: [],
      D: [],
    },
    start: "A",
    end: "D",
    expected: [], // no path exists
  },
  {
    name: "Multiple Paths with Same Start and End",
    graph: {
      A: ["B", "C"],
      B: ["D"],
      C: ["D"],
      D: [],
    },
    start: "A",
    end: "D",
    expected: [
      ["A", "B", "D"],
      ["A", "C", "D"],
    ], // two shortest paths
  },
  {
    name: "Graph with Multiple Connections",
    graph: {
      A: ["B", "C"],
      B: ["D", "E"],
      C: ["D"],
      D: ["F"],
      E: [],
      F: [],
    },
    start: "A",
    end: "F",
    expected: [
      ["A", "B", "D", "F"],
      ["A", "C", "D", "F"],
    ], // both paths
  },
  {
    name: "Complex Graph with Multiple Shortest Paths",
    graph: {
      A: ["B", "C"],
      B: ["D"],
      C: ["D"],
      D: ["E"],
      E: [],
    },
    start: "A",
    end: "E",
    expected: [
      ["A", "B", "D", "E"],
      ["A", "C", "D", "E"],
    ], // two shortest paths
  },
  {
    name: "Long Linear Graph",
    graph: {
      A: ["B"],
      B: ["C"],
      C: ["D"],
      D: ["E"],
      E: [],
    },
    start: "A",
    end: "E",
    expected: [["A", "B", "C", "D", "E"]], // only one shortest path
  },
  {
    name: "Disconnected Graph with Multiple Components",
    graph: {
      A: ["B"],
      B: ["C"],
      C: [],
      D: ["E"],
      E: [],
    },
    start: "A",
    end: "D",
    expected: [], // no path exists
  },
  {
    name: "Graph with Parallel Edges",
    graph: {
      A: ["B", "C"],
      B: ["C"],
      C: ["D"],
      D: [],
    },
    start: "A",
    end: "D",
    expected: [
      ["A", "C", "D"],
      ["A", "B", "C", "D"],
    ], // two shortest paths
  },
  {
    name: "Cyclic Graph with Multiple Paths",
    graph: {
      A: ["B", "C"],
      B: ["C", "D"],
      C: ["A", "D"],
      D: ["E"],
      E: [],
    },
    start: "A",
    end: "E",
    expected: [
      ["A", "B", "D", "E"],
      ["A", "C", "D", "E"],
    ], // two shortest paths
  },
  {
    name: "Graph with Multiple Shortest Paths",
    graph: {
      A: ["B", "C"],
      B: ["D"],
      C: ["D", "E"],
      D: ["E"],
      E: [],
    },
    start: "A",
    end: "E",
    expected: [
      ["A", "C", "E"], // Only the shortest path
    ],
  },
  {
    name: "Long Cycle",
    graph: {
      A: ["B"],
      B: ["C"],
      C: ["D"],
      D: ["B", "E"],
      E: [],
    },
    start: "A",
    end: "E",
    expected: [
      ["A", "B", "C", "D", "E"],
      ["A", "B", "D", "E"],
    ], // two shortest paths
  },
  {
    name: "Multiple Cycles",
    graph: {
      A: ["B", "C"],
      B: ["C", "D"],
      C: ["A", "D"],
      D: ["E"],
      E: [],
    },
    start: "A",
    end: "E",
    expected: [
      ["A", "B", "D", "E"],
      ["A", "C", "D", "E"],
    ], // two shortest paths
  },
  {
    name: "Source Not Found in Graph",
    graph: {
      A: ["B"],
      B: ["C"],
      C: [],
    },
    start: "X", // Source not in graph
    end: "C",
    expected: [], // No paths since source is absent
  },
  {
    name: "Destination Not Found in Graph",
    graph: {
      A: ["B"],
      B: ["C"],
      C: [],
    },
    start: "A",
    end: "Y", // Destination not in graph
    expected: [], // No paths since destination is absent
  },
  {
    name: "Both Source and Destination Not Found in Graph",
    graph: {
      A: ["B"],
      B: ["C"],
      C: [],
    },
    start: "X", // Source not in graph
    end: "Y", // Destination not in graph
    expected: [], // No paths since both nodes are absent
  },
  {
    name: "Neighbour not in graph",
    graph: {
      A: ["B", "X", "C"], // "X" not in graph
      B: ["D"],
      C: ["D"],
      D: [],
    },
    start: "A",
    end: "D",
    expected: [
      ["A", "B", "D"],
      ["A", "C", "D"],
    ], // two shortest paths
  },
];

const runTestForFunc = (
  graphFunc: (graph: Graph, start: string, target: string) => string[][],
) => {
  console.log(`Testing func: ${graphFunc.name}`);
  testCases.forEach(({ name, graph, start, end, expected }) => {
    const paths = graphFunc(graph, start, end);
    const gotPaths = paths.map((path) => JSON.stringify(path));
    const expectedPaths = expected.map((path) => JSON.stringify(path));
    const unionSet = new Set([...gotPaths, ...expectedPaths]);
    console.assert(
      unionSet.size === expected.length,
      `Test case '${name}' failed: expected all paths ${expectedPaths}, got  ${gotPaths}`,
    );
  });
  console.log("All test cases completed!");
};

const shortestPathsOfGraph1 = (
  graph: Graph,
  start: string,
  target: string,
): string[][] => {
  if (!(start in graph) || !(target in graph)) return [];

  const queue: string[] = [start];
  const queuePaths: string[][] = [[start]];
  const visitedSet = new Set();
  const paths: string[][] = [];

  while (queue.length) {
    const current: string = queue.shift() as string;
    const currentPath: string[] = queuePaths.shift() as string[];
    // If we reached the target, store the path
    if (current == target) {
      paths.push(currentPath);
    }
    // prevent cycle
    else if (visitedSet.has(current)) {
      // do nothing
    } else {
      // no path found, then consider next level nodes,
      // else exploring current queue nodes are fine
      if (!paths.length) {
        for (let neighbour of graph[current]) {
          if (neighbour in graph) {
            // consider neighbour for exploration and have its paths ready too
            queue.push(neighbour);
            queuePaths.push(currentPath.concat(neighbour));
          }
        }
      } else {
        break;
      }
    }
  }
  /*
    sometimes the early visiting neighbour give path that maynot be shortest, so filtering shortest things here!
   */
  const minLengthPaths = Math.min(...paths.map((path) => path.length));
  return paths.filter((path) => path.length === minLengthPaths);
};

function shortestPathsOfGraph2(
  graph: Graph,
  start: string,
  end: string,
  path: string[] = [],
  visited: Set<string> = new Set(),
): string[][] {
  // Add the current node to the path and mark it as visited
  path.push(start);
  visited.add(start);

  // If the current node is the end node, return the current path
  if (start === end) {
    // Create a copy of the path to avoid mutation
    const resultPath = [...path];
    // Backtrack before returning
    path.pop();
    visited.delete(start);
    return [resultPath];
  }

  // If the current node is not in the graph, backtrack
  if (!graph[start]) {
    path.pop(); // Remove the current node before returning
    visited.delete(start); // Mark it as unvisited for other paths
    return [];
  }

  let paths: string[][] = [];

  // Explore each neighbor of the current node
  for (const neighbor of graph[start]) {
    // Only visit neighbors that haven't been visited yet
    if (!visited.has(neighbor)) {
      const newPaths = shortestPathsOfGraph2(
        graph,
        neighbor,
        end,
        [...path],
        visited,
      );
      paths = paths.concat(newPaths);
    }
  }

  // Backtrack: remove the current node from the path and unmark it as visited
  path.pop();
  visited.delete(start);
  const minLengthPaths = Math.min(...paths.map((path) => path.length));
  return paths.filter((path) => path.length === minLengthPaths);
}

function findShortestPaths3(
  graph: Graph,
  start: string,
  end: string,
): string[][] {
  // Result array to hold all the shortest paths
  const result: string[][] = [];

  // BFS to find the shortest distance to the end node
  const queue: string[] = [start];
  const distances: { [key: string]: number } = { [start]: 0 };

  while (queue.length > 0) {
    const current = queue.shift()!;
    const currentDistance = distances[current] + 1;

    for (const neighbor of graph[current] || []) {
      if (!(neighbor in distances)) {
        distances[neighbor] = currentDistance;
        queue.push(neighbor);
      }
    }
  }

  // DFS to find all the shortest paths using the distances calculated
  const dfs = (node: string, path: string[]) => {
    path.push(node);

    if (node === end) {
      result.push([...path]); // Found a path to the end node
    } else if (distances[node] === (distances[end] || Infinity)) {
      for (const neighbor of graph[node] || []) {
        if (distances[neighbor] === distances[node] + 1) {
          dfs(neighbor, path);
        }
      }
    }

    path.pop(); // Backtrack
  };

  if (start in graph && end in distances) {
    dfs(start, []);
  }

  return result;
}

const findShortestPaths4 = (
  graph: Graph,
  start: string,
  target: string,
): string[][] => {
  if (start === target) return [[start]];

  const queue = [[start]];
  const visited = new Set();
  const paths = [];
  let foundShortest = false;

  while (queue.length > 0) {
    const path = queue.shift()!;
    const node = path[path.length - 1];

    if (!visited.has(node)) {
      visited.add(node);

      for (const neighbor in graph[node]) {
        const newPath = [...path, neighbor];
        if (neighbor === target) {
          foundShortest = true;
          paths.push(newPath);
        } else if (!foundShortest) {
          queue.push(newPath);
        }
      }
    }
  }

  return paths; // return all found shortest paths
};

runTestForFunc(findShortestPaths4);

```


[[Word Ladder]]
