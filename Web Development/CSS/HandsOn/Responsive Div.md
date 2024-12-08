

### **2. Create a Responsive Grid Layout**

**Question:** Create a 3-column grid layout that adjusts to a single column on small screens.  
**Answer:**

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
  gap: 10px;
}
.item {
  background: lightcoral;
  padding: 10px;
}
@media (max-width: 600px) {
  .container {
    grid-template-columns: 1fr; /* Single column on small screens */
  }
}
```


```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Responsive Grid Layout</title>
        <style>
            .container {
                display: grid;
                grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
            }
            .item {
                background: #f4f4f4;
            }
            @media (max-width: 600px) {
                .container {
                    grid-template-columns: 1fr; /* Single column on small screens */
                }
            }
        </style>
    </head>
    <body>
        <h1 style="text-align: center; padding: 20px 0">
            Responsive Product Grid
        </h1>
        <div class="container">
            <div class="item">
                <img src="https://via.placeholder.com/150" alt="Product 1" />
                <h3>Product 1</h3>
            </div>
            <div class="item">
                <img src="https://via.placeholder.com/150" alt="Product 2" />
                <h3>Product 2</h3>
            </div>
            <div class="item">
                <img src="https://via.placeholder.com/150" alt="Product 3" />
                <h3>Product 3</h3>
            </div>
            <div class="item">
                <img src="https://via.placeholder.com/150" alt="Product 4" />
                <h3>Product 4</h3>
            </div>
            <div class="item">
                <img src="https://via.placeholder.com/150" alt="Product 5" />
                <h3>Product 5</h3>
            </div>
            <div class="item">
                <img src="https://via.placeholder.com/150" alt="Product 6" />
                <h3>Product 6</h3>
            </div>
        </div>
    </body>
</html>

```