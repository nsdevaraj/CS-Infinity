

[[Missing Number ( missing natural num )]]
[[Largest or Maximum Sub Array]]
[[LinkedList Cycle]]
[[Merge two sorted list or array]]


[[Longest Increasing SubSequence]]




### **5. Binary Search**

**Problem**: Find the index of a target element in a sorted array.

**Code**:

```python
def binary_search(nums, target):
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

# Example
nums = [1, 2, 3, 4, 5, 6]
target = 4
print(binary_search(nums, target))  # Output: 3
```

---




---

### **2. Search in a Rotated Sorted Array**

**Problem**: Search for a target in a rotated sorted array.

**Code**:

```python
def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Example
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated_array(nums, target))  # Output: 4
```

---

### **3. Kth Largest Element in an Array**

**Problem**: Find the kth largest element in an array.

**Code**:

```python
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kth_largest(nums, k))  # Output: 5
```

---

### **4. Maximum Product Subarray**

**Problem**: Find the maximum product of a contiguous subarray.

**Code**:

```python
def max_product(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)
    return result

# Example
nums = [2, 3, -2, 4]
print(max_product(nums))  # Output: 6
```

---

### **5. Trapping Rainwater**

**Problem**: Calculate the total water that can be trapped between bars.

**Code**:

```python
def trap_rainwater(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# Example
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_rainwater(height))  # Output: 6
```

---

### **6. Subarray Sum Equals K**

**Problem**: Count the number of subarrays that sum to `k`.

**Code**:

```python
def subarray_sum(nums, k):
    count = prefix_sum = 0
    prefix_sums = {0: 1}
    for num in nums:
        prefix_sum += num
        count += prefix_sums.get(prefix_sum - k, 0)
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
    return count

# Example
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # Output: 2
```

---

### **7. Word Break**

**Problem**: Check if a string can be segmented into space-separated words from a dictionary.

**Code**:

```python
def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for word in word_dict:
            if dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
    return dp[-1]

# Example
s = "leetcode"
word_dict = ["leet", "code"]
print(word_break(s, word_dict))  # Output: True
```

---

Let me know if you'd like more problems or deeper explanations!


