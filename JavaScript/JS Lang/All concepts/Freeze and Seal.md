

### **Comparison of `Object.freeze()` and `Object.seal()`**

|Feature|`Object.freeze()`|`Object.seal()`|
|---|---|---|
|**Add New Properties**|❌ Not Allowed|❌ Not Allowed|
|**Delete Properties**|❌ Not Allowed|❌ Not Allowed|
|**Modify Existing Values**|❌ Not Allowed|✅ Allowed|
|**Change Property Attributes**|❌ Not Allowed|❌ Not Allowed|
|**Check Method**|`Object.isFrozen(obj)`|`Object.isSealed(obj)`|
|**Use Case**|Enforce immutability for all properties|Prevent structural changes but allow value edits|

---

### **Code Examples**

#### **1. Using `Object.freeze()`**

```javascript
const obj = { key: "value" };
Object.freeze(obj);

obj.key = "new value"; // ❌ Cannot modify
obj.newKey = "new";    // ❌ Cannot add
delete obj.key;        // ❌ Cannot delete

console.log(obj); // { key: "value" }
```

#### **2. Using `Object.seal()`**

```javascript
const obj = { key: "value" };
Object.seal(obj);

obj.key = "new value"; // ✅ Allowed
obj.newKey = "new";    // ❌ Cannot add
delete obj.key;        // ❌ Cannot delete

console.log(obj); // { key: "new value" }
```

---

### **Key Interview Points**

- `Object.freeze()` is stricter: Prevents **all modifications** (values, properties, descriptors).
- `Object.seal()` allows **modifying existing values** but disallows structural changes.
- Nested objects remain mutable unless deeply frozen.
- Commonly used to secure objects like configuration or application state.

Knowing these differences is essential for demonstrating a strong understanding of JavaScript object immutability concepts.



### **Detailed Comparison and Insights**

#### **`Object.isFrozen()` vs `Object.isSealed()`**

|Feature|`Object.isFrozen(obj)`|`Object.isSealed(obj)`|
|---|---|---|
|**Checks for Freezing**|Returns `true` if the object is fully frozen (no properties can be added, deleted, or modified).|Returns `true` if the object is sealed (no properties can be added or deleted, but existing values can be modified).|
|**Nested Objects**|Only checks the first level of the object. Nested objects remain mutable unless frozen separately.|Same as `isFrozen`. Does not check nested objects.|

#### **Code Examples**

```javascript
const obj = { a: 1, nested: { b: 2 } };

Object.freeze(obj);
console.log(Object.isFrozen(obj)); // true
console.log(Object.isFrozen(obj.nested)); // false (nested not frozen)

Object.seal(obj);
console.log(Object.isSealed(obj)); // true
console.log(Object.isSealed(obj.nested)); // false (nested not sealed)
```

---

#### **Strict Mode with Frozen/Sealed Objects**

- In **Strict Mode**, attempts to modify frozen/sealed objects will throw a `TypeError` instead of silently failing.
- Example:

```javascript
'use strict';

const obj = Object.freeze({ key: "value" });

try {
  obj.key = "new value"; // ❌ TypeError in Strict Mode
} catch (err) {
  console.error(err.message); // Cannot assign to read-only property
}
```

Without strict mode, the assignment silently fails.

---

#### **Nested Freezing and Sealing**

- Neither `Object.freeze()` nor `Object.seal()` affects nested objects by default. To handle nested properties, **deep freezing** or **deep sealing** is required.

#### **Deep Freezing Example**

```javascript
function deepFreeze(obj) {
  Object.freeze(obj);
  Object.keys(obj).forEach(key => {
    if (typeof obj[key] === "object" && obj[key] !== null) {
      deepFreeze(obj[key]);
    }
  });
}

const obj = { a: 1, nested: { b: 2 } };
deepFreeze(obj);

obj.nested.b = 3; // ❌ Cannot modify
console.log(obj.nested.b); // 2
```

#### **Deep Sealing Example**

```javascript
function deepSeal(obj) {
  Object.seal(obj);
  Object.keys(obj).forEach(key => {
    if (typeof obj[key] === "object" && obj[key] !== null) {
      deepSeal(obj[key]);
    }
  });
}

const obj = { a: 1, nested: { b: 2 } };
deepSeal(obj);

obj.nested.b = 3; // ✅ Can modify
obj.nested.c = 4; // ❌ Cannot add
console.log(obj.nested); // { b: 3 }
```

---

### **Key Differences Recap**

