

### **Generics in TypeScript – Crisp Overview for Interviews**

Generics in TypeScript allow you to create reusable, flexible, and type-safe components or functions without losing the benefits of type checking. They provide a way to define functions, classes, and interfaces that can work with different data types while maintaining type safety.

---

### **1. Why Use Generics?**

- **Flexibility**: Generics allow you to write functions and classes that work with multiple data types without duplicating code.
- **Type Safety**: It provides type-checking at compile time, reducing the chances of runtime errors.
- **Code Reusability**: It helps in reusing logic for different types while maintaining strong typing.

---

### **2. Basic Generic Syntax**

```typescript
function identity<T>(arg: T): T {
  return arg;
}

const numberIdentity = identity(5);  // T is inferred as 'number'
const stringIdentity = identity("Hello");  // T is inferred as 'string'
```

Here, `<T>` is a placeholder for a type that will be specified when the function is called.

---

### **3. Generic with Multiple Types**

You can define multiple type parameters for more complex use cases.

```typescript
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}

const stringNumberPair = pair("Age", 25);  // T is 'string', U is 'number'
```

---

### **4. Using Generics with Interfaces**

Generics can also be applied to interfaces to make them flexible.

```typescript
interface Box<T> {
  value: T;
}

const stringBox: Box<string> = { value: "Hello" };
const numberBox: Box<number> = { value: 100 };
```

Here, the `Box` interface can be used with any data type, and the `value` property will be of that specific type.

---

### **5. Generic Constraints**

Sometimes you need to restrict the types that can be used with a generic. This can be done using constraints.

```typescript
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

console.log(getLength("Hello"));  // 5
console.log(getLength([1, 2, 3]));  // 3
```

In this example, the generic `T` is constrained to types that have a `length` property (e.g., strings, arrays).

---

### **6. Generic Classes**

You can use generics in classes to define properties and methods that work with different data types.

```typescript
class Container<T> {
  private value: T;

  constructor(value: T) {
    this.value = value;
  }

  getValue(): T {
    return this.value;
  }
}

const numberContainer = new Container(123);
console.log(numberContainer.getValue());  // 123

const stringContainer = new Container("Hello");
console.log(stringContainer.getValue());  // "Hello"
```

---

### **7. Generic Functions with Defaults**

You can also provide default types for generics in case they are not specified by the user.

```typescript
function wrap<T = string>(value: T): T {
  return value;
}

console.log(wrap("Hello"));  // "Hello"
console.log(wrap(42));  // 42
```

Here, the default type for `T` is `string`, so if no type is passed, `string` will be used.

---

### **8. Using Generics in Type Aliases**

You can create flexible type aliases using generics.

```typescript
type Pair<T, U> = { first: T, second: U };

const pair: Pair<string, number> = { first: "age", second: 30 };
```

---

### **Conclusion**

Generics in TypeScript allow you to create flexible, reusable, and type-safe code. By using generics, you can ensure that your functions, classes, and interfaces are adaptable to different types, without losing the benefits of strong typing. It’s an essential concept to understand for building scalable and maintainable TypeScript applications.

### **48. How can you define a generic interface in TypeScript?**

#### **Answer:**

```typescript
interface ApiResponse<T> {
  data: T;
  status: number;
}

const response: ApiResponse<string> = { data: "Hello", status: 200 };
```





### **37. How do you use Generics in TypeScript?**

#### **Answer:**

```typescript
function identity<T>(arg: T): T {
  return arg;
}
// Usage:
const output = identity<string>("Hello"); // "Hello"
```




to check {

https://www.youtube.com/watch?v=EcCTIExsqmI&list=PLZlA0Gpn_vH_z2fqIg50_POJrUkJgBu7g&index=21


}