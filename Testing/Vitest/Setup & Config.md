
### 1. **Basic Setup and Configuration**

- **Installing Vitest**: Learn how to add Vitest to your project and configure it.
- **Config File (`vitest.config.ts` or `vitest.config.js`)**: Understand how to customize the configuration for your needs, including setting up test environments, coverage reports, and more.

### 1. **Basic Setup and Configuration**

#### **Installing Vitest**

To install Vitest, you can simply use npm or yarn:

```bash
npm install --save-dev vitest
# or
yarn add --dev vitest
```

After installation, you can add a test script to your `package.json` to run the tests easily:

```json
{
  "scripts": {
    "test": "vitest"
  }
}
```

#### **Configuring Vitest (`vitest.config.ts` or `vitest.config.js`)**

You can customize Vitest's behavior by creating a configuration file. Here's a basic example of a `vitest.config.ts`:

```ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,  // Use global functions like 'expect' without imports
    environment: 'jsdom',  // Use jsdom for DOM-based testing (like React, Vue)
    coverage: {
      provider: 'c8',  // Coverage provider (e.g., c8, istanbul)
      reporter: ['text', 'json', 'html'],  // Output formats for coverage
    },
    watch: true,  // Enable watch mode for auto test reruns
  },
});
```

Key configuration options:

- **`globals`**: Automatically imports globals like `expect`, `vi`, `describe`, etc.
- **`environment`**: Set the test environment, e.g., `'jsdom'` for browser-like tests or `'node'` for Node.js.
- **`coverage`**: Configure code coverage options like provider, report formats, and thresholds.
- **`watch`**: Enable test watch mode for automatic reruns of tests on file changes.

This setup should get you started with Vitest. You can add more customizations as your testing needs grow!