

* file system based routing mechanism
* organize files and folder determines app



---

## **1. File-Based Routing with the App Router**

   - **File-Based Structure**: In Next.js 15, routing is structured around the filesystem within the `app` folder.
   - **Conventions**:
     1. **All routes** should be inside the `app` folder.
     2. **File Naming**: Each route file must be named `page.js` or `page.tsx`.
     3. **Path Segments**: Each folder under `app` represents a segment in the browser URL.

   - **Example**: The `page.tsx` file directly within the `app` folder corresponds to the root route (`/`), and other routes are created by adding folders with a `page.tsx` file inside each.
   - export react component as default in `page file` , the page file is unique to specific route.. 


   ```bash
   app/
   ├── page.tsx          # Root route (/)
   ├── about/
   │   └── page.tsx      # /about
   └── contact/
       └── page.tsx      # /contact
   ```

   ```tsx
   // app/page.tsx (Root route)
   export default function HomePage() {
       return <h1>Welcome to the Home Page</h1>;
   }

   // app/about/page.tsx
   export default function AboutPage() {
       return <h1>About Us</h1>;
   }
   ```

   - **In Action**: Navigating to `http://localhost:3000/about` will load the `AboutPage` component, thanks to the folder structure and file naming convention.


---

### **2. Nested Routes**

   - **Concept**: Next.js allows for **nested routes** by creating a nested folder structure within `app`.
   - **Example**: To create a route like `/blog/first-post`, create a `blog` folder, then a `first-post` folder inside it, and place a `page.tsx` file within.

   ```bash
   app/
   └── blog/
       └── first-post/
           └── page.tsx  # /blog/first-post
   ```

   ```tsx
   // app/blog/first-post/page.tsx
   export default function FirstPost() {
       return <h1>First Blog Post</h1>;
   }
   ```

   - **Explanation**: The `page.tsx` file inside `blog/first-post` represents the nested route `/blog/first-post`. This structure is suitable for routes representing hierarchical content, like blog articles.

---

### **3. Dynamic Routes**

   - **Dynamic Segment**: To create routes with dynamic segments (e.g., `/products/[id]`), wrap folder names in square brackets.
   - **Parameter Handling**: Components receive `params` as a prop, allowing access to the dynamic segment.
   - Page component directly gets route params as props 
   - in nextjs 15, dynamic route params have been made asynchronous .. so func must be async... 


   ```bash
   app/
   └── products/
       └── [id]/
           └── page.tsx  # /products/[id]
   ```

   ```tsx
   // app/products/[id]/page.tsx
   export default async function ProductPage({ params }) {
       const { id } = await params;
       return <h1>Product ID: {id}</h1>;
   }
   ```

   - **Explanation**: In this example, visiting `/products/123` will render `ProductPage` with `id` dynamically set to `123`. This is useful for cases like individual product pages on an e-commerce site.

---

### **4. Route Groups**

   - **Grouping without URL Change**: Next.js 15 introduces **route groups**, allowing you to organize routes logically without affecting the URL structure. Wrap group folder names in parentheses.`(folderName)`
   - **Example**: A group folder called `(auth)` organizes authentication routes like `/register`, `/login`, and `/forgot-password`.

   ```bash
   app/
   └── (auth)/
       ├── login/
       │   └── page.tsx      # /login
       ├── register/
       │   └── page.tsx      # /register
       └── forgot-password/
           └── page.tsx      # /forgot-password
   ```

   ```tsx
   // app/(auth)/login/page.tsx
   export default function LoginPage() {
       return <h1>Login</h1>;
   }
   ```

   - **Explanation**: Route grouping here helps organize authentication routes in the codebase without affecting URLs. This keeps routes tidy, especially in larger applications.

---

