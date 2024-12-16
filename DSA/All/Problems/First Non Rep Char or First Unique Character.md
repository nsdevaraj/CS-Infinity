
## **LeetCode #387: First Unique Character in a String**

[Problem Link](https://leetcode.com/problems/first-unique-character-in-a-string/)

### **Problem Statement**

Given a string `s`, find the first non-repeating character and return its index. If no unique character exists, return `-1`.

---

### **Examples**

#### Example 1:

```plaintext
Input: s = "leetcode"
Output: 0
```

#### Example 2:

```plaintext
Input: s = "loveleetcode"
Output: 2
```

#### Example 3:

```plaintext
Input: s = "aabb"
Output: -1
```

---

### **Approach 1: Hash Map (Two Pass)**

#### **Algorithm**

1. Count the frequency of each character in the string using a hash map.
2. Iterate through the string and return the index of the first character with a frequency of `1`.
3. If no such character exists, return `-1`.

---

#### **Code in Rust**

```rust
use std::collections::HashMap;

pub fn first_uniq_char(s: String) -> i32 {
    let mut frequency = HashMap::new();

    // Count the frequency of each character
    for ch in s.chars() {
        *frequency.entry(ch).or_insert(0) += 1;
    }

    // Find the first unique character
    for (i, ch) in s.chars().enumerate() {
        if frequency[&ch] == 1 {
            return i as i32;
        }
    }

    -1
}

```


```rust

fn first_non_rep_char_index(text: String) -> i32 {
	let mut frequency_map = HashMap::new();

	for ch in text.chars() {
		*frequency_map.entry(ch).or_insert(0) += 1
	}

	for (index, ch) in text.chars().enumerate() {
		if let Some(&count) = frequency_map.get(&ch) {
			if count == 1 {
				return index as i32;
			}
		}
	}

	-1
}
    
```

---

### **Approach 2: Array (Optimized Single Pass)**

#### **Algorithm**

1. Use an array of size `26` to store the count of characters (assuming only lowercase English letters).
2. Count the frequency of each character.
3. Iterate through the string to find the first character with a frequency of `1`.

---

#### **Code in Rust**

```rust
pub fn first_uniq_char(s: String) -> i32 {
    let mut counts = [0; 26];

    // Count frequencies of each character
    for ch in s.chars() {
        counts[(ch as usize - 'a' as usize)] += 1;
    }

    // Find the first unique character
    for (i, ch) in s.chars().enumerate() {
        if counts[(ch as usize - 'a' as usize)] == 1 {
            return i as i32;
        }
    }

    -1
}


```



```rust
impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut count = [0;26];

        let charAInt = 'a' as usize;
        for ch in s.chars(){
            let charInt = ch as usize - charAInt;
            count[charInt] += 1
        }


        for (i, ch) in s.chars().enumerate(){
            let charInt = ch as usize - charAInt;
            if(count[charInt] == 1){
                return i as i32;
            }
        }

        return -1;
    }
}
```


---

### **Complexity Analysis**

#### **Hash Map (Two Pass)**

- **Time Complexity:** O(n)O(n), where nn is the length of the string.
    - The first pass builds the hash map.
    - The second pass checks the indices.
- **Space Complexity:** O(1)O(1) since the hash map stores a fixed number of characters (26 lowercase English letters).

#### **Array (Optimized Single Pass)**

- **Time Complexity:** O(n)O(n), with a single iteration and array-based character counting.
- **Space Complexity:** O(1)O(1), using a fixed-size array.

---

### **Test Cases**

```rust
    fn test_first_uniq_char(first_uniq_char_func: fn(String) -> i32) {
        let test_cases = vec![
            // Regular tests
            ("leetcode".to_string(), 0),
            ("loveleetcode".to_string(), 2),
            ("aabb".to_string(), -1),
            ("abcabcddd".to_string(), -1),
            ("z".to_string(), 0),
            // Edge cases
            ("".to_string(), -1),             // Empty string
            ("a".to_string(), 0),             // Single character string
            ("abcde".to_string(), 0),         // All unique characters
            ("aabbccddeeff".to_string(), -1), // Repeated characters only
            ("abcabcabcabc".to_string(), -1), // Repeated patterns
            ("ababababab".to_string(), -1),   // Alternating repeating patterns
            ("zaaabbbcccddd".to_string(), 0), // First unique occurrence at index 0
            ("xyzx".to_string(), 1),          // First unique character at index 1
            ("abcabcddd".to_string(), -1),
            ("y".to_string(), 0),
        ];

        for (i, (input, expected)) in test_cases.iter().enumerate() {
            let result = first_uniq_char_func(input.clone());
            assert_eq!(
                result,
                *expected,
                "Test case {} failed: input = '{}', expected {}, got {}",
                i + 1,
                input,
                expected,
                result
            );
        }

        println!("All Test cases passed!");
    }```

---

### **Summary Table**

|**Approach**|**Time Complexity**|**Space Complexity**|**Remarks**|
|---|---|---|---|
|**Hash Map (Two Pass)**|O(n)O(n)|O(1)O(1)|Easy to implement; uses a hash map.|
|**Array (Optimized Single Pass)**|O(n)O(n)|O(1)O(1)|More efficient for strings limited to lowercase letters.|

Both approaches are efficient, but the array-based approach is faster for strings containing only lowercase English letters due to reduced hash map overhead.

---


### 7. **Find First Non-Repeating Character**

**Problem:** Find the first non-repeating character in a string.

```python
from collections import Counter

def first_non_repeating_char(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None
```



```rust
fn first_non_rep_char_index(text: String) -> usize {
    // Example implementation to find first non-repeated character index
    for (index, c) in text.chars().enumerate() {
        if text.chars().filter(|&x| x == c).count() == 1 {
            return index;
        }
    }
    text.len() // Return the length if no non-repeated characters are found
}

fn main() {
    let text = String::from("hello");
    println!("{}", first_non_rep_char_index(text));
}

```



Runtime: 0ms

rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut letter_count = [0; 26];
        let mut unique_letters = HashMap::new();
        for (idx, c) in s.char_indices().rev() {
            let i = (c as u8 - b'a') as usize;
            if letter_count[i] == 0 {
                unique_letters.insert(c, idx);
            } else if letter_count[i] == 1 {
                unique_letters.remove(&c);
            }
            letter_count[i] += 1;
        }

        match unique_letters.values().min() {
            Some(&min) => min as i32,
            None => -1
        }
    }
}
```


Memory: 2.2mb

rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        
        let mut counter: HashMap<char, (i32, usize)> = HashMap::new();

        for (i, c) in s.chars().enumerate() {
            let caracter = counter.entry( c ).or_insert( (0, i) );
            caracter.0 += 1;
        }

        for (i, c) in s.chars().enumerate() {

            match counter.get( &c ).unwrap() {
                ( 1, i ) => { return *i as i32 }
                _ => {}
            }

        }

        -1
    }
}
```