\
[Leet Code #20](https://leetcode.com/problems/valid-parentheses/description/)



**Problem:** Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


## Valid Parentheses Checker

### Problem Statement
Given a string `s` containing the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

### Criteria for Validity
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples

- **Example 1:**
  - **Input:** `s = "()"`  
  - **Output:** `true`

- **Example 2:**
  - **Input:** `s = "()[]{}"`  
  - **Output:** `true`

- **Example 3:**
  - **Input:** `s = "(]"`  
  - **Output:** `false`

- **Example 4:**
  - **Input:** `s = "([])"`  
  - **Output:** `true`

### Constraints
- \( 1 \leq s.length \leq 10^4 \)
- `s` consists of parentheses only `()[]{}`.

### Solution Approach
Use a stack to track open brackets:
1. Push each opening bracket onto the stack.
2. For each closing bracket, check if it matches the top of the stack.
3. If they match, pop the stack; if not, return false.
4. At the end, if the stack is empty, return true; otherwise, return false.

**Answer:**


```python
   def isValid(self, s: str) -> bool:
        [b1, b2,b3] = [0,0,0]
        plus_b1 = "("
        plus_b2 = "["
        plus_b3 = "{"
        minus_b1 = ")"
        minus_b2 = "]"
        minus_b3 = "}"
        last_visited = []

        for i in s:
            if(i == plus_b1):
                b1 += 1
                last_visited.append(i)
            elif(i == plus_b2):
                b2 += 1
                last_visited.append(i)
            elif(i == plus_b3):
                b3 += 1
                last_visited.append(i)
            elif(i == minus_b1):
                if(not last_visited):
                    return False
                last = last_visited.pop()
                if(b1 == 0 or last != plus_b1):
                    return False
                b1 -= 1
            elif(i == minus_b2):
                if(not last_visited):
                    return False
                last = last_visited.pop()
                if(b2 == 0 or last != plus_b2):
                    return False
                b2 -= 1
            elif(i == minus_b3):
                if(not last_visited):
                    return False
                last = last_visited.pop()
                if(b3 == 0 or last != plus_b3):
                    return False
                b3 -= 1

        return len(last_visited) == 0

```



```python
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
```



```python
# just having counter is fine if we have single type of parenthesis
# ( => counter++ ,) => counter--, lastly counter == 0
```


```python
'''
Approach: STACK
- use stack to keep track of opening brackets
- when closing brackets comes, check stack's last element is respective opening brackets
Time : O(n) since iteration every char in string
Space : O(n) since pushing every item in stack (worst case)
'''
def is_valid_parenthesis1(str):
    stack = []
    brackets_mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # length must be even , open present will surely have close and viceversa
    if len(str)%2 != 0:
        return False

    for c in str:
        if brackets_mapping.get(c):
            # last item is in
            if not stack or stack[-1] != brackets_mapping[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return not stack


```



```python

'''
Approach: remove bracket_pairs one by one
- check whether str have substring of any bracket pairs
- if found, remove and recheck
- if not found, if str is empty, then valid else invalid
Time: O(n^2) -> 3*O(n) find substring in str * 3*O(n) replace substring in str
Space: O(n) -> str.replace creates new str
'''
def is_valid_parenthesis2(str):
    brackets = ['()', '{}', '[]']
    while any(x in str for x in brackets):
        for b in brackets:
            str = str.replace(b, '')
    return not str

```



```python
'''
Approach: remove bracket_pairs one by one using recursion
- find bracket_pairs and remove it
- if string become empty, then valid else check for next bracket_pairs
Time: O(n^2) - O(n) for finding bracket_pairs and O(n/2) for removing 2 chars and checking for next bracket_pairs
Space: O(n) - recursion stack, each recursion call will have new str but only 1 recursion call at a time, so one str at a time
'''
def is_valid_parenthesis3(str):
    if not str:
        return True

    for i in range(len(str) - 1):
        if (str[i] == '(' and str[i + 1] == ')') or \
           (str[i] == '{' and str[i + 1] == '}') or \
           (str[i] == '[' and str[i + 1] == ']'):
            # Remove the matching pair and recurse
            return is_valid_parenthesis3(str[:i] + str[i + 2:])

    return False

```



```python

'''
Approach: remove bracket_pairs using regex
- find bracket_pairs using regex pattern and remove it
- if string become empty, then valid else invalid
Time: O(n^2) - O(n) for finding bracket_pairs i.e re.search and O(n) for removing bracket_pairs i.e re.sub
Space: O(n) - new str created by re.sub, but only 1 str at a time in memory
'''
def is_valid_parenthesis4(str):
    # bracket_pairs's pattern => ['()', '{}', '[]']
    pattern = r'\(\)|\{\}|\[\]'
    while re.search(pattern, str):
        # replace empty string for bracket_pairs
        str = re.sub(pattern, '', str)
    return not str

```



### Tests

```python


valid_parenthesis_test_cases = [
    # Case 1: Simple valid case with parenthesis
    {
        'input': "()",
        'expected': True
    },
    # Case 2: Simple valid case with brackets
    {
        'input': "{}",
        'expected': True
    },
    # Case 3: Simple valid case with square brackets
    {
        'input': "[]",
        'expected': True
    },
    # Case 4: Mixed valid case
    {
        'input': "({[]})",
        'expected': True
    },
    # Case 5: Unmatched opening parenthesis
    {
        'input': "(((",
        'expected': False
    },
    # Case 6: Unmatched closing parenthesis
    {
        'input': ")))",
        'expected': False
    },
    # Case 7: Valid nested parenthesis
    {
        'input': "{[()]}",
        'expected': True
    },
    # Case 8: Invalid nested parenthesis
    {
        'input': "{[(])}",
        'expected': False
    },
    # Case 9: Empty string
    {
        'input': "",
        'expected': True
    },
    # Case 10: Long valid input
    {
        'input': "((()))[{}]",
        'expected': True
    },
    # Case 11: Long invalid input
    {
        'input': "((()))[{}]((())",
        'expected': False
    }
]

def test_is_valid_parenthesis(func):
    print(f"Testing: {func.__name__}")

    for i, test_case in enumerate(valid_parenthesis_test_cases, 1):
        input_data = test_case['input']
        expected_output = test_case['expected']
        result = func(input_data)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
    print("All test cases passed!")


```