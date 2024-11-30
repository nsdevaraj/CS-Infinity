

[Plus one problem - Inside code](https://youtu.be/c_SIvhkpBtU?si=dnSyG1iQkfc91Tvd)


## Problem: **Plus One**

### Problem Statement:
You are given a **non-empty array** of integers representing the digits of a **positive integer**. Your task is to add 1 to the number and return the updated array of digits.

You are **not allowed** to convert the array into an integer, add 1, and then convert it back to an array. The operation must be done **in place** on the array itself.

### Example 1:
```
Input: [2, 1, 6]
Output: [2, 1, 7]
Explanation: The number represented is 216. After adding 1, it becomes 217.
```

### Example 2:
```
Input: [9, 9, 9]
Output: [1, 0, 0, 0]
Explanation: The number represented is 999. After adding 1, it becomes 1000.
```

### Constraints:
- The input array represents a positive number without any leading zeroes.
- Each element in the array is a **single digit** (0-9).

---

## Brute Force Solution

### Approach:
1. Convert the array of digits into a number.
2. Add 1 to the number.
3. Convert the number back to an array.

However, **this approach is not allowed**, as the problem explicitly states we cannot convert the array into a number and back. Instead, we need to solve this problem directly on the array.

### Brute Force Approach

The brute force approach is simple but **not allowed** according to the problem constraints. However, for learning purposes, this method converts the array of digits to an integer, adds one to it, and converts it back to an array.

### Approach:
1. **Convert the array of digits into an integer** by iterating through the array.
2. **Add 1** to the integer.
3. **Convert the result back into an array of digits**.

### Example Walkthrough:

For input `digits = [2, 1, 6]`:
1. Convert `[2, 1, 6]` to the integer `216`.
2. Add 1 to `216` → `217`.
3. Convert `217` back to the array `[2, 1, 7]`.

### Python Code:
```python
from typing import List

def plusOneBruteForce(digits: List[int]) -> List[int]:
    """Brute force solution by converting the array to an integer, adding one, then converting back."""
    
    # Convert the array to an integer
    num = 0
    for digit in digits:
        num = num * 10 + digit  # Build the number digit by digit
    
    # Add one to the integer
    num += 1
    
    # Convert the integer back to an array of digits
    return [int(d) for d in str(num)]

# Example Usage
print(plusOneBruteForce([2, 1, 6]))  # Output: [2, 1, 7]
print(plusOneBruteForce([9, 9, 9]))  # Output: [1, 0, 0, 0]
```

### Time Complexity:
- **Time Complexity**: $O(n)$, where $n$ is the number of digits.
  - Converting the list of digits to an integer takes $O(n)$, and converting it back to an array also takes $O(n)$.

- **Space Complexity**: $O(n)$ because we create a new string and array for the result.

While this solution works, **it violates the problem's constraint** of not converting the digits to a number directly.



---

## Optimized Solution (In-place)

### Approach:

We need to handle the **rightmost digit first** (the last digit in the array):
1. Start from the last digit. Add 1 to it.
2. If the digit becomes 10, set it to 0 and **carry over** 1 to the next digit.
3. Repeat this process until there is no more carry, or you reach the first digit.
4. If all digits were 9, you will need to **insert** a 1 at the beginning of the array.

### Example Walkthrough:
Let's take the example `digits = [9, 9, 9]`:
1. Start with the rightmost 9: it becomes 0, carry 1.
2. Move to the next 9: it becomes 0, carry 1.
3. Finally, the last 9 becomes 0, carry 1.
4. Since all digits are 0 now, we need to insert 1 at the front, resulting in `[1, 0, 0, 0]`.

### Python Code:
```python
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    """Add one to the number represented by digits in the array."""
    i = len(digits) - 1  # Start from the last index (rightmost digit)
    
    # Loop over the digits starting from the last one
    while i >= 0:
        digits[i] += 1  # Add 1 to the current digit
        if digits[i] == 10:
            digits[i] = 0  # If digit becomes 10, set it to 0 and carry over 1
            i -= 1  # Move to the next left digit
        else:
            break  # No carry, we're done
    
    # If all digits were 9, we would need to insert 1 at the beginning
    if i == -1:
        digits.insert(0, 1)
    
    return digits

# Example Usage
print(plusOne([2, 1, 6]))  # Output: [2, 1, 7]
print(plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
```

### Explanation of Code:
1. **Initialization**: 
   - We start from the last index of the array (`i = len(digits) - 1`).
   
2. **Loop**: 
   - Add 1 to the current digit.
   - If the result is 10, set the current digit to 0 and move to the next left digit.
   - If the result is less than 10, break the loop (no carry needed).
   
3. **Edge Case**: 
   - If all digits were 9 (like `[9, 9, 9]`), then after the loop, the array will be all zeroes (`[0, 0, 0]`), and we will insert `1` at the front.

4. **Return**: 
   - Return the updated array of digits.

### Time Complexity:
- **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input array.
  - We loop over each digit at most once.
  
- **Space Complexity:** $O(1)$, constant space.
  - No extra space is used except for variables like `i`. The list is modified in place.

---

## Final Thoughts:
This problem demonstrates how you can work directly with arrays and manage carry-over operations for simple addition without converting the array to a number. It's a great exercise in practicing in-place algorithms.

This solution efficiently handles edge cases like multiple trailing nines, ensuring the algorithm has linear time complexity even for large arrays.



