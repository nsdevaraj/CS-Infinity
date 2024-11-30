

### **2. Route Handlers in Next.js**

Route handlers in Next.js 
* allows you to create custom request handles for your app
* unlink page routes, which is respond with HTML content, route handlers allow to create RESTful endpoints
* Give full control over response without need of backend setup
* perfect for handling everything form submissions and db queries and secure interactions with third party apis
* By running server side, ensure sensitive info like api keys remain protected

---

#### **Key Concepts of Route Handlers**

1. **File-Based Routing for APIs**: Just like UI routes, API routes in Next.js are organized within the `app` folder.
2. **Route Handler Structure**: Each API endpoint is defined in a `route.ts` file within a folder named after the route.
3. **Server-Side Execution**: Route handlers run on the server, keeping sensitive data secure and allowing interaction with databases and third-party APIs.
4. **Supports HTTP Methods**: You can define handlers for `GET`, `POST`, `PUT`, and `DELETE` methods in a single `route.ts` file, making it easy to set up CRUD (Create, Read, Update, Delete) operations.



---


Route handler's behavior:
* every route handlers receives the standard web request object and context(from which we can get url param) as params

#### **Example 1: Setting Up a Basic API Route**

Create a route handler in `app/users/route.ts` that returns an array of users in JSON format. 

**Directory Structure**:

```plaintext
app/
└── users/
    └── route.ts   # API endpoint for /users
```

**Simple Code**:

```typescript
// app/users/route.ts
const users = [
  { id: 1, name: "John Doe" },
  { id: 2, name: "Jane Doe" },
];

export async function GET() {
  return new Response(JSON.stringify(users), {
    headers: { "Content-Type": "application/json" },
  });
}
```

**Usage**: A `GET` request to `http://localhost:3000/users` will return the list of users in JSON format.

here users are directly placed , but in real world, it come from DataBases.

---

#### **Example 2: Adding a POST Handler**

To add a user to the list, add a `POST` handler in `app/users/route.ts`:

```typescript
// app/users/route.ts
const users = [
  { id: 1, name: "John Doe" },
  { id: 2, name: "Jane Doe" },
];


export async function POST(request: Request) {
  const newUser = await request.json();
  newUser.id = users.length + 1;
  users.push(newUser);
  return new Response(JSON.stringify(newUser), {
    headers: { "Content-Type": "application/json" },
    status: 201, // 201 Created
  });
}
```

**Usage**: Send a `POST` request to `/users` with a JSON body (e.g., `{ "name": "Vishwas" }`) to add a new user. The response will return the new user with a status of 201 Created.

---

#### **Example 3: Dynamic Route for Individual Users**

For operations on individual users (e.g., `/users/:id`), create a dynamic route handler by adding `[id]/route.ts` inside the `users` folder.

**Directory Structure**:

```plaintext
app/
└── users/
    ├── route.ts           # /users
    └── [id]/
        └── route.ts       # /users/:id
```

**Simple Code**:

```typescript
// app/users/[id]/route.ts
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest, { params }) {
  const user = users.find(u => u.id === parseInt(params.id));
  if (!user) {
    return new Response("User not found", { status: 404 });
  }
  // or just return Response.json(user)
  return new Response(JSON.stringify(user), {
    headers: { "Content-Type": "application/json" },
  });
}
```

**Usage**: A `GET` request to `/users/1` returns the user with `id = 1`. If no user is found, a 404 response is returned.

---

#### **Example 4: Adding PUT and DELETE Handlers for Updating and Deleting Users**

To complete CRUD functionality, add `PUT` and `DELETE` methods within `[id]/route.ts`:

```typescript
// app/users/[id]/route.ts

// PUT: Update user
export async function PUT(request: Request, { params }) {
  const userIndex = users.findIndex(u => u.id === parseInt(params.id));
  if (userIndex === -1) {
    return new Response("User not found", { status: 404 });
  }
  const updatedUser = await request.json();
  users[userIndex] = { ...users[userIndex], ...updatedUser };
  return new Response(JSON.stringify(users[userIndex]), {
    headers: { "Content-Type": "application/json" },
  });
}

// DELETE: Remove user
export async function DELETE(request: Request, { params }) {
  const userIndex = users.findIndex(u => u.id === parseInt(params.id));
  if (userIndex === -1) {
    return new Response("User not found", { status: 404 });
  }
  users.splice(userIndex, 1);
  return new Response("User deleted", { status: 200 });
}
```

- **PUT**: Updates the user’s information based on `id`.
- **DELETE**: Removes a user based on `id`.

**Usage**:
- Use `PUT` to send updated data to `/users/:id` to modify a user’s info.
- Use `DELETE` to remove a user by sending a `DELETE` request to `/users/:id`.

---

### **Real-World Use Cases**

- **Form Submissions**: Using `POST` handlers, you can handle form submissions directly in Next.js, validating and processing data server-side.
- **Data Fetching from a Database**: Use route handlers to fetch, update, or delete data in a database (e.g., MongoDB, PostgreSQL) without needing a separate backend.
- **Secure API Calls**: Route handlers can securely call external APIs (e.g., third-party payment gateways) since they run server-side, keeping sensitive information secure.
- **Microservices**: API routes can serve as lightweight microservices for a Next.js application, handling tasks like product management, user data, and more directly within the app's structure.

