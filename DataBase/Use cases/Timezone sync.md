


---

# 🕒 How to Store Time Correctly in Your Application — The Right Way to Handle Timestamps

Whether you're building a web app, mobile service, or backend system — dealing with **timestamps** is inevitable. But there’s one common pitfall that silently breaks filtering, sorting, comparisons, and even user trust: **misunderstanding how to store time**.

Let’s unpack the real issue and learn how to do it right — across **any stack** (PostgreSQL, MySQL, MongoDB, Drizzle, Prisma, Firebase, etc.).

---

## 🧠 First: Understand What You're Actually Storing

There are **two kinds of time values**:

### 1. **Absolute time** (a real event)

This represents a **specific point on the global timeline**, like:

> "The review was created at 2025-06-26 09:00 AM in Boston (UTC-4)"

This is **timezone-aware**. If a user in India views it, they should see it in their own time zone — the **actual moment** stays the same.

### 2. **Local time** (a recurring schedule)

This represents a **time without a place**, like:

> "Show the banner every day at 9:00 AM local time"

No time zone is attached. It’s just a label — the app must interpret it based on context (e.g. user location).

---

## ⚠️ The Core Problem

Many systems **store time without clarity** — e.g. just `"2025-06-26 09:00:00"` — but then try to apply time zone logic during display. This leads to bugs like:

- Wrong sorting
    
- Incorrect daily groupings
    
- “Yesterday’s data” being shown as “today’s”
    
- Inconsistent user experiences
    

---

## ✅ Best Practice: Store Time as UTC

No matter your stack:

> Always store **absolute timestamps** in UTC  
> Convert to local time only when displaying it

This applies whether you're using:

- **PostgreSQL** → `TIMESTAMPTZ`
    
- **MySQL** → `DATETIME` + enforce UTC manually
    
- **MongoDB** → ISODate stored in UTC
    
- **Firebase** → `Timestamp` in UTC
    
- **ORMs** like Prisma, Drizzle, Sequelize → use UTC-mode fields
    

---

## 🌍 Example: Why This Matters

Imagine a user in Boston (UTC-4) posts a review at 9 AM local time.

If stored as:

|Format|Stored Value|What You See in India (UTC+5:30)|
|---|---|---|
|**UTC** (correct)|`2025-06-26T13:00:00Z`|`6:30 PM IST`|
|**Without time zone**|`2025-06-26 09:00:00`|still `9:00 AM` unless manually corrected|

The second case **lies about the actual time** — and that breaks features like charts, activity logs, notifications, etc.

---

## 🧱 How This Looks in Practice (Drizzle + PostgreSQL)

### ✅ Correct way (with time zone)

```ts
timestamp('review_created_at', {
  mode: 'string',
  withTimezone: true,
}).notNull();
```

This maps to `TIMESTAMPTZ`, which:

- Accepts timezone input (`2025-06-26T13:00:00Z`)
    
- Normalizes and stores as UTC
    
- Converts correctly during queries or display
    

### ⚠️ Incorrect way (no time zone)

```ts
timestamp('review_created_at', { mode: 'string' }) // default = no time zone
```

This stores `2025-06-26 09:00:00` **without knowing where** it occurred — making it impossible to reliably display or compare.

---

## 🛠 Converting & Displaying Time

Always format time based on user locale at the **presentation layer**:

```ts
new Date(utcTime).toLocaleString('en-US', {
  timeZone: 'America/New_York',
});
```

Or with libraries like **date-fns**, **dayjs**, or **luxon** for more control.

---

## 💬 What About Scheduled or Repeating Times?

If you’re storing things like:

- “Send email every day at 9:00 AM local time”
    
- “Open at 8:30 AM no matter where the user is”
    

You may need to store **local times only** — no UTC conversion — along with **context** like time zone:

```json
{
  "hour": 9,
  "minute": 0,
  "timezone": "America/Los_Angeles"
}
```

Or use a second field for scheduling logic.

---

## ✅ TL;DR: Rules of Thumb

|Use Case|How to Store Time|
|---|---|
|Real-world events (reviews, logs)|Store in **UTC**, use **timezone-aware** fields|
|Recurring schedules (daily times)|Store as **local time**, keep time zone info|
|Cross-timezone apps (global users)|Store all times in UTC, convert for display|
|Same-timezone app|You might get away with naive time, but it’s risky|

---

## 🧠 Final Take

Time zones are hard — but they’re not optional in global apps.  
**Store time with clarity**, and your features will behave consistently across the globe.

If your system touches real-world timestamps — treat them like real-world money:

> Always store them in a universal format, and convert at the edge.

---
