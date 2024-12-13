

Find the median of two sorted arrays.

in most cases - if need bigO log, then need binary search...

median - middle value when its sorted


To find the median of the set of numbers \(1, 2, 2, 3\), follow these steps:

1. **Sort the numbers**: The numbers are already sorted: \(1, 2, 2, 3\).

2. **Determine the count**: There are 4 numbers in total (even count).

3. **Find the middle values**: Since the count is even, the median is the average of the two middle numbers. The middle numbers are the 2nd and 3rd values in the sorted list, which are both \(2\).

4. **Calculate the median**:
   \[
   \text{Median} = \frac{2 + 2}{2} = \frac{4}{2} = 2
   \]

So, the median of the numbers \(1, 2, 2, 3\) is \(2\).


To find the median of the set of numbers \(1, 2, 2, 3, 4\), follow these steps:

1. **Sort the numbers**: The numbers are already sorted: \(1, 2, 2, 3, 4\).

2. **Determine the count**: There are 5 numbers in total (odd count).

3. **Find the middle value**: Since the count is odd, the median is the middle number. The middle number is the 3rd value in the sorted list, which is \(2\).

So, the median of the numbers \(1, 2, 2, 3, 4\) is \(2\).



To find the median of the set of numbers \(10, 20\):

1. **Sort the numbers**: The numbers are already sorted: \(10, 20\).

2. **Determine the count**: There are 2 numbers in total (even count).

3. **Find the middle values**: Since the count is even, the median is the average of the two middle numbers, which are \(10\) and \(20\).

4. **Calculate the median**:
   \[
   \text{Median} = \frac{10 + 20}{2} = \frac{30}{2} = 15
   \]

So, the median of the numbers \(10\) and \(20\) is \(15\).



## Math 
### Mean
The mean is the average of a set of numbers. It is calculated by adding all the numbers together and then dividing by the count of the numbers.

**Formula**:
\[
\text{Mean} = \frac{\text{Sum of all values}}{\text{Number of values}}
\]

**Example**:
For the set of numbers: 3, 5, 7, 9
Mean = (3 + 5 + 7 + 9) / 4 = 24 / 4 = 6

### Median
The median is the middle value of a set of numbers when they are arranged in ascending order. If there is an even number of values, the median is the average of the two middle numbers.

**Steps to find median**:
1. Arrange the numbers in order.
2. If the count of numbers is odd, the median is the middle number.
3. If the count is even, the median is the average of the two middle numbers.

**Example**:
For the set of numbers: 3, 5, 7, 9
Arranged: 3, 5, 7, 9 (even count)
Median = (5 + 7) / 2 = 12 / 2 = 6

For the set: 3, 5, 7
Arranged: 3, 5, 7 (odd count)
Median = 5 (the middle number)

### Mode
The mode is the number that appears most frequently in a set of numbers. A set can have one mode, more than one mode (bimodal or multimodal), or no mode at all.

**Example**:
For the set of numbers: 3, 5, 7, 5, 9
Mode = 5 (it appears most frequently)

For the set: 1, 2, 2, 3, 3
Modes = 2 and 3 (both appear twice)

For the set: 1, 2, 3
Mode = None (no number repeats)

### Summary
- **Mean**: Average of the numbers.
- **Median**: Middle value when sorted.
- **Mode**: Most frequently occurring value.

These measures help summarize and describe a set of data in different ways.


---


### Median of Two Sorted Arrays

The **Median of Two Sorted Arrays** is a classic problem that appears frequently in coding interviews. It is also listed as **Problem 4** on LeetCode. The goal is to find the median of two sorted arrays, where the arrays may have different sizes and might not overlap.

---

### **Problem Statement**

You are given two sorted arrays `nums1` and `nums2` of size `m` and `n`, respectively. Find the median of the combined sorted array. The overall run-time complexity should be **O(log(min(m, n)))**.

#### **Examples**

**Example 1:**

```plaintext
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: The combined sorted array is [1, 2, 3]. The median is 2.0.
```

**Example 2:**

```plaintext
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: The combined sorted array is [1, 2, 3, 4]. The median is (2 + 3) / 2 = 2.5.
```

**Example 3:**

```plaintext
Input: nums1 = [0, 0], nums2 = [0, 0]
Output: 0.0
Explanation: The combined sorted array is [0, 0, 0, 0]. The median is 0.0.
```

**Example 4:**

```plaintext
Input: nums1 = [], nums2 = [1]
Output: 1.0
Explanation: The median is the only element in nums2.
```

**Example 5:**

