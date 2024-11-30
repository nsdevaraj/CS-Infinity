

[LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters)

### Problem Statement

**Title:** Longest Substring Without Repeating Characters

**Description:**
Given a string `s`, find the length of the longest substring without repeating characters. A substring is a contiguous sequence of characters within the string.

**Example:**
- Input: `"abcabcbb"`
- Output: `3`
- Explanation: The answer is `"abc"`, with the length of 3.

- Input: `"bbbbb"`
- Output: `1`
- Explanation: The answer is `"b"`, with the length of 1.

- Input: `"pwwkew"`
- Output: `3`
- Explanation: The answer is `"wke"`, with the length of 3.

**Function Signature:**
```javascript
function lengthOfLongestSubstring(s: string): number
```


## Soln:

```ts

const lengthOfLongestSubstring1 = (fullStr: string): number => {
  let maxSubStrLen = 0;
  if (!fullStr) return maxSubStrLen;

  let rightPtr = 0;
  const fullStrLen = fullStr.length;
  let currentSubStrLen = 0;
  let subStrCharIndexMap: Map<string, number> = new Map();
  while (rightPtr < fullStrLen) {
    const newChar = fullStr.slice(rightPtr, rightPtr + 1);
    const previousSameCharIndex = subStrCharIndexMap.get(newChar);
    if (previousSameCharIndex !== undefined) {
      if (subStrCharIndexMap.size > maxSubStrLen) {
        maxSubStrLen = subStrCharIndexMap.size;
      }
      rightPtr = previousSameCharIndex;
      subStrCharIndexMap = new Map();
    } else {
      subStrCharIndexMap.set(newChar, rightPtr);
    }
    rightPtr += 1;
  }

  if (subStrCharIndexMap.size > maxSubStrLen) {
    maxSubStrLen = subStrCharIndexMap.size;
  }
  return maxSubStrLen;
};

const lengthOfLongestSubstring2 = (s: string): number => {
  const subStrCharSet = new Set<string>();
  let maxLength = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    while (subStrCharSet.has(s[right])) {
      subStrCharSet.delete(s[left]);
      left++;
    }
    subStrCharSet.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
};

const lengthOfLongestSubstring3 = (s: string): number => {
  const charIndexMap = new Map();
  let maxLength = 0;
  let start = 0;

  for (let end = 0; end < s.length; end++) {
    if (charIndexMap.has(s[end])) {
      start = Math.max(charIndexMap.get(s[end]) + 1, start);
    }
    charIndexMap.set(s[end], end);
    maxLength = Math.max(maxLength, end - start + 1);
  }

  return maxLength;
};
```



```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If the input string is empty, return 0
        if not s:
            return 0

        # Initialize variables
        max_len = 0  # To track the maximum length of the substring without repeating characters
        str_ary = list(s)  # Convert the input string to a list of characters
        str_len = len(s)  # Get the length of the string
        char_index_map = {}  # Dictionary to store the last index of each character
        cur_len = 0  # To track the length of the current valid substring
        i = 0  # Initialize the index for iteration
        
        # Iterate through the string
        while i < str_len:
            c = str_ary[i]  # Current character
            
            if c in char_index_map:
                # If the current character is already in the map (repeated character)
                
                # Update max_len if the current valid substring length is larger
                if cur_len > max_len:
                    max_len = cur_len
                
                # Retrieve the index where this character was last seen
                old_index = char_index_map[c]
                
                # Reset the map and cur_len to start counting a new substring
                char_index_map = {}
                cur_len = 0
                
                # Move back the index to the position of the last occurrence of the repeated character
                i = old_index
            else:
                # If the character is not repeated, continue building the substring
                
                cur_len += 1  # Increase the length of the current valid substring
                char_index_map[c] = i  # Store the current index of the character
            
            i += 1  # Move to the next character

        # After the loop, check if the last valid substring was the longest
        if cur_len > max_len:
            max_len = cur_len

        return max_len

```

## Refs

extra by chatGPT

Finding the longest substring without repeating characters can be approached in several ways. Here are three common methods, along with explanations and their time complexities:

### 1. Brute Force Approach

**Description:**
Generate all possible substrings and check for the longest one that contains all unique characters.

