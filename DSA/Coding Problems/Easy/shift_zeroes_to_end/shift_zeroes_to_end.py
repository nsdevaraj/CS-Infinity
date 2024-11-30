
move_zeroes_test_cases = [
    # Case 1: General case with mixed elements
    {
        "name": "General Case",
        "input": [0, 1, 0, 3, 12],
        "expected": [1, 3, 12, 0, 0],
    },

    # Case 2: All zeros
    {
        "name": "All Zeros",
        "input": [0, 0, 0, 0],
        "expected": [0, 0, 0, 0],
    },

    # Case 3: No zeros
    {
        "name": "No Zeros",
        "input": [1, 2, 3],
        "expected": [1, 2, 3],
    },

    # Case 4: Leading zeros
    {
        "name": "Leading Zeros",
        "input": [0, 0, 1, 2, 3],
        "expected": [1, 2, 3, 0, 0],
    },

    # Case 5: Trailing zeros
    {
        "name": "Trailing Zeros",
        "input": [1, 2, 3, 0, 0],
        "expected": [1, 2, 3, 0, 0],
    },

    # Case 6: Mixed zeros and non-zeros
    {
        "name": "Mixed Zeros",
        "input": [0, 1, 0, 2, 0, 3],
        "expected": [1, 2, 3, 0, 0, 0],
    },

    # Case 7: Single element - zero
    {
        "name": "Single Element Zero",
        "input": [0],
        "expected": [0],
    },

    # Case 8: Single element - non-zero
    {
        "name": "Single Element Non-Zero",
        "input": [1],
        "expected": [1],
    },

    # Case 9: Large input with alternating zeros
    {
        "name": "Large Input Alternating Zeros",
        "input": [0, 1] * 5000,  # 10000 elements
        "expected": [1] * 5000 + [0] * 5000,
    },

    # Case 10: Empty input
    {
        "name": "Empty Input",
        "input": [],
        "expected": [],
    },
]

def test_move_zeroes(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(move_zeroes_test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)
        assert (
            result == expected_output
        ), f"Test case {i} ({case_name}) failed: expected {expected_output}, got {result}"

    print("All test cases passed!")


def move_zeros1(nums):
    non_zeroes = []
    zeroes = []
    for num in nums:
        if num == 0:
            zeroes.append(num)
        else:
            non_zeroes.append(num)
    return non_zeroes + zeroes


def move_zeros2(nums):
    zero_count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
        else:
            nums[i - zero_count] = nums[i]
    for i in range(len(nums) - zero_count, len(nums)):
        nums[i] = 0
    return nums




def move_zeros3(num):
    left_non_zero_ptr = 0
    for right_ptr in range(len(num)):
        if num[right_ptr] != 0:
            num[left_non_zero_ptr], num[right_ptr] = num[right_ptr], num[left_non_zero_ptr]
            left_non_zero_ptr += 1
    return num





test_move_zeroes(move_zeros3)
