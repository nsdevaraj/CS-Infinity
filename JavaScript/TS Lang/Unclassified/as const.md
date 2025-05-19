

# **Understanding `as const` in TypeScript: Deep Dive**

TypeScript is known for its powerful type system, giving developers the tools to write safer and more expressive code. One of the lesser-known but incredibly useful features of this system is the `as const` assertion.

You might have seen it used in some advanced TypeScript code and wondered:

> What exactly does `as const` do?  
> Why is it useful?  
> When should I use it?

Let’s break it down.

---

## 🔍 **What Is `as const`?**

The `as const` assertion tells TypeScript to **infer the most specific (or literal) types possible** for an expression, rather than general or "wider" types.

In plain JavaScript, when you declare a value like this:

```ts
const colors = ["red", "green", "blue"];
```

TypeScript infers this as:

```ts
const colors: string[]
```

But if you add `as const`:

```ts
const colors = ["red", "green", "blue"] as const;
```

TypeScript infers:

```ts
const colors: readonly ["red", "green", "blue"]
```

Now:

- The array is **immutable** (`readonly`)
- Each item has a **literal type**: `'red'`, `'green'`, and `'blue'`


This is the power of `as const`.


its just POJO ( Plain Old Javascript Object) but with as const.. 


```ts
const LOG_LEVEL = {
    DEBUG: "DEBUG",
    WARNING: "WARNING",
    ERROR: "ERROR",
} as const;

type ObjectValues<T> = T [keyof T];

type LogLevel = ObjectValues<typeof LOG_LEVEL>
//=> type LogLevel = "DEBUG" | "WARNING" | "ERROR"

```



```ts
// 1. Define a reusable readonly tuple type
type Point = readonly [number, number];

// 2. Function that accepts a readonly tuple
function logCoords(coords: Point) {
    console.log(coords);
}

// 3. Use a literal readonly tuple
const point = [10, 20] as const;

logCoords(point); // ✅ Works perfectly


//.js
/*=>
"use strict";
// 2. Function that accepts a readonly tuple
function logCoords(coords) {
    console.log(coords);
}
// 3. Use a literal readonly tuple
const point = [10, 20];
logCoords(point); // ✅ Works perfectly
*/

//.d.ts
// type Point = readonly [number, number];
// declare function logCoords(coords: Point): void;
// declare const point: readonly [10, 20];
```


---

## 🔬 **How It Works: Literal Narrowing**

Normally, TypeScript **widens** the types of literals:

```ts
const direction = "left"; // type: string
```

But with `as const`:

```ts
const direction = "left" as const; // type: "left"
```

This is known as **literal narrowing**—you’re telling TypeScript:

> “Don’t widen this to a general `string`. Keep it exactly as `'left'`.”

---

## ✅ **Why Use `as const`?**

### 1. **Defining Discriminated Unions**

```ts
const statuses = ["loading", "success", "error"] as const;

type Status = typeof statuses[number]; 
// type Status = "loading" | "success" | "error"
```

This is a clean and maintainable way to define union types based on a list of strings.

---

### 2. **Immutable Objects**

```ts
const config = {
  apiUrl: "https://api.example.com",
  retryAttempts: 3
} as const;
```

This will result in:

```ts
const config: {
  readonly apiUrl: "https://api.example.com";
  readonly retryAttempts: 3;
}
```

Both properties are now **immutable and have literal types**.

---

### 3. **Safe Enums (Enum Alternatives)**

Instead of:

```ts
enum Direction {
  Up = "UP",
  Down = "DOWN"
}
```

Use:

```ts
const Direction = {
  Up: "UP",
  Down: "DOWN"
} as const;

type Direction = typeof Direction[keyof typeof Direction]; 
// "UP" | "DOWN"
```

Benefits:

- Works better with tree-shaking
- Avoids runtime overhead of enums
- More readable and JS-friendly

---

### 4. **Tuple Inference in Function Parameters**

```ts
function logCoords(coords: [number, number]) {
  // ...
}

const point = [10, 20] as const;

logCoords(point); // ✅ ok
```

Without `as const`, TypeScript sees `point` as `number[]` (not `[number, number]`) and would throw a type error.

---

## 🧠 `as const` vs Other Type Assertions

You might wonder how `as const` compares to:

```ts
const x = "hello" as "hello";
```

This is a **manual literal assertion**. It works, but is verbose and not scalable.

With `as const`, **entire structures**—arrays, objects, tuples—can be locked into their exact, literal types in a single expression.

---

## ⚠️ Things to Keep in Mind

### 1. **Read-only Behavior**

When you use `as const`, the resulting array or object becomes **immutable**:

```ts
const nums = [1, 2, 3] as const;

nums[0] = 10; // ❌ Error: Readonly
```

If you need to modify the structure, `as const` may not be the right tool.

---

### 2. **Not for Runtime Logic**

Remember: `as const` is **purely a compile-time construct**. It doesn’t affect JavaScript behavior—it only affects how TypeScript infers types.

---

### 3. **Use Sparingly—but Strategically**

While `as const` is powerful, overusing it can make types overly rigid. It shines in:

- Configuration objects
    
- Static data
    
- API constants
    
- Action types in Redux-style patterns
    

---

## 🛠️ Real-World Use Case: Redux Action Types

```ts
const ADD_TODO = "ADD_TODO" as const;

type Action = 
  | { type: typeof ADD_TODO; payload: string }
  | { type: "REMOVE_TODO"; payload: number };
```

This pattern helps TypeScript **discriminate** between actions precisely and safely.


---

