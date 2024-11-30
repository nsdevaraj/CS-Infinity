



---

### Initial Project Setup
- **Create a Project**:
  - Use Vite to initialize a JavaScript project by running `npm init @vitejs/app`.
  - Select the “vanilla JavaScript” option for a simple, clean setup.
- **Add Jest for Testing**:
  - Install Jest using `npm install jest`, which will look for test files ending with `.test.js`.
- **Set Up the Test Directory**:
  - Create a `test` directory and add a file like `stack.test.js` for our stack tests.
- **Configure Jest to Run Tests**:
  - In `package.json`, add a `test` script to run the Jest command.
  - Enable auto-watching with the `watchAll` flag to rerun tests on file changes.
  - Use the `verbose` flag for detailed terminal output.

---

### Optional Tooling and Pro Tips
- **Enable Type Checking**:
  - Install Jest types using npm and create a `jsconfig.json` file with a Jest-specific configuration.
  - This adds IntelliSense for Jest matchers, helping with auto-completion and error-checking.
- **Wallaby Plugin for VS Code**:
  - Wallaby is a paid VS Code plugin with a free trial, which shows test results directly in the editor, reducing terminal checks.
  - Adds a productivity boost by displaying pass/fail status for tests immediately in the code editor.

---

### Building a Stack Data Structure (Interview Exercise)
- **Define the Test Suite**:
  - Use `describe` to group tests under a shared description, e.g., "Stack" to clarify what is being tested.
  - Inside the `describe` block, use `test` or `it` functions to define individual test cases, both of which function the same way in Jest.
  - Establish a simple test suite with three main requirements:
    1. The stack should start empty.
    2. The stack should allow pushing items to the top.
    3. The stack should allow popping items from the top.

---

### Writing and Running the First Test Case
- **Write the First Test**:
  - Goal: Verify that the stack initializes with a valid empty state.
  - Create an instance of the `Stack` class (which doesn’t yet exist) to represent the stack.
  - Use `expect` to check that the `top` property starts at `-1`, indicating an empty stack.
- **Run the Test for Feedback**:
  - Execute the test, expecting it to fail initially since the `Stack` class isn’t defined.
  - Use the error message as feedback to start implementing the `Stack` class.

---

### Implementing the Stack Class (with TDD)
- **Define the Stack Class**:
  - Create a `Stack` class to address the reference error.
  - Add a `constructor` to initialize it with a `top` value of `-1`.
  - Define an `items` property as an empty object, representing the stack items.
  - Run the test again, and adjust code as needed until the test passes.
- **Additional Assertions**:
  - Check that `items` is an empty object.
  - Switch to using `toEqual` instead of `toBe` for object equality, as `toBe` checks for reference equality, which fails with distinct empty objects.

---

### Writing the Push Test (Second Test Case)
- **Goal**: Verify that an item can be pushed to the stack’s top.
- **Initial Setup**:
  - Initialize a new stack at the start of the test.
  - **Optimize with Jest Hooks**:
    - Use `beforeEach` to set up a new stack before each test, reducing redundancy.
- **Push Implementation**:
  - Call the `push` method and verify:
    - The `top` value is incremented.
    - A `peek` method returns the recently pushed item.
  - Run the test, implement necessary code, and refactor for any optimizations needed to pass the test.

---

### Challenge: Implementing the Pop Method
- **Final Requirement**:
  - Create a test case for a `pop` method, which removes the item from the top.
  - Use TDD principles to write the failing test first, implement the `pop` method, and refactor once it’s passing.

---

### Code Coverage Reporting
- **Add Coverage Report**:
  - In `package.json`, enable the `--coverage` flag in Jest to get a coverage report.
  - Running tests with this flag generates a report indicating the percentage of code covered by tests.
  - **Limitations**: 
    - Code coverage can be misleading; high coverage doesn’t always mean the tests are thorough.
    - Useful for demonstrating test completion to managers or clients, but shouldn’t be the only metric for test quality.

---



