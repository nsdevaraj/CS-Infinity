
[LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/)

### Problem Statement

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at index `i`. You cannot use division in your solution.

### Examples

1. **Input**: `[1, 2, 3, 4, 5]`  
   **Output**: `[120, 60, 40, 30, 24]`  
   **Explanation**:  
   - For index 0: \(2 \times 3 \times 4 \times 5 = 120\)  
   - For index 1: \(1 \times 3 \times 4 \times 5 = 60\)  
   - For index 2: \(1 \times 2 \times 4 \times 5 = 40\)  
   - For index 3: \(1 \times 2 \times 3 \times 5 = 30\)  
   - For index 4: \(1 \times 2 \times 3 \times 4 = 24\)  

2. **Input**: `[2, 3, 4]`  
   **Output**: `[12, 8, 6]`  
   **Explanation**:  
   - For index 0: \(3 \times 4 = 12\)  
   - For index 1: \(2 \times 4 = 8\)  
   - For index 2: \(2 \times 3 = 6\)  

3. **Input**: `[5, 1, 2, 3]`  
   **Output**: `[6, 30, 15, 10]`  
   **Explanation**:  
   - For index 0: \(1 \times 2 \times 3 = 6\)  
   - For index 1: \(5 \times 2 \times 3 = 30\)  
   - For index 2: \(5 \times 1 \times 3 = 15\)  
   - For index 3: \(5 \times 1 \times 2 = 10\)  

### Constraints
- The input array will have at least two elements.
- The input array can contain both positive and negative integers.



## Soln


### Normal nested loopings

```python

def product_except_self_1(ary:List[int])->List[int]:
    prod_ary_except_self = []
    ary_len = len(ary) if ary else 0

    # return [] when just single element present
    if(ary_len < 2):
        return prod_ary_except_self

    ary_len = len(ary)
    for i in range(ary_len):
        product = 1
        for j in range(ary_len):
            if(i != j):
                product *= ary[j]
        prod_ary_except_self.append(product)

    return prod_ary_except_self

```


```python

def product_except_self_2(ary:List[int])-> List[int]:
    ary_len = len(ary)
    product_ary = [1]*(ary_len) if ary_len>1 else []

    for i in range(ary_len):
        for j in range(ary_len):
            if( i != j):
                product_ary[j] = product_ary[j] * ary[i]
    return product_ary


```



### optimized two times loopings


```python

# O(n) time
def product_except_self_4(nums: List[int]) -> List[int]:
    length = len(nums)
    if length < 2:
        return []

    # Initialize the output array
    output = [1] * length

    # Calculate the products of elements to the left of each index
    # we don't need to maintain left product, as we directly take from output array
    for i in range(1, length):
        output[i] = output[i - 1] * nums[i - 1]

    # Calculate the products of elements to the right of each index
    right_product = 1
    for i in range(length - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output


```



to try: with division

```python

# To do - do with divion operator
def product_except_self_x(ary:List[int])-> List[int]:
    # handle zero things differently
    def product_of_array(arr):
        product = 1
        for num in arr:
            if(num != 0):
                product *= num
        return product

    ary_product_without_zero = product_of_array(ary)

    return [ary_product_without_zero//x for x in ary ]


```
## References

watched. {

https://www.youtube.com/watch?v=bNvIQI2wAjk


}

## More


### Tests

```python 

# Test cases for the Product of Array Except Self problem
test_cases = [
    {
        "name": "Basic Case",
        "input": [1, 2, 3, 4, 5],
        "expected": [120, 60, 40, 30, 24],
        # Each element is the product of all other elements in the array.
    },
    {
        "name": "Single Zero in Array",
        "input": [1, 2, 0, 4],
        "expected": [0, 0, 8, 0],
        # The product is zero for all indices except the one where the zero is.
    },
    {
        "name": "Two Zeros in Array",
        "input": [0, 0, 1, 2],
        "expected": [0, 0, 0, 0],
        # All products will be zero since there are two zeros.
    },
    {
        "name": "Negative Numbers",
        "input": [-1, 2, -3, 4],
        "expected": [-24, 12, -8, 6],
        # The products will consider the negative signs appropriately.
    },
    {
        "name": "All Ones",
        "input": [1, 1, 1, 1],
        "expected": [1, 1, 1, 1],
        # The product of any array of ones remains one.
    },
    {
        "name": "Large Numbers",
        "input": [100000, 200000, 300000],
        "expected": [60000000000, 30000000000, 20000000000],
        # Tests the function with large values.
    },
    {
        "name": "Single Element",
        "input": [42],
        "expected": [], # some prefer [1]
        # Edge case: single element should ideally return an empty array since no products can be formed.
    },
    {
        "name": "Empty Array",
        "input": [],
        "expected": [],
        # Edge case: empty input should return an empty output.
    },
    {
        "name": "Two Elements",
        "input": [4, 5],
        "expected": [5, 4],
        # Simple case with two elements should correctly swap the products.
    },
    {
        "name": "Larger Array",
        "input": [1, 2, 3, 4, 5, 6],
        "expected": [720, 360, 240, 180, 144, 120],
        # Tests a larger array to ensure correct handling of size.
    },
]

def run_test_for_func(product_except_self_func):
    print(f"Testing function: {product_except_self_func.__name__}")
    for case in test_cases:
        input_data = case["input"]
        expected = case["expected"]
        result = product_except_self_func(input_data)
        assert result == expected, f"Test case '{case['name']}' failed: expected {expected}, got {result}"
    print("All test cases completed!")



```




