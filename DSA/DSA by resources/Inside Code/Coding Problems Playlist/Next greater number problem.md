

[Next greater number problem - Inside code](https://youtu.be/0u-5IOhUPas?si=ArisLy4pRMCDCZ7f)


### Next Greater Number Problem - Inside Code


#### Problem Statement:
You are given a positive integer `num`. Your task is to **find the next greater integer** that can be formed using the same digits of `num`. If no greater number can be formed, return `num` itself.

For example:
- Input: `231`
- Output: `312` (The next greater integer made from digits `2, 3, 1` is `312`)

If `num` is already the greatest possible arrangement of its digits, return `num`. For instance:
- Input: `321`
- Output: `321` (There is no greater arrangement possible)

---

### Brute Force Approach (Naive Solution)

#### Explanation:
The brute force solution consists of generating all **permutations** of the digits of `num`, sorting them, and finding the next permutation that is larger than `num`.

#### Steps:
1. Generate all permutations of the digits.
2. Sort the permutations.
3. Find `num` in the sorted list and return the next permutation.
4. If `num` is the largest permutation, return `num`.

This approach is inefficient as its time complexity is **$O(n!)$**, where `n` is the number of digits.

#### Python Code (Brute Force):
```python
from itertools import permutations

def nextGreaterBruteForce(num: int) -> int:
    # Convert num to a list of digits
    digits = list(str(num))
    
    # Generate all permutations of the digits
    perms = sorted(set(permutations(digits)))
    
    # Find num's position in the sorted list of permutations
    for i, perm in enumerate(perms):
        if perm == tuple(digits):
            # If num is the last permutation, return num itself
            if i == len(perms) - 1:
                return num
            # Return the next greater permutation
            return int("".join(perms[i + 1]))

# Example Usage
print(nextGreaterBruteForce(231))  # Output: 312
print(nextGreaterBruteForce(321))  # Output: 321
```

#### Time Complexity:
- **$O(n!)$** to generate and sort all permutations, where `n` is the number of digits in `num`.

#### Space Complexity:
- **$O(n!)$** for storing all permutations.

---

### Efficient Approach (Optimal Solution)

#### Key Insight:
To solve this problem efficiently, we need to observe that:
1. We want to swap some digits to create the **smallest possible larger number**.
2. Start from the **rightmost side** of the number and identify the first digit that **breaks the descending order**.
3. Swap this digit with the smallest digit to its right that is **greater** than it.
4. Finally, **reverse** the digits to the right of this swapped position to get the smallest arrangement.

#### Steps:
1. Convert `num` to a list of digits for easy manipulation.
2. Traverse the digits from **right to left** and find the first position where a smaller digit is followed by a larger digit (this is the **break point**).
3. If no such point is found, the digits are in **descending order**, and there is no larger number possible.
4. Swap the break point digit with the **smallest larger digit** to its right.
5. Reverse the digits after the break point to get the **smallest possible greater number**.

#### Python Code (Optimal Solution):
```python
from typing import List

def nextGreater(num: int) -> int:
    digits = list(str(num))  # Convert num to a list of digits
    
    # Step 1: Find the first digit (from right) that is smaller than the digit next to it
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such digit is found, the number is in descending order, return num itself
    if i == -1:
        return num
    
    # Step 2: Find the smallest digit on the right side that is greater than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Step 3: Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]
    
    # Step 4: Reverse the digits after i
    digits[i + 1:] = reversed(digits[i + 1:])
    
    # Convert back to integer and return
    return int("".join(digits))

# Example Usage
print(nextGreater(231))  # Output: 312
print(nextGreater(321))  # Output: 321
print(nextGreater(18540))  # Output: 40158
```

#### Time Complexity:
- **$O(n)$**, where `n` is the number of digits.
  - We traverse the list of digits twice: once to find the breaking point and once to swap and reverse.

#### Space Complexity:
- **$O(n)$** because we store the digits in an array.

---

### Example Walkthrough:

**Example 1:**
- Input: `231`
- Output: `312`
  
**Steps:**
1. Identify the first digit that breaks the descending order: `2` (index 0).
2. Find the smallest digit to the right of `2` that is larger than `2`: `3` (index 1).
3. Swap `2` and `3`, resulting in `[3, 2, 1]`.
4. Reverse the digits after index 0: `312`.

**Example 2:**
- Input: `321`
- Output: `321`
  
**Steps:**
1. Traverse the digits from right to left and find that all digits are in descending order.
2. Return `321` as there is no next greater number.

**Example 3:**
- Input: `18540`
- Output: `40158`
  
**Steps:**
1. The first breaking point is `4` (index 1).
2. The smallest larger digit is `5` (index 4).
3. Swap `4` and `5`, then reverse the digits after index 1.

---

This approach efficiently solves the problem in **linear time** compared to the brute force method that has **factorial time complexity**.