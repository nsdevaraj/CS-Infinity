


[max prod subarray @takeUforward](https://www.youtube.com/watch?v=hnswaLJvr6g)



subArray - contiguous array elements 
array itself will also consider as its subarray.. 



The **Maximum Product Subarray** problem is a common problem on platforms like LeetCode (Problem [152](https://leetcode.com/problems/maximum-product-subarray/)) and involves finding the maximum product of a contiguous subarray within a given integer array. Here’s a detailed breakdown of the approaches to solve this problem effectively.

---

### Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array (containing at least one number) which has the largest product. 

### Examples
#### Example 1
**Input:** `nums = [2, 3, -2, 4]`  
**Output:** `6`  
**Explanation:** The subarray `[2, 3]` has the largest product, `6`.

#### Example 2
**Input:** `nums = [-2, 0, -1]`  
**Output:** `0`  
**Explanation:** The result cannot be a product of any other subarray as zero resets the product.

### Key Observations
- A product of a subarray containing negative numbers can still result in the maximum product, depending on the position and count of the negatives.
- Multiplying by zero will reset the product, as a product of zero with any number results in zero.
- To account for both positive and negative impacts, track both the maximum and minimum products at each step.

---

### Approach 1: Dynamic Programming with Two Variables (`max_prod` and `min_prod`)
This approach uses two main variables at each step:
1. **`max_prod`**: Tracks the maximum product up to the current index.
2. **`min_prod`**: Tracks the minimum product up to the current index (useful when encountering a negative number).

**Algorithm:**
1. Initialize `max_prod` and `min_prod` to the first element, `nums[0]`, and `result` to `nums[0]`.
2. Iterate through `nums` starting from the second element.
3. For each element:
   - If the element is negative, swap `max_prod` and `min_prod` (this allows handling negative numbers correctly).
   - Update `max_prod` as the maximum of the current number and `max_prod * current number`.
   - Update `min_prod` as the minimum of the current number and `min_prod * current number`.
   - Update `result` to hold the maximum of `result` and `max_prod`.
4. Return `result` as the maximum product of any subarray.

#### Code Implementation
```python
from typing import List

def max_product(nums: List[int]) -> int:
    if not nums:
        return 0
    
    # Initialize max and min product to the first element
    max_prod = min_prod = result = nums[0]

    # Traverse the array
    for num in nums[1:]:
        # If current number is negative, swap max and min
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        # Calculate maximum product ending at the current position
        max_prod = max(num, max_prod * num)
        # Calculate minimum product ending at the current position
        min_prod = min(num, min_prod * num)
        
        # Update the result to be the maximum product found so far
        result = max(result, max_prod)
    
    return result
```


in simple:
all +ve nums => take all and get max product
even -ve nums => take all and get max product
odd -ve nums => split array in that -ve num ... either side of sub array which has even -ve num will be answer
0 - since its 0, we have to consider it as separate sub array, since including in other sub array makes them inpotentional for product.. 


```python
# Time - O(n)
def maxProduct2(numbers:List[int])->int:

    max_prod = -999999999

    numbers_len = len(numbers)
    left_prod = 1
    right_prod = 1

    for i in range(numbers_len):

        # if 0 encountered, do reset
        if(left_prod == 0):
            left_prod = 1
        if(right_prod == 0):
            right_prod = 1

        left = numbers[i]
        right = numbers[numbers_len - i - 1]

        left_prod *= left
        right_prod *= right

        max_prod = max(max_prod, max(left_prod, right_prod))

    return max_prod
```




### Explanation of Code
- The algorithm uses `max_prod` to keep track of the maximum product that can be obtained ending at each position, and `min_prod` to keep track of the minimum product at each position (to handle cases involving negative numbers).
- If `num` is negative, swapping `max_prod` and `min_prod` accounts for the sign change, thus allowing `max_prod` to capture the new maximum product.

### Complexity Analysis
- **Time Complexity:** \(O(n)\), since we only iterate through the list once.
- **Space Complexity:** \(O(1)\), only constant space is used for the variables.

---

### Approach 2: Brute Force (for Reference Only)
In the brute force approach, you calculate the product of every possible subarray and keep track of the maximum product encountered. This approach has a high time complexity and is generally inefficient for large arrays.

#### Code Implementation (Brute Force)
```python
def max_product_brute_force(nums: List[int]) -> int:
    max_prod = float('-inf')
    
    for i in range(len(nums)):
        current_prod = 1
        for j in range(i, len(nums)):
            current_prod *= nums[j]
            max_prod = max(max_prod, current_prod)
    
    return max_prod
```


```python
# time - O(n^3) since 2 iterations and 1 prod finding of sub_array
def maxProduct1(numbers:List[int])->int:
    # max_product = float('-inf')
    max_product = -999999999
    numbers_len = len(numbers)
    for i in range(numbers_len):
        for j in range(i, numbers_len):
            sub_ary = numbers[i:j+1]
            sub_ary_product = math.prod(sub_ary)
            if(sub_ary_product > max_product):
                max_product = sub_ary_product

    return max_product

```


### Complexity Analysis of Brute Force
- **Time Complexity:** \(O(n^2)\), as there are nested loops to calculate all subarray products.
- **Space Complexity:** \(O(1)\), only uses constant extra space.

---

### Summary Table

| Approach                     | Time Complexity | Space Complexity | Explanation                                       |
|------------------------------|-----------------|------------------|---------------------------------------------------|
| Dynamic Programming (Optimal)| \(O(n)\)        | \(O(1)\)         | Tracks max/min product at each index, swapping on negative values to handle signs correctly |
| Brute Force                  | \(O(n^2)\)      | \(O(1)\)         | Calculates the product of every subarray          |

### Test Cases
You can test the function with a variety of cases to ensure it handles different scenarios:

```python
def test_max_product():
    test_cases = [
        {"input": [2, 3, -2, 4], "expected": 6},
        {"input": [-2, 0, -1], "expected": 0},
        {"input": [-2, 3, -4], "expected": 24},
        {"input": [0, 2, 0, 4], "expected": 4},
        {"input": [-1, -3, -10, 0, 60], "expected": 60},
        {"input": [-2, -3, 0, -2, -40], "expected": 80},
        {"input": [6, -3, -10, 0, 2], "expected": 180},
    ]

    for i, test in enumerate(test_cases, 1):
        result = max_product(test["input"])
        assert result == test["expected"], f"Test case {i} failed: Expected {test['expected']}, got {result}"
    print("All test cases passed!")

test_max_product()
```

Each test case here is designed to capture various edge cases:
- Sequences with negative numbers.
- Sequences with zeros that reset the product.
- Cases where the largest product involves multiple negative numbers.



---

to check {

Kadane's approach for this problem..  O(n)

https://www.interviewbit.com/blog/maximum-product-subarray-problem/

https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1

https://algo.monster/liteproblems/152

https://www.geeksforgeeks.org/maximum-product-subarray/


}

Leet code soln:

Runtime: 0ms

python

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod *= num
        if prod > 0:
            return prod
        best = prod
        prod = 1
        for num in nums:
            if num == 0:
                prod = 1
            else:
                prod *= num
                best = max(best, prod)
        prod = 1
        for num in nums[::-1]:
            if num == 0:
                prod = 1
            else:
                prod *= num
                best = max(best, prod)
        return best
```


Memory: 16.3mb

python

```python
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res=max(nums)
        current_max,current_min=1,1
        for num in nums:

            tmp=current_max*num
            current_max=max(num*current_max,num*current_min, num)
            current_min = min(tmp, num * current_min, num)
            res=max(res,current_max)
        return res
```


