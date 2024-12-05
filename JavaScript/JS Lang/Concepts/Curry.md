


## Func currying

### Curry Function

**Currying** is a functional programming technique in which a function is transformed into a sequence of functions, each taking a single argument. Instead of taking multiple arguments at once, a curried function takes one argument and returns another function that takes the next argument, and so on, until all arguments have been supplied.

#### Example of a Curry Function

Here's a simple example of a curried function:

```javascript
// A simple curried function
function add(a) {
    return function(b) {
        return a + b;
    };
}

// Using the curried function
const addFive = add(5); // Returns a function that adds 5
console.log(addFive(10)); // Output: 15
console.log(add(5)(10)); // Output: 15
```

In this example, `add` is a curried function that takes one argument `a` and returns another function that takes the next argument `b`. This allows for partial application, where you can create specialized functions (like `addFive`).

### Advantages of Currying

1. **Partial Application**:
   - Currying allows you to create functions that can be partially applied. This means you can fix some arguments and create new functions, making your code more modular and reusable.
   - **Example**:
     ```javascript
     const multiply = (x) => (y) => x * y;
     const double = multiply(2); // Fixing the first argument to 2
     console.log(double(5)); // Output: 10
     ```

2. **Enhanced Readability and Clarity**:
   - Currying can make the intent of the code clearer. Each function handles a single responsibility, which improves readability and understanding.

3. **Function Composition**:
   - Curried functions can be easily composed, allowing you to build more complex functions from simpler ones. This leads to cleaner and more maintainable code.
   - **Example**:
     ```javascript
     const add = (x) => (y) => x + y;
     const multiply = (x) => (y) => x * y;

     const addAndMultiply = (x) => multiply(2)(add(x)(3)); // Composing functions
     console.log(addAndMultiply(4)); // Output: 14
     ```

4. **Improved Functionality in Higher-Order Functions**:
   - Currying allows functions to be passed as arguments with specific parameters already set, making them easier to work with in higher-order functions and callbacks.

5. **Flexibility**:
   - It provides flexibility in function usage and allows for creating a variety of functions from a single curried function.

### Conclusion

Currying is a powerful technique that enhances the expressiveness and modularity of JavaScript code. By enabling partial application and function composition, currying can lead to cleaner, more maintainable code that adheres to functional programming principles. It promotes reusability and clarity, making it easier to build complex behaviors from simple functions.




#### Currying 

```js

const sum = (a,b,c) => a+b+c


const wrapCurry = (func) => {
    return function curried(...args){
        if(args.length === func.length){
            return func(...args)
        }else{
            return (...nextArgs) => curried(...args, ...nextArgs);
        }
    }
}

const wrapCurry2 = (func) => {
    return function curried(...args){
        if(args.length === func.length){
            return () => func(...args)
        }else{
            return (...nextArgs) => curried(...args, ...nextArgs);
        }
    }
}

const currySum3 = (arg1) => {
    return function (arg2) {
        if(arg2 === undefined){
            return arg1
        }else{
            return currySum3(arg1+arg2)
        }
    }
}

const unWrapCurry = (func) => {
    return function (...args) {
        return args.reduce((fn,arg)=> fn(arg), func)
    } 
}

console.log(sum(1,2,3))
const currySum = wrapCurry(sum)
console.log(currySum(1)(2)(3))

const currySum2 = wrapCurry2(sum)
console.log(currySum2(1)(2)(3)())

console.log(currySum3(1)(2)(3)())

const unWrapCurrySum = unWrapCurry(currySum)
console.log(unWrapCurrySum(1,2,3))



```





### **21. How do you implement currying in JavaScript?**

#### **Answer:**

```javascript
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func(...args);
    } else {
      return (...nextArgs) => curried(...args, ...nextArgs);
    }
  };
}
// Usage:
const sum = (a, b, c) => a + b + c;
const curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3)); // 6
```


### Popular JavaScript Currying Interview Questions with Answers

---

### **1. What is currying in JavaScript?**

**Answer:** Currying is a technique where a function with multiple arguments is transformed into a sequence of functions, each taking a single argument.

**Example:**

