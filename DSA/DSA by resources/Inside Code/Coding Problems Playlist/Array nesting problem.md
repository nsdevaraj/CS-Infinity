

[Array nesting problem (LeetCode #565) - Inside code](https://youtu.be/Z5Xm7urgTIg?si=vDszwSri1DSVllgc)



### Problem Statement

Given an array `nums` of `n` elements representing a permutation of integers from `0` to `n-1`, our goal is to find the longest sequence where each element is determined by `nums[nums[k]]` starting from any element, and continuing until we loop back to the starting point.

#### Example:
For `nums = [5, 4, 0, 3, 1, 6, 2]`, starting from index `0`, we get the sequence `5 -> 6 -> 2 -> 0`, which has a length of `4`. This is the longest sequence.

---

### Brute Force Solution

In this approach, we:
1. Start from each element in `nums`.
2. Follow the sequence until returning to the starting element.
3. Track the longest sequence encountered.

#### Code:
```python
def arrayNesting(nums):
    maxlen = 0
    # Start from each element in the array
    for i in range(len(nums)):
        length, ptr = 0, i
        # Follow the sequence until we return to the starting point
        while ptr != i or length == 0:
            length += 1
            ptr = nums[ptr]
        # Keep track of the maximum sequence length encountered
        maxlen = max(maxlen, length)
    return maxlen

```

#### Complexity:
- **Time:** O(n²) — For each element, we trace a sequence that could potentially touch all `n` elements.
- **Space:** O(1) — No extra memory is used.

---

### Optimized Solution

Since starting from the same set of elements always gives the same sequence, we can avoid redundant computations by:
1. Using a `visited` set to track processed elements.
2. Skipping elements that are already visited to prevent recalculating their sequences.

#### Code:
```python
def arrayNesting(nums):
    maxlen = 0
    visited = set()
    # Iterate through each element in the array
    for i in range(len(nums)):
        # Skip elements already processed in a previous sequence
        if nums[i] not in visited:
            length, ptr = 0, nums[i]
            # Traverse the sequence starting from the current element
            while ptr not in visited:
                visited.add(ptr)  # Mark element as visited
                ptr = nums[ptr]   # Move to the next element in the sequence
                length += 1       # Increment sequence length
            # Update the maximum sequence length
            maxlen = max(maxlen, length)
    return maxlen

```

#### Complexity:
- **Time:** O(n) — Each element is processed only once.
- **Space:** O(n) — Due to the `visited` set.

---

### Graph Representation

The problem can also be viewed as a directed graph, where each element `i` points to `nums[i]`. Each sequence corresponds to a cycle in this graph. Since each node has exactly one outgoing edge, we can traverse the sequences efficiently without recursion.

---

### Further Optimization (In-place)

To improve space efficiency, we can modify the `nums` array itself to track visited elements. By marking visited elements as `-1` (or any invalid value), we avoid using extra space for a `visited` set.

#### Code:
```python
def arrayNesting(nums):
    maxlen = 0
    # Iterate through each element in the array
    for i in range(len(nums)):
        # Only process elements that haven't been visited (i.e., not marked as -1)
        if nums[i] != -1:
            length, ptr = 0, i
            # Traverse the sequence starting from the current element
            while nums[ptr] != -1:
                temp = nums[ptr]  # Store current value for the next step
                nums[ptr] = -1    # Mark the element as visited by setting it to -1
                ptr = temp        # Move to the next element in the sequence
                length += 1       # Increment sequence length
            # Update the maximum sequence length
            maxlen = max(maxlen, length)
    return maxlen

```

#### Complexity:
- **Time:** O(n) — Each element is visited once.
- **Space:** O(1) — The input array is modified in place, so no additional space is required.

---

### Summary of Approaches

- **Brute Force:** O(n²) time, O(1) space — inefficient due to redundant calculations.
- **Optimized with Visited Set:** O(n) time, O(n) space — avoids recalculating sequences, but uses extra space.
- **Graph Representation:** Conceptual — helps visualize the sequences as cycles in a directed graph.
- **In-place Modification (Best):** O(n) time, O(1) space — modifies the input array to track visited elements, achieving the best efficiency.

---

### Conclusion

The problem of finding the longest sequence in the array can be solved optimally by modifying the input array in place, resulting in O(n) time and O(1) space complexity. Starting with brute force helps build intuition, but focusing on avoiding redundant work and optimizing memory usage leads to the most efficient solution.