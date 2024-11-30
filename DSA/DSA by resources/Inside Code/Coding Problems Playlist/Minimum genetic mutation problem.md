
[Minimum genetic mutation problem - Inside code](https://youtu.be/wIsJ6G5qXkI?si=p3UjpN8O9FMVZqCx)

[LeetCode #433](https://leetcode.com/problems/minimum-genetic-mutation/description/)



### Problem Statement: Minimum Genetic Mutation (LeetCode #433)

We define a gene as an 8-character string where each character can be one of `'A'`, `'C'`, `'G'`, or `'T'`.

Given a `start` gene and a target `end` gene, your task is to determine the minimum number of mutations required to transform the `start` gene into the `end` gene. Each mutation is a change of one character in the gene. However, you can only mutate the gene to valid genes that are provided in a list `bank`. If it’s not possible to reach the `end` gene, return `-1`.

#### Example:
**Input:**
```
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
```

**Output:** 
```
2
```

**Explanation:**  
You can reach the `end` gene in 2 mutations:
1. Change the last `T` to `A`, which results in `"AACCGGTA"`.
2. Change the third `C` to `A`, which results in `"AAACGGTA"`.

### Approach 1: Breadth-First Search (BFS)

This problem can be modeled as a graph traversal, where each valid gene is a node and an edge exists between two nodes if you can mutate one gene to the other with one valid mutation. BFS is used here because we need the minimum number of mutations, which corresponds to finding the shortest path in an unweighted graph.

#### Approach Breakdown:
- Start by enqueuing the `start` gene with 0 mutations.
- At each step, attempt all 32 possible mutations (since 8 positions can mutate to 4 letters), but only consider mutations that exist in the `bank` and have not been visited before.
- If we reach the `end` gene, return the number of mutations. If the queue is exhausted without finding a solution, return `-1`.

#### Code Implementation:

```python
from queue import Queue
from typing import List, Tuple

def min_mutation(start: str, end: str, bank: List[str]) -> int:
    bank_set = set(bank)  # To optimize the lookup in bank
    if end not in bank_set:
        return -1

    queue = Queue()
    queue.put((start, 0))  # (gene, number of mutations)
    visited = {start}  # Track visited genes to avoid cycles

    while not queue.empty():
        gene, mutations = queue.get()
        
        # If we've reached the target gene, return the number of mutations
        if gene == end:
            return mutations
        
        # Explore all possible mutations
        for i in range(len(gene)):
            for letter in 'ACGT':
                # Mutate the current gene at position i
                mutated_gene = gene[:i] + letter + gene[i+1:]
                
                # Only enqueue if it's a valid and unvisited gene
                if mutated_gene not in visited and mutated_gene in bank_set:
                    queue.put((mutated_gene, mutations + 1))
                    visited.add(mutated_gene)

    return -1  # If no solution is found
```

**Time Complexity:**
- The BFS will explore all valid mutations. In the worst case, for each gene of length 8, there are 32 possible mutations ($8 \times 4$). 
- If there are $n$ genes in the bank, then the complexity is $O(n \times 32)$ or $O(n)$ since $32$ is a constant.

**Space Complexity:**
- The space complexity is $O(n)$ to store the queue and the set of visited genes.

### Approach 2: Bidirectional BFS

To optimize the BFS further, we can apply bidirectional BFS. Instead of searching from the `start` gene only, we can search simultaneously from both the `start` and the `end` gene, meeting in the middle. This reduces the number of states we need to explore, effectively cutting the search space in half.

#### Code Implementation:

```python
from typing import List, Set

def bidirectional_min_mutation(start: str, end: str, bank: List[str]) -> int:
    bank_set = set(bank)
    if end not in bank_set:
        return -1

    # Two sets to hold the frontiers of BFS from both directions
    start_set, end_set = {start}, {end}
    visited = {start, end}
    mutations = 0

    while start_set and end_set:
        # Always expand the smaller frontier for efficiency
        if len(start_set) > len(end_set):
            start_set, end_set = end_set, start_set

        next_set = set()
        for gene in start_set:
            for i in range(len(gene)):
                for letter in 'ACGT':
                    mutated_gene = gene[:i] + letter + gene[i+1:]

                    if mutated_gene in end_set:
                        return mutations + 1

                    if mutated_gene not in visited and mutated_gene in bank_set:
                        next_set.add(mutated_gene)
                        visited.add(mutated_gene)
        
        start_set = next_set
        mutations += 1

    return -1
```

**Time Complexity:**
- The time complexity for bidirectional BFS is $O(\sqrt{n})$, where $n$ is the number of genes in the bank. This is because bidirectional BFS reduces the search space exponentially compared to a unidirectional BFS.

**Space Complexity:**
- The space complexity is $O(n)$ since we maintain two sets for each frontier and a set of visited genes.

### Summary of Approaches

| Approach               | Time Complexity        | Space Complexity       | Key Points                                                                 |
|------------------------|------------------------|------------------------|----------------------------------------------------------------------------|
| BFS                    | $O(n)$                 | $O(n)$                 | Simple to implement, explores all valid mutations.                         |
| Bidirectional BFS       | $O(\sqrt{n})$          | $O(n)$                 | Faster than BFS as it reduces the search space by exploring from both ends. |

In conclusion, the BFS approach solves the problem efficiently, but the bidirectional BFS is an even better optimization for larger inputs, cutting the search space down by exploring from both `start` and `end`.





