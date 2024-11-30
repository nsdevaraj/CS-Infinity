
[LeetCode #70](https://leetcode.com/problems/climbing-stairs/description/)

### **Climbing Stairs**
- **Problem**: You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
- **Example**:
  - Input: `n = 3`
  - Output: [1,1,1, 1,2, 2,1]



**Answer:**
```python
def climb_stairs(n):
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second
```



```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<3):
            return n
        prev = 1
        cur = 2
        curn = 1

        for i in range(3, n+1):
            curn = cur + prev
            prev = cur
            cur = curn
        
        return curn 
```



https://youtu.be/5o-kdjv7FD0?si=D7wZU23iHpFR-x98


https://www.youtube.com/watch?v=Y0lT9Fck7qI



```python



climbing_stairs_test_cases = [
    # Case 1: Zero steps
    {
        "name": "Zero Steps",
        "input": 0,
        "expected": [[]],  # One way: do nothing.
    },
    # Case 2: One step
    {
        "name": "One Step",
        "input": 1,
        "expected": [[1]],  # Only one way: [1]
    },
    # Case 3: Two steps
    {
        "name": "Two Steps",
        "input": 2,
        "expected": [[1, 1], [2]],  # Two ways: [1,1], [2]
    },
    # Case 4: Three steps
    {
        "name": "Three Steps",
        "input": 3,
        "expected": [
            [1, 1, 1],
            [1, 2],
            [2, 1],
        ],  # Three ways
    },
    # Case 5: Four steps
    {
        "name": "Four Steps",
        "input": 4,
        "expected": [
            [1, 1, 1, 1],
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1],
            [2, 2],
        ],  # Five ways
    },
    # Case 6: Five steps
    {
        "name": "Five Steps",
        "input": 5,
        "expected": [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 2],
            [1, 1, 2, 1],
            [1, 2, 1, 1],
            [2, 1, 1, 1],
            [1, 2, 2],
            [2, 1, 2],
            [2, 2, 1],
        ],  # Eight ways
    },
    # Case 7: Larger number of steps (10 steps)
    {
        "name": "Ten Steps",
        "input": 10,
        "expected": [],  # Will have multiple combinations; you may want to calculate them or leave as is.
    },
    # Case 8: Negative steps
    {
        "name": "Negative Steps",
        "input": -1,
        "expected": [],  # Invalid input, no ways to climb negative steps.
    },
]


def test_climbing_stairs(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(climbing_stairs_test_cases, 1):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert result == expected_result, f"Test case {i} ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")




def climbing_stairs1(n: int) -> list:

    all_combinations = []
    possible_steps = [1, 2]






    return []



def climbing_stairs10(n: int) -> list:
    ways = []
    # possible ways => 1,2


    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + 2*j == n:
                ways.append([1]*i + [2]*j)
    return ways






# def climbing_stairs(n):
#     if n < 0:
#         return []
#     if n == 0:
#         return [[]]  # One way to stay at the ground: do nothing.

#     ways = []

#     def backtrack(steps, current):
#         if steps == 0:
#             ways.append(current)
#             return
#         if steps >= 1:
#             backtrack(steps - 1, current + [1])  # Take a 1-step
#         if steps >= 2:
#             backtrack(steps - 2, current + [2])  # Take a 2-step

#     backtrack(n, [])
#     return ways



test_climbing_stairs(climbing_stairs1)


```

