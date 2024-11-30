

### 12. Node.js and Full-Stack Development

JavaScript runs not only in the browser but also on the server with **Node.js**. This opens the door for building full-stack applications with JavaScript.

#### Example: Running JavaScript in Node.js

```bash
node myScript.js
```



## 11. Node.js and JavaScript on the Server

### Key Points
- Node.js allows JavaScript to run on the server.
- Frameworks like Electron enable full-stack applications using JavaScript.

### Code Example
Basic Node.js server example:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
```

### Explanation
- This code creates a simple HTTP server that responds with "Hello World" on port 3000.
