
## 🛠️ **Integrations with Vite**

---

### ⚛️ 1. React

Install plugin:

```bash
npm install @vitejs/plugin-react
```

Configure:

```ts
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
});
```

Supports:

- Fast Refresh (HMR)
    
- JSX, TSX
    
- Babel plugins
    

---

### 🔥 2. Vue

Install plugin:

```bash
npm install @vitejs/plugin-vue
```

Configure:

```ts
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
});
```

Supports:

- `.vue` SFCs
    
- HMR
    
- Vue Devtools
    

---

### 🧬 3. Svelte

Install via community plugin:

```bash
npm install @sveltejs/vite-plugin-svelte
```

Configure:

```ts
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
});
```

---

### ⚡ 4. Solid

SolidJS has first-class Vite support.

```bash
npm install vite-plugin-solid
```

Configure:

```ts
import solid from 'vite-plugin-solid';

export default defineConfig({
  plugins: [solid()],
});
```

---

### 🟦 5. TypeScript Support

- Built-in! No config needed if you use `.ts` or `.tsx` files.
    
- Uses `esbuild` for super-fast TypeScript transpilation.
    

```bash
tsc --init
```

> Vite doesn’t type-check TypeScript. Use `tsc --noEmit` or `vue-tsc` for that.

---

### 🎨 6. Tailwind CSS

Install:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Configure `tailwind.config.js` and include Tailwind in your `main.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Use with any framework or vanilla Vite setup.

---

### 🧹 7. ESLint & Prettier

#### ESLint:

```bash
npm install -D eslint
npx eslint --init
```

Optionally add ESLint plugin:

```bash
npm install -D vite-plugin-eslint
```

```ts
import eslint from 'vite-plugin-eslint';

export default defineConfig({
  plugins: [eslint()],
});
```

#### Prettier:

```bash
npm install -D prettier
```

Add `.prettierrc` and format scripts.

---

