
## 🧠 TypeScript Tip: Why `Object.keys()` Loses Literal Types — And How to Avoid `as` Workarounds

When working with strongly typed objects in TypeScript, you might expect `Object.keys()` to return exact literal types — but it doesn't.

### ❗ The Problem

```ts
const MyData = {
  FOO: { name: 'Foo' },
  BAR: { name: 'Bar' },
} as const;

type Keys = keyof typeof MyData; // "FOO" | "BAR"

const keys = Object.keys(MyData); // Type: string[]
```

Even though `MyData` has specific keys (`"FOO" | "BAR"`), `Object.keys()` returns `string[]`, not a narrowed union.

---

### 💡 Why This Happens

`Object.keys()` is a **runtime JS function** returning `string[]`.  
TypeScript **can't infer** the exact keys at compile time.

---

### ✅ Common Fix (But Not Ideal)

```ts
Object.keys(MyData) as (keyof typeof MyData)[]
```

> ✅ Works  
> ❌ Not type-safe by default  
> ❌ Requires `as` assertion manually

---

### ✅ Better Alternative (No `as` Needed)

Use `Object.values().map(...)` to extract known literal values:

```ts
const keys = Object.values(MyData).map(item => item.name); // Inferred type!
```

If you're targeting something like:

```ts
function process(keys: ('Foo' | 'Bar')[]) { ... }
```

Then this will pass **without any assertion**.

---

### 🛠️ Reusable Helper (Typed `Object.keys()`)

```ts
function typedKeys<T extends object>(obj: T): Array<keyof T> {
  return Object.keys(obj) as Array<keyof T>;
}
```

Use it like this:

```ts
const keys = typedKeys(MyData); // Type: ("FOO" | "BAR")[]
```

✅ Clean  
✅ Type-safe  
✅ No repeated assertions

---

### 🔁 When You Don't Need `keys()` at All

If you're trying to get `"Foo"` and `"Bar"` from an object like:

```ts
const MyData = {
  FOO: { name: 'Foo' },
  BAR: { name: 'Bar' },
} as const;
```

Then just use:

```ts
const names = Object.values(MyData).map(item => item.name); // "Foo" | "Bar"[]
```

---

### ✅ TL;DR

|Task|Use|`as` needed?|Type-safe?|
|---|---|---|---|
|Get exact keys|`typedKeys(obj)`|❌|✅|
|Get values from fields|`Object.values().map(...)`|❌|✅|
|Use raw `Object.keys()`|`Object.keys(obj)`|✅|❌|

---

Let me know if you want a reusable utility package version of this (e.g., `@utils/typed-keys`).