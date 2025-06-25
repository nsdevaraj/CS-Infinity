
`@tanstack/react-router-devtools` is the **official devtools package for TanStack Router**, designed to help developers **debug, inspect, and monitor the routing state** in real-time during development.

---

## 🧩 What It’s For

It gives you a **visual interface** inside your app where you can:

✅ Inspect the **current route**  
✅ View **matched routes** and **layouts**  
✅ Examine **route parameters**, **search params**, and **loader data**  
✅ Navigate between routes manually  
✅ Track **routing transitions**  
✅ Debug issues with route loaders, errors, and redirections

---

## 🚀 Key Features

|Feature|Description|
|---|---|
|🔍 Route Tree Viewer|See the active route + nested hierarchy|
|🧭 Params & Search Viewer|View route params & search query state|
|📦 Loader & Context Inspector|View loader results or errors|
|🔁 Navigation Actions|See history of route transitions|
|🛠 Dev Only|Stripped from production builds|

---

## 🛠 How to Install

```bash
npm install @tanstack/react-router-devtools
```

---

## 🔌 How to Use

### Step 1: Wrap your app with `<TanStackRouterDevtools />`

```tsx
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools';

function App() {
  return (
    <>
      <RouterProvider router={router} />
      <TanStackRouterDevtools position="bottom-right" />
    </>
  );
}
```

### Optional Props:

```tsx
<TanStackRouterDevtools
  position="bottom-right" // or 'top-left', etc.
  initialIsOpen={false}   // start closed
  closeButton={true}
/>
```

---

## 👀 What It Looks Like

A draggable, collapsible **floating dev panel** (similar to React Query Devtools) that overlays in your app:

- Click to expand the route tree
    
- See props passed to each route
    
- View loader and error states
    
- Debug transitions and redirects
    

---

## 🧪 Great for Development

- Helps trace route issues quickly
    
- See exactly which routes are matched
    
- Useful when working with deeply nested layouts
    
- Ideal when working with loaders and `beforeLoad()` hooks
    

---

## 🧼 Safe for Production?

No — it's **meant for development only**. It's tree-shakable and will **not be included in production builds** if used correctly.

```tsx
{process.env.NODE_ENV === 'development' && (
  <TanStackRouterDevtools />
)}
```

---

## 🧠 Summary

`@tanstack/react-router-devtools` is like **React DevTools** or **React Query DevTools**, but for routing. It’s built for **developer productivity**, debugging, and understanding what’s happening inside your TanStack Router-powered app.

> Highly recommended for **development workflows**, especially when working with complex route structures or loader logic.

---

