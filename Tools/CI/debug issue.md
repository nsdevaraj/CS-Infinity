

JS domain:

### 🛠️ **CI Failing: Step-by-Step Fix Guide**

#### ✅ 1. **Read the Logs Carefully**

- Go to the **failed job** in your CI tool (CircleCI, GitHub Actions, etc.).
    
- Scroll to the exact point of failure (`npm install`, `build`, `test`, etc.).
    
- Look for:
    
    - Error messages
        
    - Stack traces
        
    - "Out of memory", "Command not found", "Module not found", etc.
        

---

#### 🧱 2. **Identify the Type of Failure**

Is it a:

|Type|Examples|
|---|---|
|🧩 Dependency issue|`npm install` failing, `node-gyp`, etc.|
|🧪 Test failure|Failed assertions, test timeouts|
|🧱 Build error|`tsc`, Webpack/Vite, ESLint errors|
|🔧 Tooling/env|Missing system tools, incorrect Node version|
|💥 Resource|OOM (out of memory), timeouts|

---

#### 🧼 3. **Fix Common Issues**

|Problem|Fix|
|---|---|
|🧱 **Missing build tools**|Use `-md` or `-lg` executor. Install `build-essential`, `python3`, etc.|
|🧩 **Too many dependencies**|Use caching (`npm ci`, `node_modules` or `.npm` cache)|
|🧪 **Test flakiness**|Increase timeout, isolate slow tests|
|⚠️ **Wrong Node version**|Set correct `NODE_VERSION` in `.nvmrc` or CI config|
|🔒 **Private package access**|Make sure tokens/env vars are set (`.npmrc`, `env:` in config)|
|💾 **Out of memory**|Use larger executor (`-md`, `-lg`) or reduce memory usage|
|📦 **Missing env vars**|Add them in CI config or secrets|

---

#### 📂 4. **Use Caching Effectively**

Add cache to reduce dependency install time and failures:

```yaml
- restore_cache:
    keys:
      - node-deps-{{ checksum "package-lock.json" }}

- run: npm ci

- save_cache:
    key: node-deps-{{ checksum "package-lock.json" }}
    paths:
      - ~/.npm
      - node_modules
```

---

#### 🔄 5. **Re-run with SSH (if available)**

Use CI tool's “Re-run with SSH” to:

- SSH into the job container
    
- Debug manually (`npm install`, `node`, etc.)
    
- Try fixes interactively
    

---

#### 🧪 6. **Test Locally with CI Environment**

Replicate CI locally:

```bash
docker run -it --rm -v $PWD:/app -w /app cimg/node:20.10 bash
```

Then run:

```bash
npm ci && npm run build && npm test
```

---

#### 🚀 7. **Commit and Push Fix**

Once the issue is fixed:

- Commit
    
- Push
    
- Watch the CI rerun and (hopefully) pass 🎉
    

---

Just to confirm - when we add new dependencies to `package.json`, does the installer use the existing cache for previously installed packages and only fetch the new ones, or does adding new dependencies cause it to ignore the cache and reinstall everything?


### ✅ **What Happens When You Add a New Dependency in `package.json`?**

#### 🤖 In CI (e.g., CircleCI, GitHub Actions):

It **depends on how your CI is set up**, especially how you configure caching and installation. Here's what typically happens:

---

### 📦 **If You're Using `npm ci`:**

- **Always does a clean install**.
    
- **Ignores `node_modules` completely** (doesn't reuse partial installs).
    
- Only uses the **`package-lock.json`** to install exact versions.
    
- ✅ Best for CI because it's deterministic and clean.
    

**⚠️ What about caching?**

- CI can cache **`~/.npm`** (the _npm cache_, not `node_modules`) to speed up installs.
    
- If you **add a new dependency**, `npm ci` still downloads _only the new package_ (from cache or registry) and installs all packages fresh.
    

---

### 📦 **If You're Using `npm install`:**

- It tries to **reuse `node_modules`** if present.
    
- If cache is restored correctly:
    
    - It uses the cached `node_modules`
        
    - Installs only missing/new packages
        
- ✅ Faster, but ⚠️ can cause inconsistent builds.
    

---

### 🚀 **In CI Setup (e.g., CircleCI), This Happens:**

1. **Restore cache** using a key like:
    
    ```yaml
    node-deps-{{ checksum "package-lock.json" }}
    ```
    
2. **Run install** (usually `npm ci`)
    
3. **Save new cache** with updated key
    

So if `package-lock.json` changes (which it does when you add dependencies), then:

- **Cache miss happens**
    
- CI installs everything fresh
    
- Then stores a new cache for future runs
    

---

### 🧠 TL;DR Summary

|Question|Answer|
|---|---|
|Will it reuse cache if I add a new dep?|❌ Not fully. Adding a dep changes `package-lock.json`, causing a cache **miss** if your key uses its checksum.|
|Does it redownload everything?|✅ Yes, if `npm ci` is used. But it **may reuse `.npm` cache** to avoid downloading from the internet.|
|Should I use `npm ci` in CI?|✅ Yes, it's safer, cleaner, and designed for CI use.|
|Can I optimize caching?|✅ Cache `~/.npm` to reduce download time; avoid caching `node_modules` unless you know what you're doing.|

---

Let me know what CI you're using — I can share an exact YAML example tailored to that.

