"""
1.	Find the Missing Number
Problem: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing.
Input: [3, 0, 1]
Output: 2
"""

# Finds the missing number in an array containing only consecutive integers


"""
Approach: Iteration
- take array length and loop all numbers from 0 to array length +1
- check if number is in array, if not return it
- Time complexity: O(n) - looping through indices and checking in array
- Space complexity: O(1) -no extra space
"""


def find_missing_number1(arr):
    arr_len = len(arr)
    for i in range(arr_len + 1):
        if i not in arr:
            return i
    return -1


"""
Approach: Sorting
- sort array
- check the indices with element in sorted indices, mismatch is the missing number
- Time complexity: O(n log n) - sorting
- Space complexity: O(1) - no extra space is used
"""


def find_missing_number2(arr):
    arr.sort()  # inplace sorting
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return len(arr)


"""
Approach: HashMap
- create hash_map and put elements in map as true
- iterate through indices and check those index not in hasn_map
- Time complexity: O(n) - looping through indices
- Space complexity: O(n) - creating new hash_map
"""


def find_missing_number3(arr):
    hash_map = {num: True for num in arr}
    for i in range(len(arr) + 1):
        if i not in hash_map:
            return i
    return -1


"""
Approach: Set difference
- find out missing element
- Time complexity: O(n) - looping through indices to create set
- Space complexity: O(n) - creating new set
"""


def find_missing_number4(arr):
    return (set(range(len(arr) + 1)) - set(arr)).pop()


"""
Approach: Cyclic sort [ x number should be placed at x index]
- sort array
- check the indices with element in sorted indices, mismatch is the missing number
- Time complexity: O(n) - iterating update n ( length of array)
- Space complexity: O(1) - no extra space is used
"""


def find_missing_number5(arr):
    i = 0
    last_item = len(
        arr
    )  # The value that represents the missing number if it's n
    last_item_position = 0  # To track the index of the last item (n)

    while i < len(arr):
        current = arr[i]  # Get the value at index i

        # Check if the current value is in the valid range and not in the correct position
        if current < len(arr) and arr[i] != arr[current]:
            # Swap to place the number in its correct index
            arr[i], arr[current] = arr[current], arr[i]

            # Update last_item_position if the swapped number is the last item (n)
            if arr[i] == last_item:
                last_item_position = i
            elif arr[current] == last_item:
                last_item_position = current
        else:
            # If the current value is the last item (n), update its position
            if arr[i] == last_item:
                last_item_position = i

            # Move to the next index
            i += 1

        # Debug output to track the process
        # print(i, arr, last_item_position)

    # Check if the last item is in its correct position
    if arr[last_item_position] == last_item_position:
        return len(arr)  # Missing number is n
    else:
        return last_item_position  # Return the missing number's index


"""
   Approach: Summation Formula
    1. Calculate the sum of the first n natural numbers using the formula n(n+1)/2,
       where n is the length of the array.
    2. Find the sum of the elements in the input array.
    3. The missing number is the difference between the expected sum and the actual sum.
    Time complexity: O(n), since finding sum of given array
    Space complexity: O(1), no extra space is used.
"""


def find_missing_number6(arr):
    arr_len = len(arr)
    # sum of first n natural numbers => n(n+1)/2
    expected_sum = arr_len * (arr_len + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


"""
Approach: XOR Bitwise Operator
- Initialize a variable 'missing' with the length of the array.
- Iterate through the array, performing XOR between 'missing', the current index, and the current number. Due to the properties of XOR, duplicate numbers cancel out.
- After the iteration, 'missing' will hold the value of the missing number.
- Time Complexity: O(n) - iterating through the array once.
- Space Complexity: O(1) -  no extra space is used.
"""


def find_missing_number7(arr):
    n = len(arr)
    missing = n
    for i, num in enumerate(arr):
        missing ^= i ^ num
    return missing


find_missing_number_test_cases = [
    # Case 1: General case with a small array
    {"input": [3, 0, 1], "expected": 2},
    # Case 2: Missing number is 0
    {"input": [1, 2, 3], "expected": 0},
    # Case 3: Missing number is the last one (n)
    {"input": [0, 1, 2], "expected": 3},
    # Case 4: Array with one element missing
    {"input": [0], "expected": 1},
    # Case 5: Array with only the number 1 missing
    {"input": [0, 2], "expected": 1},
    # Case 6: Array with n numbers, missing a middle value
    {"input": [0, 1, 3, 4, 5], "expected": 2},
    # Case 7: Single element array, missing 0
    {"input": [1], "expected": 0},
    # Case 8: Large array missing the middle element
    # {
    #     'input': list(range(10000)) + [10001],
    #     'expected': 10000
    # },
    # Case 9: Non consecutive ordered numbers
    {"input": [0, 3, 2], "expected": 1},
    # Case 10: Non consecutive ordered numbers with last number as missing
    {"input": [6, 8, 1, 2, 3, 4, 5, 7], "expected": 0},
]


def test_find_missing_number(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(find_missing_number_test_cases, 1):
        input_data = test_case["input"]
        expected_output = test_case["expected"]
        result = func(input_data)
        assert (
            result == expected_output
        ), f"Test case {i} failed: expected {expected_output}, got {result}"
        # print(f"Test case {i} passed!")
    print("All test cases passed!")


test_find_missing_number(find_missing_number7)
