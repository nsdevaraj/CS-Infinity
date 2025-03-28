

# Rust DSA Interview Questions and Answers for Beginners

## 1. Arrays and Vectors

### Q1: How do you create an empty vector in Rust?

```rust
let vec: Vec<i32> = Vec::new();
// OR
let vec = Vec::<i32>::new();
// OR 
let vec = vec![];
```


```
p
```


### Q2: Write a function to reverse an array in-place

```rust
fn reverse_array(arr: &mut [i32]) {
    let mut left = 0;
    let mut right = arr.len() - 1;
    
    while left < right {
        arr.swap(left, right);
        left += 1;
        right -= 1;
    }
}

// Example usage
fn main() {
    let mut nums = [1, 2, 3, 4, 5];
    reverse_array(&mut nums);
    println!("{:?}", nums); // Prints [5, 4, 3, 2, 1]
}
```

## 2. Linked List Implementation

### Q3: Implement a simple singly linked list in Rust

```rust
// Define the node structure
struct Node {
    value: i32,
    next: Option<Box<Node>>,
}

struct LinkedList {
    head: Option<Box<Node>>,
}

impl LinkedList {
    // Create a new empty list
    fn new() -> Self {
        LinkedList { head: None }
    }
    
    // Insert at the beginning
    fn push_front(&mut self, value: i32) {
        let new_node = Box::new(Node {
            value,
            next: self.head.take(),
        });
        self.head = Some(new_node);
    }
    
    // Remove from the front
    fn pop_front(&mut self) -> Option<i32> {
        self.head.take().map(|old_head| {
            self.head = old_head.next;
            old_head.value
        })
    }
}
```

## 3. Stack Implementation

### Q4: Implement a stack using a vector

```rust
struct Stack<T> {
    items: Vec<T>,
}

impl<T> Stack<T> {
    fn new() -> Self {
        Stack { items: Vec::new() }
    }
    
    fn push(&mut self, item: T) {
        self.items.push(item);
    }
    
    fn pop(&mut self) -> Option<T> {
        self.items.pop()
    }
    
    fn peek(&self) -> Option<&T> {
        self.items.last()
    }
    
    fn is_empty(&self) -> bool {
        self.items.is_empty()
    }
}
```

## 4. Basic Algorithms

### Q5: Implement binary search

```rust
fn binary_search(arr: &[i32], target: i32) -> Option<usize> {
    let mut left = 0;
    let mut right = arr.len() - 1;
    
    while left <= right {
        let mid = left + (right - left) / 2;
        
        if arr[mid] == target {
            return Some(mid);
        }
        
        if arr[mid] < target {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    None
}

fn main() {
    let sorted_arr = [1, 3, 5, 7, 9, 11];
    match binary_search(&sorted_arr, 7) {
        Some(index) => println!("Found at index {}", index),
        None => println!("Not found"),
    }
}
```

## 5. Common Traits and Ownership

### Q6: Implement a function that uses borrowing and lifetimes

```rust
// Find the maximum element in a slice
fn find_max<'a, T: PartialOrd>(slice: &'a [T]) -> Option<&'a T> {
    slice.iter().max_by(|x, y| x.partial_cmp(y).unwrap())
}

fn main() {
    let numbers = vec![1, 5, 3, 7, 2];
    if let Some(max) = find_max(&numbers) {
        println!("Maximum value: {}", max);
    }
}
```

## Key Rust DSA Concepts to Remember

1. **Ownership Rules**:
    
    - Each value has a single owner
    - When the owner goes out of scope, the value is dropped
    - You can either have one mutable reference or any number of immutable references
2. **Borrowing**:
    
    - References allow you to refer to some value without taking ownership
    - Immutable references (&T) can be copied multiple times
    - Mutable references (&mut T) are exclusive
3. **Common Traits**:
    
    - `Clone`: Create a deep copy of an object
    - `Copy`: Enables simple bit-wise copying
    - `PartialOrd`: Allows comparison between values

## Common Pitfalls for Beginners

- Always be mindful of ownership and borrowing rules
- Use `Option` and `Result` for handling nullable or error-prone scenarios
- Prefer immutable references when possible
- Use `match` for comprehensive pattern matching
- Leverage Rust's type system and compiler checks

## Practice Recommendations

4. Implement data structures from scratch
5. Solve LeetCode/HackerRank problems in Rust
6. Read and understand the Rust standard library implementations
7. Practice ownership and borrowing patterns
8. Use Rust Playground for quick experiments