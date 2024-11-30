import math

square_root_test_cases = [
    # Case 1: Perfect square
    {
        "name": "Perfect Square",
        "input": 16,
        "expected": 4,
    },
    # Case 2: Non-perfect square
    {
        "name": "Non-Perfect Square",
        "input": 11,
        "expected": 3,
    },
    # Case 3: Another non-perfect square
    {
        "name": "Another Non-Perfect Square",
        "input": 20,
        "expected": 4,
    },
    # Case 4: Perfect square
    {
        "name": "Another Perfect Square",
        "input": 25,
        "expected": 5,
    },
    # Case 5: Single digit
    {
        "name": "Single Digit",
        "input": 0,
        "expected": 0,
    },
    # Case 6: Single digit perfect square
    {
        "name": "Single Digit Perfect Square",
        "input": 4,
        "expected": 2,
    },
    # Case 7: Large number, non-perfect square
    {
        "name": "Large Non-Perfect Square",
        "input": 999999999,
        "expected": 31622,
    },
    # Case 8: Large number, perfect square
    {
        "name": "Large Perfect Square",
        "input": 2147395600,
        "expected": 46340,
    },
    # Case 9: Single digit 1
    {
        "name": "Single Digit 1",
        "input": 1,
        "expected": 1,
    },
]


def test_square_root(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        square_root_test_cases, 1
    ):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        # if(i!=1):
        #     continue

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")


def square_root1(num: int) -> int:
    return math.floor(math.sqrt(num))


# extra : ceil int(num) + (1 if int(num)!=num else 0)
def square_root2(num: int) -> int:
    return int(num**0.5)


# Time complexity - O(n)
def square_root3(num: int) -> int:
    nearest_num = 0
    for i in range(1, num + 1):
        sq_i = i * i
        if sq_i == num:
            nearest_num = i
            break
        elif sq_i > num:
            nearest_num = i - 1
            break
    return int(nearest_num)


# Binary search implementation
# Time Complexity - O(logN)
#  to do : implement correctly
# def square_root4(num:int)->int:
#     if num < 2:
#         return 1
#     l,r = 2, num
#     while(l<r):
#         m = (l + r) // 2
#         m_2 = m*m
#         if(m_2 == num):
#             return m
#         elif(m_2 < num):
#             l = m+1
#         else:
#             r = m-1
#     return 0


def square_root4(A: int) -> int:
    if A < 2:
        return A  # 0 and 1 are their own square roots

    left, right = (
        2,
        A // 2,
    )  # Start searching between 2 and A/2

    while left <= right:
        # finding mid this way to avoid overflow in some prog lang..
        mid = left + (right - left) // 2
        square = mid * mid

        if square == A:
            return mid
        elif square < A:
            left = mid + 1
        else:
            right = mid - 1

    return right  # The floor of sqrt(A) when not a perfect square


test_square_root(square_root4)
