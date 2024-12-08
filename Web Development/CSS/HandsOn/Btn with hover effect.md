

### **3. Create a CSS Button with Hover Effect**

**Question:** Make a button with a hover effect that changes background color and scales up slightly.  
**Answer:**

```css
.button {
  background-color: royalblue;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: transform 0.2s, background-color 0.2s;
}
.button:hover {
  background-color: deepskyblue;
  transform: scale(1.1);
}
```


```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Button with Hover Effect</title>
        <style>
            .button {
                background-color: royalblue;
                color: white;
                /* padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition:
                    transform 0.2s,
                    background-color 0.2s; */
            }
            .button:hover {
                background-color: deepskyblue;
                transform: scale(1.1);
            }
        </style>
    </head>
    <body>
        <button class="button">Hover Me!</button>
    </body>
</html>

```