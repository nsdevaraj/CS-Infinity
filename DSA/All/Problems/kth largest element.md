


[Kth largest element - YT(InsideCode) ](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=812s)

[kth largest element @NeetCode](https://www.youtube.com/watch?v=XEmy13g1Qxc)

[LeetCode #215](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

[kth largest elment in array @HackerRank](https://www.hackerrank.com/contests/vit-bhopal/challenges/kth-largest-element-in-an-array-2)

[kth largest element @HackerEarth](https://www.hackerearth.com/problem/algorithm/kth-largest-element/)


[kth largest @InterviewBitBlog](https://www.interviewbit.com/blog/kth-largest-element-of-array/)




### 10. **Kth Largest Element in an Array**
**Problem:** Find the kth largest element in an unsorted array.





---

## Problem Statement: "Kth Largest Element"

Given an array of integers `arr` and an integer `k`, find the **k-th largest element** in the array.

**Example:**
```text
arr = [4, 2, 9, 7, 5, 6, 7, 1, 3], k = 4
Output: 6
```

Explanation:  
- The largest element is 9  
- The second largest is 7  
- The third largest is 7  
- The fourth largest is 6  

---

## Approach 1: Brute Force by Removing Maximum Element

### Idea:
- Remove the maximum element `k-1` times from the array. After these removals, the largest remaining element is the k-th largest.

### Steps:
1. Loop `k-1` times, removing the largest element each time.
2. After the loop, return the largest element remaining in the array.

### Code:
```python
from typing import List

def kth_largest_remove_max(arr: List[int], k: int) -> int:
    # Remove the maximum element k-1 times
    for _ in range(k - 1):
        arr.remove(max(arr))
    # Return the largest remaining element (kth largest)
    return max(arr)
```

### Time Complexity:
- Finding the maximum element takes $O(n)$ where `n` is the number of elements.
- Removing the maximum can cost up to $O(n)$ in the worst case.
- Repeating this process `k-1` times gives a time complexity of $O(k \cdot n)$.

### Space Complexity:
- We are modifying the array in-place, so space complexity is $O(1)$.

---

## Approach 2: Sorting the Array

### Idea:
- Sort the array. The k-th largest element will be at index `n - k` after sorting (where `n` is the length of the array).

### Steps:
1. Sort the array.
2. Return the element at the index `n - k`.

### Code:
```python
from typing import List

def kth_largest_sort(arr: List[int], k: int) -> int:
    # Sort the array
    arr.sort()
    # Return the element at index n-k
    return arr[-k]
```


```python
n = int(input())
arr = [int(i) for i in input().split()]
k = int(input())
arr.sort(reverse= True)
print(arr[k-1])
```


### Time Complexity:
- Sorting the array takes $O(n \log n)$.
- Accessing the element is $O(1)$.

### Space Complexity:
- Sorting may require additional space depending on the sorting algorithm. In the worst case, it is $O(n)$.

---

## Approach 3: Using a Heap (Priority Queue)

### Idea:
- Use a max-heap (simulated by negating the elements to convert Python’s `heapq` min-heap into a max-heap).
- Pop the largest element from the heap `k-1` times. The next element popped will be the k-th largest.

### Steps:
1. Convert the array to a min-heap by negating all elements.
2. Pop the largest element `k-1` times.
3. Return the next largest element, but negate it back to its original value.


### Code:
```python

import heapq
from typing import List


# in py, heapq is implemented by minHeap, not maxHeap
def kth_largest_heap(arr: List[int], k: int) -> int:
    # Negate the elements to simulate a max-heap
    arr = [-elem for elem in arr]
    # Heapify the array (min-heap with negated values)
    heapq.heapify(arr)
    # Pop the largest element k-1 times
    for _ in range(k - 1):
        heapq.heappop(arr)
    # Return the kth largest element (negated back)
    return -heapq.heappop(arr)
```


```python
import heapq
 
def kthLargest(arr, size, k):
    pq = []
 
    for i in range(size):
        heapq.heappush(pq, -1 * arr[i])
 
    l = k - 1
    while l > 0:
        heapq.heappop(pq)
        l = l - 1
 
    return -1 * pq[0]

#Time Complexity:** O(K + (N – K) * log(K) ), where N is size of the array.  
#Space Complexity: O(K), since the heap is used.
```



### Time Complexity:
- Negating all elements takes $O(n)$.
- Building the heap takes $O(n)$.
- Each pop operation takes $O(\log n)$.
- In total, the time complexity is $O(n + k \log n)$. (k cant' exceed n, but n is close to n, then  n+kLogN = nLogN, when k is low as 0, then n+kLogN = n)

### Space Complexity:
- The heap uses $O(n)$ space for storing the array.




**Answer:**
```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

The code snippet you've provided uses Python's `heapq` library to efficiently find the k-th largest element in an array, `nums`. Here’s a breakdown of how it works:

### Code Explanation
```python
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
```

### Steps and Logic
1. **Function `heapq.nlargest(k, nums)`**:
   - The `heapq.nlargest` function takes two arguments:
     - `k`: the number of largest elements to find.
     - `nums`: the list of numbers to search within.
   - `heapq.nlargest(k, nums)` returns a list of the k largest elements in `nums`, sorted in descending order.
   - For example, if `nums = [3, 2, 1, 5, 6, 4]` and `k = 2`, then `heapq.nlargest(2, nums)` would return `[6, 5]`, the two largest elements in the array.

2. **Accessing the k-th Largest Element**:
   - After obtaining the list of the k largest elements, `[-1]` accesses the last element in this list, which represents the k-th largest element in the original array.
   - In the example above, `heapq.nlargest(2, nums)[-1]` would return `5`, which is the 2nd largest element in `nums`.

3. **Return Statement**:
   - The function returns this k-th largest element, completing the solution.

### Example Walkthrough
Let's go through an example with the code:
```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```
- `heapq.nlargest(2, nums)` gives `[6, 5]`.
- `[-1]` accesses the last element in this list, which is `5`.
- So, `findKthLargest(nums, 2)` would return `5`, which is the 2nd largest element in the array.

### Complexity
- **Time Complexity**: \(O(n \log k)\), where \(n\) is the number of elements in `nums`. `heapq.nlargest` is optimized to use a heap of size \(k\) to maintain the k largest elements, which is efficient for finding the k-th largest element.
- **Space Complexity**: \(O(k)\), as it stores only the k largest elements.

This is an efficient and concise solution, especially when \(k\) is much smaller than \(n\).




---

## Quick select

Here's the **Approach 4: Quick Sort** method structured similarly to your previous approaches:

## Approach 4: Quick Sort

### Idea:
- Utilize the Quick Sort algorithm to partition the array.
- The k-th largest element can be found by partially sorting the array, focusing only on the necessary elements.

### Steps:
1. Choose a pivot element from the array.
2. Partition the array into two halves: elements greater than the pivot and elements less than the pivot.
3. Determine the position of the pivot after partitioning.
4. If the pivot's position is equal to \( n - k \) (where \( n \) is the array size), return the pivot as the k-th largest element.
5. If the pivot's position is greater than \( n - k \), recursively search the left half of the array.
6. If the pivot's position is less than \( n - k \), recursively search the right half of the array.

### Code:
```python
from typing import List
import random

def partition(arr: List[int], low: int, high: int) -> int:
    # Choose a random pivot and move it to the end
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot to end

    # Partitioning step
    store_index = low
    for i in range(low, high):
        if arr[i] > pivot:  # Elements greater than pivot go to the left
            arr[store_index], arr[i] = arr[i], arr[store_index]  # Swap
            store_index += 1

    # Move the pivot to its final place
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index  # Return the pivot index

def quick_select(arr: List[int], low: int, high: int, k: int) -> int:
    if low == high:  # Base case: only one element
        return arr[low]

    pivot_index = partition(arr, low, high)

    # The pivot is in its final sorted position
    if pivot_index == k:
        return arr[pivot_index]
    elif pivot_index > k:
        return quick_select(arr, low, pivot_index - 1, k)  # Search left
    else:
        return quick_select(arr, pivot_index + 1, high, k)  # Search right

def kth_largest_quick_sort(arr: List[int], k: int) -> int:
    n = len(arr)
    # Find the k-th largest element, which is the (n - k)-th smallest element
    return quick_select(arr, 0, n - 1, n - k)
```

### Time Complexity:
- The average time complexity is \( O(n) \) due to the partitioning steps.
- The worst-case time complexity is \( O(n^2) \) (when the smallest or largest element is consistently chosen as the pivot).
- On average, Quick Sort is efficient, making it suitable for this approach.

### Space Complexity:
- The space complexity is \( O(1) \) for the in-place partitioning, but \( O(\log n) \) can be used for the recursion stack in the average case.

### Answer:
```python
from typing import List
import random

def find_kth_largest(nums: List[int], k: int) -> int:
    def partition(arr: List[int], low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        store_index = low
        for i in range(low, high):
            if arr[i] > pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[store_index], arr[high] = arr[high], arr[store_index]
        return store_index

    def quick_select(arr: List[int], low: int, high: int, k: int) -> int:
        if low == high:
            return arr[low]
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return quick_select(arr, low, pivot_index - 1, k)
        else:
            return quick_select(arr, pivot_index + 1, high, k)

    n = len(nums)
    return quick_select(nums, 0, n - 1, n - k)
```

This structure should match your existing format, providing a clear and concise breakdown of the Quick Sort approach for finding the k-th largest element. Let me know if you need any changes or further details!

Time:
worst case  - O(n^2)
average -  O(n)


```python

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Convert k to the corresponding index if the array was sorted in ascending order
        # e.g., 1st largest element corresponds to len(nums) - 1
        # k-th largest corresponds to index len(nums) - k
        nums_len = len(nums)
        k = nums_len - k

        def quickSelect(left: int, right: int) -> int:
            # Use the last element in the current range as the pivot
            pivot_value = nums[right]
            to_pivot_index = left

            # Partitioning the array around the pivot value
            for iter_index in range(left, right):
                # Move elements less than or equal to pivot to the left side
                if nums[iter_index] <= pivot_value:
                    # Swap the elements at iter_index and to_pivot_index
                    if to_pivot_index != iter_index:
                        nums[iter_index], nums[to_pivot_index] = nums[to_pivot_index], nums[iter_index]
                    to_pivot_index += 1
            
            # Place the pivot element in its correct sorted position
            nums[right], nums[to_pivot_index] = nums[to_pivot_index], nums[right]

            # Now, to_pivot_index is the correct index of the pivot element
            pivoted_index = to_pivot_index

            # Check if we have found the k-th largest element
            if k == pivoted_index:
                return nums[pivoted_index]
            elif k < pivoted_index:
                # If k is less, search in the left partition
                return quickSelect(left, pivoted_index - 1)
            else:
                # If k is more, search in the right partition
                return quickSelect(pivoted_index + 1, right)

        # Start the Quickselect algorithm from the full array range
        return quickSelect(0, nums_len - 1)


```



```python
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert k to the target index for 0-based, ascending order
        k = len(nums) - k

        def quickSelect(left: int, right: int) -> int:
            # Choose the rightmost element as the pivot
            pivot = nums[right]
            # Initialize pivot placement index
            pivot_index = left

            # Partition: elements <= pivot to the left, others to the right
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
                    pivot_index += 1
            
            # Place the pivot in its correct sorted position
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # Check if we found the k-th largest element
            if pivot_index == k:
                return nums[pivot_index]
            # Recursively narrow down the search
            elif pivot_index < k:
                return quickSelect(pivot_index + 1, right)
            else:
                return quickSelect(left, pivot_index - 1)

        return quickSelect(0, len(nums) - 1)

```



for more duplicates, 2 way partitioning don't do things within timelimit, so use three way partitioning if needed

When the input contains many duplicate values, the standard Quickselect approach may end up with unbalanced partitions, especially if the pivot is frequently chosen from a value that appears multiple times. This can lead to worse performance. We can optimize the partitioning process by using a **3-way partitioning scheme** (similar to the Dutch National Flag algorithm), which will handle duplicates more efficiently.

Here's the refactored solution optimized for arrays with many duplicates:

```python
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert k to the target index for 0-based, ascending order
        k = len(nums) - k

        def quickSelect(left: int, right: int) -> int:
            # Choose a pivot (here, we choose the median of three for better performance with duplicates)
            mid = (left + right) // 2
            pivot = nums[mid]
            
            # 3-way partition: 
            # - Elements less than pivot go to the left
            # - Elements equal to pivot stay in the middle
            # - Elements greater than pivot go to the right
            i, j, p = left, left, right
            while j <= p:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] > pivot:
                    nums[j], nums[p] = nums[p], nums[j]
                    p -= 1
                else:
                    j += 1
            
            # Check if the k-th largest element is in the 'equal to pivot' part
            if k >= i and k <= p:
                return nums[k]
            elif k < i:
                return quickSelect(left, i - 1)  # Search in the 'less than pivot' part
            else:
                return quickSelect(p + 1, right)  # Search in the 'greater than pivot' part

        return quickSelect(0, len(nums) - 1)
```

### Explanation:

1. **Index Conversion**: Calculate `k` for 0-based index, treating the k-th largest as the `(len(nums) - k)` smallest in sorted order.
2. **Pivot Selection**: To improve balance, we choose the median of the three elements (`left`, `right`, and `mid`) as the pivot. This strategy reduces the likelihood of poor pivot choices when duplicates are present.
3. **3-Way Partitioning**:
   - **Partition Strategy**: We divide the array into three sections:
     - **Less than pivot**: Elements smaller than the pivot are moved to the left side.
     - **Equal to pivot**: Elements equal to the pivot remain in the middle.
     - **Greater than pivot**: Elements larger than the pivot move to the right side.
   - This ensures that duplicates are grouped in the middle, reducing unnecessary recursive calls.
4. **Recursive Search**:
   - If `k` falls within the "equal to pivot" section, we’ve found the k-th largest element.
   - Otherwise, we search in the left or right section based on the position of `k`.

### Complexity:
- **Average Time Complexity**: \(O(n)\) due to efficient partitioning.
- **Worst Time Complexity**: \(O(n^2)\), but the 3-way partitioning helps to mitigate this with many duplicates.
- **Space Complexity**: \(O(1)\) for in-place partitioning (excluding recursion stack). 

This refactored code is optimized for cases with numerous duplicates, making it more stable and efficient in those scenarios.


---


## Summary of Approaches

| Approach                  | Time Complexity   | Space Complexity | Explanation                                               |
| ------------------------- | ----------------- | ---------------- | --------------------------------------------------------- |
| **Remove Max k-1 Times**  | $O(k \cdot n)$    | $O(1)$           | Slow for large arrays, but conceptually simple.           |
| **Sort Array**            | $O(n \log n)$     | $O(n)$           | Efficient for moderately large arrays, easy to implement. |
| **Heap (Priority Queue)** | $O(n + k \log n)$ | $O(n)$           | Most efficient when `k` is small compared to `n`.         |
| Quick select              | O(n)              | O(1)             | Perfect answer for average case, but worst for worst case |


---

By using heaps, we achieve better performance in scenarios where `n` is large and `k` is relatively small.


to check {

https://www.hackerrank.com/contests/snapdeal-codesprint/challenges/kth-largest-smallest-number

https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

https://www.geeksforgeeks.org/kth-smallest-largest-element-in-unsorted-array/

https://www.youtube.com/watch?v=9TJYWh0adfk&pp=ygUea3RoIGxhcmdlc3QgZWxlbWVudCBxdWljayBzb3J0

}