
Sure! Let's break down the code snippet piece-by-piece to understand it fully.

```rust
for (index, ch) in text.chars().enumerate() {
    if let Some(&count) = frequency_map.get(&ch) {
        if count == 1 {
            return index;
        }
    }
}
```

---

### 1. `for (index, ch) in text.chars().enumerate()`

- **`text.chars()`**:
    
    - This converts the string `text` into an iterator over its characters (`char` values).
    - Example:
        
        ```rust
        let text = "hello";
        text.chars(); // gives an iterator over ['h', 'e', 'l', 'l', 'o']
        ```
        
- **`.enumerate()`**:
    
    - `enumerate()` transforms the iterator so it returns pairs of `(index, value)` during iteration.
    - `index` is the position (zero-based) of the current character in the string.
    - `value` (in this case `ch`) is the character at that index.
    - Example:
        
        ```rust
        let text = "hello";
        for (index, ch) in text.chars().enumerate() {
            println!("Index: {}, Char: {}", index, ch);
        }
        ```
        
        Output:
        
        ```
        Index: 0, Char: h
        Index: 1, Char: e
        Index: 2, Char: l
        Index: 3, Char: l
        Index: 4, Char: o
        ```
        

---

### 2. `if let Some(&count) = frequency_map.get(&ch)`

- **`frequency_map.get(&ch)`**:
    
    - `frequency_map` is a `HashMap<char, usize>`.
    - `get(&ch)` attempts to retrieve the frequency count of the current character (`ch`) from the map.
    - It returns an `Option<&usize>`. The options are:
        - `Some(&count)` if the character is in the map.
        - `None` if the character isn't in the map.
    - Example:
        
        ```rust
        let mut map = HashMap::new();
        map.insert('h', 2);
        map.insert('e', 1);
        
        let result = map.get(&'h'); // Some(&2)
        let result2 = map.get(&'l'); // None
        ```
        
- **`if let Some(&count)`**:
    
    - This is a Rust feature called _pattern matching with `if let`_.
    - If the `Option` contains a value (`Some(value)`), it extracts that value for use.
    - `&count` is used here to dereference the value so it can be compared directly in the next condition.
    - This avoids having to write:
        
        ```rust
        if let Some(count) = frequency_map.get(&ch) {
            if *count == 1 {
                return index;
            }
        }
        ```
        

---

### 3. `if count == 1`

- This checks if the frequency of the current character is **exactly 1** in the string based on the `frequency_map`.
- If `count` is 1, that means the character is non-repeated in the string.

---

### 4. `return index;`

- If a character is found with a frequency of **1** (i.e., it is non-repeated), the index of that character is returned immediately.
- This means the function stops searching at the first non-repeated character index found.

---

### Summary of Logic:

Putting it all together:

1. Loop through each character of the string `text`, along with its index.
2. For each character, check if it's in the `frequency_map` and whether its frequency is `1`.
3. If a character meets these conditions, return its index because it is the first non-repeated character in the string.

---

### Example with Input:

Let's say:

```rust
text = "hello";
frequency_map = { 'h': 2, 'e': 1, 'l': 2, 'o': 1 }
```

The string `"hello"` has the following frequencies:

- `'h'`: 2
- `'e'`: 1
- `'l'`: 2
- `'o'`: 1

Starting the loop:

1. Index `0`: `'h'` has frequency 2 ➜ skip.
2. Index `1`: `'e'` has frequency 1 ➜ return index `1`.

The first non-repeated character in the string `"hello"` is `'e'`, at index `1`.

---


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



```rust
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