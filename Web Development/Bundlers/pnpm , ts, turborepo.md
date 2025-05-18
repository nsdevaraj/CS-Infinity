
# ⚡️ A Minimal Yet Scalable Monorepo Setup Using TurboRepo, pnpm, and TypeScript

> Want to set up a TypeScript monorepo without bloating it with unnecessary dependencies? Here's how you can build a **high-performance, maintainable monorepo** with just **three core tools**: `pnpm`, `TypeScript`, and `TurboRepo`.

---

## 🧰 Tooling Philosophy

The goal here is to **stay lean** while **maximizing productivity**. We’ll rely on just:

|Tool|Role|
|---|---|
|**pnpm**|Fast, disk-efficient package manager|
|**TypeScript**|Type-checking, linting, and compiling|
|**TurboRepo**|Orchestrates builds and caching|

---

## 🗂 Folder Structure

Here’s a typical layout:

```
/
├── apps/
│   └── my-app/
├── packages/
│   └── shared/
├── package.json
├── turbo.json
├── tsconfig.json
├── .gitignore
└── pnpm-workspace.yaml
```

- `apps/` → Host your actual applications (web, mobile, backend)
    
- `packages/` → Shared libraries or modules
    
- `package.json` → Root dependencies and scripts
    
- `turbo.json` → Task orchestration logic
    
- `.gitignore`, `node_modules/` etc. as needed
    

---

## 🚀 Setting Up the Monorepo

### 1. Initialize the monorepo with `pnpm`:

```bash
pnpm init
pnpm add -D typescript turbo
pnpm install
```

Add a `pnpm-workspace.yaml`:

```yaml
packages:
  - apps/*
  - packages/*
```

---

## ⚙️ The Core Scripts

Inside each `package.json` (shared or app):

```json
{
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch"
  }
}
```

This allows TurboRepo to orchestrate each step centrally.

---

## 🧠 `tsconfig.json` Setup

Use a centralized `tsconfig.base.json`:

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "moduleResolution": "node",
    "composite": true,
    "declaration": true,
    "declarationMap": true,
    "skipLibCheck": true
  }
}
```

Each package can then extend this:

```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "outDir": "dist"
  },
  "include": ["src"]
}
```

---

## 🔄 TurboRepo: The Build Brain

### `turbo.json`

```json
{
  "$schema": "https://turborepo.org/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

### 🔨 `turbo build`

This command:

- Builds your packages in **dependency order**
    
- Uses TypeScript (`tsc`) to compile files
    
- **Caches** output to avoid rebuilding unchanged code
    

⚡ **Turbo’s caching** is incredible — it won’t rebuild packages if nothing changed, saving time across CI and local development.

---

### 🧪 `turbo dev`

```json
"scripts": {
  "dev": "tsc --watch"
}
```

This watches each package for changes and only triggers builds or watchers **where needed**.

By marking `"cache": false` and `"persistent": true` in the `dev` pipeline, Turbo treats it as a long-running watcher.

### ⚡ Bonus: App-level Dev

Inside `apps/my-app/package.json`:

```json
"dependencies": {
  "shared": "workspace:*"
}
```

This uses `pnpm` workspaces to link local packages. Now when you run:

```bash
turbo run dev --filter=my-app
```

TurboRepo:

- Starts dev on `my-app`
    
- Watches `shared/` and any other packages it depends on
    
- Rebuilds only what’s changed
    

---

## 🧱 TurboRepo Features to Love

|Feature|Benefit|
|---|---|
|✅ Incremental builds|Only builds changed files & dependencies|
|💾 Caching|Saves computation across runs and even between CI builds (remote)|
|🧭 Dependency graph|Builds run in topological order automatically|
|🧠 Persistent tasks|Great for watchers or dev servers|
|🌐 Remote caching|(Optional) sync cache between machines via Vercel or S3|
|🎯 Filtering|Run commands in specific packages (`--filter=...`)|

---

## 📈 Scaling Up Tips

1. **Split packages wisely** — keep shared code in `packages/`
    
2. **Use filters** for local and CI speedups:
    
    ```bash
    turbo run build --filter=shared
    ```
    
3. **Remote caching** for teams:
    
    ```bash
    turbo login
    turbo link
    ```
    
4. **Use `env` filters** in `turbo.json` for custom behaviors per environment
    
5. Add `eslint`, `vitest`, or `storybook` later as needed
    

---

## 🧠 Final Thoughts

By starting with just **pnpm + TypeScript + TurboRepo**, you get:

- Clean dev experience
    
- Blazing fast rebuilds with caching
    
- Typed shared code across apps
    
- Easy growth into more advanced tooling
    

This setup balances **minimalism** with **powerful architecture** and can support everything from a solo side project to a full enterprise-grade platform.

---

### Want more?

- 💡 Need `eslint` or `vitest` integration tips?
    
- 📦 Want to generate type-safe APIs across packages?
    
- ⚙️ Curious how to bundle apps with `vite` or `next`?
    

Just say the word — I’ll build on top of this article with practical enhancements.