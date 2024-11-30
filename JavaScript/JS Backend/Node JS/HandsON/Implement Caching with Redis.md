

### **Question 8: Implement Caching in Node.js with Redis**

**Problem:**  
Build an Express.js endpoint that fetches data from an external API and caches the response in Redis for 60 seconds. If a request is made within 60 seconds of the first fetch, serve the data from the cache instead of calling the external API again.

**Answer:**

```javascript
const express = require('express');
const axios = require('axios');
const redis = require('redis');

const app = express();
const redisClient = redis.createClient(); // Connect to Redis

// Handle Redis connection events
redisClient.on('error', (err) => console.error('Redis error:', err));

// External API URL (example: JSONPlaceholder)
const API_URL = 'https://jsonplaceholder.typicode.com/posts';

// Endpoint with caching
app.get('/data', async (req, res) => {
  try {
   
    // cachekey can get from request
    const cacheKey = 'api-data';

    // Check if data is in the cache
    redisClient.get(cacheKey, async (err, cachedData) => {
      if (err) throw err;

      if (cachedData) {
        console.log('Serving from cache');
        return res.json(JSON.parse(cachedData)); // Serve cached response
      }

      console.log('Fetching from API');
      const response = await axios.get(API_URL);
      const data = response.data;

      // Store API response in Redis with 60-second expiration
      redisClient.setex(cacheKey, 60, JSON.stringify(data));
      res.json(data);
    });
  } catch (error) {
    console.error('Error fetching data:', error);
    res.status(500).send('Server error');
  }
});

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

**Explanation:**

1. **Redis Integration:**
    
    - `redis.createClient()` connects to the Redis server.
    - `redisClient.get()` checks for cached data.
    - `redisClient.setex()` caches the API response with a 60-second expiration.
2. **API Caching Logic:**
    
    - If cached data exists, it’s served immediately, avoiding a call to the external API.
    - If no cache is found, the API is called, and the result is cached.
3. **Testing:**
    
    - First request triggers an API call.
    - Subsequent requests within 60 seconds serve the cached response.
4. **Dependencies:**  
    Install Redis and the necessary libraries:
    
    ```bash
    npm install axios redis
    ```
    

**Example Test Output:**

- **First Request:** Logs _"Fetching from API"_ and serves fresh data.
- **Subsequent Requests:** Logs _"Serving from cache"_ and serves cached data.

Let me know when you're ready for the next one!