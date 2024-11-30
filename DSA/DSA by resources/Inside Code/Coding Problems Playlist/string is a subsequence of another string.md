
[How to check if a string is a subsequence of another string? (Is subsequence problem)](https://youtu.be/I3MsjbU7uKQ?si=r-9cSTc_X5s5VxWv)


### Is Subsequence Problem


#### Problem Statement

Given two strings, `str1` and `str2`, create a boolean function that checks if `str2` is a subsequence of `str1`. 

A string `str2` is considered a subsequence of `str1` if all characters of `str2` appear in `str1` in the same order, but not necessarily consecutively.

### Examples

1. **Example 1:**
   - Input: `str1 = "abcde", str2 = "ace"`
   - Output: `True`
   - Explanation: The characters of `str2` ("a", "c", "e") appear in `str1` in the same order.

2. **Example 2:**
   - Input: `str1 = "abcde", str2 = "aec"`
   - Output: `False`
   - Explanation: Although 'a' and 'e' appear in `str1`, 'c' does not appear after 'e'.

3. **Example 3:**
   - Input: `str1 = "hello", str2 = "hlo"`
   - Output: `True`
   - Explanation: The characters "h", "l", and "o" appear in `str1` in order.

4. **Example 4:**
   - Input: `str1 = "test", str2 = "tst"`
   - Output: `True`
   - Explanation: The characters "t", "s", and "t" appear in `str1` in order.

Feel free to pause the video and try to solve the problem before watching the solution!

### Solution Approaches


Here's the brute force approach for the **Is Subsequence Problem**, including a detailed explanation, code, and complexity analysis.

---

### Approach : Brute Force Method

The brute force method involves generating all possible subsequences of `str1` and checking if `str2` matches any of them. However, this approach is inefficient and not optimal for larger strings.

#### Algorithm:
1. Generate all possible subsequences of `str1`.
2. Check if `str2` is one of these subsequences.

**Explanation:**
For a string of length \( n \), there are \( 2^n \) possible subsequences, as each character can either be included or excluded from a subsequence. Therefore, this approach can become very slow for longer strings.

#### Python Code:
```python
def generate_subsequences(s: str):
    """Helper function to generate all subsequences of a given string."""
    subsequences = []
    n = len(s)
    for i in range(1 << n):  # Iterate through all possible combinations
        subseq = ''
        for j in range(n):
            if i & (1 << j):  # Check if j-th bit is set
                subseq += s[j]
        subsequences.append(subseq)
    return subsequences

def isSubsequenceBruteForce(str1: str, str2: str) -> bool:
    """Check if str2 is a subsequence of str1 using brute force."""
    subsequences = generate_subsequences(str1)
    return str2 in subsequences  # Check if str2 is in the generated subsequences
```

### Complexity Analysis:
**Time Complexity:** \( O(2^n) \)  
- *Explanation:* The time complexity is exponential because we generate all \( 2^n \) possible subsequences of `str1`, and checking if `str2` is one of them takes linear time.

**Space Complexity:** \( O(2^n) \)  
- *Explanation:* The space complexity is also exponential due to the storage of all subsequences in a list.

### Conclusion
The brute force approach is not efficient for larger strings due to its exponential time complexity. However, it provides a clear understanding of the problem. For practical applications, consider using the two-pointer technique, as discussed earlier.


#### Approach 1: Two Pointers Technique (Iterative)

The efficient way to check if `str2` is a subsequence of `str1` is to use the two pointers technique.

**Algorithm:**
1. Initialize two pointers: `ptr1` for `str1` and `ptr2` for `str2`.
2. Traverse `str1` using `ptr1`:
   - If the characters at both pointers match (`str1[ptr1] == str2[ptr2]`), increment both pointers.
   - If they do not match, increment only `ptr1`.
3. If `ptr2` reaches the length of `str2`, it indicates that all characters of `str2` have been found in `str1`.

**Python Code:**
```python
def isSubsequence(str1: str, str2: str) -> bool:
    ptr1 = ptr2 = 0
    while ptr1 < len(str1) and ptr2 < len(str2):
        if str1[ptr1] == str2[ptr2]:
            ptr2 += 1  # Move to the next character in str2
        ptr1 += 1  # Always move to the next character in str1
    return ptr2 == len(str2)  # Check if all characters of str2 were found
```

**Time Complexity:** \( O(n) \)  
**Space Complexity:** \( O(1) \)  
*Explanation: The time complexity is linear because we traverse `str1` once. The space complexity is constant as we use only a few variables.*

---

#### Approach 2: Two Pointers Technique (Recursive)

We can also implement the solution recursively.

**Algorithm:**
1. Define a recursive function that takes the indices of both strings as parameters.
2. If the index of `str2` (`ptr2`) equals its length, return `True` (all characters found).
3. If the index of `str1` (`ptr1`) equals its length, return `False` (end of `str1` without finding all characters of `str2`).
4. If characters at both pointers match, move both pointers forward and call the function recursively.
5. If they do not match, move only the pointer for `str1` and call the function recursively.

**Python Code:**
```python
def isSubsequence(str1: str, str2: str, ptr1: int = 0, ptr2: int = 0) -> bool:
    if ptr2 == len(str2):
        return True  # Found all characters of str2
    elif ptr1 == len(str1):
        return False  # Reached end of str1
    elif str1[ptr1] == str2[ptr2]:
        return isSubsequence(str1, str2, ptr1 + 1, ptr2 + 1)  # Move both pointers
    else:
        return isSubsequence(str1, str2, ptr1 + 1, ptr2)  # Move ptr1 only
```

**Time Complexity:** \( O(n) \)  
**Space Complexity:** \( O(n) \) (due to recursion stack)  
*Explanation: The time complexity is linear as we traverse `str1` once. The space complexity is linear due to the recursive calls.*

---

### Conclusion

In this video, we explored the **Is Subsequence Problem** using two approaches: the iterative method with the two pointers technique and the recursive method. Both solutions efficiently check if `str2` is a subsequence of `str1`.