### **5. Layouts**

   - **Root Layout**: Define a **root layout** in `app/layout.tsx` to wrap all pages with shared UI elements (like headers or footers).
   - **Nested Layouts**: Add a `layout.tsx` within specific folders to create layout variations for nested routes (e.g., a product-specific layout).
   - same like page file, layout file also need to  default export func of react component
   - it will get `children` params, which is basically the route's page components.. 

   ```bash
   app/
   ├── layout.tsx           # Root layout
   └── products/
       ├── layout.tsx       # Product-specific layout
       └── [id]/
           └── page.tsx     # Product details
   ```

   ```tsx
   // app/layout.tsx
   export default function RootLayout({ children }) {
       return (
           <html>
               <body>
                   <header>Site Header</header>
                   {children}
                   <footer>Site Footer</footer>
               </body>
           </html>
       );
   }

   // app/products/layout.tsx
   export default function ProductLayout({ children }) {
       return (
           <div>
               <h2>Featured Products</h2>
               {children}
           </div>
       );
   }
   ```

   - **Explanation**: The root layout (`layout.tsx`) applies globally, while the `ProductLayout` wraps only product-specific pages with additional features, like a featured products section.


Why layout useful:
* allow define UI shared between multiple pages
* useful elements like headers, footers or navigation menus - appear consistently across different routers
* when navigation between pages that share a layout, only page components update - the layout doesn't re-render
* improved performance and smoother user experience since no unnecessary re-renders
* help to reduce code duplication and improve overall structure of project







### **Section 2: Routing in Next.js**

#### **1. How does Next.js handle routing?**

Next.js uses **file-based routing**, where the file structure under the `pages` directory defines the routes.

- A file `pages/about.js` maps to `/about`.
- Dynamic routes are created using brackets, e.g., `pages/blog/[id].js` maps to `/blog/:id`.

---

#### **2. What are dynamic routes in Next.js? How are they implemented?**

Dynamic routes allow you to define routes with parameters. They are created by using square brackets in the file name:

- Example: `pages/product/[id].js` maps to `/product/:id`.

**Accessing parameters:**

- Use `useRouter` hook: `const { query } = useRouter(); console.log(query.id);`
- Server-side functions (e.g., `getStaticProps` or `getServerSideProps`) receive params as part of the argument: `params.id`.

---

#### **3. Explain how API routes work in Next.js.**

API routes in Next.js allow you to create server-side endpoints within your application. These are defined in the `pages/api` directory.

**Example:**  
A file `pages/api/hello.js`:

```javascript
export default function handler(req, res) {
  res.status(200).json({ message: "Hello, Next.js!" });
}
```

This creates an endpoint at `/api/hello`.

**Key Points:**

- Supports HTTP methods (`GET`, `POST`, etc.).
- Useful for integrating backend logic directly in the app.
- Runs on the server, not the client.

---

#### **4. What are catch-all routes? How do they differ from optional catch-all routes?**

- **Catch-all Routes:** Use `[...slug].js` to capture multiple segments. For example, `pages/blog/[...slug].js` matches `/blog/a`, `/blog/a/b`, etc. The `slug` parameter is an array (`[a]`, `[a, b]`).
- **Optional Catch-all Routes:** Use `[[...slug]].js`. If no segments are provided, the route still matches, e.g., `/blog`.


### Catch-all Routes in Next.js

In Next.js, **catch-all routes** are a way to capture dynamic segments of a URL path, meaning they match multiple possible URL patterns. They are useful when you need to handle several routes under a single file without explicitly defining each one.

#### **Catch-all Routes:**

A **catch-all route** is defined using square brackets `[]` and an ellipsis `...` in the file name. This allows it to match any number of URL segments.

Example:

```js
// pages/[...slug].js

import { useRouter } from 'next/router';

const CatchAllRoute = () => {
  const router = useRouter();
  const { slug } = router.query;

  return (
    <div>
      <h1>Catch-all Route</h1>
      <p>Matched Path: {slug?.join(' / ')}</p>
    </div>
  );
};

export default CatchAllRoute;
```

**Explanation:**

- The `slug` will capture everything after the base path, and it's available as an array.
- For the URL `/a/b/c`, `slug` would be `['a', 'b', 'c']`.

#### **Optional Catch-all Routes:**

An **optional catch-all route** is similar but allows you to define optional segments in the URL. This means it can match both the case where there are extra segments and the case where there aren't.

It is defined by adding a question mark `?` to the catch-all route.

Example:

```js
// pages/[[...slug]].js

import { useRouter } from 'next/router';

const OptionalCatchAllRoute = () => {
  const router = useRouter();
  const { slug } = router.query;

  return (
    <div>
      <h1>Optional Catch-all Route</h1>
      <p>Matched Path: {slug ? slug.join(' / ') : 'No path segments'}</p>
    </div>
  );
};

export default OptionalCatchAllRoute;
```

