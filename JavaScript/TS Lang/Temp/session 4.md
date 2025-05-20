
Runtime type checkers need!


## 🔴 2. Overusing `as` Type Assertions

### ❌ Anti-Pattern:

ts

CopyEdit

`const user = getUser() as User; // blindly asserting`

- Skips validation.
    
- Silences compiler without guarantees.
    

### ✅ Preferred:

ts

CopyEdit

`if (isUser(user)) {   // safely narrowed }`

Use **user-defined type guards** or validation libraries like [Zod](https://zod.dev).
