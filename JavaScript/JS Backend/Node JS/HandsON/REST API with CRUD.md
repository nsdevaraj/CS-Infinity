

### **Question 7: Implement a Simple REST API with CRUD Operations**

**Problem:**  
Create an Express.js REST API for managing a list of items (e.g., books). Implement the following routes:

1. `GET /items` - Retrieve all items.
2. `POST /items` - Add a new item.
3. `PUT /items/:id` - Update an item by ID.
4. `DELETE /items/:id` - Delete an item by ID.

Use an in-memory data store (array) for simplicity.

**Answer:**

```javascript
const express = require('express');
const app = express();

// Middleware to parse JSON
app.use(express.json());

// In-memory data store
let items = [];
let nextId = 1;

// Routes
// 1. Get all items
app.get('/items', (req, res) => {
  res.json(items);
});

// 2. Add a new item
app.post('/items', (req, res) => {
  const { name, description } = req.body;
  if (!name || !description) {
    return res.status(400).send('Name and description are required.');
  }
  const newItem = { id: nextId++, name, description };
  items.push(newItem);
  res.status(201).json(newItem);
});

// 3. Update an item by ID
app.put('/items/:id', (req, res) => {
  const { id } = req.params;
  const { name, description } = req.body;
  const item = items.find((item) => item.id === parseInt(id));

  if (!item) {
    return res.status(404).send('Item not found.');
  }
  if (name) item.name = name;
  if (description) item.description = description;

  res.json(item);
});

// 4. Delete an item by ID
app.delete('/items/:id', (req, res) => {
  const { id } = req.params;
  const index = items.findIndex((item) => item.id === parseInt(id));

  if (index === -1) {
    return res.status(404).send('Item not found.');
  }

  const deletedItem = items.splice(index, 1);
  res.json(deletedItem[0]);
});

// Start server
const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

**Explanation:**

1. **In-Memory Store:** `items` holds the data, with `id` auto-incremented using `nextId`.
2. **CRUD Operations:**
    - `GET /items`: Returns all items as JSON.
    - `POST /items`: Validates input and adds a new item.
    - `PUT /items/:id`: Finds an item by ID and updates its fields.
    - `DELETE /items/:id`: Removes an item by ID.
3. **Validation:** Ensures required fields (`name` and `description`) are provided for `POST` and handles `404 Not Found` for invalid IDs.

**Testing:**  
Use tools like Postman or `curl` to test each endpoint:

- Add an item:  
    `POST /items` with JSON `{ "name": "Book 1", "description": "Description of Book 1" }`.
    
- Update an item:  
    `PUT /items/1` with JSON `{ "name": "Updated Book 1" }`.
    
- Delete an item:  
    `DELETE /items/1`.


