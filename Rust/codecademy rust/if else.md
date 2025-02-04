
### `if` and `else` in Rust: Deep and Crisp

Rust's `if` statement works similarly to other languages but has some unique properties.

---

### **1. Basic `if` Statement**

```rust
let x = 10;

if x > 5 {
    println!("x is greater than 5");
}
```

- **Condition must be a `bool`** (no implicit conversion from integers).
- **No parentheses required** around conditions.

---

### **3. `if-else if-else` Ladder**

```rust
let x = 10;

if x < 0 {
    println!("Negative number");
} else if x == 0 {
    println!("Zero");
} else {
    println!("Positive number");
}
```

- **Checks conditions sequentially** until one matches.
- **Only one block executes** based on the condition.


---


### **4. `if` as an Expression**

In Rust, `if` can return a value, allowing conditional assignment.

```rust
let number = 10;

// `if` as an expression returning a value
let result = if number % 2 == 0 { "Even" } else { "Odd" };

println!("Number is {}", result);
```

✅ **Both branches must return the same type** (here: `&str`).

---

### **Using `if` in `let` Bindings (Shadowing)**

`if` can be used in variable assignments:

```rust
let y = if true { 100 } else { 200 }; // Both branches return `i32`
println!("y is {}", y);
```

⚠️ **Type mismatch error** if branches return different types:

```rust
let y = if true { 100 } else { "Hello" }; // ❌ Won't compile!
```

---

### **1. Exhaustiveness in Conditional Expressions**

When `if` is used as an expression, **all possible cases must return a value**.

```rust
let carrots = 12;

// `if` expression must be exhaustive
let rabbit_status = if carrots > 10 {
    "In burrow"
} else if carrots == 9 {
    "Snagging one more carrot"
} else {
    "On the prowl"
};

println!("{rabbit_status}"); // ✅ Output depends on `carrots`
```

🛑 **Missing an `else` in an `if` expression results in a compilation error.**

---

### **2. Omitting `else` When Using Statements**

If `if` is used **as a statement** (not returning a value), an `else` is optional.

```rust
if true {
    println!("This is shorthand!"); // ✅ Works fine without `else`
}
```

However, `if` must be exhaustive when used in an expression:

```rust
// ✅ Explicit unit type `()` makes it clear no value is returned.
if true {
    println!("For this...");
    ()
} else {
    ()
}
```

🔹 **Statements do not return values, so no type consistency is required.**

---

### **5. Nested `if`**

```rust
let x = 42;

if x > 0 {
    if x % 2 == 0 {
        println!("Positive even number");
    }
}
```

- **Not recommended**, use `else if` instead for readability.

---


### **7. `if` with `Option` and `Result`**

```rust
let value: Option<i32> = Some(10);

if let Some(v) = value {
    println!("Value is {}", v);
}
```

- **Pattern matching with `if let` is idiomatic in Rust**.

---

### **Key Takeaways**

✅ **Conditions must return `bool`** (no implicit conversions).  
✅ **`if` can be an expression** returning a value.  
✅ **Branching must return the same type** in expressions.  
✅ **Use `if let` for handling `Option` and `Result` types.**


---

### **3. Conditional Operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)**

Rust allows **comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`) through built-in traits:

- **Equality (`==`, `!=`)** → `PartialEq` and `Eq`
- **Ordering (`<`, `>`, `<=`, `>=`)** → `PartialOrd` and `Ord`

These operators work on **primitive types** (e.g., `i32`, `f64`, `char`) and can be implemented for **custom structs and enums**.

---

### **Example 1: Basic Comparisons with Primitive Types**

```rust
let track_number = 8;

if track_number == 9 {
    println!("Number nine");
} 
if track_number != 9 {
    println!("Flip the record");
}

let pancakes = 10;

if pancakes < 3 {
    println!("Eat more pancakes.");
} else if pancakes > 10 {
    println!("Uh oh... too many!");
} else {
    println!("That's a good amount of pancakes.");
}
```

✅ Works seamlessly with built-in types.

---

## **4. Custom Conditional Operators for User-Defined Types**

For custom types (structs & enums), we derive or implement `PartialEq`, `Eq`, `PartialOrd`, and `Ord`.

---

### **Example 2: Using `derive` for Enums**

We can derive `PartialEq`, `Eq`, `PartialOrd`, and `Ord` to enable direct comparisons.

```rust
#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
enum Size {
    Small,
    Medium,
    Large,
}

let size1 = Size::Small;
let size2 = Size::Large;

if size1 < size2 {
    println!("Small is smaller than Large!");
}

if size1 == Size::Small {
    println!("It's a small size!");
}
```

✅ **Enums can now be compared using `==`, `!=`, `<`, `>` directly!**  
✅ **Ordering follows enum declaration order** (`Small` < `Medium` < `Large`).

---

### **Example 3: Implementing `PartialEq` for Structs**

Deriving `PartialEq` allows struct comparisons, but we can also **manually implement** it.

```rust
#[derive(Debug)]
struct Book {
    title: String,
    pages: u32,
}

// Implement `PartialEq` for custom equality logic
impl PartialEq for Book {
    fn eq(&self, other: &Self) -> bool {
        self.title == other.title && self.pages == other.pages
    }
}

let book1 = Book { title: String::from("Rust in Action"), pages: 300 };
let book2 = Book { title: String::from("Rust in Action"), pages: 300 };
let book3 = Book { title: String::from("The Rust Book"), pages: 400 };

if book1 == book2 {
    println!("Both books are the same!");
} else {
    println!("Different books.");
}

if book1 != book3 {
    println!("Books are different.");
}
```

✅ **Now, `Book` instances can be compared using `==` and `!=`!**

---

### **Example 4: Implementing `Ord` and `PartialOrd` for Structs**

To use `<`, `>`, `<=`, `>=`, we must implement `Ord` and `PartialOrd`.

```rust
#[derive(Debug, Eq, PartialEq)]
struct Car {
    speed: u32, 
}

// Implement ordering based on speed
impl Ord for Car {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.speed.cmp(&other.speed)
    }
}

impl PartialOrd for Car {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

let car1 = Car { speed: 150 };
let car2 = Car { speed: 180 };

if car1 < car2 {
    println!("Car 2 is faster!");
}

if car1 >= car2 {
    println!("Car 1 is as fast or faster.");
}
```

✅ **Now, `Car` can be compared using `<`, `>`, `<=`, `>=` and even sorted!**

---

## **Summary**

|Trait|Enables|Derivable for Enums?|Derivable for Structs?|
|---|---|---|---|
|`PartialEq`|`==`, `!=`|✅ Yes|✅ Yes|
|`Eq`|Full equality|✅ Yes|✅ Yes|
|`PartialOrd`|`<`, `>`, `<=`, `>=` (Partial Order)|✅ Yes|✅ Yes|
|`Ord`|`<`, `>`, `<=`, `>=` (Total Order)|✅ Yes|✅ Yes|

💡 **Use `#[derive(...)]` whenever possible for simplicity!**  
💡 **Manually implement traits when custom logic is needed.**


---



