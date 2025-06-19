

## 🔍 Case Sensitivity in URLs: What Developers Must Know

When designing or consuming web APIs, understanding **URL case sensitivity** is critical. While it may seem like a minor detail, improper handling can lead to inconsistent behavior, broken links, and poor developer experience.

---

### 🚨 Are URLs Case-Sensitive?

**Yes, but not entirely.**

|URL Component|Case-Sensitive?|Notes|
|---|---|---|
|**Protocol** (`https`)|❌ No|Treated as lowercase|
|**Domain** (`example.com`)|❌ No|Domain names are case-insensitive|
|**Path** (`/api/Users`)|✅ Yes|Paths _are_ case-sensitive by standard|
|**Query Param Keys** (`?userId`)|❌ No (mostly)|Most servers treat keys as case-insensitive|
|**Query Param Values** (`=ABC`)|✅ It Depends|Often case-sensitive, depending on logic|
|**Fragment** (`#section`)|✅ Yes|Interpreted by browser only|

---

### ✅ What Most Systems Do

Most modern web servers behave as follows:

- **Windows-based servers (IIS)**: Treat paths as **case-insensitive**
- **Linux-based servers (Apache, NGINX)**: Treat paths as **case-sensitive**
- **Frameworks (Express, NestJS, Spring Boot)**: Default to **case-sensitive routing**

👉 That means `/api/users` and `/api/Users` might **route differently**.

---

### ⚠️ Common Pitfalls

- Broken links due to wrong casing in frontend apps.
- Duplicate route handlers (e.g., `/Users` vs `/users`).
- Hard-to-debug issues in RESTful APIs.


---

### 🎯 Best Practices

1. **Normalize URLs to lowercase** — Especially paths.
2. **Enforce consistent casing** in routes and internal linking.
3. **Redirect mismatched casing** to the canonical version.
4. **Document expected casing** for query parameters and path segments.
5. Use middleware (e.g., in Express or NestJS) to normalize requests if needed.

---

### 🧰 In NestJS

You can enforce lowercase routes using middleware:

```ts
app.use((req, res, next) => {
  req.url = req.url.toLowerCase(); // Normalize path
  next();
});
```

---

### 🔚 Conclusion

> While URLs _can_ be case-sensitive, **they shouldn’t be in practice**.  
> Consistency, predictability, and resilience are more important than rigid specification.

**TL;DR**: Treat **domains and query keys** as case-insensitive, and **normalize paths to lowercase** wherever possible.

---
