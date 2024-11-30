

### **Question 9: Implement JWT Authentication in Node.js**

**Problem:**  
Create an Express.js application with a route for user login. Upon successful login, generate a JWT (JSON Web Token) and return it in the response. Protect a `/profile` route using JWT authentication, ensuring that only requests with a valid token can access the profile information.

**Answer:**

Here’s how you can implement JWT authentication:

1. **Install the required packages:**
    
    ```bash
    npm install express jsonwebtoken bcryptjs
    ```
    
2. **Create the Express app with JWT authentication:**
    

```javascript
const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

const app = express();
const secretKey = 'yourSecretKey'; // Secret key for JWT signing

// In-memory user store (for demonstration)
const users = [
  { id: 1, username: 'user1', password: '$2a$10$KIXK7AfUtMj9Zk3j/jHzm.0MjgCKg1uQfI0REi6Ot2zVndm5hBvsy' }, // password: password123
];

// Middleware to parse JSON bodies
app.use(express.json());

// Route for user login
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  const user = users.find(u => u.username === username);
  if (!user) {
    return res.status(401).send('Invalid username or password');
  }

  // Compare provided password with stored hash
  bcrypt.compare(password, user.password, (err, isMatch) => {
    if (err || !isMatch) {
      return res.status(401).send('Invalid username or password');
    }

    // Generate JWT
    const token = jwt.sign({ userId: user.id, username: user.username }, secretKey, { expiresIn: '1h' });
    res.json({ token });
  });
});

// Middleware to verify JWT
const authenticateJWT = (req, res, next) => {
  const token = req.header('Authorization')?.replace('Bearer ', '');
  if (!token) {
    return res.status(403).send('Access denied. No token provided.');
  }

  jwt.verify(token, secretKey, (err, user) => {
    if (err) {
      return res.status(403).send('Invalid token');
    }
    req.user = user;
    next();
  });
};

// Protected route: /profile
app.get('/profile', authenticateJWT, (req, res) => {
  res.json({
    message: 'Welcome to your profile!',
    user: req.user,
  });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

**Explanation:**

1. **User Login:**
    
    - The `POST /login` route accepts the `username` and `password` in the request body.
    - The password is compared using `bcrypt.compare` to check if the login credentials are valid.
    - If valid, a JWT token is generated using `jsonwebtoken` (`jwt.sign`) and returned in the response.
2. **JWT Authentication Middleware:**
    
    - The `authenticateJWT` middleware checks for the presence of a `Bearer` token in the `Authorization` header of requests.
    - If the token is valid, the request proceeds to the protected route. If not, it returns a `403 Forbidden` response.
3. **Protected Route (`/profile`):**
    
    - This route is protected and only accessible if the request contains a valid JWT token in the header.

**Testing:**

1. **Login Request:**
    
    - `POST /login` with a body like:
        
        ```json
        {
          "username": "user1",
          "password": "password123"
        }
        ```
        
    - Response:
        
        ```json
        {
          "token": "JWT_TOKEN_HERE"
        }
        ```
        
2. **Accessing Protected Route:**
    
    - `GET /profile` with `Authorization: Bearer JWT_TOKEN_HERE`.
    - Response (if the token is valid):
        
        ```json
        {
          "message": "Welcome to your profile!",
          "user": { "userId": 1, "username": "user1" }
        }
        ```
        

Let me know when you're ready for the final question!

