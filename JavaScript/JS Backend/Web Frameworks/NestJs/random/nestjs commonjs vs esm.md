
Switching a **NestJS** project to **ESM (ECMAScript Modules)** is possible but requires a few deliberate changes, because NestJS is traditionally structured around **CommonJS**. Below is a step-by-step guide to migrate your NestJS project to ESM.

---

### ✅ Step-by-Step: Convert NestJS to ESM

---

### 1. **Update `package.json`**

```json
{
  "type": "module",
  "main": "dist/main.js",
  "scripts": {
    "start": "node dist/main.js",
    "build": "tsc"
  }
}
```

---

### 2. **Update `tsconfig.json`**

```json
{
  "compilerOptions": {
    "module": "ESNext",
    "target": "ES2020",
    "moduleResolution": "node",
    "outDir": "./dist",
    "declaration": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "skipLibCheck": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true,
    "resolveJsonModule": true
  }
}
```

✅ Use `"ESNext"` for module and `"node"` for module resolution.

---

### 3. **Use `.js` extension in `import` paths**

In ESM, imports must include file extensions for local files:

```ts
// ❌ This won't work in ESM
import { AppModule } from './app.module';

// ✅ This will
import { AppModule } from './app.module.js';
```

> This applies only to local files, not to packages from `node_modules`.

---

### 4. **Rename compiled files or use `.mts` extension in source**

To keep clean build artifacts, you can:

- Rename files to `.mts` (instead of `.ts`) — useful to clearly mark ESM usage.
    
- Or configure your tooling to output `.js` files with extensions already applied.
    

---

### 5. **Avoid CommonJS-specific code**

- No `__dirname`, `__filename`, `require()`—these are not natively available in ESM.
    
- Use `import.meta.url` and `fileURLToPath()` from `url` module instead.
    

```ts
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
```

---

### 6. **Third-party packages**

Some NestJS decorators or community packages might assume CJS. Test your full app after switching. If something breaks:

- Look for ESM-compatible alternatives
    
- Consider dual-publishing (advanced) if you're writing libraries
    

---

### 🔄 Example change in `main.ts`

```ts
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module.js'; // Note the `.js` extension

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
```

---

### 🧪 Optional: Use `ts-node-esm` for dev mode

In `package.json`:

```json
{
  "scripts": {
    "start:dev": "ts-node-esm --project tsconfig.json src/main.ts"
  }
}
```

---

### ✅ Summary:

|Change|Description|
|---|---|
|`type: "module"`|Required in `package.json`|
|`module: "ESNext"`|Set in `tsconfig.json`|
|File extensions in imports|Use `.js` for local files|
|Avoid `require`, `__dirname`|Use ESM equivalents|

Would you like a sample ESM-ready NestJS starter repo or template?