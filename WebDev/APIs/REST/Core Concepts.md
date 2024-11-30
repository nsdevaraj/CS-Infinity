

1. **What is REST (Representational State Transfer)?**
   - **Definition**: An architectural style for designing networked applications using HTTP.
   - **Key Principles**: Stateless, client-server architecture, uniform interface, cacheable, layered system, and code on demand (optional).
   - **Resource-Oriented**: Resources are identified by URLs and represented using standard HTTP methods (GET, POST, PUT, DELETE).



#### 1. **What are REST and RESTful APIs?**
   - **REST (Representational State Transfer)** is an architectural style for designing network applications.
   - **RESTful API** refers to an API that adheres to REST principles like statelessness, client-server architecture, and uniform interfaces.
   
   **Key Points**:
   - REST uses HTTP for communication.
   - RESTful APIs transfer data in JSON or XML format.
   - Example flow:
     - Client (browser) sends a request.
     - Server processes data and responds.

   **Example**:
   ```bash
   GET /users
   ```




#### 2. **What is the Difference Between REST API and SOAP API?**
   - **REST API** is an architectural style using HTTP and is lightweight.
   - **SOAP API** is a protocol and uses XML for communication, can use multiple protocols (e.g., HTTP, SMTP).
   
   **Key Differences**:
   - REST is stateless, SOAP can be stateful.
   - REST uses HTTP status codes (e.g., 200 OK), SOAP uses custom error codes.
   - REST is faster, SOAP can be slower due to XML processing.





2. **HTTP Methods**:
   - **GET**: Retrieves data from the server.
   - **POST**: Sends data to the server (typically to create a new resource).
   - **PUT**: Updates an existing resource or creates a new one if it doesn't exist.
   - **DELETE**: Removes a resource.
   - **PATCH**: Partially updates a resource.



#### 3. **What are HTTP Methods (Verbs) in RESTful APIs?**
   - **HTTP Methods** represent actions for a resource in a REST API.

   **Methods**:
   - **GET**: Retrieves data.
     - Example: `GET /users` - Fetches all users.
   - **POST**: Sends data to create a resource.
     - Example: `POST /users` - Adds a new user.
   - **PUT**: Updates or creates a resource.
     - Example: `PUT /users/1` - Updates user with ID 1.
   - **DELETE**: Deletes a resource.
     - Example: `DELETE /users/1` - Deletes user with ID 1.



#### 4. **What is the Difference Between PUT and PATCH Methods?**
   - **PUT** replaces the entire resource.
     - Example: `PUT /users/1` - Replaces the entire data of user with ID 1.
   - **PATCH** updates only the provided fields (partial update).
     - Example: `PATCH /users/1` - Updates only the fields like email, not the entire resource.

   **Difference**: PUT is complete replacement, PATCH is partial.




3. **Statelessness**:
   - **Definition**: Each API call is independent; the server does not store client context between requests.
   - **Implication**: Every request must contain all the information needed to process the request.

4. **Endpoints**:
   - **Definition**: Specific paths/URLs to access resources (e.g., `/users`, `/products/{id}`).
   - **Best Practice**: Use plural nouns for resource names (e.g., `/users`, `/posts`).

5. **Request and Response Formats**:
   - **JSON**: Most common format for data exchange in REST APIs.
   - **XML**: An alternative format for data exchange, though less common than JSON.

6. **Status Codes**:
   - **2xx**: Success (e.g., 200 OK, 201 Created).
   - **4xx**: Client errors (e.g., 400 Bad Request, 401 Unauthorized, 404 Not Found).
   - **5xx**: Server errors (e.g., 500 Internal Server Error).


#### 6. **What is the Role of HTTP Status Codes in RESTful APIs?**
   - **HTTP Status Codes** convey the result of a client request.

   **Common Codes**:
   - **200 OK**: Successful request.
   - **201 Created**: Successful resource creation.
   - **400 Bad Request**: Client error (e.g., malformed request).
   - **401 Unauthorized**: Authentication required.
   - **404 Not Found**: Resource not found.
   - **500 Internal Server Error**: Server error.

#### 10. **What is the Difference Between 4xx and 5xx HTTP Status Codes?**
   - **4xx (Client Errors)**: The request is invalid, often due to the client sending wrong data.
     - Example: `400 Bad Request`, `401 Unauthorized`, `404 Not Found`.
   - **5xx (Server Errors)**: The server failed to fulfill a valid request.
     - Example: `500 Internal Server Error`.


---


