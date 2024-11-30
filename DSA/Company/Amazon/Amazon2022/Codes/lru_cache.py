
from collections import OrderedDict


# Test cases for the LRU Cache
lru_cache_test_cases = [
    # Case 1: Basic put and get
    {
        "name": "Basic Put and Get",
        "actions": [("put", 1, 1), ("get", 1)],
        "expected": 1,
    },
    # Case 2: Getting a non-existent key
    {
        "name": "Get Non-existent Key",
        "actions": [("get", 2)],
        "expected": -1,
    },
    # Case 3: Adding beyond capacity
    {
        "name": "Add Beyond Capacity",
        "actions": [("put", 1, 1), ("put", 2, 2), ("put", 3, 3), ("get", 2)],
        "expected": 2,
    },
    # Case 4: Evicting the least recently used item
    {
        "name": "Evict LRU",
        "actions": [("put", 1, 1), ("put", 2, 2), ("put", 3, 3), ("get", 1)],
        "expected": -1,
    },
    # Case 5: Updating an existing key
    {
        "name": "Update Existing Key",
        "actions": [("put", 1, 1), ("put", 1, 10), ("get", 1)],
        "expected": 10,
    },
    # Case 6: Edge case with capacity 1
    {
        "name": "Capacity One",
        "actions": [("put", 1, 1), ("get", 1), ("put", 2, 2), ("get", 1), ("get", 2)],
        "expected": 2,
    },
    # Case 7: Multiple puts and gets
    {
        "name": "Multiple Puts and Gets",
        "actions": [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2)],
        "expected": -1,  # 2 should be evicted
    },
]

def test_lru_cache(func):
    print(f"Testing function: {func.__name__}")

    for test_case in lru_cache_test_cases:
        actions = test_case["actions"]
        expected = test_case["expected"]
        case_name = test_case["name"]

        # Create a new LRUCache instance for each test case
        cache = LRUCache(2)  # Assuming a capacity of 2 for simplicity

        result = None
        for action in actions:
            if action[0] == "put":
                cache.putValue(action[1], action[2])
            elif action[0] == "get":
                result = cache.getValue(action[1])

        # Check if the final result matches the expected result
        assert result == expected, f"Test case ({case_name}) failed: expected {expected}, got {result}"

    print("All test cases passed!")


class LRUCache(OrderedDict):

    def __init__(self, capacity:int)-> None:
        self.capacity = capacity

    def getValue(self, key:int)->int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1

    def putValue(self, key:int, value:int)-> None:
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last = False)

        self.move_to_end(key)



# Run the test function
test_lru_cache(LRUCache)
