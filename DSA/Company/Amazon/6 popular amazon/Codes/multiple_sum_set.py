from typing import List, Set, Tuple

multiple_sum_set_test_cases = [
    # Case 1: Basic case with distinct elements
    {
        "name": "Distinct Elements",
        "input": [1, 2, 3],
        "expected": 4,  # Valid subsets: [], [1], [2], [3]
    },
    # Case 2: Case with duplicates
    {
        "name": "Duplicates Present",
        "input": [1, 2, 3, 3, 2],
        "expected": 5,  # Valid subsets:  [], [1], [2], [3], [2,2], [1,2,3]
    },
    # Case 3: All elements are the same
    {
        "name": "All Same Elements",
        "input": [2, 2, 2],
        "expected": 3,  # Valid subsets: [], [2], [2, 2]
    },
    # Case 4: Single element
    {
        "name": "Single Element",
        "input": [5],
        "expected": 1,  # Valid subsets: [], [5]
    },
    # Case 5: Larger set of distinct elements
    {
        "name": "Larger Distinct Set",
        "input": [1, 2, 4, 5],
        "expected": 6,  # Valid subsets: [], [1], [2], [4], [5], [1, 2]
    },
    # Case 6: All zeros
    {
        "name": "All Zeros",
        "input": [0, 0, 0],
        "expected": 1,  # Only valid subset: []
    },
    # Case 7: Larger array with some combinations
    {
        "name": "Larger Mixed Set",
        "input": [1, 2, 2, 3],
        "expected": 6,  # Valid subsets: [], [1], [2], [3], [2,3]
    },
    # Case 8: Edge case with maximum size
    {
        "name": "Maximum Size Edge Case",
        "input": [1] * 100,
        "expected": 1,  # Only valid subset: []
    },
]

def test_multiple_sum_set(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(multiple_sum_set_test_cases, 1):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert result == expected_result, f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")



def multiple_sum_set_1(ary:List[int])->int:
    valid_subsets_count = 0

    # from itertools import chain, combinations
    # def all_subsets(nums):
    #     # Create all subsets using combinations
    #     return list(chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1)))

    def get_subsets(nums:List[int])->Set[Tuple[int]]:
        subsets:Set[Tuple[int]] = set(())
        def backtrack(start, path):
            tuple_path = tuple(sorted(path))
            if(tuple_path and tuple_path not in subsets):
                subsets.add(tuple_path)
            for i in range(start, len(nums)):
                backtrack(i+1, path +[nums[i]])

        backtrack(0,[])
        return subsets

    # # Summing values
    # total_sum = sum(arr)
    # # Calculating product
    # total_product = math.prod(arr)

    subsets_ary = get_subsets(ary)
    # print(ary,subsets_ary)

    sums = []
    prods = []

    for subset in subsets_ary:
        subset_sum = 0
        subset_prod = 1
        for s in subset:
            subset_sum += s
            subset_prod *= s
        sums.append(subset_sum)
        prods.append(subset_prod)


    for i in range(sums):
        if(s in prods):
            valid_subsets_count += 1


    return valid_subsets_count


test_multiple_sum_set(multiple_sum_set_1)



# to be continued..
#
#
