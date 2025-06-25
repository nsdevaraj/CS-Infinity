

### ❓ What is `routeTree.gen.ts`?

The `routeTree.gen.ts` file is **automatically generated** by the `@tanstack/react-router` package (v1 and above). It's part of the **automatic route generation** system that builds a type-safe route tree based on your route definitions.

This file is:

- **Generated at build or dev time** (e.g., by a CLI or a Vite plugin).
    
- **Used for type inference and route configuration** in your app.
    

---

### 📦 Should you include `routeTree.gen.ts` in Git?

**No, typically you should NOT commit `routeTree.gen.ts` to your Git repository.**  
It's a generated file, like `.next/`, `dist/`, or `build/`.

---

### ✅ Recommended `.gitignore` rule:

Add this to your `.gitignore`:

```
# Ignore generated route tree
routeTree.gen.ts
```

---

### 🧠 Why ignore it?

- It can change often and cause unnecessary diffs.
    
- It’s rebuilt automatically when needed.
    
- It avoids merge conflicts from multiple devs generating it slightly differently.
    
