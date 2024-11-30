

### Section 2: Jest Mocking and Advanced Testing Concepts

**1. Mock Functions**
   - **Purpose**: Mocking in Jest is used to test functions in isolation by simulating dependencies, allowing you to test code without relying on external resources or complicated setups.
   - **Creating Mocks**: Use `jest.fn()` to create a mock function.
     ```js
     const mockFunction = jest.fn();
     mockFunction.mockReturnValue(10);
     expect(mockFunction()).toBe(10);
     ```
   - **Custom Implementation**: Use `.mockImplementation()` to provide custom behavior for mock functions.
     ```js
     mockFunction.mockImplementation(() => "Hello World");
     ```

**2. Mocking Modules**
   - **Automatic Mocking**: Use `jest.mock("moduleName")` to automatically mock a module. This is useful for external modules like `axios` or `fs`.
     ```js
     jest.mock("axios");
     axios.get.mockResolvedValue({ data: "response data" });
     ```
   - **Manual Mocking**: Create a manual mock in a `__mocks__` directory for more control over module behavior during testing.

**3. Mocking Timers**
   - **Fake Timers**: Use `jest.useFakeTimers()` to control time-related functions like `setTimeout` or `setInterval`.
     ```js
     jest.useFakeTimers();
     setTimeout(() => console.log("Hello"), 1000);
     jest.advanceTimersByTime(1000); // Moves the clock forward
     ```

**4. Snapshot Testing**
   - **Purpose**: Snapshot tests capture the rendered output of a component or function. When the code runs, Jest compares the current output to a stored "snapshot".
   - **Usage**: Ideal for UI components where visual consistency is important.
     ```js
     test("renders correctly", () => {
       const component = renderer.create(<MyComponent />);
       let tree = component.toJSON();
       expect(tree).toMatchSnapshot();
     });
     ```
   - **Updating Snapshots**: If the UI changes intentionally, you can update the snapshot by running Jest with the `-u` flag (`jest -u`).

**5. Mocking API Calls**
   - **Mocking External API Calls**: For functions that make API requests, mock the API response to test how your code handles it without actually hitting the network.
   - **Example**: Using `jest.spyOn()` and `mockResolvedValue()` to mock an API call.
     ```js
     const apiCallSpy = jest.spyOn(apiModule, "fetchData");
     apiCallSpy.mockResolvedValue({ data: "Mocked Data" });
     ```

**6. Asynchronous Testing**
   - **Purpose**: Jest provides ways to test asynchronous code using promises or async/await syntax.
   - **Handling Promises**: Use `.resolves` or `.rejects` to test promises.
     ```js
     test("fetches data", async () => {
       await expect(fetchData()).resolves.toEqual({ data: "some data" });
     });
     ```
   - **Using async/await**: Write tests as `async` functions and `await` the result for cleaner async handling.
     ```js
     test("fetches data", async () => {
       const data = await fetchData();
       expect(data).toEqual({ data: "some data" });
     });
     ```
 