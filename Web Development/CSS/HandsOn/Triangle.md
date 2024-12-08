

### **7. CSS Triangle**

**Question:** How do you create a triangle with CSS?  
**Answer:**

```css
.triangle {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 20px solid black;
}
```




Here is the complete HTML code to create a triangle with CSS using the provided styles:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Triangle</title>
    <style>
        .triangle {
            width: 0;
            height: 0;
            border-left: 10px solid transparent;
            border-right: 10px solid transparent;
            border-bottom: 20px solid black;
        }
    </style>
</head>
<body>
    <div class="triangle"></div>
</body>
</html>
```

### Explanation:

1. **CSS Triangle**:
    - `width: 0` and `height: 0` make the element invisible by default.
    - `border-left` and `border-right` are set to `10px solid transparent` to create the left and right borders that are invisible but contribute to the triangle's shape.
    - `border-bottom: 20px solid black` creates the visible part of the triangle, which points downward.

This method uses CSS borders to create a triangle shape, and the transparency of the left and right borders makes the triangular shape point in the desired direction (downward in this case).


The CSS triangle is created using the borders of an element. Here's a crisp explanation:

1. **Invisible Borders**:
    
    - The `border-left` and `border-right` are set to transparent, meaning they take up space but aren't visible.
2. **Visible Border**:
    
    - The `border-bottom` is set to a solid color (e.g., black), which becomes the visible part of the triangle.
3. **No Width and Height**:
    
    - Setting `width: 0` and `height: 0` removes the visible box of the element, leaving only the borders.
4. **Shape Formation**:
    
    - By manipulating the sizes and colors of the borders, the visible `border-bottom` forms the base of the triangle, while the transparent borders create the angled sides.

In essence, the `border` property is used to "simulate" a triangle, with the transparent borders acting as the sides and the colored border forming the point of the triangle.




### square

```css
 width: 0;
height: 0;
/* border-left: 10px solid transparent;
border-right: 10px solid transparent;
border-bottom: 20px solid black; */

border-left: 10px solid black;
border-right: 10px solid black;
border-bottom: 20px solid black;
```


to check {

other shaps in css

}