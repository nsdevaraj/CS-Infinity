

### ⚙️ **Vite Configuration**

---

#### ✅ 1. `defineConfig` Usage

- Vite provides a `defineConfig()` helper to enable **auto-completion and type safety**.
    
- Wrap your export in this for better DX (developer experience).
    

```ts
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  // your config here
});
```

> Without it, you'd export a plain object—less type-safe and harder to maintain.

---

#### 🔌 2. `plugins` (Vite & Rollup Plugins)

- Extend Vite's functionality using plugins.
    
- Vite supports both **Vite-native plugins** and **Rollup plugins**.
    

```ts
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
});
```

- Popular Plugins:
    
    - `@vitejs/plugin-react`
        
    - `vite-plugin-svgr` (SVG as React components)
        
    - `vite-plugin-pwa`
        
    - Rollup plugins like `@rollup/plugin-alias`
        

---

#### 🧭 3. Aliases (`resolve.alias`)

- Shorten import paths, avoid `../../../` hell.
    

```ts
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
});
```

- Then you can use:
    

```ts
import MyComponent from '@/components/MyComponent.vue';
```

---

#### 🌐 4. Customizing Dev Server (`server`)

Configure dev server behavior:

```ts
export default defineConfig({
  server: {
    port: 3000,           // Custom port
    open: true,           // Opens browser automatically
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
});
```

- Useful in local dev for **backend integration** without CORS issues.
    

---

#### 📦 5. Build Options (`build`)

Customize the **production build** process.

```ts
export default defineConfig({
  build: {
    outDir: 'dist',                // Output folder
    sourcemap: true,               // Include source maps
    rollupOptions: {
      input: './src/main.ts',     // Custom entry
      output: {
        manualChunks: {           // Code splitting
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },
});
```

- Uses **Rollup** under the hood for tree-shaking, code splitting, etc.
    

---
