
### **5. Create a Fixed Navigation Bar**

**Question:**  
Create a fixed navigation bar that stays at the top of the page while scrolling.

**Solution:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fixed Navbar</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
        }
        .content {
            margin-top: 50px;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="navbar">Fixed Navigation Bar</div>
    <div class="content">
        <p>Scroll down to see the navbar stay at the top.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
    </div>
</body>
</html>
```

---
