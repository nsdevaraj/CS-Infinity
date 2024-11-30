


### **Section 6: Advanced Topics in Next.js**

#### **1. What is middleware in Next.js? How is it used?**

Middleware in Next.js allows you to run code before a request is processed. It enables features like authentication, redirects, and headers modification. Middleware is implemented in the `middleware.js` file at the root of your project.

**Example:**

```javascript
import { NextResponse } from 'next/server';

export function middleware(request) {
  const url = request.nextUrl;

  if (url.pathname === '/admin' && !request.cookies.get('authToken')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  return NextResponse.next();
}
```

**Key Points:**

- Middleware runs on the Edge Runtime.
- It operates at the route level for better performance.
- Use cases: Authentication, IP blocking, logging, etc.

---

#### **2. How can you use dynamic imports in Next.js?**

Dynamic imports load components or modules only when needed, improving performance.

**Example:**

```javascript
import dynamic from 'next/dynamic';

const HeavyComponent = dynamic(() => import('../components/HeavyComponent'), {
  loading: () => <p>Loading...</p>, // Optional loading state
  ssr: false, // Disable server-side rendering for this component
});

export default function Page() {
  return <HeavyComponent />;
}
```

---

#### **3. What is ISR (Incremental Static Regeneration), and how does it compare to SSR and SSG?**

|Feature|ISR|SSR|SSG|
|---|---|---|---|
|**Definition**|Updates static pages after build time.|Fetches and renders pages on request.|Pre-builds static pages during build.|
|**Performance**|Faster than SSR after caching.|Slower as it renders on demand.|Fastest due to static content.|
|**Use Case**|Frequently updated content (e.g., blogs).|Personalized or frequently changing data.|Rarely changing content.|

**Key Benefit of ISR:** Combines the performance of SSG with the flexibility of SSR by revalidating pages.

---

#### **4. What is the difference between Client-Side Rendering (CSR) and Server-Side Rendering (SSR) in Next.js?**

|Feature|Client-Side Rendering (CSR)|Server-Side Rendering (SSR)|
|---|---|---|
|**Where it runs**|Browser only.|Server and browser.|
|**Performance**|Faster initial load, slower first render.|Slower initial load, faster after rendering.|
|**Use Case**|Non-SEO critical pages.|SEO-critical, dynamic pages.|

---

#### **5. How do you handle authentication in Next.js?**

- **Client-side Authentication:** Use libraries like `next-auth` or JWT to authenticate users on the client.
- **Server-side Authentication:** Protect routes using `getServerSideProps` or middleware.

**Example with `next-auth`:**

```javascript
import { getSession } from 'next-auth/react';

export async function getServerSideProps(context) {
  const session = await getSession(context);

  if (!session) {
    return {
      redirect: { destination: '/login', permanent: false },
    };
  }

  return { props: { session } };
}

export default function ProtectedPage({ session }) {
  return <div>Welcome {session.user.name}</div>;
}
```

---

#### **6. How does Next.js support internationalization (i18n)?**

Next.js provides built-in internationalization support using the `i18n` key in `next.config.js`:

**Example:**

```javascript
module.exports = {
  i18n: {
    locales: ['en', 'fr', 'es'],
    defaultLocale: 'en',
  },
};
```

**Usage in pages:**

```javascript
import { useRouter } from 'next/router';

export default function Page() {
  const { locale } = useRouter();

  return <p>Current locale: {locale}</p>;
}
```

---

#### **7. What is API Route Rate Limiting in Next.js?**

Rate limiting is controlling the number of requests users can make to API routes.

**Example:**

```javascript
let requestCount = 0;

export default function handler(req, res) {
  if (requestCount > 10) {
    res.status(429).json({ error: 'Too many requests' });
  } else {
    requestCount++;
    res.status(200).json({ message: 'Request allowed' });
  }
}
```

---

#### **8. How can you integrate GraphQL in Next.js?**

Use libraries like Apollo Client or Relay to integrate GraphQL.

**Example with Apollo:**

```javascript
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';

const client = new ApolloClient({
  uri: 'https://api.example.com/graphql',
  cache: new InMemoryCache(),
});

function MyApp({ Component, pageProps }) {
  return (
    <ApolloProvider client={client}>
      <Component {...pageProps} />
    </ApolloProvider>
  );
}

export default MyApp;
```

---

#### **9. How do you create a custom 500 error page in Next.js?**

Create a file named **`pages/500.js`** for handling internal server errors.

**Example:**

```javascript
export default function Custom500() {
  return <h1>500 - Something went wrong</h1>;
}
```

---

#### **10. How does Next.js handle Static Site Generation with dynamic content?**

Dynamic routes use **`getStaticPaths`** to generate pages based on available data.

**Example:**

```javascript
export async function getStaticPaths() {
  const res = await fetch('https://api.example.com/items');
  const items = await res.json();

  return {
    paths: items.map((item) => ({ params: { id: item.id.toString() } })),
    fallback: 'blocking',
  };
}

export async function getStaticProps({ params }) {
  const res = await fetch(`https://api.example.com/items/${params.id}`);
  const item = await res.json();

  return { props: { item } };
}
```

---

Would you like a **Next.js Debugging and Testing** section or another topic?