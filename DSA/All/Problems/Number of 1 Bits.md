
### Number of 1 Bits (LeetCode #191)

**LeetCode Link:** [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

[Number of 1 Bits @NeedCode ](https://www.youtube.com/watch?v=5Km3utixwZs)

### Problem Statement
Given an unsigned integer `n`, return the number of `1` bits in its binary representation. This is also known as finding the Hamming weight of the integer.

### Examples
**Example 1:**
- **Input:** `n = 00000000000000000000000000001011`
- **Output:** `3`
- **Explanation:** The binary representation of 11 has three `1`s.

**Example 2:**
- **Input:** `n = 00000000000000000000000010000000`
- **Output:** `1`
- **Explanation:** The binary representation of 128 has one `1`.

**Example 3:**
- **Input:** `n = 11111111111111111111111111111101`
- **Output:** `31`
- **Explanation:** The binary representation of -3 (in 32-bit two's complement) has thirty-one `1`s.

### Approaches
We will discuss two main approaches to solve this problem: 

1. **Bitwise Right Shift and Modulus**
2. **Brian Kernighan's Algorithm**


2 way of finding last bit is 1 or 0

```python
* valueAny bitwise_and by value1( efficient )
* valueAny mod 2 
```

to remove last bit

```python
* right shift by 1 ( efficient )
* div by 2 
```

#### 1. Bitwise Right Shift and Modulus

In this approach, we iterate through each bit of the integer using bitwise operations.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # Initialize count of 1 bits
        while n:  # Continue until n becomes 0
            count += n & 1  # Check if the least significant bit is 1
            n >>= 1  # Right shift n to process the next bit
        return count  # Return the total count of 1 bits
```

#### 2. Brian Kernighan's Algorithm

This method counts set bits more efficiently by turning off the rightmost `1` bit in each iteration.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # Initialize count of 1 bits
        while n != 0:  # Continue until n becomes 0
            n &= (n - 1)  # Clear the lowest set bit
            count += 1  # Increment count for each cleared bit
        return count  # Return the total count of 1 bits
```

### Complexity Analysis
- **Time Complexity:** 
  - Bitwise Right Shift: $O(b)$, where \( b \) is the total number of bits (32 for a standard integer).
  - Brian Kernighan’s Algorithm: $O(k)$, where \( k \) is the number of `1` bits in `n`.
  
- **Space Complexity:** 
  - Both approaches: $O(1)$, as we use a constant amount of space.

### Summary Table

| Approach                    | Time Complexity | Space Complexity | Description                                                                                 |
|-----------------------------|-----------------|------------------|---------------------------------------------------------------------------------------------|
| Bitwise Right Shift         | $O(b)$          | $O(1)$           | Iteratively checks each bit by right-shifting the number.                                  |
| Brian Kernighan’s Algorithm | $O(k)$          | $O(1)$           | Efficiently counts `1` bits by removing the lowest set bit in each iteration.              |

### Testing the Function
Here's a test function to validate both approaches:

```python
def test_hammingWeight():
    solution = Solution()
    test_cases = [
        {"input": int("00000000000000000000000000001011", 2), "expected": 3},
        {"input": int("00000000000000000000000010000000", 2), "expected": 1},
        {"input": int("11111111111111111111111111111101", 2), "expected": 31},
        {"input": 0, "expected": 0},
        {"input": int("11111111111111111111111111111111", 2), "expected": 32},  # all bits set to 1
    ]
    
    for i, test in enumerate(test_cases):
        result = solution.hammingWeight(test["input"])
        assert result == test["expected"], f"Test case {i+1} failed: Expected {test['expected']}, got {result}"

test_hammingWeight()  # Run the test function
```

This code will validate the functionality of both implementations of the Hamming weight calculation. Each approach can be tested independently by simply calling the appropriate method within the `Solution` class.


leet code:

Memory: 15.9mb

python

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_rep = bin(n)[2:]
        ones_count = binary_rep.count('1')
        return ones_count
        
```





to check {

https://www.youtube.com/watch?v=nttpF8kwgd4&pp=ygUUY291bnQgMSBiaXRzIHByb2JsZW0%3D


}