### 🧠 **Core Concepts in Vite**

---

#### 📦 1. **Native ES Modules (ESM)**

- Vite leverages **modern browsers’ support for ESM**.
    
- Instead of bundling everything upfront (like Webpack), Vite serves each module **on demand**.
    
- Benefits:
    
    - **Instant dev server start**
        
    - **Faster hot reload (HMR)** since only changed modules reload
        

> 🔍 Vite uses [esbuild](https://esbuild.github.io/) for lightning-fast dependency pre-bundling.

---

#### ⚡ 2. **Dev Server vs Build Process**

|Mode|Purpose|Tools Used|
|---|---|---|
|Dev Server|Fast startup, live reload|Native ESM, esbuild|
|Build|Optimized, minified output|Rollup|

- **Dev Server:**
    
    - Serves unbundled files via native ESM
        
    - Fast startup + Hot Module Replacement (HMR)
        
- **Build:**
    
    - Uses Rollup to bundle, minify, and optimize
        
    - Outputs production-ready static assets
        

---

#### 🛠️ 3. **vite.config.js / vite.config.ts**

- Central config file for Vite.
    
- Defined using `defineConfig` for better type support.
    
- Controls:
    
    - Plugins
        
    - Aliases
        
    - Server config (port, proxy)
        
    - Build optimizations
        
    - Env loading, SSR, PWA, etc.
        

```ts
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: 3000,
  },
  build: {
    outDir: 'dist',
  },
});
```

---

#### 🌍 4. **Environment Variables**

##### Files:

- `.env`, `.env.development`, `.env.production`, etc.
    

##### Variable Types:

|Type|Prefix Required|Accessible in Code|
|---|---|---|
|Public|✅ `VITE_`|`import.meta.env.VITE_KEY`|
|Private|❌ (no prefix)|Only in `vite.config.*` via `loadEnv`|

```env
# .env
VITE_API_URL=https://api.example.com
SECRET_KEY=super-secret
```

```ts
// In app code
console.log(import.meta.env.VITE_API_URL); // ✅ works
console.log(import.meta.env.SECRET_KEY);   // ❌ undefined

// In vite.config.ts
import { loadEnv } from 'vite';
const env = loadEnv(mode, process.cwd(), '');
console.log(env.SECRET_KEY); // ✅ works
```

---
