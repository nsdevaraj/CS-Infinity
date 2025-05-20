
 TypeScript patterns or features that are commonly used but **not recommended** (or at least should be used cautiously or with alternatives in mind):

---

## 🚫 1. **Enums** — Prefer `as const` with union types

You're aware of this, but to recap why it's discouraged:

### Problem:

```ts
enum Color {
  Red,
  Green,
  Blue
}
```

- Adds JavaScript output (not zero-cost).
    
- Can behave unexpectedly with reverse mapping.
    
- Not tree-shakable.
    

### Better:

```ts
const Colors = {
  Red: "Red",
  Green: "Green",
  Blue: "Blue",
} as const;

type Color = typeof Colors[keyof typeof Colors];
```

---

## 🚫 2. **Non-null assertions (`!`)** — Use cautiously

### Problem:

```ts
const value: string = possiblyNullValue!;
```

- **Silences** compiler warnings instead of solving them.
    
- Can lead to runtime errors if assumption is wrong.
    
- Often used as a shortcut in legacy codebases.
    

### Better:

Use actual null checks or optional chaining:

```ts
if (possiblyNullValue != null) {
  // safe to use
}
```

---

## 🚫 3. **`any` Type** — TypeScript escape hatch

### Problem:

```ts
let userData: any = getUserData();
```

- Disables all type checking.
    
- Defeats the purpose of TypeScript.
    
- Easily leaks into other parts of the system.
    

### Better:

Use `unknown` if the type is unclear, then **narrow it**.

```ts
let userData: unknown = getUserData();

if (typeof userData === "object" && userData !== null) {
  // now safe to type-assert
}
```

---

## 🚫 4. **Classes (for everything)** — Prefer functions or composition

### Problem:

```ts
class User {
  constructor(public name: string) {}
}
```

- Adds unneeded complexity for plain data holders.
    
- Encourages OOP where functional composition might be cleaner.
    
- Makes testing and typing harder in some scenarios.
    

### Better:

Use type aliases and factory functions:

```ts
type User = {
  name: string;
};

const createUser = (name: string): User => ({ name });
```

> Use classes only when you **need encapsulation**, **state**, or **polymorphism**.

---

## 🚫 5. **Namespaces / `namespace` keyword** — Avoid in modules

### Problem:

```ts
namespace Utils {
  export function add(x: number, y: number) {
    return x + y;
  }
}
```

- Old TypeScript pattern (before ES modules).
    
- Not compatible with modern ES module systems (ESM, bundlers).
    
- Creates global pollution.
    

### Better:

Use ES modules:

```ts
// utils/add.ts
export const add = (x: number, y: number) => x + y;
```

---

## 🚫 6. **Extending built-in objects (like Array, Object, etc.)**

### Problem:

```ts
class MyArray extends Array {
  customMethod() {}
}
```

- Often results in subtle bugs.
    
- Inconsistent behavior across environments.
    
- Hard to type correctly and maintain.
    

### Better:

Use composition:

```ts
type MyArray<T> = {
  data: T[];
  customMethod(): void;
};
```

---

## 🚫 7. **Too much type inference** — Be explicit with public APIs

### Problem:

```ts
export function parseUserData(data) {
  return data.id;
}
```

- No return type on a **public function**.
    
- Makes refactoring risky.
    
- Hard to understand from just the function signature.
    

### Better:

```ts
export function parseUserData(data: unknown): string {
  // type-checking is now clear
}
```

---

## 🚫 8. **Index Signatures Everywhere**

### Problem:

```ts
type AnyObject = {
  [key: string]: any;
};
```

- Breaks type safety entirely.
    
- Silences useful errors.
    

### Better:

Use union discriminators, `Record`, or mapped types:

```ts
type SafeObject = Record<"name" | "email", string>;
```

---

## 🚫 9. **Function Overloads for Everything**

### Problem:

```ts
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: any, b: any): any {
  return a + b;
}
```

- Verbose, hard to maintain.
    
- Not needed in many cases.
    

### Better:

Use union types or generic constraints:

```ts
function add<T extends string | number>(a: T, b: T): T {
  return (a as any) + (b as any);
}
```

