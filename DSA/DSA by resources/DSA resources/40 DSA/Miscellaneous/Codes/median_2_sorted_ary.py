



median_test_cases = [
    # # Case 1: Both arrays are empty (undefined behavior)
    # {
    #     "name": "Both Arrays Empty",
    #     "input": ([], []),
    #     "expected": None,  # or you can raise an exception
    # },
    # # Case 2: One empty array
    # {
    #     "name": "One Array Empty",
    #     "input": ([1, 2, 3], []),
    #     "expected": 2,
    # },
    # Case 3: Both arrays are of odd length
    {
        "name": "Odd Length Arrays",
        "input": ([1, 3], [2]),
        "expected": 2.0,
    },
    # Case 4: Both arrays are of even length
    {
        "name": "Even Length Arrays",
        "input": ([1, 2], [3, 4]),
        "expected": 2.5,
    },
    # Case 5: One array has a single element
    {
        "name": "Single Element Array",
        "input": ([1], [2, 3]),
        "expected": 2.0,
    },
    # Case 6: Large numbers
    {
        "name": "Large Numbers",
        "input": ([1000000, 2000000], [3000000, 4000000]),
        "expected": 2500000.0,
    },
    # Case 7: One array with duplicate numbers
    {
        "name": "Array with Duplicates",
        "input": ([1, 2, 2], [2, 3, 4]),
        "expected": 2.0,
    },
    # Case 8: Uneven length arrays
    {
        "name": "Uneven Length Arrays",
        "input": ([1, 2, 3], [4, 5]),
        "expected": 3.0,
    },
    # Case 9: Both arrays are the same
    {
        "name": "Same Arrays",
        "input": ([1, 2, 3], [1, 2, 3]),
        "expected": 2.0,
    },
    # Case 10: Large test case
    {
        "name": "Large Test Case",
        "input": (list(range(1000000)), list(range(1000000, 2000000))),
        "expected": 999999.5,
    },
    # # Case 11: both single element
    # {
    #     "name": "Both single element",
    #     "input": ([1], [1]),
    #     "expected": 1,
    # },
    # # Case 11:  single element and no element
    # {
    #     "name": "Single element and No element",
    #     "input": ([1], []),
    #     "expected": 1,
    # },
]

def test_find_median(func):
    print(f"Testing function: {func.__name__}")

    for test_case in median_test_cases:
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(*input_data)
        assert (
                result == expected_result
            ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")




def median_two_sorted_arys_1(ary1:list[int], ary2:list[int])-> float:
    combined_ary = ary1 + ary2
    combined_ary.sort()
    combined_ary_len = len(combined_ary)
    mid_index = combined_ary_len // 2
    if(combined_ary_len%2):
        return combined_ary[mid_index]
    else:
        return (combined_ary[mid_index-1] + combined_ary[mid_index]) / 2


#! toDo: fix logics
def median_two_sorted_arys_2(ary1:list[int], ary2:list[int])-> float:
    ary1_len , ary2_len = len(ary1), len(ary2)
    mid_index = (ary1_len + ary2_len) // 2

    if(ary1_len == 0):
        mid = ary2_len // 2
        if mid % 2:
            return ary2[mid]
        else:
            return (ary2[mid]+ary2[mid-1])/2

    if(ary2_len == 0):
        mid = ary1_len // 2
        if mid % 2:
            return ary1[mid]
        else:
            return (ary1[mid]+ary1[mid-1])/2-

    # [1] , [2] #=> [1,2] 1.5
    # [2,3],[1,4,5] #=> 3
    ptr1, ptr2 = 0,0
    prev, cur = -1,-1

    while(ptr1 < ary1_len or ptr2 < ary2_len):
        ptr_sum = ptr1 + ptr2
        if(mid_index+1 == ptr_sum):
            print(mid_index, ptr1, ptr2)
            print(ptr1, ptr2, prev, cur)
            if(mid_index%2):
                return cur
            else:
                return (prev+cur)/2

        ptr1_elm, ptr2_elm = ary1[ptr1], ary2[ptr2]
        if(ptr1_elm < ptr2_elm):
            prev, cur = cur, ptr1_elm
            ptr1 += 1
        else:
            prev, cur = cur, ptr2_elm
            ptr2 += 1




    return -1



test_find_median(median_two_sorted_arys_2)

# toDO: get different solutions..



# def findMedianSortedArrays(nums1, nums2):
#     # Ensure nums1 is the smaller array
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1

#     x, y = len(nums1), len(nums2)
#     low, high = 0, x

#     while low <= high:
#         partitionX = (low + high) // 2
#         partitionY = (x + y + 1) // 2 - partitionX

#         # If partitionX is 0 it means nothing is there on left side. Use -inf for maxLeftX
#         # If partitionX is length of input then there is nothing on right side. Use +inf for minRightX
#         maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
#         minRightX = float('inf') if partitionX == x else nums1[partitionX]

#         maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
#         minRightY = float('inf') if partitionY == y else nums2[partitionY]

#         # Check if we have partitioned the arrays correctly
#         if maxLeftX <= minRightY and maxLeftY <= minRightX:
#             # We have partitioned correctly
#             if (x + y) % 2 == 0:
#                 return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
#             else:
#                 return max(maxLeftX, maxLeftY)

#         elif maxLeftX > minRightY:
#             # We are too far on right side for partitionX. Go on left side.
#             high = partitionX - 1
#         else:
#             # We are too far on left side for partitionX. Go on right side.
#             low = partitionX + 1

# # Example usage
# nums1 = [1, 3]
# nums2 = [2]
# print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

# nums1 = [1, 2]
# nums2 = [3, 4]
# print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5
