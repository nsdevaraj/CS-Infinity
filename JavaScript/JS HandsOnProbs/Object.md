


### **41. How would you implement a function to deeply merge two objects?**

#### **Answer:**

```javascript
function deepMerge(target, source) {
  for (const key of Object.keys(source)) {
    if (source[key] instanceof Object) {
      target[key] = deepMerge(target[key] || {}, source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}
// Usage:
const obj1 = { a: { b: 1 } };
const obj2 = { a: { c: 2 } };
console.log(deepMerge(obj1, obj2)); // { a: { b: 1, c: 2 } }
```




### **17. How would you implement a deep comparison function?**

#### **Answer:**

```javascript
function deepEqual(a, b) {
  if (a === b) return true;
  if (typeof a !== 'object' || typeof b !== 'object' || a == null || b == null) return false;

  const keysA = Object.keys(a);
  const keysB = Object.keys(b);

  if (keysA.length !== keysB.length) return false;
  return keysA.every(key => deepEqual(a[key], b[key]));
}
```




### **14. How do you deep clone an object in JavaScript?**

#### **Answer:**

```javascript
const deepClone = obj => JSON.parse(JSON.stringify(obj));
```




### **10. How do you handle circular references in JSON?**

#### **Answer:**

```javascript
function safeStringify(obj) {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (typeof value === "object" && value !== null) {
      if (seen.has(value)) return undefined;
      seen.add(value);
    }
    return value;
  });
}
```


