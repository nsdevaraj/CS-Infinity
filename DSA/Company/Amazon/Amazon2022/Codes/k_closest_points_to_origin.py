from typing import List
from math import sqrt


k_closest_test_cases = [
    # Case 1: Basic test with one closest point
    {
        "name": "Basic Test 1",
        "input": ([[1, 3], [-2, 2]], 1),
        "expected": [[-2, 2]],
    },
    # Case 2: Basic test with two closest points
    {
        "name": "Basic Test 2",
        "input": ([[3, 3], [5, -1], [-2, 4]], 2),
        "expected": [[3, 3], [-2, 4]],  # Order may vary
    },
    # Case 3: All points are equidistant - unmentioned testcase - many equidistant points
    # {
    #     "name": "Equidistant Points",
    #     "input": ([[1, 0], [0, 1], [-1, 0], [0, -1]], 2),
    #     "expected": [[1, 0], [0, 1]],  # Any two points are valid
    # },
    # Case 4: Only one point
    {
        "name": "Single Point",
        "input": ([[1, 1]], 1),
        "expected": [[1, 1]],
    },
    # # Case 5: Large input - invalid since repetation of inputs
    # {
    #     "name": "Large Input",
    #     "input": ([[0, 1], [1, 0], [1, 1], [2, 2]] * 2500, 3),
    #     "expected": [[0, 1], [1, 0], [1, 1]],  # Closest 3 points
    # },
]


def test_k_closest(func):
    print(f"Testing function: {func.__name__}")

    for test_case in k_closest_test_cases:
        input_data, k = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data, k)

        # Check if the returned result matches the expected result
        assert sorted(result) == sorted(
            expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")


def k_closest_points_to_origin_1(
    points: List[List[int]], k: int
) -> List[List[int]]:
    # Define the origin
    origin_x, origin_y = 0, 0

    # Use a set to get unique points
    unique_points = list(
        set(tuple(point) for point in points)
    )

    # Sort unique points based on squared distance from the origin, then lexicographically
    sorted_points = sorted(
        unique_points,
        key=lambda p: (
            (p[0] - origin_x) ** 2 + (p[1] - origin_y) ** 2,
            p,
        ),
    )

    # Convert tuples back to lists and return the k closest points
    return [list(point) for point in sorted_points[:k]]


def k_closest_points_to_origin_2(
    points: List[List[int]], k: int
) -> List[List[int]]:
    distances = []
    result = []

    for x, y in points:
        distance = sqrt(x**2 + y**2)
        distances.append([distance, x, y])

    # Sort distances in ascending order
    distances.sort(key=lambda x: x[0])

    # Get the k closest points
    for _ in range(k):
        distance, x, y = distances.pop(
            0
        )  # Use pop(0) to get the closest point
        result.append([x, y])

    return result


test_k_closest(k_closest_points_to_origin_2)
