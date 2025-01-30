
### 3. **Mocking and Spying**

- **Mocking Functions**: Learn how to mock functions using `vi.fn()` to spy on them or replace their behavior.
- **Mocking Modules**: Understand how to mock entire modules with `vi.mock()`, including for things like API calls or external libraries.



### 1. **Mocking Functions with `vi.fn()`**

- **`vi.fn()`** creates a mock function, which you can use to spy on calls, track arguments, or replace real behavior.
    
- **Basic Example**:
    
    ```js
    const mockFn = vi.fn();
    mockFn(1, 2);
    expect(mockFn).toHaveBeenCalledWith(1, 2); // Verify call
    ```
    
- **Mocking Return Values**:
    
    ```js
    const mockFn = vi.fn().mockReturnValue(42);
    expect(mockFn()).toBe(42); // Will return 42
    ```
    
- **Mocking Implementation**:
    
    ```js
    const mockFn = vi.fn().mockImplementation((a, b) => a + b);
    expect(mockFn(2, 3)).toBe(5); // Adds the arguments
    ```
    
- **Tracking Call Count**:
    
    ```js
    const mockFn = vi.fn();
    mockFn();
    expect(mockFn).toHaveBeenCalledTimes(1);
    ```
    
- **Spying on Calls**:
    
    ```js
    const spy = vi.fn();
    spy();
    expect(spy).toHaveBeenCalled();
    ```
    

### 2. **Mocking Modules with `vi.mock()`**

- **`vi.mock()`** allows you to replace entire modules (e.g., API calls, libraries) with mock versions.
    
- **Basic Mocking**:
    
    ```js
    vi.mock('./myModule', () => ({
      myFunction: vi.fn().mockReturnValue('Mocked Value')
    }));
    
    import { myFunction } from './myModule';
    test('should mock myFunction', () => {
      expect(myFunction()).toBe('Mocked Value');
    });
    ```
    
- **Mocking Node Modules**:
    
    ```js
    vi.mock('axios', () => ({
      get: vi.fn().mockResolvedValue({ data: 'Mocked Response' })
    }));
    ```
    
- **Restore Original Module**:
    
    ```js
    vi.unmock('axios'); // Reverts mocking of the module
    ```
    

### Key Points:

- **`vi.fn()`** is used for creating mock functions and tracking their behavior.
- **`vi.mock()`** is used to replace whole modules, typically to mock external libraries or APIs.