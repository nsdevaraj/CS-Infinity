### **Section 2: REST API Best Practices**

1. **Resource Naming Conventions**:
   - **Use Plural Nouns**: `/users`, `/posts`, not `/user`, `/post`.
   - **Use Nested Resources for Hierarchical Data**: `/users/{userId}/posts` for related resources.

2. **Versioning**:
   - **In the URL**: `/v1/users`, `/v2/products`.
   - **In HTTP Headers**: `Accept: application/vnd.myapi.v1+json`.

3. **Authentication & Authorization**:
   - **Basic Authentication**: Username/Password sent in headers.
   - **OAuth**: Secure authorization using access tokens (more common for public APIs).
   - **API Keys**: Another method of authentication (typically for service-to-service calls).


#### 9. **What is Token-Based Authentication and JWT Authentication?**
   - **Token-Based Authentication** uses a token to verify the identity of a user.
   - **JWT (JSON Web Token)** is a popular method for token-based authentication.

   **JWT Authentication Process**:
   1. **User logs in** by sending credentials (`username`, `password`).
   2. **Server validates** credentials, issues a **JWT token**.
   3. **Client stores** the token (local storage/cookies).
   4. For **subsequent requests**, the token is sent in the `Authorization` header.
   
   **Example**:
   ```bash
   Authorization: Bearer <JWT_Token>
   ```



#### **8. How would you implement authentication in REST APIs?**
   - **Answer**: Authentication can be handled using:
     - **Basic Authentication**: Sending credentials with every request (less secure).
     - **OAuth**: Token-based authentication (more secure, widely used in public APIs).
     - **API Keys**: Simple key-based access.


1. **Rate Limiting**:
   - **Definition**: Limiting the number of requests a client can make to prevent abuse and ensure service availability.
   - **Common Method**: Return headers like `X-Rate-Limit` to indicate request limits and remaining attempts.

2. **Error Handling**:
   - **Standardized Error Responses**: Provide clear error messages in a consistent format.
     - Example: `{ "error": "Invalid input", "message": "The 'name' field is required." }`
   - **Use Appropriate Status Codes**: Match the HTTP status code to the type of error (e.g., `400 Bad Request` for invalid input).

3. **CORS (Cross-Origin Resource Sharing)**:
   - **Definition**: A mechanism that allows web pages to request resources from a different domain.
   - **Use Case**: Prevents cross-origin requests unless explicitly allowed by the server.



#### 7. **What is CORS in RESTful APIs?**
   - **CORS (Cross-Origin Resource Sharing)** is a browser security feature that prevents web pages from making requests to a domain different from the one that served the web page.
   
   **Example**:
   - If your website is hosted on `www.example.com`, and you try to fetch data from `www.api.com`, CORS will block it unless allowed by the server.

   **Allowing CORS**:
   ```javascript
   app.use((req, res, next) => {
       res.header('Access-Control-Allow-Origin', '*');
       next();
   });
   ```

 
---



