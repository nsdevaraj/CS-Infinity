

### Synchronous vs. Asynchronous Functions


- **Synchronous**: `Tasks are executed one at a time in a sequence.` Each task waits for the previous one to finish before starting.
    
    - Example: Reading a file line-by-line in a blocking way.
- **Asynchronous**: `Tasks can start and execute independently of each other`. A task doesn’t block the execution of others; instead, it signals (via callbacks, Promises, or events) when it’s done.
    
    - Example: Fetching data from an API while other code continues running.

### Key Difference:

- **Synchronous**: Blocks further execution until the task completes.
- **Asynchronous**: Doesn’t block; lets other tasks run and resumes the task when it’s ready.

**Synchronous Functions**:
- These functions execute sequentially, blocking the execution of the code until the current function completes. The next line of code will not run until the synchronous function has finished.
- Execute line-by-line; block further execution until complete.
- **Example**:
  ```javascript
  function syncFunction() {
      console.log("Start");
      // Simulate a time-consuming task
      for (let i = 0; i < 1e9; i++) {}
      console.log("End");
  }
  syncFunction();
  console.log("This runs after syncFunction.");


	// => Start, End, This run after syncFunction

  ```




**Asynchronous Functions**:
- **Definition**: These functions allow other code to run while they execute in the background. They do not block the main thread, enabling non-blocking behavior.
-  Execute tasks in the background without blocking the main thread.
- **Example**:
  ```javascript
  function asyncFunction() {
      console.log("Start");
      setTimeout(() => {
          console.log("End");
      }, 1000);
  }
  asyncFunction();
  console.log("This runs before End.");
	// => Start, This runs before End, End
  ```


- js is single threaded asynchronous ... 


