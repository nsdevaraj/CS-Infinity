### 5. **Snapshot Testing**

- Learn how to use snapshot testing to capture and compare rendered output (commonly used with React components or HTML structures).

### **Snapshot Testing in Vitest**

Snapshot testing is a way to capture the output of a function or component and save it as a reference. In future tests, Vitest compares the output to the saved snapshot to check if anything has changed. This is especially useful for testing UI components (e.g., React components) or HTML structures.

### **How Snapshot Testing Works in Vitest**

1. **Create a Snapshot**: When you run the test for the first time, Vitest saves the rendered output (usually a UI or a structure) in a snapshot file.
    
2. **Compare Against Snapshot**: In subsequent test runs, Vitest compares the current output with the saved snapshot. If they differ, the test fails.
    
3. **Update Snapshot**: If the change is intentional (e.g., UI updates), you can update the snapshot.
    

### **Steps to Use Snapshot Testing**

1. **Basic Setup**:
    
    - Use `expect().toMatchSnapshot()` to capture and compare the output.
        
    - **Example (React Component)**:
        
        ```js
        import { render } from '@testing-library/react';
        import MyComponent from './MyComponent';
        
        test('renders MyComponent correctly', () => {
          const { asFragment } = render(<MyComponent />);
          expect(asFragment()).toMatchSnapshot();
        });
        ```
        
    - The `asFragment()` method from **React Testing Library** captures the HTML of the component. It is then compared to a snapshot stored in a `.snap` file.
        
2. **Snapshot Files**:
    
    - Vitest stores snapshots in a `__snapshots__` folder next to your test files.
    - The first time you run the test, a snapshot file is created with the rendered output.
3. **Updating Snapshots**:
    
    - If the component or output changes, you can update the snapshot with the `--updateSnapshot` flag:
        
        ```bash
        vitest --updateSnapshot
        ```
        
4. **Example with Non-UI Output**:
    
    - Snapshot testing isn’t limited to UI components. You can use it for any serializable data.
    - **Example (Plain Object)**:
        
        ```js
        test('returns correct object', () => {
          const data = fetchData();  // fetchData is a function returning an object
          expect(data).toMatchSnapshot();
        });
        ```
        
5. **Snapshot Diffing**:
    
    - When the output changes, Vitest shows a diff in the test output, highlighting the differences between the old and new snapshot.
6. **Best Practices**:
    
    - Use snapshots for testing **UI consistency** and **serializable data** (objects, arrays).
    - **Avoid** using snapshots for highly dynamic content or if the output can change frequently without changes to logic (e.g., timestamps, random values).
    - Consider **small and focused snapshots** to keep tests easier to understand and maintain.

### **Key Points**:

- **`toMatchSnapshot()`** captures the output of a function/component and saves it.
- Snapshots are saved in `__snapshots__` folder.
- **`--updateSnapshot`** updates snapshots if changes are intentional.
- Useful for testing React components, UI, or any serializable output.