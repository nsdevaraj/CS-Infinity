

pure : returns same output for same input, no side effects ( no external state modification )



### Pure vs Impure Functions in JavaScript

|**Aspect**|**Pure Function**|**Impure Function**|
|---|---|---|
|**Definition**|Always produces the same output for the same input, without side effects.|May produce different outputs for the same input or cause side effects.|
|**Deterministic**|Yes — output is predictable.|No — output may vary.|
|**Side Effects**|None — does not modify external state.|Has side effects — modifies external state or depends on it.|
|**Dependencies**|Relies only on input arguments.|Relies on external variables or state.|
|**Example**|`javascript<br>function add(a, b) { return a + b; }<br>`|`javascript<br>let count = 0;<br>function increment() { count++; }<br>`|
|**Use Case**|Preferred in functional programming and for predictable behavior (e.g., testing).|Often used for I/O operations, logging, or updating external state.|

---

### Examples

#### **Pure Function**

```javascript
function square(num) {
  return num * num; // No side effects, deterministic
}

console.log(square(4)); // 16
console.log(square(4)); // 16 (always the same output)
```

#### **Impure Function**

```javascript
let count = 0;
function incrementCount() {
  count++; // Modifies external state
  return count;
}

console.log(incrementCount()); // 1
console.log(incrementCount()); // 2 (output changes due to external state)
```

---

### Key Takeaways

- **Pure functions** are ideal for predictable, testable code.
- **Impure functions** are necessary for side effects like modifying state, interacting with databases, or logging.

