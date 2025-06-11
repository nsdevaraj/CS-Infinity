
# 🦆 Understanding Duck Typing in TypeScript — In Depth

**“If it walks like a duck and quacks like a duck, it’s probably a duck.”**

This classic saying defines **duck typing**, and TypeScript uses this exact principle in its **type system** — which is **structural**, not nominal. In this article, we'll explore what that really means, how TypeScript handles it under the hood, and where it can be both powerful and tricky.

---

## 📘 What is Duck Typing?

**Duck typing** is a concept where an object's **shape** (i.e., the structure of its properties and methods) determines its compatibility with a type — **not the name of the type**.

### 🧠 In TypeScript:

> If an object has all the required properties of a given type, it is **considered to be of that type**, even if it has extra properties or isn't explicitly declared as that type.

This behavior comes from **TypeScript’s structural type system**, which checks **what an object has**, rather than **what it claims to be**.

---

## 🧪 Basic Example

```ts
type Person = {
  name: string;
  age: number;
};

const john = {
  name: "John",
  age: 30,
  occupation: "Engineer"
};

const greet = (p: Person) => {
  console.log(`Hello, ${p.name}!`);
};

greet(john); // ✅ Works!
```

Even though `john` has an **extra property** (`occupation`), TypeScript allows it — because `john` satisfies the required structure of the `Person` type.

---

## 🔍 Behind the Scenes: Structural Typing

TypeScript checks types based on **structure compatibility**, not by **declaration**.

So:

```ts
type A = { x: number };
type B = { x: number };

const obj: A = { x: 5 };
const same: B = obj; // ✅ Works — same structure
```

Even though `A` and `B` are **different named types**, the object is assignable because their structures match exactly.

---

## 🚨 When TypeScript Becomes Strict: Excess Property Checks

TypeScript is **more strict** when using **inline object literals**. Here's an important nuance:

```ts
type User = {
  id: number;
  name: string;
};

function register(user: User) {}

register({
  id: 1,
  name: "Alice",
  email: "alice@example.com" // ❌ Error: Object literal may only specify known properties
});
```

### 🤔 Why?

When passing **inline objects**, TypeScript performs **excess property checks** to catch potential bugs (e.g., typos or incorrect data). But if you store the object in a variable first:

```ts
const u = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
};

register(u); // ✅ Works — extra properties are allowed
```

This is because TypeScript assumes you **know what you’re doing** with a named variable — but plays it safe with inline objects.

---

## ✅ Duck Typing With Functions

Duck typing isn't just for objects — it works with **function signatures** too.

```ts
type LogFn = (msg: string) => void;

const logger = (message: string, timestamp?: number) => {
  console.log(`[LOG]: ${message}`);
};

const useLogger = (fn: LogFn) => fn("Hello");

useLogger(logger); // ✅ Works — extra param doesn't break it
```

The function `logger` is still assignable to `LogFn` because it **matches the required parameters**. Extra optional ones are fine.

---

## ⚠️ Duck Typing Caveats

While duck typing gives flexibility, it can also lead to **silent bugs**:

```ts
type Point2D = { x: number; y: number };

const point3D = { x: 10, y: 20, z: 30 };

function logPoint(p: Point2D) {
  console.log(p.x, p.y);
}

logPoint(point3D); // ✅ Allowed — but z is silently ignored
```

**Problem?** TypeScript doesn’t warn you that `z` is never used — this could hide bugs in larger codebases.

```typescript
type Person = {
	name: string;
	age: number;
};

  

const takePerson = ():Person => {
	const john = {
		name: "John",
		age: 30,
		extra:'extra', // extra key
	};
	
	return john
}
```

---

## 🧱 Best Practices with Duck Typing

- ✅ **Use interfaces/types to define expected shapes clearly.**
    
- ✅ **Prefer explicit type declarations for external data (e.g., API responses).**
    
- ❌ **Don’t rely too heavily on duck typing for deeply nested or complex objects.**
    
- ⚠️ **Be cautious with inline objects — excess property checks can save you.**
    

---

## 🛠️ Real-World Use Case: API Responses

```ts
type User = {
  id: number;
  name: string;
};

const getUserFromAPI = (): unknown => {
  return {
    id: 1,
    name: "Alice",
    email: "alice@example.com"
  };
};

const raw = getUserFromAPI();

// Unsafe but passes because of duck typing:
const user: User = raw as User; // ✅ OK — but risks ignoring 'email' or missing fields

console.log(user.name);
```

✅ Instead, use **runtime validation** libraries like `zod`, `io-ts`, or manual checks to validate shape at runtime, because **TypeScript checks nothing at runtime**.

---

## 🧩 Final Thought

TypeScript’s duck typing system is one of its most powerful features — it allows for clean, flexible, and interoperable code. But with great power comes the risk of **assuming correctness where it may not exist**.

### TL;DR:

- ✅ TypeScript uses **duck typing** via a **structural type system**.
    
- ✅ Extra properties are OK — **if assigned to a variable** before being passed.
    
- ❌ Inline object literals get **extra checks** — this is by design.
    
- ⚠️ Duck typing is powerful but not a substitute for **runtime validation**.
    

---

In **TypeScript's duck typing** (aka structural typing), it checks:

> ⚙️ **"Does the value (object) have all the properties and types required by the desired type?"**

If **yes**, it's considered valid — even if the object has **extra keys**.

