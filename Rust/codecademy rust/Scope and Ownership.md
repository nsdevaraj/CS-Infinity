


Rust’s **scope** and **ownership** concepts are at the heart of its **memory safety** guarantees. Let’s break these down clearly with concise explanations and examples.

The main goal of Rust is to avoid memory-based errors, so strict scoping rules allow the compiler to know when memory can safely be accessed.


---

### **Blocks**

A **block** in Rust is a collection of **statements** and an optional **expression** enclosed within `{}`.

#### **Examples**

1. **Statement Block**

```rust
{
    let a = 10;
    let b = 20;
    let sum = a + b;
    println!("{sum}");
}
```

2. **Expression Block**
Blocks can be treated as the single statement or expression they evaluate to.

```rust
let sum = {
    let a = 10;
    let b = 20;
    a + b // Last line without `;` returns the value
};

println!("Sum is {sum}"); // Output: "Sum is 30"
```

3. **Functions as Blocks**  
    Functions in Rust are named, callable blocks:

```rust
fn add() -> i32 {
    let a = 10;
    let b = 20;
    a + b
}

println!("Sum is {}", add()); // Output: "Sum is 30"
```

---

### **Scope**

**Scope** determines where an item exists in memory and whether it can be accessed.

In Rust, the scope of any particular item is limited to the block it is contained in.

- When a block ends, all values defined in it are **dropped** and considered **out-of-scope**.

#### **Example: Variable Shadowing**

```rust
let number = 10; // Outer scope

{
    println!("{number}"); // Prints "10"
    let number = 22; // Shadows `number` in this block
    println!("{number}"); // Prints "22"
} // Inner `number` goes out of scope here

println!("{number}"); // Prints "10"
```


- Shadowing allows us to declare new variables with the same name within nested scopes.

---

### **Visibility**

Rust items are **private** by default. To expose them outside of their scope, we use the `pub` keyword.

Private items can only be accessed within their declared module and any children modules.

Fields of complex datatypes have their own visibility qualifiers. like Struct.. 

#### **Example: Public Constants and Structs**

```rust
mod numbers {
    pub const ZERO: i32 = 0; // Public constant
}

pub struct Number {
    pub value: i32, // Public field
}

fn main() {
    let num = Number { value: 5 };
    println!("Value is {}", num.value); // Accessible due to `pub`

    println!("Zero is {}", numbers::ZERO); // Accessible due to `pub`
}
```

- Use the `pub` keyword for modules, fields, and constants to make them publicly accessible.

When our crate is a library, all items denoted as public will be accessible to anyone who imports our library

modules - https://www.codecademy.com/courses/rust-for-programmers/articles/modules-rust


---

### **Ownership**

Rust’s ownership system ensures **memory safety** without garbage collection.

Managing [lifetimes](https://www.codecademy.com/courses/rust-for-programmers/articles/lifetimes-rust) and [mutability](https://www.codecademy.com/courses/rust-for-programmers/articles/mutability-rust) in a memory-safe way is much easier when we disallow accessing items from parent blocks.


#### **Ownership Rules**

1. Each value in Rust has a variable that’s called its owner.
2. There can only be one owner at a time.
3. When the owner goes out of scope, the value will be dropped.

---

### **Stack vs Heap**

#### **Stack-Based Types**

For **stack-based** types like `i32`, assigning one variable to another **copies** the value.
( primitive normal types are stack )

```rust
let x = 10;
let y = x; // Copy occurs
println!("x = {x}, y = {y}"); // Both x and y are usable
```

#### **Heap-Based Types**

For **heap-based** types like `String`, assigning one variable to another **moves** the ownership.
( collections types are heap )


```rust
let s1 = String::from("hello");
let s2 = s1; // Ownership moves to s2

// println!("{s1}"); // Error: s1 is no longer valid
println!("{s2}"); // Works
```

When working with datatypes that utilize the heap, such as `String`, we cannot copy values from one variable to another since heap-based types do not implement the [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html) trait. Instead of copying, Rust will instead move the value out of the original variable and into the new one.

When we are not in need of a separate copy, we can instead [reference](https://www.codecademy.com/courses/rust-for-programmers/articles/references-rust) the data.
#### **Cloning Heap Data**

To create an explicit copy of heap-based data, use `.clone()`.

```rust
let s1 = String::from("hello");
let s2 = s1.clone(); // Creates a deep copy

println!("{s1}"); // Both s1 and s2 are valid
println!("{s2}");
```

---

### **Ownership in Functions**

1. **Passing Ownership**  
    Ownership transfers when values are passed into a function:

```rust
fn take_ownership(s: String) {
    println!("{}", s);
} // `s` is dropped here

let s = String::from("hello");
take_ownership(s); // `s` is moved to the function

// println!("{s}"); // Error: `s` no longer valid
```

2. **Returning Ownership**  
    Functions can return ownership back to the caller:

```rust
fn return_ownership() -> String {
    let s = String::from("hello");
    s // Ownership returned
}

let s = return_ownership();
println!("{s}");
```

3. **Passing by Reference**  
    To avoid transferring ownership, use references (`&`):

```rust
fn borrow_string(s: &String) {
    println!("{}", s);
}

let s = String::from("hello");
borrow_string(&s); // Pass a reference
println!("{s}"); // Still valid
```

---

### **Key Takeaways**

1. **Scope**: Values exist only within their block.
2. **Visibility**: Use `pub` to expose items publicly.
3. **Ownership**:
    - Values have one owner at a time.
    - Stack types are copied; heap types are moved.
    - Use `.clone()` for explicit deep copies.
4. **References**: Use `&` to borrow data without transferring ownership.

Rust’s ownership system ensures **safe, efficient memory management** while avoiding common pitfalls like dangling pointers and memory leaks.



more about ownership : https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html


