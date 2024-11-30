

[LeetCode #217](https://leetcode.com/problems/contains-duplicate)

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

Set

```python
def containsDuplicate(nums: List[int]) -> bool:
	return len(nums) != len(set(nums))
```


Hash Map

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```


