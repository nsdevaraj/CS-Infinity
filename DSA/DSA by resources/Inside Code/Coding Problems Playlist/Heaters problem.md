

[Heaters problem (LeetCode #475) - Inside code](https://youtu.be/Z-vFjfgnhrU?si=eSDRL-PnZA8iCkLj)

## Problem Statement: Heaters (LeetCode #475)

You are given positions of houses and heaters on a horizontal line. Each house needs to be heated, and each heater can heat houses within a certain radius. All heaters have the same radius. Your task is to find the minimum radius such that all houses are heated.

### Input:
- **houses**: An array of integers representing the positions of houses.
- **heaters**: An array of integers representing the positions of heaters.

### Output:
- Return the minimum radius needed to ensure all houses are covered.

### Example:
**Input**:  
`houses = [1, 2, 3, 4]`,  
`heaters = [1, 4]`

**Output**:  
`1`

**Explanation**:  
With a radius of 1, the heater at position 1 can cover houses 1 and 2, and the heater at position 4 can cover houses 3 and 4. Thus, all houses are covered.

---

## Solution 1: Brute Force (Incremental Radius)

### Approach:
- Start with a radius of 0 and incrementally increase it until all houses are covered.
- Track uncovered houses and expand the coverage range of heaters with each increase in radius.

### Code:
```python
from typing import List

def find_radius(houses: List[int], heaters: List[int]) -> int:
    uncovered = set(houses) - set(heaters)  # Initial uncovered houses (houses without heaters)
    ranges = [[heater, heater] for heater in heaters]  # Initialize ranges for each heater (left and right boundaries)
    radius = 0  # Start with radius 0
    
    while uncovered:  # Loop until all houses are covered
        radius += 1  # Increment radius
        for rng in ranges:  # Expand the range of each heater
            rng[0] -= 1  # Left boundary decreases
            rng[1] += 1  # Right boundary increases
            uncovered.discard(rng[0])  # Remove covered houses from the uncovered set
            uncovered.discard(rng[1])
    
    return radius  # Return the minimum radius
```

### Time Complexity:
- **O(n + r \times m)** where `n` is the number of houses, `m` is the number of heaters, and `r` is the final radius.
- The loop runs for `r` iterations, and each iteration processes `m` heaters.

### Space Complexity:
- **O(n + m)** for the uncovered set and the ranges array.

---

## Solution 2: Linear Search for Closest Heater

### Approach:
- For each house, find the closest heater by checking all heaters.
- Track the maximum of the minimum distances between each house and its closest heater. This maximum will be the radius needed to cover all houses.

### Code:


```python
def find_radius(houses, heaters):
    distances = []
    for house in houses:
        min_dist = float('inf')
        for heater in heaters:
            min_dist = min(min_dist, abs(heater - house))
        distances.append(min_dist)
    return max(distances)

```

we don't want all distances, we just want max min_dist


```python
from typing import List

def find_radius(houses: List[int], heaters: List[int]) -> int:
    radius = 0  # Initialize the radius
    
    for house in houses:  # For each house
        min_dist = float('inf')  # Initialize minimum distance to a large value
        for heater in heaters:  # For each heater
            min_dist = min(min_dist, abs(heater - house))  # Find the closest heater
        radius = max(radius, min_dist)  # Update the maximum radius needed
    
    return radius  # Return the minimum radius
```

### Time Complexity:
- **O(n \times m)** where `n` is the number of houses and `m` is the number of heaters.
- For each house, we check every heater.

### Space Complexity:
- **O(1)** as we only store a few variables.

---

## Solution 3: Binary Search for Closest Heater

### Approach:
- Since the heater array can be sorted, we can use binary search to find the closest heater for each house more efficiently.
- Perform a binary search on the sorted heater positions to find the closest one to each house.

### Code:
```python
from typing import List

def dist_closest(heaters: List[int], house: int) -> int:
    left, right = 0, len(heaters) - 1  # Binary search on heater array
    min_dist = float('inf')  # Initialize minimum distance to a large value
    
    while left <= right:  # Perform binary search
        mid = (left + right) // 2  # Middle index
        min_dist = min(min_dist, abs(heaters[mid] - house))  # Find minimum distance
        if heaters[mid] < house:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return min_dist  # Return the minimum distance found

def find_radius(houses: List[int], heaters: List[int]) -> int:
    heaters.sort()  # Sort the heaters array for binary search
    radius = 0  # Initialize the radius
    
    for house in houses:  # For each house
        radius = max(radius, dist_closest(heaters, house))  # Find closest heater using binary search
    
    return radius  # Return the minimum radius
```



using bisect in py

```python

import bisect

def dist_closest(heaters: list[int], house: int) -> int:
    # Find the position to insert the house in the sorted heaters list
    pos = bisect.bisect_left(heaters, house)
    
    # Check the distance to the closest heater (either left or right of the position)
    if pos == 0:
        return abs(heaters[0] - house)  # Closest is the first heater
    if pos == len(heaters):
        return abs(heaters[-1] - house)  # Closest is the last heater
    
    # Closest is either the one before or the one after the position
    return min(abs(heaters[pos - 1] - house), abs(heaters[pos] - house))

def find_radius_binary_search(houses: list[int], heaters: list[int]) -> int:
    heaters.sort()  # Sort heaters for binary search
    radius = 0
    for house in houses:
        radius = max(radius, dist_closest(heaters, house))  # Find closest heater using bisect
    return radius

```



### Time Complexity:
- **O(n \times \log m)** where `n` is the number of houses and `m` is the number of heaters. We perform binary search (O(log m)) for each house.

### Space Complexity:
- **O(1)** as we only store a few variables.

---


## Solution 4: Optimized Two-Pointer Approach

### Approach:
- By sorting both the heaters and the houses, we can efficiently find the closest heater for each house using a two-pointer technique.
- This approach allows us to traverse both lists in a single pass, keeping track of the minimum distance between each house and its closest heater.

### Code:
```python
from typing import List

def find_radius(houses: List[int], heaters: List[int]) -> int:
    houses.sort()  # Sort houses to traverse in order
    heaters.sort()  # Sort heaters for efficient searching
    heaters = [float('-inf')] + heaters + [float('inf')]  # Add sentinels to avoid out-of-bounds
    radius = 0  # Initialize the radius
    i = 1  # Start with the first heater (ignoring sentinel)
    
    for house in houses:  # For each house
        # Move the pointer i to find the right position for the current house
        while heaters[i] < house:
            i += 1  # Increment pointer until we find the closest heater
            
        # Now heaters[i] is the first heater greater than or equal to the house
        min_dist = min(house - heaters[i-1], heaters[i] - house)  # Calculate distances to the closest heaters
        radius = max(radius, min_dist)  # Update radius if needed
    
    return radius  # Return the minimum radius needed
```



```python
def find_radius_two_pointers(houses: list[int], heaters: list[int]) -> int:
    houses.sort()
    heaters.sort()
    radius = 0
    j = 0
    for house in houses:
        # Move the pointer to the closest heater
        while j < len(heaters) - 1 and abs(heaters[j] - house) >= abs(heaters[j + 1] - house):
            j += 1
        radius = max(radius, abs(heaters[j] - house))
    return radius
```



### Time Complexity:
- **O(n \log n + m \log m + n + m)**, where:
  - **O(n log n)** for sorting houses,
  - **O(m log m)** for sorting heaters,
  - **O(n + m)** for traversing both arrays. 

Thus, the total complexity simplifies to **O(n + m \log m)**.

### Space Complexity:
- **O(1)** for the additional space used in variables (aside from the input lists).

---

## Summary of Solutions


| **Approach**                     | **Description**                                                                 | **Time Complexity**            | **Space Complexity**   |
|-----------------------------------|---------------------------------------------------------------------------------|---------------------------------|------------------------|
| **Brute Force**                   | Increment radius for each heater and expand coverage until all houses are covered. | $O(n + r \cdot m)$              | $O(n + m)$             |
| **Linear Search**                 | For each house, find the closest heater using a linear scan of all heaters.      | $O(n \cdot m)$                  | $O(1)$                 |
| **Binary Search**                 | Sort heaters, and for each house, find the closest heater using binary search.   | $O(n \log m + m \log m)$        | $O(1)$                 |
| **Two Pointers (Sliding Window)** | Sort both houses and heaters, use two pointers to find closest heaters efficiently. | $O(n \log n + m \log m)$        | $O(1)$                 |


---

These solutions provide a comprehensive approach to the heaters problem, catering to different time and space complexities depending on the input sizes. You can choose the most suitable method based on the constraints of your specific scenario.

If you have any more questions or need further assistance, feel free to ask!


