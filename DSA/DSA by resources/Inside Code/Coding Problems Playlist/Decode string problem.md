
[Decode string problem (LeetCode #394) - Inside code](https://youtu.be/6KIhWERTAG8?si=N-C5nBJ8mYx7oUWu)


## Decode String Problem (LeetCode #394)

In this blog, we'll tackle the **Decode String** problem, which is a challenging and frequently asked coding problem. 
### Problem Statement:
You are given an encoded string `s`, and your task is to decode it. The encoding rule is:
- A positive integer `k` followed by a string inside square brackets `[ ]`. This string has to be repeated `k` times in the final output.

#### Example:
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```
In this example:
1. First, decode the inner string `2[c]` to get `cc`.
2. Then, decode the outer string `3[a(cc)]` to get `accaccacc`.

### Constraints:
- The input string `s` is always valid (no extra brackets or invalid characters).
- Nested encoded strings are allowed with no limit to the depth.

---

## Solution 1: Recursion

This approach leverages recursion to decode nested expressions. The idea is to decode each subexpression first, then combine them to form the final decoded string.

### Approach:
1. **Traverse the string** character by character.
2. When you encounter a letter, add it to the decoded string.
3. When you encounter a number, it indicates the start of an encoded string. 
   - Find the corresponding closing bracket by tracking the bracket depth.
   - Recursively decode the substring inside the brackets and repeat it based on the number found before the brackets.
4. Continue this process until the entire string is decoded.

### Code (with comments):

```python
# Helper function to find the end of an expression by matching brackets
def getExpressionEnd(s, start):
    depth = 1  # track the depth of nested brackets
    i = start
    while i < len(s):
        if s[i] == '[':
            depth += 1
        elif s[i] == ']':
            depth -= 1
            if depth == 0:
                return i  # found the matching closing bracket
        i += 1

# Main function to decode the string recursively
def decodeString(s):
    decoded = ""  # to accumulate decoded result
    i = 0
    while i < len(s):
        if s[i].isalpha():  # if it's a letter, add it to the result
            decoded += s[i]
        elif s[i].isnumeric():  # if it's a number, decode the upcoming encoded string
            count = 0
            while s[i].isnumeric():  # handle multi-digit numbers
                count = count * 10 + int(s[i])
                i += 1
            expStart = i + 1  # the start of the encoded substring
            expEnd = getExpressionEnd(s, expStart)  # find the end of the substring
            # Recursively decode the substring and repeat it 'count' times
            decoded += count * decodeString(s[expStart:expEnd])
            i = expEnd  # move the pointer to the end of the current encoded substring
        i += 1  # move to the next character
    return decoded
```

### Time Complexity:
- **O(n²)**: In the worst case, we traverse the entire string multiple times (nested decoding). For example, the outermost expression requires processing the whole string, then the inner expression, and so on.
  
### Space Complexity:
- **O(n)**: Recursion consumes space proportional to the depth of the nested structure.

---

## Solution 2: Regular Expressions

This approach leverages regular expressions to iteratively find and decode encoded substrings.

### Approach:
1. Use a regular expression to find patterns of the form `k[encoded_string]`.
2. Replace each matched pattern with the decoded result by repeating the substring `k` times.
3. Continue this process until no more encoded substrings are left.

### Code:

```python
import re

# Helper function to decode a single match (e.g., 3[abc])
def decodeMatch(match):
    count = match[0:match.index('[')]
    string = match[match.index('[') + 1:-1]
    return int(count) * string  # repeat the string 'count' times

# Main function to decode the string using regular expressions
def decodeString(s):
    while '[' in s:
        # Find patterns like 3[abc] and replace them with their decoded version
        s = re.sub(r"[0-9]+\[[a-z]+\]", lambda match: decodeMatch(match.group(0)), s)
    return s
```

### Time Complexity:
- **O(n²)**: In each iteration, the regular expression scans the entire string to find patterns, and decoding each pattern can take linear time.

### Space Complexity:
- **O(n)**: The decoded result is stored in a new string, so space grows linearly with the input size.

---

## Solution 3: Stack (Optimized Solution)

This is the most efficient approach, using a **stack** to handle nested expressions.

### Approach:
1. Traverse the string character by character.
2. When encountering a letter, append it to the current decoded string.
3. When encountering a number, it signals the start of an encoded string. Push the current decoded string and number to the stack, then start decoding the inner substring.
4. When encountering a closing bracket `]`, pop the stack to get the previous decoded string and number. Repeat the inner decoded string and append it to the previous string.
5. Continue until the entire string is decoded.

### Code:

```python
def decodeString(s):
    stack = []  # stack to store previous decoded parts and counts
    decoded = []  # current decoded string
    count = 0  # current multiplier for the encoded string
    
    for ch in s:
        if ch.isalpha():
            decoded.append(ch)  # add letters to the current decoded string
        elif ch.isnumeric():
            count = count * 10 + int(ch)  # handle multi-digit numbers
        elif ch == '[':
            stack.append((count, decoded))  # push current state to stack
            decoded = []  # reset decoded for the new encoded substring
            count = 0  # reset count for the next multiplier
        elif ch == ']':
            prev_count, prev_decoded = stack.pop()  # pop previous state from stack
            decoded = prev_decoded + prev_count * decoded  # repeat the decoded substring
            
    return ''.join(decoded)  # join the decoded list into a final string
```

### Time Complexity:
- **O(n)**: We traverse the string once, and each character is processed in constant time. Repeating the string when encountering a multiplier is done efficiently.

### Space Complexity:
- **O(n)**: The stack stores intermediate decoded strings and multipliers. The space required grows with the depth of nesting.

---

### Conclusion:
We’ve explored three approaches to solve the **Decode String** problem:
1. **Recursion** offers a clear approach for nested structures but is less efficient.
2. **Regular expressions** provide a concise solution but may be slower for larger inputs.
3. **Stack-based solution** is the most efficient in terms of time complexity, handling the problem in linear time.

By understanding each method’s strengths and weaknesses, you can choose the most suitable one based on the constraints of the input.









