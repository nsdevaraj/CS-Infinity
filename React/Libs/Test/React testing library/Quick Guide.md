
# ✅ **React Testing Library + Vitest — The Clean, Complete Guide**

Vitest is a blazing-fast test runner and assertion library designed for Vite projects. When combined with **React Testing Library (RTL)**, it creates a powerful and modern testing stack that’s fast, focused on user interactions, and easy to maintain.

---

## 📦 1. Installation (RTL + Vitest)

Install testing dependencies:

```bash
npm install --save-dev vitest jsdom @testing-library/react @testing-library/user-event @testing-library/jest-dom
```

Add TypeScript support (if needed):

```bash
npm install --save-dev @types/testing-library__react
```

---

## ⚙️ 2. Configure Vitest for React

In your `vite.config.ts` or `vite.config.js`:

```ts
/// <reference types="vitest" />
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: './src/setupTests.ts',
    globals: true,
  },
});
```

Create `src/setupTests.ts`:

```ts
import '@testing-library/jest-dom';
```

Now you’re ready to write user-focused tests with Vitest + RTL!

---

## 🧠 3. RTL + Vitest Basics

```tsx
// Counter.test.tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Counter from './Counter';

test('increments count on click', async () => {
  render(<Counter />);
  
  const button = screen.getByRole('button', { name: /increment/i });
  await userEvent.click(button);
  
  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```

---

## 🔍 4. Queries Recap (Best to Worst)

|Query Type|Usage Example|
|---|---|
|`getByRole`|`getByRole('button', { name: /submit/i })`|
|`getByLabelText`|`getByLabelText(/username/i)`|
|`getByPlaceholderText`|`getByPlaceholderText(/email/i)`|
|`getByText`|`getByText(/welcome/i)`|
|`getByDisplayValue`|`getByDisplayValue('john@example.com')`|
|`getByTestId`|`getByTestId('custom-element')` _(last resort)_|

---

## 🔄 5. Async Testing with Vitest

```tsx
test('loads user data', async () => {
  render(<UserProfile />);

  expect(screen.getByText(/loading/i)).toBeInTheDocument();

  const user = await screen.findByText(/john doe/i);
  expect(user).toBeInTheDocument();
});
```

Use:

- `findBy*` to wait for DOM elements
- `waitFor()` to wait for arbitrary conditions
- `waitForElementToBeRemoved()` for loaders/spinners


---

## 🧍 6. Simulate Real Users with `userEvent`

Prefer `userEvent` over `fireEvent`:

```tsx
await userEvent.type(screen.getByRole('textbox'), 'hello');
await userEvent.click(screen.getByRole('button', { name: /submit/i }));
```

---

## 🧪 7. Example: Login Form

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import LoginForm from './LoginForm';

test('shows error on invalid login', async () => {
  render(<LoginForm />);

  await userEvent.type(screen.getByLabelText(/username/i), 'wronguser');
  await userEvent.type(screen.getByLabelText(/password/i), 'wrongpass');
  await userEvent.click(screen.getByRole('button', { name: /log in/i }));

  expect(await screen.findByText(/invalid credentials/i)).toBeInTheDocument();
});
```

---

## 🌐 8. Mocking Fetch or API Calls in Vitest

Use `vi.fn()` or Mock Service Worker (MSW):

```ts
global.fetch = vi.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ username: 'john' }),
  })
);
```

Or use MSW for realistic API mocking:  
👉 [https://mswjs.io/](https://mswjs.io/)

---

## 🧼 9. Test Cleanup

- Vitest + RTL automatically clean up DOM between tests.
- You can call `unmount()` manually if needed.
- Use `beforeEach()` and `afterEach()` for setup/teardown.


---

## 🔁 10. Coverage & CI

Enable coverage reporting:

```bash
npx vitest --coverage
```

Supports out of the box formats:

- text
- lcov
- HTML


CI support:

- GitHub Actions
- GitLab CI/CD
- Vercel/Netlify build hooks


---

## 🏆 Best Practices Recap

✅ Do:

- Test user behavior, not internal logic
- Use `getByRole`, `getByLabelText`, etc.
- Use `userEvent` over `fireEvent`
- Mock APIs and isolate units
- Write focused, independent tests


❌ Don’t:

- Test internal component state or refs
- Overuse `getByTestId`
- Write overly broad or fragile tests
- Depend on timers or animations (use `vi.useFakeTimers()` if needed)


---

## 🧭 Summary

|Feature|React Testing Library + Vitest|
|---|---|
|Speed|⚡ Blazing-fast|
|Philosophy|✅ User-focused|
|Mocking|✅ vi.fn(), MSW supported|
|Async-ready|✅ `findBy*`, `waitFor`|
|CI/CD integration|✅ Easy with GitHub Actions, etc.|

---

## 📄 Download the Doc

Here is your full document in Markdown format — ready to paste into Notion, GitHub, or convert to PDF:

---

### ✅ [React Testing Library + Vitest — Full Markdown Documentation](sandbox:/mnt/data/React-Testing-Library-with-Vitest.md)

> Let me know if you’d like a **PDF version**, or to extend this guide with examples for Redux, React Query, Zustand, MSW, or CI workflows like GitHub Actions.