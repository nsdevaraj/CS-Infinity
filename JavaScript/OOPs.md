

Object-Oriented Programming (OOP) in JavaScript is a programming paradigm based on the concept of "objects," which can contain data (properties) and code (methods). Here are the key concepts of OOP in JavaScript:

### 1. **Objects**
An object is a collection of properties, where each property is defined as a key-value pair.

```javascript
const car = {
  make: 'Toyota',
  model: 'Camry',
  year: 2021,
  start: function() {
    console.log('Car started');
  }
};

console.log(car.make); // Output: Toyota
car.start(); // Output: Car started
```

### 2. **Constructor Functions**
You can create multiple instances of an object using constructor functions. A constructor function is a regular function that is used to create objects.

```javascript
function Car(make, model, year) {
  this.make = make;
  this.model = model;
  this.year = year;
  this.start = function() {
    console.log('Car started');
  };
}

const myCar = new Car('Honda', 'Civic', 2020);
myCar.start(); // Output: Car started
```

### 3. **Prototypes**
JavaScript uses prototypes for inheritance. Each object has a prototype property that can be used to share methods or properties among instances.

```javascript
function Car(make, model, year) {
  this.make = make;
  this.model = model;
  this.year = year;
}

Car.prototype.start = function() {
  console.log('Car started');
};

const myCar = new Car('Honda', 'Civic', 2020);
myCar.start(); // Output: Car started
```

### 4. **Classes (ES6+)**
With ES6, JavaScript introduced class syntax, which provides a clearer way to create objects and handle inheritance.

```javascript
class Car {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  start() {
    console.log('Car started');
  }
}

const myCar = new Car('Honda', 'Civic', 2020);
myCar.start(); // Output: Car started
```

### 5. **Inheritance**
You can create a new class that inherits from another class using the `extends` keyword.

```javascript
class Vehicle {
  constructor(make, model) {
    this.make = make;
    this.model = model;
  }

  start() {
    console.log('Vehicle started');
  }
}

class Car extends Vehicle {
  constructor(make, model, year) {
    super(make, model); // Call the parent class constructor
    this.year = year;
  }

  start() {
    console.log(`${this.make} ${this.model} started`);
  }
}

const myCar = new Car('Honda', 'Civic', 2020);
myCar.start(); // Output: Honda Civic started
```

### 6. **Encapsulation**
Encapsulation is achieved using closures or more recently with the introduction of private fields (using `#` syntax).

```javascript
class Car {
  #speed; // private field

  constructor(make, model) {
    this.make = make;
    this.model = model;
    this.#speed = 0; // initial speed
  }

  accelerate(amount) {
    this.#speed += amount;
    console.log(`Accelerating: ${this.#speed} km/h`);
  }
}

const myCar = new Car('Honda', 'Civic');
myCar.accelerate(50); // Output: Accelerating: 50 km/h
```

### Summary
OOP in JavaScript allows for better organization, reusability, and scalability of code. Key concepts include objects, constructor functions, prototypes, classes, inheritance, and encapsulation. Understanding these will help you effectively utilize OOP principles in your JavaScript projects!



---


Advanced Object-Oriented Programming (OOP) concepts in JavaScript go beyond the basics and involve deeper understanding of the language's features and design patterns. Here are some advanced OOP concepts in JavaScript:

### 1. **Inheritance Patterns**
   - **Classical Inheritance**: While JavaScript primarily uses prototypal inheritance, you can simulate classical inheritance using constructor functions and `Object.create()`.

   ```javascript
   function Animal(name) {
     this.name = name;
   }

   Animal.prototype.speak = function() {
     console.log(`${this.name} makes a noise.`);
   };

   function Dog(name) {
     Animal.call(this, name); // Call the parent constructor
   }

   Dog.prototype = Object.create(Animal.prototype);
   Dog.prototype.constructor = Dog;

   Dog.prototype.speak = function() {
     console.log(`${this.name} barks.`);
   };

   const dog = new Dog('Rex');
   dog.speak(); // Output: Rex barks.
   ```

### 2. **Mixins**
   Mixins allow you to add functionality from multiple sources to a single class. This helps avoid the limitations of single inheritance.

   ```javascript
   const CanFly = {
     fly() {
       console.log(`${this.name} is flying!`);
     }
   };

   const CanSwim = {
     swim() {
       console.log(`${this.name} is swimming!`);
     }
   };

   class Bird {
     constructor(name) {
       this.name = name;
     }
   }

   Object.assign(Bird.prototype, CanFly);

   class Fish {
     constructor(name) {
       this.name = name;
     }
   }

   Object.assign(Fish.prototype, CanSwim);

   const eagle = new Bird('Eagle');
   eagle.fly(); // Output: Eagle is flying!

   const shark = new Fish('Shark');
   shark.swim(); // Output: Shark is swimming!
   ```

### 3. **Encapsulation with Symbols and WeakMaps**
   Using `Symbols` or `WeakMaps` can help achieve true encapsulation by hiding private properties.

   ```javascript
   const privateData = new WeakMap();

   class User {
     constructor(name, age) {
       privateData.set(this, { age });
       this.name = name;
     }

     getAge() {
       return privateData.get(this).age;
     }
   }

   const user = new User('Alice', 30);
   console.log(user.getAge()); // Output: 30
   ```

### 4. **Static Methods and Properties**
   Static methods and properties belong to the class itself rather than any instance of the class. They're often used for utility functions.

   ```javascript
   class MathUtils {
     static add(x, y) {
       return x + y;
     }

     static multiply(x, y) {
       return x * y;
     }
   }

   console.log(MathUtils.add(2, 3)); // Output: 5
   ```

### 5. **Getters and Setters**
   Getters and setters allow you to define how properties are accessed and modified, enabling better control over property values.

   ```javascript
   class Rectangle {
     constructor(width, height) {
       this.width = width;
       this.height = height;
     }

     get area() {
       return this.width * this.height;
     }

     set dimensions({ width, height }) {
       this.width = width;
       this.height = height;
     }
   }

   const rect = new Rectangle(10, 5);
   console.log(rect.area); // Output: 50
   rect.dimensions = { width: 20, height: 10 };
   console.log(rect.area); // Output: 200
   ```

### 6. **Abstract Classes and Interfaces**
   JavaScript does not have built-in support for abstract classes or interfaces, but you can create similar behavior using conventions.

   ```javascript
class Shape {
  constructor() {
    if (this.constructor === Shape) {
      throw new Error('Cannot instantiate abstract class');
    }
    // or this
    // if (new.target === Shape) {
    //   throw new Error('Cannot instantiate abstract class Animal');
    // }
  }

  area() {
    throw new Error('Method "area()" must be implemented');
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }

  area() {
    return Math.PI * this.radius ** 2;
  }
}

// const shape = new Shape(); // Throws error
const circle = new Circle(5);
console.log(circle.area()); // Output: 78.53981633974483

   ```

### 7. **Method Overriding**
   Subclasses can override methods defined in parent classes, providing specific implementations.

   ```javascript
   class Animal {
     speak() {
       console.log('Animal speaks');
     }
   }

   class Cat extends Animal {
     speak() {
       console.log('Meow');
     }
   }

   const cat = new Cat();
   cat.speak(); // Output: Meow
   ```

### Conclusion
These advanced OOP concepts in JavaScript can help you build more robust, flexible, and maintainable code. Understanding these principles will enable you to design complex applications with clear architecture and reusable components.