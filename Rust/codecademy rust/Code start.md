
### **Program Structure in Rust**

#### **Installing Rust**

Install Rust via [rustup.rs](https://rustup.rs/). After installation, you’ll have these essential tools:

- **rustc**: The Rust compiler.
- **rustup**: Manages Rust versions.
- **cargo**: The primary development tool.

These are all you need to start writing Rust programs.

---

#### **Creating a New Crate**

A **crate** is a Rust project. Using Cargo, crates can be either:

- **Binary**: Creates an executable.
- **Library**: Exposes reusable code.

**To create a binary crate**:

```bash
cargo new my_binary
```

Generates:

```
my_binary/
├── src/
│   └── main.rs
└── Cargo.toml
```

The `main.rs` file is the program’s entry point.

**To create a library crate**:

```bash
cargo new --lib my_library
```

Generates:

```
my_library/
├── src/
│   └── lib.rs
└── Cargo.toml
```

Libraries require **manual exports** for accessible items.


**Cargo.toml** serves as the configuration file for our crate.

---

#### **Program Structure**

For binary crates, the `main.rs` file contains:

```rust
fn main() {
    println!("Hello, world!");
}
```

The `main()` function serves as the program’s entry point. Run the program with:

```bash
cargo run
```

Rust processes code **top to bottom, left to right** in the order it’s declared.

---

#### **Naming Conventions**

Rust enforces consistent naming styles:

- **UpperCamelCase**: Types, traits, enums.
    
    ```rust
    struct StructName { field: NamedTuple }
    trait TraitName {}
    ```

```rust
// Unit-like struct with no fields
struct UnitStruct;

// Tuple struct with a single generic field
struct TupleStruct(T);

// Named field struct
struct StructName {
    field: NamedTuple,
}

// Enum with a single variant
enum EnumName {
    VariantName,
}

// Type alias for `u8`
type TypeAlias = u8;

// Trait definition
trait TraitName {}

```


- **snake_case**: Functions, variables, macros.
    
    ```rust
    fn function_name() { let variable_name = 42; }
    ```

```rust
// Attribute definition
#![attribute_name]

// Variable declaration
let variable_name = true;

// Function definition
fn function_name() {
    function_call();
}

// Macro invocation
macro_name!();
macro_name![];
macro_name! {};

```



- **SCREAMING_SNAKE_CASE**: Constants.
    
    ```rust
    const MAX_LIMIT: u32 = 100;
    ```
    

---

#### **Common Cargo Commands**

|**Command**|**Purpose**|
|---|---|
|`cargo new`|Create a new binary crate.|
|`cargo new --lib`|Create a new library crate.|
|`cargo build`|Compile the crate.|
|`cargo build --release`|Compile with optimizations.|
|`cargo run`|Compile and run the executable.|
|`cargo test`|Run all tests.|
|`cargo doc --open`|Build and open crate documentation.|
|`cargo clean`|Remove temporary compilation files.|
|`cargo publish`|Publish the crate to `crates.io`.|
|`cargo install`|Install binaries from `crates.io`.|

---

