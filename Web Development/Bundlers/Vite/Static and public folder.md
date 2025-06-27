
## 📁 **Static Assets & Public Folder in Vite**

---

### 🖼️ 1. Handling Static Assets (Images, Fonts, etc.)

Vite supports two ways to handle static assets:

#### ✅ **Imported Assets (Recommended for App Logic)**

- Use when you want assets to go through Vite’s **build pipeline** (hashing, optimization).
    
- Works for images, fonts, etc.
    

```ts
import logo from './assets/logo.png';

<img src={logo} />
```

- Vite processes and optimizes the asset, and the URL is **hashed** in production builds.
    

---

### 📂 2. `public/` Folder Behavior

- Any file placed in `public/` is **served as-is**, without processing.
    
- Accessed via root path (`/`).
    

📁 Example structure:

```
public/
  favicon.ico  →  available at http://localhost:5173/favicon.ico
  robots.txt   →  http://localhost:5173/robots.txt
```

Use for:

- Static assets not imported in code (e.g., `manifest.json`, `robots.txt`)
    
- External scripts or files
    

> ⚠️ Files in `public/` are **not optimized** or hashed—use cautiously for large assets.

---
