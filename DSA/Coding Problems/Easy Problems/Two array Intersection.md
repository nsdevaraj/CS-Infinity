

**Problem**: Given two arrays, return their intersection.
- **Example**:
  - Input: `nums1 = [1,2,2,1]`, `nums2 = [2,2]`
  - Output: `[2]`

note: distinct intersection only shown


  ### 1. **Naive Approach (Nested Loops)**

  #### Steps:
  1. Iterate through each element in the first array.
  2. For each element, check if it exists in the second array.
  3. Add the element to the result array if it is present in both arrays and hasn't already been added.

  #### Code:

```python
def intersection(ary1:List[int], ary2: List[int])-> List[int]:
    inter = set()
    for i in ary1:
        for j in ary2:
            if(i ==j): # ary1 and ary2 have common elements
                inter.add(i)
    return list(inter)

```

  ```python
  def intersection(arr1, arr2):
      result = []
      for num in arr1:
          if num in arr2 and num not in result:
              result.append(num)
      return result
  ```


### Time Complexity:
- The function iterates through each element in `arr1`, which takes $O(n_1)$, where $n_1$ is the length of `arr1`.
- For each element, checking if it exists in `arr2` takes $O(n_2)$, where $n_2$ is the length of `arr2$.
- Additionally, checking if the element is already in `result` takes $O(k)$, where $k$ is the current size of `result`. In the worst case, $k$ can grow up to $\min(n_1, n_2)$.

Thus, the overall time complexity is:
$$
O(n_1 \cdot (n_2 + k)) = O(n_1 \cdot n_2)
$$

### Space Complexity:
- The `result` list can hold up to $\min(n_1, n_2)$ elements.

Thus, the space complexity is:
$$
O(\min(n_1, n_2))
$$

### Final Summary:
- **Time Complexity**: $O(n_1 \cdot n_2)$
- **Space Complexity**: $O(\min(n_1, n_2))$

  ---

  ### 2. **Using Sets (Efficient for Duplicates)**
  Sets are useful for removing duplicates and performing set operations like intersection, which is an efficient way to solve this problem.

  #### Steps:
  1. Convert both arrays to sets to eliminate duplicates.
  2. Use the `&` operator (or `intersection()` method) to get the common elements.
  3. Convert the result back to a list.

  #### Code:
  
```python
def intersection(ary1:List[int], ary2: List[int])-> List[int]:
    return list(set(ary1) & set(ary2))
```
### Time Complexity :

1. **Set Conversion**:
   - Converting `arr1` to a set takes \( O(n) \).
   - Converting `arr2` to a set takes \( O(m) \).
   - Total for conversions: \( O(n + m) \).

2. **Set Intersection**:
   - The intersection operation `&` takes \( O(\min(n, m)) \).

### Total Time Complexity:
Combining these, the overall time complexity is:
$$
O(n + m + \min(n, m)) = O(n + m)
$$
since \( O(n + m) \) dominates \( O(\min(n, m)) \).

when min(n,m) is n
n+m+n => 2n+m => n + m

when min(n,m) is n
n+m+m => n+2m => n + m

### Space Complexity:
- Storing the sets and the result takes \( O(n + m) \).


  **Pros**: Simple, fast, and eliminates duplicates automatically.
  **Cons**: Does not maintain the order of elements, and space complexity is higher than the two-pointer approach.

  ---

  ### 4. **Hash Map (Dictionary) Approach**
  This approach uses a hash map to count occurrences of elements in one array and then checks if elements in the second array exist in the hash map.

  #### Steps:
  1. Create a dictionary to count occurrences of each element in the first array.
  2. Traverse the second array, and for each element that exists in the dictionary, add it to the result and remove it from the dictionary to avoid duplicates.

  #### Code:

```python

def intersection(ary1:List[int], ary2: List[int])-> List[int]:
    dic = {}
    inter = set()
    # put in first array items
    for i in ary1:
        if(i not in dic):
            dic[i] = 1

	# check second array items in map
    for k in ary2:
        if (k in dic):
            inter.add(k)

    return list(inter)
```

  ```python
  def intersection(arr1, arr2):
      count_map = {}
      result = []

      # Count elements in the first array
      for num in arr1:
          if num not in count_map:
              count_map[num] = 1

      # Find intersections
      for num in arr2:
          if num in count_map and count_map[num] > 0:
              result.append(num)
              count_map[num] = 0  # To ensure no duplicates in the result

      return result
  ```

```python

def intersection(ary1:List[int], ary2: List[int])-> List[int]:
    dic = {}
    inter = []
    
    for i in ary1:
        if(i not in dic):
            dic[i] = 1

    for k in ary2:
        if (k in dic):
            inter.append(k)
            del dic[k]  # delete key once pushed

    return inter

