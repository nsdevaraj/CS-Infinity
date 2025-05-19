


Setup steps:
install dev dependencies packages, have stryker.json in root folder..
then do `stryker run` command!


Stryker configuration file : `stryker.json`

```json
{
  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  "_comment": "This config was generated using 'stryker init'. For more information, visit: https://stryker-mutator.io/docs/stryker-js/configuration/",
  
  "packageManager": "<your-package-manager>", // e.g., "npm", "yarn", or "pnpm"
  
  "reporters": [
    "clear-text",
    "progress",
    "html"
  ],

  "testRunner_comment": "Make sure the test runner plugin is installed and properly configured in your project.",
  "testRunner": "<your-test-runner>", // e.g., "jest", "mocha", "vitest"

  "coverageAnalysis": "perTest", // or "off", "all"

  "buildCommand": "<your-build-command>", // e.g., "npm run build"

  "checkers": [
    "typescript" // Optional: Add or remove checkers as needed
  ],

  "plugins": [
    "<your-test-runner-plugin>", // e.g., "@stryker-mutator/jest-runner"
    "<optional-checker-plugin>"  // e.g., "@stryker-mutator/typescript-checker"
  ],

  "incremental": true, // Optional: Enable incremental mutation testing
  "ignoreStatic": true, // Optional: Ignore static (non-changing) code

  "<test-runner-specific-config>": {
    "configFile": "<path-to-your-test-config-file>" // e.g., "test/setup/jest.config.ts"
  }
}
```


 `stryker.conf.json` file with :

```json
{
  // Path to the schema for validation and auto-completion
  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  
  // Info: Generated using 'stryker init'. More details at:
  // https://stryker-mutator.io/docs/stryker-js/configuration/
  "_comment": "This config was generated using 'stryker init'. Please take a look at: https://stryker-mutator.io/docs/stryker-js/configuration/ for more information.",

  // Specify the package manager used in your project (e.g., npm, yarn, pnpm)
  "packageManager": "pnpm",

  // Reporters define how mutation testing results are presented
  "reporters": [
    "clear-text",  // Console output in readable text
    "progress",    // Progress bar during mutation testing
    "html"         // Full HTML report generated in 'reports/mutation/html'
  ],

  // Just a comment noting a missing 'homepage' field in a plugin package
  "testRunner_comment": "Take a look at (missing 'homepage' URL in package.json) for information about the command plugin.",

  // Strategy used for calculating code coverage
  // Options: "off", "all", or "perTest" (recommended for accurate results)
  "coverageAnalysis": "perTest",

  // Command to build the project before mutation testing
  "buildCommand": "pnpm build",

  // The test runner to use (e.g., jest, mocha, vitest)
  "testRunner": "vitest",

  // Checkers run static analysis like TypeScript checking
  "checkers": [
    "typescript" // Enables TypeScript type checking
  ],

  // List of Stryker plugins required for your setup
  "plugins": [
    "@stryker-mutator/vitest-runner",         // Plugin to integrate with Vitest
    "@stryker-mutator/typescript-checker"     // Plugin to perform TypeScript checks
  ],

  // Enables incremental mutation testing (faster runs by skipping unchanged files)
  "incremental": true,

  // Ignores files that are static (no executable code), reducing noise
  "ignoreStatic": true,

  // Vitest-specific configuration block
  "vitest": {
    // Path to your Vitest config file
    "configFile": "test/unit/_setup/vitest.config.ts"
  }
}
```


add these packages in dev dependencies:

```js
"@stryker-mutator/core": "^9.0.1",
"@stryker-mutator/typescript-checker": "^9.0.1",
"@stryker-mutator/vitest-runner": "^9.0.1",
```


