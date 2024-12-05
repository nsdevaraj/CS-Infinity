

### **40. Write a TypeScript utility type to extract the return type of a function.**

#### **Answer:**

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
// Usage:
const example = () => 42;
type ExampleReturnType = ReturnType<typeof example>; // number
```




### **36. How do you implement a custom error class in TypeScript?**

#### **Answer:**

```typescript
class CustomError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "CustomError";
  }
}
```




### **33. Write a TypeScript function that accepts a tuple and swaps its elements.**

#### **Answer:**

```typescript
function swap<T, U>(tuple: [T, U]): [U, T] {
  return [tuple[1], tuple[0]];
}
// Usage:
const result = swap([1, 'a']); // ['a', 1]
```




### **13. How can you enforce immutability in TypeScript?**

#### **Answer:**

```typescript
type Immutable<T> = {
  readonly [K in keyof T]: Immutable<T[K]>;
};

const user: Immutable<{ name: string }> = { name: "John" };
// user.name = "Doe"; // Error: Cannot assign to 'name' because it is a read-only property.
```


