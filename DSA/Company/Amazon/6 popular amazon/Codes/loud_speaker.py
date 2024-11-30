from typing import List

loudspeaker_test_cases = [
    # Case 1: Simple direct path with loudspeakers
    {
        "name": "Direct Path with Loudspeakers",
        "input": (5, [[1, 2], [2, 3], [3, 4], [4, 5]], [1, 3], 1, 5),
        "expected": 3,  # Loudspeaker at city 3 can cover city 5 (distance 2), so intensity of 3 is needed.
    },
    # Case 2: No loudspeakers in the path
    {
        "name": "No Loudspeakers in Path",
        "input": (5, [[1, 2], [2, 3], [3, 4], [4, 5]], [4], 1, 5),
        "expected": -1,  # City 4 has a loudspeaker, but it cannot reach city 5, as it has no connection.
    },
    # Case 3: All cities connected with loudspeakers at each city
    {
        "name": "All Cities with Loudspeakers",
        "input": (5, [[1, 2], [2, 3], [3, 4], [4, 5]], [1, 2, 3, 4, 5], 1, 5),
        "expected": 1,  # All cities have loudspeakers, so intensity of 1 is enough to cover the distance of 4.
    },
    # Case 4: Cities are not reachable due to disconnected components
    {
        "name": "Disconnected Components",
        "input": (6, [[1, 2], [2, 3], [4, 5]], [1], 1, 6),
        "expected": -1,  # Cities 1-3 and 4-5 are disconnected; city 6 cannot be reached.
    },
    # Case 5: Loudspeakers at start and end only, need max intensity
    {
        "name": "Loudspeakers at Start and End Only",
        "input": (5, [[1, 2], [2, 3], [3, 4], [4, 5]], [1, 5], 1, 5),
        "expected": 4,  # Intensity of 4 needed for the sound to travel through 4 roads from 1 to 5.
    },
    # Case 6: Large network with multiple paths and loudspeakers
    {
        "name": "Large Network with Multiple Paths",
        "input": (7, [[1, 2], [2, 3], [3, 4], [1, 5], [5, 6], [6, 7]], [1, 5], 1, 7),
        "expected": 3,  # Intensity of 3 is required for sound to propagate from 1 to 7 via 5 and 6.
    },
    # Case 7: All cities connected but only one city has a loudspeaker
    {
        "name": "Only One Loudspeaker in Network",
        "input": (5, [[1, 2], [2, 3], [3, 4], [4, 5]], [3], 1, 5),
        "expected": 3,  # The loudspeaker at city 3 can reach city 5 (distance 2) with intensity 3.
    },
    # Case 8: Path with multiple loudspeakers and different paths
    {
        "name": "Path with Multiple Loudspeakers",
        "input": (6, [[1, 2], [2, 3], [3, 4], [1, 5], [5, 6]], [2, 3, 5], 1, 6),
        "expected": 2,  # City 5 can communicate to city 6 using intensity of 2, and the loudspeakers facilitate this.
    },
]


def test_loudspeaker(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(loudspeaker_test_cases, 1):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(*input_data)

        # Check if the returned result matches the expected result
        assert result == expected_result, f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")



def loudspeaker_1(total_cities:int, roads:List[List[int]],speaker_cities: List[int], src:int, dest:int )-> int:

    if(src == dest):
        return 0

    current_dests= [r[1] for r in roads if r[0] == src ]
    freq_for_dests = []
    for d in current_dests:
        if(d == dest):
            freq_for_dests.append(1)
        else:
            freq_for_dest = loudspeaker_1(total_cities, roads,speaker_cities, src, d)
            if(freq_for_dest != -1):
                freq_for_dests.append(freq_for_dest)

    if(not freq_for_dests):
        return -1
    else:
        return min(freq_for_dests)



test_loudspeaker(loudspeaker_1)


## pending : ToDo