**Implementation:**
```javascript
const longestSubstringBruteForce = (s) => {
    let maxLength = 0;

    for (let start = 0; start < s.length; start++) {
        for (let end = start + 1; end <= s.length; end++) {
            const substring = s.substring(start, end);
            const uniqueChars = new Set(substring);
            if (uniqueChars.size === substring.length) {
                maxLength = Math.max(maxLength, substring.length);
            }
        }
    }
    return maxLength;
};
```

**Time Complexity:**
- **O(n^3)**: The outer two loops generate substrings, and checking for uniqueness takes O(n) time.

### 2. Sliding Window Approach

**Description:**
Use two pointers to create a "window" that expands and contracts to include unique characters. This is a more efficient approach.

**Implementation:**
```javascript
const longestSubstringSlidingWindow = (s) => {
    const charMap = new Map();
    let left = 0, maxLength = 0;

    for (let right = 0; right < s.length; right++) {
        if (charMap.has(s[right])) {
            left = Math.max(charMap.get(s[right]) + 1, left);
        }
        charMap.set(s[right], right);
        maxLength = Math.max(maxLength, right - left + 1);
    }
    return maxLength;
};
```

**Time Complexity:**
- **O(n)**: Each character is processed at most twice (once added and once removed).

### 3. Dynamic Programming Approach

**Description:**
Maintain an array to store the length of the longest substring ending at each character. Update the maximum length as you traverse the string.

**Implementation:**
```javascript
const longestSubstringDynamicProgramming = (s) => {
    const dp = new Array(s.length).fill(0);
    const charIndex = new Map();
    let maxLength = 0;

    for (let i = 0; i < s.length; i++) {
        if (charIndex.has(s[i])) {
            dp[i] = Math.min(i - charIndex.get(s[i]), dp[i - 1] + 1);
        } else {
            dp[i] = (i === 0) ? 1 : dp[i - 1] + 1;
        }
        charIndex.set(s[i], i);
        maxLength = Math.max(maxLength, dp[i]);
    }
    return maxLength;
};
```

**Time Complexity:**
- **O(n)**: Each character is processed once, and array access is O(1).

### Summary of Approaches

1. **Brute Force:**
   - **Pros:** Simple to understand and implement.
   - **Cons:** Inefficient for long strings; cubic time complexity.

2. **Sliding Window:**
   - **Pros:** Efficient with linear time complexity; handles large inputs well.
   - **Cons:** Requires more careful handling of indices.

3. **Dynamic Programming:**
   - **Pros:** Efficient with linear time complexity; uses a straightforward approach to build on previous results.
   - **Cons:** Slightly more complex to implement; requires extra space for the DP array.

The **Sliding Window** approach is generally the most preferred due to its simplicity and efficiency. Choose the method based on your needs and constraints!

### More


**Answer:**
```python
def length_of_longest_substring(s):
    char_map = {}
    left = max_length = 0
    for right, char in enumerate(s):
        if char in char_map:
            left = max(left, char_map[char] + 1)
        char_map[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
```



### Test Function and Test Cases

