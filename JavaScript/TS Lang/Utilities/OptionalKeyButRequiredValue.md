
To make a **key optional** but **its value required when the key is present**, you can use a mapped type with conditional logic.

---

### ✅ Goal:

- The key may or may not exist (`optional key`)
    
- If it **does** exist, its **value must not be undefined or null**
    

---

### ✅ TypeScript Solution:

Here's how you can define that pattern:

```ts
type OptionalKeyButRequiredValue<T> = {
  [K in keyof T]?: T[K];
} & {
  [K in keyof T as K extends keyof T ? K : never]?: Exclude<T[K], undefined | null>;
};
```

But to simplify: this is often better handled by modeling each field individually.

### 🔧 Practical Example

```ts
type Example = {
  id?: string; // ✅ Optional key, value required if present
  name?: string; // ✅ Optional key, value required if present
};
```

#### How to enforce non-undefined if present?

You can use a custom utility like this:

```ts
type OptionalKeys<T> = {
  [K in keyof T]?: Exclude<T[K], undefined | null>;
};
```

```ts
type MyObj = OptionalKeys<{
  id: string | undefined;
  name: string | null;
}>;

// ✅ { id?: string; name?: string }
```

- `id` is optional
    
- But if present, must be a **string**, not `undefined`
    
- Similarly for `name`
    

---

### ❌ What Doesn’t Work

```ts
type MyObj = {
  id?: string;
}
```

This allows `id: undefined` explicitly — not what you want.

---

### ✅ Best Final Utility

```ts
type OptionalStrict<T> = {
  [K in keyof T]?: Exclude<T[K], undefined | null>;
};

type User = OptionalStrict<{
  id: string | undefined;
  name: string | null;
}>;

// ✅ Result:
// {
//   id?: string;
//   name?: string;
// }
```

This ensures that:

- Keys are optional
    
- Values are required (if the key is present)
    

Let me know if you want stricter versions (e.g., no empty strings, etc).