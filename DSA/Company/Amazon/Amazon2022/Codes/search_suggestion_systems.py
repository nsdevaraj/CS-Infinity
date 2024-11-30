from typing import List

search_suggestions_test_cases = [
    # Case 1: Basic suggestions
    {
        "name": "Basic Suggestions",
        "input": (
            [
                "mobile",
                "mouse",
                "moneypot",
                "monitor",
                "mousepad",
            ],
            "mouse",
        ),
        "expected": [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
        ],
    },
    # Case 2: Single product match
    {
        "name": "Single Product Match",
        "input": (["havana"], "havana"),
        "expected": [
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
            ["havana"],
        ],
    },
    # Case 3: Empty product list
    {
        "name": "Empty Product List",
        "input": ([], "test"),
        "expected": [[], [], [], []],
    },
    # Case 4: No matches for input
    {
        "name": "No Matches",
        "input": (["apple", "banana", "cherry"], "xyz"),
        "expected": [[], [], []],
    },
    # Case 5: Products with similar prefixes
    {
        "name": "Similar Prefixes",
        "input": (
            ["abc", "ab", "abcd", "abxyz", "abca"],
            "ab",
        ),
        "expected": [
            ["ab", "abc", "abca"],  # After typing 'a'
            ["ab", "abc", "abca"],  # After typing 'ab'
        ],
    },
    # Case 6: Case with a lot of products
    {
        "name": "Many Products",
        "input": (
            [
                "product1",
                "product2",
                "prod",
                "product3",
                "prodabc",
            ],
            "prod",
        ),
        "expected": [
            [
                "prod",
                "prodabc",
                "product1",
            ],  # After typing 'p'
            [
                "prod",
                "prodabc",
                "product1",
            ],  # After typing 'pr'
            [
                "prod",
                "prodabc",
                "product1",
            ],  # After typing 'pro'
            [
                "prod",
                "prodabc",
                "product1",
            ],  # After typing 'prod'
        ],
    },
    #  # Case 7:  Prefixes reducing
    # {
    #     "name": "Prefixes reducing",
    #     "input": (["abc", "ab", "abcd", "abxyz"], "abcd"),
    #     "expected": [
    #         ["ab", "abc", "abcd"],  # After typing 'a'
    #         ["ab", "abc", "abcd"],  # After typing 'ab'
    #         ["ab", "abcd"],  # After typing 'abc'
    #         [ "abcd"],  # After typing 'abcd'
    #     ],
    # },
    {
        "name": "Prefixes Reducing",
        "input": (["ab", "abc", "abcd"], "abcd"),
        "expected": [
            ["ab", "abc", "abcd"],  # After typing 'a'
            ["ab", "abc", "abcd"],  # After typing 'ab'
            ["abc", "abcd"],  # After typing 'abc'
            ["abcd"],  # After typing 'abcd'
        ],
    },
]


def test_search_suggestions(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        search_suggestions_test_cases, 1
    ):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(*input_data)

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"""Test case ({case_name}) failed:
            expected {expected_result},
            got {result}"""

    print("All test cases passed!")


def search_suggestions_1(
    search_list: list[str], search_word: str
) -> list[list[str]]:
    suggestions_list: list[list[str]] = []
    suggestions_limit: int = 3

    for i in range(len(search_word)):
        sub_search_word = search_word[: i + 1]
        suggestions: list[str] = [
            s
            for s in search_list
            if s.startswith(sub_search_word)
        ]
        suggestions.sort()
        suggestions_list.append(
            suggestions[:suggestions_limit]
        )

    return suggestions_list


def search_suggestions_2(
    search_list: list[str], search_word: str
) -> list[list[str]]:
    search_list.sort()
    suggestions_list: list[list[str]] = []
    suggestions_limit: int = 3
    prev_suggestions: list[str] = search_list

    # # just try:  instead filtering -> can find and take word start match and not match and inbetween items
    # suggestions = [ s for s in prev_suggestions if s.startswith(sub_search_word)]

    for i in range(len(search_word)):
        sub_search_word = search_word[: i + 1]
        suggestions: list[str] = [
            s
            for s in prev_suggestions
            if s.startswith(sub_search_word)
        ]
        prev_suggestions = suggestions
        suggestions_list.append(
            suggestions[:suggestions_limit]
        )

    return suggestions_list


def search_suggestions_3(
    products: List[str], searchWord: str
) -> List[List[str]]:
    products.sort()
    left_ptr, right_ptr = 0, len(products) - 1
    result = []

    for letter_index in range(len(searchWord)):
        search = searchWord[letter_index]
        # Move the left pointer forward,
        # when products len below search word
        # or product's index letter not match with search index letter
        while left_ptr <= right_ptr and (
            len(products[left_ptr]) <= letter_index
            or products[left_ptr][letter_index] != search
        ):
            left_ptr += 1
        # Move the right pointer backward, like above
        while left_ptr <= right_ptr and (
            len(products[right_ptr]) <= letter_index
            or products[right_ptr][letter_index] != search
        ):
            right_ptr -= 1
        # Number of words left that match the prefix
        words_left = right_ptr - left_ptr + 1

        # result.append(products[left_ptr:left_ptr + min(3, words_left)])
        if words_left >= 3:
            result.append(
                [
                    products[left_ptr],
                    products[left_ptr + 1],
                    products[left_ptr + 2],
                ]
            )
        elif words_left == 2:
            result.append(
                [products[left_ptr], products[left_ptr + 1]]
            )
        elif words_left == 1:
            result.append([products[left_ptr]])
        else:
            result.append([])
    return result


test_search_suggestions(search_suggestions_3)