|Feature|`freeze`|`seal`|Strict Mode Impact|
|---|---|---|---|
|**Add New Properties**|❌ Not Allowed|❌ Not Allowed|Throws `TypeError` if violated|
|**Delete Properties**|❌ Not Allowed|❌ Not Allowed|Throws `TypeError` if violated|
|**Modify Existing Values**|❌ Not Allowed|✅ Allowed|Throws `TypeError` on assignment failure|
|**Nested Objects**|Remain mutable unless explicitly frozen|Remain mutable unless explicitly sealed|No direct impact, but strict violations propagate|

---

### **Interview Insights**

- Understand `isFrozen` and `isSealed` usage to verify object states.
- Be able to implement **deep freeze** and **deep seal** for nested immutability.
- Discuss how **strict mode** enforces immutability constraints in frozen/sealed objects.
- Practical application includes immutability for configs, Redux state, or sensitive data.



### **Limitations of `Object.freeze()` and `Object.seal()`**

#### **1. `Object.freeze()` Limitations**

|**Limitation**|**Details**|
|---|---|
|**Shallow Freezing**|Only freezes the top-level properties of an object. Nested objects are not frozen unless explicitly frozen.|
|**No Property Deletion**|Prevents adding, modifying, or deleting properties from the object. However, the **values** of existing properties that are mutable objects can still be modified.|
|**Performance Overhead**|For large objects, deep freezing can introduce a performance overhead, especially when applying it to nested objects.|

#### **2. `Object.seal()` Limitations**

|**Limitation**|**Details**|
|---|---|
|**No New Properties**|Prevents adding new properties to an object, but existing properties can still be modified if they are not marked as `readonly`.|
|**Shallow Behavior**|Like `freeze`, `seal` only applies to the immediate properties of the object and does not affect nested objects unless explicitly sealed.|
|**No Property Deletion**|Does not allow deleting properties, but it does allow modifying the values of existing properties (if not defined as `readonly`).|

---

### **When to Use Each in Real-World Scenarios**

#### **1. `Object.freeze()` Use Cases**

- **Immutability in Data Structures**: When you need to ensure the integrity of data structures (such as configurations or state) and prevent accidental changes. This is especially important in libraries or frameworks where maintaining the initial state is critical.
    
    - **Example**: Config objects in a React app to prevent modification after initialization.
- **Security and Data Integrity**: When working with sensitive data (such as a set of constants, API responses, or cryptographic keys) that should not be altered after being initialized.
    
    - **Example**: Ensuring that sensitive API response data cannot be altered.
- **Redux or State Management**: In Redux or similar state management libraries, `Object.freeze()` can help maintain immutable states across the app to avoid unwanted side effects.
    
    - **Example**: Freezing state objects in Redux reducers to ensure they remain immutable.

#### **2. `Object.seal()` Use Cases**

- **Prevent Property Addition**: When you want to ensure that no new properties can be added to an object but still allow existing properties to be modified. This is useful for scenarios where the shape of the object should remain consistent, but the values can be adjusted.
    - **Example**: When handling objects that represent records from a database, where the number of properties is fixed but the property values are subject to change.
- **Prevent Property Deletion**: When you want to prevent deletion of properties from objects, but still allow modifications to existing properties. This ensures that critical fields (such as ID, names) are not accidentally removed while still enabling value updates.
    - **Example**: Managing user session data where properties such as `userID`, `username` must exist, but other fields can be modified.

---

### **Summary: When to Use Each**

|**Scenario**|**Use `Object.freeze()`**|**Use `Object.seal()`**|
|---|---|---|
|**Prevent modification of object values**|When you need strict immutability for object values|When you only want to prevent adding/deleting properties, but allow modification of values.|
|**Prevent adding new properties**|If you need to freeze the object completely, including no new properties.|If you want to allow modification of existing values but prevent adding new properties.|
|**Prevent deleting properties**|If you need both adding and deleting to be restricted.|If you want to prevent property deletion but allow modification.|
|**Nested Object Handling**|If the object has nested objects, use `deepFreeze`.|If the object has nested objects, use `deepSeal`.|
|**Performance considerations**|Use `Object.freeze()` for smaller or non-deep objects; avoid deep freezing large structures unless necessary.|Use `Object.seal()` when deep nesting is not required and object shape changes are expected.|

---

### **Conclusion**

- Use `**Object.freeze()**` when you need complete immutability, especially in cases like managing configurations, constants, or Redux-like state.
- Use `**Object.seal()**` when you want to ensure that the shape of an object remains consistent (no new properties can be added or deleted) but still need the flexibility to modify existing properties.

For large-scale applications and complex data, it's also important to keep in mind the **performance** impact of deep freezing or sealing objects.


