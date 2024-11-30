


### Setting Up Routes in Express.js

1. **Create a Route**:
   - Use `app.<HTTP_METHOD>` (get, post, put,  patch, delete , any http method) to define routes. 
     
     For example, to set up a GET route at the root path:
     
```javascript
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  console.log("Request received");
  res.send("Hi");
});

app.listen(3000, () => {
  console.log("server is listing");
});
```

2. **Parameters in the Callback**:
   - The callback function takes three parameters:
     - `req`: The request object.
     - `res`: The response object.
     - `next`: Used for middleware (often omitted).

3. **Sending a Response**:
   - Use `res.send()` to send data back to the client. For example:
     ```javascript
     res.send('Hi');
     ```

4. **Testing the Route**:
   - When you navigate to `http://localhost:3000`, the server logs the request and responds with "Hi".

5. 
---

Now you have a basic route set up in Express.js! This allows you to handle GET requests and respond accordingly. Let me know if you want to explore more features or additional routes!





