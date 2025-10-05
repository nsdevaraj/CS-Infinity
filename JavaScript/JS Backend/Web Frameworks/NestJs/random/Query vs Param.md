Absolutely! Let's go **in-depth** with a **generic, real-world-style example** for both `@Query()` and `@Param()` in NestJS.

---

## ✅ **Scenario: Building a Product API**

You're developing an e-commerce API with the following use cases:

1. **Get a product by ID**
    
2. **Filter products by category and price**
    
3. **Delete a product by ID**
    
4. **Get paginated product results**
    

We'll break these down using `@Param()` and `@Query()` with code examples and request URLs.

---

## 🛣️ 1. `@Param()` — **Route Parameters**

### 🔹 Use case: Get a product by ID

```ts
@Get('products/:id')
public async getProductById(@Param('id') id: string): Promise<Product> {
  return this.productService.getById(id);
}
```

### 🔸 Request:

```
GET /products/12345
```

### 🔍 Behavior:

- The `id` value `12345` is extracted **from the URL path**.
    
- You use `@Param('id')` to access that value.
    

---

## 🔎 2. `@Query()` — **Query String Parameters**

### 🔹 Use case: Filter products by category and max price

```ts
@Get('products')
public async getFilteredProducts(
  @Query('category') category?: string,
  @Query('maxPrice') maxPrice?: number,
): Promise<Product[]> {
  return this.productService.getFiltered(category, maxPrice);
}
```

### 🔸 Request:

```
GET /products?category=electronics&maxPrice=500
```

### 🔍 Behavior:

- `category` and `maxPrice` are sent in the **query string** (after `?`).
    
- You use `@Query()` to read optional filters from the request.
    

---

## 🗑️ 3. `@Param()` Example for Delete

```ts
@Delete('products/:id')
public async deleteProduct(@Param('id') id: string): Promise<void> {
  await this.productService.delete(id);
}
```

### 🔸 Request:

```
DELETE /products/9876
```

### 🔍 Behavior:

- `9876` is the product ID embedded in the route.
    
- It's used to identify which product to delete.
    

---

## 📄 4. `@Query()` for Pagination

```ts
@Get('products')
public async getPaginatedProducts(
  @Query('page') page: number = 1,
  @Query('limit') limit: number = 10,
): Promise<Product[]> {
  return this.productService.getPaginated(page, limit);
}
```

### 🔸 Request:

```
GET /products?page=2&limit=5
```

### 🔍 Behavior:

- The client asks for **page 2**, with **5 products per page**.
    
- `@Query()` pulls values from the query string.
    

---

## 🧠 Summary Table:

|Annotation|Purpose|Comes From|Example URL|Example Code|
|---|---|---|---|---|
|`@Param()`|Route parameter (usually ID)|URL path segment|`/products/123`|`@Param('id') id: string`|
|`@Query()`|Query string parameter|After `?` in URL|`/products?category=shoes&page=2`|`@Query('category') category: string`|

---

## 🔧 Pro Tip:

- Use **`@Param()`** for **required**, structured data like IDs, slugs, and endpoints.
    
- Use **`@Query()`** for **optional, flexible filtering**, like search terms, pagination, and filters.
    

---

