


Why functional programming sucks:

Functional Programmers are bad marketers!
FP programmer suck at explaining why FP is awesome.

Most people hear:

> “Monads, currying, functors, immutability…”

![[_imgs/Pasted image 20250412063427.png]]


FP focus on complexity and mathematical elegance of FP instead of explaining why its awesome and help others see how useful parts of it can be 

May be let others know that you are also secret Functional bros like monads
We just mostly need to let people know how nice to delete for loops.


Pure FP is awful, since computer itself is totally doing with state..

---

### 🧠 Core Idea: **Functions with No Side Effects**

A **pure function** is predictable:  
Same input → Same output. No state, no surprises.

```js
// Pure
const add = (a, b) => a + b;

// Impure (side effect!)
let count = 0;
const increment = () => ++count;
```



---

Semantics changes - meaning and behavior of the program


Imperative - state is external to code
Object Oriented - state is a part of code
Functional - state does not exist


Imperative :
* what to do step by step
* change variables, use loop to repeat actions and save results
* tells how to do it

Functional:
* describes - what you want 
* pure functions i.e given input always same output, no side effects
* always create new datastructure.. 

why?
most programming bugs:
 * accident change of variables
 * hard to keep track of what modified



But in **functional programming**, you **don’t give commands**. You **describe expressions**, and the program becomes a **composition of functions**.


In FP,
* instructions are not commonds, they are expression.. and program is not a concatenation of declaration and commands, but a composition of function.



![[_imgs/Pasted image 20250414083159.png]]


Language styles:
C - Imperative and procedural
Java, C++, C# - Object oriented ( based imperative)




Things why all modern languages have functional features.. becoz its good..

multiparadigm is good, because each paradigm has its benefits in different contexts.


---

motto: is not to use whole functional, but have functional approach in some part of code to make things awesome


most of the time, we just do take input, do transformation and give output.. 


true => less code, less buggy, but hard to read and debug at first...

---


Everything is so pure..

same input, same output all the time, no state inside to control any of the inner parts..
no input should be changed..


in iterators, we see the whole pass in single track and flow..
but in function, each step dispersed into different function, so hard to track when something goes wrong..

consider you have debugger, then you have to debug each smaller funcs..  so putting into constant for each steps helps very.. 


---

Higher order function:
* take func as input or output or both
* reduce code duplication by abstracting common pattern, code easier to read

```python
def double(x): return x * 2
	numbers = [1, 2, 3]
	doubled = list(map(double, numbers))
	print(doubled)
```


```python
def multiplier(factor):
    return lambda x: x * factor

times_two = multiplier(2)
print(times_two(5))  # 10
```




---



## 🔑 Key Properties of Functional Programming

Let’s break it down into 3 essential properties.

---

### ✅ Property 1: Expressions over Commands

In imperative code, we issue **commands**:

```elixir
# Imperative-like
a = 2
b = 3
result = a * a + b * b
IO.puts(result)
```

In functional code, we prefer **composing expressions**:

```elixir
# Functional
IO.puts(:math.pow(2, 2) + :math.pow(3, 2))
```

Rather than modifying variables, we **compute expressions** from inputs.

---

### 🔄 Property 2: First-Class & Anonymous Functions

In FP, functions are **first-class**: they can be passed around, stored in variables, and even returned from other functions.

#### ✅ Anonymous functions

```elixir
square = fn x -> x * x end
IO.puts(square.(4))  # Outputs 16
```

#### ✅ Functions returning functions

```elixir
defmodule Math do
  def multiplier(factor) do
    fn x -> x * factor end
  end
end

double = Math.multiplier(2)
IO.puts(double.(5))  # Outputs 10
```

This property is essential for creating **flexible and reusable code**.

---

### 🧬 Property 3: Function Composition and Currying

Instead of chaining commands, functional programming builds up computations by **composing functions**.

In Elixir, you can use `|>` to **pipe** output of one function into another:

```elixir
[1, 2, 3]
|> Enum.map(fn x -> x * x end)
|> Enum.sum()
|> IO.puts()
```

This transforms a **list of numbers**, squares them, sums the results, and prints it — **all without variables or commands**.

#### 📦 Currying

Elixir doesn’t support currying natively, but you can simulate it:

```elixir
curried_add = fn a -> fn b -> a + b end end
add_five = curried_add.(5)
IO.puts(add_five.(3))  # Outputs 8
```

Currying lets you partially apply functions and reuse logic.

---


---


### 🔄 Iteration Without Loops

Loops = mutation. Functional style = recursion or higher-order functions.

