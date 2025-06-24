

## 🚀 What is Orval?

**Orval** is a code generator that creates fully typed API clients (using Axios or Fetch) directly from an **OpenAPI** spec.

It reduces boilerplate, ensures type safety, and keeps your API client always in sync with the backend.

📦 [Orval GitHub →](https://github.com/anymaniax/orval)

---

## 🛠️ Key Features

✅ Generates API hooks (`useQuery`, `useMutation`) for React Query  
✅ Supports Axios and Fetch  
✅ Strong TypeScript support  
✅ Handles request/response typing  
✅ Auto-generates Zod validators (optional)  
✅ Supports mocking endpoints (for local dev)

---

## 📦 Installation

```bash
npm install --save-dev orval
# or
yarn add --dev orval
```

---

## 📄 1. Create `orval.config.ts`

Here’s a sample config:

```ts
export default {
  petstore: {
    input: 'https://petstore.swagger.io/v2/swagger.json', // or a local file
    output: {
      target: './src/api/petstore.ts',
      client: 'react-query', // or 'axios', 'fetch'
      schemas: './src/api/model',
      mock: true,
    },
  },
};
```

💡 Supports multiple APIs too (just add more keys).

---

## ⚙️ 2. Run Orval

```bash
npx orval
```

Or add to `package.json`:

```json
"scripts": {
  "generate:api": "orval"
}
```

This generates:

- Typed API functions (with Axios/Fetch)
    
- React Query hooks
    
- Typed schemas/interfaces
    

---

## 💡 Usage Example (React Query)

After generation:

```tsx
import { useGetPetById } from '../api/petstore';

export const PetDetails = ({ id }: { id: number }) => {
  const { data, isLoading } = useGetPetById(id);

  if (isLoading) return <p>Loading...</p>;

  return <div>{data?.name}</div>;
};
```

➡️ Hooks are fully typed based on your OpenAPI schema.

---

## ✅ Bonus: Mocking with Orval

In your config:

```ts
mock: {
  properties: true,
  delay: 500,
},
```

This generates local mock handlers using `msw` (Mock Service Worker), useful for frontend development **without needing the backend**.

---

## 🔐 Bonus: Zod Integration

If you want Zod validation schemas:

```ts
output: {
  target: './api.ts',
  schemas: './schemas',
  zod: true,
}
```

Orval will generate Zod validators for each schema — perfect for validating data at runtime.

---

## 🧠 Best Practices

- ✅ Keep OpenAPI specs updated (use Swagger or NestJS/Express decorators)
    
- ✅ Use Orval for both typed client and mocks
    
- 🔁 Automate `npx orval` via prebuild or CI
    
- 📁 Keep generated code in `/api` or `/services/api` folders
    

---

## 🧪 Perfect With...

- 🔹 React Query (preferred)
    
- 🔹 TanStack Query (v5+)
    
- 🔹 Zod (optional)
    
- 🔹 MSW (for mocking)
    
- 🔹 Vite or CRA setups
    

---

## 🧾 TL;DR

|Feature|Orval Does It? ✅|
|---|---|
|Typed clients|✅ Axios / Fetch|
|React Query|✅ Hooks generated|
|Zod support|✅ Optional|
|Mocking|✅ With MSW|
|TypeScript|✅ Out of the box|

---

## 📚 Useful Links

- Docs: [https://orval.dev/](https://orval.dev/)
    
- GitHub: [https://github.com/anymaniax/orval](https://github.com/anymaniax/orval)
    
- OpenAPI Spec example: [https://petstore.swagger.io/](https://petstore.swagger.io/)
    

---

