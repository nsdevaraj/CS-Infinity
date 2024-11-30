

[Good pairs problem - Inside code](https://youtu.be/qnCKQQE6wLM?si=nsellE6YK5kM95Eq)


# Good Pairs Problem

## Problem Statement
Given an array of integers `arr`, create a function that returns the number of good pairs. A pair \((i, j)\) is considered good if:

- `i < j`
- `arr[i] == arr[j]`

In simpler terms, a good pair is when you find the same value at two different indices in the array, where the first index comes before the second.

### Example
For the array:
```python
arr = [1, 2, 3, 1, 1, 3]
```
The good pairs are:
- (0, 3)
- (0, 4)
- (3, 4)
- (2, 5)

Thus, the function should return `4`.

## Brute Force Solution

The simplest approach to solve the problem is to use a brute force method by checking every possible pair in the array. Here's how this approach works:

1. **Initialize a counter** to track the number of good pairs.
2. Use a nested loop to traverse the array:
   - The outer loop iterates through each element.
   - The inner loop checks every subsequent element to see if they match the current element.
3. Increment the counter whenever a match is found.

### Code Implementation

```python
# Brute force solution
# Time complexity: O(n²)
# Space complexity: O(1)
def goodPairs(arr: list[int]) -> int:
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
    return count

# Example usage
arr = [1, 2, 3, 1, 1, 3]
print(goodPairs(arr))  # Output: 4
```

### Time and Space Complexity
- **Time Complexity**: \(O(n^2)\) because of the nested loops iterating through the array.
- **Space Complexity**: \(O(1)\) as no additional space is required beyond the input.

---

## Optimized Solution Using HashMap

To improve the time complexity to linear time \(O(n)\), we can use a hashmap (or dictionary) to track how many times each value has been seen as we iterate through the array.

### Approach Explanation
1. **Use a hashmap** to keep count of occurrences of each element.
2. As we iterate through the array:
   - If the current element has been seen before, the count of good pairs increases by the number of times it has been seen. This is because each previous occurrence can pair with the current occurrence.
   - Increment the count of the current element in the hashmap.

### Code Implementation

```python
# Optimized solution using a hashmap
# Time complexity: O(n)
# Space complexity: O(n)
def goodPairs(arr: list[int]) -> int:
    visited = {}
    count = 0
    for element in arr:
        if element in visited:
            count += visited[element]  # Add the number of good pairs from previous occurrences
            visited[element] += 1  # Increment count of the current element
        else:
            visited[element] = 1  # Initialize the count for new elements
    return count

# Example usage
arr = [1, 2, 3, 1, 1, 3]
print(goodPairs(arr))  # Output: 4
```

### Time and Space Complexity
- **Time Complexity**: \(O(n)\) as we only traverse the array once.
- **Space Complexity**: \(O(n)\) in the worst case, where all elements in the array are unique, thus requiring storage for each element in the hashmap.

---

## Conclusion
Using a hashmap greatly optimizes the good pairs problem by reducing the time complexity from \(O(n^2)\) to \(O(n)\). By keeping track of the number of occurrences of each element, we can quickly calculate how many new good pairs can be formed with each occurrence. This technique can be applied to various problems where counting pairs or occurrences is necessary.




