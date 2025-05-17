
# 🛠️ TypeScript `Partial` vs `Required`: Explained with Real Examples

In TypeScript, utility types like `Partial` and `Required` let you transform object types in powerful ways. They're essential when you need to create **flexible models** for APIs, forms, or state management.

---

## 🔍 What Are They?

### 🔹 `Partial<Type>`

Turns **all properties** of a type into **optional**.

```ts
type Partial<T> = {
  [P in keyof T]?: T[P];
};
```

#### ✅ Example:

```ts
type User = {
  id: string;
  name: string;
  email: string;
};

type PartialUser = Partial<User>;

const update: PartialUser = {
  name: "Alice" // ✅ OK — other fields optional
};
```

➡️ Use when: you're **updating**, **initializing**, or **patching** objects gradually.

---

### 🔸 `Required<Type>`

Turns **all properties** into **non-optional** (even if the original was optional).

```ts
type Required<T> = {
  [P in keyof T]-?: T[P];
};
```

#### ✅ Example:

```ts
type Config = {
  theme?: string;
  debug?: boolean;
};

type StrictConfig = Required<Config>;

const cfg: StrictConfig = {
  theme: "dark",
  debug: true
}; // ✅ all fields now required
```

➡️ Use when: you're **ensuring completeness** before using an object.

---

## 🎯 Real-World Use Cases

### 🧩 `Partial` — Update APIs or Form Drafts

```ts
function updateUser(id: string, updates: Partial<User>) {
  // Only some fields may be updated
}
```

- Great for **PATCH** endpoints
    
- Useful when editing forms — some fields may be untouched
    

---

### 🧩 `Required` — Final validation

```ts
function saveConfig(config: Required<Config>) {
  // Safe to assume all fields are filled
}
```

- Enforce completeness before saving
    
- Avoid undefined errors later
    

---

## 🤖 Interview Talk Track

> **Q:** "What is `Partial` in TypeScript, and when would you use it?"
> 
> **A:** "`Partial` makes all properties of a type optional. It’s useful when working with update patterns, like PATCH requests or form drafts where not all data is available at once. For example, `Partial<User>` lets you pass just the name to update."

> **Q:** "And how about `Required`?"
> 
> **A:** "`Required` is the opposite—it forces all properties to be present. It's perfect for validation before using data where optional fields are no longer acceptable."

---

## 🧠 Pro Tips

### ✅ Combine with `Pick` or `Omit`

```ts
type OptionalEmail = Partial<Pick<User, 'email'>>;
```

➡️ Makes just `email` optional, not the whole type.

### ✅ Narrow scope

```ts
type WithRequiredName = Required<Pick<User, 'name'>> & Omit<User, 'name'>;
```

➡️ Makes only `name` required, leaves other fields as-is.

---

## ⚠️ Gotchas

- `Partial` does **not** make nested properties optional.
    
    ```ts
    type Nested = { profile: { age: number } };
    Partial<Nested> // ✅ profile is optional, but profile.age is still required
    ```
    
- For deep versions, use libraries like:
    
    - `type-fest` (`DeepPartial`)
        
    - Custom recursive utility types
        

---

## 📦 Summary Table

|Feature|`Partial<T>`|`Required<T>`|
|---|---|---|
|All props optional|✅|❌|
|All props required|❌|✅|
|Use for|Form drafts, PATCH APIs|Validation, complete config check|
|Nested support|❌ (shallow only)|❌ (shallow only)|
|Composable|✅ with `Pick`, `Omit`, etc.|✅|

---

## ✅ TL;DR

- Use `Partial<T>` when:
    
    - You want flexibility
        
    - Updating or gradually building an object
        
- Use `Required<T>` when:
    
    - You want to ensure all fields are set before proceeding
        
    - You're validating config, input, or data structure integrity
        

---

# 🧩 Composability of `Partial` and `Required` in TypeScript

TypeScript’s utility types are **first-class citizens** that can be combined like building blocks. `Partial` and `Required` can be composed with:

- `Pick`
    
- `Omit`
    
- `Readonly`
    
- `Record`
    
- Custom types
    

This gives you **granular control** over how you transform existing types.

---

## 🎯 Use Cases & Examples

---

### 1️⃣ **Partial + Pick**

Make **some fields optional**, not the whole object.

```ts
type User = {
  id: string;
  name: string;
  email: string;
  password: string;
};

type UserUpdateFields = Partial<Pick<User, 'name' | 'email'>>;

const updateUser: UserUpdateFields = {
  name: 'New Name' // ✅ OK
};
```

➡️ ✅ Only `name` and `email` are optional. The rest are excluded.

---

### 2️⃣ **Required + Pick**

Force certain optional fields to be **required**.

```ts
type Config = {
  theme?: string;
  debug?: boolean;
  version?: number;
};

type StrictThemeConfig = Required<Pick<Config, 'theme'>>;

const cfg: StrictThemeConfig = {
  theme: 'dark' // ✅ required now
};
```

➡️ ✅ Only `theme` is enforced as required.

---

### 3️⃣ **Partial + Omit**

Make everything optional **except** a few fields.

```ts
type User = {
  id: string;
  name: string;
  email: string;
  password: string;
};

type PartialUser = Partial<Omit<User, 'id'>> & Pick<User, 'id'>;

const user: PartialUser = {
  id: 'u1' // ✅ required
  // name, email, password = optional
};
```

➡️ Use this to keep `id` required while relaxing other fields.

---

### 4️⃣ **Required + Partial** (Scoped required)

You can selectively require one field while keeping others optional.

```ts
type Profile = {
  name?: string;
  email?: string;
  bio?: string;
};

// Require only 'email', keep others optional
type EmailRequired = Required<Pick<Profile, 'email'>> & Partial<Omit<Profile, 'email'>>;

const user: EmailRequired = {
  email: 'me@example.com' // ✅ must have this
};
```

➡️ Useful for phased validation or multi-step forms.

---

### 5️⃣ **Combine with Readonly**

Make parts of a type optional AND read-only.

```ts
type ReadOnlyOptionalUser = Readonly<Partial<Pick<User, 'name' | 'email'>>>;

const user: ReadOnlyOptionalUser = {
  name: "Alice"
};

// user.name = "Bob"; ❌ Error — it's readonly
```

---

## 🧠 Interview-Ready Summary

> **Q: Can you selectively make certain fields optional or required in TypeScript?**
> 
> ✅ Yes! TypeScript allows you to compose `Partial` and `Required` with `Pick`, `Omit`, and others. For example:
> 
> - `Partial<Pick<T, 'name'>>` makes only `'name'` optional.
>     
> - `Required<Pick<T, 'email'>>` forces `'email'` to be present.
>     
> - Combining them gives you fine-grained control over object shapes.
>     

---

## ⚙️ Advanced Tip: Create Reusable Helpers

```ts
type RequireOnly<T, K extends keyof T> = Required<Pick<T, K>> & Partial<Omit<T, K>>;
type OptionalOnly<T, K extends keyof T> = Partial<Pick<T, K>> & Required<Omit<T, K>>;
```

Now use like this:

```ts
type FormData = {
  name: string;
  email: string;
  phone: string;
};

type Step1 = RequireOnly<FormData, 'name'>; // only 'name' is required
type Step2 = OptionalOnly<FormData, 'phone'>; // only 'phone' is optional
```

---

## ✅ TL;DR – Composability Patterns

|Pattern|Meaning|
|---|---|
|`Partial<Pick<T, K>>`|Only `K` fields are optional|
|`Required<Pick<T, K>>`|Only `K` fields are required|
|`Partial<Omit<T, K>> & Pick<T, K>`|Keep `K` required, make others optional|
|`Required<Omit<T, K>> & Partial<Pick<T, K>>`|Keep `K` optional, others required|
|`Readonly<Partial<T>>`|All optional and read-only|

---