```ts
const LONGEST_SUBSTRING_TEST_CASES = [
  {
    name: "Empty String",
    input: "",
    expected: 0,
    reason: "An empty string has no characters, so the longest substring is 0.",
  },
  {
    name: "All Unique Characters",
    input: "abcde",
    expected: 5,
    reason:
      "All characters are unique, so the entire string is the longest substring.",
  },
  {
    name: "Single Character Repeating",
    input: "aaaaa",
    expected: 1,
    reason: "The longest substring without repeating is any single character.",
  },
  {
    name: "Repeating Characters with Gaps",
    input: "abcabcbb",
    expected: 3,
    reason: "The longest substring is 'abc', with length 3.",
  },
  {
    name: "Mix of Characters",
    input: "pwwkew",
    expected: 3,
    reason: "The longest substring is 'wke', with length 3.",
  },
  {
    name: "Mixed Repeats and Uniques",
    input: "dvdf",
    expected: 3,
    reason: "The longest substring is 'vdf', with length 3.",
  },
  {
    name: "Long String with Repeats",
    input: "tmmzuxt",
    expected: 5,
    reason: "The longest substring is 'mzuxt', with length 5.",
  },
  {
    name: "Single Unique at Start",
    input: "aab",
    expected: 2,
    reason: "The longest substring is 'ab', with length 2.",
  },
  {
    name: "Ends with Repeats",
    input: "abcdeedcba",
    expected: 5,
    reason: "The longest substring is 'abcde', with length 5.",
  },
  {
    name: "Long String with Multiple Patterns",
    input: "abcdabcdaaaa",
    expected: 4,
    reason: "The longest substring is 'abcd', with length 4.",
  },
  {
    name: "Special Characters",
    input: "!@#$%^&*()_+",
    expected: 12,
    reason:
      "All characters are unique, so the entire string is the longest substring.",
  },
  {
    name: "Digits and Letters Mixed",
    input: "abc123abc456",
    expected: 9,
    reason: "The longest substring is 'abc123', with length 9.",
  },
  {
    name: "Long Repeating Sequence",
    input: "xyzxyzxyzxyz",
    expected: 3,
    reason: "The longest substring is 'xyz', with length 3.",
  },
  {
    name: "Back-to-Back Repeats",
    input: "aabbccddeeffgg",
    expected: 2,
    reason:
      "The longest substring is any pair of unique characters, with length 2.",
  },
  {
    name: "Palindrome with Unique Middle",
    input: "abcba",
    expected: 3,
    reason: "The longest substring is 'abc', with length 3.",
  },
  {
    name: "Very Long String",
    input: "abcdefghijabcdefghijabcdefghijabcdefghij",
    expected: 10,
    reason: "The longest substring is 'abcdefghij', with length 10.",
  },
  {
    name: "Complex Pattern",
    input: "abcabcabca",
    expected: 3,
    reason: "The longest substring is 'abc', with length 3.",
  },
];

const testLengthOfLongestSubstring = (func: Function) => {
  for (const testCase of LONGEST_SUBSTRING_TEST_CASES) {
    const funcOutput = func(testCase.input);
    console.assert(
      funcOutput === testCase.expected,
      `Test case '${testCase.name}' failed: expected ${testCase.expected}, but got ${funcOutput}`,
    );
  }

  console.log("All test cases completed!");
};

```



---


