


[5 types of testing](https://www.youtube.com/watch?v=YaXJeUkBe4Y)



Pyramid of testing:

| **Level**            | **Description**                                                   | **Purpose**                                              | **Examples/Tools**                |
|----------------------|-------------------------------------------------------------------|----------------------------------------------------------|------------------------------------|
| **Unit Tests**       | Small, isolated tests that check individual functions or modules. | Ensure code logic works as expected.                     | Jest, Mocha, Jasmine               |
| **Component Tests**  | Tests that focus on individual UI components in isolation.       | Ensure that UI components render and behave correctly.   | React Testing Library, Enzyme, Jest |
| **Integration Tests**| Tests that check the interaction between different modules or components. | Validate combined units work together correctly.         | Supertest, Chai, Testing Library   |
| **End-to-End (E2E) Tests** | Tests that simulate user interactions and check the full workflow. | Verify that the entire application works as intended.    | Cypress, Playwright, Puppeteer     |
| **Manual Testing**   | Human-performed tests to explore and identify issues.            | Catch issues not easily found by automated tests.        | Exploratory, usability checks      |


---

### The Testing Pyramid Overview
- The testing pyramid is a representation of how to distribute different types of tests.
- Tests at the bottom are more numerous and foundational, while tests at the top are fewer, more complex, and take longer to maintain.
- As you move up the pyramid, tests become slower, more complex, and require more maintenance.

### 1. **Unit Tests**
- Form the base of the pyramid and are the most commonly written tests.
- Focus on testing individual functions or methods to ensure the correctness of code logic.
- The number of unit tests depends on your testing strategy; aim for complete coverage of your code.
- Full code coverage means testing every line of your methods, often a sign of well-structured code.
- A function that’s hard to fully test might be doing too much or lacking testability.
- **Code Coverage**:
  - Refers to how much of the code is tested; typically targets line coverage.
  - Industries such as military or aviation may require **Modified Condition/Decision Coverage (MCDC)**.
  - MCDC requires testing each line and decision in the code, e.g., an `if` statement with three conditions needs eight unit tests for full coverage.

### 2. **Component Tests**
- Focus on testing complete, isolated sections of an application.
- Example: Testing an API separately from the frontend and database.
- Mock external dependencies (e.g., database, services) to test specific component behavior.
- Useful for checking the application’s behavior in happy paths and edge cases, such as handling database downtimes or invalid requests.
- Ensure that units tested in isolation at the lower level work well when integrated.

### 3. **Integration Tests**
- Move one level up to check how different components work together.
- Unlike component tests, integration tests involve real interactions with components such as databases.
- Validate connections and data flow between parts of the system, such as checking API calls or database interactions.
- Catch issues like mismatched naming conventions (e.g., camelCase vs. snake_case) or typos in connection strings.
- May be classified as **White Box** or **Black Box** tests:
  - **White Box**: Written by developers, aware of internal structures.
  - **Black Box**: Written by testers, focusing on outcomes without needing knowledge of internal code.

### 4. **End-to-End (E2E) Tests**
- Ensure the entire application works as expected from the user's perspective.
- Often involve automated UI tests that mimic user actions, using tools like Selenium or Cypress.
- Combine **functional testing** (e.g., verifying login functionality) with **acceptance testing** (checking business requirement fulfillment).
- Typically written using **Gherkin language** (Given-When-Then format) for better readability and stakeholder understanding, using tools like Cucumber or SpecFlow.
- E2E tests are time-consuming and may not run on every build; often run overnight to avoid delays in deployment.
- Run on environments like QA or UAT and require stable conditions, as slow load times or UI changes can lead to test failures.
- Screenshots during failures can aid in diagnosing issues.

### 5. **Manual Tests**
- Positioned at the top of the pyramid and used for complex or low-priority scenarios that aren’t worth automating.
- A lack of resources (e.g., more developers than testers) often results in more manual testing.
- Although automated testing is ideal, some tests are better handled manually due to complexity or time constraints.
- Bugs found during manual testing are harder to trace and fix compared to those caught by lower-level automated tests.
- Discovering bugs at the bottom of the pyramid (e.g., unit tests) provides faster feedback and detailed error traces.

### **Final Thoughts**
- Automating as many tests as possible is crucial to avoid a cycle of insufficient testing before releases.
- Early detection of bugs at lower levels of the pyramid saves time and effort compared to finding them during manual testing.

---

This structured approach captures all the key points and aligns them under clear subheadings for better readability.





