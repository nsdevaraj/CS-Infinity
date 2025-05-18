
# 🔁 TypeScript Mapped Types — The Ultimate Guide

Mapped types let you **create new types based on existing ones**, by “mapping” over keys and applying transformations.

Think of it as the **"for loop of types"** in TypeScript.

---

## 🧱 What Is a Mapped Type?

A **mapped type** takes a type and creates a new one by iterating over its **keys**.

### 🔤 Basic Syntax:

```ts
type NewType = {
  [K in Keys]: ValueType;
};
```

Where:

- `K` is the key name (like a loop variable)
    
- `Keys` is a union of keys (often `keyof SomeType`)
    
- `ValueType` is the type for each property
    

---

### 📌 Example 1: Convert all properties to `boolean`

```ts
type Settings = {
  darkMode: string;
  notifications: string;
};

type BooleanSettings = {
  [K in keyof Settings]: boolean;
};
// Equivalent to:
// {
//   darkMode: boolean;
//   notifications: boolean;
// }
```

---

## 🧰 Real-World Use Cases

Mapped types shine when building reusable patterns.

---

### ✅ 1. `Partial<T>` – Make all properties optional

```ts
type Partial<T> = {
  [K in keyof T]?: T[K];
};
```

Example:

```ts
type User = { id: number; name: string };

type PartialUser = Partial<User>;
// { id?: number; name?: string }
```

---

### ✅ 2. `Required<T>` – Make all properties required

```ts
type Required<T> = {
  [K in keyof T]-?: T[K];
};
```

Notice the `-?` which removes optionality.

---

### ✅ 3. `Readonly<T>` – Make all properties readonly

```ts
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};
```

---

### ✅ 4. `Record<K, T>` – Create a type with fixed keys

```ts
type Record<K extends keyof any, T> = {
  [P in K]: T;
};
```

Example:

```ts
type Role = 'admin' | 'user' | 'guest';

type RoleFlags = Record<Role, boolean>;
// {
//   admin: boolean;
//   user: boolean;
//   guest: boolean;
// }
```

---

## 🧪 Advanced Mapped Types

---

### ✂️ Transform Value Types

```ts
type WithNullable<T> = {
  [K in keyof T]: T[K] | null;
};
```

Useful for representing **nullable forms** or data from external APIs.

---

### 🚫 Remove `readonly` and `?` from a type

```ts
type Mutable<T> = {
  -readonly [K in keyof T]-?: T[K];
};
```

---

### 🧩 Conditional + Mapped Types

```ts
type OnlyStringProps<T> = {
  [K in keyof T as T[K] extends string ? K : never]: T[K];
};

type User = {
  name: string;
  age: number;
  email: string;
};

type StringOnly = OnlyStringProps<User>;
// { name: string; email: string }
```

---

## 🔧 Key Modifiers

|Modifier|Purpose|
|---|---|
|`readonly`|Add readonly|
|`-readonly`|Remove readonly|
|`?`|Make optional|
|`-?`|Remove optional|
|`as`|Rename keys during mapping (TS 4.1+)|

---

### 🔀 Example: Remap keys with `as`

```ts
type Prefixed<T> = {
  [K in keyof T as `prefix_${string & K}`]: T[K];
};

type Data = { id: number; name: string };
type PrefixedData = Prefixed<Data>;
// {
//   prefix_id: number;
//   prefix_name: string;
// }
```

---

## 💡 Best Practices

1. **Use `keyof`** to get dynamic keys.
    
2. Combine mapped types with **conditional types** for precision.
    
3. Prefer **utility types** like `Partial`, `Pick`, `Omit` for readability.
    
4. Use `as` when you need to rename keys (e.g., prefix/suffix).
    

---

## 🧠 Interview Insight

Mapped types demonstrate strong **understanding of type transformation**, useful for:

- Building type-safe APIs
    
- Creating form/validation types
    
- Meta-programming in design systems
    
- Libraries like `zod`, `react-hook-form`, `redux-toolkit`
    

📌 You may be asked to implement `Partial<T>`, `Pick<T, K>`, or `DeepReadonly<T>`.

---

## 🛠 Bonus: Deep Mapped Type (Recursive)

```ts
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};
```

---

## 🧾 Summary Table