---

## 🚫 10. **Deep optional objects (`Partial<T>` abuse)**

### Problem:

```ts
type Config = Partial<{
  server: {
    port: number;
    host: string;
  };
}>;
```

- Doesn't make nested properties optional deeply.
    
- Leads to confusing types and errors.
    

### Better:

Use custom deep utility types like `DeepPartial<T>`, or Zod for config schemas.

---

## ✅ Bonus: Things To Use Instead

|Use This Instead Of|Why?|
|---|---|
|`as const` + union|Instead of `enum`|
|`unknown`|Instead of `any`|
|`#private`|Instead of `private`|
|ES Modules|Instead of `namespace`|
|Factory functions|Instead of classes for plain objects|
|Zod / io-ts / Valibot|For runtime-safe schemas|
|Template literal types|For expressive keys like `Error_${Code}`|
|`satisfies` operator|For exact type checking without inference|

---

## 🧠 Summary

### ❌ Avoid:

- `enum`
    
- `any`
    
- `private` (in favor of `#private`)
    
- `namespace`
    
- classes for data-only objects
    
- excessive use of `Partial`
    
- implicit types in public APIs
    
- global index signatures
    
- subclassing built-ins
    

### ✅ Prefer:

- `as const`, union types
    
- `unknown` with narrowing
    
- composition over inheritance
    
- module-based organization
    
- factory functions
    
- type-safe schemas
    


---

# ❌ TypeScript Anti-Patterns (And What to Do Instead)

> Learn what _not to do_ in TypeScript — and how to replace these patterns with safer, cleaner alternatives.

---

## 🔴 1. Using `any` Everywhere

### ❌ Anti-Pattern:

```ts
function getData(): any {
  return fetch("/api").then(res => res.json());
}
```

- Removes all type safety.
    
- Leaks unsafe assumptions.
    
- Errors only show at runtime.
    

### ✅ Preferred:

```ts
function getData(): Promise<unknown> {
  return fetch("/api").then(res => res.json());
}
```

Use `unknown` + type guards for safer, intentional handling.

---

## 🔴 2. Overusing `as` Type Assertions

### ❌ Anti-Pattern:

```ts
const user = getUser() as User; // blindly asserting
```

- Skips validation.
    
- Silences compiler without guarantees.
    

### ✅ Preferred:

```ts
if (isUser(user)) {
  // safely narrowed
}
```

