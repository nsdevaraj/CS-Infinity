

[Binary Search](https://leetcode.com/discuss/study-guide/5913750/binary-search-all-you-need-to-know)


### **When to Use Binary Search**

Binary search can be applied to any problem that can be expressed as a **search problem over a monotonic function**. The key is to represent your problem as a **monotonic function** (either increasing or decreasing), making binary search applicable.

#### **Monotonic Functions and Binary Search Applicability:**

| **Monotonic Function**              | **Can Binary Search be Applied?** |
| ----------------------------------- | --------------------------------- |
| Monotonically increasing            | True                              |
| Monotonically decreasing            | True                              |
| Piecewise monotonic                 | True                              |
| Sorted array                        | True (As it is a monotonic function) |
| Non-monotonic                       | False                             |

### **Common Problems Solved by Binary Search**

| **Problem**                                             | **Monotonic Function**                                       |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| Finding the minimum or maximum value of a function       | The function is monotonically increasing or decreasing        |
| Finding the root of a number                             | The function is monotonically increasing or decreasing        |
| Finding the smallest or largest element in a range       | The function is monotonically increasing or decreasing        |
| Finding the number of times a function crosses a value   | The function is piecewise monotonic                           |
| Finding the first occurrence of a value in a sorted array| The array is sorted, so the function is monotonically increasing |
| Finding the last occurrence of a value in a sorted array | The array is sorted, so the function is monotonically decreasing |

---

### **Monotonic Functions**

- **Monotonic Function**: A function whose value either always increases or always decreases.
- **Monotonically Increasing Function**: The function's value always increases as the input increases.
- **Monotonically Decreasing Function**: The function's value always decreases as the input increases.
- **Piecewise Monotonic Function**: A function that is monotonic over some intervals but not monotonic over others.

---

### **Why Use Binary Search?**

- **Divide-and-Conquer Algorithm**: Binary search works by recursively dividing the search space in half.
- **Time Complexity**: \( O(\log n) \), where \( n \) is the number of elements. Each step reduces the search space by half.
- **Efficiency**: Suitable for large datasets, reducing the number of comparisons logarithmically compared to linear search.

#### **Binary Search Analogy**
- Similar to searching for a word in a dictionary:
  1. Open the dictionary to the middle page.
  2. If the word is on that page, you're done.
  3. If not, eliminate half the pages and continue the search in the remaining half.
  4. This process continues until you find the word.

---

### **Binary Search Algorithm**

```cpp
int binary_search(vector<int> &v, int target)
{
    int l = 0, h = v.size() - 1, ans = -1;
    while (l <= h)
    {
        int mid = (l + h) / 2;
        if (v[mid] == target)
            return ans = mid;
        else if (v[mid] < target)
            l = mid + 1;
        else
            h = mid - 1;
    }
    return ans;
}
```

---

### **Avoiding Infinite Loops in Binary Search**

- **Cause**: Infinite loops occur when the search space never shrinks.
- **Solution**: Never set `low` or `high` to `mid`. Always update them to `mid + 1` or `mid - 1` to ensure the search space shrinks and the loop eventually terminates.

#### **Lower Bound Example**

```cpp
int lowerbound(vector<int> &nums, int target)
{
    int l = 0, h = nums.size() - 1, ans = -1;
    while (l <= h)
    {
        int mid = l + (h - l) / 2;
        if (nums[mid] >= target)
        {
            ans = mid; // First element >= target
            h = mid - 1;
        }
        else
            l = mid + 1;
    }
    return ans;
}
```

#### **Upper Bound Example**

```cpp
int upperbound(vector<int> nums, int target)
{
    int l = 0, h = nums.size() - 1, mid = 0, ans = -1;
    while (h >= l)
    {
        mid = (l + h) / 2;
        if (nums[mid] > target)
        {
            ans = mid; // First element > target
            h = mid - 1;
        }
        else
            l = mid + 1;
    }
    return ans;
}
```


### Both

```python
 def binarySearch(findLeftmost: bool) -> int:
        left, right = 0, len(nums) - 1
        position = -1  # Initialize position as -1 in case target is not found

        while left <= right:
            mid = (left + right) // 2  # Calculate mid-point
            if target > nums[mid]:
                left = mid + 1  # Search right half
            elif target < nums[mid]:
                right = mid - 1  # Search left half
            else:
                position = mid  # Target found, update position
                # Narrow down search based on leftmost/rightmost flag
                if findLeftmost:
                    right = mid - 1  # Continue search in left half for leftmost position
                else:
                    left = mid + 1   # Continue search in right half for rightmost position

        return position
```

---

### **Handling Binary Search When the Search Space Cannot Shrink**

- In cases where the target is not in the array or the array is sorted in reverse, binary search might not shrink the search space.
- However, binary search will terminate after \( O(\log n) \) steps, ensuring the algorithm doesn't loop indefinitely.

---

### **Binary Search on Monotonic Functions**

#### **Square Root Example**

```cpp
class Solution {
public:
    int mySqrt(int n) {
        double left = 0, right = n, mid = 0;
        for (int i = 0; i < 100; i++) // Iterate 100 times to avoid infinite loop
        {
            mid = (left + right) / 2;
            if (mid * mid > n)
                right = mid;
            else
                left = mid;
        }
        return mid;
    }
};
```

---

### **General Binary Search Template**

```cpp
int BinarySearchTemplate(vector<int>& v, int cond) 
{
    int low = 0, high = somehighvalue, ans = choose_value_based_on_question;
    while (high >= low)
    {
        int mid = (low + high) / 2;
        if (findIsBoundary(mid, h, cond))
        {
            // Update search space and answer based on condition
            high = mid - 1;
            ans = min(ans, mid); // Example of storing result
        }
        else
        {
            low = mid + 1;
        }
    }
    return ans;
}
```

---

### **Binary Search: Understanding Boundaries**

- Binary search problems can often be reduced to finding a boundary between "true" and "false" values.
- For example:
  - **Lower Bound**: The first value that satisfies a condition.
  - **Upper Bound**: The smallest value greater than the target.

---

### **Practical Example: Koko Eating Bananas**

```cpp
class Solution {
public:
    bool iseat(int k, int h, vector<int>& piles)
    {
        long long cnt = 0;
        for (int i = 0; i < piles.size(); i++)
        {
            if (piles[i] % k) cnt++;
            cnt += piles[i] / k;
        }
        return h >= cnt;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1, high = 1e9, ans = INT_MAX;
        sort(piles.begin(), piles.end());
        while (high >= low)
        {
            int mid = (low + high) / 2;
            if (iseat(mid, h, piles))
            {
                high = mid - 1;
                ans = min(ans, mid); // Store minimum speed where condition holds true
            }
            else
            {
                low = mid + 1;
            }
        }
        return ans;
    }
};
```

---

This breakdown explains **why** and **when** binary search is useful, how it operates on **monotonic functions**, and provides concrete examples of using binary search in real-world problems.

