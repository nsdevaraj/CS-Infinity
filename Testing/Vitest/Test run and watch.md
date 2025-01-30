### 7. **Running and Watching Tests**

- **Running Tests**: Learn the various ways you can run tests in Vitest, like via CLI or with watch mode for automatic re-runs.
- **Watch Mode**: Understand the power of Vitest’s watch mode (`vitest --watch`) to run only tests related to modified files.

### **Running and Watching Tests in Vitest (Crisp Overview)**

#### **1. Running Tests**

- **Run All Tests**:
    
    ```bash
    vitest run
    ```
    
- **Run Specific Test File**:
    
    ```bash
    vitest run src/tests/myComponent.test.js
    ```
    
- **Run Tests with Coverage**:
    
    ```bash
    vitest run --coverage
    ```
    
- **Run Tests with Parallel Workers**:
    
    ```bash
    vitest run --maxWorkers 4
    ```
    

#### **2. Watch Mode**

- **Start Watch Mode**: Automatically re-runs tests when files change.
    
    ```bash
    vitest --watch
    ```
    
- **Run Tests for Specific Files**: Watch specific files or directories.
    
    ```bash
    vitest --watch src/components/**/*.test.js
    ```
    
- **Run Tests with Coverage in Watch Mode**:
    
    ```bash
    vitest --watch --coverage
    ```
    

#### **3. Interactive Watch Mode Features**

- **Re-run Tests**: Press `r` to re-run tests in watch mode.
- **Print Logs**: Press `p` to print logs of failed tests.
- **Quit Watch Mode**: Press `q` to quit.

#### **4. Watch Mode Options**

- **Run Only Failed Tests**:
    
    ```bash
    vitest --watch --onlyFailures
    ```
    
- **Clear Cache**:
    
    ```bash
    vitest --watch --clearCache
    ```
    

### **Key Points**:

- **Run tests** with `vitest run`, **watch tests** with `vitest --watch`.
- **Watch Mode** re-runs tests on file changes, filtering by modified files.
- **Interactive Mode** allows for quick control (re-run, logs, quit).