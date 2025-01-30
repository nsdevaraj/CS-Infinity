
### 2. **Writing Tests**

- **Test Functions**: Know how to use `test()`, `it()`, and `describe()` to structure your tests.
- **Assertions**: Learn the core assertions like `expect()`, `toBe()`, `toEqual()`, `toContain()`, `toHaveBeenCalled()`, etc.
- **Test Setup and Teardown**: Explore `beforeAll()`, `beforeEach()`, `afterAll()`, and `afterEach()` for setup and cleanup.


### 1. **Test Functions**

- `test()` or `it()` – These are used to define a single test case.
    
    ```js
    test('adds numbers', () => {
      expect(1 + 1).toBe(2);
    });
    ```
    
    Both `test()` and `it()` are interchangeable, but `test()` is more common.
    
- `describe()` – Groups related test cases together. Helps with test organization.
    
    ```js
    describe('Math operations', () => {
      test('adds numbers', () => { expect(1 + 1).toBe(2); });
      test('subtracts numbers', () => { expect(2 - 1).toBe(1); });
    });
    ```
    

### 2. **Assertions**

- `expect()` – Used to create an expectation.
- `toBe()` – Strict equality (compares values and types).
    
    ```js
    expect(2 + 2).toBe(4); // Checks value strictly equals 4
    ```
    
- `toEqual()` – Deep equality (checks equality of objects/arrays).
    
    ```js
    expect([1, 2]).toEqual([1, 2]); // Checks deep equality
    ```
    
- `toContain()` – Checks if an array or string contains a value.
    
    ```js
    expect([1, 2, 3]).toContain(2);
    ```
    
- `toHaveBeenCalled()` – Checks if a function was called.
    
    ```js
    const mockFn = vi.fn();
    mockFn();
    expect(mockFn).toHaveBeenCalled();
    ```
    

### 3. **Test Setup & Teardown**

- `beforeAll()` – Runs before any tests in a suite.
    
- `beforeEach()` – Runs before each individual test.
    
- `afterAll()` – Runs after all tests in a suite.
    
- `afterEach()` – Runs after each individual test.
    
    ```js
    beforeAll(() => {
      // Setup before any tests run
    });
    
    afterEach(() => {
      // Cleanup after each test
    });
    ```
    

