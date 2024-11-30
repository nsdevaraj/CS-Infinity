
[? Minimum WIndow Substring @LeetCode#76](https://leetcode.com/problems/minimum-window-substring/)

[Min window substring @InsideCode](https://youtu.be/o3DUXPRyvT8?si=VAgbcWvTuNIQjM9d&t=4812)



### Problem Description: Minimum Window Substring

Given two strings `full_str` and `contain_str`, your task is to find the smallest substring in `full_str` that contains all the characters (including duplicates) of `contain_str`. If no such substring exists, return an empty string.

### Example:

**Input:**
- `full_str`: "ADOBECODEBANC"
- `contain_str`: "ABC"

**Output:**
- "BANC"

### Explanation:
In the input example, the substring "BANC" is the smallest substring in "ADOBECODEBANC" that contains all the characters 'A', 'B', and 'C' from `contain_str`. Other valid substrings like "ADOBEC" and "CODEBA" are longer than "BANC".

The testcases will be generated such that the answer is **unique**.

```md

**Example 1:**

**Input:** s = "ADOBECODEBANC", t = "ABC"
**Output:** "BANC"
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

**Example 2:**

**Input:** s = "a", t = "a"
**Output:** "a"
**Explanation:** The entire string s is the minimum window.

**Example 3:**

**Input:** s = "a", t = "aa"
**Output:** ""
**Explanation:** Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

```


### Brute Force





```python
# LeetCode : 233 / 268 testcases passed
from collections import Counter
from typing import Dict

def min_window(full_str: str, contain_str: str) -> str:
    # Get lengths of the input strings
    full_str_len, contain_str_len = len(full_str), len(contain_str)

    # Return empty string if the full string is shorter than the contain string
    if full_str_len < contain_str_len or contain_str_len == 0:
        return ''
    
    CountType = Dict[str, int]
    # Count frequency of characters in the contain_str
    contain_str_freq: CountType = Counter(contain_str)

    # Initialize minimum substring to a large value
    min_sub_str = ' ' * (full_str_len + 1)

    # Function to check if the current substring covers all characters in contain_str
    def is_valid_substr(substring_counter: CountType) -> bool:
        for ch in contain_str_freq:
            if contain_str_freq[ch] > substring_counter[ch]):
                return False
        return True

    # Iterate over all possible substrings of full_str
    for sub_str_len in range(contain_str_len, full_str_len + 1):
        for sub_str_start in range(full_str_len - sub_str_len + 1):
            sub_str: str = full_str[sub_str_start: (sub_str_start + sub_str_len)]
            sub_str_freq: CountType = Counter(sub_str)

            # Update min_sub_str if the current substring is valid and shorter
            if is_valid_substr(sub_str_freq) and len(sub_str) < len(min_sub_str):
                min_sub_str = sub_str

    return min_sub_str if len(min_sub_str) <= full_str_len else ""

# Example usage
result = min_window("ADOBECODEBANC", "ABC")
print(result)  # Expected output: "BANC"
```

#### Time and Space Complexity:
- **Time Complexity**: \(O(n^2 \cdot m)\)
  - The outer loop iterates over the lengths of substrings (up to \(n\)), and the inner loop generates all possible substrings (up to \(n\)), with a character frequency check that takes \(O(m)\), where \(m\) is the length of `contain_str`.
  
- **Space Complexity**: \(O(m+n)\)
  - The space used for the `Counter` to store the frequency of characters in `contain_str`  and `sub_str` is \(O(m+n)\).


### Sliding window



```python
# LeetCode:  264 / 268 testcases passed

from collections import Counter
from typing import Dict

def min_window(full_str: str, contain_str: str) -> str:
    full_str_len, contain_str_len = len(full_str), len(contain_str)

    # Early return if the full string is shorter than the required characters
    if full_str_len < contain_str_len or contain_str_len == 0:
        return ''

    # Frequency count of characters in the containing string
    contain_str_freq: Dict[str, int] = Counter(contain_str)
    min_sub_str = ' ' * (full_str_len + 1)  # Initialize with a placeholder longer than any possible substring

    def is_valid_substring(substring_counter: Dict[str, int]) -> bool:
        """Check if the substring counter has at least the frequency of each char in contain_str_freq."""
        return all(substring_counter[ch] >= contain_str_freq[ch] for ch in contain_str_freq)

    # Iterate through all possible substring lengths
    for sub_str_len in range(contain_str_len, full_str_len + 1):
        sub_str_freq: Dict[str, int] = None
        # Slide the window across full_str
        for sub_str_start in range(full_str_len - sub_str_len + 1):
            sub_str_end = sub_str_start + sub_str_len - 1
            sub_str = full_str[sub_str_start:sub_str_end + 1]

            # Initialize or update the frequency counter for the current substring
            if sub_str_freq is None:
                sub_str_freq = Counter(sub_str)
            else:
			    # SLIDING WINDOW
                # Adjust the frequency by removing the leftmost char and adding the new rightmost char
                visited_char, visiting_char = full_str[sub_str_start - 1], full_str[sub_str_end]
                sub_str_freq[visited_char] -= 1
                #if sub_str_freq[visited_char] == 0:
                #    del sub_str_freq[visited_char]  # Clean up zero count
                sub_str_freq[visiting_char] += 1

            # Check if the current substring is valid and shorter than the current minimum
            if is_valid_substring(sub_str_freq) and len(sub_str) < len(min_sub_str):
                min_sub_str = sub_str

    return min_sub_str if len(min_sub_str) <= full_str_len else ""

# Time Complexity: O(n^2), where n is the length of the full string. 
# For each substring length, we check every possible starting index.
# Space Complexity: O(n+m), where m is the size of the contain_str and n is size of sub_str, for storing its character counts.

```




---
### Sliding window + optimized sliding validity check


```python
# LeetCode 265 / 268 testcases passed

from collections import Counter
from typing import Dict

class Solution:
    def minWindow(self, full: str, contain: str) -> str:
        
        # Get the lengths of `full` and `contain`
        full_len, contain_len = len(full), len(contain)

        # If `full` is shorter than `contain` or `contain` is empty, return an empty string
        if full_len < contain_len or contain_len == 0:
            return ''
        
        # Define type for character frequency dictionary
        CountType = Dict[str, int]
        
        # Count character frequencies in `contain`
        contain_freq: CountType = Counter(contain)

        # Initialize variables to track the smallest window (start and end positions)
        final_start, final_end = 0, full_len + 1

        # Iterate over all possible substring lengths starting from the length of `contain`
        for sub_len in range(contain_len, full_len + 1):
            
            sub_freq: CountType | None = None  # Counter to track frequency of chars in the current window
            sub_freq_keys_equal = 0  # Track how many chars in `sub_freq` match the count in `contain_freq`
            
            # Calculate max starting index for current substring length
            sub_start_max = full_len - sub_len
            
            # Slide the window of length `sub_len` over `full`
            for sub_start in range(sub_start_max + 1):
                sub_end = sub_start + sub_len - 1

                # Initialize frequency counter for the first window of the current length
                # if sub_start == 0:
                if sub_freq is None:
                    sub_freq = Counter()
                    # Populate `sub_freq` with the initial substring characters
                    for c_idx in range(sub_start, sub_end + 1):
                        ch = full[c_idx]
                        sub_freq[ch] += 1
                        # Check if this char now meets the required frequency
                        if ch in contain_freq and contain_freq[ch] == sub_freq[ch]:
                            sub_freq_keys_equal += 1
                else:
                    # Sliding window: adjust `sub_freq` by removing the previous char and adding the new one
                    prev_ch, added_ch = full[sub_start - 1], full[sub_end]
                    
		            # if removing and add char same, no change in freq
		            if(prev_ch == added_ch):
						continue
					
					# Decrement frequency of `prev_ch` and update `sub_freq_keys_equal` if necessary
					if prev_ch in contain_freq and contain_freq[prev_ch] == sub_freq[prev_ch]:
						sub_freq_keys_equal -= 1
					sub_freq[prev_ch] -= 1
					
					# Increment frequency of `added_ch` and update `sub_freq_keys_equal` if necessary
					sub_freq[added_ch] += 1
					if added_ch in contain_freq and contain_freq[added_ch] == sub_freq[added_ch]:
						sub_freq_keys_equal += 1
                    
                # If `sub_freq` contains all required chars at the needed frequencies, check if it's the smallest
                if sub_freq_keys_equal == len(contain_freq) and sub_len < (final_end - final_start + 1):
                    final_start, final_end = sub_start, sub_end
        
        # Return the smallest valid window or an empty string if no such window was found
        return full[final_start:final_end + 1] if final_end - final_start + 1 <= full_len else ""

# Time Complexity: O(n^2), where `n` is the length of `full`.
# - The outer loop iterates over possible substring lengths, and the inner loop slides the window across `full`.
# - In each window adjustment, character counting is done in O(1) on average using a hash map.

# Space Complexity: O(m), where `m` is the number of unique characters in `contain`.
# - We use additional space for `contain_freq` and `sub_freq` to store character counts.

```



Inside Code's answer:

Here's a refactored version of your code, including comments to clarify each part of the logic:

```python
from collections import Counter
from typing import Tuple

def min_window(s: str, t: str) -> str:
    # Lengths of the input strings
    n, m = len(s), len(t)

    # Early return if t is longer than s or t is empty
    if m > n or t == "":
        return ""

    # Frequency map for characters in t
    freqt = Counter(t)

    # Initialize variables to keep track of the best window
    start, end = 0, n + 1

    # Iterate over all possible substring lengths starting from 1 to n
    for length in range(1, n + 1):
        # Counter for the current window in s
        freqs = Counter()
        satisfied = 0  # Count of characters in s that meet the frequency requirements in t

        # Initial window setup (first 'length' characters)
        for ch in s[:length]:
            freqs[ch] += 1
            if ch in freqt and freqs[ch] == freqt[ch]:
                satisfied += 1

        # Check if the initial window meets the requirements
        if satisfied == len(freqt) and length < end - start:
            start, end = 0, length

        # Sliding the window across s with current length
        for i in range(1, n - length + 1):
            # Add the next character to the window (right end)
            freqs[s[i + length - 1]] += 1
            if s[i + length - 1] in freqt and freqs[s[i + length - 1]] == freqt[s[i + length - 1]]:
                satisfied += 1

            # Remove the character that is no longer in the window (left end)
            if s[i - 1] in freqt and freqs[s[i - 1]] == freqt[s[i - 1]]:
                satisfied -= 1
            freqs[s[i - 1]] -= 1

            # Check if the current window satisfies all character requirements and is shorter than previous
            if satisfied == len(freqt) and length < end - start:
                start, end = i, i + length

    # Return the smallest valid window or an empty string if no window was found
    return s[start:end] if end - start <= n else ""
```

### Explanation of Refactoring and Added Comments

1. **Early Return Check**:
   - We check if `t` is longer than `s` or if `t` is empty. If so, we return an empty string immediately.

2. **Frequency Map for Target String**:
   - We create a `Counter` called `freqt` to store the frequency of each character in `t`. This helps us quickly check the requirements for each character in `t`.

3. **Outer Loop (Over Lengths)**:
   - We iterate over all possible substring lengths from `1` to `n`. The idea here is to use a sliding window of a fixed length in each iteration to find valid substrings that contain all characters from `t`.

4. **Initial Window Setup**:
   - For each `length`, we initialize a window of that length at the beginning of `s`. We count the characters in this initial window and check if it meets the frequency requirements in `t`.

5. **Inner Loop (Sliding Window)**:
   - We slide the window from left to right across `s`, adjusting the character counts as characters enter and leave the window.
   - **Add the Next Character**: The character at the right end of the window is added to `freqs`. If this addition satisfies a requirement in `t`, we increase `satisfied`.
   - **Remove the Leftmost Character**: The character that leaves the window from the left end has its count reduced in `freqs`. If this reduction causes a requirement in `t` to no longer be satisfied, we decrease `satisfied`.

6. **Checking Window Validity**:
   - If the current window satisfies all character requirements and is shorter than any previously found valid window, we update `start` and `end` to mark the bounds of this new smallest window.

7. **Return the Result**:
   - Finally, we return the smallest valid substring found. If no valid substring was found, we return an empty string.

### Complexity Analysis

- **Time Complexity**: The time complexity of this approach is \( O(n^2) \), because we examine each substring length from 1 to \( n \), and for each length, we slide a window across the string \( s \).
  
- **Space Complexity**: The space complexity is \( O(n + m) \):
  - \( O(m) \) for storing `freqt`, the frequency map of `t`.
  - \( O(n) \) for storing `freqs`, the frequency map for the sliding window in `s`.


---

## Sliding window and jumping substrings of valid ones optimally


```python
# LeetCode 268 / 268 testcases passed

from collections import Counter
from typing import Dict

def minWindow(full: str, contain: str) -> str:
    full_len, contain_len = len(full), len(contain)

    # Edge case: if `contain` is longer than `full` or `contain` is empty, return empty string
    if full_len < contain_len or contain_len == 0:
        return ''
    
    # Define the frequency dictionary for `contain`
    contain_freq: Dict[str, int] = Counter(contain)

    # Initialize pointers and the result window boundaries
    first, last = 0, full_len + 1
    left, right = 0, 0

    # `sub_freq` keeps track of the frequency of characters in the current window
    sub_freq = Counter()
    sub_freq_keys_equal = 0  # Number of characters that satisfy `contain_freq` requirement in the window

    # Start expanding the window with the `right` pointer
    while right < full_len:
        # Expand the window by including the character at `right`
        right_char = full[right]
        sub_freq[right_char] += 1

        # If this character meets the frequency requirement, increment `sub_freq_keys_equal`
        if right_char in contain_freq and sub_freq[right_char] == contain_freq[right_char]:
            sub_freq_keys_equal += 1

        # Now try to shrink the window from the left if all required characters are satisfied
        while sub_freq_keys_equal == len(contain_freq):
            # Update the smallest window if the current one is smaller
            if right - left + 1 < last - first + 1:
                first, last = left, right

            # Try to remove the character at `left` from the window and move `left` forward
            left_char = full[left]
            sub_freq[left_char] -= 1

            # If removing `left_char` causes it to no longer meet the required frequency, adjust `sub_freq_keys_equal`
            if left_char in contain_freq and sub_freq[left_char] < contain_freq[left_char]:
                sub_freq_keys_equal -= 1

            left += 1  # Move the `left` pointer to the right

        # Move the `right` pointer to the next character to expand the window
        right += 1

    # Return the smallest window if one was found; otherwise, return an empty string
    return full[first:last+1] if last < full_len else ""


```


Inside code's soln:

Here’s the code you provided, with detailed comments explaining each part and the time and space complexity analysis at the end.

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    n, m = len(s), len(t)

    # Edge case: if `t` is longer than `s` or `t` is empty, no valid window exists
    if m > n or t == "":
        return ""

    # Frequency count of each character in `t`
    freqt = Counter(t)

    # Variables to store the start and end of the smallest window found
    start, end = 0, n

    # `satisfied` counts how many characters have met the required frequency from `t`
    satisfied = 0

    # Frequency count of the current window in `s`
    freqs = Counter()

    # Left pointer for the sliding window
    left = 0

    # Expand the window by moving the right pointer
    for right in range(n):
        # Add the character at `right` to the window frequency count
        freqs[s[right]] += 1

        # If this character meets the frequency requirement in `t`, increment `satisfied`
        if s[right] in freqt and freqs[s[right]] == freqt[s[right]]:
            satisfied += 1

        # Check if all characters in `t` are satisfied in the current window
        if satisfied == len(freqt):
            # Contract the window by moving the left pointer to find the minimum length window
            while s[left] not in freqt or freqs[s[left]] > freqt[s[left]]:
                freqs[s[left]] -= 1  # Remove `s[left]` from the window count
                left += 1            # Move the left pointer to the right

            # Update the smallest window if the current one is smaller
            if right - left + 1 < end - start + 1:
                start, end = left, right

    # Return the smallest window if found, otherwise return an empty string
    return s[start:end + 1] if end - start + 1 <= n else ""

# Time Complexity: O(n+m), where `n` is the length of `s`.m is for counter for `t`
# - Each character in `s` is visited at most twice, once by the right pointer and once by the left pointer.

# Space Complexity: O(m+n), where `m` is the number of unique characters in `t` and `s` for frequency storage.

```

### Explanation of Time and Space Complexity
- **Time Complexity**: \( O(n) \)
  - The sliding window approach ensures that each character in `s` is processed at most twice (once when expanding the right end, and once when contracting the left end), leading to an overall linear time complexity.
  
- **Space Complexity**: \( O(m) \)
  - We use additional space for the frequency counters `freqt` and `freqs`, which store counts for each unique character in `t`. This space usage depends on the number of unique characters in `t`, so it's \( O(m) \).


### others better soln from leet code:

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needstr = collections.defaultdict(int)
        for ch in t:
            needstr[ch] += 1
        needcnt = len(t)
        res = (0, float('inf'))
        start = 0
        for end, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1
            if needcnt == 0:
                while True:
                    tmp = s[start]
                    if needstr[tmp] == 0:
                        break
                    needstr[tmp] += 1
                    start += 1
                if end - start < res[1] - res[0]:
                    res = (start, end)
                needstr[s[start]] += 1
                needcnt += 1
                start += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
```




```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_s = Counter()
        counter_t = Counter(t)

        def all_present(counter_s, counter_t):
            for c in counter_t:
                if counter_s[c] < counter_t[c]:
                    return False
            return True

        left = 0
        right = 0
        result = None

        while right < len(s):
            counter_s[s[right]] += 1
            right += 1
            
            while all_present(counter_s, counter_t):
                if result is None:
                    result = s[left:right]
                else:
                    if len(s[left:right]) < len(result):
                        result = s[left:right]
                
                counter_s[s[left]] -= 1
                left += 1
        
        if result is None:
            return ""
        
        return result
        
```


---

### Minimum Window Substring

**LeetCode Problem**: [Minimum Window Substring (#76)](https://leetcode.com/problems/minimum-window-substring/)

---

### Problem Statement

Given two strings, `s` and `t`, find the smallest substring in `s` that contains all the characters of `t`. If there is no such substring, return an empty string `""`. When multiple substrings meet this criterion, return the substring with the minimum length.

**Examples:**

1. **Input**: `s = "ADOBECODEBANC"`, `t = "ABC"`
   - **Output**: `"BANC"`
2. **Input**: `s = "a"`, `t = "a"`
   - **Output**: `"a"`
3. **Input**: `s = "a"`, `t = "aa"`
   - **Output**: `""` (since `t` cannot be fully contained in `s`)

---

### Approach 1: Sliding Window with Hash Maps

The sliding window technique is optimal for problems involving substrings and substrings with certain conditions. Here, we will use two pointers (or indices) to form a "window" over the string `s` and check if each window contains all characters of `t`.

**Steps:**

1. **Frequency Maps**:
   - Create a frequency map for characters in `t`, as it specifies the required characters and their counts.
   - Use another map for the current window's characters in `s`.

2. **Sliding Window**:
   - Expand the window by moving the `right` pointer, adding characters to the window map.
   - When the window contains all characters from `t` (i.e., meets the required frequency), try to minimize it by moving the `left` pointer.
   - Update the result when a valid window is found with a smaller size than previously recorded.

3. **Result**:
   - Continue expanding and shrinking the window until `right` reaches the end of `s`.
   - Return the smallest window recorded or an empty string if no valid window is found.

**Code:**

```python
from collections import Counter
from typing import Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Frequency map for characters in `t`
        required = Counter(t)
        window_counts = Counter()
        
        # Initialize pointers and helper variables
        left, right = 0, 0
        have, need = 0, len(required)
        min_len = float("inf")
        result = ""
        
        # Expand the window to include `right` pointer's character
        while right < len(s):
            char = s[right]
            window_counts[char] += 1
            
            # Check if the current character meets the requirement in the window
            if char in required and window_counts[char] == required[char]:
                have += 1
            
            # When we meet all character requirements, start minimizing the window
            while have == need:
                # Check if this window is the smallest so far
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]
                
                # Move `left` pointer to shrink the window
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in required and window_counts[left_char] < required[left_char]:
                    have -= 1
                left += 1
            
            # Move `right` pointer to expand the window
            right += 1
        
        return result
```

**Explanation**:

- **Two Hash Maps**:
  - `required`: stores the count of each character in `t`.
  - `window_counts`: tracks character counts within the current window in `s`.

- **Condition Check**:
  - The `have` counter is incremented whenever a character in `window_counts` reaches the required frequency in `t`.
  - When `have == need`, it means the current window contains all characters of `t`.

**Time Complexity**:  
The time complexity is \( O(n + m) \), where \( n \) is the length of `s` and \( m \) is the length of `t`, as we potentially visit each character once with the sliding window.

**Space Complexity**:  
The space complexity is \( O(m) \), where \( m \) is the unique number of characters in `t`.

---

### Approach 2: Optimized Sliding Window with Fewer Comparisons

Instead of checking the entire window on every character addition, we can directly use `Counter` to track differences.

**Steps**:

1. Maintain only the necessary counts and a mismatch count.
2. Adjust the mismatch count based on the character additions and removals.
3. Update the result whenever the mismatch count becomes zero.

**Code**:

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Frequency map for characters in `t`
        required = Counter(t)
        mismatch = len(required)
        left, result = 0, (float("inf"), None, None)
        
        # Sliding window approach
        for right, char in enumerate(s):
            if char in required:
                required[char] -= 1
                if required[char] == 0:
                    mismatch -= 1
            
            # Contract window to minimal valid state
            while mismatch == 0:
                # Update minimum window result
                if right - left < result[0]:
                    result = (right - left, left, right)
                
                # Prepare to move left pointer and update counts
                if s[left] in required:
                    if required[s[left]] == 0:
                        mismatch += 1
                    required[s[left]] += 1
                left += 1
        
        return "" if result[0] == float("inf") else s[result[1]:result[2] + 1]
```

**Explanation**:

This approach reduces repeated comparisons by managing the mismatch count directly with character additions and removals.

**Time Complexity**: \( O(n + m) \)

**Space Complexity**: \( O(m) \)

---

### Summary of Approaches:

| Approach                           | Time Complexity   | Space Complexity | Description                                             |
|------------------------------------|-------------------|------------------|---------------------------------------------------------|
| Sliding Window with Hash Maps      | \( O(n + m) \)   | \( O(m) \)       | Uses two hash maps to track character counts and sliding window conditions |
| Optimized Sliding Window           | \( O(n + m) \)   | \( O(m) \)       | Minimizes redundant checks by tracking mismatches |

---

### Testing Function

To ensure our solutions are robust, let’s define a set of diverse test cases.

```python
def test_minWindow(func):
    test_cases = [
        {"input": ("ADOBECODEBANC", "ABC"), "expected": "BANC"},   # General case
        {"input": ("a", "a"), "expected": "a"},                    # Single char match
        {"input": ("a", "aa"), "expected": ""},                    # Single char no match
        {"input": ("abc", "cba"), "expected": "abc"},              # Exact match with all chars
        {"input": ("abdecfabcf", "abcf"), "expected": "abcf"},     # Smallest window within other valid windows
        {"input": ("abcdefgh", "z"), "expected": ""},              # No matching char
        {"input": ("aaabbcc", "abc"), "expected": "abbc"},         # Multiple occurrences, smallest needed
        {"input": ("baaaabc", "aab"), "expected": "aaab"},         # Overlapping chars with minimum coverage
        {"input": ("ADOBECODEBANCCBA", "ABC"), "expected": "BANC"},# Repeated solution match in string
    ]
    
    for i, test in enumerate(test_cases):
        result = func(*test["input"])
        assert result == test["expected"], f"Test case {i+1} failed: Expected {test['expected']}, got {result}"
    print("All test cases passed!")

# Test with both solutions
solution = Solution()
test_minWindow(solution.minWindow)
```




---




to check {

https://www.interviewbit.com/problems/window-string/

https://www.hackerearth.com/problem/algorithm/minimum-substring-1-1421cac2/

https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

https://algo.monster/liteproblems/76

https://prepinsta.com/leetcode-top-100-liked-questions-with-solution/minimum-window-substring/

https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

https://www.geeksforgeeks.org/problems/smallest-distant-window3132/1


}