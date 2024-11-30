

Subset / Power Set


To solve the problem of generating all possible subsets of an array of unique elements, we can use a **backtracking** approach or an **iterative** approach.

In this explanation, I'll provide a backtracking solution, which explores every possible subset by either including or excluding each element.

### Problem Statement:

Given an integer array `nums` of unique elements, return **all possible subsets** (the power set).

- The solution set **must not contain duplicate subsets**.
- You can return the subsets in any order.

### Example:

#### Input:
```python
nums = [1, 2, 3]
```

#### Output:
```python
[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

### Approach: Backtracking

1. **Subsets**: For each element in the array, we decide whether to include it in the current subset or exclude it. This results in all possible subsets of the array.
2. **Backtracking**: We recursively generate subsets by adding elements one by one, and backtrack after including or excluding an element to explore all possibilities.
3. **Base Case**: When we reach the end of the array, the current subset is considered complete, and it is added to the list of solutions.

### Code Implementation:

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all possible subsets of the given array `nums` using backtracking.
    
    Args:
        nums (List[int]): A list of unique integers.
    
    Returns:
        List[List[int]]: A list containing all possible subsets.
    """
    
    def backtrack(start: int, current_subset: List[int]):
        # Add the current subset to the result (deep copy)
        results.append(current_subset.copy())
        
        # Try adding each element starting from 'start' to the subset
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current_subset.append(nums[i])
            
            # Recurse and explore further with the current element included
            backtrack(i + 1, current_subset)
            
            # Backtrack by removing the last element to explore other subsets
            current_subset.pop()
    
    results = []  # To store all subsets
    backtrack(0, [])  # Start backtracking with an empty subset
    return results
```

### Explanation:

1. **`subsets(nums)`**:
   - This is the main function that initializes the backtracking process and returns all possible subsets.
   
2. **`backtrack(start, current_subset)`**:
   - **`start`**: The starting index for considering elements in the `nums` array.
   - **`current_subset`**: The current subset being constructed.
   - This function adds the current subset to the result list, then recursively explores all possibilities by adding elements one by one and backtracking to explore other combinations.

3. **Base Case**:
   - We add the current subset to the `results` list at the start of each call, and then recursively build further subsets by including elements from index `start` onwards.
   
4. **Backtracking**:
   - After including an element, we explore all possible subsets that include it.
   - We then **remove** the element to explore other subsets that don't include it (this is the backtracking step).

### Example Usage:

```python
nums = [1, 2, 3]
print(subsets(nums)```

### Output:

```python
[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

### Time Complexity:
- The time complexity is **O(2^n)** where `n` is the length of the array `nums`. This is because there are `2^n` possible subsets (each element can either be included or excluded in a subset).

### Space Complexity:
- The space complexity is **O(n)** for the recursion call stack, where `n` is the length of the array `nums`. Additionally, the space required for storing the subsets is **O(2^n)**.



#### Tags

`Backtracking`, `Hard`, `Subset`





