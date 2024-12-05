
creational  - create object items for particular scenario 
structural - combined items to create bigger framework.. create relationship between
behavioural - comunicaiton between objects


| **Pattern**       | **Type**   | **Purpose**                                |
| ----------------- | ---------- | ------------------------------------------ |
| Module Pattern    | Structural | Organizes code with private/public access. |
| Singleton Pattern | Creational | Ensures only one instance of a class.      |
| Observer Pattern  | Behavioral | Manages object communication.              |
| Factory Pattern   | Creational | Simplifies object creation logic.          |
| Prototype Pattern | Creational | Shares methods via a prototype.            |

single , factory , prototype
modular
observer


This classification ensures clarity when choosing patterns for different design needs.
### **1. Module Pattern**

Encapsulates private and public members to expose only specific functionalities.

```javascript
const TaskModule = (() => {
  let tasks = []; // Private
  return {
    addTask(task) { tasks.push(task); },
    getTasks() { return tasks; },
  };
})();

TaskModule.addTask("Learn Module Pattern");
console.log(TaskModule.getTasks()); // ["Learn Module Pattern"]
```

---

### **2. Singleton Pattern**

Ensures only one instance of a class/object exists.

```javascript
class Settings {
  constructor() {
    if (Settings.instance) return Settings.instance;
    this.config = {};
    Settings.instance = this;
  }
  set(key, value) { this.config[key] = value; }
  get(key) { return this.config[key]; }
}

const instance1 = new Settings();
instance1.set("theme", "dark");
const instance2 = new Settings();
console.log(instance2.get("theme")); // "dark" (same instance)
```

---

### **3. Observer Pattern**

Allows objects (observers) to subscribe to a subject and get notified of changes.

```javascript
class Subject {
  constructor() { this.observers = []; }
  subscribe(observer) { this.observers.push(observer); }
  notify(data) { this.observers.forEach(obs => obs.update(data)); }
}

class Observer {
  update(data) { console.log("Notified:", data); }
}

const subject = new Subject();
const observer1 = new Observer();
subject.subscribe(observer1);
subject.notify("Hello Observers!"); // "Notified: Hello Observers!"
```

---

### **4. Factory Pattern**

Creates objects based on criteria without specifying their exact class.

```javascript
class Dog { speak() { console.log("Woof!"); } }
class Cat { speak() { console.log("Meow!"); } }

class AnimalFactory {
  static createAnimal(type) {
    return type === "dog" ? new Dog() : new Cat();
  }
}

const pet = AnimalFactory.createAnimal("dog");
pet.speak(); // "Woof!"
```

---

### **5. Prototype Pattern**

Creates objects that share methods and properties from a prototype.

```javascript
const carPrototype = {
  startEngine() { console.log("Engine started for", this.model); },
};

const car = Object.create(carPrototype);
car.model = "Tesla";
car.startEngine(); // "Engine started for Tesla"
```

---

### Summary

- **Module**: Encapsulate private/public parts.
- **Singleton**: Single instance shared globally.
- **Observer**: Notify subscribers of changes.
- **Factory**: Create objects dynamically.
- **Prototype**: Share methods across objects efficiently.


to check {

https://www.dofactory.com/javascript/design-patterns

https://www.ramotion.com/blog/javascript-design-patterns/

https://www.patterns.dev/

}


