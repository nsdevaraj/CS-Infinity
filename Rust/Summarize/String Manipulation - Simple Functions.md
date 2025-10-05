


```rust
use std::collections::HashMap;


fn get_string() -> String {
    let mut input = String::new();
    println!("Please give any string:");
    std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    return input.trim().to_string();
}


fn reverse_string(input: &str) -> String {
    input.chars().rev().collect()
}


fn capitalize_string(input: &str) -> String {
    let mut str_iter = input.chars();
    let first_char = str_iter.next().expect("No first char in string");
    let first_upper = first_char.to_uppercase().collect::<String>();
    let rest_lower = str_iter.as_str().to_lowercase();
    first_upper + &rest_lower
}

fn count_words(s: &str) -> usize {
    s.split_whitespace().count()
}


fn count_characters(input: &str) -> HashMap<char, u32> {
    let mut char_map = HashMap::new();

    for ch in input.chars() {
        let count = char_map.entry(ch).or_insert(0);
        *count += 1;
    }

    char_map
}


fn main(){
    let input_string = get_string();
    println!("You entered: {input_string}");
    
    let reversed_string = reverse_string(&input_string);
    println!("Reversed string: {reversed_string}");

    let capitalized_string = capitalize_string(&input_string);
    println!("Capitalized string: {capitalized_string}");

    let word_count = count_words(&input_string);
    println!("Word count of string: {word_count}");

    let char_count = count_characters(&input_string);
    println!("Character count map for string: {char_count:?}");

}

/*=>
Please give any string:
sadf adsfa /sd/sf adsfas
You entered: sadf adsfa /sd/sf adsfas
Reversed string: safsda fs/ds/ afsda fdas
Capitalized string: Sadf adsfa /sd/sf adsfas
Word count of string: 4
Character count map for string: {'/': 2, 'd': 4, 'a': 5, 's': 6, 'f': 4, ' ': 3}
 */

```




## 🧠 Capitalize String

```rust
fn capitalize_string(input: &str) -> String {
    let mut str_iter = input.chars();
    let first_char = str_iter.next().expect("No first char in string");
    let first_upper = first_char.to_uppercase().collect::<String>();
    let rest_lower = str_iter.as_str().to_lowercase();
    first_upper + &rest_lower
}
```

---

### 🔍 Line-by-Line Explanation

#### 1. `let mut str_iter = input.chars();`

- **What:** Creates a mutable iterator over the characters of the input string.
    
- **Why:** Rust strings are UTF-8; `chars()` ensures correct handling of multi-byte Unicode characters.
    
- **How:** Lets us process the first character separately from the rest.
    

#### 2. `let first_char = str_iter.next().expect("No first char in string");`

- **What:** Extracts the first character.
    
- **Why:** We need to capitalize it.
    
- **How:** `next()` returns an `Option<char>`; `expect()` panics if the input is empty.
    

#### 3. `let first_upper = first_char.to_uppercase().collect::<String>();`

- **What:** Converts the first character to uppercase.
    
- **Why:** Some characters (like `ß`) expand to multiple uppercase letters.
    
- **How:** `to_uppercase()` returns an iterator; `collect()` turns it into a `String`.
    

#### 4. `let rest_lower = str_iter.as_str().to_lowercase();`

- **What:** Converts the remaining string to lowercase.
    
- **Why:** To ensure consistent capitalization.
    
- **How:** `as_str()` gives the unconsumed part of the string; `to_lowercase()` creates a lowercase version.
    

#### 5. `first_upper + &rest_lower`

- **What:** Concatenates the capitalized first character with the rest.
    
- **Why:** Forms the final result.
    
- **How:** Rust's `+` operator requires a `String + &str`.
    

---

### 📋 Tabular Breakdown

|Line|Purpose|Explanation|
|---|---|---|
|`input.chars()`|Create character iterator|Safe Unicode-aware splitting|
|`str_iter.next().expect(...)`|Get first char|Panics if string is empty|
|`to_uppercase().collect()`|Uppercase first char|Handles multi-char cases|
|`as_str().to_lowercase()`|Lowercase the rest|From remaining part of original string|
|`+`|Join parts|Final capitalized output|

---

### ✅ Example

**Input:** `"rUST"`  
**Output:** `"Rust"`

---

## 🔁 Reverse String

```rust
fn reverse_string(input: &str) -> String {
    input.chars().rev().collect()
}
```

This compact function reverses a string **safely** and **Unicode-correctly**.

---

### 🔍 Line-by-Line Explanation

#### 1. `input.chars()`

- **What:** Creates a character iterator.
    
- **Why:** Ensures full character handling — safe with emojis, accents, etc.
    
- **How:** Treats characters correctly, avoiding byte-level errors.
    

#### 2. `.rev()`

- **What:** Reverses the character order.
    
- **Why:** To flip the string.
    
- **How:** Iterates from end to start.
    

