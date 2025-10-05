

## 🧱 What is `createRootRouteWithContext`?

It’s a utility from **@tanstack/react-router** used to define your **root route**, with the ability to pass **strongly-typed context** across your route tree.

---

### 🔑 Purpose

- It creates the **root of your route hierarchy**.
    
- It provides a **typed shared context** that all child routes can access via hooks like `useRouteContext()`.
    

---

### 🧠 Why Use It?

#### Without Context:

If you just use `createRootRoute()`:

- You **can’t pass global data** (like user, theme, permissions) via router context.
    
- You're limited to prop drilling or external global stores.
    

#### With `createRootRouteWithContext`:

- You define a **custom context object**, such as:
    
    ```ts
    type RouterContext = {
      auth: AuthService;
      theme: ThemeConfig;
    };
    ```
    
- Then you can **inject and use it globally in child routes**:
    
    ```ts
    const rootRoute = createRootRouteWithContext<RouterContext>()({ component: App });
    
    const route = createRoute({
      getContext: () => useRouteContext<RouterContext>(),
    });
    ```
    

---

## 🚀 When to Use It

|Use Case|Use `createRootRouteWithContext`?|
|---|---|
|Just simple routes and layout|❌ Not necessary (`createRootRoute()` is fine)|
|You want to pass shared services|✅ Yes (e.g., auth, API, theme, state managers)|
|Strong typing across route tree|✅ Yes (Type-safe, scalable apps)|

---

## 🧩 Alternative: `createRootRoute()`

If you're not using shared context:

```ts
const rootRoute = createRootRoute({
  component: RootLayout,
});
```

✔️ Works for simple cases — but **no shared route context typing**.

---

## ✅ Final Example

```ts
// Define context type
type RouterContext = {
  user: User | null;
  authService: AuthService;
};

// Root route with typed context
export const rootRoute = createRootRouteWithContext<RouterContext>()({
  component: RootLayout,
});
```

Then in any route or component:

```ts
const { authService, user } = useRouteContext<RouterContext>();
```

---

## 🏁 Summary

|Method|Use When You…|
|---|---|
|`createRootRoute()`|Don't need global typed context|
|`createRootRouteWithContext<T>()`|Need to pass shared data/services in a type-safe way|

---

Let me know if you'd like help setting up an actual `RouterContext` (like for auth or feature flags)!