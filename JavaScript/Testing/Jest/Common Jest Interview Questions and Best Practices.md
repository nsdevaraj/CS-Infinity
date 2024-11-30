

### Section 3: Common Jest Interview Questions and Best Practices

**1. Common Jest Interview Questions**

   - **Explain the difference between `toBe` and `toEqual`.**
     - `toBe` checks for strict equality (similar to `===`), suitable for primitive values like strings or numbers.
     - `toEqual` is used for deep equality checks, which means it compares the structure and content, making it useful for objects and arrays.

   - **What are Jest spies, and how do they differ from mocks?**
     - Spies are used to track calls to a function and the arguments passed without altering its implementation.
     - Mocks replace a function’s implementation, allowing you to simulate behavior for testing. Spies are often created using `jest.spyOn()`, while mocks use `jest.fn()` or `jest.mock()`.

   - **How does snapshot testing work, and when should you use it?**
     - Snapshot testing captures a "snapshot" of the component’s output (e.g., HTML structure). When re-run, Jest compares the current output to the saved snapshot, flagging differences as potential issues.
     - Use snapshot testing for components or UI elements with stable, predictable outputs. Avoid it for frequently changing elements or dynamic content.

   - **How do you mock an ES6 module in Jest?**
     - Import the module you want to mock, then call `jest.mock("moduleName")` at the top of your file. Alternatively, create a manual mock in a `__mocks__` directory.

**2. Best Practices for Writing Jest Tests**

   - **Keep Tests Isolated**: Each test should be independent of others to avoid unintended interactions and flaky tests.
   - **Use Descriptive Test Names**: Clear and descriptive names help identify the purpose and functionality being tested.
   - **Mock Dependencies, Not Implementations**: Focus on mocking external dependencies (e.g., database or API calls) rather than the actual implementation details, allowing tests to focus on the function’s behavior.
   - **Use Lifecycle Hooks Wisely**: Only use `beforeAll`, `afterAll`, `beforeEach`, and `afterEach` when setup and teardown are necessary. Overusing these can complicate test maintenance.
   - **Avoid Testing Implementation Details**: Test the behavior and outcomes of code, not the specific steps within the function. This ensures tests are resilient to internal refactoring.

**3. Performance and Debugging Tips**

   - **Run Only Specific Tests**: Use `.only` to run a single test or suite during debugging.
     ```js
     test.only("this is the only test that will run", () => { /* test code */ });
     ```
   - **Use Watch Mode for Efficiency**: Running Jest in watch mode (`jest --watch`) automatically reruns tests when files change, speeding up the development process.
   - **Leverage Coverage Reports**: Jest’s `--coverage` flag generates reports on tested versus untested code, helping you identify gaps in test coverage.
   - **Use `--runInBand` for Debugging Parallelism Issues**: Running Jest with the `--runInBand` flag can reveal issues caused by parallel test execution, which can be especially helpful for troubleshooting flaky tests.