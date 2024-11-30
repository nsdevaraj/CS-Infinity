palindrome_number_test_cases = [
    # Case 1: Positive palindrome
    {
        "name": "Positive Palindrome",
        "input": 121,
        "expected": True,
    },
    # Case 2: Negative number (not a palindrome)
    {
        "name": "Negative Number",
        "input": -121,
        "expected": False,
    },
    # Case 3: Positive non-palindrome
    {
        "name": "Positive Non-Palindrome",
        "input": 123,
        "expected": False,
    },
    # Case 4: Single digit (always a palindrome)
    {
        "name": "Single Digit",
        "input": 7,
        "expected": True,
    },
    # Case 5: Zero (is a palindrome)
    {
        "name": "Zero",
        "input": 0,
        "expected": True,
    },
    # Case 6: Large palindrome
    {
        "name": "Large Palindrome",
        "input": 123456789987654321,
        "expected": True,
    },
    # Case 7: Large non-palindrome
    {
        "name": "Large Non-Palindrome",
        "input": 123456789987654320,
        "expected": False,
    },
    # Case 8: Palindrome with trailing zeros (not a palindrome)
    {
        "name": "Number with Trailing Zeros",
        "input": 1000,
        "expected": False,
    },
    # Case 9: Long palindrome
    {
        "name": "Long Palindrome",
        "input": 1234567890987654321,
        "expected": True,
    },
    # Case 10: Long non-palindrome
    {
        "name": "Long Non-Palindrome",
        "input": 1234567890987654320,
        "expected": False,
    },  # Non-palindrome
    # Case 11: Large even-length palindrome
    {
        "name": "Large Even-Length Palindrome",
        "input": 12344321,
        "expected": True,
    },
    # Case 12: Large even-length non-palindrome
    {
        "name": "Large Even-Length Non-Palindrome",
        "input": 12344320,
        "expected": False,
    },
    # Case 13: Very large palindrome (with many digits)
    # {
    #     "name": "Very Large Palindrome",
    #     "input": int("1" + "0" * 1000000 + "1"),
    #     "expected": True,
    # },
    # Case 14: Very large non-palindrome
    # {
    #     "name": "Very Large Non-Palindrome",
    #     "input": int("1" + "0" * 1000000 + "2"),
    #     "expected": False,
    # },
    # Case 15: Edge case of maximum integer value in Python
    {
        "name": "Max Integer",
        "input": 2147483647,
        "expected": False,
    },  # Not a palindrome
]


def test_palindrome_number(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        palindrome_number_test_cases, 1
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



def is_palindrome1(x:int)->bool:
    return str(x) == str(x)[::-1]


def is_palindrome2(x:int)->bool:
    reversed_x= 0
    temp_x = x

    while temp_x > 0:
        reversed_x = reversed_x * 10 + temp_x % 10
        temp_x //= 10

    return x == reversed_x


def is_palindrome3(x:int)->bool:
    if x < 0:
        return False

    digits: list[int] = []
    while x > 0:
        digits.append(x % 10)
        x //= 10

    left, right = 0, len(digits) - 1

    while(left < right):
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1

    return True

def is_palindrome4(x:int)->bool:
    if x < 0:
        return False

    num_of_digits = 0

    temp = x
    while temp > 0:
        num_of_digits += 1
        temp //= 10

    right_ptr = num_of_digits - 1

    for left_ptr in range(num_of_digits // 2):
        left_digit = (x // 10 ** right_ptr) % 10
        right_digit = (x // 10 ** left_ptr) % 10

        if left_digit != right_digit:
            return False

        right_ptr -= 1
    return True



test_palindrome_number(is_palindrome1)
