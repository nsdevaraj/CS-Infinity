


https://www.youtube.com/watch?v=CJUAL18dbKs


to check {

https://www.youtube.com/watch?v=Th3rZjfKKhI


}



In JavaScript, higher-order functions are those that take other functions as arguments or return functions. Array methods like `map`, `forEach`, `filter`, and `reduce` are higher-order functions and widely used. Additionally, `call`, `apply`, and `bind` are methods of JavaScript functions that help manage function contexts (`this`). Here’s a breakdown and polyfill examples for each:

### 1. **`Array.prototype.map`**
The `map` method creates a new array populated with the results of calling a provided function on every element in the calling array.

**Polyfill for `map`:**
```javascript
Array.prototype.myMap = function(callback) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    if (this.hasOwnProperty(i)) {
      result.push(callback(this[i], i, this));
    }
  }
  return result;
};
```

### 2. **`Array.prototype.forEach`**
The `forEach` method executes a provided function once for each array element.

**Polyfill for `forEach`:**
```javascript
Array.prototype.myForEach = function(callback) {
  for (let i = 0; i < this.length; i++) {
    if (this.hasOwnProperty(i)) {
      callback(this[i], i, this);
    }
  }
};
```

### 3. **`Array.prototype.filter`**
The `filter` method creates a new array with all elements that pass the test implemented by the provided function.

**Polyfill for `filter`:**
```javascript
Array.prototype.myFilter = function(callback) {
  let result = [];
  for (let i = 0; i < this.length; i++) {
    if (this.hasOwnProperty(i) && callback(this[i], i, this)) {
      result.push(this[i]);
    }
  }
  return result;
};
```

### 4. **`Array.prototype.reduce`**
The `reduce` method executes a reducer function on each element of the array, resulting in a single output value.

**Polyfill for `reduce`:**
```javascript
Array.prototype.myReduce = function(callback, initialValue) {
  let accumulator = initialValue === undefined ? this[0] : initialValue;
  let startIdx = initialValue === undefined ? 1 : 0;

  for (let i = startIdx; i < this.length; i++) {
    if (this.hasOwnProperty(i)) {
      accumulator = callback(accumulator, this[i], i, this);
    }
  }
  return accumulator;
};
```

### 5. **`Function.prototype.call`**
The `call` method calls a function with a given `this` value and arguments provided individually.

**Polyfill for `call`:**
```javascript
Function.prototype.myCall = function(context = {}, ...args) {
  context.fn = this;
  const result = context.fn(...args);
  delete context.fn;
  return result;
};
```

### 6. **`Function.prototype.apply`**
The `apply` method calls a function with a given `this` value, and arguments provided as an array.

**Polyfill for `apply`:**
```javascript
Function.prototype.myApply = function(context = {}, args = []) {
  context.fn = this;
  const result = context.fn(...args);
  delete context.fn;
  return result;
};
```

### 7. **`Function.prototype.bind`**
The `bind` method creates a new function that, when called, has its `this` keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.

**Polyfill for `bind`:**
```javascript
Function.prototype.myBind = function(context, ...args) {
  const fn = this;
  return function(...newArgs) {
    return fn.apply(context, [...args, ...newArgs]);
  };
};
```

These polyfills mimic the behavior of the native methods while giving a solid understanding of how higher-order functions and `this` binding work in JavaScript.




