

### **Statements**

A **statement** is a piece of code that **performs an action but does not return a value**. Statements often end with a semicolon (`;`).

#### **Examples**

1. **Literal Statement**

```rust
// This is a statement, but its value is not accessible.
"purple";
```

2. **Let Statement**  
    The `let` keyword creates a variable but does not return a value:

```rust
// The variable `answer` holds the value "purple".
let answer = "purple";
```

3. **Function or Macro Without Return**  
    Functions or macros that do not return a value are also considered statements:

```rust
fn say_answer() {
    let answer = "purple";
    println!("{answer}");
}
```

> **Note**: The final line in a function doesn’t need a semicolon if the line itself is a statement, such as the `println!` macro above.

#### **Key Rule**

Statements **do not return values**, so you cannot use them directly in contexts requiring a value.

---

### **Expressions**

An **expression** is a block of code that **evaluates to a value**. Rust is an expression-oriented language, meaning most operations, including blocks and control flows, are expressions.

#### **Examples**

1. **Simple Expression**

```rust
// This expression evaluates to the string slice "green".
"green"
```

2. **Function or Macro Returning a Value**

```rust
fn give_answer() -> String {
    let answer = "green".to_string();
    answer // Implicitly returns the value of `answer`
}

// Output: "green"
println!("{}", give_answer());
```

3. **Control Flow as Expressions**  
    Control flow constructs, like `if`, `match`, and blocks, are expressions in Rust:

```rust
let condition = true;
let number = if condition { 5 } else { 10 }; // Returns 5 or 10 based on condition
println!("The number is {number}");
```


```rust
fn main(){
    
    let value = if true { 
        let new_val = 3 + 2;
        
//         return new_val;
//          fn main(){
//             - expected `()` because of default return type

         new_val
    }else{
         0
    };
    
    println!("{:?}", value); // => 5

}
```

4. **Expression Without Semicolon**  
    The absence of a semicolon means the value is returned:

```rust
let sum = {
    let x = 2;
    let y = 3;
    x + y // No semicolon, so this block returns `x + y`
};
println!("The sum is {sum}"); // Output: "The sum is 5"
```

#### **Key Rule**

Expressions **return values**, making them reusable and composable.

---

### **Patterns**

Patterns are a powerful and flexible way to **deconstruct and match values** in Rust. They allow for elegant and concise code in variable assignments, function parameters, and control flows.

#### **Examples of Patterns**

1. **Destructuring in Let Statements**  
    Patterns can declare multiple variables at once:

```rust
let (x, y) = (5, 10); // `x` is 5, `y` is 10
println!("x = {x}, y = {y}");
```

2. **Pattern Matching with `match`**  
    The `match` expression allows matching complex patterns:

```rust
let point = (3, 5);
match point {
    (0, y) => println!("On the y-axis at {y}"),
    (x, 0) => println!("On the x-axis at {x}"),
    (x, y) => println!("On neither axis: ({x}, {y})"),
}
```

3. **Function Parameters**  
    Patterns can simplify function signatures:

```rust
fn print_point((x, y): (i32, i32)) {
    println!("Point is at ({x}, {y})");
}
print_point((3, 7)); // Output: "Point is at (3, 7)"
```

4. **Using Wildcards (`_`)**  
    Ignore specific values with `_`:

```rust
let (x, _) = (42, 99); // Only `x` is bound
println!("x = {x}"); // Output: "x = 42"
```


```rust
fn main(){
    let (_, a, _,_) = (42, 99, 100,101); // Only `a` is bound
    println!("a = {a}");  //=> a = 99
}
```


#### **Advanced Patterns**

Patterns can also destructure enums, arrays, and more:

```rust
enum Direction {
    Up,
    Down,
    Left(i32),
    Right(i32),
}

let dir = Direction::Left(10);

match dir {
    Direction::Up => println!("Moving up"),
    Direction::Left(distance) => println!("Moving left {distance} units"),
    _ => println!("Other direction"),
}
```


more:  https://doc.rust-lang.org/reference/patterns.html#identifier-patterns



---

### **Key Takeaways**

- **Statements** perform actions but do not return values.
- **Expressions** evaluate to values and are fundamental to Rust’s syntax.
- **Patterns** simplify deconstruction and matching, making code concise and readable.




