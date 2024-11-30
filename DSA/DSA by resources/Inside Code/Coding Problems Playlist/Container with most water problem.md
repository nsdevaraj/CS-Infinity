

[Container with most water problem - Inside code](https://youtu.be/I7fFgU6n4x8?si=5wvxaUsi0kuueROZ)


### Container With Most Water Problem

Welcome to this new Inside Code video where we will discuss a classic coding problem: the **Container With Most Water** problem.

#### Problem Statement

Given an array `heights` that contains the heights of \( n \) vertical lines, find two lines that can form a container capable of holding the most water. You need to return the maximum area of water that can be contained.

**Note:**
- All heights are positive.
- The array will contain at least two elements.

### Visual Representation

To better understand the problem, consider the following examples:

1. **Example 1:**
   - Input: `heights = [1,8,6,2,5,4,8,3,7]`
   - Output: `49`
   - Explanation: The lines at indices 1 and 8 (heights 8 and 7) form a container with a width of 7 and height of 7, thus the area is \( 7 \times 7 = 49 \).

2. **Example 2:**
   - Input: `heights = [1,1]`
   - Output: `1`
   - Explanation: The only possible container is formed by the two lines of height 1, leading to an area of \( 1 \times 1 = 1 \).

Feel free to pause the video to analyze these examples!

### Solution Approaches

#### Approach 1: Brute Force

The brute force approach involves checking every possible pair of lines to determine the maximum area.

**Algorithm:**
1. Initialize `maxArea` to 0.
2. Use two nested loops to check all pairs of lines.
3. For each pair, calculate the area using the formula:

   \[
   \text{Area} = \min(\text{heights}[i], \text{heights}[j]) \times (j - i)
   \]

4. Update `maxArea` if the calculated area is greater than the current `maxArea`.
5. Return `maxArea`.

**Python Code:**
```python
def containerWithMostWater(heights):
    maxArea = 0
    n = len(heights)
    for i in range(n):
        for j in range(i + 1, n):
            area = min(heights[i], heights[j]) * (j - i)
            maxArea = max(maxArea, area)
    return maxArea
```

**Time Complexity:** \( O(n^2) \)  
**Space Complexity:** \( O(1) \)  
*Explanation: The time complexity is quadratic because of the nested loops, while the space complexity is constant as we use only a few variables.*

---

#### Approach 2: Two Pointers Technique

The two pointers technique optimizes the brute force solution by reducing the number of comparisons needed.

**Algorithm:**
1. Initialize two pointers: `left` at the beginning (index 0) and `right` at the end (index \( n - 1 \)).
2. Calculate the area between the lines at the `left` and `right` pointers.
3. Update `maxArea` if the calculated area is greater than the current `maxArea`.
4. Move the pointer that points to the shorter line, hoping to find a taller line:
   - If `heights[left] < heights[right]`, increment the `left` pointer.
   - Otherwise, decrement the `right` pointer.
5. Continue until the two pointers meet, then return `maxArea`.

**Python Code:**
```python
def containerWithMostWater(heights):
    maxArea = 0
    left = 0
    right = len(heights) - 1
    
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        maxArea = max(maxArea, area)
        
        # reduce smaller heights first
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
            
    return maxArea
```



**Time Complexity:** \( O(n) \)  
**Space Complexity:** \( O(1) \)  
*Explanation: The time complexity is linear because we traverse the array only once, and the space complexity remains constant as we use only a few variables.*

---

### Conclusion

In this video, we explored the **Container With Most Water** problem through two different approaches. The brute force method, while straightforward, is less efficient than the two pointers technique, which optimally narrows down the search space. 



leet code answers:

Runtime: 0ms

python

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==2:
            return min(height)
        else:
            m=0
            i=0
            a=0
            h=max(height)
            j=len(height)-1
            while i<j:
                if height[i] < height[j]:
                    a=height[i]*(j-i)
                    i += 1
                else:
                    a=height[j]*(j-i)
                    j -= 1
                if m<a:
                    m=a
                if (j-i) * h < m:
                    return m
        return m       
```


Memory: 21mb

python

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v=0
        l, r =0, len(height)-1

        while l<r:
            v = min(height[l],height[r])*(r-l)
            max_v = max(max_v,v)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1

        
        return max_v

f = open('user.out', 'w')
S = Solution()
for case in stdin:
    f.write(f"{S.maxArea(json.loads(case))}\n")
f.flush()
exit(0)
        
```