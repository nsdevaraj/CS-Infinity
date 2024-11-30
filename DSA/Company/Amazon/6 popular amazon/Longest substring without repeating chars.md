


## Problem Statement: Longest Substring Without Repeating Characters

### Description
Given a string `s`, your task is to find the length of the longest substring that contains no repeating characters. 

A substring is defined as a contiguous sequence of characters within the string. For example, in the string "abcabcbb", the substrings "abc", "bca", and "cab" all contain unique characters, but "a", "b", and "c" are repeated.

### Examples

1. **Input:** `s = "abcabcbb"`  
   **Output:** `3`  
   **Explanation:** The longest substring without repeating characters is "abc", which has a length of 3.

2. **Input:** `s = "bbbbb"`  
   **Output:** `1`  
   **Explanation:** The longest substring without repeating characters is "b", which has a length of 1.

3. **Input:** `s = "pwwkew"`  
   **Output:** `3`  
   **Explanation:** The longest substring without repeating characters is "wke", which has a length of 3. Note that "pwke" is a subsequence, not a substring.

### Constraints
- `0 <= s.length <= 50,000`
- `s` consists of English letters, digits, symbols, and spaces.

### Objective
Implement a function that efficiently calculates the length of the longest substring without repeating characters, ensuring it can handle the upper limits of input size within reasonable time and space complexity.

\

## Soln

```python

# O(n^3) : i loop, j loop, set making => n power 3
# no of all substrings = n (n+1) / 2
# fails performance testcase
def longest_substring_1(text:str)->int:
    length = len(text)
    max_substr_len = 0
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = text[i:j]
            substring_len = len(substring)
            if(max_substr_len < substring_len  and len(set(substring)) == substring_len):
                max_substr_len = len(substring)

    return max_substr_len


# O(n^2) : i loop, j, set => n power 2
def longest_substring_2(text:str)-> int:
    length = len(text)
    max_substr_len = 0
    for i in range(length):
        substring_len = 0
        substring_set = set()
        for j in range(i, length):
            next_char = text[j]
            if(next_char in substring_set):
                break
            substring_set.add(next_char)
            substring_len +=1
            if(substring_len > max_substr_len):
                max_substr_len = substring_len
    return max_substr_len

# O(n) -> single time string char iteration
def longest_substring_3(text:str)-> int:
    max_substr_len = 0
    substr_set = set()
    for c in text:
        if(c in substr_set):
            substr_set_len = len(substr_set)
            if(substr_set_len > max_substr_len):
                max_substr_len = substr_set_len
            substr_set = set()
        else:
            substr_set.add(c)

    substr_set_len = len(substr_set)
    if(substr_set_len > max_substr_len):
        max_substr_len = substr_set_len

    return max_substr_len

# sliding window - O(2*n) => O(n)
# start - ptr1, i - ptr2
def longest_substring_4(text: str) -> int:
    char_index = {}
    max_substr_len = 0
    start = 0  # Start index of the current substring
    for i, c in enumerate(text):
        if c in char_index and char_index[c] >= start:
            start = char_index[c] + 1  # Move the start index to the right of the last occurrence

        char_index[c] = i  # Update the character's index
        max_substr_len = max(max_substr_len, i - start + 1)  # Update max length

    return max_substr_len



```


![[longest_substring_without_repeating_chars.py]]


{
to check: from chatGPT

Sure! Here are several approaches to solving the "Longest Substring Without Repeating Characters" problem, along with their explanations and complexities:

### 1. **Sliding Window Approach**

#### Explanation:
Use two pointers to create a window that can expand and contract as you traverse the string. You maintain a set to track characters in the current window. If you encounter a repeating character, move the left pointer to shrink the window until all characters are unique.

#### Complexity:
- **Time:** O(n), where n is the length of the string.
- **Space:** O(min(n, m)), where m is the size of the character set (e.g., 26 for lowercase letters, 128 for ASCII).

#### Implementation:
```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

### 2. **Dynamic Programming Approach**

#### Explanation:
Use an array to keep track of the last index of each character. Iterate through the string, updating the starting index of the current substring based on the last occurrence of the current character. Calculate the length of the current substring at each step.

#### Complexity:
- **Time:** O(n)
- **Space:** O(m), where m is the size of the character set.

#### Implementation:
```python
def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = max_length = 0

    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

### 3. **Brute Force Approach**

#### Explanation:
Generate all possible substrings and check each for uniqueness. This approach is inefficient but straightforward. You can use a nested loop to generate substrings and a set to check for duplicates.

#### Complexity:
- **Time:** O(n^3), since you generate substrings in O(n^2) and check for uniqueness in O(n).
- **Space:** O(n) for storing substrings.

#### Implementation:
```python
def length_of_longest_substring(s: str) -> int:
    def is_unique(sub: str) -> bool:
        return len(sub) == len(set(sub))

    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_unique(s[i:j]):
                max_length = max(max_length, j - i)
    
    return max_length
```

---

### 4. **Optimized Brute Force with HashMap**

#### Explanation:
Use a brute-force approach but optimize it with a hashmap to count characters, which helps avoid recomputing unique checks repeatedly. Still less efficient than sliding window or DP but better than the pure brute-force approach.

#### Complexity:
- **Time:** O(n^2)
- **Space:** O(m)

#### Implementation:
```python
def length_of_longest_substring(s: str) -> int:
    max_length = 0
    n = len(s)

    for i in range(n):
        char_count = {}
        for j in range(i, n):
            if s[j] in char_count:
                break
            char_count[s[j]] = 1
            max_length = max(max_length, j - i + 1)

    return max_length
```

---

### Summary

The sliding window and dynamic programming approaches are generally the most efficient and widely used methods for this problem. The brute-force methods can be educational but are not practical for larger strings. Choose the approach that best fits your needs based on the input size and performance requirements!


}
{

to check:

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/


https://takeuforward.org/data-structure/length-of-longest-substring-without-any-repeating-character/

https://interviewing.io/questions/longest-substring-without-repeating-characters


}
