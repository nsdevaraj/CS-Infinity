


* refers to the object that is prototye of



## This  in ES6

### Understanding "this" in JavaScript and ES6

#### 1. **Traditional Function Context**
In JavaScript, the value of `this` is determined by how a function is called. This can lead to confusion, especially in callback functions or nested functions.

**Example**:
```javascript
function Person(name) {
    this.name = name;
    this.sayName = function() {
        console.log(this.name);
    };
}

const john = new Person('John');
john.sayName(); // Outputs: John

const say = john.sayName;
say(); // Outputs: undefined (or throws an error in strict mode)
```

Here, calling `say()` loses the context of `john`, resulting in `this` referring to the global object or `undefined`.

#### 2. **Arrow Functions in ES6**
Arrow functions introduced in ES6 provide a more predictable way to handle `this`. They do not have their own `this` context; instead, they inherit `this` from the enclosing lexical scope.

**Example**:
```javascript
function Person(name) {
    this.name = name;
    this.sayName = () => {
        console.log(this.name);
    };
}

const jane = new Person('Jane');
jane.sayName(); // Outputs: Jane

const say = jane.sayName;
say(); // Outputs: Jane
```

In this example, the arrow function maintains the `this` context of the `Person` instance, making it behave as expected when `say()` is called.

#### 3. **Class Syntax and ES6**
With ES6, JavaScript introduced class syntax, which also clarifies `this` usage in constructors and methods.

**Example**:
```javascript
class Person {
    constructor(name) {
        this.name = name;
    }

    sayName() {
        console.log(this.name);
    }
}

const mike = new Person('Mike');
mike.sayName(); // Outputs: Mike

const say = mike.sayName;
say(); // Outputs: undefined (or throws an error in strict mode)
```

Even though `this` works as expected in methods, you still face issues with traditional function references. You can still use arrow functions in class methods to maintain the context:

```javascript
class Person {
    constructor(name) {
        this.name = name;
    }

    sayName = () => {
        console.log(this.name);
    }
}

const lucy = new Person('Lucy');
const say = lucy.sayName;
say(); // Outputs: Lucy
```

### Summary
- **Traditional Functions**: `this` is context-sensitive and can lead to confusion.
- **Arrow Functions**: Capture `this` from their surrounding context, avoiding common pitfalls.
- **Class Syntax**: Introduces clearer structures but still requires careful handling of `this` when using traditional functions.

ES6 significantly improves the way `this` is handled in JavaScript, making code more intuitive and reducing common errors.






// this => global in arrow func.. 

