
In JavaScript, there are several types of maps and collections that serve different purposes. Here are the main types:

### 1. **Object**
- **Usage**: The most basic key-value store. Keys are strings (or Symbols).
- **Example**:

```javascript
const obj = {
  name: 'Alice',
  age: 30
};

console.log(obj.name); // Output: Alice
```

### 2. **Map**
- **Usage**: A built-in collection that allows you to store key-value pairs. Keys can be of any type (objects, functions, etc.).
- **Features**:
  - Maintains the insertion order of keys.
  - Can use any value as a key.
  - Has a size property.
  
- **Example**:

```javascript
const map = new Map();
map.set('name', 'Alice');
map.set(1, 'one');
map.set({}, 'empty object');

console.log(map.get('name')); // Output: Alice
console.log(map.size); // Output: 3
```

### 3. **WeakMap**
- **Usage**: Similar to `Map`, but keys must be objects, and they are weakly referenced. This means that if there are no other references to the key object, it can be garbage-collected.
- **Features**:
  - Useful for caching and memory management.
  - Does not prevent garbage collection of keys.
  
- **Example**:

```javascript
const weakMap = new WeakMap();
const obj = {};

weakMap.set(obj, 'value');
console.log(weakMap.get(obj)); // Output: value

// Once `obj` is no longer referenced elsewhere, it can be garbage-collected.
```

### 4. **Set**
- **Usage**: A collection of unique values. Values can be of any type.
- **Features**:
  - Maintains the insertion order.
  - Automatically removes duplicate values.
  
- **Example**:

```javascript
const set = new Set();
set.add(1);
set.add(2);
set.add(1); // Duplicate will not be added

console.log(set.size); // Output: 2
console.log(set.has(1)); // Output: true
```

### 5. **WeakSet**
- **Usage**: Similar to `Set`, but it can only contain objects and holds weak references to them.
- **Features**:
  - Prevents memory leaks by allowing garbage collection of its elements.
  
- **Example**:

```javascript
const weakSet = new WeakSet();
const obj = {};

weakSet.add(obj);
console.log(weakSet.has(obj)); // Output: true

// Once `obj` is no longer referenced elsewhere, it can be garbage-collected.
```

### Summary
- **Object**: Basic key-value store, with string keys.
- **Map**: Key-value store with keys of any type, maintains order.
- **WeakMap**: Similar to `Map`, but keys are weakly referenced (for memory management).
- **Set**: Collection of unique values, maintains order.
- **WeakSet**: Similar to `Set`, but weakly references objects.

These collections provide flexibility for managing data and optimizing performance in JavaScript applications.

