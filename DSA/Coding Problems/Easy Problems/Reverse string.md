

•	Problem: Write a function that reverses a string.
•	Example:
Input: "hello"
Output: "olleh"



```python
# Approach:
# - Use Python's slicing to reverse the string.
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string1(text):
  return text[::-1]

```


```python
# Approach:
# - Iterate over the string from the last character to the first.
# - Append each character to a new string.
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string2(text):
  text_length = len(text)
  new_text = ''
  for i in range(text_length):
    new_text += text[text_length-1-i]
  return new_text
```



```python
# Approach:
# - Convert string to a list, use two pointers (start and end).
# - Swap characters until pointers meet in the middle.
# - Convert the list back to a string.
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string3(text):
    text_list = list(text)
    [left_ptr, right_ptr] = [0, len(text)-1]
    while left_ptr < right_ptr:
        text_list[left_ptr], text_list[right_ptr] = text_list[right_ptr], text_list[left_ptr]
        left_ptr, right_ptr = left_ptr+1, right_ptr-1
    return ''.join(text_list)

```


```python
# Approach:
# - Use Python’s built-in `reversed()` function and join the reversed characters.
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string4(text):
    return ''.join(reversed(text))
```



```python

# Approach: STACK
# - Convert string to a list.
# - Use `.pop()` to remove and append the last element to a new string.
# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse_string5(text):
    [new_text, text_list] = ['', list(text)]
    while len(text_list):
        new_text += text_list.pop()
    return new_text

```



```python
# Approach:
# - Use recursion to reverse the string.
# - Base case: empty string.
# - Recursive case: take the last character and reverse the rest of the string.
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursive call stack.
def reverse_string6(text):
    if len(text) == 0:
        return ''
    return text[-1] + reverse_string6(text[:-1])

```

### Test

```python

reverse_string_test_cases = [
    {
        'input': 'OpenAI',
        'expected': 'IAnepO'
    },
    {
        'input': 'racecar',
        'expected': 'racecar'  # Palindrome, expected output is the same as input
    },
    {
        'input': 'abcdefg',
        'expected': 'gfedcba'
    },
     {
        'input': 'hello!',
        'expected': '!olleh'
    },
    {
        'input': '12345',
        'expected': '54321'
    },
    {
        'input': 'Was it a car or a cat I saw?',
        'expected': '?was I tac a ro rac a ti saW'
    },
    {
        'input': 'Spaces   in   between',
        'expected': 'neewteb   ni   secapS'  # Reverses everything including spaces
    },
    {
        'input': 'Special chars: @#$%^&*()_+=-',
        'expected': '-=+_)(*&^%$#@ :srahc laicepS'
    },
    {
        'input': 'A man, a plan, a canal, Panama!',
        'expected': '!amanaP ,lanac a ,nalp a ,nam A'  # Reverses punctuation and spacing
    },
    {
        'input': '123 abc 456 DEF',
        'expected': 'FED 654 cba 321'
    },
    {
        'input': 'Palindrome: madam',
        'expected': 'madam :emordnilaP'  # Special case with palindrome word inside
    },
    {
        'input': 'Whitespace    test    ',
        'expected': '    tset    ecapsetihW'  # Handling trailing and leading spaces
    },
    {
        'input': '!@#$%^&*()',
        'expected': ')(*&^%$#@!'  # Only special characters
    },
    {
        'input': '',
        'expected': ''  # Empty string remains empty
    },
]

def reverse_string_tests(func):
    print(f"Testing function: {func.__name__}")
    for i, test_case in enumerate(reverse_string_test_cases, 1):
        input_data = test_case['input']
        expected_output = test_case['expected']
        result = func(input_data)
        # print(input_data,result)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
    print("Finished all passed!")



```












