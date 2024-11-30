

### **Section 4: Performance Optimization in Next.js**

#### **1. How does Next.js optimize performance by default?**

Next.js provides several built-in performance optimizations:

- **Automatic Code Splitting:** Only the code required for a specific page is loaded.
- **Image Optimization:** Automatically resizes, compresses, and serves images in modern formats like WebP.
- **Static Generation (SSG):** Reduces server load and improves page load times.
- **Server-side Rendering (SSR):** Dynamically renders pages only when necessary.
- **Prefetching:** Automatically preloads linked pages when using the `Link` component.

---

#### **2. What is automatic code splitting in Next.js?**

Next.js automatically splits your JavaScript bundles by page, ensuring that only the code required for a specific page is sent to the client. This reduces initial load times and improves overall performance.

---

#### **3. How does Next.js handle image optimization?**

Next.js provides the `<Image>` component for optimized image loading. It resizes and serves images in efficient formats, ensuring faster page loads.

**Example:**

```javascript
import Image from 'next/image';

<Image src="/example.jpg" alt="Example" width={500} height={300} />
```

**Key Features:**

- Lazy loading by default.
- Automatically serves images in modern formats (e.g., WebP).
- Supports resizing for different screen sizes and devices.

---

#### **4. What is a critical CSS strategy in Next.js?**

Next.js extracts and inlines critical CSS for each page, ensuring that only the necessary CSS is loaded initially. This reduces render-blocking CSS and improves page load speed.

---

#### **5. How does Next.js improve caching with `Cache-Control` headers?**

Next.js automatically sets appropriate caching headers for static assets (e.g., images, scripts, CSS) and pages. Custom caching headers can also be added in `next.config.js`:

**Example:**

```javascript
module.exports = {
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          { key: 'Cache-Control', value: 'public, max-age=31536000, immutable' },
        ],
      },
    ];
  },
};
```

---

#### **6. What is ISR (Incremental Static Regeneration), and how does it improve performance?**

ISR updates static pages after build time without rebuilding the entire site. It combines the benefits of SSG and dynamic updates, ensuring fast page loads and up-to-date content.

**Example:**

```javascript
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();

  return {
    props: { data },
    revalidate: 10, // Updates the page every 10 seconds
  };
}
```

---

#### **7. How can you optimize large datasets in Next.js?**

For large datasets:

- Use pagination to fetch data in smaller chunks.
- Implement **lazy loading** for client-side components.
- Use **dynamic imports** to load non-critical parts of the app only when needed:

```javascript
const HeavyComponent = dynamic(() => import('./HeavyComponent'), { ssr: false });
```

---

#### **8. How does Next.js handle font optimization?**

Next.js automatically optimizes fonts from Google Fonts. When using `<link>` tags in `_app.js` or `_document.js`, it fetches the fonts faster and reduces layout shifts.

---

#### **9. How can you reduce bundle size in Next.js?**

- **Tree Shaking:** Remove unused imports.
- **Dynamic Imports:** Load modules only when needed.
- **Bundle Analyzer:** Use tools like `@next/bundle-analyzer` to identify and reduce large dependencies.

**Example:**

```javascript
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
});

module.exports = withBundleAnalyzer({});
```

---

#### **10. How can you use CDN and edge caching in Next.js?**

Deploying Next.js on platforms like Vercel ensures automatic edge caching of static assets and pages. You can also configure CDNs like Cloudflare or AWS CloudFront to cache content closer to users.


