

### **Question 6: Create a Recursive Function to List All Files in a Directory**

**Problem:**  
Write a Node.js function that recursively lists all files (with their full paths) in a given directory and its subdirectories.

**Answer:**  
Here’s the implementation:

```javascript
const fs = require('fs');
const path = require('path');

// Recursive function to list all files
const listFiles = (dir) => {
  let results = [];
  const files = fs.readdirSync(dir);

  files.forEach((file) => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      // Recurse into subdirectory
      results = results.concat(listFiles(filePath));
    } else {
      results.push(filePath);
    }
  });

  return results;
};

// Example usage
const directoryPath = './example-directory';
try {
  const files = listFiles(directoryPath);
  console.log('Files found:');
  files.forEach((file) => console.log(file));
} catch (err) {
  console.error('Error reading directory:', err.message);
}
```

**Explanation:**

1. **Directory Reading:** `fs.readdirSync` reads the contents of a directory.
2. **File Checking:** `fs.statSync` determines whether the path is a directory or file.
3. **Recursion:** If the path is a directory, the function recursively collects files from the subdirectory.
4. **Result:** All files (with full paths) are returned as a flat array.

**Example Directory Structure:**

```
example-directory/
├── file1.txt
├── subdir1/
│   └── file2.txt
└── subdir2/
    └── file3.txt
```

**Expected Output:**

```
Files found:
./example-directory/file1.txt
./example-directory/subdir1/file2.txt
./example-directory/subdir2/file3.txt
```

This is a common interview task to test recursion, file system handling, and Node.js knowledge.



