## Introduction

This document outlines best practices to ensure consistency, maintainability, and scalability of the project.

---

## Coding Standards

- Follow [Airbnb's JavaScript Style Guide](https://github.com/airbnb/javascript).

---

## Project Structure

- Place all components in the `/src/components/` directory.
- Place all assets under the `src/assets` directory.
- Use `/src/hooks/` for reusable custom hooks.
- Use `/src/utils/` for reusable utility functions.
- Use `/src/contexts/` for context-based state management.
- Maintain a shallow directory structure, avoiding more than two nested levels.

### Feature-Based Organization

- Group files by feature (e.g., `components/product-details`, `components/user-profile`) rather than file type.
- Use descriptive names for folders and files (e.g., `ProductDetails.js`, `ProductDetails.css`).
- Keep related files together (e.g., components, styles, and tests in the same folder).

---

## File Structure

- Maintain a proper import structure:
    
    1. Built-in modules (e.g., `react`)
    2. External (third-party libraries)
    3. Internal modules (project-specific components, utilities, etc.)
- Use functional components (prefer arrow functions) that serve a single purpose and remain pure.
    
- Avoid using `any` type; include strict typing (TypeScript or PropTypes).
    
- Use the `useReducer` hook if a component exceeds four `useState` hooks or involves complex state management.
    
- Use shorthand for boolean props:
    
    ```jsx
    // Instead of this:
    <RegistrationForm hasPadding={true} withError={true} />
    
    // Use this:
    <RegistrationForm hasPadding withError />
    ```
    

---

## Naming Conventions

- Use `PascalCase` for components, interfaces, type aliases, and file names.
- Use `camelCase` for variables, arrays, objects, and functions.
- Use `UPPER_CASE_SNAKE_CASE` for constants.

---

## Component Design

- **Functional Components**: Use functional components with Hooks (`useState`, `useEffect`) instead of class components.
- **Single Responsibility**: Each component should do one thing well.
- **Small, Reusable Components**: Break down large components into smaller ones for reuse and easier testing.
- **Controlled Components**: Use controlled components for forms where React state manages the form data.
- **Avoid Prop Drilling**: Use the Context API or state management libraries (e.g., Redux, Zustand) to avoid passing props down multiple levels.

---

## State Management

- Lift state up when needed and avoid unnecessary global state.
- Use Redux for state management; prefer Redux Toolkit for simplicity and best practices.
- Always update state immutably to avoid side effects.

---

## Styling

- Use CSS Modules or `@emotion/styled` for scoped, maintainable styling.
- Follow consistent naming conventions for CSS classes (e.g., BEM).
- Avoid inline styles to prevent performance issues and maintain consistency.

---

## Performance Optimization

- Use `React.memo` for functional components to prevent unnecessary re-renders.
- Use `useCallback` and `useMemo` to memoize functions and expensive calculations.
- Implement code splitting using dynamic imports to reduce initial load time.
- Lazy load components with `React.lazy` and `Suspense`.
- Use virtualization libraries for rendering large datasets.

---

## Error Handling

- Implement error boundaries to catch JavaScript errors and display fallback UIs.

---

## Type Safety

- Use TypeScript for type safety in large applications.
- Use PropTypes for smaller projects to enforce type validation for components.

---

## Testing

- Write tests for every new feature or bug fix.
- Aim for at least 90% test coverage.
- Use tools like Jest and React Testing Library for unit and integration tests.
- Use Playwright for end-to-end testing.
- Use snapshot testing to ensure consistent rendering of components.

---

## Accessibility

- Use semantic HTML elements (e.g., `<header>`, `<nav>`, `<footer>`).
- Ensure components are navigable via keyboard.
- Provide alternative text for images and appropriate labels for form elements.

---

## Version Control

- Use feature branches, pull requests, and code reviews to maintain a clean codebase.
- Follow conventional commit messages (e.g., `feat:`, `fix:`, `chore:`).

---

## Deployment & CI/CD

- Use CI/CD pipelines for automated testing and deployment (e.g., GitHub Actions, CircleCI).
- Manage environment variables with `.env` files, configuring different settings for development and production.

---

## Security

- Sanitize inputs and escape dynamic content to prevent XSS attacks.
- Use CSRF tokens for secure backend interactions.

---

## Documentation

- Document components and hooks with clear README files, inline comments, and JSDocs.
- Use Storybook for documenting UI components and their variations.

---

## Commit Message Convention

- Use [Conventional Commits](https://www.conventionalcommits.org/) for clarity:
    
    - `feat:` for new features.
    - `fix:` for bug fixes.
    - `chore:` for non-functional changes.
- Use pre-commit hooks with Husky for linting and formatting.
    

---

## External Libraries

- **Lodash**: For utility functions.
- **Day.js**: For date and time manipulation.
- **Intl**: Use JavaScript's `Intl` API for internationalization and localization.

---
ESlint rules:

### **General Best Practices**

1. **Code Consistency:**
    
    - `"semi": ["error", "always"]` - Enforce semicolons at the end of statements.
    - `"quotes": ["error", "single"]` - Enforce single quotes for strings.
    - `"eol-last": ["error", "always"]` - Ensure files end with a newline.
    - `"indent": ["error", 2, { "SwitchCase": 1 }]` - Enforce consistent indentation with 2 spaces.
    - `"linebreak-style": ["error", "unix"]` - Enforce Unix linebreak style.
    - `"no-trailing-spaces": "error"` - Disallow trailing spaces.
    - `"curly": ["error", "all"]` - Enforce consistent use of curly braces for all control statements.
2. **Naming and Readability:**
    
    - `"camelcase": ["error", { "properties": "always" }]` - Enforce camelCase naming for variables and functions.
    - `"max-len": ["error", { "code": 80, "ignoreComments": true }]` - Enforce a maximum line length for better readability.
    - `"consistent-return": "error"` - Require consistent `return` statements.
3. **Error Prevention:**
    
    - `"no-console": ["error", { "allow": ["warn", "error"] }]` - Allow `console.warn` and `console.error` but disallow others.
    - `"no-unused-vars": ["error", { "args": "none", "ignoreRestSiblings": true }]` - Disallow unused variables while ignoring rest siblings.
    - `"no-use-before-define": ["error", { "functions": false, "classes": true }]` - Disallow use of variables before they're defined.
    - `"eqeqeq": ["error", "always"]` - Enforce strict equality (`===`) usage.
4. **Functional Best Practices:**
    
    - `"no-duplicate-imports": "error"` - Disallow duplicate imports in a single file.
    - `"no-param-reassign": "error"` - Disallow reassigning function parameters.
    - `"prefer-const": "error"` - Require `const` for variables never reassigned.
    - `"arrow-body-style": ["error", "as-needed"]` - Enforce concise arrow function bodies where possible.

---

### **React-Specific Rules**

1. **React Standards:**
    
    - `"react/react-in-jsx-scope": "off"` - Disable the need for React import in JSX files (default in React 17+).
    - `"react/jsx-uses-react": "off"` - Prevent unused React variables (now redundant).
    - `"react/jsx-filename-extension": ["error", { "extensions": [".jsx", ".tsx"] }]` - Enforce JSX syntax only in `.jsx` or `.tsx` files.
2. **Component Design:**
    
    - `"react/prop-types": "off"` - Disable PropTypes enforcement if TypeScript is used.
    - `"react/jsx-key": "error"` - Require `key` prop for list elements in JSX.
    - `"react/self-closing-comp": "error"` - Enforce self-closing tags for components without children.
    - `"react-hooks/rules-of-hooks": "error"` - Enforce React Hook rules (e.g., only call Hooks at the top level).
    - `"react-hooks/exhaustive-deps": "warn"` - Warn for missing dependencies in useEffect.

---

### **TypeScript-Specific Rules (if using TypeScript)**

1. **Strict Typing:**
    
    - `"@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }]` - Ignore unused variables starting with `_`.
    - `"@typescript-eslint/explicit-function-return-type": "off"` - Disable mandatory return types for functions (enable in strict projects).
    - `"@typescript-eslint/no-explicit-any": "warn"` - Warn against using `any` type.
2. **TypeScript Enhancements:**
    
    - `"@typescript-eslint/no-non-null-assertion": "error"` - Disallow non-null assertions (`!`).
    - `"@typescript-eslint/prefer-optional-chain": "error"` - Enforce the use of optional chaining.
    - `"@typescript-eslint/consistent-type-imports": ["error", { "prefer": "type-imports" }]` - Enforce consistent use of `import type`.

---

### **Performance and Optimization**

1. `"no-shadow": "error"` - Disallow variable declarations from shadowing outer-scope variables.
2. `"no-return-await": "error"` - Disallow unnecessary `await` inside `return` statements.
3. `"no-multi-spaces": "error"` - Disallow multiple spaces, except for alignment.
4. `"prefer-spread": "error"` - Enforce the use of `Function.prototype.apply()` with the spread operator.

---

### **Accessibility**

- `"jsx-a11y/anchor-is-valid": "warn"` - Ensure anchors have valid content.
- `"jsx-a11y/alt-text": "error"` - Require alt attributes for `<img>` tags.

---

### **Tools and Configurations**

- Use **Prettier** for code formatting and integrate it with ESLint:
    
    ```json
    "extends": ["eslint:recommended", "plugin:react/recommended", "plugin:@typescript-eslint/recommended", "prettier"]
    ```
    
- Install ESLint plugins for React, TypeScript, and accessibility:
    
    ```bash
    npm install eslint-plugin-react eslint-plugin-react-hooks eslint-plugin-jsx-a11y @typescript-eslint/eslint-plugin eslint-plugin-prettier
    ```
    
- Add a `.eslintignore` file to exclude unnecessary directories (e.g., `node_modules`, `dist`, `build`).

---

These rules are widely recognized and strike a balance between strictness and flexibility. Let me know if you'd like help integrating these into your project!



---

Code Coverage:

## Vite

To enable and generate code coverage reports in a **Vite + Vitest** setup, follow these steps:

---

### **1. Install Required Dependencies**

You need Vitest (testing library) and the coverage plugin:

```bash
npm install vitest @vitest/coverage-c8 --save-dev
```

---

### **2. Configure Vitest for Coverage**

Update your `vite.config.js` or `vitest.config.ts` file with the following configuration:

```javascript
import { defineConfig } from 'vite';

export default defineConfig({
  test: {
    globals: true, // Optional: Enables global APIs like `describe` and `it`
    environment: 'jsdom', // Or 'node', depending on your tests
    coverage: {
      provider: 'c8', // Use c8 for coverage collection
      reportsDirectory: './coverage', // Directory to output coverage reports
      reporter: ['text', 'html', 'lcov'], // Text summary and detailed HTML reports
      all: true, // Analyze all files, even untested ones
      include: ['src/**/*.{js,ts,jsx,tsx}'], // Include only source files
      exclude: ['node_modules', 'tests'], // Exclude specific directories or files
      lines: 80, // Set coverage thresholds
      functions: 80,
      branches: 80,
      statements: 80,
    },
  },
});
```

---

### **3. Write and Run Tests**

Write your unit tests in the `tests/` or `__tests__/` directory, or co-locate them with your source files.

Run the tests with coverage:

```bash
npx vitest --coverage
```

---

### **4. View Coverage Reports**

- **Console Output**: You'll see a summary of the coverage in your terminal.
- **HTML Report**: Open the `./coverage/index.html` file in your browser for a detailed, interactive view.
- **LCOV Report**: Use the `lcov` report to integrate with CI/CD tools like Coveralls or Codecov.

---

### **5. Enforce Coverage Thresholds**

To fail tests if coverage drops below thresholds, include the `lines`, `functions`, `branches`, and `statements` settings in your configuration.

Example:

```javascript
coverage: {
  lines: 90,
  functions: 90,
  branches: 80,
  statements: 90,
},
```

If thresholds are not met, Vitest will exit with an error code.

---

### **6. Integrate in CI/CD**

For CI/CD, run Vitest with coverage and upload the results to services like **Codecov**:

1. Add to your CI/CD pipeline:
    
    ```bash
    npx vitest --coverage
    npx codecov # Uploads coverage reports to Codecov
    ```
    
2. Example for **GitHub Actions**:
    
    ```yaml
    name: Run Tests and Coverage
    on: [push, pull_request]
    
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - uses: actions/setup-node@v3
            with:
              node-version: 16
          - run: npm ci
          - run: npm test -- --coverage
          - run: npx codecov
    ```
    

---

This setup provides detailed coverage insights, enforces quality standards, and integrates well with CI/CD workflows. Let me know if you need further clarification!

### **1. Jest (Most Common for React/Node.js Projects)**

Jest has built-in support for code coverage.

1. **Install Jest (if not already):**
    
    ```bash
    npm install jest --save-dev
    ```
    
2. **Enable Code Coverage:** Add the `--coverage` flag when running tests:
    
    ```bash
    npx jest --coverage
    ```
    
3. **Output:** Jest generates a `coverage` directory containing:
    
    - **HTML Report**: Viewable in a browser (`coverage/index.html`).
    - **Text Summary**: Displayed in the console.
4. **Configuration (Optional):** Add to `jest.config.js` or `package.json`:
    
    ```javascript
    module.exports = {
      collectCoverage: true,
      coverageDirectory: "coverage",
      coverageReporters: ["text", "lcov", "json"],
      collectCoverageFrom: [
        "src/**/*.{js,jsx,ts,tsx}",
        "!src/**/*.test.{js,jsx,ts,tsx}",
        "!src/index.js", // Exclude entry points
      ],
    };
    ```
    

---

### **2. Mocha + NYC (Istanbul Command-Line Interface)**

If you're using Mocha, you'll need NYC (Istanbul) to generate coverage.

1. **Install NYC and Mocha:**
    
    ```bash
    npm install nyc mocha --save-dev
    ```
    
2. **Add NYC Configuration:** Add to `package.json`:
    
    ```json
    "nyc": {
      "include": ["src/**/*.js"],
      "exclude": ["test/**/*.js"],
      "reporter": ["text", "html"],
      "all": true
    }
    ```
    
3. **Run Tests with NYC:**
    
    ```bash
    npx nyc mocha
    ```
    
4. **Output:** A `coverage` directory is created with HTML reports.
    

---

### **3. Playwright**

Playwright supports code coverage using tools like **Istanbul** or **V8 Coverage**.

1. **Install Dependencies:**
    
    ```bash
    npm install playwright istanbul --save-dev
    ```
    
2. **Integrate Istanbul:** Add Istanbul middleware for coverage instrumentation. For example:
    
    ```javascript
    const { chromium } = require('playwright');
    const { createCoverageMap } = require('istanbul-lib-coverage');
    
    const browser = await chromium.launch();
    const page = await browser.newPage();
    await page.coverage.startJSCoverage();
    
    // Perform your tests here
    
    const coverage = await page.coverage.stopJSCoverage();
    const coverageMap = createCoverageMap(coverage);
    console.log(coverageMap.toJSON());
    ```
    
3. **Generate Report:** Use Istanbul's CLI to process the coverage data.
    

---

### **4. Cypress**

Cypress supports code coverage through plugins.

1. **Install Cypress Code Coverage Plugin:**
    
    ```bash
    npm install @cypress/code-coverage --save-dev
    ```
    
2. **Instrument Your Code:** Use Babel or Istanbul to instrument your codebase.
    
3. **Add Plugin to Cypress:** In `cypress/plugins/index.js`:
    
    ```javascript
    module.exports = (on, config) => {
      require('@cypress/code-coverage/task')(on, config);
      return config;
    };
    ```
    
4. **Include Coverage Script in Tests:** Add to `cypress/support/index.js`:
    
    ```javascript
    import '@cypress/code-coverage/support';
    ```
    
5. **Run Cypress and Generate Reports:**
    
    ```bash
    npx cypress run
    ```
    

---

### **5. Vite + Vitest**

If you're using Vite with Vitest:

1. **Install Vitest and Coverage Plugin:**
    
    ```bash
    npm install vitest @vitest/coverage-c8 --save-dev
    ```
    
2. **Add Configuration:** Update `vite.config.js`:
    
    ```javascript
    import { defineConfig } from 'vite';
    import { coverageC8 } from '@vitest/coverage-c8';
    
    export default defineConfig({
      plugins: [coverageC8()],
      test: {
        coverage: {
          reporter: ['text', 'html'],
        },
      },
    });
    ```
    
3. **Run Tests:**
    
    ```bash
    npx vitest --coverage
    ```
    

---

### **6. Code Coverage Thresholds**

Set coverage thresholds to enforce minimum requirements:

```javascript
module.exports = {
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```

---

### **7. CI/CD Integration**

Add coverage reports to CI/CD pipelines:

- Upload results to tools like **Coveralls** or **Codecov**.
- Example using GitHub Actions:
    
    ```yaml
    name: Test and Coverage
    on: [push, pull_request]
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - uses: actions/setup-node@v3
            with:
              node-version: '16'
          - run: npm install
          - run: npm test -- --coverage
          - run: npx codecov
    ```
    

---

Let me know which framework you're using, and I can provide more tailored instructions!