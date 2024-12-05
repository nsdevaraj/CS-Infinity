

Here are 20 famous and relatively easy LeetCode questions with crisp Python solutions:

---

### 1. **Two Sum**

```python
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
```

---

### 2. **Reverse Integer**

```python
def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = int(str(x)[::-1])
    return rev * sign if -(2**31) <= rev <= 2**31 - 1 else 0
```

---

### 3. **Palindrome Number**

```python
def isPalindrome(x):
    return str(x) == str(x)[::-1]
```

---

### 4. **Merge Two Sorted Lists**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
```

---

### 5. **Best Time to Buy and Sell Stock**

```python
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
```

---

### 6. **Valid Parentheses**

```python
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
```

---

### 7. **Remove Duplicates from Sorted Array**

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1
```

---

### 8. **Climbing Stairs**

```python
def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

---

### 9. **Maximum Subarray**

```python
def maxSubArray(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

---

### 10. **Binary Search**

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

### 11. **Find Peak Element**

```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

---

### 12. **Search Insert Position**

```python
def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

---

### 13. **Longest Common Prefix**

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

---

### 14. **Plus One**

```python
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```

---

### 15. **Single Number**

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

---

### 16. **Fizz Buzz**

```python
def fizzBuzz(n):
    return ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n + 1)]
```

---

### 17. **Intersection of Two Arrays II**

```python
from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    result = []
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result
```

---

### 18. **Majority Element**

```python
def majorityElement(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
```

---

### 19. **Move Zeroes**

```python
def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
```

---

### 20. **Power of Three**

```python
def isPowerOfThree(n):
    return n > 0 and 1162261467 % n == 0  # 1162261467 is 3^19
```

---

These solutions are concise and widely appreciated for their simplicity.

