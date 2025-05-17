
# 🎨 `Prettify` in TypeScript: Clean Up Complex Types

In modern TypeScript, you’ll often work with utility types like `Pick`, `Omit`, `Partial`, `Exclude`, and so on. These help manipulate types—but sometimes they produce **ugly, unreadable, or nested types** that make tooling and autocomplete harder to use.

Enter: `Prettify`.

---

## 🧾 What is `Prettify`?

`Prettify` is a custom utility type that **flattens** or **cleans up** messy inferred or composite types. It **resolves intersections** and spreads into a final “pretty” form for better developer experience and readability.

### 🔧 Definition

```ts
type Prettify<T> = {
  [K in keyof T]: T[K];
} & {};
```

This forces TypeScript to **re-evaluate and simplify** the structure.

---

## ❓ Why is `Prettify` Useful?

Let’s look at a typical situation:

```ts
type User = {
  id: string;
  name: string;
};

type WithEmail = {
  email: string;
};

type Merged = User & WithEmail;
```

Now hover `Merged` in VSCode. You'll see:

```ts
type Merged = User & WithEmail
```

Instead of:

```ts
{
  id: string;
  name: string;
  email: string;
}
```

That’s where `Prettify` helps:

```ts
type PrettyMerged = Prettify<User & WithEmail>;
```

VSCode (and your brain) now sees a flattened, clean type.

---

## ✅ Real-World Use Cases

---

### 1️⃣ Return Types

In complex apps, your return types from functions can become deeply nested:

```ts
function makeUser(): Prettify<User & WithEmail> {
  return {
    id: '123',
    name: 'Alice',
    email: 'alice@example.com'
  };
}
```

➡️ This ensures dev tools **display full, flat types** instead of intersections.

---

### 2️⃣ Derived Types with `Pick`, `Omit`, etc.

```ts
type Raw = Pick<User, 'id'> & { isAdmin: boolean };

type Pretty = Prettify<Raw>;

// Without Prettify → type is "Pick<...> & {...}"
// With Prettify → shows as { id: string; isAdmin: boolean }
```

---

### 3️⃣ Input Sanitization Models

When building types that **remove sensitive fields**, you often intersect and transform types:

```ts
type SafeUser = Prettify<Omit<User & WithEmail, 'email'>>;

// Shows as clean: { id: string; name: string }
```

---

### 4️⃣ Utility Libraries & Reusability

Create a utility that merges two types and always returns a clean output:

```ts
type Merge<A, B> = Prettify<A & B>;

type MergedUser = Merge<User, { email: string }>;
```

---

## ⚠️ Limitations

- `Prettify<T>` only **flattens one level**. It doesn't deeply simplify nested structures.
    
- It doesn't change behavior—just **presentation and tooling**.
    
- It's mostly useful for **readability and DX (developer experience)**.
    

---

## ✨ Bonus: Deep Prettify (Advanced)

You can recursively prettify deeply nested types (use sparingly):

```ts
type DeepPrettify<T> = {
  [K in keyof T]: T[K] extends object
    ? DeepPrettify<T[K]>
    : T[K];
};
```

---

## 🤖 Interview Perspective

> **Q:** “What is `Prettify` in TypeScript and when would you use it?”

**A:** "`Prettify` is a custom utility type that flattens complex types—especially intersections like `A & B`—into readable object types. It improves type clarity in tooling and makes code easier to read. I often use it when combining types or working with derived DTOs."

---

## 📦 Summary

|Feature|Description|
|---|---|
|What is it?|Flattens complex/intersected types for readability|
|Use it for|DTOs, return types, intersection results|
|Improves|Type display, autocomplete, developer experience|
|Limitations|One level deep; cosmetic only|

---

## 🧪 TL;DR

```ts
type Prettify<T> = {
  [K in keyof T]: T[K];
} & {};
```

Use it to make `User & Extra` look like:

```ts
{
  id: string;
  name: string;
  email: string;
}
```

Instead of showing cryptic `User & Extra` type unions.

---
