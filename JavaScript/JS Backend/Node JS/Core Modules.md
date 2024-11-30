
core modules** are the built-in modules that come pre-packaged with Node.js. 
These modules provide essential functionalities needed to build applications without requiring any third-party libraries. 
Core modules are directly available within Node.js and are highly optimized for performance and compatibility.

### Key Features of Core Modules:
1. **No Installation Required**: Since they are part of Node.js, you don’t need to install them through `npm` or any other package manager.
2. **Optimized and Reliable**: They are maintained by the Node.js team and are optimized to work efficiently with Node.js.
3. **Common Utilities**: Core modules cover various functionalities, like working with file systems, handling streams, managing HTTP requests, and more.

### Summary
Core modules are foundational, built-in modules in Node.js, providing the core functionality to build powerful applications without needing external libraries.


### 1. **`http` Module**
   - **Purpose**: Creates HTTP servers and handles HTTP requests and responses.
   - **Key Functions**:
     - `http.createServer()`: Creates an HTTP server.
     - Node.js’s `http` module allows you to create an HTTP server to handle requests and responses.
     - - **Key Points**:
     - The `createServer` method is used to create a server that listens on a specified port.
     - The callback function receives request and response objects.
     - `req` (request object): Contains info about the request.
     - `res` (response object): Used to send responses back to the client.



   **Question**: *How do you create a simple HTTP server in Node.js?*
   - **Answer**:
     ```javascript
     const http = require('http');
     const server = http.createServer((req, res) => {
       res.writeHead(200, { 'Content-Type': 'text/plain' });
       res.end('Hello, World!');
     });
     server.listen(3000);
     ```
   - **Explanation**: The server listens on port 3000 and responds with "Hello, World!" for every request.

   **Question**:  Can you explain how the `fs` module works in asynchronous vs. synchronous mode?


The `fs` module in Node.js provides both **asynchronous** (non-blocking) and **synchronous** (blocking) methods for file operations. Here’s a quick breakdown:

### Asynchronous Mode (`fs.readFile`)
In asynchronous mode, `fs` offloads file I/O to `libuv`, which runs it in the background. This allows the main thread to continue running other code while `fs` waits for the file operation to complete.

#### Example: Asynchronous File Read
```javascript
const fs = require('fs');

console.log('Starting async file read...');

fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log('Async file content:', data);
});

console.log('Other work happening while file reads...');
```

**Output Order**:
1. "Starting async file read..."
2. "Other work happening while file reads..."
3. "Async file content: ..." (after the file read completes)

**Explanation**: `fs.readFile` is non-blocking, so it doesn’t stop the program; the callback runs only when the read completes.

### Synchronous Mode (`fs.readFileSync`)
In synchronous mode, the operation blocks the main thread until the file read completes, preventing any further code from running until it's done.

#### Example: Synchronous File Read
```javascript
const fs = require('fs');

console.log('Starting sync file read...');

const data = fs.readFileSync('example.txt', 'utf8');
console.log('Sync file content:', data);

console.log('Code after sync read executes only after reading file...');
```

**Output Order**:
1. "Starting sync file read..."
2. "Sync file content: ..." (immediately after file read completes)
3. "Code after sync read executes only after reading file..."

**Explanation**: `fs.readFileSync` is blocking, so no other code runs until the file read completes.

### Summary
- **Asynchronous (`fs.readFile`)**: Non-blocking, allows other code to run while waiting for I/O.
- **Synchronous (`fs.readFileSync`)**: Blocking, stops other code until the file read completes.

---

### 2. **`fs` (File System) Module**
   - **Purpose**: Handles file operations (read, write, delete, etc.).
   - **Key Functions**:
     - `fs.readFile()`: Reads a file asynchronously.
     - `fs.writeFile()`: Writes data to a file asynchronously.
     - `fs.unlink()`: Deletes a file.
     -  `fs.appendFile()`: Appends data to a file.

   **Question**: *How do you read a file asynchronously in Node.js?*
   - **Answer**:
     ```javascript
     const fs = require('fs');
     fs.readFile('example.txt', 'utf8', (err, data) => {
       if (err) throw err;
       console.log(data);
     });
     ```
   - **Explanation**: Reads the contents of "example.txt" and logs it. The `utf8` argument specifies encoding.





   **Question**: *How do you read a JSON file in Node.js?*
   - **Answer**:
     ```javascript
     const fs = require('fs');
     fs.readFile('data.json', 'utf8', (err, data) => {
       if (err) throw err;
       const jsonData = JSON.parse(data);
       console.log(jsonData);
     });
     ```
   - **Explanation**: Reads a file asynchronously, then parses the content into a JSON object.




---

### 3. **`path` Module**
   - **Purpose**: Works with file and directory paths.
   - **Key Functions**:
     - `path.join()`: Joins paths.
     - `path.basename()`: Gets the last part of a path.
     - `path.resolve()`: Resolves paths to an absolute path.

   **Question**: *How would you join two paths in Node.js?*
   - **Answer**:
     ```javascript
     const path = require('path');
     const fullPath = path.join(__dirname, 'folder', 'file.txt');
     console.log(fullPath);
     ```
   - **Explanation**: Joins `__dirname`, `folder`, and `file.txt` into a single path, handling separators correctly.

