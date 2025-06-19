
## 📚 Offset Pagination in Real-World APIs: Pitfalls & Solutions

Offset-based pagination (`?page=2&limit=20` or `?offset=40&limit=20`) is simple, widely used, and supported across databases and APIs. But in **real-world dynamic systems**, where data constantly changes, it introduces **serious challenges**.

Let’s dive deep into how it works, why it breaks, and what you can do about it.

---

### 📦 How Offset Pagination Works

Offset pagination skips a number of records before returning results:

```
GET /reviews?offset=20&limit=10
---> Skips first 20, returns next 10
```

This is typically translated to SQL:

```sql
SELECT * FROM reviews ORDER BY created_at DESC LIMIT 10 OFFSET 20;
```

It’s fast to implement and good for:

- Admin dashboards
    
- Static datasets
    
- Pagination UIs with "go to page 10"
    

---

### 🔥 Why Offset Pagination Breaks in Live Systems

In a real-time system (e.g., reviews being added/deleted frequently), **data between pages shifts** as the user paginates:

#### Example:

- User requests page 1 (offset=0)
    
    - Reviews: `R1, R2, R3, ..., R10`
        
- A new review `R0` is inserted just after
    
- User requests page 2 (offset=10)
    
    - Reviews: `R11, R12...` ← but _R10_ has shifted to offset 11!
        

🔁 Result: **R10 is skipped**, or some records may appear **twice or disappear**.

---

### 🧠 Real-World Impact

- **Inconsistent UX**: Users may miss or see duplicated items.
    
- **Data integrity issues** in exports, syncs, and audits.
    
- **High fragility** in frequently updated datasets (reviews, messages, logs).
    

---

### ✅ Fixes & Workarounds

#### 1. **Use Stable Sort with Tie-Breaker**

Always **sort by an immutable field** like `created_at`, and use a **unique ID** as a tiebreaker:

```sql
ORDER BY created_at DESC, id DESC
```

Helps keep ordering stable even if data shifts.

---

#### 2. **Use `WHERE created_at < last_seen_time` Pagination** (a.k.a. keyset/cursor-based)

This is **cursor-based pagination**:

```
GET /reviews?before=2024-06-01T12:00:00Z
```

```sql
SELECT * FROM reviews
WHERE created_at < '2024-06-01T12:00:00Z'
ORDER BY created_at DESC
LIMIT 10;
```

✅ Benefits:

- Immune to inserts/deletes
    
- Faster performance (especially with indexes)
    
- Consistent user experience
    

---

#### 3. **Snapshot the Data (Soft Lock)**

For certain use cases (like data exports or reports), take a snapshot:

- Store the current max `updated_at` or `id`
    
- Use that as a filter for pagination
    
- Guarantees consistency across all pages
    

---

#### 4. **Invalidate Paginated Views Quickly**

In highly dynamic systems, consider invalidating or refreshing pagination cache frequently (e.g., on first few pages).

---

### 🚦 When Offset Pagination is Still Fine

- Data doesn't change often
    
- You just need rough navigation (e.g., "next", "previous")
    
- You _don't_ require perfect consistency
    

For these, combine offset with stable sort:

```sql
ORDER BY created_at DESC, id DESC
LIMIT 20 OFFSET 40
```

---

### 🧭 Summary

|Feature|Offset Pagination|Cursor Pagination|
|---|---|---|
|Easy to implement|✅ Yes|❌ Harder|
|Handles dynamic data well|❌ No|✅ Yes|
|Supports jumping to page N|✅ Yes|❌ No|
|Performance on large pages|❌ Slower|✅ Faster|
|Consistent UX|❌ Risky|✅ Consistent|

---

### 🧩 Final Thought

> Offset pagination is not broken—but **it’s a poor fit for fast-changing data**.  
> If consistency matters, use **cursor-based pagination** with a stable `created_at` field.

---

