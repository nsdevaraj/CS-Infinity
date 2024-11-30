


### **Question 1: Implement a Custom Middleware in Express**

**Problem:**  
Create a custom middleware in an Express.js application that logs the HTTP method and URL of each request, and restricts access to a specific route based on a custom header value. For example, if the custom header `x-custom-header` is not set to `allow`, deny access to the `/secure` route with a `403 Forbidden` response.

**Answer:**  
Here’s a step-by-step implementation:

```javascript
const express = require('express');
const app = express();

// Custom middleware
const customMiddleware = (req, res, next) => {
  console.log(`HTTP Method: ${req.method}, URL: ${req.url}`);

  if (req.url === '/secure') {
    const headerValue = req.headers['x-custom-header'];
    if (headerValue !== 'allow') {
      return res.status(403).send('Forbidden: Access Denied');
    }
  }

  next();
};

// Use the middleware
app.use(customMiddleware);

// Routes
app.get('/', (req, res) => {
  res.send('Home Route');
});

app.get('/secure', (req, res) => {
  res.send('Secure Route Accessed');
});

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

**Explanation:**

- Middleware logs the HTTP method and URL for each request.
- For the `/secure` route, the middleware checks the `x-custom-header` value.
- If the header value isn’t `allow`, the request is denied with a `403 Forbidden` response.
- If the header value is valid, the request proceeds to the route handler.

Ask for the next question when ready!