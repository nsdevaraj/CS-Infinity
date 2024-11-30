
[Longest palindrome problem - Inside code](https://youtu.be/kXtMEHbaKW4?si=E2QeVkV2O9oyRtL8)


## Longest Palindrome String Count Problem

### Problem Statement
Given a string `str` made of alphabetical letters only, create a function that returns the length of the longest palindrome string that can be constructed from the letters of `str`. A palindrome is a string that reads the same forwards and backwards, such as "racecar".

### Examples
1. **Input:** `"abccccdd"`  
   **Output:** `7`  
   **Explanation:** The longest palindrome can be `"dccaccd"`.

2. **Input:** `"a"`  
   **Output:** `1`  
   **Explanation:** The longest palindrome is `"a"` itself.

3. **Input:** `"aaa"`  
   **Output:** `3`  
   **Explanation:** The longest palindrome is `"aaa"`.

4. **Input:** `"abcd"`  
   **Output:** `1`  
   **Explanation:** The longest palindrome can only be any single character, e.g., `"a"`.

---

### Approach 1: Brute Force Method

The brute force solution involves generating all possible combinations of characters from the string and checking if they form a palindrome. This is inefficient due to the vast number of combinations.

#### Complexity:
- **Time Complexity:** $O(2^n)$
- **Space Complexity:** $O(1)$ (ignoring the space needed for combinations)



Here's the brute force solution for the **Longest Palindrome Problem**.

### Brute Force Approach

The brute force solution generates all possible permutations of the characters in the string and checks each permutation to see if it is a palindrome. If it is, we keep track of the maximum length found.

#### Python Code
```python
from itertools import permutations

def is_palindrome(s: str) -> bool:
    """Check if the given string s is a palindrome."""
    return s == s[::-1]

def longestPalindromeBruteForce(s: str) -> int:
    """Calculate the length of the longest palindrome using brute force."""
    max_length = 0
    # Generate all possible permutations of the string
    for perm in set(permutations(s)):
        candidate = ''.join(perm)  # Join tuple to form the string
        if is_palindrome(candidate):
            max_length = max(max_length, len(candidate))  # Update max length if a longer palindrome is found
    
    return max_length

# Example Usage
print(longestPalindromeBruteForce("abccccdd"))  # Output: 7
```

### Explanation of the Code:
1. **`is_palindrome(s: str) -> bool`:** This helper function checks if the given string `s` is a palindrome by comparing it to its reverse.
  
2. **`longestPalindromeBruteForce(s: str) -> int`:** 
   - This function generates all unique permutations of the string `s` using `itertools.permutations`.
   - For each permutation, it checks if the string is a palindrome.
   - It keeps track of the maximum length of any palindrome found.

### Complexity:
- **Time Complexity:** $O(n! \cdot n)$  
  - *Explanation:* The generation of all permutations takes $O(n!)$, and checking each permutation for being a palindrome takes $O(n)$.
  
- **Space Complexity:** $O(n)$  
  - *Explanation:* The space required to store the permutations.

This brute force method is inefficient for longer strings due to its factorial time complexity, but it serves as a straightforward way to understand the problem conceptually.


---

### Approach 2: Optimized Counting Method (Preferred Approach)

Instead of generating combinations, we can count character occurrences and utilize them to form a palindrome. The main insights are:
- Pairs of characters can be placed symmetrically.
- At most one character can be in the center of the palindrome.

#### Algorithm:
1. Create an array to count occurrences of each character (ASCII values). ( A to Z is 65 to 90 and a to z is 97 to 122 )
2. Traverse through the occurrences:
   - For even counts, add the entire count to the length.
   - For odd counts, add the count minus one (to ensure symmetry).
3. If there's at least one character with an odd count, add one to the length for the center character.

#### Python Code:
```python
def longestPalindrome(s: str) -> int:
    """Calculate the length of the longest palindrome that can be constructed from the given string."""
    occurrences = [0] * 128  # Array to store occurrences of each character
    
    # Count occurrences of each character
    for letter in s:
        occurrences[ord(letter)] += 1
    
    length = 0
    
    # Calculate the length of the longest palindrome
    for occu in occurrences:
        length += occu if occu % 2 == 0 else occu - 1  # Add pairs
    
    # Check for odd occurrences
    if length < len(s):
        length += 1  # Add one center character if available
    
    return length
```

### Complexity Analysis
- **Time Complexity:** $O(n)$  
  - *Explanation:* The algorithm iterates through the string to count occurrences (linear time), and then through a fixed-size array (constant time, as its size is 128).

- **Space Complexity:** $O(1)$  
  - *Explanation:* The size of the occurrences array is constant (128), regardless of the input size.

---

### Conclusion
The longest palindrome problem can be efficiently solved by counting character occurrences and utilizing symmetry to build the longest possible palindrome. This approach is significantly faster than brute force methods.



---
Need whole word:

[LeetCode #5 - Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)


## Longest Palindrome substring problem


Substring:
Yes, a **substring** of a string must maintain the order of the characters as they appear in the original (main) string. However, the substring itself can be of any length, from a single character to the entire string, and the characters must be consecutive.

### Key Points:
1. **Order Preservation**: The characters in the substring must appear in the same order as in the original string.
2. **Consecutive Characters**: The characters in the substring must be contiguous in the original string.
3. **Variable Length**: A substring can be any portion of the string, as long as it follows the above rules.

### Example:
For the string `s = "abcde"`:

- **Valid substrings**: `"a"`, `"ab"`, `"abc"`, `"bcd"`, `"de"`, `"abcde"`, etc.
- **Invalid substrings** (due to order or non-contiguity): `"ac"`, `"bd"`, `"aec"`.

### Difference between **Substring** and **Subsequence**:
- **Substring**: Characters must be contiguous and in order.
- **Subsequence**: Characters do not need to be contiguous but must still maintain their relative order.

### Example of Subsequence:
For the string `s = "abcde"`, valid subsequences include `"a"`, `"ace"`, `"bde"`, but `"acb"` is **not** a valid subsequence because the characters are not in the original order.

In summary, a substring must keep the order of characters as in the main string and be contiguous within the string.



### Section 1: Longest Palindromic Substring


---

### Problem Statement:
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same forward and backward.

---

### Example 1:
```plaintext
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

### Example 2:
```plaintext
Input: s = "cbbd"
Output: "bb"
```

### Example 3:
```plaintext
Input: s = "a"
Output: "a"
```

### Example 4:
```plaintext
Input: s = "ac"
Output: "a"
```

---

### Approaches:

#### Approach 1: Brute Force (Checking All Substrings)

In the brute force approach, we generate all possible substrings and check if each one is a palindrome. We keep track of the longest palindrome encountered.

**Steps**:
1. Generate all substrings using two loops.
2. For each substring, check if it is a palindrome.
3. Track the longest palindrome found.

#### Code:

```python
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def longest_palindrome_brute_force(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    longest = ""
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
                
    return longest
```

**Time Complexity**:  
The brute force approach takes $O(n^3)$ time because:
- There are $O(n^2)$ substrings, and
- Checking each substring for being a palindrome takes $O(n)$ time.

**Space Complexity**:  
$O(1)$ since we are only using a few extra variables for tracking the result.

---

#### Approach 2: Expanding Around Center

Instead of checking all substrings, we can use the idea that a palindrome mirrors around its center. Thus, for each character (or pair of characters in the case of even-length palindromes), we expand outwards to find the largest palindrome centered around it.

**Steps**:
1. For each character, treat it as the center of a palindrome.
2. Expand outward to check for the longest palindrome around that center.
3. Track the longest palindrome found.

#### Code:

```python
def expand_around_center(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def longest_palindrome_expand_center(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    longest = ""
    
    for i in range(n):
        # Odd-length palindromes
        odd_palindrome = expand_around_center(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Even-length palindromes
        even_palindrome = expand_around_center(s, i, i+1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest
```

**Time Complexity**:  
The center expansion approach takes $O(n^2)$ time. For each character, we are expanding outwards, and in the worst case, the expansion takes $O(n)$ time for each of the $n$ characters.

**Space Complexity**:  
$O(1)$ as we are not using extra space aside from a few variables.

---

#### Approach 3: Dynamic Programming

We can use dynamic programming to track whether each substring is a palindrome or not. We define `dp[i][j]` as `True` if the substring `s[i:j+1]` is a palindrome.

**Steps**:
1. Initialize a 2D DP array `dp` where `dp[i][j] = True` if the substring `s[i:j+1]` is a palindrome.
2. A single character is always a palindrome.
3. A substring of two characters is a palindrome if both characters are the same.
4. For longer substrings, use the fact that `dp[i][j]` is `True` if `dp[i+1][j-1]` is `True` and `s[i] == s[j]`.
5. Track the longest palindrome found.

#### Code:

```python
def longest_palindrome_dp(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]
    longest_start = 0
    longest_length = 1
    
    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            longest_start = i
            longest_length = 2
    
    # Palindromes of length 3 or more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                longest_start = i
                longest_length = length
    
    return s[longest_start:longest_start + longest_length]
```

**Time Complexity**:  
The dynamic programming approach takes $O(n^2)$ time because we fill in an $n \times n$ table.

**Space Complexity**:  
$O(n^2)$ due to the space required for the DP table.




### Section 2: Approaches Comparison and Test Function

---

### Approaches Comparison

| Approach                  | Time Complexity | Space Complexity | Description |
|----------------------------|-----------------|------------------|-------------|
| **Brute Force**             | $O(n^3)$        | $O(1)$           | Generate all substrings and check if each one is a palindrome. Inefficient for large input sizes. |
| **Expand Around Center**    | $O(n^2)$        | $O(1)$           | Expand around each character (or character pair) to find the longest palindrome. More efficient than brute force. |
| **Dynamic Programming (DP)**| $O(n^2)$        | $O(n^2)$         | Use a DP table to store whether substrings are palindromes, then track the longest one. Slightly more space-intensive than center expansion. |

---

### Test Function

Here's the test function, which takes the function to test as a parameter and includes distinct test cases that check different parts of the program.

```python
def test_longest_palindrome(func):
    test_cases = [
        # Test case 1: General case with multiple palindromes
        # "bab" is the longest palindromic substring in "babad"
        {
            "name": "General Case 1",
            "input": "babad",
            "expected": ["bab", "aba"]  # Both "bab" and "aba" are valid outputs
        },
        # Test case 2: Even length palindrome
        # "bb" is the longest palindromic substring in "cbbd"
        {
            "name": "General Case 2",
            "input": "cbbd",
            "expected": "bb"  # "bb" is the only valid result
        },
        # Test case 3: Single character string
        # The only possible palindrome is "a" itself
        {
            "name": "Single Character",
            "input": "a",
            "expected": "a"
        },
        # Test case 4: Two-character string, no palindrome
        # Either "a" or "c" is the longest palindromic substring in "ac"
        {
            "name": "Two Characters No Palindrome",
            "input": "ac",
            "expected": ["a", "c"]  # Both "a" and "c" are valid outputs
        },
        # Test case 5: All characters the same
        # The entire string is the longest palindrome
        {
            "name": "All Characters Same",
            "input": "aaaa",
            "expected": "aaaa"
        },
        # Test case 6: Empty string
        # An empty string should return an empty result
        {
            "name": "Empty String",
            "input": "",
            "expected": ""
        },
        # Test case 7: Long palindrome in the middle
        # "aba" is the longest palindrome in "xxabayy"
        {
            "name": "Long Palindrome In Middle",
            "input": "xxabayy",
            "expected": "aba"
        },
        # Test case 8: Entire string is a palindrome
        # The entire string "racecar" is a palindrome
        {
            "name": "Entire String Palindrome",
            "input": "racecar",
            "expected": "racecar"
        },
        # Test case 9: Palindrome at the start of the string
        # The palindrome "abba" is at the start of the string "abbaefg"
        {
            "name": "Palindrome At Start",
            "input": "abbaefg",
            "expected": "abba"
        },
        # Test case 10: Non-palindromic long string
        # Only single-character substrings are palindromes, "a" is the result
        {
            "name": "No Long Palindrome",
            "input": "abcdef",
            "expected": "a"
        }
    ]

    for case in test_cases:
        result = func(case["input"])
        if isinstance(case["expected"], list):
            assert result in case["expected"], f"Test {case['name']} failed: expected {case['expected']} but got {result}"
        else:
            assert result == case["expected"], f"Test {case['name']} failed: expected {case['expected']} but got {result}"

    print("All test cases passed!")

# Example usage:
# test_longest_palindrome(longest_palindrome_expand_center)
```


----




