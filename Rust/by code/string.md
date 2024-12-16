

```rust
fn first_non_rep_char_index(text: String) -> usize {

    for ch in text.chars() {
        println!("{}", ch);
    }
    /*=>
    h
    e
    l
    l
    o
    */

    println!("{:?}", text.chars()); //=> Chars(['h', 'e', 'l', 'l', 'o'])

    return usize::MIN; //=> 0
}
```