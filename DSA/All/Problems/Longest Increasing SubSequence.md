

https://leetcode.com/problems/longest-increasing-subsequence/


to check {

https://www.youtube.com/watch?v=cjWnW0hdF1Y

https://www.youtube.com/watch?v=OIU8ZLC4qIQ


}

The **Longest Increasing Subsequence (LIS)** problem asks for the length of the longest subsequence in a given sequence such that all elements of the subsequence are strictly increasing. Unlike subarrays, subsequences don't need to consist of consecutive elements.

There are multiple approaches to solving this problem, with varying time complexities. Below are the most common solutions to the Longest Increasing Subsequence problem, each with different performance characteristics:


**Problem**: Find the length of the longest increasing subsequence in an array.

**Code**:

```python
def longest_increasing_subsequence(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(nums))  # Output: 4
```



### 1. **Dynamic Programming (DP) - O(n^2) Solution**

This is the most straightforward and commonly taught solution using dynamic programming.

#### Approach:

1. We use an array `dp` where `dp[i]` stores the length of the longest increasing subsequence (LIS) ending at index `i`.
2. For each element `nums[i]`, check all elements before it (`nums[0]` to `nums[i-1]`), and if `nums[j] < nums[i]`, then update `dp[i]` as `dp[i] = max(dp[i], dp[j] + 1)`.
3. The final answer will be the maximum value in the `dp` array.

#### Code:

```python
def lengthOfLIS(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Each element is its own subsequence
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

#### Time Complexity:

- **O(n^2)** because for each element `i`, we are comparing it with all previous elements (up to `i-1`).

#### Space Complexity:

- **O(n)** for the `dp` array.

#### Example:

For input `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the DP array would evolve as:

```
[1, 1, 1, 2, 2, 3, 4, 4]
```

The longest increasing subsequence length is `4` (`[2, 3, 7, 101]`).

---

### 2. **Binary Search with Greedy Approach - O(n log n) Solution**

This approach uses a **greedy** strategy combined with **binary search** to optimize the solution.

#### Approach:

1. Use an auxiliary list `sub` to store the smallest possible tail for increasing subsequences of different lengths.
2. For each element in the input list, use **binary search** to find the position where it can replace an element in the `sub` list (keeping it sorted).
3. If the element is larger than all the elements in `sub`, append it to the end of `sub`. If it can replace an element, replace it.
4. The length of the `sub` list will be the length of the longest increasing subsequence.

#### Code:

```python
import bisect

def lengthOfLIS(nums):
    sub = []
    
    for num in nums:
        idx = bisect.bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    
    return len(sub)
```

#### Time Complexity:

- **O(n log n)** due to binary search (`bisect_left`), where `n` is the length of the input list.

#### Space Complexity:

- **O(n)** for the `sub` list.

#### Example:

For the input `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the `sub` list will evolve as:

```
[2, 3, 7, 101]
```

The length of the longest increasing subsequence is `4`.

---

### 3. **Top-Down Dynamic Programming (Memoization) - O(n^2) Solution**

This is a recursive approach with memoization to avoid redundant calculations.

#### Approach:

1. We recursively calculate the length of the LIS starting from each index `i`.
2. Use memoization to store the results of subproblems to avoid redundant calculations.
3. For each element `nums[i]`, we try to find the longest subsequence starting from `nums[i]` and recursively explore subsequences starting from indices `i+1` to `n-1`.

#### Code:

```python
def lengthOfLIS(nums):
    def dfs(i, memo):
        if i in memo:
            return memo[i]
        
        max_length = 1
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                max_length = max(max_length, 1 + dfs(j, memo))
        
        memo[i] = max_length
        return max_length
    
    memo = {}
    result = 0
    for i in range(len(nums)):
        result = max(result, dfs(i, memo))
    
    return result
```

#### Time Complexity:

- **O(n^2)** due to the recursive calls and the subsequent exploration of all pairs of elements, but memoization reduces the work.

#### Space Complexity:

- **O(n)** for the recursion stack and memoization dictionary.

#### Example:

For the input `nums = [10, 9, 2, 5, 3, 7, 101, 18]`, the recursive function would explore different subsequences and compute their lengths. The result will be `4`.

---

### 4. **Segment Tree or Binary Indexed Tree (Fenwick Tree) - O(n log n) Solution**

In more advanced solutions, you can use a **Segment Tree** or a **Binary Indexed Tree (BIT)** to efficiently maintain and query the longest increasing subsequence in a dynamic manner. However, the implementation is more complex and usually less common for LIS problems.

#### Approach:

1. **Coordinate Compression:** Since the values in the array can be large or have large ranges, it's often helpful to compress the values into a smaller range to fit in a tree structure.
2. Use a **Segment Tree** or **Fenwick Tree** to store the maximum LIS value for each value of the array. For each number `x`, query the tree for the maximum LIS up to `x-1` and then update the tree to reflect the LIS ending at `x`.

#### Time Complexity:

- **O(n log n)**, similar to the binary search approach but with a more complex data structure.

---

### Summary of Different Approaches:

|Approach|Time Complexity|Space Complexity|
|---|---|---|
|**Dynamic Programming (DP)**|O(n²)|O(n)|
|**Binary Search + Greedy**|O(n log n)|O(n)|
|**Top-Down DP (Memoization)**|O(n²)|O(n)|
|**Segment Tree / BIT (Advanced)**|O(n log n)|O(n)|

### Which One to Use?

- **For smaller inputs** or when the problem allows simple DP solutions, the **O(n²)** dynamic programming solution is straightforward.
- **For larger inputs**, the **binary search with greedy** approach (**O(n log n)**) is the most efficient and widely used.
- **Memoization** (top-down DP) may be useful if you want to avoid iterative loops but still need to handle the complexity of subproblems.
- **Advanced methods like Segment Trees** are typically used in more specialized scenarios or when the problem involves more dynamic updates or queries.
