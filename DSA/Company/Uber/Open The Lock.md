

### Problem Statement: Open the Lock

You have a lock that has four wheels, each with digits ranging from 0 to 9. The lock can be opened by entering a sequence of four digits. Each digit can be rotated independently.

You are given a **deadends** list that represents the combinations that should not be attempted, as they will cause the lock to be permanently locked. You are also given a **target** combination that you want to reach.

Your task is to determine the minimum number of turns needed to open the lock. If it is not possible to open the lock, return -1.

### Function Signature
```python
def open_lock(deadends: List[str], target: str) -> int:
```

### Example
#### Input
```plaintext
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
```

#### Output
```plaintext
6
```

### Explanation
- You can start at "0000".
- The sequence of moves to reach "0202" can be calculated.

### Constraints
- The target and deadends will always be a string of length 4.
- The lock will never open for a deadend combination.


ToDo: pending 

```python
# from collections import deque
from typing import List


test_cases = [
    {
        "name": "Basic Test Case",
        "deadends": ["0201", "0101", "0102", "1212", "2002"],
        "target": "0202",
        "expected": 6,
        # Sequence: 0000 -> 0001 -> 0011 -> 0111 -> 0211 -> 0201 -> 0202
    },
    {
        "name": "Lock is a Deadend",
        "deadends": ["0000"],
        "target": "8888",
        "expected": -1,
        # Cannot open the lock as the starting point is a deadend.
    },
    {
        "name": "Direct Target",
        "deadends": [],
        "target": "0001",
        "expected": 1,
        # Only one turn to reach the target.
    },
    {
        "name": "Multiple Paths",
        "deadends": ["0101", "0001", "0002"],
        "target": "9999",
        "expected": 20,
        # Path exists but multiple turns needed.
    },
    {
        "name": "No Possible Path",
        "deadends": ["0001", "0010", "0100", "1000"],
        "target": "1111",
        "expected": -1,
        # All paths to reach the target are blocked.
    },
    {
        "name": "Large Deadends",
        "deadends": ["0001", "1111", "2222", "3333", "4444", "5555"],
        "target": "6666",
        "expected": 12,
        # Must navigate around many deadends.
    },
    {
        "name": "Edge Case with Same Deadends",
        "deadends": ["9999", "9998"],
        "target": "9990",
        "expected": 9,
        # Requires several moves to reach from 0000 to 9990.
    },
    {
        "name": "Immediate Neighbors",
        "deadends": [],
        "target": "0009",
        "expected": 9,
        # Straight path to reach the target in 9 moves.
    },
]


# def open_lock(deadends: List[str], target: str) -> int:
#     dead_set = set(deadends)
#     if "0000" in dead_set:
#         return -1
#     if target == "0000":
#         return 0

#     queue = deque(["0000"])
#     visited = {"0000"}
#     steps = 0

#     while queue:
#         for _ in range(len(queue)):
#             current = queue.popleft()
#             if current == target:
#                 return steps

#             for i in range(4):
#                 for move in [-1, 1]:
#                     next_digit = (int(current[i]) + move) % 10
#                     next_combination = current[:i] + str(next_digit) + current[i+1:]

#                     if next_combination not in visited and next_combination not in dead_set:
#                         visited.add(next_combination)
#                         queue.append(next_combination)

#         steps += 1

#     return -1

def run_test_for_func(open_lock_func):
    print(f"Testing function: {open_lock_func.__name__}")
    for case in test_cases:
        deadends = case["deadends"]
        target = case["target"]
        expected = case["expected"]
        result = open_lock_func(deadends, target)
        assert result == expected, f"Test case '{case['name']}' failed: expected {expected}, got {result}"
    print("All test cases completed!")



def open_lock_1(deadends:List[str], target:str)->int:
    digits_ary = ['0','1','2','3','4','5','6','7','8','9']


    for i in digits_ary:
        for j in digits_ary:
            for k in digits_ary:
                for l in digits_ary:
                    subStr = i+j+k+l







    return 0




# # Run the test function
# run_test_for_func(open_lock)


```

