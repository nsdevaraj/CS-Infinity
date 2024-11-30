

### **Question 4: Implement a Rate Limiter in Node.js**

**Problem:**  
Write a middleware function for an Express.js application that rate-limits API requests. Allow a maximum of 5 requests per minute per user, identified by their IP address. Return a `429 Too Many Requests` response if the limit is exceeded.

**Answer:**  
Here’s the implementation:

```javascript
const express = require('express');
const app = express();

// In-memory store for rate limiting (not suitable for production-scale apps)
const rateLimitStore = {};

// Middleware function
const rateLimiter = (req, res, next) => {
  const userIP = req.ip;
  const currentTime = Date.now();

  if (!rateLimitStore[userIP]) {
    rateLimitStore[userIP] = [];
  }

  // Remove timestamps older than 1 minute
  rateLimitStore[userIP] = rateLimitStore[userIP].filter(
    (timestamp) => currentTime - timestamp < 60 * 1000
  );

  if (rateLimitStore[userIP].length >= 5) {
    return res.status(429).send('Too Many Requests. Try again later.');
  }

  // Log the request timestamp and allow the request
  rateLimitStore[userIP].push(currentTime);
  next();
};

// Apply middleware to all routes
app.use(rateLimiter);

// Routes
app.get('/', (req, res) => res.send('Welcome to the API'));
app.get('/data', (req, res) => res.send('Here is your data'));

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

**Explanation:**

1. **Rate-Limit Store:** A simple in-memory object tracks request timestamps for each user (by IP).
2. **Request Validation:** Requests older than 1 minute are discarded, and only the last 5 requests are considered.
3. **Response Handling:** If the user exceeds the limit, a `429 Too Many Requests` response is sent.
4. **Scalability Note:** For production, use a distributed store like Redis to track request counts.

**Testing:**  
Use a tool like Postman or `curl` to make repeated requests from the same IP to observe rate limiting.

Ready for the next question?