Semantic key vs actual real world value - greatly possible in enum

```ts
const LOG_LEVEL = {
    DEBUG: "debuging",
    WARNING: "warning",
    ERROR: "oopsError",
} as const;
/*=>
const LOG_LEVEL: {
    readonly DEBUG: "debuging";
    readonly WARNING: "warning";
    readonly ERROR: "oopsError";
}
*/

type ObjectValues<T> = T [keyof T];

type LogLevelRealWorld = ObjectValues<typeof LOG_LEVEL>
//=> type LogLevelRealWorld = "debuging" | "warning" | "oopsError"


type LogLevelSemantic = keyof typeof LOG_LEVEL
//=> type LogLevelSemantic = "DEBUG" | "WARNING" | "ERROR"

// value map can be done in object with semantic key
const value = LOG_LEVEL['DEBUG'] //=> "debuging"


```

---

## 📌 Summary

|Feature|Without `as const`|With `as const`|
|---|---|---|
|Literal types|Widened (`string`, etc.)|Narrowed (`"foo"`, etc.)|
|Array type|Mutable (`string[]`)|Readonly Tuple (`readonly ["foo", "bar"]`)|
|Object properties|Mutable and general|Immutable and literal|
|Use case|General-purpose values|Constants, Enums, Immutable configs|

---

## 🚀 Final Thoughts

The `as const` assertion in TypeScript is a **small feature** with **big power**. It unlocks a more **precise**, **predictable**, and **immutable** typing system—especially for constants, tuples, and config objects.

If you're writing code that shouldn’t change and want TypeScript to help enforce that, reach for `as const`.

---

🔗 **Further Reading**:

- [TypeScript Handbook - Literal Types](https://www.typescriptlang.org/docs/handbook/literal-types.html)
- [TypeScript Playground - Try `as const`](https://www.typescriptlang.org/play)



---


```ts
const routes1 = {
  home: "/",
  admin: "/admin",
  user: "/user",
};
/*=>
const routes1: {
    home: string;
    admin: string;
    user: string;
}
*/

const goToRoute1 = (route: "/" | "/admin" | "/user") => {};

// goToRoute1('Temp')
//=: Argument of type '"Temp"' is not assignable to parameter of type '"/" | "/admin" | "/user"'.

// const temp = {text: 'text'}
// goToRoute1(temp.text)
//=: Argument of type 'string' is not assignable to parameter of type '"/" | "/admin" | "/user"'

// even this won't work
// goToRoute1(routes1.home)
//=: Argument of type 'string' is not assignable to parameter of type '"/" | "/admin" | "/user"'

// reason : obj can be changed
// routes1.admin = 'admin'
// goToRoute1(routes1.admin)
//=: Argument of type 'string' is not assignable to parameter of type '"/" | "/admin" | "/user"'

const routes2 = {
  home: "/",
  admin: "/admin",
  user: "/user",
} as const;
/*=>
const routes2: {
    readonly home: "/";
    readonly admin: "/admin";
    readonly user: "/user";
}
*/

// routes2.admin = 'admin'
//=: Cannot assign to 'admin' because it is a read-only property.

goToRoute1(routes2.admin);
// as const made object readonly, so direct literals can be taken here

const routes3 = Object.freeze({
  home: "/",
  admin: "/admin",
  user: "/user",
});
/*=>
const routes3: Readonly<{
    home: "/";
    admin: "/admin";
    user: "/user";
}>
*/

// Object.freeze make readonly in runtime, and doesn't go deeper

// routes3.admin = 'admin'
//=: Cannot assign to 'admin' because it is a read-only property.

goToRoute1(routes2.admin);
// readonly , so /admin is consider as string literal

const deepObj1 = {
  key1: "value1",
  key2: {
    key3: "value3",
  },
} as const;
/*=>
const deepObj1: {
    readonly key1: "value1";
    readonly key2: {
        readonly key3: "value3";
    };
}
*/

// deepObj1['key2']['key3'] = 'temp';
//=: Cannot assign to ''key3'' because it is a read-only property.

const deepObj2 = Object.freeze({
  key1: "value1",
  key2: {
    key3: "value3",
  },
});
/*=>
const deepObj2: Readonly<{
    key1: "value1";
    key2: {
        key3: string;
    };
}>
*/

// deepObj2['key2']['key4'] = 'temp';
// Element implicitly has an 'any' type because expression of type '"key4"' can't be used to index type '{ key3: string; }'.

deepObj2["key2"]["key3"] = "temp";
// which is wrong to set any string here

const routes4 = {
  home: "/",
  admin: "/admin",
  user: "/user",
} as const;
/*=>
const routes4: {
    readonly home: "/";
    readonly admin: "/admin";
    readonly user: "/user";
}
*/

type RouteType = typeof routes4;
/*=>
type RouteType = {
    readonly home: "/";
    readonly admin: "/admin";
    readonly user: "/user";
}
*/

type RouteKeys = keyof RouteType;
/*=>
type RouteKeys = "home" | "admin" | "user"
*/

// doing object.values in type level
type Route = RouteType[RouteKeys];
// or type Route = (typeof routes4)[keyof typeof routes4]
/*=>
type Route = "/" | "/admin" | "/user"
*/

const goToRoute2 = (route: Route) => {};

type AdminRoute = (typeof routes4)["admin"];
//=> type AdminRoute = "/admin"

type nonAdminRoute = (typeof routes4)["home" | "user"];
//=> type nonAdminRoute = "/" | "/user"

```



referred {

https://www.youtube.com/watch?v=6M9aZzm-kEc

}