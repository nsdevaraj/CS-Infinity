

### **Test Functions**

- **`test()`** / **`it()`** – Defines a test case.
    
    ```js
    test('should return true', () => {
      expect(true).toBe(true);
    });
    ```
    
- **`describe()`** – Groups tests together into a suite.
    
    ```js
    describe('Math tests', () => {
      test('should add numbers', () => { expect(1 + 1).toBe(2); });
    });
    ```
    

### **Assertions**

- **`expect()`** – Used to create assertions.
    
    ```js
    expect(1 + 1).toBe(2);
    ```
    
- **`toBe()`** – Strict equality check (checks both value and type).
    
    ```js
    expect(1 + 1).toBe(2);
    ```
    
- **`toEqual()`** – Deep equality check (works for arrays/objects).
    
    ```js
    expect({ a: 1 }).toEqual({ a: 1 });
    ```
    
- **`toBeTruthy()`** / **`toBeFalsy()`** – Checks if a value is truthy or falsy.
    
    ```js
    expect(1).toBeTruthy();
    expect(0).toBeFalsy();
    ```
    
- **`toBeGreaterThan()`**, **`toBeLessThan()`**, etc. – For numerical comparisons.
    
    ```js
    expect(3).toBeGreaterThan(2);
    ```
    
- **`toContain()`** – Checks if an array or string contains a specific value.
    
    ```js
    expect([1, 2, 3]).toContain(2);
    ```
    
- **`toHaveLength()`** – Checks the length of arrays/strings.
    
    ```js
    expect([1, 2, 3]).toHaveLength(3);
    ```
    
- **`toHaveBeenCalled()`** – Verifies if a mock function has been called.
    
    ```js
    const mockFn = vi.fn();
    mockFn();
    expect(mockFn).toHaveBeenCalled();
    ```
    
- **`toHaveBeenCalledTimes()`** – Verifies how many times a mock function was called.
    
    ```js
    expect(mockFn).toHaveBeenCalledTimes(1);
    ```
    
- **`toHaveBeenCalledWith()`** – Verifies if a mock function was called with specific arguments.
    
    ```js
    expect(mockFn).toHaveBeenCalledWith(2);
    ```
    

### **Setup & Teardown**

- **`beforeAll()`** – Runs before all tests in the suite.
    
    ```js
    beforeAll(() => { /* setup logic */ });
    ```
    
- **`beforeEach()`** – Runs before each test in the suite.
    
    ```js
    beforeEach(() => { /* setup logic */ });
    ```
    
- **`afterAll()`** – Runs after all tests in the suite.
    
    ```js
    afterAll(() => { /* teardown logic */ });
    ```
    
- **`afterEach()`** – Runs after each test in the suite.
    
    ```js
    afterEach(() => { /* cleanup logic */ });
    ```
    

### **Mocking and Spying**

- **`vi.fn()`** – Creates a mock function.
    
    ```js
    const mockFn = vi.fn();
    mockFn('hello');
    expect(mockFn).toHaveBeenCalledWith('hello');
    ```
    
- **`vi.spyOn()`** – Creates a spy for an existing method.
    
    ```js
    const obj = { greet: () => 'Hello' };
    const spy = vi.spyOn(obj, 'greet');
    obj.greet();
    expect(spy).toHaveBeenCalled();
    ```
    

### **Timers**

- **`vi.useFakeTimers()`** – Enables fake timers (useful for testing time-related code like `setTimeout`).
    
    ```js
    vi.useFakeTimers();
    setTimeout(() => { /* code */ }, 1000);
    vi.advanceTimersByTime(1000);
    ```
    
- **`vi.runAllTimers()`** – Runs all timers (like `setTimeout`, `setInterval`).
    
    ```js
    vi.runAllTimers();
    ```
    
- **`vi.clearAllTimers()`** – Clears all fake timers.
    
    ```js
    vi.clearAllTimers();
    ```
    

### **Asynchronous Testing**

- **`await`** – Used for async code testing.
    
    ```js
    test('async test', async () => {
      const result = await someAsyncFunction();
      expect(result).toBe(true);
    });
    ```
    
- **`done()`** – Callback to signal the completion of an asynchronous test.
    
    ```js
    test('async with done()', (done) => {
      setTimeout(() => {
        expect(true).toBe(true);
        done();
      }, 100);
    });
    ```
    

### **Other Useful Helpers**

- **`vi.mock()`** – Mocking modules.
    
    ```js
    vi.mock('./myModule', () => ({
      myFunction: vi.fn().mockReturnValue(42),
    }));
    ```
    
- **`vi.unmock()`** – Unmocks a module.
    
    ```js
    vi.unmock('./myModule');
    ```
    
- **`expect.assertions()`** – Ensures a certain number of assertions are called.
    
    ```js
    test('ensure multiple assertions', () => {
      expect.assertions(2);
      expect(1).toBe(1);
      expect(2).toBe(2);
    });
    ```
    
- **`expect.hasAssertions()`** – Checks that at least one assertion is called.
    
    ```js
    test('check assertions', () => {
      expect.hasAssertions();
      expect(true).toBe(true);
    });
    ```
    



