

### 🔁 **Hot Module Replacement (HMR)**

---

#### How it Works

- Vite leverages native ES Modules to update only the changed modules **in the browser** without a full reload.
    
- When you save a file, Vite’s dev server sends an update to the client, which swaps in the new module code.
    
- This keeps **state intact** (like component state) during updates, making development super fast.
    

#### HMR Boundaries in Frameworks

- **React:** Uses Fast Refresh — preserves React component state on edits. Only components with changes reload.
    
- **Vue:** HMR updates `.vue` SFC blocks independently (template, script, style).
    
- **Key:** Modules should export boundaries that Vite can patch; non-boundary changes force full reload.
    

---
