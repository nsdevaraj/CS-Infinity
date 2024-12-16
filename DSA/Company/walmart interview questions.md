

[[Missing Number ( missing natural num )]]
[[Largest or Maximum Sub Array]]
[[LinkedList Cycle]]
[[Merge two sorted list or array]]


[[Longest Increasing SubSequence]]


[[Word Break]]

[[Search in rotated sorted array]]

[[Tapping Rain Water]]

[[Valid Parentheses]]

[[Validate IP Address]]

[[Two Sum or 2sum]]

[[Reverse LinkedList]]

[[Median - 2 sorted arrays]]

[[First Non Rep Char or First Unique Character]]



---

### **3. Kth Largest Element in an Array**

**Problem**: Find the kth largest element in an array.

**Code**:

```python
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(nums, k))  # Output: 5
```

---

### **4. Maximum Product Subarray**

**Problem**: Find the maximum product of a contiguous subarray.

**Code**:

```python
def max_product(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)
    return result

# Example
nums = [2, 3, -2, 4]
print(max_product(nums))  # Output: 6
```

---

---

### **6. Subarray Sum Equals K**

**Problem**: Count the number of subarrays that sum to `k`.

**Code**:

```python
def subarray_sum(nums, k):
    count = prefix_sum = 0
    prefix_sums = {0: 1}
    for num in nums:
        prefix_sum += num
        count += prefix_sums.get(prefix_sum - k, 0)
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
    return count

# Example
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Output: 2
```

---

Here are some popular Data Structures and Algorithms (DSA) interview questions often asked at Walmart, along with concise Python solutions:

---


---


---

### 8. **Maximum Subarray (Kadane’s Algorithm)**

**Problem:** Find the contiguous subarray (containing at least one number) which has the largest sum.

```python
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

---

### 9. **Find the Intersection of Two Arrays**

**Problem:** Given two arrays, return their intersection (common elements).

```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```

---

### 10. **Kth Largest Element in an Array**

**Problem:** Find the kth largest element in an unsorted array.

```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

---

These solutions represent concise and optimized approaches for solving common interview problems. Walmart, like many other tech companies, emphasizes problem-solving, efficiency, and clarity, so practicing these types of problems will help you prepare.


Here are some medium-level Data Structures and Algorithms (DSA) questions often asked at Walmart, along with their concise Python solutions:

---

### 1. **3Sum**

**Problem:** Given an array of integers, find all unique triplets in the array which gives the sum of zero.

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate values for the first element
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicates
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
```

---

### 2. **Longest Substring Without Repeating Characters**

**Problem:** Given a string, find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s):
    char_map = {}
    left, max_len = 0, 0
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

---

### 3. **Group Anagrams**

**Problem:** Given a list of strings, group anagrams together.

```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
```

---

### 4. **Longest Palindromic Substring**

**Problem:** Given a string, find the longest palindromic substring.

```python
def longest_palindromic_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    if not s:
        return ""
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Even length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest
```

---

### 7. **Permutations**

**Problem:** Given a collection of distinct integers, return all possible permutations.

```python
def permute(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result
```

---

### 8. **Word Search**

**Problem:** Given a 2D board and a word, find if the word exists in the grid.

```python
def exist(board, word):
    def dfs(i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        found = (dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or 
                 dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1))
        board[i][j] = temp
        return found
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
```

---

### 9. **Kth Smallest Element in a BST**

**Problem:** Given a binary search tree (BST), find the kth smallest element.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
```

---

### 10. **Subsets**

**Problem:** Given a set of distinct integers, return all possible subsets (the power set).

```python
def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

---

These are medium-level problems that are commonly asked in Walmart interviews. They test your understanding of algorithms and problem-solving skills, as well as your ability to write clean, efficient code. Practice these problems to improve your chances in technical interviews!


Here are some **hard** Data Structures and Algorithms (DSA) interview questions often asked at companies like Walmart, along with their concise Python solutions:

---

---

### 2. **Longest Consecutive Sequence**

**Problem:** Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

```python
def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # Start of a potential sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    
    return longest
```

---

### 3. **Median of Two Sorted Arrays (Optimal Approach)**

**Problem:** Given two sorted arrays, find the median of the two arrays. The overall time complexity should be O(log(min(n, m))).

```python
def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]
        
        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1
    
    raise ValueError("Input arrays are not sorted")
```

---

### 4. **N-Queens Problem**

**Problem:** The N-Queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. Write a program to solve the N-Queens problem.

```python
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def solve(board, row):
        if row == n:
            result.append(["." * i + "Q" + "." * (n - i - 1) for i in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    result = []
    solve([-1] * n, 0)
    return result
```

---

### 5. **Word Ladder II**

**Problem:** Given two words (beginWord and endWord), and a dictionary’s word list, find all shortest transformation sequences from `beginWord` to `endWord`. The transformation can change only one character at a time, and each transformed word must exist in the dictionary.

```python
from collections import defaultdict, deque

def find_ladders(beginWord, endWord, wordList):
    if endWord not in wordList:
        return []
    
    wordList.add(beginWord)
    graph = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            graph[pattern].append(word)
    
    queue = deque([(beginWord, [beginWord])])
    visited = set([beginWord])
    result = []
    found = False
    
    while queue and not found:
        level_visited = set()
        for _ in range(len(queue)):
            current_word, path = queue.popleft()
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for neighbor in graph[pattern]:
                    if neighbor == endWord:
                        result.append(path + [neighbor])
                        found = True
                    elif neighbor not in visited:
                        level_visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
        visited.update(level_visited)
    
    return result
```

---

### 6. **Merge k Sorted Lists**

**Problem:** Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def merge_k_sorted_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, node)
    
    dummy = ListNode()
    current = dummy
    
    while heap:
        node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, node.next)
    
    return dummy.next
```

---

### 7. **Largest Rectangle in Histogram**

**Problem:** Given an array of integers representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Add a zero height to pop out remaining bars
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

---

### 8. **Burst Balloons**

**Problem:** Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by `nums[i]`. You are asked to burst all the balloons. If you burst balloon `i`, you will get `nums[i-1] * nums[i] * nums[i+1]` coins. Return the maximum coins you can collect by bursting the balloons wisely.

```python
def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right])
    
    return dp[0][n - 1]
```

---

### 9. **Palindrome Partitioning II**

**Problem:** Given a string `s`, partition it such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of `s`.

```python
def minCut(s):
    n = len(s)
    dp = [i for i in range(-1, n)]  # dp[i] means the minimum cuts for substring s[0:i]
    
    palindrome = [[False] * n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length <= 2 or palindrome[i + 1][j - 1]):
                palindrome[i][j] = True
                dp[j + 1] = min(dp[j + 1], dp[i] + 1)
    
    return dp[n]
```

---

### 10. **Maximum Flow (Edmonds-Karp Algorithm)**

**Problem:** Implement the Edmonds-Karp algorithm to find

the maximum flow in a flow network.

```python
from collections import deque

def bfs(capacity, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(len(capacity)):
            if not visited[v] and capacity[u][v] > 0:  # Path with positive capacity
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
                visited[v] = True
    return False

def edmonds_karp(capacity, source, sink):
    parent = [-1] * len(capacity)
    max_flow = 0
    
    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
    
    return max_flow
```

---

These problems are more complex and require advanced problem-solving and optimizations. They cover a range of topics including dynamic programming, graph algorithms, greedy techniques, and more. Solving these will significantly improve your preparation for tough interviews like those at Walmart or other major tech companies.


