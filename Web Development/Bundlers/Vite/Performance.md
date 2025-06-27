
### ⚡ **Performance**

---

#### Dependency Pre-Bundling

- Uses `esbuild` to pre-bundle dependencies on server start.
    
- Speeds up page loads by reducing repeated requests and optimizing node_modules.
    
- Avoids slow native ESM imports of CommonJS modules.
    

#### Code Splitting

- Vite leverages Rollup’s code splitting on build.
    
- Automatically splits vendor and dynamic imports.
    
- You can customize chunks via `build.rollupOptions.output.manualChunks`.
    

#### Optimizing Production Build

- Minification with `esbuild` or `terser`.
    
- Tree shaking to remove unused code.
    
- Source maps optional for debugging.
    
- Asset hashing for cache busting.
    

---
