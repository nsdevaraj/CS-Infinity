


```rust

#[derive(Debug)]
struct User {
    name: String,
}

impl User {
    fn new(name: &str) -> Self {
        User {
            name: name.to_string(),
        }
    }
}

fn print(user: &User) {
    println!("User name: {}", user.name);
}

fn print_obj(user: User){
    println!("User: {:?}", user);
} // object is dropped and memory is free

fn main() {
    let user1 = User::new("Alice");

    
    print(&user1);// Borrow instead of move
    println!("User: {}", user1.name); // Still usable here
    print(&user1); // OK: we're just borrowing

    // If you really want to move:
    let user2 = user1; // object ownership is transferred
    // print(&user1); // ❌ Compile error: user1 has been moved
    print(&user2); // ✅ OK
    
    print_obj(user2);
    
    // print(&user2);//:=  borrow of moved value: `user2`
}


```



Move semantics:

In Rust, **move semantics** means transferring ownership of data from one variable to another. When you move data, the original variable is no longer valid, and you can’t use it anymore.

### Key Points:

1. **Move**: When a variable is assigned to another, the ownership is transferred. The original variable is no longer usable.
    
    ```rust
    let x = String::from("Hello");
    let y = x;  // Ownership of the String is moved from x to y
    // println!("{}", x); // Error: x is no longer valid
    ```
    
2. **Borrow**: Instead of moving data, you can borrow it. Borrowing means accessing the data without taking ownership, so the original variable is still valid.
    
    ```rust
    let x = String::from("Hello");
    let y = &x;  // Borrowing: x is still valid
    println!("{}", x); // This works
    ```
    
3. **Copy**: Some types (like integers) implement the `Copy` trait, meaning their value is duplicated instead of moved.
    
    ```rust
    let x = 42;
    let y = x;  // Copying the value, both x and y are valid
    ```
    

### Why It Matters:

- **Performance**: Moving is efficient since no extra memory allocation or copying happens, unlike in languages that use garbage collection.
- **Safety**: Rust ensures there’s no accidental data duplication or double-free by enforcing strict rules on ownership.


---

### 📌 **Borrowing Rules: The Three Laws of Safety**

1. You can have **many immutable** borrows **or** **one mutable** borrow - but not both at the same time.
2. Borrows **must not outlive the owner**.
3. The compiler enforces these rules at **compile time**, not runtime.


reference ~= borrowing


```rust

#[derive(Debug)]
struct User {
    name: String,
}

impl User {
    fn new(name: &str) -> Self {
        User {
            name: name.to_string(),
        }
    }
}

fn print_name(user: &User) {
    println!("User name: {}", user.name);
}

// fn change_name_try(user: &User){
//     user.name = "new name".to_string();
//     //:= cannot assign to `user.name`, which is behind a `&` reference
// } 

fn change_name(user: &mut User){
    user.name = "new name1".to_string();
}

fn change_name2(user: &mut User){
    user.name = "new name2".to_string();
}

fn main() {
    let user1 = User::new("Alice");
    let user2 = user1; // user1 memory is moved
    
    // print_name(&user1);//:= borrow of moved value: `user1`
    print_name(& user2); // just borrowing
    print_name(& user2); // just borrowing
    
    // change_name_try(&user2);
    
    
    let mut user3 = user2; // user2 memory is moved and made mutable
    // print_name(&user2); //:=  borrow of moved value: `user2`
    
    print_name(& user3); //? warning: variable does not need to be mutable
    
    change_name(&mut user3);
    print_name(& user3); // new name1
    
    let user3_non_mut = &user3; // create im_mut reference from mut reference
    print_name(& user3_non_mut); // new name1
    
    
    change_name2(&mut user3);
    print_name(& user3); // new name2
    
    // print_name(& user3_non_mut); 
    // :Cannot borrow `user3` as mutable because it is also borrowed as immutable
    // mutable borrow occurs here after taking immutable reference so causing issue
    
    let user3_non_mut2 = & user3;
    print_name(& user3_non_mut2); // new name2
    print_name(& user3); // new name2
    
    let user3_non_mut3 = & user3;
    print_name(& user3_non_mut3); // new name2
    
    let user2_non_mut2_copy = & user3_non_mut2;
    print_name(& user2_non_mut2_copy); // new name2
   
    
}

```



Borrowing rules:
1) Immutable vs mutable references
2) 1 mutable XOR N immutable references
3) References validity


