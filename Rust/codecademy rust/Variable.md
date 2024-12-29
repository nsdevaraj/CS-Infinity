

Variables are **identifiers** pointing to a memory location, used to store data or functions. By default, they are **immutable** unless explicitly marked mutable.

---

### **Variable Declaration**

Use the `let` keyword to declare variables:

```rust
let variable = "this is a &str";
```

#### Example:

```rust
let double = |d| d * 2;  // A closure
let var = double(10);    // Call the func/closure and store return value
let doubled_var = var;   // assign and reassign value
```

---

### **Type Inference**

Rust infers types based on context.

- **Default Types:**
    - Integers: `i32`
    - Floats: `f64`

#### Examples:

```rust
let integer = 10;       // `i32`
let float = 1.2;        // `f64`

fn double(num: u128) -> u128 {
    num * 2
}
let stars = 10;         // Inferred as `u128`
```



To find type of any variable : 

Note: This unstable func only avail on Nighty versions

```rust

#![feature(core_intrinsics)]

fn print_type_of<T>(_: &T) {
    println!("{}", unsafe { std::intrinsics::type_name::<T>() });
}
```



Type inference by rust automatically:

```rust
#![allow(unused)]
#![feature(core_intrinsics)]

fn print_type_of<T>(_: &T) {
    println!("{}", unsafe { std::intrinsics::type_name::<T>() });
}

fn main() {
	let stars = 10; 
	print_type_of(&stars); //=> i32

}
```



```rust

#![allow(unused)]
#![feature(core_intrinsics)]


fn print_type_of<T>(_: &T) {
    println!("{}", unsafe { std::intrinsics::type_name::<T>() });
}

fn main() {
	let stars = 10; 
	print_type_of(&stars); //=> u128
	
	fn double(num: u128) -> u128 { num * 2 }
	double(stars);
}

```





---

### **Type Annotation**

Specify types explicitly with `: Type`:

```rust
let small_integer: u16 = 28;
let unsigned_int: u8 = 28;
```

---

### **Shadowing**

Shadowing allows reusing the same variable name within the same scope, creating a new variable:

```rust
let color = "orange";
let color = "blue"; // Shadows the previous `color`
println!("{color}"); // Outputs: blue
```

---

### **Pattern Binding**

let also do pattern binding.. Bind multiple variables with tuples or arrays:

```rust
let (a, b) = (10, "pie");                 // Tuple
let [x, y, z] = ["arrays", "are", "fun"]; // Array
```

---

### **Unused Variables**

Suppress unused variable warnings by prefixing with `_`:

```rust
let _unused = "ignored";
let _used = "visible";
println!("{_used}");
```

---

### **Other Highlights**

1. **Mutability:**
    
    ```rust
    let mut counter = 0; 
    counter += 1; // Mutable variable
    ```
    
2. **Constants:**  
    Use `const` for unchanging values:
    
    ```rust
    const PI: f64 = 3.1415;
    ```
    
3. **Static Variables:**  
    Declared with `static` and have a `'static` lifetime:
    
    ```rust
    static MAX: u32 = 100;
    ```
    

---


