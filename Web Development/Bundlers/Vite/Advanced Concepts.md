
### 🖥️ **Advanced Vite Concepts**

---

#### 1. **Server-Side Rendering (SSR)**

- Vite supports **SSR out-of-the-box**, enabling you to render your app on the server for better SEO and faster initial loads.
    
- It provides a **dev server with SSR support** and a flexible build pipeline.
    
- You write separate entry points for client and server bundles.
    
- Integrates with frameworks like Vue, React, and Svelte for SSR.
    

---

#### 2. **Using Vite with Backend Frameworks**

- Vite can be paired seamlessly with backend frameworks like **Express, Laravel, Fastify**, etc.
    
- Typically, Vite handles frontend assets and HMR during development, while backend serves API/routes.
    
- Proxy setups (`server.proxy`) are used to forward API calls during development.
    
- Production builds can be served by backend static middleware (e.g., Laravel’s public folder).
    

---

#### 3. **Custom Plugins**

- Vite’s plugin API is built on top of Rollup’s plugin system with additional hooks.
    
- You can write plugins to:
    
    - Transform source code
        
    - Add new file handlers
        
    - Extend dev server behavior (middleware)
        
    - Inject environment variables or global constants
        
- Plugins are reusable and composable, empowering deep customizations.
    

---

#### 4. **Multi-Page Applications (MPA)**

- Vite supports MPAs by specifying multiple entry points in `rollupOptions.input`.
    
- Each page gets its own HTML and bundle.
    
- Useful for projects needing multiple independent pages without SPA routing.
    

```ts
build: {
  rollupOptions: {
    input: {
      main: 'index.html',
      admin: 'admin.html',
    }
  }
}
```

---

#### 5. **Monorepo Setup**

- Vite works well in monorepos managed by tools like **pnpm**, **Yarn Workspaces**, or **Lerna**.
    
- Supports:
    
    - Dependency linking across packages
        
    - Shared config files and plugins
        
    - Faster builds through caching and symlink support
        
- Requires proper configuration of `resolve.preserveSymlinks` and sometimes path aliasing.
    

---
