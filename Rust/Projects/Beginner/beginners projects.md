Here’s a list of **simple Rust project ideas** that are perfect for beginners:

## 🦀 Simple Rust Projects for Beginners

### 1. **Command-line Todo App**

**What you'll learn:** File I/O, CLI parsing, structs, enums.  
**Features:**

- Add/remove/list tasks.
- Store tasks in a local file (like JSON or CSV).
- Use crates like `clap` and `serde`.


📦 Crates to explore:

```toml
clap = "4"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

---

### 2. **Guessing Game (from Rust Book)**

**What you'll learn:** Standard input/output, pattern matching, loops.  
**Features:**

- Random number generation.
    
- User input to guess the number.
    

📦 Crates:

```toml
rand = "0.8"
```

---

### 3. **Simple HTTP Client**

**What you'll learn:** Networking, async, error handling.  
**Features:**

- Fetch and display a webpage’s HTML.
    
- Optional: Save the page to a file.
    

📦 Crates:

```toml
reqwest = { version = "0.11", features = ["blocking"] }
```

---

### 4. **Basic Calculator**

**What you'll learn:** Arithmetic, parsing, CLI input.  
**Features:**

- CLI-based calculator.
    
- Support for `+ - * /` and parentheses.
    

Bonus: Add expression parsing with the `meval` crate or write your own parser.

---

### 5. **Markdown to HTML Converter**

**What you'll learn:** File handling, using libraries, basic text transformation.  
**Features:**

- Convert `.md` file into HTML.
    
- Save the output to a new file.
    

📦 Crates:

```toml
pulldown-cmark = "0.9"
```

---

### 6. **Text-based RPG Game**

**What you'll learn:** Structs, enums, loops, basic state machine design.  
**Features:**

- Move between rooms.
    
- Fight monsters.
    
- Pick up items.
    

---

### 7. **File Organizer**

**What you'll learn:** Working with the filesystem.  
**Features:**

- Organize files in a folder based on extension/type.
    
- Move files into subfolders: `images/`, `docs/`, etc.
    

📦 Crates:

```toml
walkdir = "2"
```

---

### Recommendation: Start with the **Todo CLI App** or **Guessing Game**.

They’re small enough to finish in a day but cover core Rust concepts like ownership, enums, structs, file I/O, and libraries.

---

