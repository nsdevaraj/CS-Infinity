

```rust
fn main() {
    let text = "text";
    let mut iter = text.chars().enumerate();
    
//      println!("{:?},{:?}", iter, iter.count()); //=> Enumerate { iter: Chars(['t', 'e', 'x', 't']), count: 0 }
//   |     ----------------------------^^^^---------
//   |     |                     |     |
//   |     |                     |     move out of `iter` occurs here
//   |     |                     borrow of `iter` occurs here
//   |     borrow later used here
}
```


The error is because `println!("{:?}", iter)` **borrows** `iter`, but then `.count()` **consumes** it (moves it).  
You can’t borrow and move the same iterator in one statement.

### 🔧 Fix

If you want both debug output _and_ the count, you can:

#### Option 1: Clone the iterator (if it implements `Clone`)

```rust
fn main() {
    let text = "text";
    let iter = text.chars().enumerate();

    println!("{:?}, {:?}", iter.clone(), iter.count());
}
```

---

#### Option 2: Use `.by_ref()` to borrow the iterator

```rust
fn main() {
    let text = "text";
    let mut iter = text.chars().enumerate();

    println!("{:?}, {:?}", iter.by_ref(), iter.count());
}
```

---

#### Option 3: Collect first, then reuse

```rust
fn main() {
    let text = "text";
    let iter: Vec<_> = text.chars().enumerate().collect();

    println!("{:?}, {:?}", iter, iter.len());
}
```

---

👉 Crispest fix for your code:

```rust
println!("{:?}, {:?}", iter.clone(), iter.count());
```

---

```rust
fn main() {
    let text = "text";
    let mut iter = text.chars().enumerate();
    
//      println!("{:?},{:?}", iter, iter.count()); //=> Enumerate { iter: Chars(['t', 'e', 'x', 't']), count: 0 }
//   |     ----------------------------^^^^---------
//   |     |                     |     |
//   |     |                     |     move out of `iter` occurs here
//   |     |                     borrow of `iter` occurs here
//   |     borrow later used here
    
    println!("{:?}", iter); //=> Enumerate { iter: Chars(['t', 'e', 'x', 't']), count: 0 }
    
    println!("{:?}", iter.clone().count()); //=> 4
}
```