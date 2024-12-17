
A **reference** is a way of **pointing to data in memory** without taking ownership. It allows us to reuse existing data efficiently and helps make Rust memory-safe and performant.

---

### **Creating References (`&`)**

To create a reference, use the `&` prefix. References **borrow** data instead of owning it.

#### **Example: Basic Reference**

```rust
let pi = 3.14159265359;  
let funny_number = &pi; // `funny_number` references `pi`  
println!("{funny_number}"); // Prints "3.14159265359"
```

#### **References to References**

Rust allows references to references (nested borrowing):

```rust
let lightspeed = 299792458;

let fast = &lightspeed;       // Reference
let still_fast = &&lightspeed; // Reference to a reference

let speed_of_light = &still_fast; // Equivalent to &&&lightspeed
```

---

### **Dereferencing (`*`)**

To access the **value** ( underlying data ) a reference points to, use the `*` operator:

#### **Example: Dereferencing**

```rust
let mut year = 3020;
let y = &mut year; // Mutable reference  

*y += 10; // Dereference to modify the value  
println!("The year is {year}"); // Prints "The year is 3030"
```

---

### **Automatic Dereferencing**

Rust **automatically dereferences** references when using the `.` operator for method calls.

#### **Example**

```rust
let planet = "Earth";
let earth = &&&&planet; // Deeply nested reference  

assert_eq!("EARTH", earth.to_uppercase()); // Compiler auto-dereferences `earth`
```

---

### **`ref` Keyword**

The `ref` keyword allows us to create a reference during **pattern matching**. It is used when borrowing inner values.

#### **Example: Using `ref` in Patterns**

```rust
let starship: Option<String> = Some("Omaha".to_string());

match starship {
    Some(ref name) => println!("{}", name), // Borrowing inner value
    None => {}
}

// `starship` remains accessible since we only borrowed it
println!("{:?}", starship); // Prints "Some("Omaha")"
```

#### **Mutable References with `ref mut`**

To borrow mutably inside patterns, use `ref mut`:

```rust
let mut planet: Option<String> = Some("Waleco".to_string());

match planet {
    Some(ref mut name) => {
        name.push('8'); // Modify borrowed data
    }
    None => {}
}

println!("{:?}", planet); // Prints "Some("Waleco8")"
```

#### **Reciprocal Nature of `&` and `ref`**

`ref` behaves like the reciprocal of `&` when assigning:

```rust
let val = "reciprocal";

let ref r1 = val; // Creates a reference
let r2 = &val;    // Equivalent to above

assert_eq!(r1, r2); // Both are references to `val`
```


For quickly accessing inner values with a method, such as when attempting to use an `&Option<T>` as an `Option<&T>`, check out the [`as_ref()`](https://doc.rust-lang.org/std/convert/trait.AsRef.html#tymethod.as_ref) method.


---

### **Slices**

A **slice** is a reference to a portion of a collection. Slices allow accessing part of data without copying it.

#### **Example: String Slices**

```rust
let s = String::from("hello world");

let hello = &s[0..5]; // Slice of "hello"
let world = &s[6..11]; // Slice of "world"

println!("{hello}{world}"); // Prints "helloworld"
```

- **Omitting Index Bounds**:
    - `&s[..5]` is equivalent to `&s[0..5]`.
    - `&s[6..]` slices to the end of the collection.


more about arrays and vectors : https://www.codecademy.com/courses/rust-for-programmers/articles/arrays-and-vec


---

### **Key Points**

1. **References**: Use `&` to borrow data.
2. **Dereferencing**: Use `*` to access or modify referenced values.
3. **Automatic Deref**: The `.` operator automatically dereferences.
4. **`ref` and `ref mut`**: Useful in pattern matching for borrowing inner values.
5. **Slices**: References to a subset of a collection.

Rust’s **ownership and borrowing** rules, combined with references, make it easy to work with data efficiently and safely! 🚀


```rust
fn main{
    let planet = "Earth";
    let earth = &&&&planet;

    println!("{}", earth); //=> Earth
    println!("{}", *earth); //=> Earth
    println!("{}", ****earth); //=> Earth

    // println!("{}", *****earth);
    //: error[E0277]: the size for values of type `str` cannot be known at compilation time

    // 1. Basic Reference and Dereferencing
    let number = 42;
    let number_ref = &number; // Immutable reference
    println!("Number via reference: {}", number_ref); //=> Number via reference: 42

    // 2. Mutable Reference
    let mut year = 2024;
    let year_ref = &mut year;
    *year_ref += 1; // Dereference to modify value
    let planet = "Earth";
    println!("Next year: {}", year); //=> Next year: 2025

    // 3. ref and ref mut in Pattern Matching
    let starship = Some(String::from("Enterprise"));
    match starship {
        Some(ref name) => println!("Starship name: {}", name), // Borrow inner value
        //=> Starship name: Enterprise
        None => println!("No starship"),
    }

    let mut planet = Some(String::from("Earth"));
    match planet {
        Some(ref mut name) => name.push_str(" 2.0"), // Correct syntax for push_str
        None => println!("No planet"),
    }
    println!("Planet after update: {:?}", planet);
    //=> Planet after update: Some("Earth 2.0")

    // 4. Nested References and Automatic Deref
    let galaxy = "Milky Way";
    let nested_ref = &&&&galaxy; // Deep reference
    println!("Galaxy name: {}", nested_ref.to_uppercase()); // Auto-dereference

    //=> Galaxy name: MILKY WAY

    // 5. Slices
    let greeting = String::from("hello world");
    let hello = &greeting[..5]; // Slice: "hello"
    let world = &greeting[6..]; // Slice: "world"
    println!("Greeting split: {} {}", hello, world);
    //=> Greeting split: hello world
}
```


handsOn: [[Refs]]
