

# 📘 Bulk Insert with Error Handling – MongoDB vs Postgres

---

## 1. **MongoDB**

- **Default behavior:**  
    `insertMany` fails the entire batch if one document errors.
    
- **Solution:** Use `ordered: false`
    
    ```js
    await Model.insertMany(docs, { ordered: false });
    ```
    
    - ✅ Inserts valid docs
        
    - ❌ Skips invalid ones
        
    - You can inspect `err.writeErrors` to identify failed docs.
        
- **Status tracking:** Build a success/failure list by comparing `insertedDocs` with input.
    
- **Alternative:** Use `bulkWrite` for mixed operations (`insertOne`, `deleteOne`, etc.).
    

---

## 2. **Postgres**

Postgres behaves differently:

- **Default behavior:** If any row fails (FK violation, duplicate, null, etc.), the **entire `INSERT` fails and rolls back**.
    

---

### 2.1 Handling Duplicates → `ON CONFLICT`

- Best if **only duplicate keys** are the problem.
    
- Example:
    
    ```sql
    INSERT INTO items (id, name, value)
    VALUES (1, 'apple', 10), (2, 'banana', 20)
    ON CONFLICT (id) DO NOTHING
    RETURNING id;
    ```
    
- ✅ Inserts valid rows
    
- ✅ Skips duplicates
    
- ✅ Use `RETURNING` to detect successful rows
    
- ❌ Does **not** handle FK errors, null violations, type errors, etc.
    

---

### 2.2 Handling Any Constraint Failures

If you want to **insert valid rows but skip bad ones** (e.g., FK violations, nulls, check constraints):

#### **Option A: Staging Table (Recommended for Bulk)**

1. Bulk insert into a **temporary staging table** (no constraints).
    
2. Validate rows using SQL (`JOIN` with FK tables, check conditions).
    
3. Insert only valid rows into the target table.
    
4. Collect invalid rows for error reporting.
    

✅ Keeps bulk performance  
✅ Allows detailed error reporting  
❌ Requires extra logic

#### **Option B: Row-by-Row Insert with Exception Blocks**

- Use PL/pgSQL loop with `BEGIN … EXCEPTION … END` per row.
    
- ✅ Works for any error type
    
- ❌ Slow for large batches
    

#### **Option C: Application Layer Fallback**

- Try **bulk insert first**.
    
- If it fails, fallback to **row-by-row insert** in the application (collect statuses).
    
- ✅ Best of both worlds (fast path + safe path)
    
- ❌ Requires app logic for retry/fallback
    

---

## 3. **Throwing Custom Exceptions**

You wanted bulk inserts to behave consistently with single inserts (where you throw custom exceptions).

- ✅ This is possible:
    
    - Use `RETURNING` (with `ON CONFLICT`) or validation queries (with staging).
        
    - Build a **status report per row** (`success` / `failed` + `reason`).
        
    - If any failures → throw a **custom bulk exception** containing that report.
        

Example structure:

```json
{
  "message": "Bulk insert had failures",
  "statuses": [
    { "id": 1, "status": "success" },
    { "id": 2, "status": "failed", "reason": "foreign key violation" }
  ]
}
```

---

## 4. **Performance Considerations**

- Row-by-row inserts are **very slow** → avoid if you expect large batches.
    
- Best options:
    
    - **Duplicates only:** `ON CONFLICT`
        
    - **Mixed constraints:** Staging + Validation
        
    - **Occasional dirty data:** Bulk insert first, fallback to row-by-row on error
        

---

# ✅ Final Takeaway

- MongoDB → `insertMany({ ordered: false })` handles per-doc errors.
    
- Postgres → no native per-row skipping. You need:
    
    - `ON CONFLICT` for duplicates, or
        
    - **Staging table + validation** for broader error handling, or
        
    - Row-by-row (slow) or app fallback strategy.
        
- To mimic your **single insert exception flow**, collect per-row statuses (success/failure + reason) and throw a **custom bulk exception** after the insert.
    

---

👉 Do you want me to **write a ready-to-use Postgres function (PL/pgSQL)** that does bulk insert into a staging table, inserts valid rows, and returns **two lists** (`inserted_rows`, `failed_rows_with_reason`) so you can throw your custom exception directly?