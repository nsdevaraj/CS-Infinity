

## Square Root Calculation

**Description:**
Given a non-negative integer `A`, compute and return the integer part of the square root of `A`. If `A` is not a perfect square, return the largest integer less than the square root of `A` (i.e., the floor of the square root).

You are not allowed to use any built-in square root functions or exponentiation operators from the standard library.

**Input Format:**
- A single integer `A` where `0 ≤ A ≤ 2^31 - 1`.

**Output Format:**
- Return an integer representing the floor value of the square root of `A`.

**Examples:**

1. **Input:**  
   `A = 11`  
   **Output:**  
   `3`  
   **Explanation:** The square root of 11 is approximately 3.316, so the floor value is 3.

2. **Input:**  
   `A = 9`  
   **Output:**  
   `3`  
   **Explanation:** The square root of 9 is 3, which is a perfect square.

3. **Input:**  
   `A = 0`  
   **Output:**  
   `0`  
   **Explanation:** The square root of 0 is 0.

**Constraints:**
- Implement the solution with a time complexity of `O(log(A))`.


**Notes:**
- Ensure the returned integer is non-negative.
- Avoid using built-in mathematical functions related to square roots or exponentiation.


## Soln

```python
# Time complexity - O(n)
def square_root3(num:int)->int:
    nearest_num = 0
    for i in range(1,num+1):
        sq_i = i*i
        if(sq_i == num):
            nearest_num = i
            break
        elif(sq_i > num):
            nearest_num = i-1
            break
    return int(nearest_num)
```



```python

def square_root4(A: int) -> int:
    print("A", A)
    if A < 2:
        return A  # 0 and 1 are their own square roots

    left, right = 2, A // 2  # Start searching between 2 and A/2

    while left <= right:
        # finding mid this way to avoid overflow in some prog lang..
        mid = left + (right - left) // 2
        square = mid * mid

        if square == A:
            return mid
        elif square < A:
            left = mid + 1
        else:
            right = mid - 1

    return right  # The floor of sqrt(A) when not a perfect square


```



![[square_root.py]]



{

different apporaches - chatGPT

Certainly! Here are several approaches to compute the integer part of the square root of a non-negative integer \( A \):

### 1. **Binary Search Approach**

#### Explanation:
Use binary search to find the integer square root. The idea is to maintain a search range from 0 to \( A \) (or \( A/2 \) for optimization). For each midpoint, calculate the square and adjust the search range based on whether the square is less than, equal to, or greater than \( A \).

#### Complexity:
- **Time:** O(log A)
- **Space:** O(1)

#### Implementation:
```python
def square_root(A: int) -> int:
    if A < 2:
        return A
    
    left, right = 2, A // 2
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == A:
            return mid
        elif square < A:
            left = mid + 1
        else:
            right = mid - 1
            
    return right  # The floor of sqrt(A)
```

---

### 2. **Newton's Method (Newton-Raphson)**

#### Explanation:
This iterative method starts with an initial guess and refines it using the formula \( x_{n+1} = \frac{1}{2} \left( x_n + \frac{A}{x_n} \right) \). The iterations continue until the guess stabilizes (i.e., two successive guesses are the same).

#### Complexity:
- **Time:** O(log A) in practice
- **Space:** O(1)

#### Implementation:
```python
def square_root(A: int) -> int:
    if A < 2:
        return A
    
    x = A
    while True:
        y = (x + A // x) // 2
        if y >= x:  # When guesses stabilize
            return x
        x = y
```

---

### 3. **Brute Force Approach**

#### Explanation:
This method involves iterating from 0 up to \( A \) and checking each integer to see if its square equals \( A \). It is simple but inefficient for large values of \( A \).

#### Complexity:
- **Time:** O(A)
- **Space:** O(1)

#### Implementation:
```python
def square_root(A: int) -> int:
    if A < 2:
        return A
    
    for i in range(1, A + 1):
        if i * i > A:
            return i - 1
```

---

### 4. **Optimized Brute Force**

#### Explanation:
Instead of checking all numbers up to \( A \), check only up to \( A/2 \) since the square root of \( A \) cannot exceed \( A/2 \) (except for numbers less than 4). This reduces the number of iterations significantly.

#### Complexity:
- **Time:** O(A/2) → O(A)
- **Space:** O(1)

#### Implementation:
```python
def square_root(A: int) -> int:
    if A < 2:
        return A
    
    for i in range(1, A // 2 + 1):
        if i * i > A:
            return i - 1
    return A // 2  # If A is very small, this handles the case
```

---

### Summary

- **Binary Search** and **Newton's Method** are efficient and suitable for this problem, both achieving \( O(\log A) \) complexity.
- The **Brute Force** approach is straightforward but inefficient for large numbers.
- The **Optimized Brute Force** improves the naive method slightly but is still not ideal compared to binary search or Newton's method.

Choose the approach that best fits your needs based on the constraints and performance requirements! Let me know if you need further details on any of these methods.

}


{
for more:

https://leetcode.com/problems/sqrtx/

https://www.geeksforgeeks.org/square-root-of-an-integer/

https://stackoverflow.com/questions/71148575/integer-square-root-of-a-number



}







