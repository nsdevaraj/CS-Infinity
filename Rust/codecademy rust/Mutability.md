

_Mutability_ is the capability of a variable’s value to be altered in memory.



### Mutability in Rust

Rust enforces **immutability by default** for variables, a design choice that prioritizes safety, predictability, and concurrency. Mutability must be explicitly enabled using the `mut` keyword.

---

### **Key Principles**

1. **Default Immutability**:
    
    - Variables are immutable unless declared with `mut`.
    - Helps prevent unintended data changes and simplifies reasoning about code.
    
    Example:
    
    ```rust
    let x = 3; // Immutable
    x = 5;     // Compile-time error
    ```
    
2. **Declaring Mutability**:
    
    - Use `mut` to allow variable modification.
    
    ```rust
    let mut x = 5; // Mutable
    x += 1;        // Allowed
    ```
    
3. **Variable-Level Mutability**:
    
    - Mutability applies to the variable, not individual fields within a structure.
    
    ```rust
    struct Coordinate { x: i32, y: i32 }
    let mut point = Coordinate { x: 10, y: 20 };
    point.x = 15; // Allowed because `point` is mutable
    ```
    
4. **Shadowing as an Alternative**:
    
    - Instead of mutating, you can "shadow" a variable to assign a new value.
    - Shadowing avoids mutability but increases memory usage due to reallocation.
    
    ```rust
    let number = 10;
    let number = number + 10;
    println!("{number}"); // Output: 20
    ```
    

---

### **Mutable References**

1. **Creating Mutable References**:
    
    - Use `&mut` to borrow data mutably.
    
    ```rust
    fn modify(s: &mut String) {
        s.push_str(" World!");
    }
    
    let mut greeting = String::from("Hello");
    modify(&mut greeting);
    println!("{greeting}"); // Output: Hello World!
    ```
    
2. **Borrowing Rules**:
**Borrowing and Ownership:** Rust's ownership system is closely tied to mutability.

- **Borrowing:** You can borrow a reference to an immutable variable (`&x`) or a mutable variable (`&mut x`).
- **Rules:**
    - Only one mutable borrow is allowed at a time.
    - Multiple immutable borrows are allowed simultaneously.
    - Mutable borrows cannot coexist with any other borrows.


    - Only **one mutable reference** to data is allowed at a time.
    - Mutable and immutable references cannot coexist.
    
    ```rust
    let mut sentence = String::from("Hello");
    let immutable_ref = &sentence;  // Immutable reference
    let mutable_ref = &mut sentence; // Compile-time error
    ```
    


```rust
fn main() {
    let mut x = 5; 

    {
        let y = &mut x; // Mutable borrow of x
        *y += 1; 
    } 

    println!("{}", x); // Output: 6
}
```


### Mutable References: Borrowing Rules

In Rust, **only one mutable reference** to a piece of data is allowed at a time. Additionally, you **cannot immutably borrow** data while a mutable reference exists.

#### Example:

```rust
let mut sentence = String::from("Take care, take care.");
let immutable_reference = &mut sentence;

// This is valid because `immutable_reference` is used first
println!("{}", immutable_reference);

// Attempting to use `sentence` here will cause a compile-time error
// println!("{}", sentence); // Error: cannot use `sentence` while it is mutably borrowed
```

#### **Error Breakdown:**

1. **Ownership Rules:**
    - A mutable borrow (`&mut`) grants exclusive access to the data.
    - Other references (mutable or immutable) cannot coexist during this borrow.
2. **Fix:** Ensure the mutable reference is dropped (used or no longer needed) before accessing the original data.

```rust
let mut sentence = String::from("Take care, take care.");
let mutable_reference = &mut sentence;
println!("{}", mutable_reference); // Mutable borrow used here

println!("{}", sentence); // Now valid, mutable reference no longer in use
```

