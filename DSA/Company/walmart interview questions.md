

[[Missing Number ( missing natural num )]]
[[Largest or Maximum Sub Array sum]]
[[LinkedList Cycle]]
[[Merge two sorted list or array]]


[[Longest Increasing  SubSequence]]


[[Word Break]]

[[Search in rotated sorted array]]

[[Tapping Rain Water]]

[[Valid Parentheses]]

[[Validate IP Address]]

[[Two Sum or 2sum]]

[[Reverse LinkedList]]

[[Median - 2 sorted arrays]]

[[First Non Rep Char or First Unique Character]]


[[Word Search]]

[[Longest Consecutive Sequence]]


[[Kth Smallest Element in a BST]]


[[Three Sum or 3Sum]]

[[Largest rectangle in histogram]]

[[Maximum Product subArray]]

[[Subarray Sum Equals K]]

[[Largest or Maximum Sub Array sum]]

[[N-Queen]]



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

---

These are medium-level problems that are commonly asked in Walmart interviews. They test your understanding of algorithms and problem-solving skills, as well as your ability to write clean, efficient code. Practice these problems to improve your chances in technical interviews!


Here are some **hard** Data Structures and Algorithms (DSA) interview questions often asked at companies like Walmart, along with their concise Python solutions:

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


