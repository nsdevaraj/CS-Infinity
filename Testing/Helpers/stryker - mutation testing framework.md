


# 🔬 Stryker: Mutation Testing for JavaScript and TypeScript

## What Is Mutation Testing?

Traditional code coverage tools like **Istanbul** or **nyc** measure whether code has been _executed_ by tests, but they don’t measure how well the tests detect _faults_. In other words, they answer:

> “Was this line executed?”

But not:

> “Would the test fail if this line was wrong?”

**Mutation testing** fills this gap by measuring the quality of your test suite. It works by **intentionally introducing bugs** (called _mutants_) into your code and then re-running your tests to see if they fail. If your test suite doesn’t catch the introduced bug, it may be weak or incomplete.

---

## What Is Stryker?

**Stryker** is a powerful, open-source **mutation testing framework** for JavaScript, TypeScript, and related ecosystems. Named after a character from _X-Men_, Stryker helps developers create **more effective test suites** by evaluating their ability to catch real-world bugs.

### Supported Runtimes & Tools

Stryker works with:

- **Test runners**: Jest, Mocha, Vitest, Jasmine, Karma
    
- **Frameworks**: React, Angular, Vue, Node.js
    
- **Languages**: JavaScript (ES5+), TypeScript
    
- **Package managers**: npm, yarn, pnpm
    

---

## Why Use Mutation Testing?

### ✅ Advantages of Stryker:

1. **Uncovers Weak Tests**  
    Helps you identify tests that _appear_ to provide coverage but do not assert correct behavior.
    
2. **Improves Code Quality**  
    Encourages stronger testing practices by revealing untested logic and false positives.
    
3. **Boosts Confidence**  
    With higher mutation scores, you can trust that your code is genuinely well-tested.
    
4. **Prevents Regressions**  
    By simulating real bugs, Stryker helps ensure your tests catch future failures.
    

---

## How Stryker Works

Here’s a high-level view of the process:

1. **Instrumentation**: Stryker modifies your source code by introducing small changes (_mutants_), such as changing `+` to `-`, or `true` to `false`.
    
2. **Execution**: It runs your tests for each mutant.
    
3. **Evaluation**:
    
    - If a test **fails**, the mutant is **killed** (good!).
        
    - If all tests **pass**, the mutant **survives** (bad — your tests missed it).
        
4. **Report Generation**: A detailed report shows which mutants survived, died, or caused issues, along with a **mutation score**.
    

---

## Example of a Mutant

Original code:

```ts
function isPositive(n: number): boolean {
  return n > 0;
}
```

Mutated version:

```ts
function isPositive(n: number): boolean {
  return n >= 0; // mutant: > changed to >=
}
```

If your tests don’t detect this change, it means they’re not checking the boundary condition properly.

---

## Mutation Score

After testing, Stryker gives you a **mutation score**:

```
Mutation Score: 85%
```

This means 85% of the mutants were killed (your tests detected them). The higher, the better. A good benchmark is:

- **90%+**: Strong test suite
    
- **70–90%**: Good, with room for improvement
    
- **<70%**: Weak — likely to miss bugs
    

---

## Installation and Setup

To get started:

### 1. Install Stryker

```bash
npm install --save-dev @stryker-mutator/core
```

Or use:

```bash
pnpm add -D @stryker-mutator/core
```

### 2. Initialize Configuration

```bash
npx stryker init
```

This will prompt you to select:

- Your test runner (e.g., Jest, Mocha, Vitest)
    
- Framework/language options
    
- Reporters
    
- Package manager
    

It generates a `stryker.conf.json` file.

### 3. Run Mutation Tests

```bash
npx stryker run
```

Reports will be output to the `reports/mutation/html` directory by default.

---

## Configuration Example

Here’s a basic `stryker.conf.json` for a TypeScript + Vitest project:

```json
{
  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  "packageManager": "pnpm",
  "reporters": ["clear-text", "progress", "html"],
  "coverageAnalysis": "perTest",
  "buildCommand": "pnpm build",
  "testRunner": "vitest",
  "checkers": ["typescript"],
  "plugins": [
    "@stryker-mutator/vitest-runner",
    "@stryker-mutator/typescript-checker"
  ],
  "incremental": true,
  "ignoreStatic": true,
  "vitest": {
    "configFile": "test/unit/_setup/vitest.config.ts"
  }
}
```

---

## Best Practices

✅ **Write Strong Assertions**  
Ensure your tests fail when code is incorrect.

✅ **Cover Edge Cases**  
Stryker often exposes missed boundary conditions.

✅ **Use perTest Coverage Analysis**  
This allows Stryker to associate mutants with specific tests and run only those, speeding things up.

✅ **Incremental Mode for CI**  
Enable `incremental: true` to skip unchanged files on subsequent runs.

✅ **Use HTML Reports**  
Easier to browse and explore which mutants survived.

---

## Limitations

🔸 **Performance**: Mutation testing can be slow, especially on large projects. Stryker supports parallelization and selective testing to mitigate this.

🔸 **Flaky Tests**: Tests that don’t behave deterministically can cause false positives or negatives in mutation testing.

🔸 **Not a Replacement for Coverage**: Use it alongside code coverage tools, not instead of them.

---

## Tools & Integrations

- **VS Code Extension**: Highlights survived mutants in your editor.
    
- **GitHub Actions**: Run Stryker as part of CI/CD pipelines.
    
- **Stryker Dashboard (Beta)**: For tracking mutation scores across builds.
    

---

## Conclusion

Mutation testing with Stryker is a **next-level technique** for ensuring test quality. While traditional code coverage tells you if code has been run, Stryker tells you if your tests actually **detect bugs**.

By introducing and testing real-world fault simulations, Stryker helps developers build **more robust, trustworthy applications**—an essential practice in today’s quality-focused development pipelines.

---

## Resources

- 🔗 [Stryker Official Docs](https://stryker-mutator.io/)
    
- 📦 [GitHub Repo](https://github.com/stryker-mutator/stryker-js)
    
- 🛠️ [Try it in a sandbox](https://stryker-mutator.io/docs/stryker-js/getting-started/)
    

---

Let me know if you'd like this formatted for a blog, documentation, or as a Markdown file!