```

  #### Complexity:
  - **Time**: O(n + m), where `n` is the size of `arr1` and `m` is the size of `arr2`.
  - **Space**: O(n) for the hash map.

  **Pros**: Fast lookup and avoids duplicates without sorting.
  **Cons**: Slightly more complex due to the hash map, and extra space is needed.

  ---

  ### 6. **Counter-based Approach (Counting Frequencies)**
  You can use Python’s `collections.Counter` to count the frequency of elements in both arrays and then take the minimum frequency for common elements.

  #### Steps:
  1. Use `Counter` to count occurrences of elements in both arrays.
  2. Take the minimum of the counts for common elements and add them to the result.

```python

def intersection(arr1:List[int], arr2: List[int])-> List[int]:
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    result = []

    for num in counter1:
        if num in counter2:
            # can be used if including duplicates count
            # result.extend([num] * min(counter1[num], counter2[num]))
            if num not in result:
                result.append(num)

    return result

```

  #### Complexity:
  - **Time**: O(n + m), where `n` is the size of `arr1` and `m` is the size of `arr2`.
  - **Space**: O(n + m) for the counters.

  **Pros**: Good for counting frequencies

  , especially when there are duplicate elements and you want to respect their counts.
  **Cons**: Requires extra space to store the counters.

  ---



  ### 3. **Two-pointer Approach (Sorted Arrays)**
  If both arrays are sorted, you can use two pointers to efficiently find the intersection. This method works best when arrays are already sorted or when sorting them is acceptable.

  #### Steps:
  1. Sort both arrays if they are not sorted.
  2. Use two pointers, one for each array, to traverse both arrays.
  3. Compare the elements at the two pointers, move the pointer in the array with the smaller element.
  4. If both elements are the same, add it to the result and move both pointers.


```python

def intersection(ary1:List[int], ary2: List[int])-> List[int]:

    # sort arrays
    ary1.sort()
    ary2.sort()


    result = []
    i,j = 0,0
    ary1_len, ary2_len = len(ary1), len(ary2)

    # traverse ascending order and check equality
    while(i<ary1_len and j<ary2_len):
        if(ary1[i] == ary2[j]):
            # checking last is fine, since sorted arrays
            if not result or result[-1] != ary1[i] :
                if ary1[i] not in result: # distinct maintain
                    result.append(ary1[i])
            i,j = i+1, j+1
        elif(ary1[i] < ary2[j]):
            i += 1
        else:
            j += 1

    return result
    
```


### Time Complexity:

- Sorting `ary1` and `ary2` takes $O(n_1 \log n_1)$ and $O(n_2 \log n_2)$ respectively, where $n_1$ and $n_2$ are the lengths of the arrays.
- The two-pointer traversal runs in $O(n_1 + n_2)$.


Thus, the total time complexity is:

$$
O(n_1 \log n_1 + n_2 \log n_2)
$$

### Space Complexity:

- Sorting happens in place, so no extra space is needed for sorting.
- The result array stores up to $\min(n_1, n_2)$ elements.

Thus, the space complexity is:

$$
O(\min(n_1, n_2))
$$


  **Pros**: Efficient for large arrays if sorting is acceptable.
  **Cons**: Requires sorted arrays, so initial sorting adds overhead.

  ---



  ### 5. **Binary Search (If One Array is Large and Sorted)**
  If one array is much larger than the other, and the larger array is sorted, you can use binary search to find elements of the smaller array in the larger array efficiently.

  #### Steps:
  1. Sort the larger array.
  2. For each element in the smaller array, perform binary search in the larger array.
  3. Add elements to the result if they are found in both arrays.


```python
import bisect

def intersection(arr1: List[int], arr2: List[int]) -> List[int]:
    # Make arr1 is the smaller array, for lesser iterations
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    arr2.sort()  # Sort the second array
    result: set[int] = set()

    for num in arr1:
        insert_index: int = bisect.bisect_left(arr2, num)

        # Check if the insertion index is within bounds
        # and if the value at that index matches num
        if insert_index < len(arr2) and arr2[insert_index] == num:
            result.add(num)

    return list(result)

```

  #### Complexity:
  - **Time**: O(n log m), where `m` is the size of the larger array.
  - **Space**: O(m) for sorting and the result.


### Time Complexity

1. **Sorting `arr2`**: 
   - Sorting `arr2` takes $O(m \log m)$, where $m$ is the length of `arr2$.
   
2. **Iterating through `arr1`**: 
   - The loop iterates through all elements in `arr1$, which has a maximum length of $n$. For each element in `arr1$, a binary search operation is performed on `arr2$ to find the insertion index using `bisect.bisect_left$, which has a time complexity of $O(\log m)$.
   - Therefore, the total time for this loop is $O(n \cdot \log m)$.

	Putting it all together, the overall time complexity is:
$$
O(m \log m) + O(n \cdot \log m) = O(m \log m + n \log m) 
$$

### Space Complexity

1. **Space for `result` set**: 
   - The space used by the `result` set will, in the worst case, store all elements of the smaller array, so it takes $O(\min(n, m))$.

2. **Space for sorting**: 
   - The sorting of `arr2` does not require extra space beyond what is used by the input array, assuming in-place sorting. However, if we consider the space complexity of the sorting algorithm (like Timsort in Python), it takes $O(m)$ in the worst case.

Thus, the overall space complexity can be summarized as:
$$
O(m) + O(\min(n, m)) = O(m)
$$

