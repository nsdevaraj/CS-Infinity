

https://www.codecademy.com/courses/rust-for-programmers/articles/lifetimes-rust


https://www.codecademy.com/courses/rust-for-programmers/articles/tooling-rust



#### Rust Editions

The `edition` field denotes which _Rust Edition_ the crate utilizes. Rust Editions are not the same as `rustc` compiler versions. Editions are released every few years and are intended mainly for backwards incompatible changes to the language.

We will use the `2021` edition for all examples in this course. To view the specific changes between Rust Editions we can run the command `rustup doc --edition-guide`.




https://doc.rust-lang.org/reference/patterns.html#identifier-patterns


```rust
fn main() {

  fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>());
  }

  fn double(num: u128) -> u128 {
    num * 2
  }

  let int: i32 = 32;
  let (big_int, _float, int_val) = (10,1.2, int);
  println!("{}", int_val); //=> 32

  let doubled_outcome = double(big_int);
  print_type_of(&doubled_outcome); //=> 128

  println!("doubled_outcome {} => {}", big_int, doubled_outcome);
  //=> doubled_outcome 10 => 20
  
}

```



https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html


https://www.codecademy.com/courses/rust-for-programmers/articles/modules-rust


https://www.codecademy.com/courses/rust-for-programmers/articles/mutability-rust


https://doc.rust-lang.org/std/marker/trait.Copy.html


https://www.codecademy.com/courses/rust-for-programmers/articles/references-rust

https://www.codecademy.com/courses/rust-for-programmers/articles/arrays-and-vec


https://doc.rust-lang.org/std/convert/trait.AsRef.html#tymethod.as_ref