---

### 4. **`os` Module**
   - **Purpose**: Provides OS-related utilities and information.
   - **Key Functions**:
     - `os.type()`: Returns OS type.
     - `os.uptime()`: Returns system uptime in seconds.
     - `os.cpus()`: Returns info about each CPU/core.

   **Question**: *How can you get system uptime in Node.js?*
   - **Answer**:
     ```javascript
     const os = require('os');
     console.log(`System uptime: ${os.uptime()} seconds`);
     ```
   - **Explanation**: Fetches and logs system uptime using `os.uptime()`.

---

### 5. **`events` Module**
   - **Purpose**: Allows working with events and implementing the event-driven model.
   - **Key Functions**:
     - `EventEmitter`: Class for handling custom events with `emit()` and `on()` methods.
     - `emit(eventName)`: Triggers an event.
     - `on(eventName, callback)`: Listens for a specific event.
    * event arguments : additional information passed along with emitted event ... emit(eventName, ... args)

   **Question**: *How would you use `EventEmitter` in Node.js?*
   - **Answer**:
     ```javascript
     const EventEmitter = require('events');
     const emitter = new EventEmitter();

     emitter.on('greet', (name) => console.log('Hello! ${name}'));
     emitter.emit('greet','ashok');
     ```
   - **Explanation**: Defines a `greet` event, logs "Hello! ashok" when the event is triggered by `emit()`.


```js
// Import the built-in 'events' module from Node.js
const EventEmitter = require('events');

// Create a new instance of EventEmitter, which will allow us to create and manage events
const emitter = new EventEmitter();

// Register a listener (handler) for the 'greet' event
// The listener is a callback function that takes an argument (name) and logs a greeting message
emitter.on('greet', (name) => {
  console.log(`Hello, ${name}!`);
});

// Trigger (emit) the 'greet' event, passing an argument 'Alice' to the event
// This will call the listener function defined above, passing 'Alice' as the 'name' argument
emitter.emit('greet', 'Alice'); // Output: Hello, Alice!

```


---

### 6. **`url` Module**
   - **Purpose**: Parses and formats URL strings.
   - **Key Functions**:
     - `url.parse()`: Parses a URL string into an object.
     - `url.format()`: Formats a URL object into a string.

   **Question**: *How can you parse a URL string in Node.js?*
   - **Answer**:
     ```javascript
     const url = require('url');
     const myURL = url.parse('https://example.com/path?name=Node');
     console.log(myURL.query);
     ```
   - **Explanation**: Parses the URL, allowing access to properties like `query` (e.g., `{ name: 'Node' }`).

---

### 7. **`crypto` Module**
   - **Purpose**: Provides cryptographic functionalities (hashing, encryption).
   - **Key Functions**:
     - `crypto.createHash()`: Creates a hash.
     - `crypto.randomBytes()`: Generates random data.
     - `crypto.createCipher()`: Creates encryption instances.

   **Question**: *How do you create a SHA256 hash in Node.js?*
   - **Answer**:
     ```javascript
     const crypto = require('crypto');
     const hash = crypto.createHash('sha256').update('password').digest('hex');
     console.log(hash);
     ```
   - **Explanation**: Hashes the string "password" using SHA256, outputting the result in hexadecimal format.

---

### 8. **`stream` Module**
   - **Purpose**: Handles streaming data (large file handling).
   - **Key Types**:
     - `Readable`: For reading streams.
     - `Writable`: For writing streams.
     - `Duplex`: For reading and writing.

   **Question**: *How would you create a readable stream in Node.js?*
   - **Answer**:
     ```javascript
     const fs = require('fs');
     const readableStream = fs.createReadStream('example.txt', 'utf8');
     readableStream.on('data', (chunk) => console.log(chunk));
     ```
   - **Explanation**: Reads data from `example.txt` as chunks and logs each chunk.

---

### 9. **`util` Module**
   - **Purpose**: Provides utility functions for debugging and other helpers.
   - **Key Functions**:
     - `util.promisify()`: Converts a callback-based function into a Promise-based one.
     - `util.format()`: Formats strings (similar to `printf`).

   **Question**: *How can you use `util.promisify` to convert `fs.readFile` into a Promise?*
   - **Answer**:
     ```javascript
     const fs = require('fs');
     const util = require('util');
     const readFile = util.promisify(fs.readFile);

     readFile('example.txt', 'utf8').then(console.log).catch(console.error);
     ```
   - **Explanation**: Promisifies `fs.readFile`, allowing it to be used with Promises.

---

### 10. **`querystring` Module**
   - **Purpose**: Works with query strings in URLs.
   - **Key Functions**:
     - `querystring.parse()`: Parses a query string into an object.
     - `querystring.stringify()`: Converts an object to a query string.

   **Question**: *How can you parse a query string in Node.js?*
   - **Answer**:
     ```javascript
     const querystring = require('querystring');
     const parsedQuery = querystring.parse('name=Node&age=10');
     console.log(parsedQuery);
     ```
   - **Explanation**: Parses the string into an object `{ name: 'Node', age: '10' }`.







