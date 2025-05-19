
## 3. Private Class Fields with `#`

Traditionally, TypeScript provided `private` properties, but JavaScript now supports true private fields using `#`.

### Example:

```javascript
class User {
    #secret = "Hidden Message";

    getSecret() {
        return this.#secret;
    }
}

const user = new User();
console.log(user.getSecret()); // Output: Hidden Message
console.log(user.#secret); // SyntaxError: Private field '#secret' must be declared in an enclosing class
```

Using `#`, private properties cannot be accessed outside the class, providing true encapsulation.


### **Private Fields in JavaScript Classes**

JavaScript introduced **truly private fields** in ES2020 using the `#` (hash) prefix. These fields are only accessible within the class that defines them.

#### **1. Declaring Private Fields**

```js
class Person {
  #age; // Private field

  constructor(name, age) {
    this.name = name;
    this.#age = age; // Accessible only inside the class
  }

  getAge() {
    return this.#age; // Can access inside class methods
  }
}

const john = new Person("John", 30);
console.log(john.getAge()); // ✅ 30
console.log(john.#age); // ❌ SyntaxError: Private field '#age' must be declared in an enclosing class
```

Here, `#age` is truly private and cannot be accessed outside the class.

---

#### **2. Private Methods and Getters/Setters**

You can also define private methods to encapsulate internal logic.

```js
class BankAccount {
  #balance = 0; // Private field

  deposit(amount) {
    this.#validateAmount(amount);
    this.#balance += amount;
  }

  getBalance() {
    return this.#balance;
  }

  #validateAmount(amount) { // Private method
    if (amount <= 0) throw new Error("Invalid amount");
  }
}

const account = new BankAccount();
account.deposit(100);
console.log(account.getBalance()); // ✅ 100
console.log(account.#balance); // ❌ SyntaxError
console.log(account.#validateAmount(50)); // ❌ SyntaxError
```

Private methods like `#validateAmount()` ensure encapsulation, preventing direct modification from outside the class.

---

#### **3. Comparison: `#private` vs. `private` in TypeScript**

|Feature|`#private` (JS)|`private` (TS)|
|---|---|---|
|Enforced at runtime?|✅ Yes|❌ No (only compile-time)|
|Accessible outside the class?|❌ No|✅ Yes via type casting|
|Works in plain JavaScript?|✅ Yes (ES2020+)|❌ No (TypeScript only)|

Example of TypeScript `private` leaking in compiled JS:

```ts
class Example {
  private secret = "hidden";
}

const obj = new Example();
console.log(obj["secret"]); // Works in JS, breaks encapsulation!
```

Using `#private` ensures true privacy even after transpilation.

---

### **4. Private Static Fields**

Private fields can also be **static**, shared across all instances.

```js
class Counter {
  static #count = 0;

  static increment() {
    this.#count++;
    return this.#count;
  }
}

console.log(Counter.increment()); // ✅ 1
console.log(Counter.increment()); // ✅ 2
console.log(Counter.#count); // ❌ SyntaxError
```

Here, `#count` is a private static field accessible only within the class.

---

### **Key Takeaways 🚀**

1. **`#privateField` is truly private** (unlike `private` in TypeScript).
2. **Encapsulation is enforced at runtime**, preventing direct access.
3. **Supports private methods & static fields**, ensuring better class design.
4. **Cannot be accessed via `this["#field"]` or reflection techniques.**

🔹 **Use `#private` for real privacy and encapsulation in modern JavaScript!** 💡

```js
  

class C1 {
	private secret:string = "my secret";
}

class C2 {
	#secret:string = "my secret";
}

  

const c1 = new C1();

// console.log(c1.secret) //=: Property 'secret' is private and only accessible within class 'C1'.(2341)

console.log((c1 as any).secret); //=> "my secret"

  

const c2 = new C2();

// console.log(c2.#secret) //=:Property '#secret' is not accessible outside class 'C2' because it has a private identifier.(18013)

// console.log((c1 as any).#secret); //=: Private identifiers are not allowed outside class bodies.(18016)
```

---



