
### **Section 1: Basics of Next.js**

#### **1. What is Next.js? Why is it used?**

Next.js is a React-based framework that enables server-side rendering (SSR) and static site generation (SSG). It simplifies building web applications with built-in routing, optimized performance, and support for incremental static regeneration. It's used for fast, scalable, SEO-friendly applications.

---

#### **2. What are the key features of Next.js?**

Key features include:

- **Server-side Rendering (SSR):** Renders pages on the server at request time.
- **Static Site Generation (SSG):** Generates static HTML pages at build time.
- **Dynamic Routing:** Supports file-based routing for dynamic URLs.
- **API Routes:** Allows building API endpoints directly in the app.
- **CSS and Sass Support:** Enables global and modular CSS with built-in styling support.
- **Image Optimization:** Provides automatic image resizing and optimization.
- **Built-in TypeScript Support:** Simplifies working with TypeScript.

---

#### **3. What is file-based routing in Next.js?**

In Next.js, the file system is the main routing mechanism. Every file in the `pages` directory automatically becomes a route:

- `pages/index.js` → `/`
- `pages/about.js` → `/about`
- `pages/blog/[id].js` → `/blog/:id` for dynamic routes.

---

#### **4. How is Next.js different from Create React App (CRA)?**

|Feature|Next.js|CRA|
|---|---|---|
|Rendering|SSR, SSG, ISR, CSR|CSR only|
|Routing|File-based|Manual setup (e.g., React Router)|
|Performance|Highly optimized with automatic code splitting|Depends on manual optimizations|
|SEO|Excellent (SSR/SSG)|Needs manual configuration|
|Built-in Features|API routes, image optimization|Requires third-party libraries|

---

#### **5. What rendering modes does Next.js support?**

- **Server-side Rendering (SSR):** Fetches data and renders HTML on each request.
- **Static Site Generation (SSG):** Pre-generates pages at build time for better performance.
- **Incremental Static Regeneration (ISR):** Updates static pages after a specific interval or upon demand.
- **Client-side Rendering (CSR):** Similar to React, renders components on the client.

---