```javascript
function multiply(a) {
  return function (b) {
    return a * b;
  };
}
const multiplyBy2 = multiply(2);
console.log(multiplyBy2(5)); // 10
console.log(multiply(3)(4)); // 12
```

---

### **2. Implement a function that converts a normal function to a curried function.**

**Answer:**

```javascript
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func.apply(this, args); // Invoke the function if all arguments are supplied
    } else {
      return function (...nextArgs) {
        return curried.apply(this, args.concat(nextArgs)); // Keep collecting arguments
      };
    }
  };
}

// Example:
function sum(a, b, c) {
  return a + b + c;
}
const curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3)); // 6
console.log(curriedSum(1, 2)(3)); // 6
```

---

### **3. How can currying be used to create reusable functions?**

**Answer:** Currying allows partial application of arguments, creating specialized versions of a function.

**Example:**

```javascript
function calculate(operation) {
  return function (a) {
    return function (b) {
      if (operation === 'add') return a + b;
      if (operation === 'multiply') return a * b;
    };
  };
}

const add = calculate('add');
const multiply = calculate('multiply');

console.log(add(5)(3)); // 8
console.log(multiply(5)(3)); // 15
```

---

### **4. Create a curried version of a function to filter an array.**

**Answer:**

```javascript
const filter = (criteria) => (array) => array.filter(criteria);

// Example:
const isEven = (num) => num % 2 === 0;
const filterEvens = filter(isEven);

console.log(filterEvens([1, 2, 3, 4, 5])); // [2, 4]
```

---

### **5. Write a curried function for logging with different prefixes.**

**Answer:**

```javascript
const logger = (prefix) => (message) => console.log(`${prefix}: ${message}`);

// Example:
const errorLogger = logger('Error');
const infoLogger = logger('Info');

errorLogger('Something went wrong!'); // "Error: Something went wrong!"
infoLogger('All systems operational.'); // "Info: All systems operational."
```

---

### **6. Convert a curried function back to a normal function.**

**Answer:**

```javascript
function uncurry(curried) {
  return function (...args) {
    return args.reduce((fn, arg) => fn(arg), curried);
  };
}

// Example:
const curriedSum = (a) => (b) => (c) => a + b + c;
const normalSum = uncurry(curriedSum);

console.log(normalSum(1, 2, 3)); // 6
```

---

### **7. Write a function that sums an indefinite number of arguments using currying.**

**Answer:**

```javascript
function sum(a) {
  return function (b) {
    if (b !== undefined) {
      return sum(a + b);
    }
    return a;
  };
}

// Example:
console.log(sum(1)(2)(3)()); // 6
console.log(sum(4)(5)());    // 9
```

---

### **8. Explain the difference between partial application and currying.**

**Answer:**

- **Currying**: Transforms a function into nested functions, each taking one argument at a time.
- **Partial Application**: Pre-fixes some arguments of a function, creating a new function with fewer parameters.

**Example:**

```javascript
// Currying:
const curriedAdd = (a) => (b) => a + b;
console.log(curriedAdd(1)(2)); // 3

// Partial Application:
const add = (a, b) => a + b;
const add5 = add.bind(null, 5);
console.log(add5(3)); // 8
```

---

### **9. Implement a curried function for string formatting.**

**Answer:**

```javascript
function format(prefix) {
  return function (suffix) {
    return function (message) {
      return `${prefix}${message}${suffix}`;
    };
  };
}

// Example:
const withBrackets = format('[')(']');
console.log(withBrackets('Hello')); // "[Hello]"
```

---

### **10. How can currying help in React or functional programming?**

**Answer:** Currying simplifies passing configurations or arguments incrementally.

**Example:**

```javascript
const connect = (mapState) => (mapDispatch) => (Component) => {
  // Hypothetical connect logic
  return function (props) {
    return `<Connected ${Component} />`;
  };
};

const mapStateToProps = (state) => state.user;
const mapDispatchToProps = (dispatch) => ({ login: () => dispatch('LOGIN') });

const connectedComponent = connect(mapStateToProps)(mapDispatchToProps)('MyComponent');
console.log(connectedComponent); // "<Connected MyComponent />"
```

---


