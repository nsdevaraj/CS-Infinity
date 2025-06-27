

---

## 🌐 **Environment Modes in Vite**

---

### 1. **What are Env Modes?**

Vite supports multiple modes (environments) to load different environment variables and configs depending on your workflow stage, such as:

- `development` (default when running `vite` or `vite dev`)
    
- `production` (default when running `vite build`)
    
- Any custom mode you define (e.g., `staging`, `test`)
    

---

### 2. **How Modes Affect `.env` Files**

Vite loads environment variables from specific `.env` files based on the current mode:

|Mode|Files Loaded (in order)|
|---|---|
|`development`|`.env`, `.env.development`|
|`production`|`.env`, `.env.production`|
|`staging`|`.env`, `.env.staging` (if `mode=staging`)|

- Variables in mode-specific files override those in `.env`.
    
- `.env` is always loaded as the base.
    

---

### 3. **Example `.env` Files**

```env
# .env (common to all modes)
VITE_APP_NAME=MyApp
API_URL=https://default.api.com

# .env.development
VITE_API_URL=http://localhost:3000/api

# .env.production
VITE_API_URL=https://api.myapp.com
```

---

### 4. **Using Modes**

- Start dev server in a mode:
    

```bash
vite --mode development
vite --mode staging
```

- Build for a mode:
    

```bash
vite build --mode production
vite build --mode staging
```

---

### 5. **Accessing Environment Variables**

- In your app code, **only variables prefixed with `VITE_` are exposed**:
    

```ts
console.log(import.meta.env.VITE_API_URL);  // Available
console.log(import.meta.env.API_URL);       // Undefined (no prefix)
```

- Non-prefixed variables are accessible **only in `vite.config.js`** via `loadEnv`.
    

---

### 6. **Loading Env Variables in `vite.config.js`**

```ts
import { loadEnv } from 'vite';

export default ({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');  // loads all vars, no prefix filter
  console.log(env.API_URL);                       // accessible here even if no VITE_ prefix

  return {
    // config options
  };
};
```

---

### 7. **Summary**

|Feature|Description|
|---|---|
|Modes|Different `.env` files loaded per mode|
|`.env`|Base env file loaded for all modes|
|Mode-specific `.env`|Overrides `.env` for that mode|
|`VITE_` prefix|Expose variable to frontend code|
|Non-prefixed variables|Available only in build/config context via `loadEnv`|

---


Here's how to **load both prefixed (`VITE_`) and non-prefixed** variables from a `.env` file.

---

## ✅ 1. How Vite Handles Env Variables

### 🔓 Public (Exposed to Frontend)

- **Must be prefixed with `VITE_`**
    
- Available in your code as `import.meta.env.VITE_MY_VAR`
    

### 🔒 Private (Only used in config files like `vite.config.js`)

- Variables **not** prefixed with `VITE_` are _not_ exposed to frontend
    
- You must manually load them using `loadEnv`
    

---

## ✅ 2. Loading Env Variables in `vite.config.js`

### Step-by-step:

```ts
// vite.config.js or vite.config.ts
import { defineConfig, loadEnv } from 'vite';

export default ({ mode }) => {
  // Load all variables (both VITE_ and non-prefixed)
  const env = loadEnv(mode, process.cwd(), '');

  // You can access both VITE_ and non-VITE_ variables from `env`
  console.log(env.VITE_API_URL);    // Public
  console.log(env.SECRET_KEY);      // Private (only in config)

  return defineConfig({
    define: {
      // If you want to use non-VITE variables in your frontend,
      // you must manually define them here
      __SECRET_KEY__: JSON.stringify(env.SECRET_KEY),
      // import.meta.env.SECRET_KEY - makes work like normal env
    },
  });
};
```

---

## ✅ 3. Accessing in Your App Code

```env
# .env file
VITE_API_URL=https://api.example.com
SECRET_KEY=123456
```

### In JS/TS files:

```ts
console.log(import.meta.env.VITE_API_URL); // ✅ Works

console.log(import.meta.env.SECRET_KEY);   // ❌ Undefined unless injected manually
```

---

## ✅ TL;DR

|Variable|In `.env`|Access in frontend|Access in vite.config.js|
|---|---|---|---|
|`VITE_API_URL`|`VITE_API_URL=...`|`import.meta.env.VITE_API_URL`|`env.VITE_API_URL`|
|`SECRET_KEY`|`SECRET_KEY=...`|❌ Not accessible directly|✅ `env.SECRET_KEY`|

---