|Task|Mapped Type Example|
|---|---|
|Make all optional|`[K in keyof T]?: T[K]`|
|Make all required|`[K in keyof T]-?: T[K]`|
|Make all readonly|`readonly [K in keyof T]: T[K]`|
|Remove readonly|`-readonly [K in keyof T]: T[K]`|
|Pick only strings|`[K in keyof T as T[K] extends string ? K : never]`|
|Prefix keys|`[K in keyof T as \`prefix_${K}`]: T[K]`|

---

Examples:



```ts

type User = {
  id: string;
  name: string;
  age: number;
};

type Prettify<T> = {
  [K in keyof T]: T[K];
} & {};

type Transform1<T> = {
  [K in keyof T]: K;
};

let t1: Prettify<Transform1<User>>;
/*=>
let t1: {
    id: "id";
    name: "name";
    age: "age";
}
*/

type Transform2<T> = {
  [K in keyof T]: [K];
};

let t2 : Prettify<Transform2<User>>;
/*=>
let t2: {
    id: ["id"];
    name: ["name"];
    age: ["age"];
}
*/


type Transform3<T> = {
  [K in keyof T]: T[K];
};

let t3 : Prettify<Transform3<User>>;
/*=>
let t3: {
    id: string;
    name: string;
    age: number;
}
*/

type Transform4<T> = {
  readonly [K in keyof T]?: T[K];
};

let t4 : Prettify<Transform4<User>>;
/*=>
let t4: {
    readonly id?: string | undefined;
    readonly name?: string | undefined;
    readonly age?: number | undefined;
}
*/


// type Transform5<T> = {
//   [K in keyof T as Capitalize<K>]: T[K];
// };
/*=:
Type 'K' does not satisfy the constraint 'string'.
  Type 'keyof T' is not assignable to type 'string'.
    Type 'string | number | symbol' is not assignable to type 'string'.
      Type 'number' is not assignable to type 'string'.(2344)
(type parameter) K
*/

type Transform5<T> = {
  [K in Extract<keyof T, string> as Capitalize<K>]: T[K];
};

let t5: Prettify<Transform5<User>>;
/*=>
let t5: {
    Id: string;
    Name: string;
    Age: number;
}
*/


type Transform6<T> = {
  [K in Extract<keyof T, string> as `get${Capitalize<K>}`]: () => T[K];
};

let t6: Prettify<Transform6<User>>;
/*=>
let t6: {
    getId: () => string;
    getName: () => string;
    getAge: () => number;
}
*/


```



---

# ⚡️ IIMT: Immediately Invoked Mapped Types in TypeScript

> **IIMT** is not an official TypeScript term — it's a nickname (inspired by IIFEs in JavaScript) for using **mapped types immediately as inline type expressions** instead of defining them separately.

---

## 🤔 The Analogy

Think of this like an **IIFE (Immediately Invoked Function Expression)** in JavaScript:

```ts
const result = ((x) => x * 2)(4);
```

Now, instead of defining a mapped type first, you **inline it directly**:

### 🧠 Instead of:

```ts
type Stringified<T> = {
  [K in keyof T]: string;
};