We can only have one mutable reference to a piece of data at a time. This means we cannot immutably borrow a mutable reference outside the [lifetime](https://www.codecademy.com/courses/rust-for-programmers/articles/lifetimes-rust) of the mutable reference.


---

### **Interior Mutability**

For cases where mutability is needed inside an immutable structure, Rust provides **interior mutability** via types like `std::cell::Cell` and `std::cell::RefCell`.

1. **Example with `RefCell`:**
    
    ```rust
    use std::cell::RefCell;
    
    struct Data {
        value: RefCell<i32>,
    }
    
    let data = Data { value: RefCell::new(10) };
    *data.value.borrow_mut() += 5;
    println!("{}", data.value.borrow()); // Output: 15
    ```
    
2. **Warnings**:
    
    - Interior mutability bypasses compile-time checks, potentially leading to **runtime errors** like multiple mutable borrows.


Allowing mutability of a field when our data structure is otherwise immutable is called “Interior Mutability.” Rust’s std library provides us the `std::cell::Cell` and `std::cell::RefCell` types which allow this capability.

Be warned that these types can circumvent compile-time guarantees and generate runtime errors when not used properly. The [`std::cell` documentation](https://doc.rust-lang.org/std/cell/index.html) has more information about its implications.


---

### **Advantages of Immutability**

1. **Safety**: Prevents unexpected state changes.
2. **Concurrency**: Reduces data race risks.
3. **Clarity**: Makes reasoning about program state easier.

### **When to Use Mutability**

1. **Performance**: When avoiding unnecessary reallocations is critical.
2. **Complex State**: When shadowing leads to convoluted code.




---




---

### Shadow vs mut

### Question:

In Rust, variables without the `mut` keyword can't be mutated. However, I can use shadowing with the same variable name to mimic mutation. Am I correct, and what are your thoughts on this?

### Answer:

Yes, you're correct! Shadowing in Rust allows you to redefine a variable with the same name, mimicking mutation without using `mut`.


This allows us to avoid the complexity of mutability but at the cost of extra memory allocation.

Here's the distinction:

1. **Shadowing**:
    
    - Creates a new variable, hiding the previous one.
    - Useful for transformations or changing variable types.
    - Example:
        
        ```rust
        let x = 5;
        let x = x + 1; // new `x` shadows the old one
        println!("{}", x); // prints 6
        ```
        
2. **Mutation (`mut`)**:
    
    - Modifies the value of the same variable in place.
    - Example:
        
        ```rust
        let mut x = 5;
        x += 1;
        println!("{}", x); // prints 6
        ```
        

### Thoughts:

- **Advantages of Shadowing**:
    - Aligns with Rust's immutability-by-default philosophy.
    - Allows type changes:
        
        ```rust
        let x = "123"; 
        let x: i32 = x.parse().unwrap();
        ```
        
- **Downsides**:
    - May reduce readability due to variable redefinition.

Shadowing is great for functional-style transformations, but for in-place updates, `mut` is clearer. Use each tool where it fits best!

---

### **Key Principles of Mutability**

1. **Default Immutability**: By default, all variables in Rust are immutable. This means that once a variable is assigned a value, that value cannot be changed unless explicitly declared as mutable using the `mut` keyword. For example:
   ```rust
   let x = 1; // Immutable
   x = 2; // This will cause a compile error!
   ```

2. **Declaring Mutable Variables**: To allow for changes, you must declare a variable as mutable:
   ```rust
   let mut x = 1; // Mutable
   x = 2; // This is allowed!
   ```

3. **Mutability at the Variable Level**: Unlike some languages where individual fields can be mutable or immutable, in Rust, mutability applies to the entire variable. If a variable is mutable, you can modify any of its fields (if they themselves are not immutable):
   ```rust
   struct Dog {
       name: &'static str,
       age: usize,
   }

   let mut harris = Dog { name: "Harris", age: 0 };
   harris.age += 1; // Allowed because `harris` is mutable.
   ```

4. **Immutable References**: When you pass references to data, you can specify whether those references are mutable or immutable. An immutable reference does not allow you to change the data it points to:
   ```rust
   fn get_friends(&self) -> &Vec<Dog> {
       &self.friends // Immutable reference
   }
   ```

5. **Unique Mutable References**: Rust enforces strict borrowing rules to ensure safety. You can only have one mutable reference to a piece of data at any time, which prevents data races:
   ```rust
   let mut harris = Dog { name: "Harris", age: 0 };
   let friends = harris.get_friends(); // Immutable reference
   friends.push(Dog { name: "Buck", age: 1 }); // Compile error!
   ```


---



to check {

https://doc.rust-lang.org/std/cell/index.html


}