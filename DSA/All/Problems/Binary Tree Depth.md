
[LeetCode - Max Binary Tree Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)


## Problem Statement: Maximum Depth of a Binary Tree

Given a binary tree, write a function to find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Input:**
- A binary tree represented by its root node.

**Output:**
- An integer representing the maximum depth of the tree.


## Soln

**recursive soln is easier

### Recursion

```ts
// by recursion
// Time - O(n) - going through all nodes in tree
// Space - O(h) - recursive stack upto height of tree [skewed tree h = n]
const getMaxDepth1 = (treeHead: BinaryTreeNode | null): number => {
  if (!treeHead) return 0;
  return (
    1 + Math.max(getMaxDepth1(treeHead.left), getMaxDepth1(treeHead.right))
  );
};

```


### Iteration

```ts

// by iteration
// Time -  O(n) - going through all nodes in tree
// Space - O(h) - stack upto height of tree [skewed tree h = n]
const getMaxDepth2 = (treeHead: BinaryTreeNode | null): number => {
  if (!treeHead) return 0;
  const [stack, stackDepth] = [[treeHead], [1]];
  let maxDepth: number = -Infinity;
  while (stack.length && stackDepth.length) {
    const topElementWithDepth: [BinaryTreeNode, number] = [
      stack.pop() as BinaryTreeNode,
      stackDepth.pop() as number,
    ];
    const [topElement, topElementDepth] = topElementWithDepth;
    const [leftElement, rightElement] = [topElement.left, topElement.right];
    let noChildren = true;
    if (leftElement) {
      stack.push(leftElement);
      stackDepth.push(topElementDepth + 1);
      noChildren = false;
    }

    if (rightElement) {
      stack.push(rightElement);
      stackDepth.push(topElementDepth + 1);
      noChildren = false;
    }

    if (noChildren) {
      maxDepth = Math.max(maxDepth, topElementDepth);
    }
  }

  return maxDepth;
};

```



## Refs

by chatGPT

Finding the height of a binary tree can be accomplished using different approaches in JavaScript. Here are three common methods: recursive, iterative (using a queue), and using depth-first search (DFS) with a stack.

### 1. Recursive Approach

The most straightforward method is to use recursion. The height of a binary tree is defined as the number of edges in the longest path from the root to a leaf node.

```javascript
class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function heightOfBinaryTree(root) {
    if (root === null) {
        return -1; // Return -1 for height of an empty tree
    }
    const leftHeight = heightOfBinaryTree(root.left);
    const rightHeight = heightOfBinaryTree(root.right);
    return Math.max(leftHeight, rightHeight) + 1;
}
```

### 2. Iterative Approach (Using Queue)

You can also find the height of a binary tree using an iterative approach with a queue. This is helpful when you want to avoid recursion.

```javascript
function heightOfBinaryTreeIterative(root) {
    if (root === null) return -1;

    let queue = [root];
    let height = -1;

    while (queue.length > 0) {
        let levelSize = queue.length;
        height++;

        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
    }

    return height;
}
```

### 3. Depth-First Search (DFS) Using Stack

Another method is to use a depth-first search approach with an explicit stack. This method allows you to track the height as you traverse the tree.

```javascript
function heightOfBinaryTreeDFS(root) {
    if (root === null) return -1;

    const stack = [{ node: root, depth: 0 }];
    let maxHeight = -1;

    while (stack.length > 0) {
        const { node, depth } = stack.pop();
        if (node) {
            maxHeight = Math.max(maxHeight, depth);
            stack.push({ node: node.left, depth: depth + 1 });
            stack.push({ node: node.right, depth: depth + 1 });
        }
    }

    return maxHeight;
}
```

### Summary

- **Recursive Approach**: Simple and elegant, but can lead to stack overflow for very deep trees.
- **Iterative Approach**: Avoids recursion and uses a queue to traverse levels.
- **DFS Using Stack**: An explicit stack simulates recursion, which is useful for deeper trees without the risk of stack overflow.

