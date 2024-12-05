

### **Famous TypeScript Utility Types**

TypeScript provides several built-in utility types that help in manipulating types more efficiently and flexibly. These utility types are widely used in real-world applications to enhance type safety and reduce boilerplate.

Here’s a list of the most commonly used utility types:

---

### **1. `Partial<T>`**

Makes all properties of `T` optional.

#### Example:

```typescript
interface User {
  name: string;
  age: number;
}

const user: Partial<User> = { name: "John" }; // age is optional now
```

### **2. `Required<T>`**

Makes all properties of `T` required.

#### Example:

```typescript
interface User {
  name?: string;
  age?: number;
}

const user: Required<User> = { name: "John", age: 25 }; // Both name and age are required
```

### **3. `Readonly<T>`**

Makes all properties of `T` read-only, preventing reassignment.

#### Example:

```typescript
interface User {
  name: string;
  age: number;
}

const user: Readonly<User> = { name: "John", age: 25 };
// user.age = 26; // Error: Cannot assign to 'age' because it is a read-only property
```

### **4. `Record<K, T>`**

Constructs an object type with keys `K` and values of type `T`.

#### Example:

```typescript
type Role = "admin" | "user";
const userRoles: Record<Role, string> = {
  admin: "Administrator",
  user: "Standard User",
};
```

### **5. `Pick<T, K>`**

Constructs a type by picking a subset of properties `K` from `T`.

#### Example:

```typescript
interface User {
  name: string;
  age: number;
  email: string;
}

type UserNameAndAge = Pick<User, "name" | "age">;

const user: UserNameAndAge = { name: "John", age: 25 };
```

### **6. `Omit<T, K>`**

Constructs a type by excluding properties `K` from `T`.

#### Example:

```typescript
interface User {
  name: string;
  age: number;
  email: string;
}

type UserWithoutEmail = Omit<User, "email">;

const user: UserWithoutEmail = { name: "John", age: 25 };
```

### **7. `Exclude<T, U>`**

Constructs a type by excluding types from `T` that are assignable to `U`.

#### Example:

```typescript
type A = "a" | "b" | "c";
type B = Exclude<A, "a" | "b">; // B is "c"
```

### **8. `Extract<T, U>`**

Constructs a type by extracting types from `T` that are assignable to `U`.

#### Example:

```typescript
type A = "a" | "b" | "c";
type B = Extract<A, "a" | "c">; // B is "a" | "c"
```

### **9. `NonNullable<T>`**

Constructs a type by excluding `null` and `undefined` from `T`.

#### Example:

```typescript
type A = string | null | undefined;
type B = NonNullable<A>;  // B is string
```

### **10. `Parameters<T>`**

Extracts the parameter types of a function type as a tuple.

#### Example:

```typescript
type Func = (a: string, b: number) => void;
type Params = Parameters<Func>; // [string, number]
```

### **11. `ReturnType<T>`**

Extracts the return type of a function type.

#### Example:

```typescript
type Func = (a: string) => number;
type Return = ReturnType<Func>; // number
```

### **12. `InstanceType<T>`**

Extracts the instance type of a constructor function type.

#### Example:

```typescript
class User {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
}

type UserInstance = InstanceType<typeof User>; // User
```

### **13. `ThisType<T>`**

Provides the type of `this` for an object or function.

#### Example:

```typescript
interface User {
  name: string;
}

const obj = {
  name: "John",
  greet(this: ThisType<User>) {
    console.log(this.name);
  },
};

obj.greet(); // Output: "John"
```

---

### **Conclusion**

TypeScript's utility types are powerful tools for manipulating types in various scenarios. By using them effectively, you can improve the readability and maintainability of your codebase while ensuring type safety. These types are widely used in TypeScript-based applications, particularly in larger codebases where flexibility and strict type-checking are essential.


### **51. How do you create a utility type to make all properties optional in TypeScript?**

#### **Answer:**

```typescript
type Partial<T> = {
  [K in keyof T]?: T[K];
};

type User = { id: number; name: string };
type OptionalUser = Partial<User>;
```


