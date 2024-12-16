


### **1. Swapping Ownership**

**Question**: Write a function to swap the ownership of two `String` values.  
**Solution**: Use a tuple to return swapped values.

```rust
fn swap_ownership(s1: String, s2: String) -> (String, String) {
    (s2, s1)
}

fn main() {
    let string1 = String::from("hello");
    let string2 = String::from("world");
    let (new_string1, new_string2) = swap_ownership(string1, string2);

    println!("Swapped: {} and {}", new_string1, new_string2);
}
```

---

### **2. Shared Reference Example**

**Question**: Write a function that calculates the length of a string without taking ownership.  
**Solution**: Use immutable borrowing.

```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}

fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}", s1, len); // s1 is still valid here
}
```


### **5. Multiple Borrowing**

**Question**: Write a function that takes multiple immutable references to calculate the sum of lengths of two strings.

**Solution**: Use multiple immutable references.

```rust
fn total_length(s1: &String, s2: &String) -> usize {
    s1.len() + s2.len()
}

fn main() {
    let string1 = String::from("hello");
    let string2 = String::from("world");
    let total = total_length(&string1, &string2);

    println!("Total length: {}", total);
}
```


### **6. Ownership Transfer in Functions**

**Question**: Write a function that takes ownership of a `String` and returns its uppercase version.

**Solution**: Ownership is moved to the function.

```rust
fn to_uppercase(mut s: String) -> String {
    s = s.to_uppercase();
    s
}

fn main() {
    let string1 = String::from("hello");
    let upper = to_uppercase(string1);
    println!("{}", upper); // string1 is no longer valid
}
```



---

### **3. Mutable Reference Example**

**Question**: Write a function that appends a suffix to a string using mutable borrowing.  
**Solution**: Use mutable references.

```rust
fn append_suffix(s: &mut String, suffix: &str) {
    s.push_str(suffix);
}

fn main() {
    let mut s1 = String::from("hello");
    append_suffix(&mut s1, " world");
    println!("{}", s1); // Output: hello world
}
```


### **7. Combining Borrowing and Ownership**

**Question**: Write a function that calculates the length of a string and appends a suffix to it.  
**Solution**: Use both immutable and mutable references.

```rust
fn process_string(s: &mut String) -> usize {
    let len = s.len(); // Immutable borrow
    s.push_str(" suffix"); // Mutable borrow
    len
}

fn main() {
    let mut s = String::from("hello");
    let length = process_string(&mut s);
    println!("Original length: {}, Modified string: {}", length, s);
}
```


---

### **4. Preventing Dangling References**

**Question**: Why does the following code fail, and how can you fix it?

```rust
fn dangling() -> &String {
    let s = String::from("hello");
    &s // ERROR: s is dropped here, returning a dangling reference
}
```

**Solution**: Return the `String` instead of a reference to ensure ownership transfer.

```rust
fn dangling() -> String {
    let s = String::from("hello");
    s // Ownership is transferred
}

fn main() {
    let result = dangling();
    println!("{}", result);
}
```


---

### **8. Passing References in Loops**

**Question**: Create a function that prints each element of a vector of strings using references.  
**Solution**: Use immutable references in a loop.

```rust
fn loop_and_print(strings: &Vec<String>) {
    for s in strings {
        println!("{}", s);
    }
}

fn main() {
    let texts = vec![
        String::from("one"),
        String::from("two"),
        String::from("three"),
    ];

    loop_and_print(&texts);
}
```

---

### **9. Nested Borrowing**

**Question**: Why does the following code fail? Fix it.

```rust
fn nested_borrow() {
    let mut s = String::from("hello");
    let r1 = &s; // Immutable borrow
    let r2 = &mut s; // ERROR: Cannot borrow as mutable while immutable borrow exists
}
```

**Solution**: Ensure mutable and immutable references do not overlap.

```rust
fn nested_borrow() {
    let mut s = String::from("hello");
    {
        let r1 = &s; // Immutable borrow
        println!("{}", r1); // Use r1 within its scope
    }
    let r2 = &mut s; // Mutable borrow is now safe
    r2.push_str(" world");
    println!("{}", r2);
}
```



```rust
fn nested_borrow() {
    let mut s = String::from("hello");
    let r1 = &s; // Immutable borrow
    let r2 = &mut s; // ERROR: Cannot borrow as mutable while immutable borrow exists

    println!("{}", r2)
}
```

This code illustrates **Rust’s borrowing rules**, particularly the rule that **mutable and immutable references cannot coexist**. Let's break it down step by step:

---

### **Key Concepts**

1. **Immutable Borrow**:
    
    ```rust
    let r1 = &s;
    ```
    
    Here, `r1` is an **immutable reference** to the `String` `s`. While `r1` exists, `s` is effectively "locked" in a read-only state. You cannot modify `s` or create a mutable reference (`&mut s`) until all immutable references (`r1`) go out of scope.
    
2. **Mutable Borrow**:
    
    ```rust
    let r2 = &mut s;
    ```
    
    Here, you're trying to create a **mutable reference** (`r2`) to `s`. However, a mutable reference requires **exclusive access** to the variable. This means no other references—immutable or mutable—can exist at the same time.
    
3. **Conflict**:
    
    - Rust prevents the creation of `r2` because `r1` is still active.
    - Allowing both references at the same time could lead to **undefined behavior**, such as a read-after-write or write-after-read issue.

---

### **The Borrow Checker**

Rust’s borrow checker ensures memory safety at compile time by enforcing strict borrowing rules:

1. You can have **either**:
    - Any number of immutable references (`&T`), **or**
    - Exactly one mutable reference (`&mut T`).
2. References must always be valid. Rust prevents **dangling references**.

---

### **Why This Code Fails**

In this example:

- The immutable borrow `r1` of `s` is still active when you attempt to create the mutable borrow `r2`.
- Rust does not allow simultaneous mutable and immutable references, so the compiler raises an error:

```
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as immutable
```

---

### **Fixing the Code**

To fix the issue, ensure `r1` is no longer used before creating `r2`. You can achieve this by limiting the scope of `r1`:

```rust
fn nested_borrow() {
    let mut s = String::from("hello");
    
    {
        let r1 = &s; // Immutable borrow
        println!("{}", r1); // Use r1 and let it go out of scope
    } // r1 goes out of scope here
    
    let r2 = &mut s; // Mutable borrow is now allowed
    r2.push_str(" world");
    println!("{}", r2);
}
```

---

### **Explanation of Fix**

1. `r1` (the immutable borrow) is enclosed in a smaller block scope (`{ ... }`).
2. Once `r1` goes out of scope, the borrow checker allows the mutable borrow `r2`.
3. Now, you can safely modify `s` through `r2` without violating Rust’s borrowing rules.

---

### **Output of Fixed Code**

```
hello
hello world
```

This ensures the code adheres to Rust’s strict memory safety guarantees, preventing data races and undefined behavior.


---

### **10. Lifetime Annotations in Functions**

**Question**: Write a function that returns the longer of two string slices with lifetime annotations.

**Solution**: Use lifetime annotations.

```rust
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}

fn main() {
    let string1 = "hello";
    let string2 = "world!";
    let result = longest(string1, string2);
    println!("The longer string is: {}", result);
}
```

---
