

```rust
use std::collections::HashMap;

// Define a struct for Book with title, author, and status
#[derive(Debug)]
struct Book {
    title: String,
    author: String,
    is_available: bool,
}

fn main() {
    // 1. Initialize a library catalog using a HashMap
    let mut library: HashMap<u32, Book> = HashMap::new();

    // Add books to the library
    library.insert(
        1,
        Book {
            title: "1984".to_string(),
            author: "George Orwell".to_string(),
            is_available: true,
        },
    );
    library.insert(
        2,
        Book {
            title: "The Rust Programming Language".to_string(),
            author: "Steve Klabnik".to_string(),
            is_available: true,
        },
    );
    library.insert(
        3,
        Book {
            title: "The Hobbit".to_string(),
            author: "J.R.R. Tolkien".to_string(),
            is_available: false,
        },
    );

    // 2. Borrow book information using references
    println!("Current Library Catalog:");
    for (id, book) in &library {
        println!(
            "ID: {id}, Title: \"{}\", Author: {}, Available: {}",
            book.title, book.author, book.is_available
        );
    }
    /* =>
    Current Library Catalog:
    ID: 3, Title: "The Hobbit", Author: J.R.R. Tolkien, Available: false
    ID: 1, Title: "1984", Author: George Orwell, Available: true
    ID: 2, Title: "The Rust Programming Language", Author: Steve Klabnik, Available: true
    */

    // 3. Update book availability using mutable references
    let book_id = 2; // Let's mark book ID 2 as unavailable
    if let Some(book) = library.get_mut(&book_id) {
        book.is_available = false;
        println!(
            "\nUpdated Book ID {book_id}: \"{}\" is now unavailable.",
            book.title
        );
    }
    //=> Updated Book ID 2: "The Rust Programming Language" is now unavailable.

    // 4. Use slices to display parts of book titles
    println!("\nBook Titles (first 5 characters):");
    for book in library.values() {
        let slice = &book.title[..5.min(book.title.len())]; // Safe slicing
        println!("\"{}\" => First 5 chars: \"{}\"", book.title, slice);
    }
    /*=>
    Book Titles (first 5 characters):
    "The Hobbit" => First 5 chars: "The H"
    "1984" => First 5 chars: "1984"
    "The Rust Programming Language" => First 5 chars: "The R"
    */

    // 5. Pattern matching with `ref` to borrow specific book fields
    let book_id_to_check = 3;
    match library.get(&book_id_to_check) {
        Some(ref book) if book.is_available => println!(
            "\nBook ID {book_id_to_check} is available: \"{}\"",
            book.title
        ),
        Some(ref book) => println!(
            "\nBook ID {book_id_to_check} is NOT available: \"{}\"",
            book.title
        ),
        None => println!("\nBook ID {book_id_to_check} not found."),
    }
    //=> Book ID 3 is NOT available: "The Hobbit"

    // 6. Example of nested references
    let library_ref = &&library; // Nested references
    println!("\nLibrary Summary (using nested reference):");
    for (id, book) in *library_ref {
        println!("ID: {id}, Title: \"{}\"", book.title);
    }
    /*
    Library Summary (using nested reference):
    ID: 3, Title: "The Hobbit"
    ID: 1, Title: "1984"
    ID: 2, Title: "The Rust Programming Language"
    */
}

```