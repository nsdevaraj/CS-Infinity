
private fields

as const

enums 
inter, return, as const

template literal types

type inference
type narrowing

type predicates
any vs unknown
as



## ✅ **Why Use `as const`?**

### 1. **Defining Discriminated Unions**

```ts
const statuses = ["loading", "success", "error"] as const;

type Status = typeof statuses[number]; 
// type Status = "loading" | "success" | "error"
```

This is a clean and maintainable way to define union types based on a list of strings.



### 3. **Safe Enums (Enum Alternatives)**

Instead of:

```ts
enum Direction {
  Up = "UP",
  Down = "DOWN"
}
```

Use:

```ts
const Direction = {
  Up: "UP",
  Down: "DOWN"
} as const;

type Direction = typeof Direction[keyof typeof Direction]; 
// "UP" | "DOWN"
```

Benefits:

- Works better with tree-shaking
- Avoids runtime overhead of enums
- More readable and JS-friendly


### 2. **Not for Runtime Logic**

Remember: `as const` is **purely a compile-time construct**. It doesn’t affect JavaScript behavior—it only affects how TypeScript infers types.

