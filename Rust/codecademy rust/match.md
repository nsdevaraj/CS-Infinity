

Rust’s `match` keyword is a powerful control flow construct that allows you to compare a value against a series of patterns and execute code based on which pattern matches. It's like a supercharged `if` / `else if`, with more power and readability.


Each `match` arm uses the `=>` syntax to separate the pattern from the result block. If the arm is a single expression, it ends with a comma `,`.


Every possible value must be handled in a `match`. If you don’t care about all specific values, you can use `_` as a **catch-all pattern**: i.e Exhaustiveness. 
If a pattern is not covered and the compiler can detect it, it will throw an error.


```rust

fn main(){
    
    fn describe_num(num:i32)-> &'static str {
        match num {
            1 => return "one",
            2 =>  return "two",
            _ => return "not one/two"
        }
    }
    
    println!("{}",describe_num(1)); //=> one
    println!("{}",describe_num(2)); //=> two
    println!("{}",describe_num(3)); //-=> not one/two
}
```


---

### 🔸 Pattern Matching Features

#### ✅ **Or Patterns** (`|`)

Match multiple values with a single arm:

```rust
let plant = "dandelion";

match plant {
    "dandelion" | "almond" | "apple" => println!("Rose Family"),
    "tomato" | "pepper" | "potato" => println!("Nightshade Family"),
    _ => println!("not found"),
}
```


### 🔸 Match Guards

Add extra conditions to a match arm using `if`:

```rust
let answer = Some("herring");

match answer {
    Some(x) if x.len() > 7 => {
        println!("incorrect");
        println!("hint: password is less than 7 characters long");
    }
    Some(x) => println!("incorrect"),
    None => println!("no input"),
}
```


```rust
fn find_pwd(pwd: Option<&str>) {
    match pwd {
        Some(p) if p.is_empty() => {
            println!("password found empty");
        }
        Some(_) => println!("password is good"),
        None => println!("pwd not applicable"),
    }
}

fn main() {
    let pwd1 = Some("");
    let pwd2 = Some("secret");
    let pwd3: Option<&str> = None;

    let pwds = [pwd1, pwd2, pwd3];

    pwds.iter().for_each(|pwd| find_pwd(*pwd));
    /*=>
    password found empty
    password is good
    pwd not applicable
    */
}

```


```rust

fn main() {
    let greeting = Some("Good Morning");
    
    match greeting {
        Some(word) if word.starts_with("Good") => {
            println!("this greeting is {word}");
        }
        Some(word) => println!("Some word: {word}"),
        _ => println!("no word")
    } //=> this greeting is Good Morning
    
    // match greeting {
    //     Some(word) & word.starts_with("Good") => {
    //         println!("this greeting is {word}");
    //     }
    //     Some(word) => println!("Some word: {word}"),
    //     _ => println!("no word")
    // }
    /*
    error: expected one of `=>`, `if`, or `|`, found `&`
  --> src/main.rs:15:20
   |
15 |         Some(word) & word.starts_with("Good") => {
   |                    ^ expected one of `=>`, `if`, or `|`

*/
    
    
}

```


✅ **Quick meaning:**

- **`|`** → directly in patterns (example: `1 | 2`)
    
- **`if`** → add extra condition (example: `if word.starts_with("Good")`)
    
- **`&&`, `||`** → _inside_ an `if` condition — allowed.
    
- **`&&`, `||`** _outside_ (between patterns directly) — **not** allowed.




---

#### ✅ **Ranges** (`..` and `..=`)

- `..=` includes the upper bound.
- `..` excludes the upper bound.
    
### 🔸 Binding with `@`

Use `@` to **bind a matched value to a variable**:


```rust
let chipmunks = 5;

match chipmunks {
    0 => println!("no chipmunks"),
    1..=20 => println!("some chipmunks"),
    n @ 21..=40 => println!("warning: {n} chipmunks!"),
    _ => println!("too many chipmunks."),
}
```



---

### 🔸 Matching Enums

Match shines when working with enums like `Option`, `Result`, and custom enums:

### 🔸 Nested Matches

You can match inside a match:

```rust
enum Animal {
    Dog(String),
    Cat,
    Bird,
}

fn main() {
    let maybe_pet = Some(Animal::Dog("Barky".to_string()));

    match maybe_pet {
        Some(animal) => match animal {
            Animal::Dog(name) => println!("Dog: {name}"),
            Animal::Cat => println!("Cat"),
            Animal::Bird => println!("Bird"),
        },
        None => println!("No pet"),
    }   
    //=> Dog: Barky
}
```

---

### ✅ Summary

| Feature          | Syntax                         |
| ---------------- | ------------------------------ |
| Basic Match      | `match x { pattern => block }` |
| Catch-all        | `_ => ...`                     |
| Multiple matches | `"a" \| "b"`                   |
| Ranges           | `1..=5 => ...`                 |
| Binding          | `x @ 1..=5 => ...`             |
| Match guards     | `Some(x) if x > 5 => ...`      |

