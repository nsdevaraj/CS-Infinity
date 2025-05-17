
# 🔧 Beyond `Prettify`: Powerful Custom TypeScript Utilities

Here are **commonly used custom utility types** that solve real problems in real apps—like flattening types, making fields conditional, enforcing exactness, and more.

---

## 1️⃣ `Prettify<T>`

You already know this one. It flattens intersections and makes complex types readable.

```ts
type Prettify<T> = {
  [K in keyof T]: T[K];
} & {};
```

---

## 2️⃣ `Merge<A, B>`

Combines two object types, with B overwriting A’s overlapping keys—**flattened automatically**.

```ts
type Merge<A, B> = Prettify<Omit<A, keyof B> & B>;

type A = { id: string; name: string };
type B = { name: number; age: number };

type Merged = Merge<A, B>; 
// { id: string; name: number; age: number }
```

✅ Use when combining config objects, form schemas, etc.

---

## 3️⃣ `Mutable<T>`

Removes `readonly` from all fields.

```ts
type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

type ReadonlyUser = {
  readonly id: string;
  readonly name: string;
};

type MutableUser = Mutable<ReadonlyUser>;
```

---

## 4️⃣ `DeepPartial<T>`

Makes all nested fields optional (recursive `Partial`).

```ts
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};
```

✅ Great for nested form data, partial updates.

---

## 5️⃣ `DeepRequired<T>`

Make all fields deeply required.

```ts
type DeepRequired<T> = {
  [K in keyof T]-?: T[K] extends object ? DeepRequired<T[K]> : T[K];
};
```

---

## 6️⃣ `Exact<T, Shape>`

Restricts extra properties. TypeScript by default allows excess properties in object literals—this helps prevent that.

```ts
type Exact<T, Shape> = T extends Shape
  ? Exclude<keyof T, keyof Shape> extends never
    ? T
    : never
  : never;
```

✅ Helps enforce **strict typing** for API contracts or DTOs.

---

## 7️⃣ `UnionToIntersection<U>`

Turns a union into an intersection.

```ts
type UnionToIntersection<U> = 
  (U extends any ? (k: U) => void : never) extends (k: infer I) => void
    ? I
    : never;

type A = { a: string };
type B = { b: number };

type Inter = UnionToIntersection<A | B>; 
// => { a: string } & { b: number }
```

✅ Used in advanced generics and inference patterns.

---

## 8️⃣ `KeysOfType<T, Type>`

Get keys of a specific type from an object.

```ts
type KeysOfType<T, V> = {
  [K in keyof T]: T[K] extends V ? K : never;
}[keyof T];

type Example = { a: string; b: number; c: string };
type StringKeys = KeysOfType<Example, string>; 
// "a" | "c"
```

---

## 9️⃣ `OptionalKeys<T>`, `RequiredKeys<T>`

Extract only optional or required keys from a type.

```ts
type OptionalKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? K : never;
}[keyof T];

type RequiredKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? never : K;
}[keyof T];
```

✅ Useful for advanced validation and schema generation.

---

## 🔟 `Override<Base, Override>` (Safe overwriting)

```ts
type Override<A, B> = Prettify<Omit<A, keyof B> & B>;
```

Same idea as `Merge`, but semantically clearer for API overrides, prop merging, or theme customization.

---

## ✅ Summary Table

|Utility|Purpose|
|---|---|
|`Prettify<T>`|Flatten types for readability|
|`Merge<A, B>`|Merge two types, `B` wins on conflicts|
|`Mutable<T>`|Make readonly fields mutable|
|`DeepPartial<T>`|Optional at all levels|
|`DeepRequired<T>`|All fields required, recursively|
|`Exact<T, U>`|Disallow extra keys|
|`UnionToIntersection<U>`|Convert union to intersection|
|`KeysOfType<T, V>`|Get keys of a certain value type|
|`OptionalKeys<T>`|Extract only optional keys|
|`Override<A, B>`|Safely override type members|

---

## 🧠 Bonus Tip: Compose These!

You can combine them for more power:

```ts
type SafeUpdate<T, U> = Prettify<Override<DeepPartial<T>, U>>;
```

➡️ Allows deep partial updates, then merges in `U`.

---

## Want More?

Would you like:

- A sharable GitHub cheatsheet version of this?
    
- A type-safe snippet collection for VSCode?
    
- Or a React-focused version of these utilities?
    

