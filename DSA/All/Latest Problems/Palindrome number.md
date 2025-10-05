
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Easy problem

## 🔁 Problem: Palindrome Number

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

---

## ✅ Approach 1: Convert Integer to String

This is the most straightforward solution.

### 💡 Idea:

- Convert the number to a string.
    
- Check if the string is equal to its reverse.
    

### 🔧 Code:

```rust
pub fn is_palindrome(x: i32) -> bool {
    let s = x.to_string();
    s.chars().rev().collect::<String>() == s
}
```

### ⏱️ Complexity:

- **Time:** O(n) – where n is the number of digits
    
- **Space:** O(n) – for the string and its reverse
    

---

## ✅ Approach 2: Reverse Half of the Number (No String Conversion)

This is the optimal solution as per the follow-up constraint.

### 💡 Idea:

- Negative numbers are not palindromes.
    
- Reverse only **half** of the number and compare with the other half.
    

### 🔧 Code:

```rust
pub fn is_palindrome(x: i32) -> bool {
    if x < 0 || (x % 10 == 0 && x != 0) {
        return false;
    }

    let mut x = x;
    let mut reversed_half = 0;

    while x > reversed_half {
        reversed_half = reversed_half * 10 + x % 10;
        x /= 10;
    }

    x == reversed_half || x == reversed_half / 10
}
```

### ⏱️ Complexity:

- **Time:** O(log₁₀(n)) – Only half the digits are processed
    
- **Space:** O(1) – Constant space
    

---

## ✅ Approach 3: Full Integer Reversal and Compare (Still No Strings)

This is simpler than half-reversal, but with a small risk of overflow (if not handled).

### 💡 Idea:

- Reverse the full number (check for overflow).
    
- Compare original with reversed.
    

### 🔧 Code:

```rust
pub fn is_palindrome(x: i32) -> bool {
    if x < 0 {
        return false;
    }

    let mut x = x;
    let mut rev = 0;

    while x != 0 {
        match rev.checked_mul(10).and_then(|r| r.checked_add(x % 10)) {
            Some(new_rev) => rev = new_rev,
            None => return false, // Overflow
        }
        x /= 10;
    }

    x == rev
}
```

### ⏱️ Complexity:

- **Time:** O(log₁₀(n))
    
- **Space:** O(1)
    

---

## ✍️ Summary Table

|Approach|Time Complexity|Space Complexity|Notes|
|---|---|---|---|
|String Conversion|O(n)|O(n)|Easiest to implement|
|Half Reversal (No String)|O(log₁₀(n))|O(1)|Most optimal, follows constraints|
|Full Reversal (Safe Overflow)|O(log₁₀(n))|O(1)|Needs overflow safety|

---


Runtime: 0ms

rust

```rust
impl Solution {
    fn revert_n(n: i32, num_size: u32) -> i32 {
        if n == 0 {
            return 0;
        }
        return (n % 10) * 10i32.pow(num_size - 1) + Self::revert_n(n / 10, num_size - 1);
    }

    pub fn is_palindrome(x: i32) -> bool {
        let num_size = (x as f32).log10().floor() + 1f32;
        return Self::revert_n(x, num_size as u32) == x;
    }
}
```



rust

```rust
impl Solution {

pub fn is_palindrome(x: i32) -> bool {
    
    if x < 0 {
        return false;
    }

    let x_str = x.to_string();
    let len = x_str.len();
    
    let front = &x_str[..len/2];
    let back = &x_str[(len/2 + len % 2)..];

    for tuple in front.chars().zip(back.chars().rev()){
        if tuple.0 != tuple.1 {
            return false;
        }
    }
    
    return true;    
}
}
```

---

to check extra:


Palindrome: Same sequence forwards and backwards.
Anagram: Rearranged letters to form a different word or phrase.


