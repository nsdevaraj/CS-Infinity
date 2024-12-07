### **Type Conversion / Casting in JavaScript**

Type conversion (or casting) is the process of explicitly converting a value from one data type to another using built-in functions like `String()`, `Number()`, `Boolean()`, etc.

---

### **String Conversion**

To convert a value to a string, use `String()` or `toString()`:

#### **Key Differences Between `String()` and `toString()`**

|**Aspect**|**`toString()`**|**`String()`**|
|---|---|---|
|**Type**|Method (belongs to an object).|Global function.|
|**Invocation**|Called on an object (`obj.toString()`).|Used globally (`String(value)`).|
|**Undefined/Null**|Throws `TypeError` for `null` or `undefined`.|Safely converts to `"null"` or `"undefined"`.|
|**Objects/Primitives**|Calls the object's `toString()` method.|Works across all data types safely.|
|**Example**|`true.toString()` → `"true"`.|`String(true)` → `"true"`.|

#### **Examples**

```javascript
const num = 42;
console.log(String(num));       // "42" (safe conversion)
console.log(num.toString());    // "42"

const booleanValue = true;
console.log(String(booleanValue)); // "true"
console.log(booleanValue.toString()); // "true"

const nullValue = null
console.log(String(nullValue));      // "null"
// console.log(nullValue.toString());
//: TypeError: Cannot read properties of null (reading 'toString')

const undefinedValue = undefined
console.log(String(undefinedValue)); // "undefined"
// console.log(undefinedValue.toString())
//: TypeError: Cannot read properties of undefined (reading 'toString')

```


Here’s the behavior of `toString()` and `String()` grouped by input values in a tabular format:

|**Input Value**|**toString()**|**String()**|
|---|---|---|
|`"123"`|`"123"`|`"123"`|
|`"123abc"`|`"123abc"`|`"123abc"`|
|`"abc123"`|`"abc123"`|`"abc123"`|
|`"123.45"`|`"123.45"`|`"123.45"`|
|`"123.45abc"`|`"123.45abc"`|`"123.45abc"`|
|`"abc"`|`"abc"`|`"abc"`|
|`"true"`|`"true"`|`"true"`|
|`false`|`"false"`|`"false"`|
|`undefined`|**TypeError** (Cannot call on `undefined`)|`"undefined"`|
|`null`|**TypeError** (Cannot call on `null`)|`"null"`|
|`123`|`"123"`|`"123"`|
|`NaN`|`"NaN"`|`"NaN"`|
|`[]` (Empty array)|`""`|`""`|
|`[1, 2, 3]` (Array)|`"1,2,3"`|`"1,2,3"`|
|`{}` (Empty object)|`"[object Object]"`|`"[object Object]"`|
|`function() {}` (Function)|`"function () {}"`|`"function () {}"`|

---

### Key Differences:

1. **`toString()`**:
    
    - **Can throw an error** when called on `null` or `undefined`.
    - Converts an object to a string using its own `toString()` method (for objects, arrays, etc.).
    - `null` and `undefined` cannot be used with `toString()`.
2. **`String()`**:
    
    - Safely converts **any value** to a string, including `null` and `undefined`.
    - Converts `null` to `"null"` and `undefined` to `"undefined"`.
    - Works across all types without throwing errors.

---

This table shows how **`toString()`** and **`String()`** handle different input values, highlighting their differences, especially with `null` and `undefined`.

#### **Best Practices**

- Use **`toString()`** if working directly with valid objects.
- Use **`String()`** for safe and general-purpose conversions.

---

### **Number Conversion**

To convert values to numbers, use `Number()`, `parseInt()`, or `parseFloat()`.

#### **Key Differences Between `Number()` and `parseInt()`/`parseFloat()`**

|**Method**|**Behavior**|**Parsing Type**|**Stops at Invalid Characters?**|
|---|---|---|---|
|**`Number(value)`**|Converts any value to a number.|Full conversion (floats included).|No.|
|**`parseInt(value)`**|Extracts integer from string.|Integer only.|Yes.|
|**`parseFloat(value)`**|Extracts floating-point from string.|Float only.|Yes.|

#### **Examples**

```javascript
// Number()
console.log(Number("123.45"));   // 123.45
console.log(Number("abc"));      // NaN
console.log(Number(true));       // 1
console.log(Number(false));      // 0

// parseInt()
console.log(parseInt("123.45")); // 123
console.log(parseInt("123abc")); // 123
console.log(parseInt("abc123")); // NaN

// parseFloat()
console.log(parseFloat("123.45abc")); // 123.45
```


Here’s the expanded table that includes how **Number()**, **parseInt()**, and **parseFloat()** behave when called with arrays and objects:

