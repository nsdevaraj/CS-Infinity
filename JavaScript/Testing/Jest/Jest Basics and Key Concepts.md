


### Section 1: Jest Basics and Key Concepts

**1. What is Jest?**
   - Jest is a JavaScript testing framework developed by Facebook, commonly used for testing React applications. 
   - It is fast, easy to set up, and integrates well with CI/CD pipelines.
   - It supports testing frameworks like unit tests, integration tests, and snapshot tests.

**2. Key Jest Features**
   - **Zero Configuration**: Works out of the box without much setup.
   - **Mocks and Spies**: Allows mocking functions, modules, and timers.
   - **Snapshot Testing**: Useful for UI testing; captures snapshots of components and compares against stored versions.
   - **Parallel Testing**: Runs tests in parallel, improving speed and efficiency.

**3. Commonly Used Jest Methods**

   - **describe()**: Organizes tests into sections; helpful for grouping related tests.
     ```js
     describe("Math functions", () => { /* tests go here */ });
     ```

   - **test() / it()**: Defines individual tests. `test()` and `it()` are aliases and can be used interchangeably.
     ```js
     test("adds numbers", () => { expect(add(2, 3)).toBe(5); });
     ```

   - **expect()**: Sets expectations for test values. Various matchers can be used within `expect()`:
     - `.toBe(value)`: Checks for strict equality.
     - `.toEqual(value)`: Checks for deep equality (useful for objects and arrays).
     - `.toBeTruthy()`, `.toBeFalsy()`: Checks for truthy/falsy values.
     - `.toContain(item)`: Verifies if an array or string contains an item.

**4. Test Lifecycle Hooks**
   - **beforeAll()** / **afterAll()**: Runs once before/after all tests in a `describe` block.
   - **beforeEach()** / **afterEach()**: Runs before/after each individual test.

