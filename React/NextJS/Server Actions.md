


### **1. Introduction to Server Actions in Next.js**

Server Actions in Next.js 
*  asynchronous functions executed on the server. 
* They allow us to define and run server-side logic directly from our components, which is useful for: 
	* Handling form submissions
	- Updating databases or performing backend operations securely

Unlike traditional client-side actions, Server Actions keep sensitive data secure, as everything is executed on the server side.

---

### **2. Setting Up Mock API for Testing Server Actions**

To demonstrate updating data, we’ll use [MockAPI](https://mockapi.io/) as it allows us to simulate a backend with the ability to add or modify data. Follow these steps to set up MockAPI:

1. **Create an Account and Project**:
   - Go to MockAPI, create a new account, and set up a project called “NextJS.”

2. **Set Up a Resource**:
   - In your project, add a new resource called “Users” with just two fields: `id` and `name`.
   - Remove unnecessary fields, like `createdAt` and `avatar`.

3. **Generate Sample Data**:
   - Set the resource to generate 25 users with only `id` and `name` properties.
   - This will provide a mock API endpoint to fetch, add, or update users.

---

### **3. Fetching and Displaying Data with a Server Component**

First, create a server component to fetch and display users.

#### **File Structure**:

```plaintext
app/
└── mock-users/
    └── page.tsx
```

#### **Code for `page.tsx`**:

```typescript
// Define a User type
type User = {
  id: number;
  name: string;
};

export default async function MockUsers() {
  const response = await fetch("https://mockapi.io/projects/YOUR_PROJECT_ID/users");
  if (!response.ok) throw new Error("Failed to fetch users");

  const users: User[] = await response.json();

  return (
    <div className="p-4">
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

#### **Explanation**:
- This component fetches and displays the list of users from the MockAPI endpoint.
- Replace `"YOUR_PROJECT_ID"` with your actual project ID from MockAPI.

---

### **4. Adding a Form to Create New Users**

Next, we’ll add a form to the component to allow adding new users.

#### **Updating `page.tsx`**:

Add an input form for the user’s name and a submit button.

```typescript
export default async function MockUsers() {
  const response = await fetch("https://mockapi.io/projects/YOUR_PROJECT_ID/users");
  const users: User[] = await response.json();

  return (
    <div className="p-4">
      {/* Form to add a new user */}
      <form action={addUser} className="mb-4">
        <input
          type="text"
          name="name"
          required
          placeholder="Enter user's name"
          className="border px-2 py-1 mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-1">Add User</button>
      </form>

      {/* Displaying users */}
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

---

### **5. Defining the Server Action for Form Submission**

To securely add a new user, define a **Server Action** that will handle the form submission on the server.

#### **Code for Server Action**:

```typescript
"use server"; // Marks this function to run on the server

async function addUser(formData: FormData) {
  const name = formData.get("name") as string;

  // Post request to add user to MockAPI
  const response = await fetch("https://mockapi.io/projects/YOUR_PROJECT_ID/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name }),
  });

  if (!response.ok) throw new Error("Failed to add user");

  // Optional: Log the new user object for verification
  const newUser = await response.json();
  console.log(newUser);
}
```

#### **Explanation**:
- `addUser` is a Server Action function, triggered by the form submission.
- It securely sends a POST request to MockAPI to add a new user.
- **Security Advantage**: The fetch request is executed server-side, keeping any private keys or sensitive headers secure.

---

### **6. Automatically Updating the User List**

When a new user is added, we want the page to update automatically without requiring a refresh. We achieve this by revalidating the path using `revalidatePath`.

#### **Updating `addUser` Function**:

```typescript
import { revalidatePath } from "next/cache";

async function addUser(formData: FormData) {
  const name = formData.get("name") as string;

  const response = await fetch("https://mockapi.io/projects/YOUR_PROJECT_ID/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name }),
  });

  if (!response.ok) throw new Error("Failed to add user");

  // Revalidate the path to show the newly added user immediately
  revalidatePath("/mock-users");
}
```

#### **Explanation**:
- `revalidatePath` tells Next.js to re-fetch data for the `/mock-users` path, instantly showing the newly added user without needing a page refresh.

---

### **7. Testing the Form Submission and Auto-Update**

1. **Navigate to `/mock-users`**:
   - You should see the list of users and a form to add a new user.

2. **Add a User**:
   - Enter a name and click **Add User**.
   - The new user should appear in the list instantly, thanks to the `revalidatePath` function.

---

### **8. Key Advantages of Using Server Actions**

- **Security**: Sensitive data, like API keys, remain server-side.
- **Automatic Revalidation**: Next.js can update the UI immediately after data changes.
- **Seamless Integration**: Server Actions work directly within components, simplifying the flow of data management.

---


if this done in client side, we need to refetch and update or direct-update ( which may have old data unchanged even its changed in backend ):

```js
import { useState, useEffect } from "react";

type User = {
  id: number;
  name: string;
};

export default function UsersPage() {
  const [users, setUsers] = useState<User[]>([]);
  const [newUserName, setNewUserName] = useState("");
  const [loading, setLoading] = useState(false);

  // Fetch users on component mount
  useEffect(() => {
    async function fetchUsers() {
      setLoading(true);
      const response = await fetch("https://mockapi.io/projects/YOUR_PROJECT_ID/users");
      const data = await response.json();
      setUsers(data);
      setLoading(false);
    }
    fetchUsers();
  }, []);

  // Handle form submission
  const handleAddUser = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newUserName) return; // Don't submit if name is empty

    // Make POST request to add new user
    const response = await fetch("https://mockapi.io/projects/YOUR_PROJECT_ID/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: newUserName }),
    });

    if (response.ok) {
      const newUser = await response.json();
      setUsers((prevUsers) => [...prevUsers, newUser]); // Update UI immediately
      setNewUserName(""); // Clear input field
    } else {
      alert("Failed to add user");
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Users List</h1>

      {/* Add New User Form */}
      <form onSubmit={handleAddUser} className="my-4">
        <input
          type="text"
          value={newUserName}
          onChange={(e) => setNewUserName(e.target.value)}
          placeholder="Enter user name"
          className="border px-2 py-1 mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-1">Add User</button>
      </form>

      {/* Display List of Users */}
      {loading ? (
        <p>Loading users...</p>
      ) : (
        <ul>
          {users.map((user) => (
            <li key={user.id}>{user.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

```

#### Benefits of Client side Approach**:

- **Real-time Update**: The UI updates immediately after the form is submitted without requiring a page refresh.
- **Client-Side Execution**: The entire process happens on the client side, making the code simple and quick to implement.
- **Direct Interaction**: No server-side logic needed; everything is managed within the React component.
