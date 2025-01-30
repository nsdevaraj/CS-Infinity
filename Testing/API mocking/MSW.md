Mock Service Worker is an API mocking library that allows you to write client-agnostic mocks and reuse them across any frameworks, tools, and environments.

https://mswjs.io/


When using **MSW (Mock Service Worker)** for **integration testing**, the main goal is to mock HTTP requests and responses in your application to simulate real-world API interactions. This is crucial for testing the behavior of your components without hitting actual APIs, allowing you to control and test various edge cases.

### **Key Topics to Explore for MSW in Integration Testing:**

#### **1. **Introduction to MSW (Mock Service Worker)**

- **What MSW is**: A tool for mocking API requests by intercepting network requests in the browser or Node.js and providing mock responses.
- **Why Use MSW**: For integration testing, MSW allows you to simulate various API responses (success, failure, empty data) without depending on external services, making tests more reliable and fast.

#### **2. **Setting Up MSW in Your Project**

- **Installation**:
    
    ```bash
    npm install msw --save-dev
    ```
    
- **Configuring MSW**: Set up a `worker` for the browser or a `server` for Node.js.
    - **For Browser (Service Worker)**:
        
        ```ts
        import { setupWorker, rest } from 'msw';
        
        const worker = setupWorker(
          rest.get('/api/user', (req, res, ctx) => {
            return res(ctx.status(200), ctx.json({ username: 'John Doe' }));
          })
        );
        
        worker.start();  // Start the worker to intercept requests
        ```
        
    - **For Node.js (Mocking in tests)**:
        
        ```ts
        import { setupServer, rest } from 'msw/node';
        
        const server = setupServer(
          rest.get('/api/user', (req, res, ctx) => {
            return res(ctx.status(200), ctx.json({ username: 'John Doe' }));
          })
        );
        
        server.listen();  // Start the server to mock requests
        ```
        

#### **3. **Using MSW for API Mocking in Tests**

- **Creating Mock Handlers**: MSW lets you create mock handlers for different HTTP methods (GET, POST, PUT, DELETE) and simulate various responses.
    - **Example**:
        
        ```ts
        const handlers = [
          rest.get('/api/user', (req, res, ctx) => {
            return res(ctx.status(200), ctx.json({ username: 'John Doe' }));
          }),
          rest.post('/api/login', (req, res, ctx) => {
            return res(ctx.status(200), ctx.json({ token: '12345' }));
          }),
        ];
        ```
        

#### **4. **Testing Different Response Scenarios**

- **Success Responses**: Mock successful API responses with specific data.
- **Error Responses**: Mock error scenarios (e.g., 500, 404 errors) to test how your app handles failures.
    - **Example**:
        
        ```ts
        rest.get('/api/user', (req, res, ctx) => {
          return res(ctx.status(500), ctx.json({ error: 'Internal Server Error' }));
        });
        ```
        
- **Empty or No Data**: Test cases where APIs return empty or null data.
- **Delayed Responses**: Mock delayed responses to simulate slow networks or timeouts.
    
    ```ts
    rest.get('/api/user', (req, res, ctx) => {
      return res(
        ctx.status(200),
        ctx.delay(500),  // Simulate network delay
        ctx.json({ username: 'John Doe' })
      );
    });
    ```
    

#### **5. **Integration with Test Frameworks (e.g., Jest, Vitest)**

- **Setting up MSW with Jest**: MSW works seamlessly with test frameworks like Jest or Vitest to mock API requests during tests.
    - **Example with Jest**:
        
        ```ts
        import { server } from './server';  // Your MSW server setup
        
        beforeAll(() => server.listen());  // Start mocking before tests
        afterEach(() => server.resetHandlers());  // Reset handlers after each test
        afterAll(() => server.close());  // Close the server after all tests
        ```
        

#### **6. **Handling Global State and Setup/Teardown**

- **Global Setup and Teardown**: Properly clean up after tests to avoid side effects from previous tests. This includes resetting handlers and stopping the worker/server after tests are done.
    
    ```ts
    afterEach(() => server.resetHandlers());  // Reset handlers after each test
    afterAll(() => server.close());  // Clean up after all tests
    ```
    

#### **7. **Testing UI Components with Mocked Data**

- **Testing Components that Fetch Data**: Use MSW to test how your UI components behave when they interact with a mocked API.
    - Example: If you have a React component that fetches user data:
        
        ```tsx
        const UserComponent = () => {
          const [user, setUser] = useState(null);
        
          useEffect(() => {
            fetch('/api/user')
              .then((res) => res.json())
              .then((data) => setUser(data));
          }, []);
        
          return <div>{user ? user.username : 'Loading...'}</div>;
        };
        ```
        
        In your test, mock the `/api/user` endpoint with MSW:
        
        ```ts
        import { render, screen } from '@testing-library/react';
        import { server } from './server'; // Your MSW server setup
        import { rest } from 'msw';
        
        test('should display username', async () => {
          server.use(
            rest.get('/api/user', (req, res, ctx) => {
              return res(ctx.status(200), ctx.json({ username: 'John Doe' }));
            })
          );
        
          render(<UserComponent />);
          
          expect(await screen.findByText('John Doe')).toBeInTheDocument();
        });
        ```
        

#### **8. **Handling Mocking Different Environments (Browser vs. Node.js)**

- **Browser Mode**: MSW uses the service worker to intercept network requests in the browser, making it perfect for frontend tests where you want to mock network calls without affecting actual API endpoints.
- **Node.js Mode**: In Node.js (for backend or testing), you use `setupServer` to mock the HTTP requests.

#### **9. **Combining MSW with Other Mocking Libraries**

- **MSW + Testing Libraries**: Combine MSW with other libraries (e.g., `jest-fetch-mock`, `axios-mock-adapter`) if needed, although MSW usually handles most scenarios without the need for other libraries.
- **Mocking GraphQL**: MSW also supports mocking GraphQL queries, providing flexibility if you're working with GraphQL APIs.

#### **10. **Error Handling and Customizing Responses**

- **Custom Response Handlers**: Customize mock responses to simulate a variety of edge cases (e.g., timeouts, unexpected data formats).
- **Error Handling in MSW**: Properly test how your application handles different response statuses and errors (like `500 Internal Server Error` or `404 Not Found`).

### **Key Points to Remember**:

- **Mocking APIs**: Use MSW to mock API endpoints and control response data for more predictable tests.
- **Simulating Different Scenarios**: Mock successful responses, errors, delays, and empty states to test how your application handles different real-world situations.
- **Testing UI Interactions**: MSW works seamlessly with UI testing tools like React Testing Library to simulate API interactions.
- **Setup/Teardown**: Ensure that MSW is properly started and cleaned up in your test setup and teardown to avoid side effects between tests.

By mastering these concepts, you'll be able to effectively use MSW to conduct integration testing, ensuring your application's behavior is thoroughly validated with various API scenarios.