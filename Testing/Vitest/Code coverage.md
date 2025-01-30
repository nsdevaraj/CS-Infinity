
### 6. **Code Coverage**

- **Setting up coverage**: Understand how to set up code coverage with Vitest and interpret the coverage reports.
- **Thresholds**: Learn how to configure coverage thresholds to enforce minimum coverage percentages.


### **Code Coverage in Vitest**

**Code coverage** helps you track how much of your code is being tested. It shows which lines of code are covered by tests and which are not, allowing you to identify untested parts of your codebase.

### 1. **Setting Up Code Coverage in Vitest**

To enable code coverage with Vitest, you need to configure it in your `vitest.config.ts` or `vitest.config.js` file.

#### **Basic Setup**:

1. **Install Vitest and Coverage Dependencies**: If you haven't already, make sure Vitest and the necessary coverage package are installed:
    
    ```bash
    npm install --save-dev vitest
    npm install --save-dev c8  # Coverage tool
    ```
    
2. **Configure Coverage in `vitest.config.ts`**: In your Vitest configuration file, you can enable coverage using the `coverage` property.
    
    ```js
    // vitest.config.ts
    import { defineConfig } from 'vitest/config';
    
    export default defineConfig({
      test: {
        coverage: {
          provider: 'c8',  // Use c8 as the coverage provider (default for Vitest)
          reporter: ['text', 'html'],  // You can use 'text', 'json', 'lcov', or 'html' for reports
          include: ['src/**/*.js'],  // Path to the files you want to measure coverage for
          exclude: ['src/**/*.test.js'],  // Optionally exclude test files
        },
      },
    });
    ```
    
3. **Running Tests with Coverage**: Once configured, you can run the tests with coverage reporting:
    
    ```bash
    vitest run --coverage
    ```
    
    This will generate coverage reports in the console and/or in an HTML file (depending on the reporter configuration). By default, the coverage report will include:
    
    - **Lines covered**
    - **Functions covered**
    - **Branches covered**
    - **Statements covered**

### 2. **Interpreting Coverage Reports**

Coverage reports help you understand which parts of your code are tested:

- **Statements**: Percentage of code lines that are executed.
- **Branches**: Percentage of conditional branches (like `if` statements) that are tested.
- **Functions**: Percentage of functions that have been called during tests.
- **Lines**: Percentage of lines that have been executed by tests.

Example output might look like:

```
Statements   : 90% (45/50)
Branches     : 85% (35/41)
Functions    : 100% (20/20)
Lines        : 88% (150/170)
```

You can click on the generated **HTML report** (if configured) to see detailed coverage for each file.

### 3. **Setting Coverage Thresholds**

You can configure **coverage thresholds** to enforce minimum coverage percentages. This ensures that your tests meet specific coverage standards before the build or tests are considered successful.

#### **Configure Coverage Thresholds**:

In your `vitest.config.ts`, use the `coverage.thresholds` property to define minimum coverage percentages for different categories:

```js
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    coverage: {
      provider: 'c8',
      thresholds: {
        global: {
          statements: 90,  // Minimum percentage of statements covered
          branches: 80,    // Minimum percentage of branches covered
          functions: 90,   // Minimum percentage of functions covered
          lines: 85,       // Minimum percentage of lines covered
        },
        // You can also set thresholds for specific files or directories:
        './src/specificFile.js': {
          statements: 100,
        },
      },
    },
  },
});
```

### 4. **What Happens If Thresholds Are Not Met?**

- If the code coverage falls below the set thresholds, Vitest will **fail the test** and notify you in the console that the coverage requirements weren’t met.
- You’ll get detailed output showing which thresholds were not met.

### 5. **Generating Different Report Formats**

- **Text Output**: Displays a summary in the console.
- **HTML Output**: Generates an interactive HTML report for visual inspection.
- **JSON Output**: Generates a machine-readable JSON file for integration with CI/CD or other tools.
- **LCOV Output**: Produces a format compatible with tools like Codecov or Coveralls.

Example:

```js
coverage: {
  reporter: ['text', 'html'],  // Generates both text summary and HTML report
}
```

### 6. **Best Practices for Code Coverage**

- **Aim for high coverage**, but don’t obsess over 100%. Focus on critical paths, business logic, and edge cases.
- **Don’t test everything** — especially trivial or auto-generated code (like getters/setters or pure getters in classes).
- **Enforce coverage thresholds** to ensure new code doesn't decrease test coverage.
- Use **HTML reports** for a visual understanding of coverage gaps.

---

### **Key Points**:

- **Setting Up Coverage**: Add `coverage` config in `vitest.config.ts` with a provider like `c8`.
- **Interpreting Reports**: Coverage reports show statements, branches, functions, and lines covered.
- **Thresholds**: Enforce minimum coverage (e.g., 80% statements, 90% functions).
- **Multiple Reporters**: Generate different report formats like `text`, `html`, or `json`.