
## React DOM

• react takes component tree & builds js datastucture called react DOM - light weight in memory representation - each component is basically virtual dom element & everytime changes happen it check with old virtual dom and new virtual dom & find changed nodes and only refresh that in actual dom- these things done by companion library called react-dom( instead of react dom, we can use react native for mobile & desktop app development)  


### What is the Virtual DOM?

The **Virtual DOM (Document Object Model)** is a concept used in modern web development to enhance the performance and efficiency of updating a user interface. It's particularly popular in libraries and frameworks like **React**.


Here’s a breakdown of the Virtual DOM:

#### 1. **Virtual Representation**

- The Virtual DOM is a lightweight, in-memory representation of the actual DOM.
- It’s a plain JavaScript object that mirrors the structure of the real DOM tree.

#### 2. **Purpose**

- The Virtual DOM allows for efficient updates and rendering of the UI by minimizing direct manipulation of the real DOM, which can be slow and expensive in terms of performance.

#### 3. **How It Works**

- **Step 1:** When the state of an application changes (e.g., due to user input or API responses), the Virtual DOM is updated to reflect these changes.
- **Step 2:** The new Virtual DOM is compared to the previous Virtual DOM snapshot using a process called **diffing**.
- **Step 3:** Only the parts of the real DOM that have changed are updated (using minimal operations). This process is called **reconciliation**.

#### 4. **Advantages of Virtual DOM**

- **Improved Performance:** Reduces the number of direct manipulations on the real DOM, making UI updates faster.
- **Predictability:** Changes to the UI are first computed in memory (Virtual DOM) and then applied, reducing errors and side effects.
- **Cross-Browser Compatibility:** Abstracts away browser-specific quirks in DOM updates.

---

### How Virtual DOM Enhances Performance

The real DOM is slow to manipulate because it involves reflowing and repainting the UI. Directly updating it for every change can lead to bottlenecks, especially in complex or dynamic web applications. The Virtual DOM solves this problem by:

- Keeping an in-memory version to compute changes.
- Batch-applying updates to the real DOM instead of doing it one-by-one.

---

### Crisp Virtual DOM Implementation

If you're referring to the **crispness** or **efficiency** of Virtual DOM:

- **Key Techniques:**
    - **Efficient Diffing Algorithms:** Modern frameworks use highly optimized algorithms to quickly compare two versions of the Virtual DOM.
    - **Fiber Architecture:** Frameworks like React use advanced mechanisms (like React Fiber) to manage rendering tasks in chunks, ensuring smoother performance.Its headline feature is incremental rendering: the ability to split rendering work into chunks and spread it out over multiple frames.


This balance of simplicity and power is why Virtual DOM is a fundamental concept in many modern UI frameworks.






# How react work?

- React creates a VIRTUAL DOM in memory.
- Instead of manipulating the browser's DOM directly, React creates a virtual DOM in memory, where it does all the necessary manipulating, before making the changes in the browser DOM.

In **React**, the Virtual DOM underpins the rendering process:

1. React components return a description of the UI structure in JSX.
2. React converts this JSX into a Virtual DOM representation ( objects ).
3. When state or props change, React compares the old and new Virtual DOMs to figure out what has changed.
4. It efficiently updates only the necessary parts of the real DOM.



Extra:
# Config Driven UI
* In a configuration-driven UI, the layout, styles, and other properties of UI elements are defined in a configuration file or database, which can be easily modified without requiring changes to the codebase.
