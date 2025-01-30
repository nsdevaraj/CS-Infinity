
### 4. **Asynchronous Testing**

- **Promises & async/await**: Get comfortable testing asynchronous code with `async/await` and `expect`’s `.resolves` or `.rejects`.
- **Timers and Delays**: Learn how to test code that uses timers (`setTimeout`, `setInterval`) and promises that resolve after delays using `vi.useFakeTimers()`.


### 1. **Testing Promises & `async/await`**

- **`async/await`**: You can use `async/await` to handle async code in tests. `expect().resolves` and `expect().rejects` are used for promises.
    
- **Using `async/await`**:
    
    ```js
    test('async function resolves', async () => {
      const result = await someAsyncFunction();
      expect(result).toBe('success');
    });
    ```
    
- **Using `expect().resolves`**: For testing promises that resolve.
    
    ```js
    test('promise resolves', () => {
      return expect(someAsyncFunction()).resolves.toBe('success');
    });
    ```
    
- **Using `expect().rejects`**: For testing promises that reject.
    
    ```js
    test('promise rejects', () => {
      return expect(someAsyncFunction()).rejects.toThrow('error');
    });
    ```
    

### 2. **Testing Timers and Delays**

- **`vi.useFakeTimers()`**: Enables fake timers for testing `setTimeout`, `setInterval`, or delayed promises without actually waiting.
    
- **Simulating Delays**:
    
    ```js
    vi.useFakeTimers();
    test('delayed function call', () => {
      const mockFn = vi.fn();
      setTimeout(mockFn, 1000); // Delayed by 1 second
      vi.advanceTimersByTime(1000); // Fast-forward timers
      expect(mockFn).toHaveBeenCalled();
    });
    ```
    
- **Testing Timed Promises**:
    
    ```js
    vi.useFakeTimers();
    test('delayed promise resolves', async () => {
      const promise = new Promise(resolve => setTimeout(() => resolve('done'), 1000));
      vi.advanceTimersByTime(1000); // Fast-forward 1 second
      await expect(promise).resolves.toBe('done');
    });
    ```
    
- **`vi.runAllTimers()`**: Runs all pending timers at once.
    
    ```js
    vi.useFakeTimers();
    setTimeout(() => { /* some logic */ }, 1000);
    vi.runAllTimers(); // Runs all timers
    ```
    
- **Restoring Real Timers**:
    
    ```js
    vi.useRealTimers(); // Restores the real timers after fake timers are used
    ```
    

### Key Points:

- **Promises**: Use `async/await` or `expect().resolves`/`expect().rejects` for testing async code.
- **Timers**: Use `vi.useFakeTimers()` to simulate `setTimeout`, `setInterval`, and delay-based promises without actual waiting.
- **Fast-forwarding**: With `vi.advanceTimersByTime()` and `vi.runAllTimers()`, you can quickly run through delayed logic in your tests.