type UserString = Stringified<User>;
```

### 🚀 You write:

```ts
type UserString = {
  [K in keyof User]: string;
};
```

You're “invoking” the mapped type directly — hence the term **Immediately Invoked Mapped Type**.

---

## 📌 When and Why Use IIMTs?

### ✅ 1. **Avoid Repetition in One-Off Cases**

Why define a new reusable type if you're only using it once?

```ts
type ApiResponse = {
  data: {
    [K in keyof User]: string;
  };
  success: boolean;
};
```

### ✅ 2. **Quick Transformations in-place**

When doing on-the-fly transformations without cluttering your type namespace.

```ts
type FormFields = {
  [K in keyof User as `form_${K}`]: string;
};
```

### ✅ 3. **Clean Up Utility Compositions**

If you're already deep in `Pick`, `Omit`, etc., and need to apply a tweak:

```ts
type ReadonlyPick = {
  readonly [K in keyof Pick<User, 'id' | 'email'>]: User[K];
};
```

---

## 🧪 Real-World Examples

### 🧩 Prefixed Keys with IIMT

```ts
type Prefixed = {
  [K in keyof User as `user_${string & K}`]: User[K];
};
```

### 🧩 Make API version of type

```ts
type Apiified = {
  [K in keyof User]: { value: User[K]; isValid: boolean };
};
```

Instead of defining a separate utility like `ApiWrapper<T>`.

---

## 🔄 Combine with Utility Types

You can **nest** them with existing utility types:

```ts
type OptionalAndPrefixed = Partial<{
  [K in keyof User as `opt_${string & K}`]: User[K];
}>;
```

This makes `opt_id?`, `opt_name?`, etc.

---

## 🧠 Type Inference Works Well

Because these are just standard mapped types, the compiler can still infer, autocomplete, and check types.

---

## 💡 Advanced Usage: IIMT + Conditional Types

```ts
type OnlyStrings = {
  [K in keyof T as T[K] extends string ? K : never]: T[K]
};
```

You can drop that directly into:

```ts
type StringPropsOfUser = {
  [K in keyof User as User[K] extends string ? K : never]: User[K];
};
```

No need to create a `StringProps<T>` helper unless reused multiple times.

---

## 🧰 Best Practices

|When to use IIMT|When to extract into a named type|
|---|---|
|One-off transformation|Reused in multiple places|
|Inside nested or complex types|You want better readability|
|Utility building (e.g. with `Partial`, `Pick`, `Record`)|Used across files or libraries|

---

## 🧠 Interview Insight

> Knowing how to use mapped types immediately (without cluttering with separate type aliases) shows **deep fluency with the type system**. It's like using arrow functions fluently in JavaScript—concise, readable, powerful.

An interviewer might ask:

> "How would you make all properties of `User` optional and prefixed with `'custom_'`?"

Your IIMT answer:

```ts
type CustomUser = {
  [K in keyof User as `custom_${string & K}`]?: User[K];
};
```

No helper types needed — clean and confident.

---

## 🧾 Summary

|Concept|Description|
|---|---|
|IIMT|An inline mapped type used immediately|
|Benefits|Cleaner code, no extra type declarations|
|Use Cases|Transformations, prefixed/suffixed keys, one-offs|
|Type Safety|Fully type-safe with inference and autocomplete|
|Composition|Works with `Pick`, `Omit`, `Partial`, etc.|

---

## 🚀 Want More?

Would you like:

- A visual diagram comparing IIMT vs helper types?
    
- A cheat sheet PDF of mapped type patterns?
    
- Live examples on TypeScript Playground?
    

---

Examples

```ts

type Prettify<T> = {
  [K in keyof T]: T[K];
} & {};


type Actions = {
  login: {
    name: string;
    pwd : string;
  };
  lougout: {
    reason: string;
  };
  update : {
    id:string;
    data: unknown;
  };
}

type ActionAsDiscoUnion1 = {
  [K in keyof Actions] : {};
}
/*=>
type ActionAsDiscoUnion1 = {
    login: {};
    lougout: {};
    update: {};
}
*/

type ActionAsDiscoUnion2 = {
  [K in keyof Actions] : {
    type: K
  };
}
/*=>
type ActionAsDiscoUnion2 = {
    login: {
        type: "login";
    };
    lougout: {
        type: "lougout";
    };
    update: {
        type: "update";
    };
}
*/


type ActionAsDiscoUnion3 ={
    [K in keyof Actions] : Prettify<{
    type: K
  } & Actions[K]>;
}
/*=>
type ActionAsDiscoUnion3 = {
    login: {
        type: "login";
        name: string;
        pwd: string;
    };
    lougout: {
        type: "lougout";
        reason: string;
    };
    update: {
        type: "update";
        id: string;
        data: unknown;
    };
}
*/

// Make into union type using IIMT
type ActionAsDiscoUnion4 ={
    [K in keyof Actions] : Prettify<{
    type: K
  } & Actions[K]>;
}[keyof Actions]
/*=>
type ActionAsDiscoUnion4 = {
    type: "login";
    name: string;
    pwd: string;
} | {
    type: "lougout";
    reason: string;
} | {
    type: "update";
    id: string;
    data: unknown;
}
*/

type AllValues = Actions[keyof Actions]
/*=>
type AllValues = {
    name: string;
    pwd: string;
} | {
    reason: string;
} | {
    id: string;
    data: unknown;
}
*/
type LogValues = Actions['login' | 'lougout']
/*=>
type LogValues = {
    name: string;
    pwd: string;
} | {
    reason: string;
}
*/

```