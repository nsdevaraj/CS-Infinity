

[LeetCode #242: Valid Anagram](https://leetcode.com/problems/valid-anagram)



## isValidAnagram


[LeeCode #242](https://leetcode.com/problems/valid-anagram/)

#### Problem Statement: **Valid Anagram**

Given two strings `s1` and `s2`, determine if they are anagrams of each other. Two strings are anagrams if they contain the same characters with the same frequencies but possibly in a different order.

#### Example 1:
- **Input**: `s1 = "danger"`, `s2 = "garden"`
- **Output**: `true`
- **Explanation**: Both strings contain the same characters with the same frequencies.

#### Example 2:
- **Input**: `s1 = "hello"`, `s2 = "bello"`
- **Output**: `false`
- **Explanation**: The character 'h' is missing in `s2`.
- 
### Brute Force

```python
# Time - O(n * m) 
# Space - O(1)
def isAnagram(str1:str, str2:str):
    if(len(str1) != len(str2)):
        return False
    for i in str1:
        i_in_j:bool = False
        for j in str2:
            if(i == j):
                i_in_j = True
                break
        if(not i_in_j):
            return False
    return True

```




### Approach 3: Sorting the Strings

An alternative method is to sort both strings and check if they are equal.

#### Steps:
1. Sort both strings.
2. If the sorted versions of the strings are equal, return `true`; otherwise, return `false`.

#### Code:

```python
def are_anagrams_with_sorting(s1: str, s2: str) -> bool:
    # Check if sorted versions of both strings are equal
    return sorted(s1) == sorted(s2)
```

#### Time Complexity:
- **O(n \log n)** due to sorting both strings, where `n` is the length of the strings.

#### Space Complexity:
- **O(n)** because we create new sorted versions of the strings.
- 
```python
# time - O(nlogn)+O(mlogm)+O(min(n,m)) [sort1,sort2,compare] = O(nlogn+mlogm)
# sort - O(n) + O(m) [sort1, sort2] => O(n+m)
def isAnagram(str1:str, str2:str):
    return sorted(str1) == sorted(str2)

```


### Approach 1: Hash Table (Frequency Count)

The first approach uses a hash table to count the frequency of characters in both strings and compares them.

#### Steps:
1. If the lengths of `s1` and `s2` are different, return `false`.
2. Create two hash tables (dictionaries) to store the frequency of characters in both strings.
3. Traverse both strings and update the frequencies in their respective hash tables.
4. Compare the hash tables. If they match, return `true`; otherwise, return `false`.

#### Code:

```python
from collections import defaultdict

def are_anagrams(s1: str, s2: str) -> bool:
    # If the lengths are not equal, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    freq1 = defaultdict(int)
    freq2 = defaultdict(int)

    # Build frequency maps for both strings
    for i in range(len(s1)):
        freq1[s1[i]] += 1
        freq2[s2[i]] += 1

    # Compare frequency maps
    return freq1 == freq2
```

#### Time Complexity:
- **O(n)**, where `n` is the length of the strings. We traverse both strings once and comparing the hash tables is `O(n)`.

#### Space Complexity:
- **O(n)**, because of the hash tables storing character frequencies.



```python
# time - O(n)+O(m)+O(min(n,m)) [iter1,iter2,compare] = O(n+m)
# space -  O(n+m) [ two hasmaps ]
def isAnagram(str1:str, str2:str):
    # must have same leng - since same chars with freq
    if(len(str1) != len(str2)):
        return False
    (str1_freq, str2_freq) = ({},{})
    for i in str1:
        if(i not in str1_freq):
            str1_freq[i] = 0
        str1_freq[i] += 1
    for j in str2:
        if(j not in str2_freq):
            str2_freq[j] = 0
        str2_freq[j] += 1

    # same chars and same freq - hashmap equal
    return str1_freq == str2_freq


```


in js, object comparison is done by checking keys length are same and check by revolving each key's value!

### 3. Using Fixed-Size Array
Since the input consists of lowercase English letters, we can use a fixed-size array of size 26 to count occurrences. This approach is more space-efficient than using a dictionary.

**Algorithm Steps:**
1. Check if the lengths of `s` and `t` are the same. If not, return `false`.
2. Initialize an array of size 26 with zeros.
3. Iterate through each character in `s`, incrementing the corresponding index in the array.
4. Iterate through each character in `t`, decrementing the corresponding index in the array.
5. If all values in the array are zero, return `true`; otherwise, return `false`.

**Time Complexity:** $O(n)$, where \( n \) is the length of the strings.  
**Space Complexity:** $O(1)$ (constant space for the array).

**Python Code:**
```python
def is_anagram_fixed_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = [0] * 26  # For 26 lowercase letters

    for char in s:
        count[ord(char) - ord('a')] += 1

    for char in t:
        count[ord(char) - ord('a')] -= 1
        if count[ord(char) - ord('a')] < 0:
            return False

    return True  # All counts should be zero
```


The approaches covered earlier are the most commonly used methods to solve the **Valid Anagram** problem effectively. However, there are a couple of variations and optimizations worth mentioning:


```python
def isAnagram(s: str, t: str) -> bool:
    # Return False if lengths differ
    if len(s) != len(t):
        return False

    # Initialize counts for each letter
    letter_counts = [0] * 26
    ascii_offset = ord('a')  # Offset for 'a' to 'z' indices

    # Update counts based on characters in s and t
    for i in range(len(s)):
        letter_counts[ord(s[i]) - ascii_offset] += 1
        letter_counts[ord(t[i]) - ascii_offset] -= 1

    # Return True if all counts are zero
    return all(count == 0 for count in letter_counts)

```


### Approach 2: Using Python's `Counter` from `collections`

In Python, the `Counter` class can easily handle counting character frequencies and comparing them.

#### Steps:
1. Use `Counter` to count the characters in both `s1` and `s2`.
2. Return the comparison of the two `Counter` objects.

#### Code:

```python
from collections import Counter

def are_anagrams_with_counter(s1: str, s2: str) -> bool:
    # Use Counter to build frequency maps and directly compare them
    return Counter(s1) == Counter(s2)
```

#### Time Complexity:
- **O(n)**, where `n` is the length of the strings. The time complexity is linear because `Counter` builds the frequency table in linear time and the comparison is also linear.

#### Space Complexity:
- **O(n)** for storing the character counts.



Let's break down and structure the solution for **Valid Anagram** while ensuring clarity and depth. I'll include problem statements, detailed explanations, code, and a summary table.

---






### 5. Using a Single Count Array
This is a variation of the fixed-size array method that counts characters in a single pass for both strings. It can potentially save some operations by combining the counting and checking steps.

**Algorithm Steps:**
1. Check if the lengths of `s` and `t` are the same. If not, return `false`.
2. Initialize a single count array of size 26.
3. Iterate through each character in `s`, incrementing the corresponding index in the array.
4. Iterate through each character in `t`, decrementing the corresponding index in the array.
5. If any index in the count array is not zero at the end of the iteration, return `false`; otherwise, return `true`.

**Time Complexity:** $O(n)$, where \( n \) is the length of the strings.  
**Space Complexity:** $O(1)$ (constant space for the array).

**Python Code:**
```python
def is_anagram_single_count(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # For 26 lowercase letters

    for char in s:
        count[ord(char) - ord('a')] += 1

    for char in t:
        count[ord(char) - ord('a')] -= 1

    return all(x == 0 for x in count)  # All counts should be zero
```







### Summary of Approaches

| Approach                  | Time Complexity | Space Complexity | Description                                           |
|---------------------------|------------------|------------------|-------------------------------------------------------|
| Sorting                   | $O(n \log n)$    | $O(1)$ or $O(n)$ | Sort both strings and compare.                        |
| Counting Characters (Map) | $O(n)$           | $O(1)$           | Use a dictionary to count characters in both strings.|
| Fixed-Size Array          | $O(n)$           | $O(1)$           | Use a fixed-size array for counting characters.       |
| `collections.Counter`      | $O(n)$           | $O(1)$           | Use Counter to count characters in both strings.     |
| Single Count Array        | $O(n)$           | $O(1)$           | Use a single count array to count characters.        |

### Conclusion
The `collections.Counter` approach is particularly favored for its readability and ease of use in Python, while the single count array method is efficient and concise. Depending on the context and the constraints, you may choose any of these methods, but the differences in performance are generally minimal for practical input sizes.

If you have specific constraints or requirements in mind, feel free to mention them!

### Tests
Here are some test cases to validate our function:

```python
valid_anagram_test_cases = [
    {'input': ("anagram", "nagaram"), 'expected': True},
    {'input': ("rat", "car"), 'expected': False},
    {'input': ("listen", "silent"), 'expected': True},
    {'input': ("triangle", "integral"), 'expected': True},
    {'input': ("apple", "pale"), 'expected': False},
    {'input': ("", ""), 'expected': True},
    {'input': ("abc", "cba"), 'expected': True},
]

def test_is_anagram(func):
    print(f"Testing: {func.__name__}")
    for i, test_case in enumerate(valid_anagram_test_cases, 1):
        input_data = test_case['input']
        expected_output = test_case['expected']
        result = func(*input_data)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
    print("All test cases passed!")

# Uncomment to run tests
# test_is_anagram(is_anagram)
```

---



