

[Max points on a line problem - Inside code](https://youtu.be/TaT5oAn4ezQ?si=iOds3e89x2I_2FkS)
[LeetCode #149](https://leetcode.com/problems/max-points-on-a-line/description/)



### Problem Statement: Max Points on a Line (LeetCode #149)

You are given an array of points represented by their Cartesian coordinates in a 2D plane. Each point is unique, and your task is to find the maximum number of points that lie on the same straight line. 

### Example:

```text
Input: points = [(1,1), (2,2), (3,3)]
Output: 3
Explanation: All three points lie on the line y = x.
```

```text
Input: points = [(3,8), (4,3), (5,7), (6,1), (9,5), (10,9), (11,4), (14,7), (15,2), (15,6), (16,9), (19,4)]
Output: 5
Explanation: Five points form a line in this set.
```

### Approach 1: Brute Force (Finding Lines for Each Pair of Points)

#### Explanation:

The brute-force approach is to consider all pairs of points. For each pair of points, calculate the line that passes through them (represented by its slope and intercept), and then count how many other points lie on this line. The challenge is to avoid infinite slopes and floating-point precision issues.

We use a hash map to store the unique lines as keys and their respective sets of points as values. For each pair of points, we calculate the slope and intercept, ensuring to handle vertical lines and horizontal lines as special cases.

#### Code Implementation:

```python
from collections import defaultdict
from typing import List, Tuple

def find_line(x0: int, y0: int, x1: int, y1: int) -> Tuple[float, float]:
    """Finds the slope and intercept of the line through two points."""
    if y0 == y1:  # Horizontal line
        return 0, y0
    if x0 == x1:  # Vertical line
        return x0, None
    else:
        slope = (y1 - y0) / (x1 - x0)  # Slope formula
        intercept = y0 - slope * x0  # Intercept formula
        return slope, intercept

def max_points(points: List[Tuple[int, int]]) -> int:
    """Finds the maximum number of points that lie on the same line."""
    if len(points) == 1:
        return 1
    
    lines = defaultdict(set)  # To store lines and their points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x0, y0 = points[i]
            x1, y1 = points[j]
            line = find_line(x0, y0, x1, y1)
            lines[line].add(i)  # Add point indices to the line
            lines[line].add(j)
    
    return max(len(line_points) for line_points in lines.values())

# Example usage
points = [(3, 8), (4, 3), (5, 7), (6, 1), (9, 5), (10, 9), (11, 4), (14, 7), (15, 2), (15, 6), (16, 9), (19, 4)]
print(max_points(points))  # Output: 5
```

#### Time Complexity:
- Calculating the slope and intercept for each pair of points takes constant time $O(1)$. 
- Since we are traversing every pair of points, the time complexity is $O(n^2)$, where $n$ is the number of points.

#### Space Complexity:
- The space complexity is $O(n^2)$ due to the storage of unique lines and points.

### Approach 2: Optimized Approach Using GCD to Avoid Precision Issues

#### Explanation:

In the brute force approach, floating-point precision issues could cause problems when comparing slopes and intercepts. To avoid these issues, we can represent the slope as a fraction in its reduced form by using the greatest common divisor (GCD).

For every pair of points, the slope between them is calculated as a fraction $\frac{\Delta y}{\Delta x}$, reduced by dividing both the numerator and the denominator by their GCD. We use a hash map where the key is this reduced slope and the value is the count of points on that slope. We also handle vertical and horizontal lines separately.

#### Code Implementation:

```python
from math import gcd
from typing import List, Tuple
from collections import defaultdict

def max_points_optimized(points: List[Tuple[int, int]]) -> int:
    """Finds the maximum number of points on a line using GCD to avoid floating point issues."""
    def gcd_slope(x0: int, y0: int, x1: int, y1: int) -> Tuple[int, int]:
        """Calculates the slope as a reduced fraction."""
        dx = x1 - x0
        dy = y1 - y0
        if dx == 0:  # Vertical line
            return (0, 1)
        if dy == 0:  # Horizontal line
            return (1, 0)
        divisor = gcd(dx, dy)
        return (dx // divisor, dy // divisor)

    if len(points) <= 1:
        return len(points)
    
    max_points_on_a_line = 0
    for i in range(len(points)):
        slopes = defaultdict(int)
        duplicate = 1  # Count the point itself
        cur_max = 0
        for j in range(i + 1, len(points)):
            if points[i] == points[j]:
                duplicate += 1  # Identical point
            else:
                slope = gcd_slope(points[i][0], points[i][1], points[j][0], points[j][1])
                slopes[slope] += 1
                cur_max = max(cur_max, slopes[slope])
        max_points_on_a_line = max(max_points_on_a_line, cur_max + duplicate)
    
    return max_points_on_a_line

# Example usage
points = [(3, 8), (4, 3), (5, 7), (6, 1), (9, 5), (10, 9), (11, 4), (14, 7), (15, 2), (15, 6), (16, 9), (19, 4)]
print(max_points_optimized(points))  # Output: 5
```

#### Time Complexity:
- The time complexity remains $O(n^2)$ as we still check every pair of points.

#### Space Complexity:
- Space complexity is $O(n)$ because we use a hash map to store the slopes and counts for each point.

### Summary of Approaches:

| Approach         | Time Complexity | Space Complexity | Comments |
|------------------|-----------------|------------------|----------|
| Brute Force       | $O(n^2)$        | $O(n^2)$         | Uses floating-point slope and intercept. |
| Optimized with GCD | $O(n^2)$        | $O(n)$           | Uses GCD to handle slope as reduced fractions. Avoids precision errors. |

This solution offers two approaches to handle the problem, including both brute-force and precision-optimized methods using GCD for slope representation.