**Palindrome Number**
- **Problem**: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
- **Example**:
  - Input: `121`
  - Output: `true`


  To check if a number is a palindrome, there are several different approaches depending on whether you want to reverse the number itself, convert it to a string, or use more mathematical operations. Here are a few approaches along with their explanations:

  ### 1. **String Conversion Approach**
  One of the simplest methods to check if a number is a palindrome is to convert the number to a string, reverse the string, and compare it with the original.

  #### Steps:
  1. Convert the number to a string.
  2. Reverse the string.
  3. Compare the reversed string with the original string.
  4. Return `True` if they are the same, otherwise `False`.

  #### Code:
  ```python
  def is_palindrome(num):
      num_str = str(num)
      return num_str == num_str[::-1]
  ```

  #### Complexity:
  - **Time**: O(n), where `n` is the number of digits in the number.
  - **Space**: O(n), because of the string conversion.

  **Pros**: Simple and easy to implement.
  **Cons**: Uses extra space for string conversion.

  ---

  ### 2. **Reversing the Number (Mathematical Approach)**
  You can reverse the number mathematically without converting it to a string. This approach involves extracting digits and rebuilding the reversed number.

  #### Steps:
  1. Initialize a variable `reversed_num` to 0.
  2. Extract the last digit of the original number and append it to `reversed_num`.
  3. Remove the last digit from the original number.
  4. Repeat until all digits are processed.
  5. Compare the original number with `reversed_num`.

  #### Code:
  ```python
  def is_palindrome(num):
      if num < 0:
          return False  # Negative numbers are not palindromes

      original = num
      reversed_num = 0

      while num > 0:
          last_digit = num % 10
          reversed_num = reversed_num * 10 + last_digit
          num //= 10

      return original == reversed_num
  ```

  #### Complexity:
  - **Time**: O(n), where `n` is the number of digits in the number.
  - **Space**: O(1), since only a few variables are used.

  **Pros**: Efficient and does not use extra space.
  **Cons**: More complex than the string conversion approach.

  ---

  ### 3. **Two-pointer Approach (String Method)**
  Similar to the string conversion approach but without fully reversing the string. Instead, use two pointers to compare characters from the start and end.

  #### Steps:
  1. Convert the number to a string.
  2. Use two pointers, one starting from the beginning and the other from the end.
  3. Compare the characters at the two pointers.
  4. If all characters match, return `True`, otherwise return `False`.

  #### Code:
  ```python
  def is_palindrome(num):
      num_str = str(num)
      left, right = 0, len(num_str) - 1

      while left < right:
          if num_str[left] != num_str[right]:
              return False
          left += 1
          right -= 1

      return True
  ```

  #### Complexity:
  - **Time**: O(n), where `n` is the number of digits in the number.
  - **Space**: O(n), because of the string conversion.

  **Pros**: Simple and avoids reversing the whole string.
  **Cons**: Still uses extra space for string conversion.

  ---

  ### 4. **Half-Reverse Approach (Mathematical and Efficient)**
  This is an optimized version of the reversing method, where instead of reversing the entire number, you only reverse half of the digits. This is more efficient when the number of digits is large.

  #### Steps:
  1. Handle negative numbers immediately (they cannot be palindromes).
  2. Reverse half of the number by continually dividing the number by 10 and constructing the reversed part.
  3. Stop when the reversed part is greater than or equal to the remaining part of the number.
  4. If the reversed part is equal to the remaining part, or if ignoring the last digit (for odd-digit numbers) gives equality, the number is a palindrome.

  #### Code:
  ```python
  def is_palindrome(num):
      if num < 0 or (num % 10 == 0 and num != 0):
          return False  # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes

      reversed_half = 0
      while num > reversed_half:
          reversed_half = reversed_half * 10 + num % 10
          num //= 10

      return num == reversed_half or num == reversed_half // 10
  ```

  #### Complexity:
  - **Time**: O(n), where `n` is half the number of digits in the number.
  - **Space**: O(1), as it only uses a few variables.

  **Pros**: Very efficient, especially for large numbers.
  **Cons**: Slightly harder to understand and implement.

  ---

  ### 5. **Recursive Approach**
  This approach uses recursion to compare the first and last digits of the number repeatedly. This method is less efficient but showcases recursion as a technique.

  #### Steps:
  1. Define a helper function to find the size of the number (number of digits).
  2. Recursively compare the first and last digits by removing them at each step.
  3. Continue until all digits are processed.

  #### Code:
  ```python
  def is_palindrome(num):
      def helper(num, divisor):
          if num == 0:
              return True

          first_digit = num // divisor
          last_digit = num % 10

          if first_digit != last_digit:
              return False

          # Remove the first and last digits
          num = (num % divisor) // 10
          divisor //= 100

          return helper(num, divisor)

      if num < 0:
          return False

      divisor = 1
      while num // divisor >= 10:
          divisor *= 10

      return helper(num, divisor)
  ```

  #### Complexity:
  - **Time**: O(n), where `n` is the number of digits in the number.
  - **Space**: O(n) due to recursion depth.

  **Pros**: Good for learning recursion.
  **Cons**: Inefficient and takes extra space for the recursive call stack.

  ---

  ### Summary of Approaches:

  1. **String Conversion**: Simple but uses extra space.
  2. **Reversing the Number (Mathematical)**: Efficient with no extra space.
  3. **Two-pointer (String)**: Avoids reversing the string, but still uses extra space.
  4. **Half-Reverse (Optimized)**: Best for large numbers with O(1) space.
  5. **Recursive Approach**: Showcases recursion but is less efficient.

  For practical use, the **Half-Reverse Approach** (Method 4) is typically the most efficient in terms of time and space, especially for very large numbers. However, for simplicity, **String Conversion** (Method 1) is also widely used in interview settings due to its clarity.



  Here are various approaches to check whether a number is a palindrome or not:

  ### 1. **Reversing the Number (Simple Approach)**
  This approach involves reversing the number and comparing the reversed number with the original.

  #### Steps:
  1. Convert the number to a string.
  2. Reverse the string.
  3. Compare the reversed string with the original string.

  #### Code:
  ```python
  def is_palindrome_number(n):
      return str(n) == str(n)[::-1]
  ```

  #### Complexity:
  - **Time**: O(d), where `d` is the number of digits in the number.
  - **Space**: O(d) for the string representation of the number.

  **Pros**: Simple to implement.
  **Cons**: Uses additional space for the string conversion.

  ---

  ### 2. **Reversing Half of the Number (Without String Conversion)**
  This approach avoids converting the number to a string. Instead, it reverses half of the number and compares it with the other half.

  #### Steps:
  1. Handle negative numbers and numbers with trailing zeros.
  2. Reverse half of the digits.
  3. Compare the reversed half with the first half of the original number.

  #### Code:
  ```python
  def is_palindrome_number(n):
      if n < 0 or (n % 10 == 0 and n != 0):
          return False

      reversed_half = 0
      while n > reversed_half:
          reversed_half = reversed_half * 10 + n % 10
          n //= 10

      return n == reversed_half or n == reversed_half // 10
  ```

  #### Complexity:
  - **Time**: O(d), where `d` is the number of digits in the number.
  - **Space**: O(1), no additional space is required.

  **Pros**: Efficient and avoids string conversion.
  **Cons**: A bit more complex to implement.

  ---

  ### 3. **Recursive Approach**
  A recursive approach can be used to check if the number is a palindrome, by comparing the first and last digits of the number recursively.

  #### Steps:
  1. Define a helper function that compares the first and last digits.
  2. Recursively strip off the first and last digits and continue comparing.

  #### Code:
  ```python
  def is_palindrome_number(n):
      def helper(n, divisor):
          if n == 0:
              return True
          first_digit = n // divisor
          last_digit = n % 10
          if first_digit != last_digit:
              return False
          # Remove first and last digits
          n = (n % divisor) // 10
          return helper(n, divisor // 100)

      if n < 0:
          return False

      divisor = 1
      while n // divisor >= 10:
          divisor *= 10

      return helper(n, divisor)
  ```

  #### Complexity:
  - **Time**: O(d), where `d` is the number of digits in the number.
  - **Space**: O(d) due to recursion depth.

  **Pros**: Provides a recursive solution.
  **Cons**: Recursion may lead to stack overflow for large numbers.

  ---

  ### 4. **Converting to String and Comparing Digit by Digit**
  Another simple approach is converting the number to a string and comparing digits from the start and the end.

  #### Steps:
  1. Convert the number to a string.
  2. Use two pointers to compare digits from the start and the end.

  #### Code:
  ```python
  def is_palindrome_number(n):
      s = str(n)
      left, right = 0, len(s) - 1

      while left < right:
          if s[left] != s[right]:
              return False
          left += 1
          right -= 1

      return True
  ```

  #### Complexity:
  - **Time**: O(d), where `d` is the number of digits in the number.
  - **Space**: O(d) for the string representation of the number.

  **Pros**: Simple and easy to understand.
  **Cons**: Extra space used for the string.

  ---

  ### 5. **Mathematical Approach (Digit-by-Digit Comparison)**
  This method extracts the digits from both ends of the number and compares them without converting to a string.

  #### Steps:
  1. Calculate the number of digits in the number.
  2. Extract the first and last digits and compare them.
  3. Continue comparing until all digits are checked.

  #### Code:
  ```python
  def is_palindrome_number(n):
      if n < 0:
          return False

      num_digits = len(str(n))
      divisor = 10 ** (num_digits - 1)

      while n:
          first_digit = n // divisor
          last_digit = n % 10
          if first_digit != last_digit:
              return False
          # Remove the first and last digits
          n = (n % divisor) // 10
          divisor //= 100

      return True
  ```

  #### Complexity:
  - **Time**: O(d), where `d` is the number of digits in the number.
  - **Space**: O(1).

  **Pros**: No extra space for string conversion.
  **Cons**: More involved to implement compared to the string-based methods.

  ---

  ### 6. **Handling Edge Cases**
  It's important to handle some specific cases:
  - **Negative Numbers**: By definition, negative numbers cannot be palindromes.
  - **Numbers Ending with Zero**: A number with trailing zeros (except 0 itself) cannot be a palindrome because the number would need to start with a zero.

  ---

  ### Summary of Approaches:
  1. **Reversing the Number**: Easy to implement but uses string conversion.
  2. **Reversing Half of the Number**: Efficient with O(1) space, no string conversion.
  3. **Recursive Approach**: Elegant but could lead to stack overflow for large numbers.
  4. **String Comparison with Two Pointers**: Simple, uses string but is memory-intensive.
  5. **Mathematical Digit Comparison**: Avoids string conversion, uses no extra space.

  For large numbers and performance-sensitive tasks, the mathematical or "reversing half" approach is recommended due to its space efficiency.



