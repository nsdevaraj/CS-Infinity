 **TypeScript** provides ways to check whether an **inferred type** matches an **explicit type**, but it doesn't do this at runtime — it's purely a **compile-time, type-level check**.

You can write helper utilities to **assert type equality** using TypeScript's type system. These are mainly used in libraries, tests, or development tooling to ensure your types are behaving as expected.

---

## ✅ Check if Inferred and Explicit Types Are the Same

Here’s how you can do it:

### 1. **Type Utility: `AssertEqual`**

```ts
type AssertEqual<A, B> =
  (<T>() => T extends A ? 1 : 2) extends
  (<T>() => T extends B ? 1 : 2) ? true : false;
```

This utility compares two types. If they are **exactly** the same, it resolves to `true`, otherwise `false`.

---

### 2. **Example Usage:**

```ts
// Inferred type
const x = {
  id: 123,
  name: "Alice"
};

// Explicit type
type ExplicitType = {
  id: number;
  name: string;
};

// TypeScript will infer this type
type InferredType = typeof x;

// Check if they are the same
type Test = AssertEqual<InferredType, ExplicitType>; // true
```

---

### 3. **Using `@ts-expect-error` for Hard Checks**

If you're testing explicitly whether something _should not compile_ (e.g., types are not the same), you can use:

```ts
// @ts-expect-error
type NotEqual = AssertEqual<InferredType, { id: string; name: string }>; // should error
```

---

## ✅ Use in Testing (Optional)

If you're using **TypeScript in a monorepo or lib**, some testing tools like `tsd` can be used to assert types during CI:

```bash
npm install --save-dev tsd
```

Write test files like:

```ts
import { expectType } from 'tsd';

expectType<ExplicitType>(x); // pass if x matches ExplicitType
```

---

## 🛠️ Summary

|Feature|Description|
|---|---|
|`AssertEqual<A, B>`|Checks if two types are exactly equal|
|`typeof`|Gets the inferred type of a variable|
|`@ts-expect-error`|Validates that something _should fail_|
|`tsd`|External tool to test types in CI|

Let me know if you want a ready-to-use utility file or a VS Code snippet!