---

### ✨ Tips

- `match` is **exhaustive** – you _must_ cover all cases.
- Great for working with enums like `Option`, `Result`, and your own.    
- Prefer `match` for readability when handling complex conditional logic.


---

extra:

what different it make when I put the  func inside and outside of main ?


**Rust **_does_** allow function definitions inside other functions — but only in very limited ways**.

### 🔍 So... what's the deal?

Rust **does support** nested functions as of **stable Rust**, but:

- They're limited to the current function scope (they’re **not accessible outside** the function they're declared in).
    
- This feature has been stable for a long time, despite what some older tutorials or outdated answers may say.
    

### ✅ Your Example Works Because:

You defined `print_number` **inside `main()`**, and then you **called it within `main()`**. It never leaves that scope — which is perfectly valid.

```rust
fn main() {
    // Inner function only available within `main`
    fn print_number(n: i32) {
        match n {
            1 => println!("1"),
            2 => println!("2"),
            3 => println!("3"),
            _ => println!("another number"),
        }
    }

    print_number(3);   // 3
    print_number(10);  // another number
}
```

### ❌ This Would NOT Work:

```rust
fn main() {
    print_number(1); // ❌ Error! Not in scope here.
}

fn print_number(n: i32) {
    // This is a *different* top-level function.
}
```

Or:

```rust
fn main() {
    fn inner() {
        println!("hi");
    }
}

inner(); // ❌ Error! Can't call it outside `main`
```

---

### 🔑 TL;DR

- ✅ Yes, you **can** define functions inside `main()` (or other functions).
    
- ☑️ But they are **local** to that function.
    
- 🔒 You **can’t use them outside** the function they were defined in.
    
- 🧰 This is useful when the helper is very specific to a single function and you want to limit its visibility.
    


---


### 🧠 Quick Recap of `@` Syntax:

```rust
Some(id @ 100..=199) => println!("ID in range: {}", id),
```

This means: _"If it's a `Some` and the inner value is between 100 and 199, bind that value to `id`."_

---

## 🛠 Real-World Use Cases

---

### ✅ 1. **Matching & binding user input (e.g., ID ranges)**

Imagine you're handling user IDs differently based on their value:

```rust
fn handle_user(id: u32) {
    match id {
        admin_id @ 1..=10 => println!("Admin user with ID: {}", admin_id),
        regular_id @ 11..=1000 => println!("Regular user with ID: {}", regular_id),
        _ => println!("Guest or invalid user"),
    }
}
```

---

### ✅ 2. **Error codes in APIs or system responses**

```rust
enum Response {
    Success,
    Error(u16),
}

fn handle_response(res: Response) {
    match res {
        Response::Error(code @ 400..=499) => println!("Client error: {}", code),
        Response::Error(code @ 500..=599) => println!("Server error: {}", code),
        Response::Error(code) => println!("Other error: {}", code),
        Response::Success => println!("All good!"),
    }
}
```

---

### ✅ 3. **Enum with embedded values (think networking, parsing, etc.)**

```rust
enum Packet {
    Ping(u8),
    Data { id: u32, payload: Vec<u8> },
}

fn process_packet(p: Packet) {
    match p {
        Packet::Ping(seq @ 0..=10) => println!("Low-seq ping: {}", seq),
        Packet::Ping(seq) => println!("Ping seq: {}", seq),
        Packet::Data { id: packet_id @ 1000..=2000, payload } => {
            println!("Important packet {}, payload size: {}", packet_id, payload.len())
        }
        Packet::Data { id, .. } => println!("Other packet: {}", id),
    }
}
```

---

### ✅ 4. **Custom pattern matching in compiler/interpreter projects**

If you're writing a parser or interpreter (e.g., a mini language), you might want to bind and inspect tokens or nodes in a specific range or type:

```rust
enum Token {
    Number(i64),
    Ident(String),
}

fn analyze_token(tok: Token) {
    match tok {
        Token::Number(val @ -10..=10) => println!("Small number: {}", val),
        Token::Number(val) => println!("Big number: {}", val),
        Token::Ident(name) => println!("Identifier: {}", name),
    }
}
```

---

### ✅ 5. **Nested Destructuring + Matching**

```rust
struct Event {
    kind: String,
    code: u32,
}

fn log_event(event: Event) {
    match event {
        Event { kind, code @ 100..=199 } => println!("{}: Informational ({})", kind, code),
        Event { kind, code @ 400..=499 } => println!("{}: Client Error ({})", kind, code),
        _ => println!("{}: Other Event", event.kind),
    }
}
```

---

### 🧩 Why Use `@` Instead of Matching Twice?

Without `@`, you'd need to match a range **and** re-use the value:

```rust
match x {
    1..=10 => {
        let value = x; // clunky and repetitive
    }
    _ => {}
}
```

With `@`, it's concise and clean:

```rust
val @ 1..=10 => println!("Value: {}", val)
```

---

Want to try building a small real-world example with it? Or see how it behaves in a match guard or nested structure?