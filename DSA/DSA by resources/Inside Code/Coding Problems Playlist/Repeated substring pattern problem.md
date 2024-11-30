


[Repeated substring pattern problem (LeetCode 459 [3 solutions] - Inside code](https://youtu.be/lumwBLJOQpk?si=Sbmn-KvFcDRRzLEb)


## Problem Statement: 
Given a string `s`, determine if it can be constructed by repeating a substring multiple times. A valid substring repetition implies the original string can be represented as `substring` repeated multiple times.

### Examples:
- Input: `"abab"`, Output: `True` (substring = `"ab"`)
- Input: `"abcdabcdabcd"`, Output: `True` (substring = `"abcd"`)
- Input: `"abcabc"`, Output: `True` (substring = `"abc"`)
- Input: `"abcab"`, Output: `False`

---

### Solution 1: Brute Force (Prefix Repetition)
#### Approach:
- Try every prefix of length \(i\), repeat it \(n/i\) times, and check if the result equals the string `s`.
- Only consider prefix lengths that divide the length of the string.

#### Time Complexity:
- **O(n²)**: The outer loop iterates over the possible prefix lengths up to \(n/2\), which takes \(O(n)\). For each iteration, constructing and comparing the repeated prefix with the original string takes \(O(n)\). Thus, the total time complexity is \(O(n) \times O(n) = O(n²)\).

#### Space Complexity:
- **O(n)**: The space complexity is \(O(n)\) because, at each step, we store and compare a repeated prefix of the string. Additionally, we use \(O(n)\) space for the input string and the repeated prefix comparison.

#### Code:
```python
def repeatedSubstringPattern(s):
    n = len(s)
    # Try each prefix of size i
    for i in range(1, (n//2) + 1):
        if n % i == 0:  # Only check if i divides n
            if s[:i] * (n // i) == s:  # Repeat the prefix n/i times and check equality
                return True
    return False
```



The condition `if n % i == 0:` is used to check if the length of the string `n` is divisible by `i`. This step is important because:

### Explanation:
- **What does this check?**  
  The expression `n % i == 0` checks if the length of the string `n` is evenly divisible by the current prefix length `i`. If `n % i == 0` is `True`, it means the string can be divided into equal parts of length `i`.

- **Why is it necessary?**  
  For the string `s` to be constructed by repeating a substring of length `i`, the total length of `s` must be a multiple of `i`. If `n` is not divisible by `i`, then you **cannot repeat a substring of length `i`** to cover the entire length of `s`. So, checking this saves unnecessary computations.

### Example:

1. **Valid case:**
   ```python
   s = "abab"
   n = len(s) = 4
   i = 2
   n % i == 0   # True, because 4 is divisible by 2
   # Now, it's worth checking if repeating the prefix "ab" (of length 2) twice equals "abab"
   ```
   This check is useful because it indicates that a substring of length `i = 2` could possibly form the entire string.

2. **Invalid case:**
   ```python
   s = "abcabc"
   n = len(s) = 6
   i = 4
   n % i == 0   # False, because 6 is not divisible by 4
   # It's impossible to repeat a substring of length 4 evenly to form a string of length 6
   ```
   Without this check, you'd waste time checking invalid prefix lengths that cannot evenly divide the string.

### Summary:
This condition is used to **filter out prefix lengths** that could never fully repeat to form the string. It improves efficiency by only checking valid candidates that can potentially match the repeated pattern.


---

### Solution 2: KMP Algorithm (Using Longest Prefix Suffix - LPS Array)


KMP - Knuth Morris Pratt
#### Approach:
- Use the concept of the **longest proper prefix which is also a suffix** (LPS) from the **KMP algorithm**.
- The string can be a repeated substring if the string length \(n\) is divisible by \(n - k\), where \(k\) is the length of the longest proper prefix that is also a suffix.

#### Time Complexity:
- **O(n)**: Building the LPS array takes linear time.
- **Space Complexity:** \(O(n)\) for storing the LPS array.

#### Code:
```python
def get_lps_array(s):
    lps = [0] * len(s)  # Initialize LPS array
    j = 0  # Pointer for prefix
    i = 1  # Pointer for suffix
    while i < len(s):
        if s[i] == s[j]:  # Match found
            j += 1
            lps[i] = j  # Store length of LPS at index i
            i += 1
        elif j > 0:  # Mismatch, fall back in prefix using previous LPS value
            j = lps[j - 1]
        else:  # No LPS found, move forward
            lps[i] = 0
            i += 1
    return lps

def repeated_substring(s):
    n = len(s)
    lps = get_lps_array(s)
    k = lps[-1]  # Longest proper prefix which is also suffix
    # Check if n is divisible by (n - k) where k is the LPS length
    return k > 0 and n % (n - k) == 0
```

---

### Solution 3: String Manipulation (Rotation Trick)
#### Approach:
- A repeated substring is essentially a **non-trivial rotation** of itself.
- If you concatenate the string `s` with itself, and remove the first and last characters, the original string `s` should appear in this new string.

#### Time Complexity:
- **O(n)**: Efficient string concatenation and search operations.
- **Space Complexity:** \(O(n)\) for the temporary string created by concatenation.

#### Code:
```python
def repeated_substring(s):
    # Concatenate s with itself and remove first and last character
    # Check if s exists in this new string
    return s in (s + s)[1:-1]
```

---

### Conclusion:
- **Brute Force Solution (O(n²))** is easy to implement but inefficient for large strings, as it requires repeated string construction and comparison.
- **KMP-based Solution (O(n))** uses the LPS array for a more optimized approach by identifying the longest proper prefix that is also a suffix.
- **String Manipulation Solution (O(n))** is the most intuitive and space-efficient approach. It leverages the fact that a repeated substring is a rotation of the string itself.

Each solution has its merits:
- **Brute Force** is simple to understand.
- **KMP** is based on a deeper understanding of string patterns.
- **String Manipulation** is a clever, concise, and highly efficient trick.





