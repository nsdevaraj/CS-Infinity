

## **LeetCode #139: Word Break**

https://leetcode.com/problems/word-break



### **Problem Statement**

Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a sequence of one or more dictionary words. A word can appear multiple times in the segmentation.

### **Examples**

#### Example 1:

- **Input**: `s = "leetcode"`, `wordDict = ["leet", "code"]`
- **Output**: `true`
- **Explanation**: `s` can be segmented as `"leet code"`.

#### Example 2:

- **Input**: `s = "applepenapple"`, `wordDict = ["apple", "pen"]`
- **Output**: `true`
- **Explanation**: `s` can be segmented as `"apple pen apple"`. Reuse of words is allowed.

#### Example 3:

- **Input**: `s = "catsandog"`, `wordDict = ["cats", "dog", "sand", "and", "cat"]`
- **Output**: `false`
- **Explanation**: No valid segmentation is possible.

---


```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        str_len = len(s)
        reachable_index = []
        for i in range(str_len):
            if(i == 0):
                reachable_index.append(True)
            else:
                reachable_index.append(False)
        reachable_index.append(False)
        for k in range(str_len):
            if(reachable_index[k]):
                for word in wordDict:
                    word_len = len(word)
                    k_upto = k + word_len
                    if( k_upto > str_len ):
                        continue                
                    if(s[k:k_upto] == word):
                        reachable_index[k_upto] = True
        return reachable_index[str_len]
```




----




### **Approach 1: Dynamic Programming**

#### **Algorithm**

1. Use a boolean DP array `dp` where `dp[i]` is `True` if the substring `s[:i]` can be segmented into valid words.
2. Initialize `dp[0] = True` (empty string can always be segmented).
3. Iterate through the string and check if any valid word in `wordDict` ends at the current position.
4. Update `dp[i]` if a valid segmentation is found.

#### **Code**

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)  # Convert list to set for O(1) lookups
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    
    return dp[n]
```

#### **Time Complexity**

- **O(n²)**: Nested loop to check all substrings.
- **O(m)**: Dictionary lookup, where mm is the total length of all words in `wordDict`.

#### **Space Complexity**

- **O(n)**: DP array.
- **O(m)**: For storing the dictionary in a set.

---

### **Approach 2: Backtracking with Memoization**

#### **Algorithm**

1. Use recursion to explore all possible segmentations.
2. Use a `memo` dictionary to store results of overlapping subproblems for efficiency.
3. At each step, try to match a word from `wordDict` with the prefix of the string.

#### **Code**

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    memo = {}

    def canBreak(start: int) -> bool:
        if start == len(s):
            return True
        if start in memo:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordSet and canBreak(end):
                memo[start] = True
                return True

        memo[start] = False
        return False

    return canBreak(0)
```

#### **Time Complexity**

- **O(n²)**: Substring operations in the worst case.
- **O(m)**: Dictionary lookup.

#### **Space Complexity**

- **O(n)**: Recursion stack and memoization.

---

### **Approach 3: BFS (Breadth-First Search)**

#### **Algorithm**

1. Treat the problem as a graph traversal.
2. Use a queue to store starting indices for substrings to explore.
3. Maintain a `visited` set to avoid redundant computations.

#### **Code**

```python
from collections import deque

def wordBreak(s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)
    queue = deque([0])
    visited = set()

    while queue:
        start = queue.popleft()
        if start in visited:
            continue
        visited.add(start)

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordSet:
                if end == len(s):
                    return True
                queue.append(end)

    return False
```

#### **Time Complexity**

- **O(n²)**: Explore all substrings.
- **O(m)**: Dictionary lookup.

#### **Space Complexity**

- **O(n)**: Queue and visited set.

---

### **Comparison of Approaches**

|Approach|Time Complexity|Space Complexity|Key Feature|
|---|---|---|---|
|**Dynamic Programming**|O(n²)|O(n)|Iterative with a boolean DP array.|
|**Backtracking + Memo**|O(n²)|O(n)|Recursive with memoization for optimization.|
|**BFS**|O(n²)|O(n)|Graph-based approach with a queue and visited.|

---

### **Test Cases**

```python
test_cases = [
    {"s": "leetcode", "wordDict": ["leet", "code"], "expected": True},
    {"s": "applepenapple", "wordDict": ["apple", "pen"], "expected": True},
    {"s": "catsandog", "wordDict": ["cats", "dog", "sand", "and", "cat"], "expected": False},
    {"s": "", "wordDict": [], "expected": True},
    {"s": "a", "wordDict": ["b"], "expected": False},
]

def test_word_break(func):
    for i, test in enumerate(test_cases, 1):
        s, wordDict, expected = test["s"], test["wordDict"], test["expected"]
        result = func(s, wordDict)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
    print(f"All test cases passed for {func.__name__}")

# Uncomment to test
# test_word_break(wordBreak)
```

---

### **Conclusion**

The **Dynamic Programming** approach is often the most straightforward and efficient for solving the Word Break problem. However, depending on the input size and constraints, **BFS** or **Backtracking with Memoization** can also be effective. Use the approach that best aligns with your problem context and language-specific strengths.


-----

Others soln:

python

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        def isword(word,wordDict,result):
            if word in wordDict:
                return True
            elif len(word)==1:
                return False
            else:
                print("word",word)
                ptr1=0
                if len(word)>1:
                    while ptr1<len(word):
                        word1 = word[0:ptr1+1]
                        word2 = word[ptr1+1:]
                        tval1 = (isword(word1,wordDict,result))
                        tval2= (isword(word2,wordDict,result))
                        result = result or (tval1 and tval2)
                        ptr1+=1
            
        result =False
        isword(s,wordDict,result)
        return result
        '''
        '''
        words = set(wordDict)
        queue = deque([0])
        seen =set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            
            for end in range(start+1, len(s)+1):
                if end in seen:
                    continue
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
        return False
        '''
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i<len(word)-1:
                    continue
                if i== len(word)-1 or dp[i-len(word)]:
                    if s[i-len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]       
```


Memory: 16.2mb

python

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize DP array where dp[i] means s[0:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: Empty string can be segmented
        # Loop through all positions in the string s
        for i in range(1, len(s) + 1):
            # Check all possible words that can end at position i
            for word in wordDict:
                # Check if the word fits in the current substring ending at i
                if i >= len(word) and s[i-len(word):i] == word:
                    # If word matches and dp[i - len(word)] is True, update dp[i]
                    dp[i] = dp[i] or dp[i - len(word)]   
        # Return whether the entire string can be segmented
        return dp[len(s)]
```



