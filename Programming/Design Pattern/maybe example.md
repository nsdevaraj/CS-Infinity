
Here’s a crisp LinkedIn post comparing JavaScript’s optional chaining with the Maybe pattern, highlighting where Maybe excels, along with clear code examples.

## Optional Chaining vs. Maybe Pattern in JavaScript

**Optional chaining** (`?.`) is great for safely accessing deeply nested properties, returning `undefined` if any reference is missing. However, it stops at returning `undefined`-you can’t easily chain transformations or provide rich error handling. The **Maybe pattern** (from functional programming) wraps values, letting you chain operations and handle missing data more robustly.

## Example Scenario

Suppose you want to get a user’s city, transform it to uppercase, and provide a fallback if it’s missing.

**Using Optional Chaining**

```js
const user = {
  name: "Alice",
  address: {
    city: "Bangalore"
  }
};

const city = user?.address?.city?.toUpperCase() ?? "Unknown City";
console.log(city); // "BANGALORE"

```

If any property is missing, you get `"Unknown City"`[2](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)[3](https://daily.dev/blog/optional-chaining-in-javascript-what-is-it-and-how-to-use-it).

**Using the Maybe Pattern**

```js
function Maybe(value) {
  return {
    map: fn => value == null ? Maybe(null) : Maybe(fn(value)),
    getOrElse: fallback => value == null ? fallback : value
  };
}

const user = {
  name: "Alice",
  address: {
    city: "Bangalore"
  }
};

const city = Maybe(user)
  .map(u => u.address)
  .map(a => a.city)
  .map(c => c.toUpperCase())
  .getOrElse("Unknown City");

console.log(city); // "BANGALORE"
```

With Maybe, you can **chain as many transformations as you want**, and provide a fallback only at the end
## Why Maybe Excels

- **Chaining:** Transform values step-by-step without breaking the chain.
    
- **Composability:** Easily compose complex data flows.
    
- **Explicit Handling:** Clearly state what happens when data is missing.
    

> “The Maybe type encapsulates the concept of Some (contains a value) and None (no value present). With these two abstractions, we can safely handle cases where no value is present, avoiding NullPointerException errors and excessive null checks.”


Optional chaining is concise for property access. The Maybe pattern shines when you need to chain multiple operations and handle missing data in a functional, composable way.



  

Here’s an example where the **Maybe pattern** clearly outperforms optional chaining by enabling **multi-step transformations with fallbacks** and **explicit error handling**:

  

---

  

### Scenario

  

Process a user’s order history to calculate a discount, where:

  

1. Fetch the user’s last order.

2. Validate it’s from the last 30 days.

3. Extract the cart total.

4. Apply a 10% discount if eligible.

5. Return the discounted price or a fallback message.

  

---

  

**Using Optional Chaining**

  
```js
const user = {
  orders: [
    { date: '2025-05-01', cart: { total: 100 } },
    { date: '2025-04-10', cart: { total: 50 } }
  ]
};

// Complex nested checks and temporary variables
const lastOrder = user?.orders?.[0];
const isRecent = lastOrder?.date && 
  (new Date() - new Date(lastOrder.date)) < 30 * 86400000;
const discount = isRecent ? lastOrder?.cart?.total * 0.1 : null;
const result = discount != null ? 
  `Discounted price: $${100 - discount}` : 
  "No discount available";

console.log(result); // "Discounted price: $90"

```
  

- Requires manual date validation and null checks.

- Code becomes nested and harder to maintain.

  

---

  

**Using the Maybe Pattern**

  



```js
function Maybe(value) {
  return {
    map: fn => value == null ? Maybe(null) : Maybe(fn(value)),
    chain: fn => value == null ? Maybe(null) : fn(value),
    getOrElse: fallback => value ?? fallback
  };
}

const result = Maybe(user)
  .map(u => u.orders?.[0]) // Get last order
  .chain(order => 
    Maybe(order.date).map(date => 
      (new Date() - new Date(date)) < 30 * 86400000 ? order : null
    )
  ) // Validate date
  .map(order => order.cart.total * 0.1) // Calculate discount
  .map(discount => `Discounted price: $${100 - discount}`)
  .getOrElse("No discount available");

console.log(result); // "Discounted price: $90"

```
  

- **Chaining**: Seamlessly links validation, transformation, and fallback logic.

- **Reusability**: Each step is modular and testable.

- **Explicit flow**: No hidden `null`/`undefined` checks; failures propagate silently.

  

---

  

### Why Maybe Wins Here

  

1. **Complex Validation**: The `chain` method lets you exit early if validation fails (e.g., invalid date), which optional chaining can’t do without nested conditionals[^2][^3].

2. **Business Logic**: Encapsulates multi-step workflows (e.g., discount rules) without temporary variables

3. **Functional Composition**: Easily reuse or swap steps (e.g., change date validation rules)

  

Optional chaining (`?.`) is ideal for simple property access, but **Maybe** excels when managing multi-step operations with conditional logic



---

```js
const user = {}; // No age property

const nextAge = user?.age + 1 || "Unknown age";
console.log(nextAge); // "1"  (Oops! Not what we want)

```



```js
function Maybe(value) {
  return {
    map: fn => value == null ? Maybe(null) : Maybe(fn(value)),
    getOrElse: fallback => value == null ? fallback : value
  };
}

const user = {}; // No age property

const nextAge = Maybe(user.age)
  .map(age => age + 1)
  .getOrElse("Unknown age");

console.log(nextAge); // "Unknown age"


```





**optional chaining** is already very good for safely accessing nested properties, and in most simple cases, it’s concise and clear. The **Maybe pattern** really shines when you want to do more than just access properties-**especially when you need to chain multiple operations where a failure in any step should stop the rest**.

Let’s look at a **very simple, practical case** where Maybe is clearly better:

## Scenario: Chaining Multiple Operations with Early Exit

Suppose you have a user object, and you want to:

1. Get the user's email.
2. Extract the domain from the email.
3. Convert the domain to uppercase.
4. If any step fails (missing user, email, or invalid format), return `"NO DOMAIN"`.



```js
const user = { email: "alice@example.com" };

const domain = user?.email?.split('@')[1]?.toUpperCase() ?? "NO DOMAIN";
console.log(domain); // "EXAMPLE.COM"

```


**But:**  
If `user.email` is `""` (empty string), `split('@')` is `undefined`, so you get `"NO DOMAIN"`.  
If `user.email` is not a string, you get an error.  

If you want to add more checks (e.g., validate email), the code gets messy.


```js
function Maybe(value) {
  return {
    map: fn => value == null ? Maybe(null) : Maybe(fn(value)),
    getOrElse: fallback => value == null ? fallback : value
  };
}

const user = { email: "alice@example.com" };

const domain = Maybe(user)
  .map(u => u.email)
  .map(email => typeof email === "string" ? email.split('@')[1] : null)
  .map(domain => domain && domain.toUpperCase())
  .getOrElse("NO DOMAIN");

console.log(domain); // "EXAMPLE.COM"

```


## Why Maybe is Better Here

- **Safe chaining:** Each transformation only runs if the previous value exists and is valid.
- **Custom logic:** You can add type checks, regex validation, or any logic in the chain.
- **No runtime errors:** If any step fails, you get the fallback-no exceptions, no messy checks.


**Summary:**  
Optional chaining is great for property access, but **Maybe** is better when you need to chain multiple operations and stop early if anything fails, all while keeping your code readable and robust.



Here’s a clear and concise **comparison between nullish checks, optional chaining, and the Maybe pattern**, showing their differences in usage, readability, safety, and power.

---

### ✅ **1. Nullish Checks**

**Style:** Manual `if` or ternary checks  
**Example:**

```js
const domain = user && user.email
  ? user.email.split('@')[1].toUpperCase()
  : 'NO DOMAIN';
```

**Pros:**

- Familiar to all JS devs
    
- No special syntax or patterns
    

**Cons:**

- Verbose and repetitive
    
- Easy to miss a case
    
- Hard to read with deep chains
    

---

### ✅ **2. Optional Chaining**

**Style:** Native JavaScript `?.` operator  
**Example:**

```js
const domain = typeof user?.email === 'string'
  ? user.email.split('@')[1]?.toUpperCase()
  : 'NO DOMAIN';
```

**Pros:**

- Clean and readable
    
- Built into modern JavaScript
    
- Reduces boilerplate
    

**Cons:**

- Doesn’t prevent runtime errors on non-method-safe values (e.g. `.split()` on non-string)
    
- No transformation control — just safe access
    

---

### ✅ **3. Maybe Pattern (Functional)**

**Style:** Functional chaining with safety  
**Example:**

```js
const domain = Maybe(user)
  .map(u => u.email)
  .map(email => (typeof email === 'string' ? email.split('@')[1] : null))
  .map(domain => domain?.toUpperCase())
  .getOrElse('NO DOMAIN');
```

**Pros:**

- Handles both access and transformation safely
    
- Eliminates nested conditionals
    
- Composable and predictable
    

**Cons:**

- Requires custom implementation or library
    
- May feel unfamiliar to JS devs new to FP
    

---

### 🧠 Summary Table:

|Feature|Nullish Checks|Optional Chaining|Maybe Pattern|
|---|---|---|---|
|Built-in|✅|✅|❌ (custom/library)|
|Readability|⚠️ (can get messy)|✅|✅|
|Handles transformations|❌|⚠️ (partially)|✅|
|Composability|❌|❌|✅|
|FP-style chaining|❌|❌|✅|
|Runtime safety|⚠️|⚠️|✅|

---

### 🙋‍♂️ When to use what?

- Use **nullish checks** for simple, one-off conditions.
    
- Use **optional chaining** for safe access to deep properties.
    
- Use the **Maybe pattern** when you want **safe chaining + clean transformations**—especially in more complex flows.
    

---

Would you like this as a visual slide or carousel for a LinkedIn post?


