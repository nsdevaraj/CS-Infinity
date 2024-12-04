

**Find the Missing Number**
**Problem:** Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one number that is missing from the array.

i.e Find the missing number in an array containing only consecutive integers


Input: [3, 0, 1]
Output: 2





The sum of the first \(n\) natural numbers is given by the formula:

$S = \frac{n(n + 1)}{2}$`



**Answer:**
```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
```





Cyclic Sort (Optimized for when the array elements are not distinct)
•	Idea: Use a cyclic sort to place each element at its correct index. The first index where the number doesn't match the index will be the missing number.
•	Steps:
1.	Iterate through the array and swap numbers to their correct positions.
2.	Once sorted, iterate again to find the index where the number is missing.
o	Time Complexity: O(n).
o	Space Complexity: O(1) (in-place sorting).
python
Copy code
def find_missing_number_cyclic(arr):
    i = 0
    while i < len(arr):
        correct = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return len(arr)
These methods provide more variety and might be useful depending on the constraints of your problem (like space, time efficiency, or whether the array is already partially sorted).










How XOR works here:
The XOR operation has the property that a ^ b ^ a = b. This code leverages this by XORing all the numbers from 0 to n (including the missing number) with all the numbers in the array. Since each number except the missing one appears twice, they cancel each other out (due to the XOR property). The final result in missing will be the missing number.
Example:
If arr = [0, 1, 3], the code would do the following:
•	missing = 3 (length of array)
•	missing = 3 ^ 0 ^ 0 (missing ^ index ^ number)
•	missing = 3 ^ 1 ^ 1
•	missing = 3 ^ 2 ^ 3
•	missing = 2 (The missing number)




### Problem Link

[268. Missing Number - LeetCode](https://leetcode.com/problems/missing-number/)

---

### Problem Statement

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the **only number in the range that is missing** from the array.

---

### Examples

**Example 1:**

- **Input:** `nums = [3, 0, 1]`
- **Output:** `2`
- **Explanation:** The range is `[0, 1, 2, 3]`, and `2` is the missing number.

**Example 2:**

- **Input:** `nums = [0, 1]`
- **Output:** `2`
- **Explanation:** The range is `[0, 1, 2]`, and `2` is the missing number.

**Example 3:**

- **Input:** `nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]`
- **Output:** `8`
- **Explanation:** The range is `[0, 1, 2, ..., 9]`, and `8` is the missing number.

---

### Approaches

---

#### Approach 1: Sum Formula

The sum of the first $n$ numbers is given by the formula:  
Sumn=n⋅(n+1)2\text{Sum}_{n} = \frac{n \cdot (n + 1)}{2}  
The difference between this sum and the sum of the elements in the array gives the missing number.

**Code:**

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Sum Formula Approach.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
```

---

#### Approach 2: XOR Method

Using the XOR property:

- $a \oplus a = 0$
- $a \oplus 0 = a$

XOR all indices from $0$ to $n$ and all elements in the array. The remaining value is the missing number.


The **XOR logic** works in this problem due to the properties of XOR:

1. **Key XOR Properties**:
    
    - $a \oplus a = 0$: Any number XORed with itself is 0.
    - $a \oplus 0 = a$: Any number XORed with 0 remains unchanged.
    - XOR is commutative and associative: The order of operations doesn't matter.
2. **How It Works for the Missing Number**:
    
    - If we XOR all indices from $0$ to $n$ and XOR all elements of the `nums` array, any number present in both will cancel out because of the $a \oplus a = 0$ property.
    - The only number left will be the one that is missing, as it doesn't get canceled.
3. **Step-by-Step Example**:
    
    - Input: `nums = [3, 0, 1]`  
        Range: $[0, 1, 2, 3]$ (expected numbers)
    - XOR all numbers in the range:  
        0⊕1⊕2⊕3=0b00⊕0b01⊕0b10⊕0b11=0b10 (2)0 \oplus 1 \oplus 2 \oplus 3 = 0b00 \oplus 0b01 \oplus 0b10 \oplus 0b11 = 0b10 \ (2)
    - XOR all elements in the array:  
        3⊕0⊕1=0b11⊕0b00⊕0b01=0b10 (2)3 \oplus 0 \oplus 1 = 0b11 \oplus 0b00 \oplus 0b01 = 0b10 \ (2)
    - XOR the results of the two steps:  
        (0⊕1⊕2⊕3)⊕(3⊕0⊕1)=2⊕2=2(0 \oplus 1 \oplus 2 \oplus 3) \oplus (3 \oplus 0 \oplus 1) = 2 \oplus 2 = 2

Thus, the missing number is `2`.


**Code:**

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        XOR Approach.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        xor_result = 0
        n = len(nums)
        
        for i in range(n + 1):
            xor_result ^= i
        for num in nums:
            xor_result ^= num
        
        return xor_result
```

---

#### Approach 3: Sorting

Sort the array and check the difference between the index and the value. The first mismatch is the missing number.

**Code:**

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Sorting Approach.
        Time Complexity: O(n \log n) - Due to sorting.
        Space Complexity: O(1) - Ignoring in-place sorting overhead.
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
```

---

#### Approach 4: Set Comparison

Construct a set of numbers from `0` to `n`, and subtract the set of `nums`. The only remaining number is the missing one.

**Code:**

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Set Difference Approach.
        Time Complexity: O(n)
        Space Complexity: O(n) - For set storage.
        """
        return (set(range(len(nums) + 1)) - set(nums)).pop()
```

---

### Summary of Approaches

|Approach|Time Complexity|Space Complexity|Description|
|---|---|---|---|
|**Sum Formula**|$O(n)$|$O(1)$|Uses mathematical sum formula.|
|**XOR Method**|$O(n)$|$O(1)$|Uses XOR properties for calculation.|
|**Sorting**|$O(n \log n)$|$O(1)$|Sorts the array and checks indices.|
|**Set Comparison**|$O(n)$|$O(n)$|Uses a set to find the missing number.|

---


```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return i

        
```



---

### Test Function

```python
def test_missingNumber(func):
    """
    Test function for missingNumber implementations.
    """
    test_cases = [
        {"input": [3, 0, 1], "expected": 2},
        {"input": [0, 1], "expected": 2},
        {"input": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8},
        {"input": [0], "expected": 1},
        {"input": [1], "expected": 0},
        {"input": [0, 2, 3], "expected": 1},
        {"input": [4, 3, 2, 1], "expected": 0},
        {"input": [0, 1, 2, 3], "expected": 4},
        {"input": [], "expected": 0},
        {"input": [5, 4, 3, 2, 0], "expected": 1},
    ]

    for i, test in enumerate(test_cases):
        result = func(test["input"])
        assert result == test["expected"], f"Test case {i + 1} failed: Input {test['input']} Expected {test['expected']}, got {result}"

# Example usage:
# test_missingNumber(Solution().missingNumber)
```