Use **user-defined type guards** or validation libraries like [Zod](https://zod.dev/).

---

## 🔴 3. Using `enum` Instead of `as const`

### ❌ Anti-Pattern:

```ts
enum Status {
  Idle,
  Loading,
  Success,
  Error,
}
```

- Adds JS output.
    
- Reverse mapping is rarely needed.
    
- Not tree-shakable.
    

### ✅ Preferred:

```ts
const Status = {
  Idle: "Idle",
  Loading: "Loading",
  Success: "Success",
  Error: "Error",
} as const;

type Status = typeof Status[keyof typeof Status];
```

---

## 🔴 4. Using `namespace` in Module-Based Code

### ❌ Anti-Pattern:

```ts
namespace Utils {
  export function add(a: number, b: number) {
    return a + b;
  }
}
```

- Outdated pre-ES module pattern.
    
- Causes global pollution.
    

### ✅ Preferred:

```ts
// utils/math.ts
export const add = (a: number, b: number) => a + b;
```

---

## 🔴 5. Extending Built-In Objects (e.g. `Array`)

### ❌ Anti-Pattern:

```ts
class MyArray extends Array<number> {
  sum() {
    return this.reduce((a, b) => a + b, 0);
  }
}
```

- Breaks prototype chains.
    
- Can behave differently in environments (e.g., browsers vs Node.js).
    

### ✅ Preferred:

```ts
const sum = (arr: number[]) => arr.reduce((a, b) => a + b, 0);
```

Use composition over inheritance.

---

## 🔴 6. Declaring Index Signatures Loosely

### ❌ Anti-Pattern:

```ts
type LooseMap = {
  [key: string]: any;
};
```

- Accepts everything.
    
- Disables type checking.
    

### ✅ Preferred:

Use `Record<string, Value>` or strict object types:

```ts
type Settings = Record<"theme" | "mode", string>;
```

---

## 🔴 7. `private` Instead of `#private`

### ❌ Anti-Pattern:

```ts
class Account {
  private password: string;
}
```

- Not truly private at runtime.
    
- Leaks via `this["password"]`.
    

### ✅ Preferred:

```ts
class Account {
  #password: string;
}
```

- Enforced privacy by JavaScript engine.
    
- Cannot be accessed or reflected.
    

---

## 🔴 8. Skipping Types for Public APIs

### ❌ Anti-Pattern:

```ts
export function login(data) {
  // what is `data`?
}
```

- No context for consumers.
    
- Prone to misuse and type drift.
    

### ✅ Preferred:

```ts
export function login(data: LoginRequest): Promise<LoginResponse> {
  ...
}
```

Always annotate exported/public types.

---

## 🔴 9. Deeply Nested Partial Objects

### ❌ Anti-Pattern:

```ts
type Config = Partial<{
  server: {
    port: number;
    ssl: boolean;
  };
}>;
```

- `Partial` is shallow — doesn't deeply affect nested objects.
    
- Misleads intent.
    

### ✅ Preferred:

```ts
type DeepPartial<T> = {
  [K in keyof T]?: DeepPartial<T[K]>;
};
```

Use custom `DeepPartial<T>` if needed — or schema validators.

---

## 🔴 10. Overloading Functions Too Much

### ❌ Anti-Pattern:

```ts
function format(value: string): string;
function format(value: number): string;
function format(value: any): string {
  return value.toString();
}
```

- Hard to maintain.
    
- Unnecessary in most cases.
    

### ✅ Preferred:

```ts
function format(value: string | number): string {
  return value.toString();
}
```

Use unions unless overload is **absolutely necessary**.

---

## ✅ BONUS: Modern Best Practices

|What to Use|Why|
|---|---|
|`satisfies` keyword|For narrowing without losing exactness|
|`unknown` instead of `any`|Forces type-safe access|
|`as const` for literals|Enforces narrow literal types|
|Zod / Valibot / io-ts|Runtime-safe schema validation|
|`readonly` for immutability|Prevents accidental mutation|
|Composition over inheritance|Simpler, more testable logic|
|Type-safe builder patterns|Avoids class hierarchies|
|`infer` and conditional types|For expressive advanced typings|

---

## 🧠 Summary

|🚫 Anti-Pattern|✅ Use Instead|
|---|---|
|`any`|`unknown` + type guards|
|`enum`|`as const` object + union type|
|`private`|`#private`|
|`namespace`|ES module system|
|`Loose index signatures`|`Record`, mapped types|
|`type assertions everywhere`|Narrowing, validation libraries|
|Overuse of function overloads|Union types|
|Extending built-ins|Composition|
|Implicit return types|Explicit type annotations|
|Shallow `Partial<T>`|`DeepPartial<T>` or schema types|

---
## 🔴 11. **Mutating Parameters / Function Arguments**

### ❌ Anti-Pattern:

```ts
function update(user: User) {
  user.name = user.name.toUpperCase(); // mutation
}
```

- Mutates the original object.
    
- Breaks immutability expectations.
    
- Can cause hard-to-debug side effects.
    

### ✅ Preferred:

```ts
function update(user: User): User {
  return { ...user, name: user.name.toUpperCase() };
}
```

- Pure function = safer & testable.
    

---

## 🔴 12. **Implicit `any` in object literals**

### ❌ Anti-Pattern:

```ts
const config = {
  apiKey: process.env.API_KEY,
};
```

- `apiKey` is inferred as `string | undefined`, but not explicitly declared.
    
- Can leak unexpected types to downstream usage.
    

### ✅ Preferred:

```ts
const config: { apiKey: string } = {
  apiKey: process.env.API_KEY!,
};
```

Or safer with runtime checks:

```ts
if (!process.env.API_KEY) throw new Error("Missing API key");
```

---

## 🔴 13. **Overly Generic Types Without Constraints**

### ❌ Anti-Pattern:

```ts
function identity<T>(value: T): T {
  return value;
}
```

- Technically valid, but not helpful for real-world use if misused generically.
    

### ✅ Preferred (with constraints):

```ts
function identity<T extends string | number>(value: T): T {
  return value;
}
```

Adds type safety and intent.

---

## 🔴 14. **Overuse of Global Types**

### ❌ Anti-Pattern:

```ts
declare global {
  interface Window {
    __MY_GLOBAL_VAR__: any;
  }
}
```

- Encourages hidden dependencies.
    
- Pollutes global scope.
    
- Breaks modularity.
    

### ✅ Preferred:

Use DI or explicitly pass dependencies to functions/modules.

---

## 🔴 15. **Using `Object` / `Function` Instead of Proper Types**

### ❌ Anti-Pattern:

```ts
function process(input: Object): void { }
function callback(fn: Function): void { }
```

- Too loose.
    
- `Object` allows almost anything, `Function` misses parameter typing.
    

### ✅ Preferred:

```ts
function process(input: Record<string, unknown>): void { }
function callback(fn: () => void): void { }
```

---

## 🔴 16. **Using `new Array()` / `Array<T>` Everywhere**

### ❌ Anti-Pattern:

```ts
const nums: Array<number> = new Array(5);
```

- `new Array(5)` creates an empty array with `length=5`, not 5 elements.
    
- `Array<T>` is fine, but less readable than `T[]`.
    

### ✅ Preferred:

```ts
const nums: number[] = [1, 2, 3];
```

---

## 🔴 17. **Ignoring Exhaustiveness in `switch`**

### ❌ Anti-Pattern:

```ts
switch (status) {
  case "idle":
  case "loading":
    break;
}
```

- Misses `"error"` or `"success"` cases.
    
- No compiler error.
    

### ✅ Preferred:

Use an `assertNever` function for exhaustive checking:

```ts
function assertNever(x: never): never {
  throw new Error("Unexpected case: " + x);
}

switch (status) {
  case "idle":
  case "loading":
    break;
  default:
    assertNever(status); // error if status isn't narrowed
}
```

---

## 🔴 18. **Extending External Types Directly**

### ❌ Anti-Pattern:

```ts
interface User extends Express.User {
  role: string;
}
```

- Tightly couples to external library interfaces.
    
- You lose control if the upstream changes.
    

### ✅ Preferred:

```ts
type AppUser = Express.User & { role: string };
```

Use **intersection types** for better control and modularity.

---

## 🔴 19. **Using `typeof` on Values Without Narrowing**

### ❌ Anti-Pattern:

```ts
const val: unknown = getSomething();

if (typeof val === "object") {
  val.name; // ❌ still unsafe
}
```

- `typeof` doesn't narrow enough on `object`.
    

### ✅ Preferred:

Use full type guards:

```ts
function isUser(x: unknown): x is { name: string } {
  return typeof x === "object" && x !== null && "name" in x;
}
```

---

## 🔴 20. **Skipping Linting or Configuration Consistency**

While not a code-level anti-pattern, many TypeScript teams:

- Skip `strict` mode
    
- Don’t use `noUncheckedIndexedAccess`
    
- Lack `tsconfig.json` consistency across packages
    

### ✅ Preferred:

Turn these on:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true
  }
}
```

---

## ✅ Summary Table of Subtler Anti-Patterns

|🚫 Anti-Pattern|✅ Better Practice|
|---|---|
|Mutating arguments|Return new object|
|Implicit `any` in object literals|Explicit typing or validation|
|Overly generic functions|Add type constraints|
|Global type declarations|Avoid; use modular code|
|Using `Object`, `Function` types|Use `Record<string, unknown>`, `() => void`, etc.|
|`new Array()` with size|Use literal arrays or `Array.fill`|
|Unchecked `switch` blocks|Add exhaustive checks|
|Extending 3rd party types|Prefer intersections|
|Incomplete type narrowing|Use custom type guards|
|Loose tsconfig|Use strict flags in `tsconfig.json`|

---
