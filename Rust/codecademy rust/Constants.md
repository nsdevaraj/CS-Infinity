

## Constants in Rust

### **What Are Constants?**

In Rust, constants are immutable values defined using the `const` keyword. Unlike variables, constants are always evaluated at compile time and cannot be changed once defined. They provide a reliable way to declare values that are fixed and reused throughout a program.

### **Key Features of Constants**

1. **Immutability**:
    
    - Constants are always immutable, meaning their value cannot be altered once assigned.
2. **Compile-Time Evaluation**:
    
    - The value of a constant must be known and evaluated at compile time. Any runtime computation or function call is not allowed in constant definitions.
3. **Global Scope**:
    
    - Constants have a `'static` lifetime, making them accessible throughout the entire program where their visibility permits.
4. **Explicit Type Annotation**:
    
    - Constants require explicit type annotations. The compiler does not infer the type.
5. **No Memory Address**:
    
    - Constants are inlined wherever they are used, so they do not occupy a fixed memory address.
6. **SCREAMING_SNAKE_CASE**:
    
    - By convention, constant names are written in SCREAMING_SNAKE_CASE.

### **Syntax**

```rust
const NAME: TYPE = VALUE;
```

### **Examples**

1. **Basic Constant**:
    
    ```rust
    const PI: f64 = 3.14159;
    const MAX_USERS: u32 = 1000;
    ```
    
2. **Expressions in Constants**:
    
    ```rust
    const SECONDS_IN_A_MINUTE: u32 = 60;
    const SECONDS_IN_AN_HOUR: u32 = SECONDS_IN_A_MINUTE * 60;
    ```
    
3. **String Constant**:
    
    ```rust
    const GREETING: &str = "Hello, Rust!";
    ```
    
4. **Array Constant**:
    
    ```rust
    const NUMBERS: [i32; 4] = [1, 2, 3, 4];
    ```



### **Constants vs Variables vs** `**static**`

|**Feature**|**Constants (**`**const**`**)**|**Variables (**`**let**`**)**|**Static Variables (**`**static**`**)**|
|---|---|---|---|
|**Mutability**|Always immutable|Immutable by default; mutable with `mut`|Immutable by default; `mut` allowed with `unsafe`|
|**Declaration Keyword**|`const`|`let`|`static`|
|**Shadowing**|Cannot be shadowed|Can be shadowed|N/A|
|**Scope**|Global or local|Limited to their scope|Global|
|**Evaluation**|Compile-time only|Can be runtime|Compile-time or runtime|
|**Type Annotation**|Required|Optional (inferred)|Required|
|**Memory Location**|Inlined wherever used|Stack (or heap if boxed)|Single memory location|


### **Advanced Features of Constants**

#### **Constant Functions (`const fn`):**

Rust allows the use of functions within constant expressions if they are marked with the `const fn` keyword. These functions must not have side effects and must rely only on compile-time evaluable expressions. (`pure func`)

**Example:**

```rust
const fn square(x: u32) -> u32 {
    x * x
}

const AREA: u32 = square(4);

fn main() {
    let perimeter = square(5); // Can also be used at runtime
    println!("Area: {}, Perimeter: {}", AREA, perimeter);
}
```

#### **Associated Constants:**

Constants can be associated with traits and types, making them useful in defining domain-specific constants.

**Example:**

```rust
trait Shape {
    const SIDES: u32;
}

struct Square;

impl Shape for Square {
    const SIDES: u32 = 4;
}

fn main() {
    println!("A square has {} sides.", Square::SIDES);
}
```

### **Best Practices**

1. **Use Constants for Fixed Values:**
    
    - Define values that are reused and remain the same throughout the program.
    - Example:
        
        ```rust
        const LIGHT_SPEED: u32 = 299_792_458; // Speed of light in m/s
        ```
        
2. **Follow Naming Conventions:**
    
    - Use SCREAMING_SNAKE_CASE for constant names to distinguish them from variables.
3. **Prefer `const` Over `static` When Possible:**
    
    - Use `const` for compile-time evaluable values and avoid potential unsafe behavior of mutable static variables.
4. **Replace Magic Numbers with Constants:**
    
    - Avoid using unexplained numbers directly in your code by giving them meaningful names as constants.
5. **Leverage `const fn` for Reusable Computations:**
    
    - Encapsulate constant expressions in functions for readability and reuse.

### **Limitations**

1. **No Runtime Computations:**
    
    - Constants cannot rely on runtime inputs or operations.
    
    **Invalid:**
    
    ```rust
    const INVALID: u32 = get_number(); // Error: get_number is not a constant function
    ```
    
2. **Limited to Simple Data Types:**
    
    - Constants must have types with a fixed size known at compile time.
    
    **Invalid:**
    
    ```rust
    const NAME: String = String::from("Rust"); // Error: String size is not fixed
    ```
    

### **Conclusion**

Constants in Rust provide a robust and efficient way to define immutable, reusable values that enhance code readability and safety. By adhering to best practices and understanding their limitations, you can effectively leverage constants to write clean and maintainable Rust programs.


to check {


https://github.com/rust-lang/rust/issues/76560

https://doc.rust-lang.org/stable/reference/items/associated-items.html#associated-constants





}