#### 👎 Traditional Loop

```js
for (let i = 0; i < items.length; i++) {
  console.log(items[i]);
}
```

#### 👍 Functional Style

```js
items.forEach(item => console.log(item));
```


using the mutability of recursion.. call stack.. haha
recursion is fancier form of iteration.. 



avoid using loop using recursion or abstraction



---

### 🔍 Filtering with Clarity

```js
const receipts = [/* ... */];

const userReceipts = receipts.filter(r => r.userId === 'abc123');
```

---

### 🧰 Custom Filter Function

We can build our own `filter` to better understand FP:

```js
const filter = (arr, predicate) => {
  if (arr.length === 0) return [];
  const [head, ...tail] = arr;
  return predicate(head)
    ? [head, ...filter(tail, predicate)]
    : filter(tail, predicate);
};
```

---

### 🧪 Currying – Just Binding Data

Instead of:

```js
const userMatches = (r, id) => r.userId === id;
```

Do this:

```js
const userMatches = id => r => r.userId === id;

const results = receipts.filter(userMatches('abc123'));
```

Now `userMatches('abc123')` creates a **custom function** that remembers the `id`.  
This is _currying_, and yeah — it’s useful.

---

### 🔗 Data Pipelines (aka Why FP Feels Good)

From messy logic:

```js
const result = [];
for (let r of receipts) {
  if (r.total > 10 && r.total < 20) {
    result.push(r.merchant);
  }
}
```

To ✨ **functional clarity**:

```js
const result = receipts
  .filter(r => r.total > 10 && r.total < 20)
  .map(r => r.merchant)
  .slice(0, 5);
```

Readable. Declarative. Easy to maintain.

---

### 🧱 Build Reusable Tools

```js
const take = n => arr => arr.slice(0, n);

const bigTips = receipts
  .filter(r => r.total > 30)
  .map(r => r.merchant)
  .filter(name => name.includes('BBQ'))
  |> take(5);
```

(_Using [pipeline operator](https://github.com/tc39/proposal-pipeline-operator) `|>` in future JS_)

---

### ⚠️ But Let’s Be Real...

Pure FP in the real world is hard:

- No side effects? But we need to log, save, show data.
    
- No mutation? JS is built on mutability.
    

So... **just take the good parts**:

✅ Favor pure functions  
✅ Use `map`, `filter`, `reduce` over loops  
✅ Avoid shared state  
✅ Compose logic cleanly

---

Functional principals useful:

1) Reduce state
2) Make data pipelines
3) Use lambdas for lightweight generic code


---

Here’s a clean, structured **article version** of that video, rewritten in a reader-friendly way with **Elixir examples** to help demonstrate functional programming concepts in action.

---




---

## 🔁 No Loops, Just Recursion

Functional languages don’t rely on `while` or `for` loops. Instead, **recursion** is used.

```elixir
defmodule Recursion do
  def sum([]), do: 0
  def sum([head | tail]), do: head + sum(tail)
end

IO.puts(Recursion.sum([1, 2, 3, 4]))  # Outputs 10
```

Tail recursion can optimize performance and simulate iteration.

---

## 🛠 Functional Constructs in Practice

### 💡 Pure Functions

Pure functions depend **only on their input** and produce **no side effects**.

```elixir
defmodule Pure do
  def add(a, b), do: a + b
end
```

Compare this to impure functions that rely on or modify external state — something we **avoid** in FP.

---

### 🧱 Built-In Functional Tools

Elixir (like most FP languages) gives you higher-order tools like:

#### `Enum.map`

```elixir
Enum.map([1, 2, 3], fn x -> x * 2 end)  # [2, 4, 6]
```

#### `Enum.filter`

```elixir
Enum.filter([1, 2, 3, 4], fn x -> rem(x, 2) == 0 end)  # [2, 4]
```

#### `Enum.reduce`

```elixir
Enum.reduce([1, 2, 3], 0, fn x, acc -> x + acc end)  # 6
```

These replace loops and make logic more **declarative**.

---

## 🧩 Pattern Matching: The Functional Switch

Pattern matching is one of the **most powerful tools** in Elixir and other functional languages:

```elixir
defmodule Matcher do
  def describe({:ok, val}), do: "Success: #{val}"
  def describe({:error, reason}), do: "Error: #{reason}"
end

IO.puts(Matcher.describe({:ok, 42}))
```

Instead of `if` and `switch`, we destructure and match directly in function heads.

---

## 🌀 Functional Programming ≠ No Side Effects

What about printing, errors, and IO?

