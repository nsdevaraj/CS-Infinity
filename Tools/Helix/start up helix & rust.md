

To exit Helix editor, type `:q` or `:quit` and press Enter. To force quit and discard changes, use `:q!` or `:quit!`.


https://docs.helix-editor.com




### **Step 1: Install Rust and Helix**

#### **1. Install Rust (if not installed)**

Open a terminal and run:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env  # Apply changes to the current session
rustc --version          # Verify installation
```

If Rust is installed, you’ll see a version like `rustc 1.x.x`.

#### **2. Install Helix (if not installed)**

Run:

```sh
# On Debian/Ubuntu
sudo apt install helix

# On macOS (with Homebrew)
brew install helix
```

Check if it's installed:

```sh
hx --version
```

---

### **Step 2: Create a Rust Project**

```sh
cargo new rust_dsa
cd rust_dsa
hx .
```

This opens **Helix** in the `rust_dsa` directory.

---

### **Step 3: Open `src/main.rs` and Write a Simple Rust DSA Code**

Press `Space` + `/` to open **file picker**, then navigate to `src/main.rs`.

Now, let’s write a basic **binary search** algorithm:

```rust
fn binary_search(arr: &[i32], target: i32) -> Option<usize> {
    let mut left = 0;
    let mut right = arr.len() - 1;

    while left <= right {
        let mid = left + (right - left) / 2;
        if arr[mid] == target {
            return Some(mid);
        } else if arr[mid] < target {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    None
}

fn main() {
    let numbers = [1, 3, 5, 7, 9, 11];
    let target = 5;
    
    match binary_search(&numbers, target) {
        Some(index) => println!("Found at index {}", index),
        None => println!("Not found"),
    }
}
```

---

### **Step 4: Save the File in Helix**

- Press `Esc` (to enter **normal mode**).
    
- Press `:w` and `Enter` to save.
    

To **exit Helix** after saving:

1. Press **`Esc`** (ensure you're in **normal mode**).
    
2. Type **`:q`** (quit) and press **Enter**.
    

### Alternative Commands:

- **`:q!`** → Quit without saving.
    
- **`:wq`** → Save and quit.
    
- **`ZZ`** → Save and quit (faster shortcut).
    


---

### **Step 5: Run the Rust Code**

In the terminal (inside `rust_dsa` folder), run:

```sh
cargo run
```

You should see:

```
Found at index 2
```

---

### **Step 6: (Optional) Enable Rust LSP for Helix**

To get **syntax highlighting and auto-completion**, ensure Rust analyzer is installed:

```sh
rustup component add rust-analyzer
```

Then, open Helix and check if it's working:

```sh
hx src/main.rs
```

Try typing some Rust code and see if it suggests completions.


Yes, you need to **enable Rust LSP (Language Server Protocol)** globally, not just in a specific project.

### **Steps to Enable Rust LSP in Helix**

#### **1. Install Rust Analyzer**

First, ensure you have **rust-analyzer** installed (globally):

```sh
rustup component add rust-analyzer
```

This installs Rust’s official language server.

### **Step 1: Open Helix Config File**

```sh
hx ~/.config/helix/languages.toml
```

If the file doesn’t exist, create it.

---

### **Step 2: Add Rust LSP Configuration**

Paste this inside `languages.toml`:

```toml
[[language]]
name = "rust"
auto-format = true
language-servers = ["rust-analyzer"]
```

---

### **Step 3: Restart Helix**

Now, open a Rust file:

```sh
hx src/main.rs
```

Test it by typing some Rust code—Helix should show **syntax highlighting, auto-completions, and error diagnostics**. 🚀

Let me know if you face any issues!


---



see different configs setup in system

```
cd ~/.config
```



https://youtu.be/PERvTNiupe8?si=GvuGSGtWlEfdYdjU


### **Understanding the Nano Keybindings**

In **Nano**, commands are shown at the bottom, and they use `Ctrl` (`^` means `Ctrl`). Here’s what they mean:

|Command|Meaning|Keys to Press|
|---|---|---|
|**^G**|Get Help|`Ctrl + G`|
|**^O**|Write (Save) File|`Ctrl + O`, then `Enter`|
|**^X**|Exit Nano|`Ctrl + X`|
|**^W**|Search in File|`Ctrl + W`|
|**^K**|Cut Line|`Ctrl + K`|
|**^U**|Paste (Uncut)|`Ctrl + U`|





Space + F => editor window in helix