|**Input Value**|**Number()**|**parseInt()**|**parseFloat()**|
|---|---|---|---|
|`"123"`|123|123|123|
|`"123abc"`|NaN|123|123|
|`"abc123"`|NaN|NaN|NaN|
|`"123.45"`|123.45|123|123.45|
|`"123.45abc"`|NaN|123|123.45|
|`"abc"`|NaN|NaN|NaN|
|`"true"`|NaN|NaN|NaN|
|`false`|0|0|0|
|`undefined`|NaN|NaN|NaN|
|`null`|0|0|0|
|`[]` (Empty array)|0|0|0|
|`[1, 2, 3]` (Array)|3|3|3|
|`{}` (Empty object)|NaN|NaN|NaN|
|`{a: 1}` (Object with key)|NaN|NaN|NaN|
|`function(){}` (Function)|NaN|NaN|NaN|

---

### Explanation of Behaviors:

1. **Arrays:**
    - **`Number([])`**: Converts the array to a string first (`""`) and then to a number. `Number([])` returns `0`.
    - **`Number([1,2,3])`**: When using a non-empty array, it converts it to a string first (`"1,2,3"`) and then attempts conversion, which results in a `3`.
    - **`parseInt([1,2,3])`**: Interprets the first number in the string converted from the array (`"1"`).
    - **`parseFloat([1,2,3])`**: Similar behavior to `parseInt`, it finds only the first number (`1`) in string conversion.

---

2. **Objects:**
    - **`Number({})`**: Converts an empty object to a string (`"[object Object]"`), which cannot be converted to a number, leading to `NaN`.
    - **`parseInt({})` and `parseFloat({})`**: Objects are stringified to `"[object Object]"`, leading to `NaN`.

---

3. **Function:**
    - Calling `Number(function(){})` leads to `NaN`.
    - Parsing a function with `parseInt` or `parseFloat` also leads to `NaN`.

---

### Key Summary:

- Empty arrays return **0** when passed to `Number()`.
- Non-empty arrays behave differently depending on their string coercion (`[1,2,3]` → `"1,2,3"`).
- Objects return `NaN` with all parsing functions because their string coercion doesn't translate into numbers directly.
- Functions are treated as invalid inputs and lead to `NaN`.

---

### Explanation:

1. **`Number()`**: Converts the entire input to a number, returning `NaN` for invalid string conversions.
2. **`parseInt()`**: Converts integers up to the first invalid character and stops parsing there.
3. **`parseFloat()`**: Converts floating-point numbers up to the first invalid character.


#### **Best Practices**

- Use **`Number()`** for full and safe number conversion.
- Use **`parseInt()`/`parseFloat()`** to extract numbers from strings containing mixed characters.

---

### **Boolean Conversion**

To convert a value to a boolean, use `Boolean()`:

|**Input Value**|**Converted to Boolean**|
|---|---|
|`0`, `null`, `undefined`, `""`, `NaN`|`false`|
|All other values (e.g., non-empty strings, objects, etc.)|`true`|

#### **Examples**

```javascript
console.log(Boolean(0));         // false
console.log(Boolean(""));        // false
console.log(Boolean("hello"));   // true
console.log(Boolean(123));       // true
console.log(Boolean(null));      // false
```

---

### **Summary**

|**Function**|**Purpose**|**Behavior**|
|---|---|---|
|**`String(value)`**|Converts any value to a string safely.|Handles `null` and `undefined` safely.|
|**`toString()`**|Converts an object's value to a string.|Throws error on `null` or `undefined`.|
|**`Number(value)`**|Converts any value to a number.|Converts full strings; outputs `NaN` for invalid strings.|
|**`parseInt()`**|Extracts integer from a string.|Stops parsing at non-digit characters.|
|**`parseFloat()`**|Extracts floating-point number from a string.|Stops parsing at invalid characters.|
|**`Boolean(value)`**|Converts value to boolean (`true`/`false`).|`Falsy` values → `false`, others → `true`.|

---

### **Interview-Ready Code Snippets**

#### **String Conversion**

```javascript
let num = 123;
console.log(String(num));   // "123"
console.log((123).toString()); // "123"
console.log(String(null));  // "null"
```

#### **Number Conversion**

```javascript
let str = "123.45";
console.log(Number(str));       // 123.45
console.log(parseInt(str));     // 123
console.log(parseFloat(str));   // 123.45
```

#### **Boolean Conversion**

```javascript
console.log(Boolean(0));        // false
console.log(Boolean("hello"));  // true
```

**Key Tip:** Always choose the right conversion method based on input and error handling requirements.