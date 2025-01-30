
### 10. **Advanced Features**

- **Custom Matchers**: If you’re feeling adventurous, you can extend Vitest’s capabilities with custom matchers.
- **Parallel Test Running**: Understand how Vitest runs tests in parallel to optimize performance and speed up your test runs.
- **Testing with Mocked Date/Time**: Explore how Vitest handles global objects like `Date`, `Math`, and `localStorage` using `vi`.


### **Advanced Features in Vitest (Crisp Overview)**

#### **1. Custom Matchers**

Vitest allows you to extend its built-in assertions with **custom matchers**, which can simplify complex or repetitive test scenarios.

- **How to Create Custom Matchers**: You can define your own matcher functions to extend the `expect` API. This is useful when you need specific or domain-specific checks that aren’t covered by the default matchers.
    
    - **Example**:
        
        ```ts
        // customMatchers.ts
        export function toBeEven(received: number) {
          const pass = received % 2 === 0;
          return {
            message: () => `expected ${received} to be even`,
            pass,
          };
        }
        
        // In your test file
        import { toBeEven } from './customMatchers';
        expect.extend({ toBeEven });
        
        test('check if number is even', () => {
          expect(4).toBeEven();
          expect(5).not.toBeEven();
        });
        ```
        
- **Use Case**: If you're testing some custom behavior (e.g., certain conditions in a math function), custom matchers make tests more readable and easier to maintain.
    

#### **2. Parallel Test Running**

Vitest runs tests in **parallel** by default, leveraging multi-core CPUs to speed up the testing process.

- **Performance Boost**: This makes test runs faster, especially in larger projects with many tests, because each test suite or test file is executed concurrently.
    
- **Control Parallelism**:
    
    - You can limit or modify the number of parallel workers to optimize resource usage:
        
        ```bash
        vitest run --maxWorkers 4  # Limit to 4 parallel workers
        ```
        
    - **How It Works**: Each test file or suite runs in its own worker thread, so they don't block each other. This is great for reducing the overall test run time.
        
- **Note**: Some tests (e.g., tests involving global state) may require configuration to run serially. Use `--runInBand` to disable parallelism for certain tests:
    
    ```bash
    vitest run --runInBand  # Run tests serially (one after another)
    ```
    

#### **3. Testing with Mocked Date/Time**

Vitest provides tools to mock global objects like `Date`, `Math`, or `localStorage` to make tests more predictable and control external factors like time and randomness.

- **Mocking Date**: Use `vi.useFakeTimers()` to mock time-related functionality and control `Date`, `setTimeout`, and `setInterval`.
    
    - **Example**:
        
        ```ts
        test('mock Date', () => {
          const mockDate = new Date(2020, 0, 1);  // January 1, 2020
          vi.setSystemTime(mockDate);  // Mock system time to this date
          
          expect(new Date().getFullYear()).toBe(2020);
        });
        ```
        
- **Mocking `Math.random()`**:
    
    - You can mock `Math.random()` to return fixed values, which is helpful for testing random behavior in your code.
    
    ```ts
    test('mock Math.random()', () => {
      vi.spyOn(Math, 'random').mockReturnValue(0.5);  // Always return 0.5
      
      expect(Math.random()).toBe(0.5);  // Test logic that depends on random values
    });
    ```
    
- **Mocking `localStorage`**: Vitest also allows mocking browser-specific objects like `localStorage` for testing web apps:
    
    ```ts
    test('mock localStorage', () => {
      const mockStorage = {};
      global.localStorage = {
        getItem: (key) => mockStorage[key],
        setItem: (key, value) => { mockStorage[key] = value },
      };
    
      localStorage.setItem('key', 'value');
      expect(localStorage.getItem('key')).toBe('value');
    });
    ```
    

### **Key Points**:

- **Custom Matchers**: Extend Vitest’s `expect` with custom matchers for specific tests (e.g., checking even numbers).
- **Parallel Test Running**: Vitest runs tests in parallel by default for faster test execution, with control over the number of workers.
- **Mocking Date/Time**: Use `vi.useFakeTimers()` to mock global objects like `Date`, `Math.random()`, and `localStorage` for predictable and controlled tests.