```python

palindrome_number_test_cases = [
    # Case 1: Positive palindrome
    {
        "name": "Positive Palindrome",
        "input": 121,
        "expected": True,
    },
    # Case 2: Negative number (not a palindrome)
    {
        "name": "Negative Number",
        "input": -121,
        "expected": False,
    },
    # Case 3: Positive non-palindrome
    {
        "name": "Positive Non-Palindrome",
        "input": 123,
        "expected": False,
    },
    # Case 4: Single digit (always a palindrome)
    {
        "name": "Single Digit",
        "input": 7,
        "expected": True,
    },
    # Case 5: Zero (is a palindrome)
    {
        "name": "Zero",
        "input": 0,
        "expected": True,
    },
    # Case 6: Large palindrome
    {
        "name": "Large Palindrome",
        "input": 123456789987654321,
        "expected": True,
    },
    # Case 7: Large non-palindrome
    {
        "name": "Large Non-Palindrome",
        "input": 123456789987654320,
        "expected": False,
    },
    # Case 8: Palindrome with trailing zeros (not a palindrome)
    {
        "name": "Number with Trailing Zeros",
        "input": 1000,
        "expected": False,
    },
    # Case 9: Long palindrome
    {
        "name": "Long Palindrome",
        "input": 1234567890987654321,
        "expected": True,
    },
    # Case 10: Long non-palindrome
    {
        "name": "Long Non-Palindrome",
        "input": 1234567890987654320,
        "expected": False,
    },  # Non-palindrome
    # Case 11: Large even-length palindrome
    {
        "name": "Large Even-Length Palindrome",
        "input": 12344321,
        "expected": True,
    },
    # Case 12: Large even-length non-palindrome
    {
        "name": "Large Even-Length Non-Palindrome",
        "input": 12344320,
        "expected": False,
    },
    # Case 13: Very large palindrome (with many digits)
    # {
    #     "name": "Very Large Palindrome",
    #     "input": int("1" + "0" * 1000000 + "1"),
    #     "expected": True,
    # },
    # Case 14: Very large non-palindrome
    # {
    #     "name": "Very Large Non-Palindrome",
    #     "input": int("1" + "0" * 1000000 + "2"),
    #     "expected": False,
    # },
    # Case 15: Edge case of maximum integer value in Python
    {
        "name": "Max Integer",
        "input": 2147483647,
        "expected": False,
    },  # Not a palindrome
]


def test_palindrome_number(func):
    print(f"Testing function: {func.__name__}")

    for i, test_case in enumerate(
        palindrome_number_test_cases, 1
    ):
        input_data = test_case["input"]
        expected_result = test_case["expected"]
        case_name = test_case["name"]

        result = func(input_data)

        # Check if the returned result matches the expected result
        assert (
            result == expected_result
        ), f"Test case ({case_name}) failed: expected {expected_result}, got {result}"

    print("All test cases passed!")



def is_palindrome1(x:int)->bool:
    return str(x) == str(x)[::-1]


def is_palindrome2(x:int)->bool:
    reversed_x= 0
    temp_x = x

    while temp_x > 0:
        reversed_x = reversed_x * 10 + temp_x % 10
        temp_x //= 10

    return x == reversed_x


def is_palindrome3(x:int)->bool:
    if x < 0:
        return False

    digits: list[int] = []
    while x > 0:
        digits.append(x % 10)
        x //= 10

    left, right = 0, len(digits) - 1

    while(left < right):
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1

    return True

def is_palindrome4(x:int)->bool:
    if x < 0:
        return False

    num_of_digits = 0

    temp = x
    while temp > 0:
        num_of_digits += 1
        temp //= 10

    right_ptr = num_of_digits - 1

    for left_ptr in range(num_of_digits // 2):
        left_digit = (x // 10 ** right_ptr) % 10
        right_digit = (x // 10 ** left_ptr) % 10

        if left_digit != right_digit:
            return False

        right_ptr -= 1
    return True



test_palindrome_number(is_palindrome1)

```