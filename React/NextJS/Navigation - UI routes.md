
### **4. Navigation in Next.js**

In Next.js, navigation between routes is managed using the `Link` component for client-side transitions and the `useRouter` hook for programmatic navigation. Together, these make for a smooth navigation experience, eliminating page reloads and preserving application state.

---

#### **Key Navigation Concepts**

1. **Link Component**: Allows client-side transitions between pages without a full reload, making navigation faster and smoother.
2. **useRouter Hook**: Enables programmatic navigation, ideal for redirecting users based on certain conditions (e.g., after form submission).
3. **Active Link Styling**: Adds visual cues (e.g., bold font or a different color) to the currently active route.

  
---

#### **Example 1: Using the Link Component for Client-Side Navigation**

The `Link` component in Next.js is used for client-side navigation. Here's how to create a simple navigation menu with links.

**File Structure**:

```plaintext
app/
└── components/
    └── Navigation.tsx
└── app/
    ├── page.tsx
    ├── about/
    │   └── page.tsx
    └── products/
        └── [id]/
            └── page.tsx
```

**Code for `Navigation.tsx`**:

```typescript
// app/components/Navigation.tsx
"use client"; // Required to use hooks in Next.js

import Link from "next/link";
import { usePathname } from "next/navigation"; // Hook for getting current path

export default function Navigation() {
  const pathname = usePathname(); // Current route path

  return (
    <nav>
      <Link href="/" className={pathname === "/" ? "font-bold" : ""}>
        Home
      </Link>
      <Link href="/about" className={pathname === "/about" ? "font-bold" : ""}>
        About
      </Link>
      <Link
        href="/products/1"
        className={pathname.startsWith("/products") ? "font-bold" : ""}
      >
        Product 1
      </Link>
    </nav>
  );
}
```

**Explanation**:

- `usePathname()` is used to get the current route, allowing conditional styling to highlight the active link.
- The `font-bold` class is applied to the active link, making it bold.

---

#### **Example 2: Adding the Navigation Component to the Layout**

Add the `Navigation` component to your `app/layout.tsx` to make it appear on all pages.

**Code for `layout.tsx`**:

```typescript
// app/layout.tsx
import Navigation from "./components/Navigation";

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Navigation />
        {children}
      </body>
    </html>
  );
}
```

**Usage**: This setup will display the navigation menu at the top of every page in the application.

---

#### **Example 3: Programmatic Navigation with `useRouter`**

The `useRouter` hook in Next.js is helpful for redirecting users based on certain actions or conditions, such as after a form submission.

**Code for `page.tsx` in `about` folder**:

```typescript
// app/about/page.tsx
"use client";

import { useRouter } from "next/navigation";

export default function About() {
  const router = useRouter();

  return (
    <div>
      <h1>About Page</h1>
      <button onClick={() => router.push("/")}>
        Go to Home
      </button>
    </div>
  );
}
```

**Explanation**:

- `useRouter()` is used to get the `router` instance, and `router.push("/")` navigates to the home page when the button is clicked.

**Usage**: When users visit `/about` and click the "Go to Home" button, they will be redirected to the homepage.

---

#### **Example 4: Styling Active Links**

Using the `usePathname` hook, you can add custom styling to indicate the active link.

```typescript
// app/components/Navigation.tsx
import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Navigation() {
  const pathname = usePathname();

  return (
    <nav>
      <Link href="/" className={pathname === "/" ? "text-blue-500" : ""}>
        Home
      </Link>
      <Link href="/about" className={pathname === "/about" ? "text-blue-500" : ""}>
        About
      </Link>
      <Link href="/products/1" className={pathname.startsWith("/products") ? "text-blue-500" : ""}>
        Product 1
      </Link>
    </nav>
  );
}
```

**Explanation**: In this example, the `text-blue-500` class is applied to the active link, making it visually distinct.


