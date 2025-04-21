

# Variables

Variable names are always in `snake_case`.


When assigning a value, Rust will be able to infer the type of your variable 99% of the time. If it cannot you may add the type to your variable declaration.

Notice how we can assign to the same variable name multiple times. This is called variable shadowing and the type can be changed for subsequent references to that name.



Nice summary! You're diving into some core Rust concepts there. Let’s break that down a bit for clarity and maybe a couple extras to round it out:

---

### 🔧 **Variables in Rust**



Variables are declared using the **let** keyword.

#### ✅ **Declaring a Variable**

```rust
let name = "Alice";
let age = 30;
```

Rust infers the types here: `&str` for `name` and `i32` for `age`.

---

### 🔍 **Explicit Typing (when needed)**

```rust
let score: f64 = 98.6;
```

Useful when:

- Rust can't infer the type
    
- You want to be extra clear
    
- You're working with multiple numeric types
    

---

### 🔁 **Variable Shadowing**

```rust
let spaces = "   ";
let spaces = spaces.len();  // now spaces is a number!
```

Shadowing lets you reuse the same variable name and even **change its type**. It’s different from `mut`, which only allows changing the value—not the type.

---

### 🔄 **Mutable Variables**

```rust
let mut counter = 0;
counter += 1;
```

Use `mut` if you want to update the value without shadowing. Type must stay the same.

### 🐍 **snake_case Naming**

- All variable names in Rust use `snake_case`
- e.g., `user_name`, `total_score`, `max_value`




