
## Paradigms:

- a way of thinking about and structuring code to solve problems


![[_imgs/Pasted image 20250416064733.png]]

### Main Categories

### 1. Imperative  — _"How to do it"_

**HOW** the program should do something by explicitly specifying each instruction (or statement) step by step, which mutate the program's state... 

#### Key Subtypes:

- **Structural Programming**  
    Emphasizes control structures like loops, conditionals, and blocks for organized flow.  
    _Examples: C, Pascal_
    
- **Procedural Programming**  
    Builds on structural programming with reusable procedures and functions.  ( simplicity, reusable )
    _Examples: C, Python (procedural style)_
    
- **Object-Oriented Programming (OOP)**  
    Organizes code around objects—encapsulating data and behavior. ( everything seen as object )
    _Examples: Java, C++, C#_


### 2. Declarative  — _"What to do"_

**WHAT** the program does, without explicitly specifying its control flow.
#### Key Subtypes:

- **Functional Programming**  
    Based on pure functions, immutability, and stateless computations.  
    _Examples: Haskell, Elm, JavaScript (FP style)_
    
- **Reactive Programming**  
    Deals with data streams, asynchronous flows, and event-driven models.  
    _Examples: RxJS, SolidJS_
    
- **Logic Programming**  
    Specifies rules and facts; the system derives conclusions.  
    _Example: Prolog_
    
- **Query/Data-driven Programming**  
    Focuses on data retrieval and manipulation through queries.  
    _Examples: SQL, GraphQL_


Every paradigm has its pros and cons, so adoption of a paradigm changes based on use-cases . Mostly combination of 2 paradigms were followed in most software.

---

## Why Learn FP

- it’s becoming a foundational approach in modern software development. Most modern programming languages adopts FP paradigm
- not only write clearer, and more maintainable code but also its scalable and safer


---


## Core Concepts of Functional Programming

* writing software by composing pure functions, avoiding shared state (immutability), and minimizing side effects. 

### 1. Pure Functions

A **pure function** is one that:
- **Deterministic**: Always returns the same output for the same input.
- **No Side Effects**: Does not alter any external state or perform observable interactions with the outside world.


```typescript
// Pure Function
function add(a: number, b: number): number {
  return a + b;
}
```

This function is pure because it doesn't rely on or modify any external state.

---

### 2. Immutability

Immutability means that once a data structure is created, it cannot be changed. Instead of modifying existing data, new data structures are created with the desired changes.

```typescript
const originalArray = [1, 2, 3];
const newArray = [...originalArray, 4]; // originalArray remains unchanged
```

Here, `newArray` is a new array with the added element, while `originalArray` remains unchanged.

---

### 3. No Side Effects

Side effects are any observable interactions with the outside world or changes to external state that occur during function execution. 

```typescript
let counter = 0;

function increment(): number {
  counter += 1; // Side effect: modifies external state
  return counter;
}
```

This function has a side effect because it modifies the external variable `counter`.

---
### Immutability advantage explained at specific scenario :

![[_imgs/Pasted image 20250416114252.png]]


In your code:

```javascript
let counter = 0;

for (let i = 0; i < 100; i++) {
  counter += 1;
}

for (let i = 0; i < 100; i++) {
  counter += 1;
}
```

If run in a **single-threaded** JavaScript environment, it works fine and you end up with `counter = 200`.

But in a **multi-threaded** environment (like in some JavaScript engines with Web Workers, or in other languages like Java, C++, etc.), if two threads run these loops **simultaneously**, they might interfere with each other. This is called a **race condition**.

For example, both threads read the same value (say 99), increment it to 100, and write back 100—so one increment gets lost.


 #### Solution 1: Mutex (Mutual Exclusion)

A **mutex** ensures that only one thread can access the shared variable (`counter`) at a time.


```javascript
let counter = 0;
let mutex = new Mutex();

for (let i = 0; i < 100; i++) {
  mutex.lock();
  counter += 1;
  mutex.unlock();
}
```

In real systems (like with C++ or Java), this is done using libraries like `std::mutex` or `synchronized`.

Only one thread can enter the critical section at a time, so no updates get lost. But mutexes can lead to **performance bottlenecks** ( critical section is accessed by one thread at a time ) or **deadlocks** if not used carefully.


#### Solution 2: Immutability & Functional Programming

In **functional programming**, we avoid **shared mutable state** entirely.

Instead of modifying `counter`, we create new values and pass them around.

### Functional Style Example (conceptual):

```javascript
const incrementNTimes = (start, times) =>
  Array(times).fill(1).reduce((sum, val) => sum + val, start);

const result1 = incrementNTimes(0, 100);
const result2 = incrementNTimes(result1, 100);
```

