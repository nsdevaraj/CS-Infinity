
### **1. Create a Responsive Layout**

**Question:**  
Build a responsive layout with two columns. The first column should take 70% width, and the second column should take 30% width. On screens smaller than 600px, stack them vertically.

**Solution:**

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Responsive Layout</title>
        <style>
            .container {
                display: flex;
            }
            .col-70 {
                flex: 70%;
                background: lightblue;
            }
            .col-30 {
                flex: 30%;
                background: lightgreen;
            }
            @media (max-width: 600px) {
                .container {
                    flex-direction: column;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="col-70">Column 1</div>
            <div class="col-30">Column 2</div>
        </div>
    </body>
</html>
```




Here’s how the code works to meet the requirement:

1. **Responsive Layout Setup**:
    
    - The `display: flex;` property in the `.container` class creates a **flex container**, enabling its child elements to behave as flexible items.
    - Flexbox makes it easy to define proportional widths for the columns.
2. **Column Widths**:
    
    - The `flex: 70%;` in `.col-70` ensures that this column takes **70% of the available width** within the container.
    - Similarly, `flex: 30%;` in `.col-30` ensures that the second column takes **30% of the available width**.
    - Together, these percentages sum up to 100%, ensuring a two-column layout.
3. **Responsiveness for Smaller Screens**:
    
    - The `@media (max-width: 600px)` rule triggers when the screen width is **600px or smaller**.
    - Inside this media query, the `.container` gets `flex-direction: column;`, which changes the flex items from a horizontal row to a **vertical stack**.
4. **Background Colors** (Optional for clarity):
    
    - The `background: lightblue;` and `background: lightgreen;` in the columns visually differentiate them, helping to see the 70%-30% division.

### **How the Layout Meets Requirements**:

- **70%-30% Width Division:** The use of `flex: 70%` and `flex: 30%` proportionally allocates the column widths.
- **Responsive Design:** When the screen size shrinks below 600px, the columns stack vertically, fulfilling the mobile-friendly requirement.
- **Flexibility:** Flexbox ensures that the layout adjusts dynamically to any container size without additional calculations or fixed widths.

