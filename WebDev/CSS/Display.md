


### 10. **What does the `display` property do in CSS?**
   - **Answer:** The `display` property determines how an element is displayed. Common values:
     - `block`: Element takes up full width.
     - `inline`: Element takes up only as much width as its content.
     - `inline-block`: Behaves like an inline element but allows width and height to be set.
     - `none`: Hides the element.


Here’s a crisp explanation of the **`display`** property in CSS:

---

### 1. **`block`**
   - Elements take up **full width** of their parent container, stacking on top of each other.
   - Always starts on a **new line**.
   - Example: `<div>`, `<p>`, `<h1>`
   ```css
   .element {
       display: block;
   }
   ```

---

### 2. **`inline`**
   - Elements take up only as **much width as their content**.
   - Does **not start on a new line**; they sit alongside other inline elements.
   - Example: `<span>`, `<a>`
   ```css
   .element {
       display: inline;
   }
   ```

---

### 3. **`inline-block`**
   - Behaves like **inline**, but allows you to set **width** and **height**.
   - Elements sit **next to each other**, but can have block-level styling like margins and padding.
   - Example:
   ```css
   .element {
       display: inline-block;
       width: 100px;
       height: 50px;
   }
   ```

---

### 4. **`none`**
   - The element is **completely removed** from the document flow and is **not displayed**.
   - **Does not occupy space**.
   - Example:
   ```css
   .element {
       display: none;
   }
   ```

---

### 5. **`flex`**
   - Enables **flexbox layout**; allows elements to grow and shrink dynamically to fill the available space.
   - Elements are **arranged in a row** or **column** depending on flex-direction.
   - Example:
   ```css
   .container {
       display: flex;
   }
   ```

---

### 6. **`grid`**
   - Enables **grid layout**; elements are arranged into **rows and columns**.
   - You can define both **rows** and **columns** to create complex layouts.
   - Example:
   ```css
   .container {
       display: grid;
   }
   ```

---

### 7. **`table`**
   - Elements behave like **HTML `<table>`** elements.
   - It is typically used for creating table-like structures.
   - Example:
   ```css
   .element {
       display: table;
   }
   ```

---

### 8. **`list-item`**
   - Elements behave like **list items** in an unordered or ordered list (`<ul>`, `<ol>`).
   - Example:
   ```css
   .element {
       display: list-item;
   }
   ```

---

The `display` property is crucial in controlling how elements are laid out on a page. It determines whether an element is rendered as a block, inline, or in other layout models like flexbox or grid.







### 3. **Explain the difference between inline, block, and inline-block elements with examples.**

- **Answer:**
    - **Inline:** Elements like `<span>` do not start on a new line and respect width/height settings.
    - **Block:** Elements like `<div>` start on a new line and occupy full width.
    - **Inline-block:** Mixes characteristics, respecting width/height but not breaking onto a new line.
- **Example:**
    

    
    `<div style="display: inline-block; width: 50px; height: 50px; background: red;"></div>`
    

---


### 21. **What is the difference between `inline` and `block` elements?**
   - **Answer:**
     - **Inline** elements take up only as much width as their content.
     - **Block** elements take up the full width of their container, with a new line before and after.



### 32. **What is the difference between `inline-block` and `block` elements?**
   - **Answer:**
     - **`inline-block`:** Behaves like inline but allows width/height settings.
     - **`block`:** Takes full width and starts on a new line.
- 