#### 3. `.collect()`

- **What:** Converts the reversed characters into a `String`.
    
- **Why:** We need a proper `String` as the output.
    
- **How:** Uses iterator collection; Rust infers `String`.
    

---

### 📝 Summary Table

|Step|Purpose|
|---|---|
|`chars()`|Unicode-safe character splitting|
|`rev()`|Reverse character order|
|`collect()`|Build final `String`|

---

### ✅ Example

**Input:** `"Rust 🦀"`  
**Output:** `"🦀 tsuR"`

---

## 📥 Get User Input

```rust
fn get_string() -> String {
    let mut input = String::new();
    println!("Please give any string:");
    std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    return input.trim().to_string();
}
```

This function reads a full line of text from the user and returns it as a clean `String`, trimmed of leading/trailing whitespace and newline characters.

---

### 🔍 Line-by-Line Explanation

#### 1. `let mut input = String::new();`

- **What:** Initializes an empty, mutable `String`.
    
- **Why:** To store the input from standard input (stdin).
    

#### 2. `println!("Please give any string:");`

- **What:** Displays a prompt to the user.
    
- **Why:** Informs the user to enter a string.
    

#### 3. `std::io::stdin().read_line(&mut input)`

- **What:** Reads a full line of user input.
    
- **Why:** Captures input up to the newline.
    
- **How:** Appends the input to the `input` string.
    

#### 4. `.expect("Failed to read line");`

- **What:** Handles potential I/O errors.
    
- **Why:** Panics with a message if reading fails.
    

#### 5. `input.trim().to_string()`

- **What:** Trims whitespace (especially `\n`) and returns a clean `String`.
    
- **Why:** Removes trailing newline or extra spaces from user input.
    
- **How:** `trim()` returns a `&str`; `.to_string()` converts it back to `String`.
    

---

### 📝 Summary Table

|Line|Purpose|Explanation|
|---|---|---|
|`String::new()`|Initialize buffer|Prepares to collect input|
|`println!(...)`|Prompt user|Makes interaction clear|
|`read_line(...)`|Read from stdin|Captures input with newline|
|`expect(...)`|Error handling|Fails gracefully if input fails|
|`trim().to_string()`|Clean output|Removes newline and returns a `String`|

---

### ✅ Example

```
Please give any string:
  Hello, Rust!
```

**Returned String:** `"Hello, Rust!"`

---

## 🔤 Count Words

```rust
fn count_words(s: &str) -> usize {
    s.split_whitespace().count()
}
```

This function counts the number of words in a string by splitting on whitespace and returning the total count.

---

### 🔍 Explanation

- `split_whitespace()` splits the string on any whitespace (spaces, tabs, newlines).
    
- `.count()` returns the number of resulting substrings, effectively the word count.
    

---

### ✅ Example

Input: `"Hello, Rust world!"`  
Output: `3`


---

## 🔢 Count Characters

```rust
fn count_characters(input: &str) -> HashMap<char, u32> {
    let mut char_map = HashMap::new();

    for ch in input.chars() {
        let count = char_map.entry(ch).or_insert(0);
        *count += 1;
    }

    char_map
}
```

This function counts how many times each character appears in a given string and returns a `HashMap<char, u32>` mapping each character to its frequency.

---

### 🔍 Line-by-Line Explanation

#### 1. `let mut char_map = HashMap::new();`

- **What:** Initializes an empty `HashMap`.
    
- **Why:** Used to store character frequencies.
    
- **How:** Keys are characters (`char`), values are counts (`u32`).
    

#### 2. `for ch in input.chars() {`

- **What:** Iterates over each character in the string.
    
- **Why:** To count each occurrence.
    
- **How:** Uses `.chars()` for Unicode-aware iteration.
    

#### 3. `let count = char_map.entry(ch).or_insert(0);`

- **What:** Accesses the current count for the character or inserts 0 if not found.
    
- **Why:** Ensures we can safely increment the count.
    
- **How:** `entry()` gives mutable access to the value.
    

#### 4. `*count += 1;`

- **What:** Increments the count.
    
- **Why:** Tracks how many times the character has occurred.
    
- **How:** Uses dereference to modify the value in-place.
    

#### 5. `char_map`

- **What:** Returns the final character count map.
    
- **Why:** Gives access to frequency data.
    

---

### 📝 Summary Table

|Line|Purpose|Explanation|
|---|---|---|
|`HashMap::new()`|Create map|Stores counts of each character|
|`input.chars()`|Iterate|Unicode-safe character loop|
|`.entry(...).or_insert(0)`|Insert or update count|Handles new and existing chars uniformly|
|`*count += 1`|Increment count|Adds to existing value|
|`char_map`|Return result|Final map of character frequencies|

---

### ✅ Example

Input: `"hello"`

Output: `{ 'h': 1, 'e': 1, 'l': 2, 'o': 1 }`

---






to do {

first non repeating char index program


}