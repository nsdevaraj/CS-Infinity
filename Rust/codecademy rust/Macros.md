### Macros in Rust: 

Macros in Rust are powerful **metaprogramming tools** that allow developers to write code that generates other code. This capability enhances efficiency by abstracting repetitive patterns and enabling custom syntax and behavior.

---

### What Are Macros?

Macros in Rust operate at the **syntax level**, transforming input tokens into Rust code during the compilation phase. Unlike functions, macros do not execute at runtime but instead generate code before compilation begins.

Unlike functions, the input of the body of a macro call is arbitrary. The macro author has complete control over the syntactical bits of the language down to individual tokens.

When calling function-like macros, we can denote the body of the macro with `()`, `[]`, or `{}` interchangeably.

```rust
// Macros utilizing `[]` are conventionally used for collections.
let clouds = vec![12, 97, 24];

// `rustfmt` will not format macros that utilize `{}`
let today = println! {
  "Look up
toward the sky,
it's a beautiful day."

};
```

---

### Types of Macros in Rust

#### 1. **Declarative Macros (`macro_rules!`)**

Declarative macros are defined using `macro_rules!` and rely on pattern matching to transform input into code.

##### Example:

```rust
macro_rules! greet {
    () => {
        println!("Hello, Rust!");
    };
}

greet!(); // Expands to println!("Hello, Rust!");
```

##### Features:

- **Pattern Matching**: Match specific input structures.
- **Flexibility**: Generate various Rust constructs.
- **Hygiene**: Avoid accidental variable capture by maintaining separate namespaces.

##### Example with Pattern Matching:

```rust
macro_rules! calculate {
    ($x:expr) => {
        println!("Result: {}", $x);
    };
    ($x:expr, $y:expr) => {
        println!("Sum: {}", $x + $y);
    };
}

calculate!(5);          // Prints: Result: 5
calculate!(3, 7);       // Prints: Sum: 10
```

#### 2. **Procedural Macros**

Procedural macros operate on the Rust Abstract Syntax Tree (AST) and are defined in separate crates using the `proc_macro` crate.

##### Types:

- **Function-Like Macros**: Invoked with `!`, similar to declarative macros.
- **Derive Macros**: Used with `#[derive]` to automatically implement traits.
- **Attribute Macros**: Modify or extend behavior for functions, structs, or modules.

##### Example - Derive Macro:

```rust
#[proc_macro_derive(MyTrait)]
pub fn derive_my_trait(input: TokenStream) -> TokenStream {
    // Generate code for `MyTrait` implementation
}

#[derive(MyTrait)]
struct Example;
```

#### 3. **Built-In Macros**

Rust includes several predefined macros for common tasks.

##### Common Examples:

- **`println!`**: Prints formatted text to stdout.
    
    ```rust
    println!("Hello, {}!", "world");
    ```
    
- **`assert!`**: Asserts a condition; panics if false.
    
    ```rust
    assert!(1 + 1 == 2);
    ```
    
- **`vec!`**: Creates a vector.
    
    ```rust
    let nums = vec![1, 2, 3];
    ```
    

---

### Declarative vs. Procedural Macros

|**Feature**|**Declarative Macros**|**Procedural Macros**|
|---|---|---|
|**Definition**|`macro_rules!`|`#[proc_macro]`|
|**Use Case**|Pattern matching and code reuse|AST transformations|
|**Complexity**|Easier to write|Requires parsing and emitting syntax trees|
|**Customizability**|Limited|Highly customizable|
|**Performance**|Faster compilation|Slower due to AST manipulation|

---

### Advanced Examples

#### Declarative Macro with Repetition:

```rust
macro_rules! repeat_print {
    ($($x:expr),*) => {
        $(println!("{}", $x);)*
    };
}

fn main() {
    repeat_print!("Hello", "world", "!"); // Prints each item on a new line
}
```

#### Procedural Macro with `#[derive]`

