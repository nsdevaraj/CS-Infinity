
# Turbo Monorepo: Everything You Need to Know

Turbo (Turborepo) is a **high-performance build system for JavaScript/TypeScript monorepos**, designed to make managing multiple packages and applications fast, scalable, and efficient.

---

## 1️⃣ What is a Monorepo?

A **monorepo** is a single repository that contains multiple projects or packages, often including:

- Applications (`apps/ui`, `apps/api`)
    
- Shared libraries (`packages/utility`, `packages/types`)
    

**Advantages of monorepos:**

- Single source of truth for code
    
- Easier refactoring and dependency management
    
- Simplified CI/CD pipelines
    

---

## 2️⃣ Why Turbo?

When a monorepo grows, **build times explode**. Turbo solves this with:

1. **Incremental builds** – Only rebuilds packages that changed.
    
2. **Remote caching** – Share build artifacts across devs or CI.
    
3. **Parallel execution** – Runs independent tasks simultaneously.
    
4. **Task pipelines** – Define dependencies between tasks across packages.
    

---

## 3️⃣ Basic Concepts

### a) Tasks

A **task** is a command that Turbo can run, usually defined in your package.json:

```json
"scripts": {
  "build": "tsc -b",
  "test": "vitest"
}
```

Or defined in `turbo.json`:

```json
"tasks": {
  "build": {
    "dependsOn": ["^build"],
    "inputs": ["$TURBO_DEFAULT$", "**/package.json"],
    "outputs": ["dist/**"]
  }
}
```

- `dependsOn`: other tasks to run first.
    
    - `^build` = build all dependencies.
        
    - `~build` = build only direct dependencies.
        
- `inputs`: files Turbo watches to decide if a task is stale.
    
- `outputs`: what Turbo caches after running the task.
    

---

### b) Filtering

You can run tasks **only on specific packages**:

```bash
pnpm turbo run build --filter=ui...
```

- `ui...` = UI package + all its dependencies.
    
- Filters prevent rebuilding unrelated packages.
    

---

### c) Caching

Turbo tracks:

- **Inputs** (source files, configs, env files)
    
- **Outputs** (build artifacts)
    

If inputs **did not change**, Turbo uses cached outputs — saving a lot of build time.

---

## 4️⃣ Structuring a Turbo Monorepo

Typical structure:

```
repo-root/
├─ apps/
│  ├─ ui/
│  │  ├─ package.json
│  │  └─ src/
│  └─ api/
├─ packages/
│  ├─ utility/
│  └─ types/
├─ package.json
└─ turbo.json
```

- `apps/` → runnable applications
    
- `packages/` → reusable libraries
    

---

### Example `turbo.json` for a UI app

```json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["$TURBO_DEFAULT$", ".env*", "**/package.json"],
      "outputs": ["dist/**"]
    },
    "build:ui:dev": {
      "dependsOn": ["^build"],
      "inputs": ["$TURBO_DEFAULT$", ".env*", "**/package.json"],
      "outputs": ["dist/**"]
    }
  }
}
```

- `build:ui:dev` runs only for the UI app and its dependencies.
    
- Dependencies like `@repo/utility` are built first.
    

---

## 5️⃣ Environment-Specific Builds

You can define separate scripts for **local/dev/staging/production**:

```json
"scripts": {
  "build:ui:local": "tsc -b && vite build --mode localdev",
  "build:ui:dev": "tsc -b && vite build --mode development",
  "build:ui:stg": "tsc -b && vite build --mode staging",
  "build:ui:prd": "tsc -b && vite build --mode production"
}
```

- Combine with Turbo filters to **only build the app + its dependencies** in CI/CD.
    
- Example:
    

```bash
pnpm turbo run build:ui:dev --filter=ui...
```

---

## 6️⃣ Best Practices

1. **Always define `inputs` and `outputs`** – this enables caching and incremental builds.
    
2. **Use `^build` for dependency builds** – ensures proper build order.
    
3. **Filter tasks in CI/CD** – avoids rebuilding unrelated packages.
    
4. **Do not use `sudo`** – pnpm and Turbo handle workspace dependencies safely.
    
5. **Keep scripts DRY** – pass environment flags dynamically instead of duplicating commands.
    

---

## 7️⃣ CI/CD Integration

Example GitHub Actions step:

```yaml
- name: Build UI
  run: pnpm turbo run build:ui:local --filter=ui...
```

Turbo will:

- Build `ui` + all dependencies (like `@repo/utility`)
    
- Skip unrelated packages
    
- Use cached builds if nothing changed
    

---

## 8️⃣ Summary

Turbo monorepo gives you:

- **Incremental and fast builds**
    
- **Dependency-aware pipelines**
    
- **Remote caching support**
    
- **Environment-specific builds scoped to packages**
    

By properly defining `tasks`, `inputs`, `outputs`, and using `--filter`, you can manage large monorepos with multiple apps and packages **efficiently and reliably**.

---
