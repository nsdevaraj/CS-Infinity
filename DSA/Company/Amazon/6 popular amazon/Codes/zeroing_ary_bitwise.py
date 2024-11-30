from typing import List

saving_gotham_test_cases = [
    # Case 1: All elements are the same and non-zero
    {
        "name": "All Same Non-Zero",
        "input": [2, 2, 2],
        "expected": False,
    },
    # Case 2: All elements are zero
    {
        "name": "All Zeros",
        "input": [0, 0, 0],
        "expected": True,
    },
    # Case 3: One element is zero, others are the same
    {
        "name": "One Zero, Others Same",
        "input": [0, 2, 2],
        "expected": True,
    },
    # Case 4: Mixed values, possible to make zero
    {
        "name": "Mixed Values, Possible",
        "input": [2, 3, 1],
        "expected": True,
    },
    # Case 5: Mixed values, impossible to make zero
    {
        "name": "Mixed Values, Impossible",
        "input": [2, 3, 5],
        "expected": False,
    },
    # Case 6: Large values with a mix
    {
        "name": "Large Values, Possible",
        "input": [10**9, 10**9, 10**9],
        "expected": False,
    },
    # Case 7: Large values, impossible case
    {
        "name": "Large Values, Impossible",
        "input": [10**9, 10**9 - 1, 10**9 - 2],
        "expected": False,
    },
    # Case 8: Single element
    {
        "name": "Single Element",
        "input": [1],
        "expected": False,
    },
    # Case 9: Two elements, same
    {
        "name": "Two Same Elements",
        "input": [4, 4],
        "expected": True,
    },
    # Case 10: Two different elements
    {
        "name": "Two Different Elements",
        "input": [4, 5],
        "expected": False,
    },
]


def test_saving_gotham(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        saving_gotham_test_cases, 1
    ):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        # if(i!=5):
        #     continue

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")


# Time complexity - O(n^2) since taking all pairs
def zeroing_ary_bitwise_1(ary: List[int]) -> bool:
    ary_len = len(ary)
    changed = True
    while changed:
        changed = False
        for i in range(ary_len - 1):
            for j in range(i + 1, ary_len):
                x = ary[i] & ary[j]
                if x > 0:
                    updated_i, updated_j = (
                        ary[i] ^ x,
                        ary[j] ^ x,
                    )
                    if (
                        ary[i] != updated_i
                        or ary[j] != updated_j
                    ):
                        ary[i], ary[j] = (
                            updated_i,
                            updated_j,
                        )
                        changed = True

    return all(x == 0 for x in ary)


# Time complexity - 32n => O(n)
# space complexity - 32 => O(1)
def zeroing_ary_bitwise_2(ary: List[int]) -> bool:
    bits_count = [0] * 31
    for e in ary:
        for i in range(32):
            if (e >> i) & 1:
                bits_count[i] += 1
    for b in bits_count:
        if b % 2:
            return False
    return True


# # this also have logical error - given by chatGPT
# def can_make_all_zero(A):
#     # Check if we can make all elements zero
#     # Using the insight that we need at least one common factor to zero out all elements
#     # Special case for single elements
#     if len(A) == 1:
#         return A[0] == 0
#     # Calculate the GCD of all elements
#     from math import gcd
#     from functools import reduce
#     overall_gcd = reduce(gcd, A)
#     return overall_gcd == 0 or overall_gcd != 1

# test_saving_gotham(can_make_all_zero)
