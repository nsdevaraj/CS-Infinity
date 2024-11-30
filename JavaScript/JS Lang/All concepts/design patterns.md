
creational  - create object items for particular scenario
structural - combined items to create bigger framework.. create relationship between
behavioural - comunicaiton between objects



Certainly! Here’s a breakdown of some widely-used design patterns in JavaScript, along with code examples for each. We'll go through the **Module**, **Singleton**, **Observer**, **Factory**, and **Prototype** patterns.

---

### **1. Module Pattern**
The Module Pattern is used to encapsulate private and public parts within a single object. This allows us to expose only specific functionalities to the outside, making the rest private.

#### Example:

```javascript
const TaskModule = (() => {
  // Private variables and functions
  let tasks = [];

  const addTask = (task) => {
    tasks.push(task);
    console.log(`Task "${task}" added.`);
  };

  const getTasks = () => tasks;

  // Public API
  return {
    addTask,
    getTasks,
  };
})();

TaskModule.addTask("Complete module pattern");
console.log(TaskModule.getTasks()); // ["Complete module pattern"]
```

Here, `TaskModule` provides public access to `addTask` and `getTasks` while keeping the `tasks` array private.

---

### **2. Singleton Pattern**
The Singleton Pattern ensures that only one instance of a class or object is created and provides a global point of access to it.

#### Example:

```javascript
class Settings {
  constructor() {
    if (Settings.instance) {
      return Settings.instance;
    }
    this.settings = {};
    Settings.instance = this;
  }

  set(key, value) {
    this.settings[key] = value;
  }

  get(key) {
    return this.settings[key];
  }
}

const appSettings1 = new Settings();
const appSettings2 = new Settings();

appSettings1.set("theme", "dark");
console.log(appSettings2.get("theme")); // "dark" - same instance
console.log(appSettings1 === appSettings2); // true - only one instance
```

This example ensures that `appSettings1` and `appSettings2` refer to the same instance of `Settings`.

---

### **3. Observer Pattern**
The Observer Pattern is useful for implementing subscription-based functionality, where objects (observers) subscribe to another object (subject) and are notified when it changes.

#### Example:

```javascript
class Subject {
  constructor() {
    this.observers = [];
  }

  subscribe(observer) {
    this.observers.push(observer);
  }

  unsubscribe(observer) {
    this.observers = this.observers.filter((obs) => obs !== observer);
  }

  notify(data) {
    this.observers.forEach((observer) => observer.update(data));
  }
}

class Observer {
  update(data) {
    console.log("Observer received:", data);
  }
}

// Usage
const subject = new Subject();
const observer1 = new Observer();
const observer2 = new Observer();

subject.subscribe(observer1);
subject.subscribe(observer2);

subject.notify("Hello Observers!"); // Both observers receive the update
```

In this example, `Subject` manages a list of observers and notifies them of any changes.

---

### **4. Factory Pattern**
The Factory Pattern provides a way to create objects based on some criteria without specifying the exact class of the object that will be created.

#### Example:

```javascript
class Dog {
  speak() {
    console.log("Woof!");
  }
}

class Cat {
  speak() {
    console.log("Meow!");
  }
}

class AnimalFactory {
  static createAnimal(type) {
    switch (type) {
      case "dog":
        return new Dog();
      case "cat":
        return new Cat();
      default:
        throw new Error("Animal type not recognized");
    }
  }
}

// Usage
const myPet = AnimalFactory.createAnimal("dog");
myPet.speak(); // "Woof!"
```

Here, `AnimalFactory` decides which type of animal to create based on the input type.

---

### **5. Prototype Pattern**
The Prototype Pattern is used to create objects based on a prototype, enabling shared properties and methods across instances without creating multiple copies.

#### Example:

```javascript
const carPrototype = {
  startEngine() {
    console.log("Engine started for", this.model);
  },
};

const myCar = Object.create(carPrototype);
myCar.model = "Tesla Model S";
myCar.startEngine(); // "Engine started for Tesla Model S"

const anotherCar = Object.create(carPrototype);
anotherCar.model = "BMW X5";
anotherCar.startEngine(); // "Engine started for BMW X5"
```

Here, `carPrototype` serves as a prototype, allowing instances like `myCar` and `anotherCar` to share the `startEngine` method without duplicating it.

---

These are just a few foundational design patterns. They’re effective for organizing code and managing complex JavaScript applications, making your code cleaner, more modular, and maintainable. Let me know if you want more details or additional patterns!




to check {

https://www.dofactory.com/javascript/design-patterns

https://www.ramotion.com/blog/javascript-design-patterns/

https://www.patterns.dev/

}


