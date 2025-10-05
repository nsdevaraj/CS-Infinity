
If you have **two environment variables with the same name**, the one that gets used depends on **how and where they're defined** — and in what **order** they're loaded.

### 🔢 Precedence order (most common scenarios):

1. **Shell / runtime environment** (highest priority):
    
    ```bash
    export API_KEY=from-shell
    node app.js
    ```
    
2. **Passed inline when running a command:**
    
    ```bash
    API_KEY=from-inline node app.js
    ```
    
3. **`.env` file loaded by `dotenv` or similar tools:**
    
    ```env
    API_KEY=from-env-file
    ```
    
4. **Defaults in code:**
    
    ```ts
    const key = process.env.API_KEY || 'default-key';
    ```
    

### 📌 So if you have:

```env
# .env
API_KEY=key-in-env
```

And also run:

```bash
API_KEY=key-from-shell node app.js
```

➡️ **Result:** `process.env.API_KEY` will be `"key-from-shell"` — because the shell variable **overrides** the `.env` file.

---

### 💡 Tip:

Avoid duplicating variable names across sources unless you're intentionally overriding for different environments (e.g., `.env.development` vs `.env.production`).


---

If you define **two variables with the same name in the same `.env` file**, **only the last one is used** — it **overrides** the earlier one.

### ✅ Example:

```env
API_KEY=first-value
API_KEY=second-value
```

### 🟰 Result:

```ts
process.env.API_KEY // "second-value"
```

### 🧠 Why?

Most `.env` parsers (like `dotenv`) read the file **line by line** — so the **last assignment wins**.

---

### 💡 Recommendation:

Avoid redefining the same key in the same `.env` file unless you’re intentionally overriding it and you know what you're doing. If values differ across environments, use separate files like:

- `.env.development`
    
- `.env.production`
    
- `.env.local`
    

