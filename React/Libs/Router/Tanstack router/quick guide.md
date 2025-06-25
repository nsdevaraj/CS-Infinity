
# 🔀 TanStack Router: The Future of Type-Safe Routing in React

**TanStack Router** is a **fully type-safe, headless routing solution** for React (and potentially other frameworks) created by [Tanner Linsley](https://twitter.com/tannerlinsley), the creator of React Query, TanStack Table, and more.

> 🌟 It’s part of the TanStack ecosystem and provides powerful, modern, and flexible routing with full control over rendering, layouts, and type inference.

---

## 🚀 What Makes TanStack Router Different?

|Feature|TanStack Router|React Router (v6)|Next.js App Router|
|---|---|---|---|
|⚙️ Type Safety|✅ Full route param/type inference|❌ No inference|✅ (with TS + config)|
|🔌 Headless|✅ You control rendering/UI|❌ Opinionated UI|❌ Tied to Next.js|
|🗺️ Nested Routing|✅ Built-in layout hierarchy|✅ Yes|✅ File-based|
|⏳ Deferred Data|✅ Full loader support|✅ (`loader`)|✅ `fetch` + suspense|
|🧠 Code Splitting|✅ Works with `lazy()` easily|✅ Yes|✅ By default|
|📚 Schema-based Routing|✅ Full route schema validation|❌ No|⚠️ Optional|

---

## 📦 Installation

```bash
npm install @tanstack/react-router
```

Or with Yarn:

```bash
yarn add @tanstack/react-router
```

---

## 🧱 Core Concepts

### 1. **File-less Routing**

TanStack Router is **not file-system based** like Next.js. You **define routes as config objects**.

```tsx
// routes/index.tsx
import { Route } from '@tanstack/react-router';

export const route = new Route({
  getParentRoute: () => rootRoute,
  path: '/',
  component: HomePage,
});
```

This makes it:

- Framework-agnostic
    
- Highly configurable
    
- Type-safe with auto inference
    

---

### 2. **Route Tree (Explicit Nesting)**

```tsx
const rootRoute = new RootRoute({ component: AppLayout });

const indexRoute = new Route({
  getParentRoute: () => rootRoute,
  path: '/',
  component: IndexPage,
});

const aboutRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'about',
  component: AboutPage,
});

const routeTree = rootRoute.addChildren([indexRoute, aboutRoute]);

export const router = new Router({ routeTree });
```

> 📌 Explicit tree definition = full control over nesting and layout hierarchy.

---

### 3. **Type-Safe Params**

Define params in route paths and get full TS support:

```tsx
const userRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'users/$userId',
  component: UserPage,
});

function UserPage() {
  const { userId } = useParams({ from: userRoute.id });
  // userId is inferred as string
}
```

✅ No need to define types manually. It’s all inferred!

---

### 4. **Loaders + Data Fetching**

Each route can have a loader (like `React Router` or `Remix`):

```tsx
const userRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'users/$userId',
  component: UserPage,
  loader: async ({ params }) => {
    return fetchUser(params.userId);
  },
});
```

Inside the component:

```tsx
const { data: user } = useLoaderData({ from: userRoute.id });
```

---

### 5. **Search Params (Query String)**

Search params are declared and validated **statically**:

```tsx
const usersRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'users',
  validateSearch: z.object({
    page: z.number().default(1),
  }),
  component: UsersList,
});
```

```tsx
const { search } = useSearch({ from: usersRoute.id });
```

> ✅ Great for paginated lists, filters, etc.

---

## 🧰 Useful APIs

|Hook|Description|
|---|---|
|`useRouter()`|Access router instance|
|`useParams()`|Access route parameters|
|`useSearch()`|Access and update search params|
|`useLoaderData()`|Access loader data|
|`useNavigate()`|Navigate programmatically|
|`Link`|Declarative navigation|

---

## 🧪 Advanced Features

### 📦 Code Splitting

Each route can be loaded lazily:

```tsx
const AboutPage = lazy(() => import('./About'));

const aboutRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'about',
  component: AboutPage,
});
```

### 🔄 Redirects

```tsx
const protectedRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'dashboard',
  beforeLoad: ({ context }) => {
    if (!context.authenticated) {
      throw redirect({ to: loginRoute.id });
    }
  },
});
```

---

## 🔐 Authentication + Protected Routes

TanStack Router allows fine-grained **`beforeLoad()`** control:

```tsx
beforeLoad: async ({ context }) => {
  if (!context.authenticated) {
    throw redirect({ to: loginRoute.id });
  }
}
```

Context can be passed at router level:

```tsx
const router = new Router({
  routeTree,
  context: {
    authenticated: false,
  },
});
```

---

## 🧪 When to Use TanStack Router?

✅ Use when:

- You need full **type safety**
    
- You want headless control of rendering/layout
    
- You prefer **schema-based routing** (great for larger apps)
    
- You need **custom navigation logic**, loaders, or guards
    

❌ Avoid if:

- You prefer file-based routing like in Next.js
    
- Your team is unfamiliar with TanStack ecosystem
    
- You want a quick prototyping tool (it requires more setup)
    

---

## 🧩 Integrates Well With:

- **React Query / TanStack Query**
    
- **Zod / Yup** (for input validation)
    
- **Suspense & Lazy loading**
    
- **Custom layout systems**
    

---

## 🔚 Final Thoughts

TanStack Router is a **next-gen router for React apps**, built with **developer productivity**, **type safety**, and **modularity** at its core. While it’s still stabilizing compared to React Router, its feature set and extensibility make it a compelling choice for production-grade apps—especially when coupled with **TanStack Query** and **Zod**.

---

## 📘 Official Links

- [TanStack Router Docs](https://tanstack.com/router/latest)
    
- [GitHub Repo](https://github.com/TanStack/router)
    
- [React Router vs TanStack Comparison](https://tanstack.com/router/v1/docs/framework/react/overview#comparison-with-other-routers)
    

---

Would you like a full working project template or a comparison chart with other routers like Next.js or Remix?