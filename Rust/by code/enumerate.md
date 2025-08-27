

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

    println!("{:?}", iter.next()); // Some((0, 't'))
    println!("{:?}", iter); //=> Enumerate { iter: Chars(['e', 'x', 't']), count: 1 }
    println!("{:?}", iter.clone().count()); //=> 3
    
    println!("{:?}", iter.next()); // Some((1, 'e'))
    println!("{:?}", iter); //=> Enumerate { iter: Chars(['x', 't']), count: 2 }
    println!("{:?}", iter.clone().count()); //=> 2
    
    println!("{:?}", iter.next()); // Some((2, 'x'))
    println!("{:?}", iter.next()); // Some((3, 't'))
    println!("{:?}", iter.next()); // None 
    println!("{:?}", iter.next()); // None 
    println!("{:?}", iter);//=> Enumerate { iter: Chars([]), count: 4 }
    println!("{:?}", iter.count()); //=> 0
}
```





What’s happening:

- `text.chars()` returns an **iterator** (`Chars<'_>`).
    
- `enumerate()` **wraps** the iterator and yields `(index, value)` pairs.
    
- Printing the iterator itself with `{:?}` just shows the struct (`Enumerate { … }`), not the values.
    
- To **advance** the iterator, you need to _consume_ it (with `for`, `.collect()`, `.next()`, etc).
    

---

### ✅ Example: iterate and see the pairs

```rust
fn main() {
    let text = "text";

    // Convert into a Vec of (index, char) pairs
    let enumerated: Vec<_> = text.chars().enumerate().collect();
    println!("{:?}", enumerated); 
    // [(0, 't'), (1, 'e'), (2, 'x'), (3, 't')]
}
```

---

### ✅ Example: using `.next()`

If you want to **manually step through**:

```rust
fn main() {
    let text = "text";
    let mut iter = text.chars().enumerate();

    println!("{:?}", iter.next()); // Some((0, 't'))
    println!("{:?}", iter.next()); // Some((1, 'e'))
    println!("{:?}", iter.next()); // Some((2, 'x'))
    println!("{:?}", iter.next()); // Some((3, 't'))
    println!("{:?}", iter.next()); // None 
    println!("{:?}", iter.next()); // None 
}
```



```rust



fn main(){
    let text = "text";
    println!("{:?}", text.chars());//=> Chars(['t', 'e', 'x', 't'])
    
    println!("{:?}", text.chars().enumerate());//=> Enumerate { iter: Chars(['t', 'e', 'x', 't']), count: 0 }
    
    // println!("{:?}", text.chars().enumerate().collect());
    /*
    
10   |     println!("{:?}", text.chars().enumerate().collect());
     |                                               ^^^^^^^ cannot infer type of the type parameter `B` declared on the method `collect`
     |
     = note: cannot satisfy `_: FromIterator<(usize, char)>`
note: required by a bound in `collect`
    --> /playground/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib/rustlib/src/rust/library/core/src/iter/traits/iterator.rs:2014:19
     |
2014 |     fn collect<B: FromIterator<Self::Item>>(self) -> B
     |                   ^^^^^^^^^^^^^^^^^^^^^^^^ required by this bound in `Iterator::collect`
help: consider specifying the generic argument
     |
10   |     println!("{:?}", text.chars().enumerate().collect::<Vec<_>>());
     |                                                      ++++++++++

*/
    println!("{:?}", text.chars().enumerate().collect::<Vec<_>>()); //=> [(0, 't'), (1, 'e'), (2, 'x'), (3, 't')]

    for (index, character) in text.chars().enumerate(){
        println!("{} {}", index,character);
    }
}

```

