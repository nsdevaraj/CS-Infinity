
_**Premise**_

`“Any application that can be written in JavaScript, will eventually be written in JavaScript.” -Jeff Atwood`                                 

This was said back in 2007, and we can say that it is proving true till now. You can think of any technical keyword and there might be a JavaScript library build around it. So if it’s so popular and in demand, this can be a great programming language to learn. But that’s not the only skill that is required, since you have to apply this to solve practical problems. And one of such problems is to build scalable products.

**Gen Z backend**  
  
After jQuery animation dev shifted to a single page application for better control of ui/ux and thus came frontend frameworks such as angular js and angular. After that JavaScript was made available to port into literally any modern machine that exists and runs as a standalone application i.e Node.js. It was widely accepted as a backend framework and comes to the top, 2nd year in a row in 2020 of StackOverflow survey.



### comparison between client-side and server-side:

| **Aspect**                | **Client-Side**                              | **Server-Side**                              |
| ------------------------- | -------------------------------------------- | -------------------------------------------- |
| **Definition**            | Code executed on the user's device (browser) | Code executed on the web server              |
| **Primary Languages**     | HTML, CSS, JavaScript                        | PHP, Python, Ruby, Java, .NET                |
| **Purpose**               | Handles UI and user interactions             | Manages business logic, database, security   |
| **Execution Environment** | Browser (user's device)                      | Server (remote machine)                      |
| **Response Time**         | Faster (no need to contact server)           | Slightly slower (requires server response)   |
| **Security**              | Less secure (code is visible to user)        | More secure (code is hidden from user)       |
| **Examples**              | Form validation, animations, dynamic pages   | Database queries, authentication, file I/O   |
| **Data Storage**          | Uses browser storage (cookies, localStorage) | Uses server-side databases                   |
| **Scalability**           | Limited by user’s device capability          | Scalable with powerful server infrastructure |
|                           |                                              |                                              |

### **Client-Side**
   - **Primary Tasks**: Handles UI rendering, user interactions, form validation, and making requests to the server.
   - **Examples**: Loading a webpage, displaying dynamic content, validating form inputs before submission.
   - **Performance**: Dependent on the user’s device and browser.
   - Document , window, navigator and event objects - are available on client side only

### **Server-Side**
   - **Primary Tasks**: Manages database operations, processes client requests, enforces business logic, and sends data to the client.
   - **Examples**: Authenticating users, querying a database, processing data, generating dynamic web pages.
   - **Performance**: Dependent on server resources, scalability, and network latency.
   - Request, response, server, database objects are available on server side only

### **Summary**
   - **Client-Side** is user-facing, handling visual aspects and interactions in the browser, while **Server-Side** manages data, business logic, and backend processes on the server.


### Single vs Multi threaded programming

| Feature                 | **Single-Threaded Programming**                                    | **Multi-Threaded Programming**                                    |
|-------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------|
| **Definition**          | Executes one task at a time within a single thread                 | Executes multiple tasks concurrently using multiple threads        |
| **Concurrency**         | Limited, handles tasks sequentially                                | High, enables parallel execution of tasks                          |
| **Complexity**          | Easier to write and debug                                         | More complex due to thread management and synchronization          |
| **Use Case**            | Suitable for simple applications with lightweight operations       | Ideal for CPU-intensive or high-performance applications           |
| **Resource Usage**      | Uses less memory and CPU, as only one thread is active             | Can use more memory and CPU due to multiple active threads         |
| **Examples**            | JavaScript (Node.js is single-threaded for event loop)             | Java, C++, Python (supports multi-threaded programming)            |

### **Summary**
   - **Single-threaded** is simpler and sequential, ideal for tasks not requiring concurrency.
   - **Multi-threaded** allows parallelism, best for complex or performance-intensive applications needing concurrent task handling.



### comparison between synchronous and asynchronous programming:


| Feature                 | **Synchronous Programming**                                   | **Asynchronous Programming**                                   |
|-------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| **Execution**           | Tasks are executed sequentially, one after the other          | Tasks can start without waiting for previous tasks to complete |
| **Blocking**            | Blocks further execution until the current task completes     | Non-blocking; other tasks can proceed in parallel              |
| **Performance**         | Slower for I/O-bound tasks, as each task waits for the previous | Faster, as tasks don’t wait and can be processed in the background |
| **Use Case**            | Suitable for small tasks, or when order of operations is crucial | Ideal for I/O operations, network requests, and concurrent tasks |
| **Examples**            | Reading a file synchronously in Node.js with `fs.readFileSync` | Reading a file asynchronously with `fs.readFile` in Node.js   |

### **Summary**
   - **Synchronous** programming is sequential and blocks execution, suitable for simple or order-sensitive tasks.
   - **Asynchronous** programming is non-blocking, efficient for I/O-bound operations, and allows concurrency.


In Nodejs, async flow is achieved by its single threaded, non blocking and event driven architecture...

* In Node.js if there are 3 Tasks ( Task1, Task2, Task3) to be completed for an event, then below steps will be executed.
1) Thread T1 will be created
2) T1 intiates Task1, but won't wait for the completion of T1, instread proceed to intiate to Task2 and then Task3, this async allows T1 to efficiently handle multiple tasks concurrently.
3) Whenever Task1 completes, an even is emited
4) Thread T1 being event-driver, promptly responds to this event, interrupting its current tasks and delivering the result of Task1








