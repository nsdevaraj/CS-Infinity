
from typing import List, Set, Tuple
import time

island_test_cases = [
    # Case 1: Single island
    {
        "name": "Single Island",
        "input": [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        "expected": 1,
    },
    # Case 2: Multiple islands
    {
        "name": "Multiple Islands",
        "input": [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ],
        "expected": 3,
    },
    # Case 3: No islands
    {
        "name": "No Islands",
        "input": [
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"]
        ],
        "expected": 0,
    },
    # Case 4: All land
    {
        "name": "All Land",
        "input": [
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"]
        ],
        "expected": 1,
    },
    # Case 5: Separate islands
    {
        "name": "Separate Islands",
        "input": [
            ["1", "0", "0", "1"],
            ["0", "0", "0", "0"],
            ["1", "0", "0", "1"]
        ],
        "expected": 4,
    },
    # Case 6: Complex shape islands
    {
        "name": "Complex Shape Islands",
        "input": [
            ["1", "1", "0", "0", "0"],
            ["1", "0", "1", "0", "1"],
            ["0", "0", "0", "0", "0"],
            ["1", "1", "1", "1", "0"]
        ],
        "expected": 4
    },
    # Case 7: Long narrow island
    {
        "name": "Long Narrow Island",
        "input": [
            ["1"],
            ["1"],
            ["1"],
            ["0"],
            ["1"],
            ["1"]
        ],
        "expected": 2,
    },
    # Case 8: Edge case - single cell island
    {
        "name": "Single Cell Island",
        "input": [
            ["1"]
        ],
        "expected": 1,
    },
    # Case 9: Edge case - single cell water
    {
        "name": "Single Cell Water",
        "input": [
            ["0"]
        ],
        "expected": 0,
    },
    # # Case 10: Performance Test - Large grid with a single island
    # {
    #     "name": "Large Single Island",
    #     "input": [["1"] * 300 for _ in range(300)],
    #     "expected": 1,
    # },
    # # Case 11: Performance Test - Large grid with multiple islands
    # {
    #     "name": "Large Multiple Islands",
    #     "input": [
    #         ["1" if (i % 2 == 0 and j % 2 == 0) else "0" for j in range(300)]
    #         for i in range(300)
    #     ],
    #     "expected": 7500,  # There will be 7500 separate islands
    # },
]



def test_island_count(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(island_test_cases, 1):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        start_time = time.time()
        result = func(input_data)
        end_time = time.time()

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

        # Print performance for large test cases
        if "Performance" in case_name:
            print(f"{case_name} executed in {end_time - start_time:.4f} seconds.")

    print("All test cases passed!")


def islands_1(board: List[List[str]])->int:
    visited_pts:Set[Tuple[int, int]] = set()
    island_count:int = 0
    row_limit = len(board)
    col_limit = len(board[0])



    def visit_neighbours(pt:Tuple[int,int]):
        p1,p2 = pt


        if(not(-1<p1<row_limit) or not(-1<p2<col_limit ) or board[p1][p2] == '0' or pt in visited_pts):
            return

        visited_pts.add(pt)

        neighbours = [
            (p1-1,p2),
            (p1,p2+1),
            (p1+1,p2),
            (p1,p2-1),
        ]

        for neighbour in neighbours:
            visit_neighbours(neighbour)



    for i in range(row_limit):
        for j in range(col_limit):
            pt:Tuple[int,int] = (i,j)
            pt_value = board[i][j]
            if(pt in visited_pts):
                continue
            elif(pt_value == '1'):
                island_count += 1
                visit_neighbours(pt)

    return island_count


test_island_count(islands_1)