Immutable reference - should not have underlying value change at any cost!

```rust
#![allow(warnings)]

#[derive(Debug)]
struct User {
    name: String,
}

impl User {
    fn new(name: &str) -> Self {
        User {
            name: name.to_string(),
        }
    }
}

fn print_name(user: &User) {
    println!("{}", user.name);
}

fn change_name(user: &mut User, new_name:&str){
    user.name = new_name.to_string();
}

fn main() {
    let mut user1 = User::new("David");
    print_name(& user1); // David
    change_name(&mut user1, "James");
    print_name(& user1); // James
    
    
    let mut user2 = User::new("Amin");
    let user2_r1 = &mut user2;
    print_name(& user2_r1); // Amin
    
    
    // change_name(&mut user2_r1, "Rajesh");
    //:= cannot borrow `user2_r1` as mutable, as it is not declared as mutable
    
    // let mut user2_r2 = &mut user2;
    // print_name(& user2_r1); //:= cannot borrow `user2` as mutable more than once at a time
    // drop(user2_r1) //:cannot borrow `user2` as mutable more than once at a time
    
    drop(user2_r1); 
    let mut user2_r2 = &mut user2;
    print_name(& user2_r2); // Amin
    
    // print_name(& user2_r1); //:= cannot borrow `user2` as mutable more than once at a time
    
    change_name(&mut user2_r2, "Rajesh");
    print_name(& user2_r2); // Rajesh
    
    print_name(& user2); // Rajesh
    change_name(&mut user2, "Sunil");
    print_name(& user2); // Sunil
    
    print_name(& user2_r2); // : cannot borrow `user2` as immutable because it is also borrowed as mutable
    
}

```


### 🔐 Rust Borrowing Rule — "1 Mutable XOR N Immutable"

Rust enforces this rule to ensure **memory safety without a garbage collector**:

> **At any one time, you can have either:**
> - **One mutable reference** (`&mut T`) **OR**
> - **Any number of immutable references** (`&T`)
> **But not both!**

---

### 🚫 Why?

To prevent:
- **Data races**
- **Unexpected mutations**
- **Dangling or invalid references**

---

### ✅ Examples

**Immutable references (many allowed):**

```rust
let data = String::from("Hello");

let r1 = &data;
let r2 = &data;

println!("{}, {}", r1, r2); // OK
```

**Mutable reference (only one allowed, no immutable refs at same time):**

```rust
let mut data = String::from("Hello");

let r1 = &mut data;
// let r2 = &data; // ❌ ERROR: cannot borrow as immutable while mutable borrow exists

r1.push_str(" world"); // OK
```

---

### 📌 Key Rule:

> **You can read or write, but not both at the same time.**

---



```rust
#![allow(warnings)]

#[derive(Debug)]
struct User {
    name: String,
}

impl User {
    fn new(name: &str) -> Self {
        User {
            name: name.to_string(),
        }
    }
}

fn print_name(user: &User) {
    println!("{}", user.name);
}

fn change_name(user: &mut User, new_name:&str){
    user.name = new_name.to_string();
}

fn main() {
    let mut user1 = User::new("Alice");
    print_name(& user1); //=> Alice
    change_name(&mut user1, "Shanthi");
    print_name(& user1); //=> Shanthi
    
    let r1 = &mut user1;
    let r2 = &user1;
    print_name(&r2); //=> Shanthi
  
    
    // drop(r1); // borrow happend and freed, so user itself freed
    //=: cannot borrow `user1` as immutable because it is also borrowed as mutable
    
    let mut user2 = User::new("Sam");
    let r3 = &mut user2;
    let r4 = &user2;
    
    print_name(&r4); //=> Sam
    
    // print_name(&r3);
    // : cannot borrow `user2` as immutable because it is also borrowed as mutable
    
    
    let mut user3 = User::new("Tommy");
    let mut r5 = &mut user3;
    print_name(&r5); //=> Tommy
    change_name(&mut r5, "Valter");
    print_name(&r5); //=> Valter
    
    let r6 = & r5;
    print_name(&r6); //=> Valter
    
    let r7 = & user3;
    print_name(&r7); //=> Valter
    
    //  change_name(&mut r5, "Arnauld");
     //:  cannot borrow `user3` as immutable because it is also borrowed as mutable
    // affects r7 area
}

```