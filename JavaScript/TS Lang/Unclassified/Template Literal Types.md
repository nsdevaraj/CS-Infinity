


## 📘 What Are Template Literal Types?

Template literal types let you **construct string literal types dynamically**, much like JavaScript string interpolation (`` `${value}` ``), but in the **type system**.

```ts
type Greeting = `Hello, ${string}`; // "Hello, John", "Hello, world", etc.
```

They were introduced in **TypeScript 4.1** and allow you to build **powerful, type-safe string patterns**.

---

## 🔤 Basic Syntax

```ts
type Prefix = "user";
type UserId = `${Prefix}_${number}`; // e.g., "user_1", "user_42"
```

Here, `UserId` is a type that matches strings like `"user_123"`, `"user_999"`, but **not** `"admin_1"` or `"user_"`.

---

## 🧠 Why Use Them?

- Enforce naming conventions
    
- Create discriminated unions
    
- Safely map object keys
    
- Combine with conditional and infer types for meta-programming
    

---

## 🔍 Detailed Examples

### 1. **Combining Literals**

```ts
type Lang = "en" | "fr" | "de";
type Page = "home" | "about";

type Route = `/${Lang}/${Page}`;

// Valid:
const route1: Route = "/en/home";

// Invalid:
const route2: Route = "/it/home"; // ❌ Type error
```

---

### 2. **Tagging Keys Dynamically**

```ts
type ButtonVariants = "primary" | "secondary";
type ButtonClass = `btn-${ButtonVariants}`;

// Accepts: "btn-primary", "btn-secondary"
const cls: ButtonClass = "btn-primary";
```

---

### 3. **Mapping Object Keys**

```ts
type Options = "bold" | "italic";
type Flags = {
  [K in Options as `is${Capitalize<K>}`]: boolean;
};

// Equivalent to:
// type Flags = {
//   isBold: boolean;
//   isItalic: boolean;
// }
```

> 🧠 `Capitalize<K>` is a **built-in utility type** that transforms `"bold"` to `"Bold"`.

---

### 4. **Validating Specific String Patterns**

```ts
type UUID = `${string}-${string}-${string}-${string}-${string}`;

function isUUID(id: UUID): boolean {
  return id.length === 36;
}

// isUUID("abc-def-ghi-jkl-mno"); ✅
// isUUID("not-a-uuid"); ❌ type error
```

---

## 🔁 With `infer` and Conditionals

```ts
type ExtractLang<T> = T extends `${infer Lang}/${string}` ? Lang : never;

type L1 = ExtractLang<"en/home">; // "en"
type L2 = ExtractLang<"/home">;   // never
```

- `infer` extracts parts of a string based on a template.
    
- Extremely useful for building types from routes, keys, etc.
    

---

## 🧪 Practical Use Case: API Versioning

```ts
type Version = "v1" | "v2";
type Endpoint = "login" | "logout";

type ApiRoute = `/api/${Version}/${Endpoint}`;

// Example: "/api/v1/login"
```

---

## 🛠️ Limitations

- Not runtime-validated — still just types.
    
- Only works at compile time.
    
- Can become complex and hard to read if overused.
    

---

## 📝 Summary

|Feature|Description|
|---|---|
|🔗 Compose types|Use `${}` to interpolate types into strings|
|🛠 Pattern enforcement|Enforce format for strings like IDs, URLs|
|🧠 Works with infer|Extract info from types using `infer`|
|🔤 Combine with utilities|Use `Capitalize`, `Lowercase`, etc.|

---

Would you like to try a hands-on challenge or explore template literals with enums or classes next?