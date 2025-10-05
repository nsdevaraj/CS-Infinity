
# C vs Rust strings


## 🧵 1. **Representation**

|Language|String Type|Description|
|---|---|---|
|**C**|`char *`|A pointer to a null-terminated array of bytes (`\0` marks the end)|
|**Rust**|`String`, `&str`|UTF-8 encoded, explicitly sized — **no null termination**|

---

## 🔒 2. **Safety & Bounds Checking**

|Language|Behavior|
|---|---|
|**C**|Strings are **unsafe**: no bounds checking, easy to cause buffer overflows|
|**Rust**|Strings are **memory safe**: bounds-checked, type-safe, and no dangling pointers|

> Rust won’t compile code that might lead to memory corruption — C will.

---

## 🧠 3. **Types & Ownership**

### C:

- `char *s = "hello";` → string literal (read-only)
    
- `char s[] = "hello";` → mutable buffer
    

### Rust:

- `&str` = string **slice** (borrowed, read-only): `"hello"`
    
- `String` = **owned**, growable string: `"hello".to_string()`
    

|Rust Type|Description|
|---|---|
|`&str`|Borrowed, immutable view of a string (stored on the stack or in static data)|
|`String`|Owned, heap-allocated, mutable, and growable UTF-8 string|

---

## 📏 4. **Mutability**

|Language|Mutability|
|---|---|
|**C**|Strings are arrays of `char`; mutability depends on how you define them|
|**Rust**|Mutability is enforced via the `mut` keyword and ownership system|

Example:

```rust
let mut s = String::from("hi");
s.push('!');
```

---

## 🌐 5. **Encoding**

|Language|Encoding|
|---|---|
|**C**|Bytes — typically ASCII, or manually managed encodings|
|**Rust**|Always **valid UTF-8** — required by the `String` and `&str` types|

Rust won’t let you create invalid UTF-8 `String`s without using unsafe code.

---

## 🧹 6. **Memory Management**

|Language|Memory Control|
|---|---|
|**C**|Manual: you must allocate (`malloc`) and free (`free`)|
|**Rust**|Automatic via **ownership and RAII** — memory is freed when the variable goes out of scope|

---

## 🛠️ 7. **String Operations**

- **C**:
    
    - Manual: `strcpy`, `strlen`, `strcat` — and lots of risk
        
- **Rust**:
    
    - Safe, built-in methods: `.len()`, `.push()`, `.replace()`, `.split()`, etc.
        
    - Must handle UTF-8 properly
        

---

## 🛡️ 8. **Null-Termination vs Length-based**

|Feature|C|Rust|
|---|---|---|
|End of string|`\0` null byte|Tracked length|
|Cost|Linear (must scan)|Constant time (stored length)|

---

## 🔚 Summary Table

|Feature|C|Rust|
|---|---|---|
|Type|`char*`, `char[]`|`&str`, `String`|
|Encoding|Raw bytes / ASCII|UTF-8|
|Termination|Null (`\0`)|Length-based|
|Mutability|Depends|Explicit via `mut`|
|Memory Mgmt|Manual|Ownership + RAII|
|Safety|Unsafe by default|Memory-safe by default|
|Slicing|Manual pointer math|Safe slices|

---



# String vs &str


## 🧬 Overview

|Feature|`String`|`&str`|
|---|---|---|
|Type|**Owned**, heap-allocated string|**Borrowed** string slice|
|Mutability|Mutable (if declared `mut`)|Immutable|
|Memory|Heap|Stack (or points to heap/static)|
|Length|Stored|Stored|
|Encoding|UTF-8|UTF-8|

---

## 📦 `String`: Owned, Growable

```rust
let mut s = String::from("hello");
s.push('!');
```

### Characteristics:

- Stored on the **heap**
    
- **Owns** its data — responsible for freeing memory
    
- Can **grow/shrink** (mutable buffer)
    
- Often created from `&str`:
    
    ```rust
    let s: String = "hello".to_string();
    ```
    

### When to use:

- When you **need to modify** the string
    
- When you need to **own** the data (e.g., storing in a struct)
    
- When you're **building strings dynamically**
    

---

## 📎 `&str`: Borrowed, Fixed

```rust
let s: &str = "hello"; // string literal
```

### Characteristics:

- A **view** into a string — doesn't own the data
    
- Often points to:
    
    - A string literal (`&'static str`)
        
    - A slice of a `String`
        
- **Immutable**
    
- Efficient: no allocation, just a pointer and length
    

### When to use:

- When **reading or referencing** string data
    
- When **passing** string data to functions without taking ownership
    
- For **literal values**: `"hello"` is of type `&'static str`
    

---

## 🔁 Conversions

### `&str` ➡️ `String`

- Clones the data to the heap:
    
    ```rust
    let s: &str = "hi";
    let owned: String = s.to_string();
    ```
    

### `String` ➡️ `&str`

- Cheap slice:
    
    ```rust
    let s: String = String::from("hi");
    let slice: &str = &s;
    ```
    

---

## 🚫 Mutability Rules

- `&str` is **always immutable**
    
- `String` is **mutable only if declared `mut`**
    

```rust
let s = String::from("hello");
s.push('!');        // ❌ error: s not mutable

let mut s = String::from("hello");
s.push('!');        // ✅ works
```

---

## 🧠 Memory & Performance

|Feature|`String`|`&str`|
|---|---|---|
|Allocation|Heap|None (just view)|
|Lifetime|`'static` (if literal), or tied to source|Tied to source|
|Cost|More (allocation, copying)|Very low (slicing)|

---

## 📘 Summary

|Category|`String`|`&str`|
|---|---|---|
|Ownership|Owns data|Borrows data|
|Storage|Heap|Stack or reference|
|Growable|Yes|No|
|Mutable|Yes (if declared `mut`)|No|
|Use when...|You need to build, store, or own strings|You only need to read/view data|

---

## 🛠️ Pro Tip:

Functions should **usually accept `&str`** for flexibility:

```rust
fn greet(name: &str) {
    println!("Hello, {name}!");
}
```

This allows the function to take both `String` and `&str` as arguments.


> **How can a function that takes `&str` also accept a `String` as an argument?**

This is possible because of **Rust's deref coercion** — a powerful feature that automatically converts a `String` to `&str` when needed.

---

## ✅ Example

```rust
fn greet(name: &str) {
    println!("Hello, {name}!");
}

fn main() {
    let s1 = "Alice";                  // &str
    let s2 = String::from("Bob");      // String

    greet(s1);     // passes &str
    greet(&s2);    // passes &String, coerced to &str
}
```

---

## 🔍 Why does this work?

### Because `String` implements:

```rust
impl Deref for String {
    type Target = str;

    fn deref(&self) -> &str {
        // behind the scenes, returns &self[..]
    }
}
```

So when a function expects a `&str` and you pass a `&String`, Rust automatically:

```rust
&String => &str   // via deref coercion
```

---

## 🔁 Summary

|Passed Type|Function Param|Works?|Why|
|---|---|---|---|
|`&str`|`&str`|✅|Direct match|
|`String`|`&str`|✅|Auto `&s` + deref coercion|
|`&String`|`&str`|✅|Deref coercion|
|`String`|`String`|✅|Owns the value|
|`&str`|`String`|❌|Cannot coerce borrowed to owned|

---

## 🧠 Best Practice

Write functions like this:

```rust
fn do_something(text: &str) {
    // Can take both &str and String
}
```

Unless you **need ownership**, then take `String`.

---




to check :

nice one - all string types  
https://youtu.be/CpvzeyzgQdw




