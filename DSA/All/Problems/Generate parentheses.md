

[Generate parentheses - YT(InsideCode)](https://www.youtube.com/watch?v=o3DUXPRyvT8&list=PL3edoBgC7ScW_CBHbMc0FtdXfzgpBOGIb&index=29&t=1590s) 

[? Generate Parentheses @LeetCode #22](https://leetcode.com/problems/generate-parentheses)



## Problem: Generate Parentheses

We are given an integer $n$, and the task is to generate all valid combinations of $n$ pairs of parentheses. 

### Problem Statement:

Given an integer $n$, generate all valid combinations of $n$ pairs of parentheses. A combination is valid if:
1. Every opening parenthesis `(` has a corresponding closing parenthesis `)`.
2. No closing parenthesis appears without a preceding unused opening parenthesis.

**Example:**
- **Input**: $n = 3$
- **Output**: `["((()))", "(()())", "(())()", "()(())", "()()()"]`


The text in the image states:

"A combination that contains one type of parentheses is valid if every opening parenthesis has its closing parenthesis, and it doesn't have a closing parenthesis without having an unused opening parenthesis before it."

### Explanation:
For a sequence of parentheses to be valid:
1. Every opening parenthesis `(` must have a corresponding closing parenthesis `)`.
2. A closing parenthesis `)` cannot appear before its matching opening parenthesis `(`.

### Examples:

#### Valid cases:
1. **Example 1: `()`**
   - There is one opening parenthesis and one closing parenthesis in the correct order.

2. **Example 2: `(())`**
   - The parentheses are properly nested: two pairs of opening and closing parentheses.

3. **Example 3: `((()))`**
   - Multiple levels of nesting, but every opening parenthesis has a corresponding closing one.

#### Invalid cases:
1. **Example 1: `)(`**
   - The closing parenthesis comes before the opening one, which violates the rule.

2. **Example 2: `(()`**
   - There is an unmatched opening parenthesis.

3. **Example 3: `())`**
   - There is an unmatched closing parenthesis.

The key is to maintain balance between the opening and closing parentheses as you traverse the sequence.

### Approach 1: Backtracking

Backtracking is ideal for problems that require generating all combinations and pruning invalid ones as early as possible. 

#### Key Points:
- For every combination, we can either add an opening parenthesis `(` or a closing parenthesis `)`. 
- At every stage, we ensure that the combination remains valid by maintaining a balance variable (`diff`) that tracks the difference between opening and closing parentheses.
  - If `diff < 0` (more closing than opening), the current branch is invalid, and we backtrack.
  - If `diff > n` (too many unclosed opening parentheses left), we also backtrack.
  - We add a combination only if it is valid when all parentheses are added (`diff == 0` at the end).

**Recursive Function Workflow**:
- At each recursive call, we either:
  - Add an opening parenthesis `(`, incrementing `diff`.
  - Add a closing parenthesis `)`, decrementing `diff`.
- The recursion continues until all $2n$ parentheses are added, and the valid combinations are returned.

### Code:

#### check validity 

```python
def is_valid(combination: str) -> bool:
    # Initialize an empty stack to keep track of open parentheses
    stack = []

    # Traverse each character in the given combination
    for par in combination:
        if par == '(':  # If we encounter an opening parenthesis
            # Push it onto the stack
            stack.append(par)
        else:
            # Validity condition 1: Check if stack is not empty (to prevent popping from an empty stack)
            # If stack is empty, it means we found a closing parenthesis without an opening one
            if len(stack) == 0:
                return False
            else:
                # Pop the matching opening parenthesis from the stack
                stack.pop()

    # Validity condition 2: After processing all parentheses, the stack must be empty
    # If it's not, it means there are unmatched opening parentheses
    return len(stack) == 0

```



```python
def is_valid(combination: str) -> bool:
    # Initialize a counter to track the balance between opening and closing parentheses
    diff = 0

    # Traverse each character in the given combination
    for par in combination:
        if par == '(':  # If we encounter an opening parenthesis
            # Increment diff, as we have one more unmatched opening parenthesis
            diff += 1
        else:
            # Validity condition 1: Check if diff is zero
            # If diff is 0, it means there's no unmatched opening parenthesis left to pair with this closing parenthesis
            if diff == 0:
                return False
            else:
                # Decrement diff, as we found a match for one opening parenthesis
                diff -= 1

    # Validity condition 2: After processing all parentheses, diff should be zero
    # If diff is not zero, it means there are unmatched opening parentheses left
    return diff == 0

```


### Answers

 

```python
from typing import List

def generate_parentheses(n: int) -> List[str]:
    def rec(n: int, diff: int, comb: List[str], combs: List[str]) -> None:
        # Base cases to stop recursion
        if diff < 0 or diff > n:  # Invalid combination, backtrack
            return
        elif n == 0:  # If no more parentheses to add
            if diff == 0:  # If balance is maintained, add to result
                combs.append(''.join(comb))
        else:
            # Try adding an opening parenthesis
            comb.append('(')
            rec(n - 1, diff + 1, comb, combs)
            comb.pop()  # Backtrack
            
            # Try adding a closing parenthesis
            comb.append(')')
            rec(n - 1, diff - 1, comb, combs)
            comb.pop()  # Backtrack
    
    combs = []  # This will store all valid combinations
    rec(2 * n, 0, [], combs)  # Start the recursion with initial parameters
    return combs
```

### Explanation:
- `n`: Remaining number of parentheses to add (total $2n$ since $n$ pairs).
- `diff`: The difference between the number of opening and closing parentheses. It should stay within a valid range.
- `comb`: The current combination of parentheses being built.
- `combs`: The list of valid combinations found.

### Time Complexity:
The time complexity for generating all combinations is $O(n \cdot 2^n)$. This comes from:
- Exploring every possible combination of parentheses with depth $2n$.
- Each valid combination has length $2n$, and we need to store and process them.

### Space Complexity:
- Call stack requires $O(n)$ space for the recursion, where $n$ is the depth of the recursion tree.
- Additionally, we need $O(n \cdot 2^n)$ space to store the valid combinations.

### Recurrence Relation:
The recurrence relation for this approach is: 
\[
T(n) = 2T(n-1) + O(1)
\]
Solving this gives the overall time complexity of $O(n \cdot 2^n)$.


```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(remaining: int = n * 2, open_count: int = 0, current: List[str] = []):
            # If there are more closing parentheses than opening ones, it's invalid
            if open_count < 0:
                return
            
            # If we have used more open parentheses than allowed, stop
            if open_count > n:
                return
            
            # Base case: if there are no parentheses left to add
            if remaining == 0:
                if open_count == 0:
                    result.append(''.join(current))
                return
            
            # Try adding an open parenthesis
            current.append('(')
            backtrack(remaining - 1, open_count + 1, current)
            current.pop()  # backtrack

            # Try adding a closing parenthesis
            current.append(')')
            backtrack(remaining - 1, open_count - 1, current)
            current.pop()  # backtrack

        backtrack()
        return result

```


```python
class Solution:
    def backtrack(self,st,oc,cc,n,res):
        if oc==n==cc:
            res.append(st)
            return 
        if oc<n:
            self.backtrack(st+'(',oc+1,cc,n,res)
        if cc<oc:
            self.backtrack(st+')',oc,cc+1,n,res)
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        aa=self.backtrack("",0,0,n,res)
        return res
```


```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # choices are to select "(" or ")"
        # constraints are "(" must precede a ")" and num () must be equal to n
        # back out is to remove "("
        # goal is when the len(string) == 2*n

        res = []
        p = ""
        def backtrack(numOpen, numClosed, p):
            if numOpen > n or numClosed > n or numClosed > numOpen:
                return
            elif len(p) == 2 * n:
                res.append(p)
                return

            backtrack(numOpen + 1, numClosed, p + "(")
            backtrack(numOpen, numClosed + 1, p + ")")
        
        backtrack(0, 0, "")
        return res
```

---

### Approach 2: Iterative Stack-Based Approach 

An iterative solution can also generate valid parentheses combinations by leveraging a stack. Here, we simulate the recursive approach but using an explicit stack to handle the states.

### Code:

```python
from typing import List

def generate_parentheses_iterative(n: int) -> List[str]:
    stack = [('(', 1, 0)]  # (current_combination, open_count, close_count)
    result = []
    
    while stack:
        comb, open_count, close_count = stack.pop()
        
        # If we have used all n pairs, add to result
        if open_count == n and close_count == n:
            result.append(comb)
        
        # Add opening parentheses if possible
        if open_count < n:
            stack.append((comb + '(', open_count + 1, close_count))
        
        # Add closing parentheses if valid
        if close_count < open_count:
            stack.append((comb + ')', open_count, close_count + 1))
    
    return result
```

### Explanation:
- Use a stack to maintain the current combination, the count of open and close parentheses used so far.
- Push valid transitions (either opening or closing parentheses) onto the stack until we generate all valid combinations.

### Time Complexity:
The time complexity remains $O(n \cdot 2^n)$, as we're still exploring all valid paths in the parentheses combinations.

### Space Complexity:
The space complexity for this approach is $O(n \cdot 2^n)$ due to the need to store combinations in memory.

---

### Summary of Approaches

| Approach            | Time Complexity | Space Complexity | Explanation |
|---------------------|-----------------|------------------|-------------|
| **Recursive Backtracking** | $O(n \cdot 2^n)$  | $O(n \cdot 2^n)$  | Uses recursion to explore all valid combinations. Efficiently prunes invalid ones. |
| **Iterative Stack-based**  | $O(n \cdot 2^n)$  | $O(n \cdot 2^n)$  | Uses a stack to simulate the recursive backtracking approach iteratively. |

---

I hope this lecture gave you a clear understanding of how to generate valid parentheses combinations using backtracking. We also discussed an alternative iterative approach for solving the problem. Both approaches have the same time and space complexity.


to check {

https://www.geeksforgeeks.org/print-all-combinations-of-balanced-parentheses/


}


