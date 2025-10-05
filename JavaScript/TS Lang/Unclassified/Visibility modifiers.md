
 developer-friendly cheatsheet** for **visibility modifiers in TypeScript**, including both TypeScript and JavaScript-native options (`private`, `protected`, `public`, `readonly`, and `#private`).

---

# 🧾 TypeScript Visibility Modifiers Cheatsheet

|Modifier|Scope / Access Level|Applies To|Runtime Private?|Inheritance?|Notes|
|---|---|---|---|---|---|
|`public`|✅ Accessible everywhere|Classes|❌|✅|Default if no modifier is given|
|`private`|❌ Only accessible within the class|Classes|❌|❌|Compile-time only (not enforced at runtime)|
|`protected`|❌ Only within class and subclasses|Classes|❌|✅|Useful in class hierarchies|
|`readonly`|✅ Accessible everywhere but can't be reassigned after init|Classes, Interfaces|❌|✅|Often combined with other modifiers|
|`#private`|❌ Only accessible within the class (hard enforced by JS engine)|Classes (fields only)|✅ ✅ ✅|❌|ECMAScript-native private field (cannot be accessed or reflected at all)|

---

## 🧠 Quick Examples

### 1. `public` (default)

```ts
class Car {
  public brand: string;
  constructor(brand: string) {
    this.brand = brand;
  }
}
```

✅ Accessible everywhere, even outside the class.

---

### 2. `private`

```ts
class Car {
  private engineNumber: string;
  constructor(engineNumber: string) {
    this.engineNumber = engineNumber;
  }
}
```

❌ Cannot be accessed outside the class in TypeScript, but not private in emitted JS.

---

### 3. `protected`

```ts
class Vehicle {
  protected move() {
    console.log("Moving...");
  }
}

class Car extends Vehicle {
  drive() {
    this.move(); // ✅ OK
  }
}
```

✅ Subclasses can access it. ❌ Outside code cannot.

---

### 4. `readonly`

```ts
class Book {
  readonly title: string;
  constructor(title: string) {
    this.title = title;
  }

  updateTitle(newTitle: string) {
    this.title = newTitle; // ❌ Error: title is readonly
  }
}
```

✅ Value can only be set once — either at declaration or in constructor.

---

### 5. `#private` (Hard Private)

```ts
class Safe {
  #combination: string = "1234";

  unlock(pass: string) {
    return pass === this.#combination;
  }
}
```

✅ Cannot be accessed, even with:

```ts
safe["#combination"] // ❌ Error
(safe as any).#combination // ❌ Syntax error
```

---

## 🔁 Combinations

You can **combine** modifiers:

```ts
class User {
  public readonly id: string;
  private readonly passwordHash: string;
  protected readonly createdAt: Date;
  #token: string; // ECMAScript private field

  constructor(id: string, hash: string) {
    this.id = id;
    this.passwordHash = hash;
    this.createdAt = new Date();
    this.#token = "abc123";
  }
}
```

---

## 🧮 Modifier Comparison Table

|Feature|`public`|`private`|`protected`|`readonly`|`#private`|
|---|---|---|---|---|---|
|Accessible outside class|✅|❌|❌|✅|❌|
|Accessible inside class|✅|✅|✅|✅|✅|
|Accessible in subclass|✅|❌|✅|✅|❌|
|Compile-time enforcement|✅|✅|✅|✅|✅|
|Runtime enforcement|❌|❌|❌|❌|✅ ✅ ✅|
|Usable with interfaces|✅|❌|✅|✅|❌|
|Reflection safe|❌|❌|❌|❌|✅|

---

## ✨ Bonus: Custom Branding

Want to pseudo-hide values without runtime enforcement? Use branded types:

```ts
type Password = string & { __brand: "Password" };
const password = "secret" as Password;
```

---

## 💬 Summary

|When to Use...|Use Modifier|
|---|---|
|Anyone can use the property|`public` (default)|
|Only this class should use it|`private`|
|Subclasses can also access it|`protected`|
|Should not be reassigned|`readonly`|
|Should be truly hidden at runtime|`#private`|

---