Or even better: Run in parallel without sharing state:

```javascript
const result1 = incrementNTimes(0, 100);
const result2 = incrementNTimes(0, 100);
const total = result1 + result2;
```

Each thread or function works with its own **copy of the data**, so there's no race condition. This is inherently **thread-safe**.

Immutable data ensures:
* Thread safely - No writes, only reads
* Consistency - state cannot change unexpectedly
* Simplicity - No locking mechanisms needed


---

## Getting back to FP:

* writing software by composing pure functions, avoiding shared state, and minimising side effects. 


![[_imgs/Pasted image 20250416093010.png]]

Building software by executing function after functions to get the desired result from given input.


Core concept:
- **there shall be no State** 
- you have inputs which are transformed into outputs in order to get stuff done 
- you compose and connect functions to other functions hooking up their inputs and outputs together into one big long chain that achieves the goal of the program 
- but you don't have objects or structures in memory that you mutate to track what's going on


---
## Benefits of Functional Programming

### 1. Predictability

Pure functions ensure that the same input always yields the same output, making the system behavior predictable.

**Real-World Scenario:** In financial applications, calculating interest should consistently produce the same result for the same inputs.

**Functional Approach:**

```typescript
function calculateInterest(principal: number, rate: number, time: number): number {
  return principal * rate * time;
}
```

**Imperative Approach:**

```typescript
let globalRate = 0.05;

function calculateInterest(principal: number, time: number): number {
  return principal * globalRate * time; // Depends on external state
}
```

The functional approach is predictable, while the imperative one depends on external state, making it less predictable.

---
### 2. Testability

Pure functions are easier to test because they don't rely on external state or cause side effects.

**Real-World Scenario:** Validating user credentials should be straightforward to test without dependencies on external systems.

**Functional Approach:**

```typescript
function isValidUser(username: string, password: string): boolean {
  return username === 'admin' && password === 'secure123';
}
```

**Imperative Approach:**

```typescript
let currentUser: string;

function login(username: string, password: string): boolean {
  if (username === 'admin' && password === 'secure123') {
    currentUser = username; // Side effect: modifies external state
    return true;
  }
  return false;
}
```

The functional version is self-contained and easily testable, whereas the imperative version's reliance on external state complicates testing.

---
### 3. Concurrency Safety

Pure functions and immutability make concurrent programming safer by avoiding shared mutable state, thus preventing race conditions.

**Real-World Scenario:** In web servers handling multiple requests simultaneously, pure functions ensure that each request is processed independently.

**Functional Approach:**

```typescript
function processData(input: string): string {
  return input.trim().toUpperCase();
}
```

**Imperative Approach:**

```typescript
let sharedData: string = '';

function processData(input: string): string {
  sharedData += input.trim().toUpperCase(); // Side effect: modifies shared state
  return sharedData;
}
```

The functional version avoids shared state, making it safer for concurrent execution.

---
### 4. Referential Transparency

In FP, expressions can be replaced with their corresponding values without changing the program's behavior, facilitating reasoning and optimization.

**Real-World Scenario:** In caching mechanisms, referential transparency allows for safe memoization, improving performance by avoiding redundant computations.

Functional Approach (Referentially Transparent)

```typescript
function square(n: number): number {
  return n * n;
}

const result1 = square(4); // Always 16
const result2 = square(4); // Still 16
```

- The function `square` depends solely on its input.
- It has no side effects and does not rely on external state.
- The output is predictable and consistent, making it safe for memoization and substitution.


Imperative Approach (Not Referentially Transparent)

```typescript
let multiplier = 2;

function square(n: number): number {
  return n * multiplier;
}

const result1 = square(4); // 8

multiplier = 3;

const result2 = square(4); // 12
```

- The function `square` depends on a mutable external variable (`multiplier`).
- The same input (`4`) produces different results depending on the state of `multiplier`.
- This makes the function harder to reason about, unsuitable for caching, and introduces potential bugs due to hidden dependencies.

---
### 5. Safer State Management

Immutability ensures that data cannot be altered once created, reducing bugs related to unintended mutations.

**Real-World Scenario:** Managing application state in a Redux store benefits from immutability, as it prevents unintended side effects.

**Functional Approach:**

```typescript
function addItem(items: string[], newItem: string): string[] {
  return [...items, newItem];
}
```

**Imperative Approach:**

```typescript
function addItem(items: string[], newItem: string): void {
  items.push(newItem); // Side effect: modifies original array
}
```

The functional version returns a new array, preserving the original, while the imperative one mutates the original array.

---
### 6. Easier Debugging

With immutability and pure functions, tracking changes becomes straightforward, simplifying debugging.

----
