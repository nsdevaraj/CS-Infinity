

[How to merge k sorted lists (k-way merge algorithms)](https://youtu.be/xS9Qix5RDA8?si=gi_wajiWmJKGGX0l)


### Problem: Merge k Sorted Lists (k-Way Merge)

You are given `k` sorted linked lists (or arrays) and need to merge them into one sorted list. Each list contains integers sorted in non-decreasing order. The task is to efficiently combine all the lists into one sorted output.

#### Example:
```plaintext
Input: [[1, 4, 5], [1, 3, 4], [2, 6]]
Output: [1, 1, 2, 3, 4, 4, 5, 6]
```

---

### Approach 1: K-Way Sorting

This approach maintains an index for each list to track which element to merge next. It finds the minimum among the current elements of the lists and merges them.

#### Algorithm:
1. Maintain an array to store the position of the current element from each list.
2. Find the minimum among the current elements of the lists.
3. Append the minimum element to the output and update its position.

#### Code:
```python
def kway_sort(lists: list[list[int]]) -> list[int]:
    k = len(lists)
    n = sum(len(lst) for lst in lists)
    output = []
    pos = [0] * k  # Positions in each list
    while len(output) < n:
        # Find the index of the list with the smallest current element
        list_idx = min(range(k), key=lambda i: lists[i][pos[i]] if pos[i] < len(lists[i]) else float("inf"))
        output.append(lists[list_idx][pos[list_idx]])
        pos[list_idx] += 1  # Move to the next element in the chosen list
    return output

# Time Complexity: O(nk), where n is the total number of elements and k is the number of lists.
# Space Complexity: O(n) for the output list.
```

#### Explanation:
- **Time Complexity:** In the worst case, for every output element, we check \(k\) lists to find the minimum, resulting in \(O(nk)\).
- **Space Complexity:** \(O(n)\) for storing the merged output.

---

### Approach 2: Naive Approach (Brute Force)

This method simply concatenates all the lists and sorts the result.

#### Algorithm:
1. Combine all lists into one large list.
2. Sort the combined list.

#### Code:
```python
def kway_naive(lists: list[list[int]]) -> list[int]:
    # Concatenate all lists into a single list and sort it
    return sorted(sum(lists, []))

# Time Complexity: O(n \log n), where n is the total number of elements.
# Space Complexity: O(n) for storing the output list.
```

#### Explanation:
- **Time Complexity:** Sorting takes \(O(n \log n)\), where \(n\) is the total number of elements across all lists.
- **Space Complexity:** \(O(n)\) for storing the result.

---

### Approach 3: Two-Way Merge

We merge two lists at a time, repeatedly combining lists.

#### Algorithm:
1. Start by merging two lists.
2. Use the merged list as the new base and continue merging with the next list.
3. Repeat until all lists are merged.

#### Code:
```python
def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    # Helper function to merge two sorted lists
    output = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1
    output.extend(list1[i:])
    output.extend(list2[j:])
    return output

def kway_two_way(lists: list[list[int]]) -> list[int]:
    # Initialize an empty list
    output = []
    for lst in lists:
        output = merge_two_lists(output, lst)
    return output

# Time Complexity: O(nk), where n is the total number of elements and k is the number of lists.
# Space Complexity: O(n) for the output list.
```

#### Explanation:
- **Time Complexity:** Each merge takes \(O(n)\) time, and since there are \(k\) lists, the total time complexity is \(O(nk)\).
- **Space Complexity:** \(O(n)\) for storing the merged output.

---


The code snippet you provided represents an approach to merge multiple sorted lists using a variation of the divide and conquer strategy, often referred to as the **Pairwise Merge** or **Iterative Merge** approach. This method iteratively merges adjacent lists until only one sorted list remains. 

Here’s a detailed explanation of this approach:

### Approach4: Pairwise Merge (Iterative Merge)

This approach continuously merges pairs of lists until all lists are combined into one. Instead of using recursion like the previous divide and conquer methods, this approach utilizes a loop to perform the merges in pairs.

#### Algorithm:
1. **Initialization**: While there is more than one list in the input:
   - Iterate through the lists in pairs (i.e., merge the first list with the second, the third with the fourth, etc.).
   - For each pair, merge them using a two-way merge function.
   - Replace the first list of each pair with the merged result.
2. **Reduction of Lists**: After merging adjacent pairs, update the list of lists to only include the merged results.
3. **Termination**: Repeat this process until only one list remains.
4. **Return the Result**: The remaining list is the fully merged sorted list.

#### Code:
```python
def two_way(list1: list[int], list2: list[int]) -> list[int]:
    # Helper function to merge two sorted lists
    output = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1
    output.extend(list1[i:])
    output.extend(list2[j:])
    return output

def kway(lists: list[list[int]]) -> list[int]:
    while len(lists) > 1:
        # iterate even indices and merge index, index+1 and put into index array and remove index+1 arrays repeatedly
        for i in range(0, len(lists) - 1, 2):
            lists[i] = two_way(lists[i], lists[i + 1])
        lists = [lists[i] for i in range(0, len(lists), 2)]
    return lists[0]

# Time Complexity: O(n log k), where n is the total number of elements and k is the number of lists.
# Space Complexity: O(n) for the merged output.
```

#### Explanation:
- **Time Complexity:** The total time complexity is \(O(n \log k)\), where \(n\) is the total number of elements across all lists and \(k\) is the number of lists. Each merge operation takes \(O(n)\), and the number of merging levels is \(O(\log k)\).
- **Space Complexity:** The space complexity is \(O(n)\) to store the final merged output, as we create new lists during the merging process.

### Summary
This Pairwise Merge approach is efficient and straightforward, leveraging iterative merging to achieve the same results as recursive methods while maintaining good performance characteristics. It is especially effective when merging a moderate number of lists.


---

### Approach 5: Non-Optimized Divide and Conquer

This method uses divide and conquer to merge two lists at a time in a recursive manner.

#### Algorithm:
1. Divide the list of lists into two halves.
2. Recursively merge both halves.
3. Use the two-way merge function to combine the results.

#### Code:
```python
def kway_non_optimized_divide_conquer(lists: list[list[int]]) -> list[int]:
    if len(lists) == 1:
        return lists[0]
    else:
        mid = len(lists) // 2
        # Recursively divide and merge
        left = kway_non_optimized_divide_conquer(lists[:mid])
        right = kway_non_optimized_divide_conquer(lists[mid:])
        return merge_two_lists(left, right)

# Time Complexity: O(n \log k), where n is the total number of elements and k is the number of lists.
# Space Complexity: O(n) for the merged output.
```

#### Explanation:
- **Time Complexity:** In each level of recursion, we perform \(O(n)\) work, and there are \(O(\log k)\) levels. Hence, the total time complexity is \(O(n \log k)\).
- **Space Complexity:** \(O(n)\) for storing the merged result.

---

### Approach 6: Optimized Divide and Conquer

Instead of merging lists sequentially, we merge them in pairs, reducing the number of iterations.

#### Algorithm:
1. Merge adjacent pairs of lists.
2. Repeat until only one list remains.

#### Code:
```python
def kway_optimized_divide_conquer(lists: list[list[int]]) -> list[int]:
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_lists.append(merge_two_lists(lists[i], lists[i + 1]))
            else:
                merged_lists.append(lists[i])
        lists = merged_lists
    return lists[0]

# Time Complexity: O(n log k), where n is the total number of elements and k is the number of lists.
# Space Complexity: O(n) for storing the final merged output.
```

#### Explanation:
- **Time Complexity:** \(O(n \log k)\), as we reduce the number of lists by half in each iteration.
- **Space Complexity:** \(O(n)\) for the merged output.

---

### Approach 7: Using a Min-Heap (Priority Queue)

We can improve the process by always selecting the smallest element from all the lists using a heap (min-priority queue). This reduces the time spent searching for the minimum.

#### Algorithm:
1. Initialize a min-heap with the first element from each list.
2. Extract the smallest element from the heap and append it to the output.
3. If the list from which the element was taken still has elements, insert the next element from that list into the heap.
4. Repeat until all elements are processed.

#### Code:
```python
import heapq

def kway_heap(lists: list[list[int]]) -> list[int]:
    k = len(lists)
    n = sum(len(lst) for lst in lists)
    output = []
    # Priority queue stores tuples of (element, index_in_list, list_index)
    pq = [(lists[i][0], 0, i) for i in range(k) if lists[i]]
    heapq.heapify(pq)
    
    while len(output) < n:
        elem, elem_idx, list_idx = heapq.heappop(pq)
        output.append(elem)
        # If there are more elements in the same list, insert the next one into the heap
        elem_idx += 1
        if elem_idx < len(lists[list_idx]):
            heapq.heappush(pq, (lists[list_idx][elem_idx], elem_idx, list_idx))
    
    return output

# Time Complexity: O(n log k), where n is the total number of elements and k is the number of lists.
# Space Complexity: O(n) for the output list and O(k) for the heap.
```

#### Explanation:
- **Time Complexity:** \(O(n \log k)\), where \(n\) is the total number of elements. Each heap operation (insert and extract) takes \(O(\log k)\).
- **Space Complexity:** \(O(n)\) for the output list and \(O(k)\) for the heap.

---

### Summary of Time Complexities:

Here are short notes summarizing each approach along with their complexities:

| Approach                             | Time Complexity | Space Complexity | Notes                                                                                                      |
| ------------------------------------ | --------------- | ---------------- | ---------------------------------------------------------------------------------------------------------- |
| **K-Way Sorting**                    | \(O(n log n)\)  | \(O(n)\)         | Concatenates all lists and sorts them, leading to higher time complexity due to sorting.                   |
| **Naive Approach (Brute Force)**     | \(O(n log n)\)  | \(O(n)\)         | Simple but inefficient; combines all lists and sorts, not optimal for large datasets.                      |
| **Two-Way Merge**                    | \(O(nk)\)       | \(O(n)\)         | Merges lists pairwise, repeatedly combining until one list remains, less efficient when `k` is large.      |
| **Pairwise Merge**                   | \(O(n log k)\)  | \(O(n)\)         | Merges adjacent pairs of lists, reducing the number of lists each iteration; better performance overall.   |
| **Non-Optimized Divide and Conquer** | \(O(n log k)\)  | \(O(n)\)         | Uses recursion to divide lists into halves and merge; can be more memory-intensive due to recursive calls. |
| **Optimized Divide and Conquer**     | \(O(n log k)\)  | \(O(n)\)         | Similar to non-optimized, but reduces the number of iterations by merging in pairs, more efficient.        |
| **Min-Heap (Priority Queue)**        | \(O(n log k)\)  | \(O(n) + O(k)\)  | Utilizes a min-heap to efficiently fetch the smallest elements across all lists, optimal for large `k`.    |

These notes provide a concise overview of each method for merging sorted lists, highlighting their complexities and key characteristics.