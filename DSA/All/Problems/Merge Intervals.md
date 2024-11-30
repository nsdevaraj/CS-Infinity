

[LeetCode #56 - Merge Intervals](https://leetcode.com/problems/merge-intervals)


### 3. **Merge Intervals**
**Problem:** Given a collection of intervals, merge all overlapping intervals.

**Answer:**
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```


# Merge Intervals - LeetCode #56

## Problem Statement

You are given an array of intervals where `intervals[i] = [start_i, end_i]`, representing the start and end of the $i^{th}$ interval. Your task is to merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Example 1:
```plaintext
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, they are merged into [1,6].
```

### Example 2:
```plaintext
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### Constraints:
- $1 \leq intervals.length \leq 10^4$
- $intervals[i].length == 2$
- $0 \leq start_i \leq end_i \leq 10^4$

## Approach

The general idea to solve this problem is to first **sort** the intervals based on the starting value and then iterate over the sorted intervals. While iterating, we can check whether the current interval overlaps with the previous one. If it does, merge the intervals; otherwise, add the current interval to the result.

### Steps:
1. **Sort the intervals** by their starting time.
2. Initialize an empty list `merged` to store the merged intervals.
3. Iterate over the sorted intervals:
   - If the `merged` list is empty or if the last interval in `merged` does not overlap with the current interval, append the current interval.
   - If the last interval in `merged` does overlap, merge them by updating the end of the last interval.

### Approach 1: Greedy Method with Sorting

#### Code:
```python
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort intervals based on the start of each interval
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    for interval in intervals:
        # If merged list is empty or no overlap with the previous interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge intervals by updating the end of the last merged interval
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged
```


```python

def merge_intervals_1(unmerged:List[List[int]])-> List[List[int]]:

    merged = []

    # sort based on start intervals
    unmerged.sort(key= lambda x : x[0])
    unmerged_len = len(unmerged)

    interval_start:int | None = None
    interval_end:int | None = None
    for i in range(unmerged_len):
        [start, end] = unmerged[i]

        # handling first item
        if(i ==0):
            interval_start = start
            interval_end = end

        if(interval_end is not None):
            # start not come under pervious interval
            if(interval_end < start):
                merged.append([interval_start, interval_end])
                interval_start = start
                interval_end = end
            
            # extending previous interval
            if(interval_end < end):
                interval_end = end
        
        # handling last item  
        if(i == unmerged_len -1):
            merged.append([interval_start, interval_end])

    return merged

```

### Time Complexity:
- **Sorting** the intervals takes $O(n \log n)$, where $n$ is the number of intervals.
- The merging step takes $O(n)$ because we iterate through the intervals once.

Thus, the overall time complexity is:
\[
O(n \log n)
\]

### Space Complexity:
- Sorting the intervals in place uses $O(1)$ additional space.
- The `merged` list takes $O(n)$ space.

Thus, the overall space complexity is:
\[
O(n)
\]

## Detailed Walkthrough:

Let's consider the first example to understand how this algorithm works:

### Input: `[[1,3],[2,6],[8,10],[15,18]]`

1. **Sort intervals**: After sorting based on the start time, we get:
   \[
   [[1,3],[2,6],[8,10],[15,18]]
   \]
   
2. **Merge intervals**:
   - The `merged` list starts as empty.
   - We start iterating over the sorted intervals.
   
   - **First interval**: `[1,3]`
     - Since `merged` is empty, we add `[1,3]` to `merged`.
     
   - **Second interval**: `[2,6]`
     - The last interval in `merged` is `[1,3]`, and `[2,6]` overlaps with it (since 2 is less than 3).
     - We merge them into `[1,6]`, so `merged` becomes `[[1,6]]`.
     
   - **Third interval**: `[8,10]`
     - No overlap with the last interval in `merged` (`[1,6]`), so we add `[8,10]` to `merged`.
     
   - **Fourth interval**: `[15,18]`
     - No overlap with `[8,10]`, so we add `[15,18]`.
     
3. **Final merged intervals**: `[[1,6],[8,10],[15,18]]`



### Approach 2: In-place Merge (Optimized Space)

In this approach, we aim to reduce the space complexity by modifying the input intervals array directly instead of using an additional list or stack. By sorting the array first and then merging the intervals in-place, we can achieve optimal space usage.

### Key Idea:

- Sort the intervals by the start value.
- Use a pointer to track the position of the last merged interval and modify the input array in-place.
- As we iterate over the intervals, we check for overlaps and adjust the end of the current interval if necessary.
- Finally, return the part of the array containing the merged intervals.

### Code:

```python
from typing import List

def merge_in_place(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    
    # Sort intervals by the start of each interval
    intervals.sort(key=lambda x: x[0])
    
    # Use a pointer to track the last merged position
    merged_index = 0
    
    for i in range(1, len(intervals)):
        # Check if the current interval overlaps with the last merged one
        if intervals[merged_index][1] >= intervals[i][0]:
            # Merge by updating the end of the merged interval
            intervals[merged_index][1] = max(intervals[merged_index][1], intervals[i][1])
        else:
            # No overlap, move the pointer and copy the current interval
            merged_index += 1
            intervals[merged_index] = intervals[i]
    
    # Return the merged intervals from the input array
    return intervals[:merged_index + 1]
```

### Explanation:

1. **Sorting**: The intervals are sorted by their start times to ensure that we can easily merge overlapping intervals.
2. **In-place merging**: We use a `merged_index` to track the position of the last merged interval in the input array.
3. **Iterating**: For each subsequent interval, we check if it overlaps with the interval at `merged_index`. If it does, we merge by updating the end value of the merged interval.
4. **Modifying in-place**: Instead of using an additional list, we modify the input array directly. When no overlap is found, we move the `merged_index` pointer and copy the current interval to that position in the array.
5. **Final result**: After the loop, we return the portion of the array that contains the merged intervals.

### Time Complexity:

- Sorting the intervals takes $O(n \log n)$.
- Merging the intervals requires a single pass over the array, which takes $O(n)$.

Thus, the overall time complexity is:
\[
O(n \log n)
\]

### Space Complexity:

- The in-place modification of the input array means no extra space is used apart from a few variables.
- Sorting is done in place if the sorting algorithm is implemented accordingly.

Thus, the overall space complexity is:
\[
O(1) \text{ (excluding input space)}
\]

### Example:

Let’s go through an example:

#### Input: `[[1,3], [2,6], [8,10], [15,18]]`

1. **Sort intervals**: `[[1,3], [2,6], [8,10], [15,18]]`
2. **Start merging**:
   - `merged_index = 0`: The first interval is `[1,3]`.
   - **Second interval**: `[2,6]` overlaps with `[1,3]`, so merge them to get `[1,6]`.
   - **Third interval**: `[8,10]` does not overlap with `[1,6]`, so move `merged_index` to 1 and copy `[8,10]`.
   - **Fourth interval**: `[15,18]` does not overlap with `[8,10]`, so move `merged_index` to 2 and copy `[15,18]`.
   
3. **Final result**: `[[1,6], [8,10], [15,18]]`


## LeetCode Link

[LeetCode #56 - Merge Intervals](https://leetcode.com/problems/merge-intervals)


## Additional Approach

### Approach 2: Interval Merging with Stack

An alternative approach is to use a stack. After sorting the intervals, we push the first interval onto the stack. For each subsequent interval, we check whether it overlaps with the interval at the top of the stack. If it does, we merge them; otherwise, we push the new interval onto the stack.

#### Code:
```python
def merge_with_stack(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    stack = [intervals[0]]
    
    for i in range(1, len(intervals)):
        top = stack[-1]
        current = intervals[i]
        
        if top[1] >= current[0]:  # Overlap detected
            stack[-1][1] = max(top[1], current[1])
        else:
            stack.append(current)
    
    return stack
```

### Time and Space Complexity:
- **Time Complexity**: Same as Approach 1, $O(n \log n)$ due to sorting.
- **Space Complexity**: $O(n)$, as the stack might store all intervals in the worst case.



## Test Function:

### Test Cases:
```python

def test_merge_intervals(func):
    test_cases = [
        {
            "name": "General Case",
            "input": [[1, 3], [2, 6], [8, 10], [15, 18]],
            "expected": [[1, 6], [8, 10], [15, 18]]
        },
        {
            "name": "Single Interval",
            "input": [[1, 4]],
            "expected": [[1, 4]]
        },
        {
            "name": "No Overlap",
            "input": [[1, 2], [3, 4], [5, 6]],
            "expected": [[1, 2], [3, 4], [5, 6]]
        },
        {
            "name": "Complete Overlap",
            "input": [[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]],
            "expected": [[1, 10]]
        },
        {
            "name": "Partial Overlap",
            "input": [[1, 4], [4, 5]],
            "expected": [[1, 5]]
        },
    ]
    for i, test_case in enumerate(test_cases):
        input_data = test_case['input']
        expected = test_case['expected']

        result = func(input_data)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All test cases passed!")

```

## Summary of Approaches

| Approach                    | Time Complexity | Space Complexity | Explanation                                                                   |
| --------------------------- | --------------- | ---------------- | ----------------------------------------------------------------------------- |
| Greedy with Sorting         | $O(n \log n)$   | $O(n)$           | Sort intervals, then merge in a single pass                                   |
| Interval Merging with Stack | $O(n \log n)$   | $O(n)$           | Similar to greedy but uses stack for merging                                  |
| **In-place Merge**          | $O(n \log n)$   | $O(1)$           | Sort intervals and merge them in-place by modifying the input array directly. |