Longest substring without repeating characters (LeetCode #3) - Inside code

[Longest substring without repeating characters - InsideCode](https://youtu.be/UGDXH9dJosg?si=QiT23qaRz7GIi69O)

[LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)


### Problem Statement: Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.

### Example

**Input**:  
`s = "abcdebaeafcbhfab"`

**Output**:  
`6`  
**Explanation**: The longest substring without repeating characters is `"eafcbh"`, which has length 6.

---

### Approach 1: Brute Force

In the brute force approach, we generate all possible substrings and check whether each substring has unique characters. This involves nested loops to create substrings and an additional check to ensure no characters repeat in each substring.

#### Steps:
1. Traverse all possible substrings.
2. For each substring, check if all characters are unique.
3. Keep track of the maximum length of substrings with unique characters.

#### Time Complexity:
- **Generating substrings**: $O(n^2)$, where $n$ is the length of the string.
- **Checking for uniqueness**: $O(n)$ in the worst case for each substring.
- **Overall time complexity**: $O(n^3)$.

#### Code:

```typescript
export function longestSubStringBruteForce(str: string): number {
    const hasUniqueCharacters = (substring: string): boolean => {
        const uniqueChars = new Set(substring);
        return uniqueChars.size === substring.length;
    };

    let maxLength = 0;

    for (let start = 0; start < str.length; start++) {
        for (let end = start + 1; end <= str.length; end++) {
            const substring = str.slice(start, end);
            if (hasUniqueCharacters(substring)) {
                maxLength = Math.max(maxLength, substring.length);
            }
        }
    }

    return maxLength;
}
```

**Time Complexity**: $O(n^3)$  
**Space Complexity**: $O(n)$

---

### Approach 2: Sliding Window with Hash Set

We can optimize the brute-force approach by using the sliding window technique. The idea is to expand the window with the right pointer (`end`) and shrink the window from the left pointer (`start`) whenever we encounter a repeated character.

#### Steps:
1. Use a set to store characters in the current window.
2. Expand the window with the right pointer (`end`).
3. If a character repeats, shrink the window by moving the left pointer (`start`) until no characters repeat.
4. Track the maximum length of valid substrings.

#### Code:

```typescript
export function longestSubStringSlidingWindow(str: string): number {
    const seenChars = new Set<string>();
    let maxLength = 0;
    let start = 0;

    for (let end = 0; end < str.length; end++) {
        const currentChar = str[end];

        while (seenChars.has(currentChar)) {
            seenChars.delete(str[start]);
            start++;
        }

        seenChars.add(currentChar);
        maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;
}
```

**Time Complexity**: $O(n)$  
**Space Complexity**: $O(min(n, m))$, where $m$ is the size of the character set (e.g., 26 for lowercase English letters).

---

### Approach 3: Optimized Sliding Window with Hash Map

To further improve, we can use a hash map (or an object) to store the last seen position of each character. This allows us to skip the shrinking loop by directly moving the `start` pointer to the position after the previous occurrence of the repeating character.

#### Steps:
1. Traverse the string while keeping track of each character's last seen index in a hash map.
2. For each character, if it has been seen before and its last position is within the current window, update the `start` pointer.
3. Compute the length of the valid substring at each step and track the maximum length.

#### Code:

```typescript
export function longestSubStringOptimized(str: string): number {
    const lastSeen: Record<string, number> = {};
    let maxLength = 0;
    let start = 0;

    for (let end = 0; end < str.length; end++) {
        const currentChar = str[end];

        // If the character is repeated within the current window
        if (lastSeen[currentChar] !== undefined && lastSeen[currentChar] >= start) {
            start = lastSeen[currentChar] + 1;
        }

        // Update the character's last seen position
        lastSeen[currentChar] = end;

        // Update the maximum length of the substring
        maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;
}
```

**Time Complexity**: $O(n)$  
**Space Complexity**: $O(min(n, m))$, where $m$ is the size of the character set.

---

This approach shown in the image can be categorized as a variation of the **Sliding Window** technique that uses Python’s `find` method to search for characters within a specific range.

Let's include this method as a separate approach in the solution for the "Longest Substring Without Repeating Characters" problem.

---

### Approach 4: Sliding Window with `find()`

In this approach, we use the sliding window technique with Python’s built-in `find()` method to locate the last occurrence of a character within a substring between two pointers. This helps efficiently determine whether we need to update the start pointer to exclude the repeating character.

#### Steps:
1. Initialize `start` and `max_len` as 0.
2. Traverse the string using a loop. For each character at index `end`, use the `find()` method to get its last occurrence within the window from `start` to `end`.
3. If the character appears in the current window, update the `start` pointer to exclude that character.
4. Update the `max_len` at each step by calculating the length of the window.
5. Return the maximum length of the substring without repeating characters.

#### Code:

```python
def longest_sub_no_repeating(s: str) -> int:
    max_len = 0
    start = 0
    for end in range(len(s)):
        s_end_last_pos = s.find(s[end], start, end)
        if start <= s_end_last_pos < end:
            start = s_end_last_pos + 1
        max_len = max(max_len, end - start + 1)
    return max_len
```

**Time Complexity**: $O(n^2)$  
**Space Complexity**: $O(1)$ (no extra space besides variables)

#### Explanation:
- The `find()` method inside the loop makes this approach slower than the optimized hash map approach, as it searches for the last occurrence of each character in a substring, leading to a time complexity of $O(n^2)$.

---

### Summary of Approaches

| Approach                               | Time Complexity | Space Complexity | Explanation                                                                 |
|----------------------------------------|-----------------|------------------|-----------------------------------------------------------------------------|
| Brute Force                            | $O(n^3)$        | $O(n)$           | Checks every substring and tests if it contains unique characters.           |
| Sliding Window with Hash Set           | $O(n)$          | $O(min(n, m))$   | Uses a set to store characters in the current window and eliminate duplicates.|
| Optimized Sliding Window with Hash Map | $O(n)$          | $O(min(n, m))$   | Uses a hash map to store the last seen position of each character.            |
| Sliding Window with `find()`           | $O(n^2)$        | $O(1)$           | Uses the `find()` method to check for repeating characters in the current window.|

---

### Time and Space Complexity (General Explanation)

- **Time Complexity**: 
  - The brute force approach takes $O(n^3)$ because it involves generating all substrings ($O(n^2)$) and checking each for uniqueness ($O(n)$).
  - The sliding window approaches reduce the time complexity to $O(n)$ since each character is processed at most twice, once by the `start` pointer and once by the `end` pointer.
  
- **Space Complexity**:
  - Space complexity depends on the number of unique characters in the string. Using a set or hash map, the space complexity is $O(min(n, m))$, where $m$ is the number of unique characters (e.g., 26 for lowercase English). The brute force approach requires additional space to store substrings.

Let me know if you'd like any further clarifications or adjustments!


















