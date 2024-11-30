

The **k-th permutation problem** involves generating the k-th permutation of a sequence of numbers. Below are three different approaches to solve this problem, along with their respective code, time complexity, and space complexity.

### Approach 1: Factorial Number System

This approach uses the factorial number system to determine the k-th permutation directly without generating all permutations.

#### Code:
```python
from math import factorial

def get_permutation(n: int, k: int) -> str:
    nums = list(range(1, n + 1))
    k -= 1  # Convert to zero-based index
    permutation = []

    for i in range(n):
        idx = k // factorial(n - 1 - i)
        permutation.append(str(nums[idx]))
        nums.pop(idx)
        k %= factorial(n - 1 - i)

    return ''.join(permutation)

# Example usage
n = 4
k = 9
print(get_permutation(n, k))  # Output: "2314"
```

#### Time Complexity:
- **O(n²)**: The loop runs n times, and the `pop` operation takes O(n) time in the worst case.

#### Space Complexity:
- **O(n)**: For the list of numbers and the result.

---

### Approach 2: Backtracking

In this method, we generate permutations using backtracking and keep count until we reach the k-th permutation.

#### Code:
```python
def backtrack(nums, path, result, k):
    if len(path) == len(nums):
        result.append(''.join(map(str, path)))
        return

    for i in range(len(nums)):
        backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result, k)

def get_kth_permutation(n: int, k: int) -> str:
    nums = list(range(1, n + 1))
    result = []
    backtrack(nums, [], result, k)
    return result[k - 1]  # k is 1-based

# Example usage
n = 4
k = 9
print(get_kth_permutation(n, k))  # Output: "2314"
```

#### Time Complexity:
- **O(n!)**: All permutations are generated, which is factorial time.

#### Space Complexity:
- **O(n)**: For the recursion stack and the result list.

---

### Approach 3: Iterative Approach Using Heapq (for finding permutations)

This approach generates permutations iteratively and retrieves the k-th permutation.

#### Code:


```python
import itertools

def get_kth_permutation(n: int, k: int) -> str:
    nums = list(map(str, range(1, n + 1)))
    permutations = itertools.permutations(nums)
    for _ in range(k - 1):  # Skip to the k-th
        next(permutations)
    return ''.join(next(permutations))

# Example usage
n = 4
k = 9
print(get_kth_permutation(n, k))  # Output: "2314"
```

#### Time Complexity:
- **O(n!)**: Generating all permutations is factorial time, and we iterate to the k-th.

#### Space Complexity:
- **O(n)**: For storing the list of numbers.

---

### Summary

1. **Factorial Number System**: Efficient, O(n²) time, O(n) space.
2. **Backtracking**: Simple but inefficient for large n, O(n!) time, O(n) space.
3. **Iterative using itertools**: Straightforward, O(n!) time, O(n) space.

The factorial number system approach is generally the most efficient for this problem, especially for larger values of n.


---

[kth permutation @InsideCode](https://youtu.be/o3DUXPRyvT8?si=pUYVbhN_D2JgMVqI&t=4000)


BruteForce:


```python

def kth_perm(n, k):
	permutations = list(itertools.permutations(range(1,n+1)))
	return ''.join(map(str, permutations[k-1]))
```

This cause `n*n!`  to generate them, Time complexity is `O(n*n!)`


Math:

```python
def kth_perm(n,k):
	permutaiton = []
	unused = list(range(1,n+1))
	
	fact = [1]*(n+1)
	for i in range(1, n+1):
		fact[i] = i * fact[i-1]
	
	k -= 1

	while (n > 0):
		part_length = fact[n] // n
		i = k // part_length
		
		perumatation.append(unused[i])
		unused.pop(i)
		
		n -=1
		k %= part_length
	
	return ''.join(map(str, permutation))
```


Time = O(n^2)
Space = O(n)  # n for perutation , n+1 for factorial array



