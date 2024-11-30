
In JavaScript, all object keys are either strings or symbols. When you use a non-string value (like a number) as a key, JavaScript automatically converts it to a string. For example:

```javascript
const obj = {};
obj[123] = "value"; // 123 is converted to "123"
console.log(obj["123"]); // "value"
```

However, if you use a `Symbol` as a key, it remains a unique and non-string key:

```javascript
const sym = Symbol("mySymbol");
const obj = {
  [sym]: "value"
};
console.log(obj[sym]); // "value"
```

So, while strings are the most common key type, symbols provide an alternative for unique keys.

