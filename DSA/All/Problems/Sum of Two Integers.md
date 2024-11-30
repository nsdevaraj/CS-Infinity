
leetcode 371 - https://leetcode.com/problems/sum-of-two-integers/submissions/


The **Sum of Two Integers** problem on LeetCode (Problem #371) is a common coding challenge that asks you to calculate the sum of two integers without using the `+` or `-` operators. This problem typically involves bit manipulation to simulate addition.

### Problem Statement
Given two integers, `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

**Example 1:**
- **Input:** `a = 1`, `b = 2`
- **Output:** `3`

**Example 2:**
- **Input:** `a = 2`, `b = 3`
- **Output:** `5`

**Constraints:**
- $-2^{31} \leq a, b \leq 2^{31} - 1$


XOR => 2 different give 1 else give 0



### Approach
To solve this problem, we use **bit manipulation** to handle the addition without using `+` or `-`:
1. **Bitwise AND** (`a & b`) gives the carry that needs to be added to the sum.
2. **Bitwise XOR** (`a ^ b`) gives the sum without considering the carry.
3. We **left-shift** the carry by one bit (`carry << 1`) because the carry affects the next higher bit position.
4. Repeat this process until there’s no carry left.

For Python, this approach also requires handling **integer overflow**. In a language like Python, which has arbitrary-precision integers, we manually restrict values to 32-bit signed integer limits by:
- Masking with a 32-bit integer (`0xFFFFFFFF`) to simulate 32-bit overflow.
- Converting values to negative if they exceed `2^{31} - 1` (the maximum positive integer in 32-bit representation).

### Code Implementation
Here's how the solution is implemented in Python:

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to keep the result within 32-bit range
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while b != 0:
            # Calculate carry (common bits of a and b)
            carry = (a & b) & mask
            # Sum without carry
            a = (a ^ b) & mask
            # Shift carry to the left
            b = (carry << 1) & mask
        
        # If a is negative in 32-bit signed integer, convert it to negative in Python
        return a if a <= max_int else ~(a ^ mask)
```




### Explanation
1. **Carry Calculation:** `(a & b) & mask` calculates the carry. We use `& mask` to keep the result within 32 bits.
2. **Sum Calculation:** `(a ^ b) & mask` calculates the sum without carry.
3. **Carry Propagation:** `carry << 1` shifts the carry by one position to add it to the next higher bit.
4. **Loop Until No Carry:** We repeat until `b` (the carry) is zero.
5. **Convert to Signed Integer:** If `a` is greater than `max_int`, we interpret it as a negative number in 32-bit signed integer representation.

### Complexity Analysis
- **Time Complexity:** $O(1)$ in the worst case because the loop runs a maximum of 32 times (for 32-bit integers).
- **Space Complexity:** $O(1)$ since we use a constant amount of space.

### Testing
Here's a test function to verify the solution against different cases.

```python
def test_getSum():
    solution = Solution()
    test_cases = [
        {"input": (1, 2), "expected": 3},
        {"input": (2, 3), "expected": 5},
        {"input": (0, 0), "expected": 0},
        {"input": (-1, 1), "expected": 0},
        {"input": (-1, -1), "expected": -2},
        {"input": (123, 456), "expected": 579},
        {"input": (-123, -456), "expected": -579},
        {"input": (2147483647, 1), "expected": -2147483648},  # Edge case for overflow
        {"input": (-2147483648, -1), "expected": 2147483647},  # Edge case for underflow
    ]
    
    for i, test in enumerate(test_cases):
        a, b = test["input"]
        expected = test["expected"]
        result = solution.getSum(a, b)
        assert result == expected, f"Test case {i + 1} failed: Expected {expected}, got {result}"

test_getSum()
```

### Summary Table

| Approach                  | Time Complexity | Space Complexity | Description                                                                                  |
|---------------------------|-----------------|------------------|----------------------------------------------------------------------------------------------|
| Bit Manipulation + Masking | $O(1)$          | $O(1)$           | Uses bitwise XOR, AND, and left shifts with masking to simulate 32-bit signed integer addition.|

This method provides a robust way to handle addition without using the `+` or `-` operators by leveraging bitwise operations.



for this problem, just follow other programming lang, since py make it hard since py handle bits not with 32 , its will be different!

```python

def getSum(self, a: int, b: int) -> int:
	while(b != 0):
	    # get carray by and and do left shift removing last item
		carry = (a & b) << 1
		# doing XOR
		a = a ^ b
		# taking carray and do next iteration when carray present
		b = carry

	return a


```


in py

```python 

bitTest = 0xffffffff # just 32 1's
print(getsizeof(0), getsizeof(0)*8). #=> 24 bytes, 192 bits 
print(getsizeof(-1), getsizeof(1)*8) #=> 28 bytes, 224 bits
print(getsizeof(bitTest), getsizeof(bitTest)*8) #=> 32 bytes, 256 bits
```


```python

def getSum(self, a: int, b: int) -> int:
	bitShortner = 0xffffffff

	# > 0 since bit can be negative
	while((b & bitShortner) > 0):
		carry = (a & b) << 1
		a = a ^ b
		b = carry
	
	return (a & bitShortner) if b > 0 else a
```


Referred {

https://www.youtube.com/watch?v=_pUidg9gQyA



just for -ve values check its comment

https://www.youtube.com/watch?v=6vETcY7qfEo



}

leetcode ans

Memory: 16.3mb

python

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask&b) > 0:
            a , b = a^b , (a&b) <<1
        return (mask & a) if b>0 else a
```