Define a custom derive macro to implement a trait:

```rust
// In a separate crate with `proc_macro` enabled
use proc_macro::TokenStream;

#[proc_macro_derive(HelloWorld)]
pub fn hello_world_macro(input: TokenStream) -> TokenStream {
    let input_ast = syn::parse(input).unwrap(); // Parse input into syntax tree
    let gen = impl_hello_world(&input_ast);    // Generate code
    gen.into()                                // Return generated code
}

fn impl_hello_world(ast: &syn::DeriveInput) -> quote::Tokens {
    let name = &ast.ident;
    quote! {
        impl HelloWorld for #name {
            fn hello() {
                println!("Hello, {}!", stringify!(#name));
            }
        }
    }
}
```

Usage:

```rust
#[derive(HelloWorld)]
struct MyStruct;

MyStruct::hello(); // Outputs: Hello, MyStruct!
```

---

### std Library Macros

Macros are used very commonly throughout the std library. Let’s take a peek at some of the most commonly used function-like macros.

#### `format!()`

We can interpolate and format strings with the `format!()` macro.

```rust
let exit = 8;
let town = "Willoughby";

let address = format!("Next stop, {town}. Train is at exit number {exit}.");
```

The possibilities for interpolating and formatting values with this syntax are expansive. A detailed list of all capabilities can be found in the std::fmt documentation.

#### `println!()`

`print!()` and `println!()` internally call the `format!()` macro while also printing the formatted String to stdout. Printing to stderr is accomplished with `eprint!()` and `eprintln!()`.

```rust
let jungle_bird = "Macaw";
let sound = "caws";

print!("The {jungle_bird}");  // Does not print a newline
println!(" {sound}.");      // Prints a newline
```

#### `assert!()`

We can assert a conditional evaluation or panic upon failure with the `assert!()` and `assert_eq!()` macros. To assert non-equality, we can use `assert_ne!()`.

```rust
let number = 12;
let you = "us";
let i = "us";

assert!(you == i);
assert_eq!(i, you);
assert_ne!(number, you.len());
```

---

### Panicking Macros

We can utilize the `unreachable!()` macro in situations where the compiler cannot determine code to be unreachable. The `unimplemented!()` macro denotes that a part of your code has not yet been implemented. The `todo!()` macro denotes the same but implies an intent to complete it.

These three macros will all panic if they are reached. We can also intentionally panic our program utilizing the `panic!()` macro.

All of these macros can also optionally print a supplied string as a message upon panicking.

```rust
let number = 10;

if number <= 5 {
  todo!("we will handle this outcome soon.")
} else if number > 5 {
  unimplemented!("we might do something here eventually")
} else {
  unreachable!()
}
panic!("we should use panics sparingly.");
```

---

### Best Practices for Writing Macros

1. **Use Declarative Macros for Simplicity**:
    
    - Favor `macro_rules!` for repetitive patterns that don’t require deep syntax tree manipulations.
2. **Keep Macros Readable**:
    
    - Write clear and concise patterns.
    - Avoid overly complex macros that obscure code logic.
3. **Use Procedural Macros Judiciously**:
    
    - Ideal for advanced use cases like custom `#[derive]` implementations or function-like transformations.
    - Avoid when simple functions or traits suffice.
4. **Hygiene Matters**:
    
    - Macro hygiene prevents unintended conflicts with surrounding code.
    - Use explicit scoping to minimize issues.
5. **Document Your Macros**:
    
    - Include clear examples and explanations of what the macro does and its parameters.

---

### Conclusion

Macros in Rust provide a robust mechanism for metaprogramming, enabling developers to write reusable, efficient, and expressive code. By mastering both declarative and procedural macros, developers can significantly enhance their productivity and the quality of their Rust applications.

to check {

https://www.codecademy.com/courses/rust-for-programmers/articles/attributes-rust

https://doc.rust-lang.org/std/fmt/


}