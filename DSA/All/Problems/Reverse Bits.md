


### LeetCode Problem: [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)


referred {
https://www.youtube.com/watch?v=UcoN6UjAI64

}


---

### Problem Statement:

You are given a **32-bit unsigned integer**, reverse its bits and return the result as an **unsigned integer**.

---

### Examples:

#### Example 1:

Input:

```plaintext
n = 43261596 (binary: 00000010100101000001111010011100)
```

Output:

```plaintext
964176192 (binary: 00111001011110000010100101000000)
```

#### Example 2:

Input:

```plaintext
n = 4294967293 (binary: 11111111111111111111111111111101)
```

Output:

```plaintext
3221225471 (binary: 10111111111111111111111111111111)
```

---

### Approaches:



```python

def reverseBits1(n: int):
    res = 0  # Initialize the result variable to 0

    for i in range(32):  # Loop through each bit index from 0 to 31
        bit = (n >> i) & 1  # Extract the i-th bit of n
        res = res | (bit << (31 - i))  # Place the extracted bit in the reversed position in res
    return res  # Return the final reversed bits
    
```



---

#### **Approach 1: Bit-by-Bit Reversal**

**Logic**:

- Reverse the bits of the input by extracting each bit from the least significant side (rightmost bit) and shifting it into the reversed number from the leftmost side.
- Use bitwise operations to extract and shift bits:
    - Extract the last bit of `n` using `n & 1`.
    - Shift the bit into the correct position in the result.
    - Right-shift `n` to process the next bit.




**Algorithm**:

1. Initialize `result = 0`.
2. Loop 32 times (since the input is a 32-bit integer):
    - Extract the least significant bit of `n` using `n & 1`.
    - Left-shift `result` by 1 to make space for the new bit.
    - Add the extracted bit to `result`.
    - Right-shift `n` by 1 to remove the processed bit.
3. Return `result`.



**Code**:

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):  # Process all 32 bits
            result = (result << 1) | (n & 1)  # Shift result left and add the last bit of n
            n >>= 1  # Shift n to process the next bit
        return result
```

**Time Complexity**:

- $O(32) = O(1)$: Always loops 32 times, regardless of input.

**Space Complexity**:

- $O(1)$: No extra space used apart from variables.

---

#### **Approach 2: Precompute Masks (Optimized for Multiple Calls)**

**Logic**:

- If you need to reverse bits for multiple inputs, you can use **precomputed lookup tables** for efficient bit manipulation.
- Precompute the reverse of 8-bit integers and use it to reverse a 32-bit integer by breaking it into four 8-bit chunks.

**Algorithm**:

1. Precompute a lookup table `reverseByte` for reversing bits in an 8-bit integer.
2. Split the 32-bit input into 4 chunks of 8 bits each.
3. Reverse each chunk using the lookup table and reassemble the 32-bit result.

**Code**:

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        # Precomputed table for reversing bits in a byte
        reverseByte = [0] * 256
        for i in range(256):
            reverseByte[i] = (reverseByte[i >> 1] >> 1) | ((i & 1) << 7)
        
        # Reverse each 8-bit chunk using the lookup table
        return (
            (reverseByte[n & 0xff] << 24) |
            (reverseByte[(n >> 8) & 0xff] << 16) |
            (reverseByte[(n >> 16) & 0xff] << 8) |
            (reverseByte[(n >> 24) & 0xff])
        )
```

**Time Complexity**:

- $O(1)$: Lookup and bit-shifting operations are constant time.

**Space Complexity**:

- $O(256) = O(1)$: Precomputed lookup table size.

---

#### **Approach 3: Python Built-In Functions**

**Logic**:

- Convert the integer to its binary string, reverse the string, and convert it back to an integer.
- Use Python's built-in functions for simplicity.

**Code**:

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert to binary string, reverse, and convert back to integer
        return int(bin(n)[2:].zfill(32)[::-1], 2)
```

**Time Complexity**:

- $O(32) = O(1)$: Constant number of operations for 32 bits.

**Space Complexity**:

- $O(32) = O(1)$: Space used for the binary string representation.

---

### Summary of Approaches:

|**Approach**|**Time Complexity**|**Space Complexity**|**Remarks**|
|---|---|---|---|
|**Bit-by-Bit Reversal**|$O(1)$|$O(1)$|Best for one-off calculations.|
|**Precomputed Masks**|$O(1)$|$O(1)$|Efficient for repeated calculations.|
|**Built-In Functions**|$O(1)$|$O(1)$|Simplest to implement, but less efficient.|

---


untime: 14ms

python

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans |= (n & 1) << (31 - i)
            n >>= 1
        return ans
```



python

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        binn = bin(n)[2:].zfill(32)
        return int(binn[::-1], 2)
```



-----


### Test Function:

```python
def test_reverseBits(func):
    test_cases = [
        {"input": 0b00000010100101000001111010011100, "expected": 0b00111001011110000010100101000000},
        {"input": 0b11111111111111111111111111111101, "expected": 0b10111111111111111111111111111111},
        {"input": 0b00000000000000000000000000000000, "expected": 0b00000000000000000000000000000000},
        {"input": 0b11111111111111111111111111111111, "expected": 0b11111111111111111111111111111111},
    ]
    for i, case in enumerate(test_cases):
        result = func(case["input"])
        assert result == case["expected"], f"Test case {i+1} failed: Input {case['input']:032b} Expected {case['expected']:032b}, but got {result:032b}"
    print("All test cases passed!")

# Test the first approach
solution = Solution()
test_reverseBits(solution.reverseBits)
```