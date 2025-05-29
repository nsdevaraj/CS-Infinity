

Pagination is the process of dividing content into discrete pages, essential for performance, usability, and data navigation in web and mobile apps. There are **three main types**:

1. **Offset-based Pagination**
2. **Cursor-based Pagination**
3. **Keyset Pagination (a variation of Cursor-based)**
4. **Infinite Scroll (a UI-centric approach)**


---

## 1. 📖 **Offset-based Pagination**

### 📌 How It Works:

You fetch items by using an `OFFSET` and `LIMIT`.

```sql
SELECT * FROM posts ORDER BY created_at DESC LIMIT 10 OFFSET 30;
```

### ✅ Pros:

- Simple to implement and understand
    
- Easy to jump to any page (e.g., page 100)
    
- Works well for admin dashboards, data tables
    

### ❌ Cons:

- Slow with large datasets (high OFFSET is costly)
    
- Duplicate or missing records possible if data changes (non-deterministic)
    
- Bad for real-time or frequently updated feeds
    

### 💡 Best Use Cases:

- Static datasets (e.g., product catalogs, archived content)
    
- UIs that require page numbers (pagination controls)
    

---

## 2. 🔑 **Cursor-based Pagination (a.k.a. Seek Pagination)**

### 📌 How It Works:

Uses a unique, ordered field (like an ID or timestamp) as a cursor.

```sql
SELECT * FROM posts 
WHERE created_at < '2023-01-01 00:00:00' 
ORDER BY created_at DESC 
LIMIT 10;
```

You pass the last seen `created_at` as a cursor to fetch the next page.

### ✅ Pros:

- Fast and efficient at scale (no OFFSET)
    
- Consistent even if data changes (deterministic)
    
- Great for real-time apps (e.g., social feeds)
    

### ❌ Cons:

- Can't jump to arbitrary pages
    
- More complex to implement (requires cursor encoding/decoding)
    
- Requires stable sorting fields (usually unique indexes)
    

### 💡 Best Use Cases:

- Infinite scrolling (Twitter, Instagram, etc.)
    
- Real-time feeds
    
- Large datasets needing performance
    

---

## 3. 🧭 **Keyset Pagination** (Subset of Cursor-based)

### 📌 How It Works:

Uses multiple fields (compound indexes) to paginate deterministically.

```sql
SELECT * FROM posts
WHERE (created_at, id) < ('2023-01-01', 1001)
ORDER BY created_at DESC, id DESC
LIMIT 10;
```

This ensures uniqueness and proper ordering.

### ✅ Pros:

- Resolves tie-breaker issues in cursor pagination
    
- Ultra-performant, especially with composite indexes
    

### ❌ Cons:

- Complex SQL and logic
    
- Can’t go to arbitrary pages
    
- Requires thought-out indexes
    

### 💡 Best Use Cases:

- High-throughput systems (e.g., financial transactions)
    
- Pagination with non-unique timestamps
    
- Feeds where consistent order is crucial
    

---

## 4. 🔁 **Infinite Scroll** (UI-driven pattern)

### 📌 How It Works:

Automatically fetches more data as the user scrolls down, usually with **cursor-based** backend.

### ✅ Pros:

- Seamless, modern UX
    
- Encourages exploration (used in social media)
    

### ❌ Cons:

- Hard to bookmark/share positions
    
- Performance hits on very long sessions
    
- Harder to implement accessibility, SEO, or print support
    

### 💡 Best Use Cases:

- Mobile-first apps
    
- Social media, image feeds, recommendation engines
    

---

## 📊 Comparison Table

|Feature / Type|Offset-based|Cursor-based|Keyset Pagination|Infinite Scroll|
|---|---|---|---|---|
|Jump to page|✅ Easy|❌ Not possible|❌ Not possible|❌ Not possible|
|Performance (Large Datasets)|❌ Poor|✅ Excellent|✅ Excellent|✅ Excellent|
|Consistency w/ updates|❌ Fragile|✅ Strong|✅ Strong|✅ Strong|
|Implementation Ease|✅ Simple|⚠️ Moderate|❌ Complex|⚠️ Moderate|
|User Experience|⚠️ Traditional|⚠️ Backend only|⚠️ Backend only|✅ Fluid|
|Best Use|Data tables|Feeds, APIs|Transaction logs|Mobile/social feeds|

---

## ✅ Summary of Use-Case Mapping

|Scenario|Best Pagination Type|
|---|---|
|Admin dashboards with page numbers|Offset-based|
|APIs with large datasets|Cursor-based|
|Sorted feeds (posts, comments, updates)|Cursor-based or Keyset|
|Paginating real-time events|Keyset|
|Social/infinite feeds (Instagram, TikTok)|Cursor + Infinite Scroll|
|SEO or deep-linking required|Offset-based|

---

## ⚡ Final Thoughts

- **Offset-based** is great for simplicity and static data.
- **Cursor/Keyset** is ideal for dynamic, large-scale, high-performance systems.
- **Infinite scroll** enhances UX but needs a solid backend (preferably cursor/keyset).
    

> 🎯 **Rule of Thumb:**  
> If you need **performance**, go **Cursor/Keyset**.  
> If you need **user control** (page numbers), go **Offset**.  
> If you need **immersion**, go **Infinite Scroll** (but back it with Cursor/Keyset).

---

more nice points:

https://dev.to/pragativerma18/unlocking-the-power-of-api-pagination-best-practices-and-strategies-4b49

https://www.merge.dev/blog/rest-api-pagination

https://nordicapis.com/restful-api-pagination-best-practices/


---
