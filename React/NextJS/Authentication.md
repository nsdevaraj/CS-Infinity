
### Authentication with Clerk in Next.js - Step-by-Step Breakdown

In this guide, we'll walk through how to implement authentication with **Clerk** in a **Next.js** application. This will include user sign-up, sign-in, managing account information, and protecting routes based on authentication status, show ui elements based on auth status, read session and user data, sign out


### **Steps to Set Up Authentication with Clerk**

---

### 1. **Set Up Clerk Account**
1. Go to [Clerk](https://clerk.com) and create an account.
2. Create a new application (e.g., **Next.js App**).
3. Choose the authentication methods you want to support (e.g., Email & Password, Google, GitHub).
4. Copy your **API Keys** from Clerk for use in your Next.js app.

---

### 2. **Install Clerk Package**
Run the following command to install Clerk's Next.js SDK:
```bash
npm install @clerk/nextjs
```

---

### 3. **Set Up Environment Variables**

Create a `.env.local` file in the root of your project and add your **Clerk API Keys**:
```plaintext
NEXT_PUBLIC_CLERK_FRONTEND_API=your_clerk_frontend_api
CLERK_API_KEY=your_clerk_secret_key
```

---

### 4. **Middleware Configuration**
Create a `middleware.ts` file in the `src` folder to handle Clerk's authentication middleware for route protection.


1. By default, `clerkMiddleware()` will not protect any routes. All routes are public and you must opt-in to protection for routes. See the [`clerkMiddleware()` reference](https://clerk.com/docs/references/nextjs/clerk-middleware) to learn how to require authentication for specific routes.



```ts
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```


---

### 5. **Wrap Your Application with Clerk Provider**

In your `app/layout.tsx` file, import and wrap the `ClerkProvider` to provide Clerk's context to the app:

```tsx
import { ClerkProvider } from '@clerk/nextjs';
import { useRouter } from 'next/router';
import { ClerkLoaded, RedirectToSignIn } from '@clerk/nextjs';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider>
      <ClerkLoaded>
        <div>
          {children}
        </div>
      </ClerkLoaded>
    </ClerkProvider>
  );
}
```

---

### 6. **Creating the Navigation with Sign In/Sign Out Buttons**

In `components/navigation.tsx`, implement the `SignInButton` and `UserButton` components from Clerk:

```tsx
import { SignInButton, UserButton, SignedIn, SignedOut } from '@clerk/nextjs';

export default function Navigation() {
  return (
    <nav>
      {/* Display sign-in button if the user is not authenticated */}
      <SignedOut>
        <SignInButton mode="modal" />
      </SignedOut>

      {/* Display user button if the user is authenticated */}
      <SignedIn>
        <UserButton />
      </SignedIn>
    </nav>
  );
}
```

- `SignedOut`: Displays the `SignInButton` only when the user is not signed in.
- `SignedIn`: Displays the `UserButton` when the user is signed in.

---

### 7. **Protecting Routes Based on Authentication Status**

In `middleware.ts`, protect specific routes (like `/mock-users`) by adding a condition to check if the user is authenticated:

```ts
import { ClerkMiddlewareOptions } from '@clerk/nextjs/server';

export default withClerkMiddleware({
  publicRoutes: ['/login', '/signup'], 
  protectedRoutes: ['/mock-users'], // Protect this route
});
```




```ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isProtectedRoute = createRouteMatcher(['/mock-users']);

export default clerkMiddleware(async(auth, req)=>{
	if(isProtectedRoute(req)) await auth.protect(); // direct to sign in page
});

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```



- Any user who tries to access `/mock-users` while not signed in will be redirected to the sign-in page.

---

### 8. **Reading User Session Data**

To read the session data (user details) on the server side, use `currentUser` from Clerk. For client-side, use `useUser` and `useAuth` hooks.

#### **Server-Side:**

In `pages/mock-users.tsx` or another server component:

```tsx
import { currentUser } from '@clerk/nextjs/server';

export default async function MockUsersPage() {
  const user = await currentUser();
  console.log(user); // Logs the current user data
  return <div>Welcome, {user?.firstName}</div>;
}
```

#### **Client-Side:**

In a client component (`components/Counter.tsx`):

```tsx
import { useUser, useAuth } from '@clerk/nextjs';

export default function Counter() {
  const { user, isSignedIn } = useUser();
  const {isLoaded, userId, sessionId, getToken} = useAuth()
  
  if (!isSignedIn) return null; // Render nothing if the user is not signed in
  if(!isLoaded || !userId) return null;
  
  return (
    <div>
      <h1>Welcome {user?.firstName}</h1>
      {/* Display other content */}
    </div>
  );
}
```

- `useUser`: A hook for accessing user information on the client-side.
- `useAuth`: A hook that provides authentication status.

---

### 9. **Sign-In, Sign-Up, and Sign-Out Flow**

1. **Sign-In**: Use the `SignInButton` to allow users to sign in with the authentication method chosen during setup.
2. **Sign-Up**: The same `SignInButton` will also open the sign-up modal for new users.
3. **Sign-Out**: The `UserButton` allows users to manage their account or sign out.

Example for `SignInButton` and `UserButton`:

```tsx
import { SignInButton, UserButton } from '@clerk/nextjs';

export default function Navigation() {
  return (
    <nav>
      <SignedOut>
        <SignInButton mode="modal" />
      </SignedOut>
      <SignedIn>
        <UserButton />
      </SignedIn>
    </nav>
  );
}
```

---

### 10. **Managing User Data**

To manage the account, users can access profile information using the **User Button**. You can also integrate a custom form to update user data if needed.

#### Example of a custom user settings form:
```tsx
import { useUser } from '@clerk/nextjs';

export default function UserSettings() {
  const { user } = useUser();
  
  const handleUpdateProfile = () => {
    // Custom form handling code here
  };
  
  return (
    <div>
      <h2>Update Profile</h2>
      <input
        type="text"
        defaultValue={user?.firstName}
        // Add onChange handler to update the user data
      />
      <button onClick={handleUpdateProfile}>Save</button>
    </div>
  );
}
```

---

### **Summary**

By following these steps, you will:
- Integrate Clerk for authentication in a Next.js application.
- Allow users to sign up, sign in, and manage their accounts.
- Use middleware to protect routes based on the user's authentication status.
- Conditionally render UI elements based on authentication status.
- Access user data both server-side and client-side with Clerk's hooks.

Clerk simplifies authentication tasks, making it much easier to focus on building your app's features.


