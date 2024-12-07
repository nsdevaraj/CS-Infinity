

when function is not made as async, but have await keyword inside, what would it do.. 

play with async.. returning promise.. without await, with await but not sync func likewise.. 


play things with string and regex handsOn ...




Event Loop:

https://www.youtube.com/watch?v=8aGhZQkoFbQ

https://www.youtube.com/watch?v=okkHnAo8GmE

https://www.youtube.com/watch?v=Xs1EMmBLpn4&t=19s

https://www.youtube.com/watch?v=eiC58R16hb8&t=150s


async:

https://www.youtube.com/watch?v=Kpn2ajSa92c

https://www.youtube.com/watch?v=vn3tm0quoqE

https://www.youtube.com/watch?v=OFpqvaJ3QYg


https://www.youtube.com/watch?v=PoRJizFvM7s

https://www.youtube.com/watch?v=exBgWAIeIeg

https://www.youtube.com/watch?v=ZYb_ZU8LNxs


https://www.youtube.com/watch?v=RvYYCGs45L4





### The Event Loop - Interview Preparation Topics

1. **Definition and Purpose**
   - Understand what the event loop is and its role in JavaScript's concurrency model.
   - Recognize how it enables non-blocking I/O operations.

2. **Execution Context**
   - Explain the call stack and how it relates to the event loop.
   - Distinguish between synchronous and asynchronous execution.

3. **Web APIs**
   - Describe how web APIs (like `setTimeout`, `fetch`, etc.) interact with the event loop.
   - Understand how callbacks are scheduled in the event loop.

4. **Task Queue vs. Microtask Queue**
   - Differentiate between the task queue (for callbacks) and the microtask queue (for promises).
   - Explain the priority of microtasks over tasks in the event loop.

5. **Event Loop Phases**
   - Break down the phases of the event loop: 
     - **Microtask Queue**: Process microtasks first (promises, mutation observer).
     - **Task Queue**: Process macrotasks (setTimeout, setInterval).
   - Illustrate how the event loop continuously cycles through these phases.

6. **Common Patterns and Examples**
   - Provide code snippets that demonstrate how the event loop works, including:
     - Nested callbacks (callback hell).
     - Using Promises and `async/await`.
     - Set intervals and timeouts.

7. **Implications on Performance**
   - Discuss how the event loop affects performance and responsiveness in web applications.
   - Address potential pitfalls, such as long-running synchronous code blocking the event loop.

8. **Debugging Tools**
   - Identify tools available for analyzing the event loop and asynchronous operations (e.g., Chrome DevTools).
   - Understand how to use the Performance tab to investigate bottlenecks.

9. **Best Practices**
   - Discuss best practices for managing asynchronous code to maintain performance and readability (e.g., avoiding callback hell, using `async/await`).

10. **Real-World Applications**
    - Explain scenarios where the event loop is critical, such as handling user interactions in web applications or server requests in Node.js.