```plaintext
Input: nums1 = [2], nums2 = []
Output: 2.0
Explanation: The median is the only element in nums1.
```

---

### **Approach**

The problem requires an efficient solution with a time complexity of **O(log(min(m, n)))**. This is achieved using a **binary search** technique.

---

### **Key Observations**

1. **Median Concept**:
    
    - If the total number of elements is odd, the median is the middle element.
    - If the total number of elements is even, the median is the average of the two middle elements.
2. **Binary Search on Shorter Array**:
    
    - Always perform the binary search on the shorter array (`nums1` or `nums2`).
    - Partition the arrays into two halves such that all elements in the left half are less than or equal to all elements in the right half.

---

### **Algorithm**

1. **Input Validation**:
    
    - If one of the arrays is empty, return the median of the non-empty array.
2. **Binary Search Setup**:
    
    - Define low (`low = 0`) and high (`high = m`) pointers for the shorter array.
3. **Partitioning**:
    
    - Find the partition index for `nums1` (`partitionX`) and derive `partitionY` for `nums2` using: partitionY=(m+n+1)2−partitionXpartitionY = \frac{(m + n + 1)}{2} - partitionX
4. **Median Calculation**:
    
    - Calculate maxLeft and minRight for both arrays:
        - `maxLeftX` and `minRightX` for `nums1`.
        - `maxLeftY` and `minRightY` for `nums2`.
    - The median is determined based on whether the total number of elements is odd or even:
        - If odd: `max(maxLeftX, maxLeftY)`
        - If even: (max⁡(maxLeftX,maxLeftY)+min⁡(minRightX,minRightY))/2(\max(maxLeftX, maxLeftY) + \min(minRightX, minRightY)) / 2
5. **Adjust Partition**:
    
    - If `maxLeftX > minRightY`, move the partition left.
    - If `maxLeftY > minRightX`, move the partition right.

---

### **Code Implementation (Python)**

```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the shorter array

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted")
```

---

### **Complexity Analysis**

|**Approach**|**Time Complexity**|**Space Complexity**|
|---|---|---|
|Binary Search|O(log(min(m, n)))|O(1)|
|Merge Both Arrays|O(m + n)|O(m + n)|

---

### **Edge Cases**

1. One or both arrays are empty.
2. Arrays have unequal sizes.
3. Overlapping or duplicate elements.

---

### **LeetCode Link**

