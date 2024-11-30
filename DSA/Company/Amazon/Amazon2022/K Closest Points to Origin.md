

## K Closest Points to Origin


Sure! Here’s the problem statement for "K Closest Points to Origin":

---

### Problem Statement: K Closest Points to Origin

**Medium**

Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance, which can be calculated using the formula:
\[
\text{distance} = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
\]

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

### Example 1:
**Input:**
```plaintext
points = [[1, 3], [-2, 2]], k = 1
```
**Output:**
```plaintext
[[-2, 2]]
```
**Explanation:** The distance between (1, 3) and the origin is \(\sqrt{10}\). The distance between (-2, 2) and the origin is \(\sqrt{8}\). Since \(\sqrt{8} < \sqrt{10}\), (-2, 2) is closer to the origin. We only want the closest \(k = 1\) points from the origin, so the answer is just [[-2, 2]].

### Example 2:
**Input:**
```plaintext
points = [[3, 3], [5, -1], [-2, 4]], k = 2
```
**Output:**
```plaintext
[[3, 3], [-2, 4]]
```
**Explanation:** The answer [[-2, 4], [3, 3]] would also be accepted.

### Constraints:
- \(1 \leq k \leq \text{points.length} \leq 10^4\)
- \(-10^4 \leq x_i, y_i \leq 10^4\)

---

```py
# Problem Statement: K Closest Points to Origin

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance, which can be calculated using the formula:
distance = sqrt((x1 - x2)² + (y1 - y2)²)

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

# Example 1:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation: The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]

# Constraints:
# 1 <= k <= points.length <= 10^4
# -10^4 <= xi, yi <= 10^4


```


The answer is **guaranteed** to be **unique** (except for the order that it is in).

![[k_closest_points_to_origin.py]]



Feel free to ask if you need further clarifications or additional details!

	
### Problem Statement
Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin (0, 0).

The distance between two points on the X-Y plane is defined by the Euclidean distance:

\text{distance} = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} \]

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

### Example 1
**Input**: 
```plaintext
points = [[1, 3], [-2, 2]], k = 1
```
**Output**: 
```plaintext
[[-2, 2]]
```
**Explanation**: 
The distance between (1, 3) and the origin is \(\sqrt{10}\).  
The distance between (-2, 2) and the origin is \(\sqrt{8}\).  
Since \(\sqrt{8} < \sqrt{10}\), (-2, 2) is closer to the origin.  
We only want the closest `k = 1` points from the origin, so the answer is just `[[-2, 2]]`.

### Example 2
**Input**: 
```plaintext
points = [[3, 3], [5, -1], [-2, 4]], k = 2
```
**Output**: 
```plaintext
[[3, 3], [-2, 4]]
```
**Explanation**: 
The answer `[[3, 3], [-2, 4]]` would also be accepted. 

### Constraints
- \(1 \leq k \leq \text{points.length} \leq 10^4\)
- \(-10^4 \leq x_i, y_i \leq 10^4\)

### Approach
1. **Calculate Distances**: For each point, calculate its squared distance from the origin to avoid unnecessary computation with square roots.
2. **Sorting**: Sort the points based on their squared distance.
3. **Selecting k Closest Points**: Return the first `k` points from the sorted list.

### Python Implementation
```python
from typing import List

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # Calculate squared distances and sort points
    points.sort(key=lambda point: point[0]**2 + point[1]**2)
    
    # Return the first k points
    return points[:k]
```

### Explanation of the Code
- **Sorting**: The `sort` method sorts the points based on their squared distance from the origin using a lambda function.
- **Slicing**: We slice the first `k` points from the sorted list to get the desired result.

### Complexity
- **Time Complexity**: \(O(n \log n)\), where \(n\) is the number of points (due to sorting).
- **Space Complexity**: \(O(1)\) if sorting is done in-place; otherwise \(O(n)\) for storing the sorted points.

This implementation efficiently finds the `k` closest points to the origin based on the provided constraints.


## Soln

