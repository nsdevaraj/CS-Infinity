

[LeetCode #39 - Combination Sum](https://leetcode.com/problems/combination-sum/)


[Combination Sum - Backtracking - @NeetCode](https://www.youtube.com/watch?v=GBKI9VSKdGg)

---

#### Problem Statement:
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

**Constraints:**
- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

#### Example 1:

**Input:**
```plaintext
candidates = [2,3,6,7], target = 7
```
**Output:**
```plaintext
[[2,2,3],[7]]
```
**Explanation:**
- `2 + 2 + 3 = 7`
- `7 = 7`
- These are the only two combinations that sum to `7`.

#### Example 2:

**Input:**
```plaintext
candidates = [2,3,5], target = 8
```
**Output:**
```plaintext
[[2,2,2,2],[2,3,3],[3,5]]
```

#### Example 3:

**Input:**
```plaintext
candidates = [2], target = 1
```
**Output:**
```plaintext
[]
```

---

### Approaches:

#### 1. Backtracking

##### Explanation:
The most common approach for solving the "Combination Sum" problem is **backtracking**. This technique systematically builds a solution by exploring different combinations of candidates, choosing an element multiple times if necessary, and backtracking when a certain combination exceeds the target sum.

##### Steps:
1. Sort the array to improve efficiency by avoiding unnecessary recursions.
2. Use recursion to explore all possible combinations. For each recursive call, the problem is reduced by subtracting the current candidate from the target.
3. When a combination matches the target, it is added to the result.
4. If the sum exceeds the target, we backtrack and try a different combination.


## easy dfs

```python
from typing import List

class Solution:
    # Function to find all unique combinations that sum up to the target
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # This will store all the valid combinations

        # Depth-First Search (DFS) helper function
        def dfs(i, cur, total):
            # If the current total equals the target, we have a valid combination
            if total == target:
                res.append(cur.copy())  # Append a copy of the current combination
                return

            # If we've gone past the candidate list or exceeded the target, stop
            if i >= len(candidates) or total > target:
                return

            # Include the current candidate in the combination and recurse
            cur.append(candidates[i])
            # Recur with the same index (i) because we can reuse the same candidate
            dfs(i, cur, total + candidates[i])

            # Backtrack: remove the last element and try the next candidate
            cur.pop()
            # Recur with the next index to explore other candidates
            dfs(i + 1, cur, total)

        # Initial call to the DFS with index 0, empty current combination, and total 0
        dfs(0, [], 0)
        
        return res  # Return the list of valid combinations

```

##### Code (Python):


```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(combination, start, target):
            # If the target is met, add the combination to the result
            if target == 0:
                result.append(list(combination))
                return
            # If target goes negative, no point in continuing
            elif target < 0:
                return
            
            # Try all candidates from the current position onwards
            for i in range(start, len(candidates)):
                # Include the candidate in the current combination
                combination.append(candidates[i])
                # Recursively try to find combinations with the reduced target
                backtrack(combination, i, target - candidates[i])
                # Backtrack by removing the last added candidate
                combination.pop()
        
        # Sort candidates (optional, but helps avoid some unnecessary recursions)
        candidates.sort()
        # Start the backtracking process
        backtrack([], 0, target)
        return result
```

##### Time Complexity:
- In the worst case, we may have to explore every combination of the numbers, leading to exponential time complexity: $O(2^{T/D})$, where $T$ is the target and $D$ is the smallest candidate.
  
##### Space Complexity:
- The space complexity is proportional to the depth of the recursion tree, which is $O(T/D)$, where $T$ is the target and $D$ is the smallest candidate. The space used by the result list is proportional to the number of valid combinations.

#### 2. Dynamic Programming (Alternative Approach)

##### Explanation:
A dynamic programming (DP) approach can be used as an alternative. Here, the problem is solved iteratively by using a DP table that stores combinations for each sub-target leading up to the final target.

##### Steps:
1. Create a DP table where each index `i` represents the target sum `i`.
2. For each candidate, update the DP table by adding combinations that lead to the target.


```python
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # DP table where dp[i] holds all combinations that sum up to i
    dp = [[] for _ in range(target + 1)]
    
    # There's one way to make target 0: use no numbers
    dp[0].append([])

    # Iterate through each candidate number
    for cur_num in candidates:
        # For each number, try to form sums from cur_num up to the target
        for cur_tgt in range(cur_num, target + 1):
            # Calculate the needed target to reach cur_tgt by subtracting cur_num
            need_tgt = cur_tgt - cur_num
            # For each combination that sums to need_tgt, add cur_num to form cur_tgt
            for need_tgt_comb in dp[need_tgt]:
                # Append the new combination to dp[cur_tgt]
                dp[cur_tgt].append(need_tgt_comb + [cur_num])
    
    # Return all combinations that sum up to the target
    return dp[target]

```
##### Code (Python):
```python
from typing import List

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

	# DP table where dp[i] holds all combinations that sum up to i
	dp = [[] for _ in range(target + 1)]
	dp[0].append([])  # There's one way to make target 0: use no numbers
	
	for num in candidates:
		for t in range(num, target + 1):
			for comb in dp[t - num]:
				dp[t].append(comb + [num])
	
	return dp[target]
```

##### Time Complexity:
- The time complexity is $O(N \times T)$, where $N$ is the number of candidates and $T$ is the target.

##### Space Complexity:
- The space complexity is also $O(N \times T)$ due to the DP table.



### need sorted results


[CombinarionSum - sorted order results @HackerRank](https://www.hackerrank.com/contests/vit-bhopal/challenges/combinational-sum-1-1/submissions/code/1384682263)


- Given an array of positive integers arr[] and an integer x, The task is to find all unique combinations in arr[] where the sum is equal to x.
- The same repeated number may be chosen from arr[] an unlimited number of times. Elements in a combination (a1, a2, …, ak) must be printed in non-descending order. (ie, a1 <= a2 <= … <= ak). If there is no combination possible print “Empty”.


```python
n = int(input())
options = list(map(int, input().split()))
tgt = int(input())


# Create a list of lists to store combinations for each target value
dp = [[] for _ in range(tgt + 1)]

# Start with an empty combination for the target 0
dp[0].append([])

# Iterate through each option
for i in range(len(options)):
    option = options[i]
    for cur_tgt in range(option, tgt + 1):
        need_tgt = cur_tgt - option
        for comb in dp[need_tgt]:
                dp[cur_tgt].append(comb + [option])

# Get the combinations for the target value
ans = dp[tgt]

# Print results
if ans:
    # sorted order
    ans.sort()
    for a in ans:
        print(*a)
else:
    print("Empty")

```


### Section 2: Approaches Comparison and Test Function

#### Approaches Comparison Table

T / D => target or depth (when put 1, depth = target )

| Approach                | Time Complexity | Space Complexity | Key Idea                                                                                                  |
| ----------------------- | --------------- | ---------------- | --------------------------------------------------------------------------------------------------------- |
| **Backtracking**        | $O(2^{T/D})$    | $O(T/D)$         | Systematically explores combinations and backtracks when needed. Recursion is used to explore valid sums. |
| **Dynamic Programming** | $O(N \times T)$ | $O(N \times T)$  | Builds up solutions iteratively using sub-solutions stored in a table.                                    |

- **Time Complexity Explanation**: 
    - In the backtracking approach, each recursive call can potentially explore all combinations, and thus, the time complexity grows exponentially with the target and the size of the smallest element.
    - The dynamic programming approach iterates over the candidates and the target, leading to a more efficient polynomial time solution compared to backtracking.

- **Space Complexity Explanation**:
    - In backtracking, the recursion depth is bounded by $T/D$, where $T$ is the target and $D$ is the smallest candidate. This results in $O(T/D)$ space complexity for the recursion stack.
    - The dynamic programming approach stores all possible combinations up to the target in a table, leading to $O(N \times T)$ space complexity.

---

#### Test Function with Distinct Test Cases

Here’s the test function with various cases to test the solution on different scenarios, such as no solution, multiple combinations, etc.

```python
def test_combination_sum(solution):
    test_cases = [
        # Test case 1: Simple combination of two numbers
        {
            "candidates": [2, 3, 6, 7],
            "target": 7,
            "expected": [[2, 2, 3], [7]]
        },
        # Test case 2: Multiple combinations of numbers
        {
            "candidates": [2, 3, 5],
            "target": 8,
            "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        },
        # Test case 3: No solution
        {
            "candidates": [2],
            "target": 1,
            "expected": []
        },
        # Test case 4: Large target value, single combination
        {
            "candidates": [1],
            "target": 5,
            "expected": [[1, 1, 1, 1, 1]]
        },
        # Test case 5: Target equals one of the candidates
        {
            "candidates": [2, 3, 5],
            "target": 5,
            "expected": [[2, 3], [5]]
        },
        # Test case 6: Multiple combinations with large target
        {
            "candidates": [2, 3],
            "target": 10,
            "expected": [[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 3, 3]]
        },
        # Test case 7: Large list of candidates
        {
            "candidates": [1, 2, 3],
            "target": 4,
            "expected": [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]
        },
        # Test case 8: Single candidate equals target
        {
            "candidates": [5],
            "target": 5,
            "expected": [[5]]
        },
        # Test case 9: No combinations that meet the target
        {
            "candidates": [5, 10],
            "target": 3,
            "expected": []
        },
        # Test case 10: No candidates available
        {
            "candidates": [],
            "target": 7,
            "expected": []
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        candidates = test_case["candidates"]
        target = test_case["target"]
        expected = test_case["expected"]
        
        output = solution(candidates, target)
        assert sorted(output) == sorted(expected), f"Test case {i+1} failed: expected {expected}, got {output}"
        print(f"Test case {i+1} passed!")
    
# Running the test function
sol = Solution().combinationSum
test_combination_sum(sol)
```





to check {

https://www.youtube.com/watch?v=inKd43aUqF0

https://www.youtube.com/watch?v=4fCRTF9lZcI

https://www.youtube.com/watch?v=VPdg1gPRe04

https://www.hackerrank.com/contests/pyladies-hackathon/challenges/level-2-storm-find-combinations

https://www.hackerrank.com/challenges/the-power-sum/problem

https://www.hackerrank.com/contests/moodys-analytics-2018-women-in-engineering/challenges/combination-of-digits


https://leetcode.com/problems/combination-sum/solutions/5426168/video-simply-check-all-combinations/

https://www.geeksforgeeks.org/combinational-sum/

https://www.interviewbit.com/problems/combination-sum/


}