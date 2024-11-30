


### **Section 5: Deployment and Configuration in Next.js**

#### **1. What are the different ways to deploy a Next.js application?**

1. **Vercel (recommended):** Offers seamless deployment with automatic optimizations.
2. **Custom Servers:** Deploy on platforms like AWS, Azure, Google Cloud, or DigitalOcean using Node.js.
3. **Static Export:** Generate static HTML files using `next export` for deployment on any static hosting service (e.g., Netlify, GitHub Pages).

---

#### **2. How do you deploy a Next.js app on Vercel?**

1. Push your Next.js project to a Git repository (GitHub, GitLab, or Bitbucket).
2. Connect the repository to Vercel at [vercel.com](https://vercel.com/).
3. Vercel automatically detects Next.js and deploys the application with default settings.
4. Each push to the repository triggers an automatic redeployment.

---

#### **3. What is the difference between `next start` and `next build`?**

- **`next build`:** Compiles the application for production, optimizing JavaScript, CSS, and generating static assets.
- **`next start`:** Starts a production-ready server to serve the optimized build created by `next build`.

---

#### **4. How do you configure environment variables in Next.js?**

Use `.env` files to define environment variables:

- `.env.local`: For local development.
- `.env.production`: For production builds.
- `.env.test`: For testing environments.

**Accessing environment variables:**

- Add variables in `.env.local`:
    
    ```env
    NEXT_PUBLIC_API_URL=https://api.example.com
    ```
    
- Access in your app:
    
    ```javascript
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    ```
    

**Key Points:**

- Prefix variables with `NEXT_PUBLIC_` for client-side access.
- Server-only variables do not require this prefix.

---

#### **5. How do you customize the Next.js build process?**

Customize using `next.config.js`:

- Example of enabling WebP image formats:
    
    ```javascript
    module.exports = {
      images: {
        formats: ['image/webp'],
      },
    };
    ```
    
- Example of adding custom headers:
    
    ```javascript
    async headers() {
      return [
        {
          source: '/(.*)',
          headers: [{ key: 'X-Custom-Header', value: 'Custom Value' }],
        },
      ];
    },
    ```
    

---

#### **6. What is the purpose of the `next.config.js` file?**

The `next.config.js` file allows you to configure the behavior of a Next.js application, such as:

- Setting environment variables.
- Modifying build settings.
- Enabling custom headers and redirects.
- Adding Webpack customizations.

---

#### **7. How do you export a Next.js app to static HTML?**

Use `next export` to generate static HTML for your app. This is suitable for purely static sites without server-side functionality.

**Steps:**

1. Add an `exportPathMap` in `next.config.js` (optional).
2. Run the following commands:
    
    ```bash
    next build
    next export
    ```
    
3. Deploy the generated `out` directory to any static host.

---

#### **8. How do you configure custom server logic in Next.js?**

To use a custom server, you must disable the default Next.js server and write your own using Node.js, Express, or other frameworks.

**Example: Custom server with Express:**

```javascript
const express = require('express');
const next = require('next');

const app = next({ dev: process.env.NODE_ENV !== 'production' });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();

  server.get('/custom-route', (req, res) => {
    return app.render(req, res, '/custom-page', req.query);
  });

  server.all('*', (req, res) => {
    return handle(req, res);
  });

  server.listen(3000, () => {
    console.log('> Ready on http://localhost:3000');
  });
});
```

---

#### **9. How do redirects work in Next.js?**

Redirects are defined in `next.config.js` using the `redirects` property:

```javascript
module.exports = {
  async redirects() {
    return [
      {
        source: '/old-route',
        destination: '/new-route',
        permanent: true, // Use 308 for permanent or 307 for temporary
      },
    ];
  },
};
```

---

#### **10. How do you configure custom error pages in Next.js?**

Create the following files in the `pages` directory:

- **404.js:** Handles "Page Not Found" errors.
- **_error.js:** Handles all other server-side errors.

**Example:**

```javascript
// pages/404.js
export default function Custom404() {
  return <h1>404 - Page Not Found</h1>;
}
```

---

Would you like to proceed with the **Advanced Topics in Next.js** or a different section?