Yes, functional programming prefers to avoid side effects, but **you can still have them** — they’re just **isolated and controlled**.

Elixir allows side effects like printing using `IO.puts`, logging, etc. But you **separate them** from the rest of your pure logic.

---

## 🧙 Lambda Calculus & Church Origins

The idea of anonymous functions comes from **Lambda Calculus**, introduced by **Alonzo Church**. The `fn ->` syntax in Elixir is inspired by this.

### 📚 Fun Fact: Currying

In Lambda Calculus, every function only takes **one argument**. Multi-arg functions are simulated like this:

```elixir
# f(x, y) = x + y
# becomes:
f = fn x -> fn y -> x + y end end
```

This technique is called **currying**, named after Haskell Curry.

---

## 🚀 Real-World Functional Use Cases

Functional programming is great for:

- Distributed systems (Elixir/Erlang are built for this)
    
- Concurrent apps (immutable state = safe parallelism)
    
- Financial systems (predictability)
    
- Compilers and interpreters
    
- Mathematical computing
    
- Web servers (Phoenix/Elixir)
    

---

## 🔚 Final Thoughts

Functional programming encourages you to:

- Think in terms of **what** to do, not how
    
- Use **expressions**, not commands
    
- Embrace **functions as values**
    
- Avoid mutable state
    
- Build **modular, reusable code**
    