### Summary

- **Time Complexity**: $O(m \log m + n \log m)$ 
- **Space Complexity**: $O(m)$


  **Pros**: Efficient for cases where one array is much larger.
  **Cons**: Requires sorting and binary search implementation, slightly more complex.

  ---


  ### Summary of Approaches:
Here’s the same table formatted with inline LaTeX for use in Obsidian:


| **Approach**               | **Time Complexity**                                        | **Space Complexity** | **Sorted/Unsorted**   |
| -------------------------- | ---------------------------------------------------------- | -------------------- | --------------------- |
| **Naive (Nested Loops)**   | $O(n \cdot m)$                                             | $min(O(n + m))$      | Unsorted              |
| **Set-based Approach**     | $O(n + m)$                                                 | $O(n + m)$           | Unsorted              |
| **Hash Map (Dictionary)**  | $O(n + m)$                                                 | $O(n + m)$           | Unsorted              |
| **Counter-based Approach** | $O(n + m)$                                                 | $O(n + m)$           | Unsorted              |
| **Two-pointer Approach**   | $O(n \log n + m \log m)$ (sorting)                         | $min(O(n + m))$      | Sorted                |
| **Binary Search**          | $O(m \log m + n \log m)$ <br>( sorting + (iter * bisect) ) | $min(O(n + m))$      | Sorted (on one array) |

### Key Notes:
- **Naive (Nested Loops)**: Inefficient but simple. Useful for small arrays.
- **Set-based Approach**: Efficient for large, unsorted arrays but doesn't preserve the order.
- **Hash Map (Dictionary)**: Efficient for handling duplicates and large unsorted arrays.
- **Counter-based Approach**: Useful when counting element frequencies is important.
- **Two-pointer Approach**: Best for sorted arrays, requires sorting if arrays aren't already sorted.
- **Binary Search**: Ideal when one array is significantly larger and sorted.

### Tests


```python

intersection_test_cases = [
    # Case 1: General case with duplicates
    {
        "name": "General Case",
        "input": ([1, 2, 2, 1], [2, 2]),
        "expected_array": [2],
    },

    # Case 2: No intersection
    {
        "name": "No Intersection",
        "input": ([1, 2, 3], [4, 5, 6]),
        "expected_array": [],
    },

    # Case 3: Complete overlap
    {
        "name": "Complete Overlap",
        "input": ([1, 2, 3], [1, 2, 3]),
        "expected_array": [1, 2, 3],
    },

    # Case 4: Empty first array
    {
        "name": "Empty First Array",
        "input": ([], [1, 2, 3]),
        "expected_array": [],
    },

    # Case 5: Empty second array
    {
        "name": "Empty Second Array",
        "input": ([1, 2, 3], []),
        "expected_array": [],
    },

    # Case 6: Some elements in both arrays
    {
        "name": "Some Common Elements",
        "input": ([1, 2, 2, 3], [2, 3, 4]),
        "expected_array": [2, 3],
    },

    # Case 7: Different order of elements
    {
        "name": "Different Order",
        "input": ([3, 1, 2], [2, 3, 1]),
        "expected_array": [1, 2, 3],
    },

    # Case 8: All elements are the same
    {
        "name": "All Duplicates",
        "input": ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),
        "expected_array": [2],
    },

    # Case 9: Empty arrays
    {
        "name": "Empty Arrays",
        "input": ([], []),
        "expected_array": [],
    },

    # Case 10: Single element arrays
    {
        "name": "Single Element Arrays",
        "input": ([5], [5]),
        "expected_array": [5],
    },

    # Case 11: Larger input with duplicates
    {
        "name": "Larger Input with Duplicates",
        "input": ([1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7], [1, 1, 2, 3, 4, 5, 6, 7]),
        "expected_array": [1, 2, 3, 4, 5, 6, 7],
    },

    # Case 12: Alternating duplicates
    {
        "name": "Alternating Duplicates",
        "input": ([1, 2, 1, 2, 1, 2], [1, 2, 1, 2, 1, 2]),
        "expected_array": [1, 2],
    },

    # Case 13: Unsorted inputs
    {
        "name": "Unsorted Inputs",
        "input" : ([3, 51, 2, 24, 15], [12, 33, 1, 5, 4]),
        "expected_array": [],
    },

    # Case 14: Larget input with no duplicates for performance testing
    {
        "name": "Larger Input with No Duplicates",
        "input": (list(range(1, 10001)), list(range(10001, 20001))),
        "expected_array": [],
    },
]

def test_intersection(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(intersection_test_cases, 1):
        input_data = test_case["input"]
        expected_array = test_case["expected_array"]
        case_name = test_case["name"]

        # Clone input to avoid modifying test cases' original input
        input_clone = input_data[0][:], input_data[1][:]

        result_array = func(*input_clone)

        # Check if the returned array matches the expected array
        assert (
            sorted(result_array) == sorted(expected_array)
        ), f"Test case {i} ({case_name}) failed: expected array {expected_array}, got {result_array}"

    print("All test cases passed!")


```



