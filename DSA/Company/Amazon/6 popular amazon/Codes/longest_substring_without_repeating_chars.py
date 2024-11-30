longest_substring_test_cases = [
    # Case 1: Basic example with repeating characters
    {
        "name": "Basic Example",
        "input": "abcabcbb",
        "expected": 3,
    },
    # Case 2: All characters are the same
    {
        "name": "All Same Characters",
        "input": "bbbbb",
        "expected": 1,
    },
    # Case 3: Mixed characters
    {
        "name": "Mixed Characters",
        "input": "pwwkew",
        "expected": 3,
    },
    # Case 4: Empty string
    {
        "name": "Empty String",
        "input": "",
        "expected": 0,
    },
    # Case 5: Single character
    {
        "name": "Single Character",
        "input": "a",
        "expected": 1,
    },
    # Case 6: Non-repeating characters
    {
        "name": "Non-Repeating Characters",
        "input": "abcdef",
        "expected": 6,
    },
    # Case 7: Special characters and spaces
    {
        "name": "Special Characters",
        "input": "a b c d e f g",
        "expected": 3,
    },
    # Case 8: Long input with repeating patterns
    {
        "name": "Long Repeating Pattern",
        "input": "abcdefghijklmnaaaaaaabccccdefghijkl",
        "expected": 14,
    },
    # Case 9: Large input with random characters (performance)
    {
        "name": "Large Random Input",
        "input": "abcd" * 12500,  # 50000 characters
        "expected": 4,
    },
    # Case 10: Input with digits and symbols
    {
        "name": "Digits and Symbols",
        "input": "123@abc#abc123!",
        "expected": 8,
    },
]


def test_longest_substring(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        longest_substring_test_cases, 1
    ):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")


# O(n^3) : i loop, j loop, set making => n power 3
# no of all substrings = n (n+1) / 2
# fails performance testcase
def longest_substring_1(text: str) -> int:
    length = len(text)
    max_substr_len = 0
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = text[i:j]
            substring_len = len(substring)
            if (
                max_substr_len < substring_len
                and len(set(substring)) == substring_len
            ):
                max_substr_len = len(substring)

    return max_substr_len


# O(n^2) : i loop, j, set => n power 2
def longest_substring_2(text: str) -> int:
    length = len(text)
    max_substr_len = 0
    for i in range(length):
        substring_len = 0
        substring_set = set()
        for j in range(i, length):
            next_char = text[j]
            if next_char in substring_set:
                break
            substring_set.add(next_char)
            substring_len += 1
            if substring_len > max_substr_len:
                max_substr_len = substring_len
    return max_substr_len


# O(n) -> single time string char iteration
def longest_substring_3(text: str) -> int:
    max_substr_len = 0
    substr_set = set()
    for c in text:
        if c in substr_set:
            substr_set_len = len(substr_set)
            if substr_set_len > max_substr_len:
                max_substr_len = substr_set_len
            substr_set = set()
        else:
            substr_set.add(c)

    substr_set_len = len(substr_set)
    if substr_set_len > max_substr_len:
        max_substr_len = substr_set_len

    return max_substr_len


# sliding window - O(2*n) => O(n)
# start - ptr1, i - ptr2
def longest_substring_4(text: str) -> int:
    char_index = {}
    max_substr_len = 0
    start = 0  # Start index of the current substring
    for i, c in enumerate(text):
        if c in char_index and char_index[c] >= start:
            start = (
                char_index[c] + 1
            )  # Move the start index to the right of the last occurrence

        char_index[c] = i  # Update the character's index
        max_substr_len = max(
            max_substr_len, i - start + 1
        )  # Update max length

    return max_substr_len


def longest_substring_5(text: str) -> int:
    long_substr_len = 0
    substr = ""
    for c in text:
        if c in substr:
            substr_len = len(substr)
            if substr_len > long_substr_len:
                long_substr_len = substr_len
            substr = ""
        else:
            substr += c

    substr_len = len(substr)
    if substr_len > long_substr_len:
        long_substr_len = substr_len

    return long_substr_len


def longest_substring_6(text: str) -> int:
    unique_chars = set(text)
    max_len = 0
    for c in unique_chars:
        substrings_lens = [
            len(x) + 1
            for x in text.split(c)
            if len(x) >= max_len and len(x) == len(set(x))
        ]
        if not substrings_lens:
            continue
        max_substrings_len = max(substrings_lens)
        if max_substrings_len > max_len:
            max_len = max_substrings_len
    return max_len


test_longest_substring(longest_substring_4)
