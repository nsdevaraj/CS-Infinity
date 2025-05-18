



# 🎯 TypeScript `Extract` vs `Exclude`: Mastering Union Type Filtering

TypeScript's `Extract` and `Exclude` utility types allow you to **filter union types** with surgical precision. Whether you're building type-safe APIs, form logic, or narrowing input types, these tools are essential.

These works on Union types only!

---

## 🧪 TL;DR

|Utility|Purpose|Result|
|---|---|---|
|`Extract<A, B>`|Keep only types in `A` that are also in `B`|Intersection of unions|
|`Exclude<A, B>`|Remove all types in `A` that are also in `B`|Subtract union members|

---

## 📘 Syntax

```ts
Extract<A, B> // Keep common types between A and B
Exclude<A, B> // Remove types in B from A
```

Both work on **union types**, not objects.

---

## 🔍 Basic Examples

### 🔹 `Extract`

```ts
type Status = 'active' | 'inactive' | 'pending';

type LiveStatus = Extract<Status, 'active' | 'pending'>;
// Result: 'active' | 'pending'
```

### 🔸 `Exclude`

```ts
type Status = 'active' | 'inactive' | 'pending';

type ArchivedStatus = Exclude<Status, 'active'>;
// Result: 'inactive' | 'pending'
```

---

## 🌍 Real-World Use Cases

---

### ✅ 1. Role-Based Access Control (RBAC)

```ts
type Role = 'admin' | 'editor' | 'viewer';

type AdminRoles = Extract<Role, 'admin' | 'editor'>;
// Only elevated roles

type ReadOnlyRoles = Exclude<Role, 'admin'>;
// Viewer & editor, but no admin access
```

➡️ Useful for **conditional permissions** and **UI logic**.

---

### ✅ 2. API Method Filtering

```ts
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';

type SafeMethods = Exclude<HttpMethod, 'DELETE'>;
// 'GET' | 'POST' | 'PUT'
```

➡️ Use to **limit frontend forms** to safe HTTP methods.

---

### ✅ 3. Filtering Enums

```ts
type PaymentStatus = 'paid' | 'unpaid' | 'refunded' | 'error';

type Refundable = Extract<PaymentStatus, 'paid' | 'refunded'>;
// 'paid' | 'refunded'
```

➡️ Helps in modeling **business logic** clearly.

---

## 🔧 Advanced: With Custom Types

```ts
type Input = string | number | boolean;
type OnlyPrimitives = Extract<Input, string | number>; // string | number

type NotBoolean = Exclude<Input, boolean>; // string | number
```

➡️ Useful when refining types from 3rd-party libraries or `unknown`.

---

## 🤖 Interview Tip

### Question:

> “How would you narrow a union type in TypeScript?”

### Answer:

> “I’d use `Extract` to keep only desired members or `Exclude` to remove certain members. For example, `Extract<'a' | 'b' | 'c', 'a' | 'c'>` results in `'a' | 'c'`. This is helpful for permission systems, input filtering, and conditional type logic.”

---

## 🧠 Pro Tips

### ✅ Combine with `keyof`

```ts
type User = { id: string; name: string; password: string };

type SafeKeys = Exclude<keyof User, 'password'>;
// 'id' | 'name'
```

➡️ Use to safely **omit sensitive keys**.

---

### ✅ Use in Conditional Types

```ts
type OnlyStrings<T> = Extract<T, string>;

type A = OnlyStrings<string | number | boolean>; // string
```

➡️ Custom filtering logic based on type.

---

## ⚠️ Gotchas

- Only works with **union types**, not object shapes.
    
- Doesn’t go deep — no nested filtering (you need custom recursive types or libraries like `type-fest`).
    
- Can’t use on values directly, only **types**.
    

---

## 🧩 Summary Table

|Use Case|`Extract<A, B>`|`Exclude<A, B>`|
|---|---|---|
|Keep common members|✅|❌|
|Remove specific members|❌|✅|
|Filter union types|✅|✅|
|Refine keys from objects|With `keyof`|With `keyof`|

---

## ✅ Wrap-Up

- `Extract<T, U>` is like `T & U` for unions: **intersection** of union members.
    
- `Exclude<T, U>` is like `T - U`: **subtraction** of union members.
    
- Use them to **refine unions**, **build flexible APIs**, and **enforce clean logic** in your types.
    

---



Try extract and exclude on non-union object types 


```typescript
type Obj = {
	id: string;
	name: string;
};

type temp1 = Extract<Obj, 'id'> // type temp1 = never
type temp2 = Exclude<Obj, 'id'> // type temp2 = { id: string; name: string; }
```


----


### Better examples

```ts
type AlbumState =
| {
	type: "released";
	releaseDate: string;
}
| {
	type: "recording";
	studio: string;
}
| {
	type: "mixing";
	engineer: string;
};

type NotReleased1 = Exclude<AlbumState, { type: "released" }>;
/*=>
type NotReleased1 = {
	type: "recording";
	studio: string;
} | {
type: "mixing";
engineer: string;
}
*/

type NotReleased2 = Exclude<AlbumState, { releaseDate: string }>;
/*=>
type NotReleased2 = {
	type: "recording";
	studio: string;
} | {
	type: "mixing";
	engineer: string;
}
*/
```



```ts
type Example = "a" | "b" | 1 | 2 | 3 | "c" | boolean

type ExampleNumbers = Extract<Example, number>
//=> type ExampleNumbers = 1 | 2 | 3

type ExampleStrings = Extract<Example, string>
// => type ExampleStrings = "a" | "b" | "c"

type ExampleNonNumbers = Exclude<Example, number>
//=> type ExampleNonNumbers = boolean | "a" | "b" | "c"

type ExampleNonStrings = Exclude<Example, string>
//=> type ExampleNonStrings = boolean | 1 | 2 | 3


// object utilities to union type does work

// type ExampleStrings2 = Pick<Example, string>
//=: Type 'string' does not satisfy the constraint '"valueOf"'.(2344

type ExampleStrings3 = Omit<Example, string>
//=> type ExampleStrings3 = {}
```