```python
from typing import List
from math import sqrt

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = []
    result = []

    for x, y in points:
        distance = sqrt(x**2 + y**2)
        distances.append([distance, x, y])

    # Sort distances in ascending order
    distances.sort(key=lambda x: x[0])

    # Get the k closest points
    for _ in range(k):
        distance, x, y = distances.pop(0)  # Use pop(0) to get the closest point
        result.append([x, y])

    return result

# Example usage
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
result = kClosest(points, k)
print(result)  # Output will be the k closest points to the origin

```



{

to check: from ChatGPT

Here are several different approaches to solving the problem of finding the k closest points to the origin (0, 0):

### 1. **Brute Force Approach**
- **Description:** Calculate the distance for each point from the origin and store the distances along with the points. Then sort the list of distances and return the first k points.
- **Complexity:** O(n log n) for sorting, where n is the number of points.

```python
def kClosest_brute_force(points: List[List[int]], k: int) -> List[List[int]]:
    distances = [(sqrt(x**2 + y**2), [x, y]) for x, y in points]
    distances.sort(key=lambda d: d[0])
    return [point for _, point in distances[:k]]
```

### 2. **Using a Min-Heap**
- **Description:** Use a min-heap to keep track of the closest k points. You can push all points into the heap and then pop the smallest k elements.
- **Complexity:** O(n log k), which is more efficient when k is much smaller than n.

```python
import heapq

def kClosest_heap(points: List[List[int]], k: int) -> List[List[int]]:
    min_heap = []
    
    for x, y in points:
        distance = x**2 + y**2  # Squared distance
        heapq.heappush(min_heap, (distance, [x, y]))
    
    return [heapq.heappop(min_heap)[1] for _ in range(k)]
```

### 3. **Using Quickselect Algorithm**
- **Description:** This is a selection algorithm to find the k-th smallest element. It can be adapted to find the k closest points without fully sorting the list.
- **Complexity:** Average O(n), worst-case O(n^2).

```python
def quickselect(points: List[List[int]], k: int) -> List[List[int]]:
    def distance(point):
        return point[0]**2 + point[1]**2
    
    def partition(left, right, pivot_index):
        pivot_distance = distance(points[pivot_index])
        points[pivot_index], points[right] = points[right], points[pivot_index]
        store_index = left
        
        for i in range(left, right):
            if distance(points[i]) < pivot_distance:
                points[store_index], points[i] = points[i], points[store_index]
                store_index += 1
        
        points[right], points[store_index] = points[store_index], points[right]
        return store_index
    
    left, right = 0, len(points) - 1
    while left <= right:
        pivot_index = left + (right - left) // 2
        pivot_new_index = partition(left, right, pivot_index)
        
        if pivot_new_index == k:
            return points[:k]
        elif pivot_new_index < k:
            left = pivot_new_index + 1
        else:
            right = pivot_new_index - 1
    
    return points[:k]
```

### 4. **Sorting and Deduplication**
- **Description:** First, convert points to a set to ensure uniqueness. Then sort the points based on distance.
- **Complexity:** O(n log n) due to sorting, but can be slower due to set conversion.

```python
def kClosest_deduplicate(points: List[List[int]], k: int) -> List[List[int]]:
    unique_points = list(set(tuple(point) for point in points))  # Deduplicate
    unique_points.sort(key=lambda p: (p[0]**2 + p[1]**2))
    return unique_points[:k]
```

### Summary of Approaches:
- **Brute Force:** Simple and straightforward but less efficient for large datasets.
- **Min-Heap:** Efficient when k is small; allows for quick retrieval of the closest points.
- **Quickselect:** Optimal average time complexity; useful for very large datasets.
- **Sorting and Deduplication:** Ensures unique points but incurs additional overhead from converting to a set.

Each of these approaches has its own trade-offs and can be chosen based on the specific requirements of the problem (size of input, need for uniqueness, etc.).



}



for more: check
K Closest Points to Origin: [https://leetcode.com/problems/k-closest-points-to-origin/) 