Languages like Elixir, Haskell, OCaml, and Scala are designed with FP in mind, but you can apply FP concepts in Python, JavaScript, and even Java (if you're brave enough 😄).

---

Absolutely, here's a polished and presentation-ready **Markdown summary** of **Functional Programming (FP)** — complete with clear explanations and **TypeScript examples** to demonstrate key concepts. This will help you break down the core ideas for your audience in an engaging and informative way.

---

# 📘 Functional Programming: A Summary with TypeScript Examples

## 🔍 What is Functional Programming?

Functional Programming (FP) is a paradigm where programs are constructed by applying and composing **pure functions**. It avoids shared state, mutable data, and side effects.

> "Functional programming is a mindset—a way of thinking about problems using transformations and function composition rather than step-by-step instructions."

---

## 🧱 Core Principles

### 1. ✅ Pure Functions

- Same input → same output.
    
- No side effects (e.g., no logging, no mutation).
    

```ts
// Pure function example
const square = (x: number): number => x * x;
console.log(square(4)); // 16
```

---

### 2. 🚫 No Side Effects

- Side effects are isolated or eliminated.
    
- Helps with predictability and testability.
    

```ts
// Impure
let count = 0;
const increment = () => count++; // side effect: mutates external state

// Pure version
const incrementPure = (x: number): number => x + 1;
```

---

### 3. 🔒 Immutability

- Data is not changed once created.
    
- Leads to safer and more predictable code.
    

```ts
const original = [1, 2, 3];
const added = [...original, 4]; // new array, original untouched
```

---

### 4. 🔁 Recursion Over Loops

- No `for` or `while`; use recursive calls.
    

```ts
// Recursive factorial
const factorial = (n: number): number =>
  n === 0 ? 1 : n * factorial(n - 1);

console.log(factorial(5)); // 120
```

---

### 5. 🧠 Higher-Order Functions

- Functions that take or return other functions.
    

```ts
const greet = (name: string): string => `Hello, ${name}`;
const excited = (fn: (s: string) => string) => (name: string) =>
  fn(name).toUpperCase() + '!!!';

const excitedGreet = excited(greet);
console.log(excitedGreet('Alice')); // HELLO, ALICE!!!
```

---

## 🛠️ Key Functional Tools in TypeScript

### map, filter, reduce

```ts
const nums = [1, 2, 3, 4, 5];

const squared = nums.map(x => x * x);       // [1, 4, 9, 16, 25]
const evens = nums.filter(x => x % 2 === 0); // [2, 4]
const sum = nums.reduce((acc, x) => acc + x, 0); // 15
```

---

### 🧩 Function Composition

```ts
const add = (x: number) => x + 2;
const multiply = (x: number) => x * 3;

const compose = <T>(...fns: Array<(x: T) => T>) => (x: T): T =>
  fns.reduceRight((v, f) => f(v), x);

const addThenMultiply = compose(multiply, add);
console.log(addThenMultiply(2)); // (2 + 2) * 3 = 12
```

---

## 🌀 Closures & Currying

```ts
const makeMultiplier = (factor: number) => (x: number) => x * factor;
const double = makeMultiplier(2);
console.log(double(5)); // 10

// Currying
const addCurried = (a: number) => (b: number) => a + b;
console.log(addCurried(2)(3)); // 5
```

---

## 🧭 Declarative vs Imperative

|Style|Focus|Example|
|---|---|---|
|Imperative|How|Loop to filter items manually|
|Declarative|What|Use `filter`, `map` functions|

```ts
// Imperative
const result: number[] = [];
for (const n of nums) {
  if (n > 2) result.push(n);
}

// Declarative
const result2 = nums.filter(n => n > 2);
```

---

## ⚖️ Pros and Cons

### ✅ Advantages

- Predictable, testable code
    
- Easy to reason about
    
- Encourages modular, reusable functions
    
- Great for concurrency and async tasks
    

### ❗ Challenges

- Learning curve (especially recursion)
    
- Pure FP can be restrictive
    
- Performance considerations in recursion-heavy solutions
    

> "Pure functional programming... is still mostly academic. Real-world apps need a pragmatic, hybrid approach." — _Dear Functional Bros_

---

## 🔚 Summary

Functional programming isn't about dogma—it's a **mindset** and a set of **tools**. Embracing its principles in a multi-paradigm language (like TypeScript) helps you write **cleaner**, **safer**, and more **maintainable** code.

---
Here is some crisp content for your Functional Programming presentation:

**Introduction to Functional Programming**

- Functional Programming (FP) is a programming paradigm that treats computation as the evaluation of **mathematical functions**.
- It emphasizes **pure functions**, which, for the same input, always return the same output and have **no side effects**. This means they don't modify anything outside of their scope, like global variables or the input itself.
- FP discourages **mutable data (state that can change)** and reliance on **global state**. Instead, when a value needs to change, a new value is created.
- It's often described as a **declarative** style of programming, focusing on _what_ the program should do rather than explicitly specifying _how_ to do it step-by-step (as in **imperative/procedural** programming).

**Key Concepts in Functional Programming**

- **Pure Functions:**
    - Given the same input, they always return the same output.
    - They have no **side effects** (no mutation, no I/O, etc.).
    - Easier to reason about and test.
- **Immutability:**
    - Once data is created, it cannot be changed.
    - All operations that seem to modify data instead return a new copy with the changes.
    - Helps prevent unexpected changes and simplifies debugging, especially in concurrent environments.
- **Higher-Order Functions:**
    - Functions that can take other functions as arguments or return functions as their results.
    - Enable powerful abstractions and code reuse (e.g., `map`, `filter`, `reduce`).
- **Function Composition:**
    - Combining simple functions to build more complex ones by chaining the output of one function as the input of the next.
    - Facilitates building clear **data pipelines**.
- **Recursion:**
    - In purely functional languages, iteration (loops) is often replaced by recursion, where a function calls itself. This is done without mutating loop variables.
- **Currying:**
    - A technique of transforming a function that takes multiple arguments into a sequence of functions that each take a single argument.
- **Anonymous Functions (Lambdas):**
    - Functions defined without a specific name, often used as arguments to higher-order functions.

**Benefits of Functional Programming**

- **Reduced Side Effects:** Makes code easier to understand, debug, and maintain.
- **Increased Predictability:** Pure functions are deterministic; the same input always yields the same output.
- **Improved Testability:** Testing pure functions is straightforward as you only need to check input-output relationships.
- **Enhanced Concurrency:** Immutability eliminates many common concurrency issues like race conditions, as data cannot be modified by multiple threads simultaneously. Pure functions are inherently thread-safe.
- **More Declarative Style:** Focus on _what_ needs to be done, leading to more readable and concise code.
- **Better Code Reusability:** Higher-order functions and function composition promote the creation of reusable and modular code.
- **Effective Data Processing:** Functional paradigms are well-suited for transforming, filtering, and mapping data.

**FP in Relation to Other Paradigms**

- **Procedural/Imperative Programming:** Focuses on a sequence of commands that modify the program's state. FP takes a more declarative approach.
- **Object-Oriented Programming (OOP):** Organizes code around objects that encapsulate data (state) and methods (behavior). While OOP manages state within objects, FP aims to minimize state and side effects. Many modern languages support **multi-paradigm programming**, allowing you to combine aspects of FP and OOP.

**Bringing it to Your Work**

- Consider incorporating functional principles like writing pure functions and using immutable data structures where it makes sense in your current projects.
- Explore using higher-order functions available in your language for data manipulation tasks.
- Understand that adopting FP is often a spectrum, and integrating some of its best practices can lead to more robust and maintainable code.

By understanding these core concepts and benefits, your team can start to appreciate the value and principles of Functional Programming.





