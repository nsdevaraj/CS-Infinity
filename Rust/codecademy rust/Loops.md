

# 🔄 Loops in Rust – A Complete Guide

Rust provides powerful loop constructs to control code execution. 
These loops can be **infinite**, **conditional**, or based on **iteration over collections**. 

---

## 🌀 1. `loop` – The Infinite Loop

The `loop` keyword is used to create a loop that runs endlessly until explicitly stopped using `break`.

### Syntax:

```rust
loop {
    // your code
    println!("infinite");
}
```


```rust
println!("This is the program that never ends...");  
  
loop {  
  print!(" yes, it goes on and on, my friend,")  
}
```

### Example: Keep prompting user until input is valid

```rust
use std::io;

loop {
    println!("Enter your age:");
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    if let Ok(age) = input.trim().parse::<u32>() {
        println!("You are {age} years old.");
        break;
    } else {
        println!("Invalid input, try again.");
    }
}
```


```rust
use std::io;
use chrono::Datelike;

fn main() {
    loop {
    
        println!("Enter your birth year :");
        
        let mut birth_year_input = String::new();
        
        io::stdin()
	        .read_line(&mut birth_year_input)
	        .expect("Failed to read input!");
        
        
        let birth_year:i32 = match birth_year_input.trim().parse() {
            Ok(year) => year,
            Err(_) => {
                println!("Please give valid year!\n");
                continue;
            }
        };
        
        let current_year = chrono::Utc::now().year();
        
        let age = current_year - birth_year;
        
        println!("{}", 
            if age < 0 { "You are from future!".to_string() } 
            else { format!("Your age is {}", age) }
            );

        return;    
    }
}
```


---

## 🛑 `break` and `continue`

- `break`: Exit the loop.
    
- `continue`: Skip the rest of the current iteration and move to the next.
    


```rust
loop {  
  println!("I will be printed once");  
  break;  
  println!("I will not be printed");  
}  
  
println!("that was fast");
```


```rust
loop {  
  print!(".");  
  continue;  
  println!("I will not be printed");  
}  
  
println!("I will also never print");
```


### Example: Print once then exit

```rust
loop {
    println!("Hello, Rustacean!");
    break;
}
```

### Example: Skip even numbers

```rust
for i in 1..=5 {
    if i % 2 == 0 {
        continue;
    }
    println!("{i} is odd");
}
```

---

## 🔖 Loop Labels

Used to control nested loops by labeling them and breaking out of specific ones.

 syntax `` `label: loop {}``


```rust
'first: loop {  
  println!("entering 'first");  
  
  'second: loop {  
    println!("entering 'second");  
    break 'first;  
  }  
  println!("I will never print")  
}
```

### Example: Break outer loop from inner

```rust
'outer: loop {
    println!("In outer loop");
    
    'inner: loop {
        println!("In inner loop");
        break 'outer; // Exit both loops
    }
}
```


break until which loop


```rust

fn main() {

    let grid = vec![
        vec![1,2,3],
        vec![4,5,6],
        vec![7,8,9]
    ];
    
    let target = 5;
    let mut found_at = None;
    
    
    'search: for row in 0..grid.len(){
        for col in 0..grid[row].len(){
            if grid[row][col] == target {
                found_at = Some((row,col));
                break 'search;
            }
        }
    }
    
    println!("Found target at {:?}", found_at.unwrap());
    //=> Found target at (1, 1)
}
```


---

## 🔁 2. `while` – Conditional Loop

Repeats code while a condition holds true.

### Syntax:

```rust
while condition {
    // code
}
```


```rust
let mut number = 0;  
  
while number <= 11 {  
  println!("{number}");  
  number += 2;  
}
```

### Example: Countdown timer

```rust
let mut countdown = 5;
while countdown > 0 {
    println!("T-minus {countdown}...");
    countdown -= 1;
}
println!("Lift off!");
```

---

## 🔍 3. `while let` – Pattern-Based Loop

Useful for working with types like `Option`, `Result`, and enums. Loops while the pattern matches.


```rust
let mut timer = Some(10);  
  
while let Some(seconds_left) = timer {  
  if seconds_left == 0 {  
    println!("done!");  
    timer = None;  
  } else {  
    println!("{seconds_left}");  
    std::thread::sleep_ms(1000);  
    timer = Some(seconds_left - 1);  
  }  
}
```

### Example: Option countdown

```rust
fn main() {
    let mut timer = Some(3);
    while let Some(remaining) = timer {
        println!("Time left: {remaining}");
        timer = if remaining == 1 {
            None
        } else {
            Some(remaining - 1)
        };
    }
    /*=>
    Time left: 3
    Time left: 2
    Time left: 1
    */
}```

---

## 📚 4. `for in` – Iterating Over Collections

Ideal for arrays, vectors, ranges, or any iterable (i.e., types implementing `Iterator`).

### Basic Syntax:

```rust
for item in collection {
    // use item
}
```

### Example: Loop through a vector

```rust
let nums = vec![1, 2, 3, 4, 5];
for num in nums {
    println!("Number: {num}");
}
```

### Real-world Example: Iterate through lines of a file

```rust
use std::fs::File;
use std::io::{BufReader, BufRead};

let file = File::open("log.txt").unwrap();
let reader = BufReader::new(file);

for line in reader.lines() {
    println!("Log: {}", line.unwrap());
}
```

---

## 🔢 Range-Based Loops

Useful for numeric sequences.

### Example: Count 0 to 4

```rust
for i in 0..5 {
    println!("{i}"); // Prints 0 to 4
}
```

### Inclusive Range:

```rust
for i in 1..=5 {
    println!("{i}"); // Prints 1 to 5
}
```

### Reverse:

```rust
for i in (1..=5).rev() {
    println!("{i}"); // Prints 5 to 1
}
```

---

## 🧠 Bonus: Iteration Tips

### Ownership in `for` loops

- `for x in vec` — **takes ownership** of each element.
    
- `for x in &vec` — **borrows** each element.
    
- `for x in &mut vec` — **mutable borrow**.
    

### Example: Borrow elements to avoid moving

```rust
let names = vec!["Alice", "Bob", "Charlie"];
for name in &names {
    println!("Hello, {name}");
}
// names is still usable here
```

### With `.enumerate()` for index

```rust
let items = ["apple", "banana", "cherry"];
for (i, item) in items.iter().enumerate() {
    println!("Item {i}: {item}");
}
```

---

## ✅ Summary Table

|Loop Type|Use Case|Breakable|Condition-based|Collection Support|
|---|---|---|---|---|
|`loop`|Infinite/repeat-until-break|✅|❌|❌|
|`while`|Repeat while condition is true|✅|✅|❌|
|`while let`|Pattern match on condition|✅|✅|❌|
|`for in`|Iterate over collections/ranges|❌*|✅|✅|

> *You can still simulate breaking out using `.take(n)` or return-based logic in closures.

---


more check {

https://www.codecademy.com/courses/rust-for-programmers/articles/functional-iteration

https://www.codecademy.com/courses/rust-for-programmers/articles/if-let-rust

https://doc.rust-lang.org/std/iter/trait.Iterator.html

}