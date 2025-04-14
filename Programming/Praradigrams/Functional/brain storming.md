


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

## 💬 Got Questions?

Let me know if you'd like this turned into slides, a blog post, or visual illustrations for each section!

---
