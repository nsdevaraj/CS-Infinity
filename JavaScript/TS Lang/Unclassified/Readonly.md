
# 🔒 Understanding `readonly` in TypeScript

In TypeScript, `readonly` is a powerful keyword used to **enforce immutability** on class properties and interface fields. It ensures that once a value is assigned, it cannot be changed—helping catch bugs and make your code more predictable.

---

## 🧠 Where Can You Use `readonly`?

### 1. **In Classes**

Use `readonly` in a class to declare properties that should not be reassigned after initialization.

```ts
class User {
  readonly id: number;

  constructor(id: number) {
    this.id = id; // ✅ Allowed
  }

  changeId(newId: number) {
    this.id = newId; // ❌ Error: Cannot assign to 'id' because it is a read-only property.
  }
}
```

### 2. **In Interfaces & Types**

Use it in interfaces to signal that a property must remain unchanged.

```ts
interface Config {
  readonly apiUrl: string;
}

const config: Config = { apiUrl: 'https://api.example.com' };
config.apiUrl = 'https://new-url.com'; // ❌ Error
```

---

## 🎯 Key Rules of `readonly`

- `readonly` properties **can only be set once** — usually in the constructor (for classes).
- They **cannot be reassigned** after the initial value is set.
- It works at **compile-time** only. At runtime, the property can still be changed unless you freeze the object manually.


---

## 🔁 `readonly` vs `const`

|Feature|`readonly`|`const`|
|---|---|---|
|Applies to|**Class or interface properties**|**Variables** (bindings)|
|Scope|Object-oriented (property level)|Block-scoped (variable level)|
|Reassignment|Prevents reassignment **of properties**|Prevents reassignment **of variables**|

```ts
const user = { name: 'Alice' };
user.name = 'Bob'; // ✅ Allowed (object is mutable)

interface User {
  readonly name: string;
}
const u: User = { name: 'Alice' };
u.name = 'Bob'; // ❌ Error
```

---

## 🧩 Deep vs Shallow Immutability

- `readonly` in TypeScript is **shallow**.
- It prevents reassigning the property itself, **but not the nested object**.


```ts
interface Settings {
  readonly options: { darkMode: boolean };
}

const s: Settings = { options: { darkMode: false } };
s.options.darkMode = true; // ✅ Allowed! (nested object is still mutable)
```

🔒 To enforce **deep immutability**, consider libraries like [`deep-freeze`](https://www.npmjs.com/package/deep-freeze) or using `as const` or utility types.

---

## ✅ Best Practices

- Use `readonly` for **IDs, constants, and configuration values**.
- Combine `readonly` with **immutability patterns** for safer code.
- Avoid using `readonly` with mutable data structures unless you deeply control their usage.

---

## 🧾 Summary

|Keyword|Use Case|Prevents|
|---|---|---|
|`readonly`|Class/interface properties|Reassignment of fields|
|`const`|Variables|Rebinding the variable|

---

TypeScript’s `readonly` gives you a safer, more predictable codebase—especially in large applications where immutability helps prevent unintended side effects.

---

### Examples:

Absolutely! Let’s dive into practical examples of TypeScript's immutability tools like `Readonly<T>`, `as const`, and strategies for deep immutability.

---

## 🔹 1. `Readonly<T>` – Make All Properties Immutable

The built-in `Readonly<T>` utility makes **all properties** of an object type **readonly**.

### ✅ Example:

```ts
type User = {
  id: number;
  name: string;
};

const user: Readonly<User> = {
  id: 1,
  name: 'Alice',
};

user.name = 'Bob'; // ❌ Error: Cannot assign to 'name' because it is a read-only property.
```

> ⚠️ `Readonly<T>` is **shallow** — nested objects are still mutable.

---

## 🔹 2. `as const` – Freeze Value Inference

The `as const` assertion tells TypeScript to treat the value and its nested properties as **literal and readonly**.

### ✅ Example:

```ts
const config = {
  apiUrl: 'https://api.example.com',
  retries: 3,
} as const;

config.apiUrl = 'https://new-url.com'; // ❌ Error: Cannot assign to 'apiUrl'
```

This:

- Converts all properties to `readonly`
    
- Inference changes from `string` → `'https://api.example.com'`, making it fully literal
    

### 📌 Use `as const` for:

- Static configuration
    
- Literal objects used as constants
    
- Preventing unintended mutation in deeply nested values
    

---

## 🔹 3. Deep Immutability Strategy

TypeScript doesn’t offer **deep readonly** out of the box, but you can write your own utility:

### 🛠 DeepReadonly (Recursive)

```ts
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object
    ? DeepReadonly<T[K]>
    : T[K];
};
```

### ✅ Example Usage:

```ts
type Profile = {
  user: {
    id: number;
    name: string;
  };
  settings: {
    theme: string;
  };
};

const profile: DeepReadonly<Profile> = {
  user: { id: 1, name: 'Alice' },
  settings: { theme: 'dark' },
};

profile.user.name = 'Bob'; // ❌ Error
profile.settings.theme = 'light'; // ❌ Error
```

> 🚫 Even nested properties are now fully read-only!

---

## 🧠 Summary Table

|Tool|Use Case|Immutability Scope|Notes|
|---|---|---|---|
|`readonly`|Class/interface fields|Property only|Used in OOP-style classes|
|`Readonly<T>`|Object-wide shallow immutability|Top-level only|Doesn’t recurse into children|
|`as const`|Literal object freezing|Deep (literal only)|Ideal for config/constants|
|`DeepReadonly<T>`|Full immutability|Recursive|Custom utility (or use libraries)|

---

## 📦 Bonus: Libraries for Deep Readonly

- [`type-fest`](https://github.com/sindresorhus/type-fest) offers `ReadonlyDeep`
    
- Runtime immutability? Use [`deep-freeze`](https://www.npmjs.com/package/deep-freeze)
    

---