**Explanation:**

- The route matches both `/` and `/a/b/c` paths.
- When no path segments are provided, `slug` is `undefined`, and you can handle it as a fallback (like displaying "No path segments").

### Differences Between Catch-all and Optional Catch-all Routes:

1. **Catch-all (`[...param]`)**:
    
    - **Mandatory segments**: Always expects at least one segment in the URL.
    - Example: `/a`, `/a/b/c` are matched, but `/` is not.
2. **Optional Catch-all (`[[...param]]`)**:
    
    - **Optional segments**: It can match both URLs with segments and the root URL.
    - Example: `/`, `/a`, `/a/b/c` are all matched.

### Summary:

- **Catch-all route**: Captures multiple segments, always expects at least one.
- **Optional catch-all route**: Captures multiple segments but can also match an empty path.

---

#### **5. How do you handle route prefetching in Next.js?**

Next.js automatically prefetches linked pages in the background using the `Link` component:

```javascript
import Link from "next/link";

<Link href="/about">About</Link>
```

The `prefetch` property is enabled by default for static pages and improves navigation speed.

---

#### **6. How do middleware and redirects work in Next.js?**

- **Middleware:** Allows custom code execution before a request is completed. Middleware is defined in a `middleware.js` file at the root or within the `pages` directory.
- **Redirects:** Define redirects in `next.config.js`:

```javascript
module.exports = {
  async redirects() {
    return [
      { source: '/old-route', destination: '/new-route', permanent: true },
    ];
  },
};



```



### Middleware in Next.js

**Middleware** in Next.js allows you to run code before a request is completed. It can be used for tasks such as authentication, logging, or modifying the request/response.

- **Location**: Middleware files are placed inside the `middleware.js` (or `middleware.ts` if using TypeScript) file at the root of your project or within specific directories.

**Example**: Redirect users who are not authenticated.

```js
// middleware.js
import { NextResponse } from 'next/server';

export function middleware(req) {
  const token = req.cookies.get('auth_token');  // Check if user is authenticated
  
  if (!token) {
    return NextResponse.redirect(new URL('/login', req.url));  // Redirect to login if not authenticated
  }
  
  return NextResponse.next();  // Continue processing the request
}

export const config = {
  matcher: ['/dashboard', '/profile'],  // Apply middleware to these paths
};
```

**Explanation**:

- `NextResponse.redirect()`: Redirects the user if they are not authenticated.
- `NextResponse.next()`: Allows the request to continue if the condition is met.

### Redirects in Next.js

**Redirects** in Next.js can be handled at both the **server** and **client** levels.

#### 1. **Server-side Redirects** (via `next.config.js`):

You can define redirects globally in `next.config.js`.

**Example**: Redirect from `/old-page` to `/new-page`.

```js
// next.config.js
module.exports = {
  async redirects() {
    return [
      {
        source: '/old-page',
        destination: '/new-page',
        permanent: true,  // 301 redirect (permanent)
      },
    ];
  },
};
```

**Explanation**:

- `source`: The URL to match.
- `destination`: The new URL to redirect to.
- `permanent`: A boolean indicating whether the redirect is permanent (301) or temporary (302).

#### 2. **Client-side Redirects** (via `useRouter`):

You can also perform redirects on the client-side using the `useRouter` hook.

**Example**: Redirect on a button click:

```js
import { useRouter } from 'next/router';

const MyComponent = () => {
  const router = useRouter();
  
  const handleRedirect = () => {
    router.push('/new-page');  // Redirect to /new-page
  };
  
  return <button onClick={handleRedirect}>Go to New Page</button>;
};

export default MyComponent;
```

**Explanation**:

- `router.push()`: Navigates to the specified URL, which performs a client-side redirect.

### Summary:

- **Middleware**: Intercepts requests before they are processed, useful for authentication or modifying the request.
- **Redirects**:
    - **Server-side**: Defined globally in `next.config.js` to handle permanent or temporary redirects.
    - **Client-side**: Handled via `useRouter.push()` for programmatic navigation.
- 

---



