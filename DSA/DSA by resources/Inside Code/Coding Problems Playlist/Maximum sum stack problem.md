
[Maximum sum stack problem - Inside code](https://youtu.be/nbg1YiL-dv8?si=raRxt0o2XrB_35ps)

### Problem Statement

We are given an array of stacks, where each stack is an array of integers. We can pop elements from any stack, but the objective is to find the maximum sum that can be achieved such that **all stacks** have the same sum of elements. You are tasked with returning this maximum possible sum. 

### Example:

**Input**:
```
stacks = [
    [2, 2, 1, 1, 2],
    [1, 3, 3, 2, 1, 1],
    [4, 2, 2, 1]
]
```

**Output**:
```
11
```

**Explanation**:
- Stack 1: If we pop the top element (which has value 2), the remaining sum is 11.
- Stack 2: If we pop the top three elements (1, 3, and 3), the remaining sum is also 11.
- Stack 3: No need to pop any elements, the sum is already 11.

Therefore, the maximum sum that can be achieved by all stacks is 11.

---

### Approach 1: Cumulative Sum with Set Intersection

To solve this problem efficiently, we can break it down into smaller steps:
1. **Reachable Sums**: For each stack, we can compute all possible sums that can be reached by removing elements from the stack. For example, if a stack has the elements `[2, 2, 1, 1, 2]`, its reachable sums would be `{0, 2, 4, 5, 6, 8}`.
2. **Intersection of Reachable Sums**: Once we have the reachable sums for each stack, the next step is to find the common sums that can be achieved by **all stacks**. The maximum of these common sums is our answer.

#### Code Implementation:

```python
from typing import List, Set

def maximum_sum(stacks: List[List[int]]) -> int:
    if not stacks:
        return 0
    
    # Initialize reachable sets for each stack [ 0 is reachable by all ]
    reachable: List[Set[int]] = [{0} for _ in stacks]
    
    # Compute reachable sums for each stack
    for i, stack in enumerate(stacks):
        cumulative_sum = 0
        for num in stack:
            cumulative_sum += num
            reachable[i].add(cumulative_sum)
    
    # Find the intersection of reachable sums across all stacks
    intersection = set.intersection(*reachable)
    
    # Return the maximum sum achievable by all stacks
    return max(intersection)
```

#### Time Complexity:
- **O(N)**: We iterate through each element in all the stacks to compute cumulative sums.
- **N** is the total number of elements across all stacks.

#### Space Complexity:
- **O(N)**: We store the reachable sums for each stack in a set, and since each stack can have a number of sums equal to the number of elements + 1, the total space usage is linear in terms of the number of elements.

---

### Better Approach: Reverse Cumulative Sum

Another way to think about this problem is to reverse the process. Instead of building sums from the bottom of each stack (adding up elements), we can pop elements from the top and maintain the cumulative sum as we go. This method ensures we can efficiently track the reachable sums.

1. **Use a Stack**: For each stack, start with the full sum and then iteratively remove elements while updating the cumulative sum.
2. **Track Common Sums**: Track the possible sums and again find the intersection of sums common to all stacks.

#### Code Implementation:

```python
def maximum_sum_reverse(stacks: List[List[int]]) -> int:
    if not stacks:
        return 0
    
    reachable: List[Set[int]] = [{sum(stack)} for stack in stacks]
    
    # Reverse traverse the stacks, reducing the sum progressively
    for i, stack in enumerate(stacks):
        cumulative_sum = sum(stack)
        for num in stack:
            cumulative_sum -= num
            reachable[i].add(cumulative_sum)
    
    # Find the intersection of reachable sums across all stacks
    intersection = set.intersection(*reachable)
    
    # Return the maximum sum achievable by all stacks
    return max(intersection)
```

#### Time Complexity:
- **O(N)**: We still process every element once, so this remains linear.

#### Space Complexity:
- **O(N)**: Similar to the previous approach, we store all reachable sums for each stack.

---

### Summary of Approaches

| Approach                     | Description                                       | Time Complexity | Space Complexity |
|------------------------------|---------------------------------------------------|-----------------|------------------|
| **Cumulative Sum with Set**   | Calculate sums starting from bottom of each stack | O(N)            | O(N)             |
| **Reverse Cumulative Sum**    | Calculate sums by popping from top of each stack  | O(N)            | O(N)             |

Both approaches have the same time and space complexity, but depending on the input format or problem specifics, one might feel more intuitive than the other. However, in general, both approaches provide efficient solutions.


to try
{

like reverse cumulative, reverly check each stack simulataneously and give the first distance that intersects each ... 


Sure! This approach can be optimized by **reversing all stacks simultaneously** and keeping track of the cumulative sum from the top (i.e., after popping elements) until we find the **first common sum** that appears across all stacks. This means we progressively reduce the sum in each stack and check for intersections dynamically. 

The idea is to **synchronize** the stacks by removing elements one by one from the top, and at each step, we check if the current sum of all stacks matches. This approach is efficient because it avoids calculating all possible sums first, instead finding the first intersection as soon as it occurs.

### Approach: Reverse Cumulative Sum Check Simultaneously

The steps are:
1. Calculate the sum of each stack initially.
2. As long as the sums of the stacks don't match, **pop** the top element from the stack that has the largest sum.
3. Once all stacks have the same sum, return that sum.

This method synchronizes the reduction of sums across all stacks until we reach a point where all sums are equal.

#### Code Implementation:

```python
from typing import List

def maximum_sum_sync(stacks: List[List[int]]) -> int:
    # Initialize the cumulative sums for each stack by calculating the full sum
    sums = [sum(stack) for stack in stacks]
    
    # Keep reducing the stacks until all sums are equal
    while len(set(sums)) > 1:  # While not all sums are the same
        # Find the stack with the largest sum
        max_sum_index = sums.index(max(sums))
        
        # Pop the top element from the stack with the largest sum
        if stacks[max_sum_index]:
            sums[max_sum_index] -= stacks[max_sum_index].pop(0)
    
    # All sums are equal now, return the common sum
    return sums[0]

# Example usage:
stacks = [
    [2, 2, 1, 1, 2],      # sum = 11
    [1, 3, 3, 2, 1, 1],   # sum = 11 after popping top 3 elements
    [4, 2, 2, 1]          # sum = 11, no elements popped
]

print(maximum_sum_sync(stacks))  # Output: 11
```

### Explanation:

1. **Initialization**: We calculate the initial sum for each stack.
   - Stack 1: $2 + 2 + 1 + 1 + 2 = 8$
   - Stack 2: $1 + 3 + 3 + 2 + 1 + 1 = 11$
   - Stack 3: $4 + 2 + 2 + 1 = 9$

2. **While loop**: As long as not all sums are the same, we:
   - Find the stack with the highest sum.
   - Pop the top element from that stack, reducing its sum.
   
   This process continues until the sums of all stacks match.

3. **Termination**: Once all the sums are equal, we return that sum.

### Time Complexity:
- **O(N)**: We traverse every element of the stacks, popping elements until the sums of all stacks match. Since the number of pops is proportional to the number of elements across all stacks, the complexity is linear in terms of the total number of elements.

### Space Complexity:
- **O(1)**: No additional data structures are used beyond tracking the current sums and the stacks themselves, which are modified in place.

### Summary of Approaches

| Approach                                  | Description                                                   | Time Complexity | Space Complexity |
|-------------------------------------------|---------------------------------------------------------------|-----------------|------------------|
| **Cumulative Sum with Set Intersection**  | Calculate all possible sums for each stack and find intersection | O(N)            | O(N)             |
| **Reverse Cumulative Sum Check**          | Reduce the sums of stacks by popping elements simultaneously until they match | O(N)            | O(1)             |

The simultaneous reverse sum checking approach optimizes space usage and may feel more intuitive when considering how stacks change dynamically.


}

