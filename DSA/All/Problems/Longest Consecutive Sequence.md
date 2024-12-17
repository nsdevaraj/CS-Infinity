**Problem Statement: Longest Consecutive Sequence**

https://leetcode.com/problems/longest-consecutive-sequence/


Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

Your algorithm should run in **O(n)** time complexity.

---

### Examples

- **Example 1:**
    
    - Input: `nums = [100, 4, 200, 1, 3, 2]`
    - Output: `4`
    - Explanation: The longest consecutive elements sequence is `[1, 2, 3, 4]`.
- **Example 2:**
    
    - Input: `nums = [0,3,7,2,5,8,4,6,0,1]`
    - Output: `9`

---

### Constraints

- 0≤nums.length≤1050 \leq nums.length \leq 10^5
- −109≤nums[i]≤109-10^9 \leq nums[i] \leq 10^9

---

### Solution

We can solve this problem in **O(n)** time by using a **HashSet**:

1. Add all elements to a `HashSet` to enable O(1)O(1) lookups.
2. For each number, if it's the **start** of a sequence (i.e., `num - 1` is not in the set), count the length of the sequence starting from that number.
3. Keep track of the maximum sequence length.

---

### Implementation in Rust

```rust
use std::collections::HashSet;

pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
    // Edge case: if array is empty
    if nums.is_empty() {
        return 0;
    }
    
    // Create a HashSet from the numbers for O(1) lookup
    let num_set: HashSet<i32> = nums.into_iter().collect();
    let mut max_length = 0;

    // Iterate over the set
    for &num in &num_set {
        // Check if this is the start of a sequence
        if !num_set.contains(&(num - 1)) {
            let mut current_num = num;
            let mut current_length = 1;

            // Count the length of the sequence
            while num_set.contains(&(current_num + 1)) {
                current_num += 1;
                current_length += 1;
            }

            max_length = max_length.max(current_length);
        }
    }

    max_length
}


```



```rust

    fn ans_func(nums: Vec<i32>) -> usize {
        let mut longest: usize = 0;
        let nums_set: HashSet<i32> = nums.into_iter().collect();

        for &num in &nums_set {
            if !nums_set.contains(&(num - 1)) {
                let mut length: usize = 1;

                while nums_set.contains(&(num + length as i32)) {
                    length += 1;
                }

                longest = longest.max(length);
            }
        }

        return longest;
    }
```

---

### Explanation of the Code

1. **HashSet for Fast Lookup**:
    
    - We use a `HashSet` to store all numbers for O(1)O(1) lookups.
2. **Check Sequence Start**:
    
    - For each number, check if it's the start of a sequence (`num - 1` not in set).
3. **Count Sequence Length**:
    
    - Starting from the current number, check for consecutive numbers and count the sequence length.
4. **Update Maximum Length**:
    
    - Keep track of the longest sequence length found so far.

---

### Complexity Analysis

- **Time Complexity**: O(n)O(n), where nn is the number of elements in `nums`. We iterate through the set and perform constant time operations for each number.
- **Space Complexity**: O(n)O(n) for the `HashSet`.

---

Test

```rust
fn test_longest_consecutive(ans_func: fn(Vec<i32>) -> i32) {
    let cases = vec![
        // Test Case 1: Example with a simple consecutive sequence
        (vec![100, 4, 200, 1, 3, 2], 4),
        // Test Case 2: Example with duplicates and mixed order
        (vec![0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        // Test Case 3: Single element
        (vec![1], 1),
        // Test Case 4: All elements the same
        (vec![1, 1, 1, 1], 1),
        // Test Case 5: No consecutive numbers
        (vec![10, 20, 30, 40], 1),
        // Test Case 6: Long sequence with negative numbers
        (vec![-5, -4, -3, -2, -1, 0, 1, 2], 8),
        // Test Case 7: Empty array
        (vec![], 0),
        // Test Case 8: All negative numbers with a break
        (vec![-10, -9, -8, -6, -5, -4], 3),
        // Test Case 9: Sequence at the end of the array
        (vec![10, 15, 20, 25, 26, 27, 28], 4),
        // Test Case 10: Random order with multiple sequences
        (vec![9, 1, 2, 3, 8, 5, 4, 7], 5),
        // Test Case 11: Array of length n with unique values
        ((1..=10000).collect::<Vec<i32>>(), 10000),
        // Test Case 12: Array containing negatives and positive gaps
        (vec![-1, -2, -3, 5, 6, 7, 8, 0, 1, 2, 3, 4], 12),
    ];

    for (i, (input, expected)) in cases.iter().enumerate() {
        let result = ans_func(input.clone());
        assert_eq!(result, *expected, "Test case {} failed", i + 1);
    }
    println!("All test cases passed!");
}

```


---


Others


Runtime: 6ms

rust

```rust
use std::cmp::max;

impl Solution {
    pub fn longest_consecutive(mut nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        nums.sort_unstable();
        // nums.dedup();
        let mut longest = 1;
        let mut count = 1;
        let mut prev = nums[0];
        for ele in nums.into_iter().skip(1) {
            if ele == prev {
                continue;
            }
            if ele == prev + 1 {
                count += 1;
            } else {
                longest = max(longest, count);
                count = 1;
            }
            prev = ele;
        }
        max(longest, count)
    }
}
```


Memory: 3.3mb

rust

```rust
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();
        nums.dedup();
        nums.chunk_by(|x,y| x + 1==*y).map(|x| x.len()).max().unwrap_or_default() as i32
    }
}
```


