

[Find all anagrams problem (LeetCode #438) - Inside code](https://youtu.be/Y6DLFLceX7Q?si=063uWk5-oVINiXlI)

[LeetCode #242: Valid Anagram](https://leetcode.com/problems/valid-anagram)

[Valid Anagram - YT(InsideCode)](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=25s)

[LeetCode #49 - Group Anagrams](https://leetcode.com/problems/group-anagrams)

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Find All Anagrams in a String (LeetCode #438) - Inside Code

#### Problem Statement:
Given two strings, **`s`** and **`p`**, we are asked to return an array containing all the start indices of **`p`'s** anagrams in **`s`**. Both strings consist of lowercase English letters. 

##### Anagram Definition:
Two strings are **anagrams** if they are rearrangements of the same characters. For example, `"listen"` and `"silent"` are anagrams because they have the same character frequencies.

altered question: given two string is anagram or not!
#### Example:

Input:
- `s = "cbaebabacd"`, `p = "abc"`

Output:
- `[0, 6]`

Explanation:
- The substring starting at index 0 (`"cba"`) is an anagram of `"abc"`.
- The substring starting at index 6 (`"bac"`) is an anagram of `"abc"`.


### Approach 1: Brute Force (Inefficient Solution, Time Complexity: O(n*m))

One of the basic ways to solve this problem is to check every possible substring of length **`len(p)`** in **`s`** and verify if it is an anagram of **`p`**. This approach results in **O(n * m)** time complexity, where **n** is the length of **`s`** and **m** is the length of **`p`**.

#### Code (Brute Force):

```python
from collections import Counter

def find_anagrams_bruteforce(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    
    p_counter = Counter(p)  # Count of characters in 'p'
    result = []
    
    for i in range(len(s) - len(p) + 1):
        if Counter(s[i:i+len(p)]) == p_counter:  # Compare substring with 'p'
            result.append(i)
    
    return result
```


```python
from collections import Counter
def findAnagrams(self, s: str, p: str) -> List[int]:
	
	anagram_indices = []
	p_counter = Counter(p)
	
	p_len = len(p)
	s_len = len(s)
	
	for i in range(s_len-p_len+1):
		sub_str = s[i:i+p_len]
		if(Counter(sub_str) == p_counter):
			anagram_indices.append(i)
	
	return anagram_indices
```



#### Time Complexity:
- **Time Complexity**: For each starting index, we compare character counts using `Counter`, which takes **O(m)**. Therefore, the overall time complexity is **O(n * m)**.
- **Space Complexity**: We use extra space to store the frequency of characters in both **p** and each substring, which is **O(m)**.

### Approach 2: Optimized Sliding Window (Efficient Solution, Time Complexity: O(n))

#### Sliding Window Technique:
We optimize the solution by avoiding recalculating character frequencies for every substring. Instead, we use a **sliding window** to keep track of the frequency of characters in the current window of **`s`** and compare it with the frequency of characters in **`p`**. 

The key idea is to update the sliding window at each step: as we move the window forward, we:
1. **Remove** the character that goes out of the window.
2. **Add** the character that enters the window.

Since both **`s`** and **`p`** consist of lowercase letters, we can use a fixed-size array (of size 26) to store the frequency counts of each character.

#### Code (Optimized):

```python
from typing import List

def find_anagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []

    # Output list to store starting indices of anagrams
    output = []

    # Frequency maps for 's' and 'p', both with 26 elements (for lowercase letters 'a' to 'z')
    s_map = [0] * 26
    p_map = [0] * 26

    # Helper function to convert a character to an index (0 to 25)
    def char_to_index(c: str) -> int:
        return ord(c) - ord('a')

    # Initialize the frequency maps with the first window in 's' and all of 'p'
    for i in range(len(p)):
        s_map[char_to_index(s[i])] += 1
        p_map[char_to_index(p[i])] += 1

    # Compare the first window
    if s_map == p_map:
        output.append(0)

    # Traverse through the rest of 's', updating the sliding window
    for i in range(len(p), len(s)):
        # Remove the element that goes out of the window
        s_map[char_to_index(s[i - len(p)])] -= 1
        # Add the new element that enters the window
        s_map[char_to_index(s[i])] += 1

        # If current window matches 'p_map', it's an anagram
        if s_map == p_map:
            output.append(i - len(p) + 1)

    return output
```


```python
def findAnagrams(self, s: str, p: str) -> List[int]:
	anagram_indices = []
	p_len = len(p)
	s_len = len(s)
	
	if(s_len < p_len):
		return anagram_indices

	s_map = [0]*26
	p_map = [0]*26
	
	for i in p:
		p_map[ord(i)-ord('a')] += 1

	for i in range(p_len):
		index_char = s[i]
		s_map[ord(index_char) - ord('a')] += 1

	if(p_map == s_map):
		anagram_indices.append(0)

	for i in range(p_len,s_len):
		
		# removing last char
		last_char_index = i - p_len
		last_char = s[last_char_index]
		s_map[ord(last_char)- ord('a')] -= 1
		
		# putting current char
		current_char_map_index = ord(s[i]) - ord('a')
		s_map[current_char_map_index] += 1
		
		if(p_map == s_map):
			anagram_indices.append(last_char_index+1)
	
	return anagram_indices
```

if no.of possibe char is big, not just alphabetical ...  then use hash table.. 

### Time and Space Complexity Analysis:

- **Time Complexity**:
  - We traverse through the string **`s`** exactly once, and at each step, we update the sliding window, which takes **O(1)** due to constant size maps (26 letters).
  - Hence, the overall time complexity is **O(n)**, where **n** is the length of **`s`**.

$$
\text{Time Complexity} = O(n)
$$

- **Space Complexity**:
  - We use two arrays of size 26 to store the frequency counts of letters in **`p`** and the current window of **`s`**.
  - We also store the output array, which in the worst case could contain **O(n)** indices.
  
$$
\text{Space Complexity} = O(n)
$$

### Conclusion:
Using the sliding window technique, we optimized the brute-force approach to achieve **O(n)** time complexity. This solution efficiently finds all anagrams of **`p`** in **`s`** by maintaining a frequency map and updating it dynamically as the window slides across the string.






---




## Group Anagrams

#### Problem Statement

Given an array of strings `strs`, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, typically using all the original letters exactly once.

You can return the answer in **any order**.

#### Example

**Example 1**:
```plaintext
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**:
```plaintext
Input: strs = [""]
Output: [[""]]
```

**Example 3**:
```plaintext
Input: strs = ["a"]
Output: [["a"]]
```

#### Constraints:
- $1 \leq \text{strs.length} \leq 10^4$
- $0 \leq \text{strs[i].length} \leq 100$
- `strs[i]` consists of lowercase English letters.

---

### Approach 1: Sorting-Based Grouping

#### Explanation:
The key idea is that **anagrams**, when sorted, will result in the same string. Therefore, we can sort each string and use the sorted version as a key in a dictionary. All strings that map to the same sorted key are anagrams of each other.

Steps:
1. Iterate over the strings.
2. Sort each string and use it as a dictionary key.
3. Append each string to the list of values associated with its sorted key.
4. The dictionary's values will be the required groups of anagrams.

#### Code:

```python
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    # Dictionary to hold groups of anagrams
    anagram_groups = {}

    # Iterate through each string in the input list
    for string in strs:
        # Sort the string to use as the key for grouping
        sorted_str = ''.join(sorted(string))
        
        # Append the original string to the appropriate group
        if sorted_str not in anagram_groups:
            anagram_groups[sorted_str] = []
        anagram_groups[sorted_str].append(string)

    # Return all the values (groups of anagrams)
    return list(anagram_groups.values())
```

#### Time and Space Complexity:
- **Time Complexity**: Sorting each string takes $O(m \log m)$, where $m$ is the length of the string. For `n` strings, the overall time complexity is $O(n \cdot m \log m)$.
- **Space Complexity**: $O(n \cdot m)$ for the dictionary that stores the groups and the result.

---

### Approach 2: Character Count-Based Grouping

#### Explanation:
Instead of sorting, we can use a **character count** array of size 26 (for each letter in the alphabet) to represent each string. Two strings are anagrams if they have the same character frequencies.

Steps:
1. Create a frequency array for each string.
2. Use the tuple of this frequency array as the key in a dictionary.
3. Group strings by the same character frequency tuple.

#### Code:

```python
from typing import List

def group_anagrams_by_count(strs: List[str]) -> List[List[str]]:
    # Dictionary to hold groups of anagrams
    anagram_groups = {}

    # Iterate through each string
    for string in strs:
        # Create a count of 26 characters for each string
        count = [0] * 26
        for char in string:
            count[ord(char) - ord('a')] += 1
        
        # Use the character count tuple as the key for grouping
        count_tuple = tuple(count)
        if count_tuple not in anagram_groups:
            anagram_groups[count_tuple] = []
        anagram_groups[count_tuple].append(string)

    # Return all the values (groups of anagrams)
    return list(anagram_groups.values())
```

[Anagrams @InterviewBit](https://www.interviewbit.com/problems/anagrams/)

```
**Note:**

Ordering of the result :  
You should not change the relative ordering of the strings within the group suppose within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.

  
  
**Example Input**  

Input 1:

 A = [cat, dog, god, tca]

Input 2:

 A = [rat, tar, art]

  
  
**Example Output**  

Output 1:

 [ [1, 4],
   [2, 3] ]

Output 2:

 [ [1, 2, 3] ]
```

```python
def anagrams(A):
    anagram_groups = {}

    for i in range(len(A)):
        s = A[i]
        letter_counts = [0] * 26  # Initialize counts for 26 lowercase letters
        ascii_offset = ord('a')   # Offset to map 'a' to 0

        # Count occurrences of each letter in the string
        for c in s:
            letter_counts[ord(c) - ascii_offset] += 1

        # Use the letter counts as a key in the dictionary
        letter_counts_tuple = tuple(letter_counts)

        # Add the index to the appropriate anagram group
        if letter_counts_tuple not in anagram_groups:
            anagram_groups[letter_counts_tuple] = []
        anagram_groups[letter_counts_tuple].append(i + 1)

    # Return the list of anagram groups
    return list(anagram_groups.values())

```

#### Time and Space Complexity:
- **Time Complexity**: Building the count array for each string takes $O(m)$, where $m$ is the length of the string. For `n` strings, the overall time complexity is $O(n \cdot m)$.
- **Space Complexity**: $O(n \cdot m)$ for the dictionary that stores the groups and the result.

### Test Cases

```python
def test_group_anagrams(func):
    print(f"Testing function: {func.__name__}")

    test_cases = [
        {
            "name": "General Case",
            "input": ["eat", "tea", "tan", "ate", "nat", "bat"],
            "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        },
        {
            "name": "Empty String Case",
            "input": [""],
            "expected": [[""]],
        },
        {
            "name": "Single Character Strings",
            "input": ["a", "b", "c"],
            "expected": [["a"], ["b"], ["c"]],
        },
        {
            "name": "Duplicate Anagrams",
            "input": ["abc", "cba", "bca", "cab", "bac"],
            "expected": [["abc", "cba", "bca", "cab", "bac"]],
        },
        {
            "name": "All Identical Strings",
            "input": ["abc", "abc", "abc"],
            "expected": [["abc", "abc", "abc"]],
        },
        {
            "name": "Mixed Case",
            "input": ["race", "care", "acer", "hello", "lloeh"],
            "expected": [["race", "care", "acer"], ["hello", "lloeh"]],
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        # Sort the output and expected to compare unordered lists
        assert sorted([sorted(lst) for lst in result]) == sorted([sorted(lst) for lst in expected_output]), \
            f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")

# Example usage:
test_group_anagrams(group_anagrams)
test_group_anagrams(group_anagrams_by_count)
```

---

### Summary of Approaches

| Approach                        | Time Complexity        | Space Complexity       | Explanation                                                                                 |
|----------------------------------|------------------------|------------------------|---------------------------------------------------------------------------------------------|
| Sorting-Based Grouping           | $O(n \cdot m \log m)$   | $O(n \cdot m)$         | Sort each string, use it as a dictionary key for grouping anagrams.                         |
| Character Count-Based Grouping   | $O(n \cdot m)$          | $O(n \cdot m)$         | Use a character frequency array as a key for grouping anagrams. More efficient than sorting. |

- \( n \) is the number of strings.
- \( m \) is the length of the strings.

Both approaches work well, but the **Character Count-Based Grouping** is generally more efficient since it avoids sorting and works directly with frequency counts.

----


[[Valid Anagram]]