You can practice this problem [here](https://leetcode.com/problems/median-of-two-sorted-arrays/).

----



**Problem:** Given two sorted arrays, find the median of the two sorted arrays.

```python
def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
```


----
---



### Median of Two Sorted Arrays

The **Median of Two Sorted Arrays** is a frequently encountered problem in algorithmic challenges and coding interviews. It is also listed as **Problem 4** on LeetCode. The task is to find the median of two sorted arrays while maintaining an optimal time complexity of **O(log(min(m, n)))**.

---

### **Problem Statement**

Given two sorted arrays `nums1` of size `m` and `nums2` of size `n`, return the median of the combined sorted array. If the total number of elements is even, the median is the average of the two middle elements.

#### Examples

---

**Example 1**

```plaintext
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: The merged array is [1, 2, 3]. The median is 2.0.
```

---

**Example 2**

```plaintext
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: The merged array is [1, 2, 3, 4]. The median is (2 + 3) / 2 = 2.5.
```

---

**Example 3**

```plaintext
Input: nums1 = [0, 0], nums2 = [0, 0]
Output: 0.0
Explanation: The merged array is [0, 0, 0, 0]. The median is 0.0.
```

---

**Example 4**

```plaintext
Input: nums1 = [], nums2 = [1]
Output: 1.0
Explanation: The merged array is [1]. The median is 1.0.
```

---

**Example 5**

```plaintext
Input: nums1 = [2], nums2 = []
Output: 2.0
Explanation: The merged array is [2]. The median is 2.0.
```

---

## **Approach 1: Merge and Sort**

This is a straightforward approach where both arrays are merged and sorted, and then the median is calculated.

---

### **Algorithm**

1. Merge the two arrays.
2. Sort the merged array.
3. Find the median:
    - If the total number of elements is odd, return the middle element.
    - If the total number of elements is even, return the average of the two middle elements.

---

### **Code**

```python
def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
```


```python

def findMedian(ary1, ary2):

    new_ary = []

    new_ary.extend(ary1)
    new_ary.extend(ary2)
    new_ary.sort()

    if(len(new_ary)%2):
        return new_ary[len(new_ary) // 2]
    else:
        return ((new_ary[len(new_ary) // 2] + new_ary[(len(new_ary) // 2)-1]) / 2 )
```

---

### **Complexity**

|**Time Complexity**|**Space Complexity**|
|---|---|
|O((m+n)log⁡(m+n))O((m + n) \log(m + n))|O(m+n)O(m + n)|

---

## **Approach 2: Binary Search (Optimal)**

This approach uses **binary search** to achieve the required time complexity of **O(log(min(m, n)))**.

---

### **Algorithm**

1. **Divide and Conquer**:
    
    - Perform binary search on the smaller of the two arrays to partition both arrays into two halves.
    - Ensure that: maxLeftX≤minRightYandmaxLeftY≤minRightX\text{maxLeftX} \leq \text{minRightY} \quad \text{and} \quad \text{maxLeftY} \leq \text{minRightX}
2. **Median Calculation**:
    
    - If the total number of elements is odd: Median=max⁡(maxLeftX,maxLeftY)\text{Median} = \max(\text{maxLeftX}, \text{maxLeftY})
    - If even: Median=max⁡(maxLeftX,maxLeftY)+min⁡(minRightX,minRightY)2\text{Median} = \frac{\max(\text{maxLeftX}, \text{maxLeftY}) + \min(\text{minRightX}, \text{minRightY})}{2}

---

### **Code**

```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is smaller
        
    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted")
```

---

### **Complexity**

|**Time Complexity**|**Space Complexity**|
|---|---|
|O(log⁡(min⁡(m,n)))O(\log(\min(m, n)))|O(1)O(1)|

---

## Summary of Approaches

|**Approach**|**Time Complexity**|**Space Complexity**|**Remarks**|
|---|---|---|---|
|Merge and Sort|O((m+n)log⁡(m+n))O((m + n) \log(m + n))|O(m+n)O(m + n)|Simple but inefficient for large arrays.|
|Binary Search (Optimal)|O(log⁡(min⁡(m,n)))O(\log(\min(m, n)))|O(1)O(1)|Optimal solution; uses divide-and-conquer technique.|

---

## **Test Cases**

### Python Test Function

```python
def test_findMedianSortedArrays():
    test_cases = [
        {"nums1": [1, 3], "nums2": [2], "expected": 2.0},
        {"nums1": [1, 2], "nums2": [3, 4], "expected": 2.5},
        {"nums1": [0, 0], "nums2": [0, 0], "expected": 0.0},
        {"nums1": [], "nums2": [1], "expected": 1.0},
        {"nums1": [], "nums2": [2,3], "expected": 2.5},
        {"nums1": [2,3], "nums2":[], "expected": 2.5},
        {"nums1": [2], "nums2": [], "expected": 2.0},
        {"nums1": [1,2], "nums2": [1,2], "expected": 1.5},
    ]
    
    for i, tc in enumerate(test_cases):
        result = findMedianSortedArrays(tc["nums1"], tc["nums2"])
        assert result == tc["expected"], f"Test case {i + 1} failed: {result} != {tc['expected']}"
    
    print("All test cases passed!")

test_findMedianSortedArrays()
```

This article provides an in-depth explanation of different approaches to solving the "Median of Two Sorted Arrays" problem. The optimal solution leverages binary search for efficient computation.


---


```python
def findMedian(ary1, ary2):

    new_ary = []

    new_ary.extend(ary1)
    new_ary.extend(ary2)
    new_ary.sort()

    if(len(new_ary)%2):
        return new_ary[len(new_ary) // 2]
    else:
        return ((new_ary[len(new_ary) // 2] + new_ary[(len(new_ary) // 2)-1]) / 2 )


```



```python

def findMedian2(ary1, ary2):
    total_len = len(ary1) + len(ary2)
    mid = total_len // 2

    if(total_len == 0):
        return -1

    p1, p2 = 0,0
    sortedItems = []
    while(len(sortedItems) < mid+1):
        if(p1 == len(ary1)):
            sortedItems.append(ary2[p2])
            p2 += 1
        elif(p2 == len(ary2)):
            sortedItems.append(ary1[p1])
            p1 += 1
        elif(ary1[p1] < ary2[p2]):
            sortedItems.append(ary1[p1])
            p1 += 1
        else:
            sortedItems.append(ary2[p2])
            p2 += 1

    if(total_len % 2):
        return sortedItems[-1]
    else:
        return ((sortedItems[-1] + sortedItems[-2]) / 2 )

```


to check {

https://www.youtube.com/watch?v=q6IEA26hvXc


}






