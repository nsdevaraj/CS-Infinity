

While **Orval** is one of the best options for generating typed API clients from OpenAPI specs (especially for React + TypeScript), there are a few strong alternatives depending on your **project needs**, **tooling preferences**, or **runtime (Node, browser)**.

---

## 🔝 Top Alternatives to Orval

### 1. **OpenAPI Generator**

**💡 Best for:** Language-agnostic code generation

- **Supports 50+ languages** (TypeScript, Java, Go, Python, etc.)
    
- Can generate **Angular/Fetch/Axios** clients
    
- CLI tool, highly customizable
    
- Requires more setup than Orval
    
- Less React-query-specific support
    

🔗 [https://openapi-generator.tech/](https://openapi-generator.tech/)

---

### 2. **Swagger Codegen**

**💡 Best for:** Backend or full-stack teams already using Swagger tooling

- Predecessor to OpenAPI Generator (more stable, less modern)
    
- Generates client/server code from Swagger/OpenAPI specs
    
- Less modern TypeScript support than others
    

🔗 [https://github.com/swagger-api/swagger-codegen](https://github.com/swagger-api/swagger-codegen)

---

### 3. **Autorest**

**💡 Best for:** Microsoft ecosystem or Azure APIs

- Built by Microsoft, supports TypeScript, C#, Python, etc.
    
- Heavily used for Azure SDKs
    
- Steeper learning curve
    
- Not focused on React Query
    

🔗 [https://github.com/Azure/autorest](https://github.com/Azure/autorest)

---

### 4. **zodios**

**💡 Best for:** Zod + TypeScript users who prefer runtime validation

- Define endpoints using **Zod** first, then generate typed clients
    
- OR use a plugin to convert OpenAPI → Zodios
    
- Smaller ecosystem, more flexibility
    
- Doesn’t support auto-generating hooks like Orval
    

🔗 [https://zodios.dev/](https://zodios.dev/)

---

### 5. **Restful-react**

**💡 Best for:** React projects wanting GraphQL-like data fetching via REST

- Uses OpenAPI or manual endpoint declarations
    
- Generates React Query-like hooks
    
- TypeScript-first, minimal config
    
- Less active development compared to Orval
    

🔗 [https://github.com/contiamo/restful-react](https://github.com/contiamo/restful-react)

---

### 6. **oazapfts**

**💡 Best for:** Projects using Fetch and OpenAPI, prefer minimalism

- OpenAPI → Fetch-based client with TS types
    
- Functional-style usage (`getPetById()`)
    
- Inspired by `axios`, smaller footprint
    
- No hook generation like Orval
    

🔗 [https://github.com/cellular/oazapfts](https://github.com/cellular/oazapfts)

---

## 🧠 Comparison Table

| Tool              | Hook Gen | Typed | Mocking | Zod Support  | React Focus | Ease of Use |
| ----------------- | -------- | ----- | ------- | ------------ | ----------- | ----------- |
| **Orval**         | ✅        | ✅     | ✅ (MSW) | ✅ (optional) | ✅           | ⭐⭐⭐⭐⭐       |
| OpenAPI Generator | ❌        | ✅     | ❌       | ❌            | ❌           | ⭐⭐⭐         |
| Zodios            | ❌        | ✅     | ❌       | ✅ (core)     | ❌           | ⭐⭐⭐⭐        |
| Restful-react     | ✅        | ✅     | ❌       | ❌            | ✅           | ⭐⭐⭐⭐        |
| oazapfts          | ❌        | ✅     | ❌       | ❌            | ❌           | ⭐⭐⭐⭐        |

---

## ✅ When to Use Orval

Use **Orval** if:

- You want auto-generated React Query hooks
    
- You’re using OpenAPI
    
- You want type safety + optional Zod support + mocking
    
- You prefer minimal config
    

---

## ❓ When to Consider Alternatives

- Want more control → use **OpenAPI Generator**
    
- Need runtime validation via Zod → try **Zodios**
    
- Building a backend as well → use **Swagger Codegen**
    
- Not using React Query → consider **oazapfts** or **Restful-react**
    

---