You can choose any of these methods based on your preferences and the specific requirements of your application!


## Others
### Test

```ts
class BinaryTreeNode {
  val: number;
  left: BinaryTreeNode | null;
  right: BinaryTreeNode | null;
  constructor(val: number) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const MAX_DEPTH_TEST_CASES = [
  {
    name: "Empty Tree",
    input: null,
    expected: 0,
    reason: "An empty tree has no nodes, so its depth is 0.",
  },
  {
    name: "Single Node",
    input: { val: 1, left: null, right: null },
    expected: 1,
    reason: "A tree with a single node has a depth of 1.",
  },
  {
    name: "Two Levels",
    input: {
      val: 1,
      left: { val: 2, left: null, right: null },
      right: { val: 3, left: null, right: null },
    },
    expected: 2,
    reason:
      "The longest path from the root (1) to a leaf (2 or 3) has 2 nodes.",
  },
  {
    name: "Three Levels - Balanced",
    input: {
      val: 1,
      left: {
        val: 2,
        left: { val: 4, left: null, right: null },
        right: { val: 5, left: null, right: null },
      },
      right: {
        val: 3,
        left: { val: 6, left: null, right: null },
        right: { val: 7, left: null, right: null },
      },
    },
    expected: 3,
    reason: "All leaf nodes (4, 5, 6, 7) are at the same level, which is 3.",
  },
  {
    name: "Three Levels - Unbalanced",
    input: {
      val: 1,
      left: {
        val: 2,
        left: {
          val: 3,
          left: null,
          right: null,
        },
        right: null,
      },
      right: null,
    },
    expected: 3,
    reason: "The longest path is from 1 to 2 to 3, totaling 3 nodes.",
  },
  {
    name: "Mixed Depths",
    input: {
      val: 1,
      left: {
        val: 2,
        left: { val: 4, left: null, right: null },
        right: null,
      },
      right: {
        val: 3,
        left: {
          val: 5,
          left: { val: 6, left: null, right: null },
          right: null,
        },
        right: null,
      },
    },
    expected: 4,
    reason: "The longest path is from 1 to 3 to 5 to 6, totaling 4 nodes.",
  },
  {
    name: "Full Tree",
    input: {
      val: 1,
      left: {
        val: 2,
        left: { val: 4, left: null, right: null },
        right: { val: 5, left: null, right: null },
      },
      right: {
        val: 3,
        left: { val: 6, left: null, right: null },
        right: { val: 7, left: null, right: null },
      },
    },
    expected: 3,
    reason: "All leaf nodes are at level 3, which is the maximum depth.",
  },
  {
    name: "Skewed Right",
    input: {
      val: 1,
      left: null,
      right: {
        val: 2,
        left: null,
        right: {
          val: 3,
          left: null,
          right: null,
        },
      },
    },
    expected: 3,
    reason: "The longest path is from 1 to 2 to 3, totaling 3 nodes.",
  },
  {
    name: "Complex Mixed Structure",
    input: {
      val: 1,
      left: {
        val: 2,
        left: {
          val: 4,
          left: null,
          right: {
            val: 8,
            left: null,
            right: null,
          },
        },
        right: null,
      },
      right: {
        val: 3,
        left: null,
        right: {
          val: 5,
          left: { val: 6, left: null, right: null },
          right: null,
        },
      },
    },
    expected: 4,
    reason: "The longest path is from 1 to 2 to 4 to 8, totaling 4 nodes.",
  },
];

const testMaxDepthFunc = (func: Function) => {
  for (const testCase of MAX_DEPTH_TEST_CASES) {
    const funcOutput = func(testCase.input);
    console.assert(
      funcOutput === testCase.expected,
      `Test case '${testCase.name}' failed: expected ${testCase.expected}, but got ${funcOutput}`,
    );
  }

  console.log("All test cases completed!");
};


```