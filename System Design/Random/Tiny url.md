
# 🚀 System Design: Designing a Scalable TinyURL Service

Designing a URL shortening service like **TinyURL** is a **classic system design interview question** that tests your ability to balance simplicity, scalability, and reliability. In this article, we’ll walk through a complete and scalable design, explore various trade-offs, and provide insights into what interviewers typically look for.

---

## 🧩 Functional Requirements

The requirements are deceptively simple:

- **Create a short URL** when provided with a long URL.
    
- **Redirect to the original long URL** when a short URL is visited.
    

---

## 🛡 Non-Functional Requirements

- **Low latency**: Redirections should be near-instantaneous.
    
- **High availability**: The service should be resilient and fault-tolerant.
    
- **Scalability**: Must support billions of URLs and high read/write throughput.
    
- **Uniqueness**: Each short URL must map to one unique long URL.
    
- **Analytics (Optional)**: Track usage stats like click count, user location, etc.
    

---

## 📬 API Design (RESTful)

|Method|Endpoint|Description|Request Payload / Params|Response|
|---|---|---|---|---|
|POST|`/shorten`|Create a short URL|`{ "long_url": "..." }`|`201 Created { "short_url": "..." }`|
|GET|`/{short_url}`|Redirect to the long URL|URL path param|`301 Redirect` to original URL|

---

## 🗃 Data Schema

```sql
TABLE UrlMappings (
    short_url VARCHAR(10) PRIMARY KEY,
    long_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    click_count INT DEFAULT 0,
    user_ip TEXT,
    country TEXT
)
```

---

## 🔐 How Short Should the URL Be?

We determine this by estimating **scale**:

Assume the system handles:

- `1,000` new URLs/second
    
- Over a year:  
    `1,000 * 60 * 60 * 24 * 365 = ~31.5 billion URLs/year`
    

Now using a **Base62 encoding** (`A-Z`, `a-z`, `0-9` = 62 characters), the total combinations are:

|Length|Combinations|
|---|---|
|6|62⁶ ≈ 56 billion|
|7|62⁷ ≈ 3.5 trillion|

🟢 **Conclusion**: Use **7-character** short URLs to comfortably support billions of URLs for years.

---

## 🧠 Naive Architecture

```plaintext
Client --> Load Balancer --> Web Server --> DB
                                  |
                             Redirect to long URL
```

This **works for small scale**, but lacks:

- **Caching** → Slows down under high read load.
    
- **Scalability** → Single DB becomes a bottleneck.
    
- **Fault Tolerance** → No redundancy.
    

---

## 🧱 Adding a Cache Layer

```plaintext
Client --> Load Balancer --> Web Server
                                  |
                              Redis / Memcached
                                  |
                                Database
```

✅ **Improves performance**  
❌ But we still have a **central counter** problem for ID generation.

---

## 💥 Problem: Counter Collision

When multiple servers generate short URLs from the same counter, **collisions** can occur.

---

## 🦺 Solution: Distributed ID Generation with Zookeeper

Instead of a global counter, use **Zookeeper + Ranges**.

### 🧠 How it works:

- Each web server **requests a range** (e.g., 1M IDs) from Zookeeper.
    
- Converts the numeric ID to **Base62** to form the short URL.
    
- Ensures **no two servers generate overlapping IDs**.
    

```plaintext
Zookeeper -- gives range --> Web Server
Web Server -- encodes --> Base62 --> Short URL
```

### 🔒 What if a server dies with unused range?

That range is lost (e.g., 1M wasted). But with 3.5 trillion possible IDs, this is acceptable.

---

## 🗂 Database Selection

**Tradeoffs:**

- **SQL** (PostgreSQL with sharding): Strong consistency but harder to scale.
    
- **NoSQL** (e.g., **Cassandra**, DynamoDB): Better for horizontal scale and availability.
    

📌 For this case:

- Use **Cassandra** for write-heavy, high-scale workloads.
    
- Use **Redis** or **Memcached** to cache popular short URLs.
    

---

## 🔁 Flow Diagrams

### 🔨 URL Creation Flow (POST /shorten)

```plaintext
Client --> Load Balancer --> Web Server
          |                   |
          |<-- Check Cache ---|
                              |
        Web Server checks DB / assigns ID
                              |
          Stores (short, long) in DB + Cache
                              |
                   Returns short URL
```

### ↪️ Redirection Flow (GET /{short_url})

```plaintext
Client --> Load Balancer --> Web Server
                              |
                     Check Redis for short URL
                              |
                   If cache miss --> DB lookup
                              |
                       Return 301 redirect
```

---

## 📈 Analytics (Optional)

- Track `clicks`, `IP addresses`, `geo-location`.
    
- Use for **caching strategies** (e.g., hot URLs).
    
- Enable **monitoring** of spam/abuse patterns.
    

---

## ⛔ Security Considerations

- **Predictability**: Sequential IDs make short URLs guessable.
    
    - ➕ Solution: Add **random characters** or **hash long URLs** (e.g., SHA256 + truncation).
        
- **Abuse**: Rate-limit API usage to avoid spam and DDoS.
    
- **Expiration**: Optionally expire unused URLs after a time.
    

---

## 🎯 Interview Tips

|Area|What Interviewers Want|
|---|---|
|API Design|Clear, RESTful endpoints, proper responses|
|Encoding Scheme|Base62, length estimation, ID uniqueness|
|Scalability|Avoid SPOF, horizontal scaling|
|Data Modeling|SQL vs NoSQL trade-offs|
|Caching Strategy|Hotkey problem, eviction policy|
|ID Generation|Collision avoidance, Zookeeper/UUIDs|
|Fault Tolerance|What happens on server crash or failure|
|Optional Enhancements|Analytics, rate-limiting, TTL|

---

## 📌 Extra Enhancements

- **Custom Aliases**: Allow users to request a custom short URL.
    
- **Preview Page**: Show a preview instead of auto-redirecting.
    
- **Link Expiry**: Option to expire URLs after X days or views.
    
- **User Auth**: Allow logged-in users to manage links.
    

---

## 🧾 Final Notes

This system is a **robust, production-level** design for TinyURL, balancing performance and simplicity. In interviews, your ability to discuss **trade-offs**, propose **incremental improvements**, and demonstrate **scaling foresight** will help you stand out.

---

## 📌 Summary Architecture

```plaintext
                +--------------------+
                |    Load Balancer   |
                +--------+-----------+
                         |
         +---------------+------------------+
         |               |                  |
+--------v-----+  +------v------+   +-------v------+
| Web Server 1 |  | Web Server 2|   | Web Server N |
+--------------+  +-------------+   +--------------+
      |                |                   |
+-----v--+       +-----v--+         +------v------+
|  Cache |       | Zookeeper |       |   Database   |
| Redis  |       | (Range ID) |       |  Cassandra  |
+--------+       +-----------+       +-------------+
```

---

If you'd like this turned into a downloadable PDF with visuals or prepared as a slide deck, just let me know!



referred {

https://youtu.be/Cg3XIqs_-4c

}