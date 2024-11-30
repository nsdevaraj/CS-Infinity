from typing import List

log_reorder_test_cases = [
    # Example 1
    {
        "name": "Example 1",
        "input": [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ],
        "expected": [
            "let1 art can",
            "let3 art zero",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ],
    },
    # Example 2
    {
        "name": "Example 2",
        "input": [
            "a1 9 2 3 1",
            "g1 act car",
            "zo4 4 7",
            "ab1 off key dog",
            "a8 act zoo",
        ],
        "expected": [
            "g1 act car",
            "a8 act zoo",
            "ab1 off key dog",
            "a1 9 2 3 1",
            "zo4 4 7",
        ],
    },
    # Case 3: Only letter logs
    {
        "name": "Only Letter Logs",
        "input": [
            "let1 apple",
            "let2 banana",
            "let3 cherry",
        ],
        "expected": [
            "let1 apple",
            "let2 banana",
            "let3 cherry",
        ],
    },
    # Case 4: Only digit logs
    {
        "name": "Only Digit Logs",
        "input": ["dig1 1 1", "dig2 2 2", "dig3 3 3"],
        "expected": ["dig1 1 1", "dig2 2 2", "dig3 3 3"],
    },
    # Case 5: Mixed logs with same contents
    {
        "name": "Mixed Logs with Same Content",
        "input": [
            "let1 cat",
            "let2 cat",
            "dig1 1 1",
            "let3 bat",
        ],
        "expected": [
            "let3 bat",
            "let1 cat",
            "let2 cat",
            "dig1 1 1",
        ],
    },
    # Content same, Identifier sorting
    {
        "name": "Content same, Identifier sorting",
        "input": [
            "let3 art",
            "let1 art",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ],
        "expected": [
            "let1 art",
            "let3 art",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ],
    },
]


def test_reorder_logs(func):
    print(f"Testing function: {func.__name__}")

    for test_case in log_reorder_test_cases:
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")


def reorder_data_1(logs: List[str]) -> List[str]:

    letter_logs, digit_logs = [], []

    for log in logs:
        # we can take last letter or whole text after first word too
        second_word_first_char = log.split(" ")[1][0]
        if second_word_first_char.isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(
        key=lambda x: (x.split(" ")[1:], x.split(" ")[0])
    )

    return letter_logs + digit_logs


test_reorder_logs(reorder_data_1)
