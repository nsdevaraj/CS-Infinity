

### **1. Center a Div Horizontally and Vertically**

**Question:** How do you center a div both horizontally and vertically within its parent?  
**Answer:**

```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Ensure parent has height */
}
.child {
  width: 100px;
  height: 100px;
  background-color: lightblue;
}
```


```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Image Gallery</title>

        <style>
            .gallery {
                background-color: red;
                width: 100vh;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .focuser {
                background-color: green;
                width: 50vh;
                height: 50vh;
            }
        </style>
    </head>
    <body>
        <div class="gallery">
            <div class="focuser"></div>
        </div>
    </body>
</html>

```



---


**Alternate:** Using `position`:

```css
.parent {
  position: relative;
  height: 100vh;
}
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```


```html

<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Center Div</title>
        <style>
            .parent {
                position: relative;
                height: 100vh;

                background-color: #f4f4f4; /* Optional background for better visualization */
            }
            .child {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);

                background-color: #fff; /* Optional background */
            }
        </style>
    </head>
    <body>
        <div class="parent">
            <div class="child">This div is centered!</div>
        </div>
    </body>
</html>

```


Certainly! Here's a detailed explanation of how the CSS works to center the `.child` div:

---

### 1. **Positioning**:

- **`position: relative` (on `.parent`)**:  
    This sets `.parent` as the **reference point** for any absolutely positioned child elements. Without `position: relative` (or another positioning context like `absolute` or `fixed`), the `.child` element would align itself relative to the nearest ancestor that has positioning set—or the entire viewport if no such ancestor exists.
    
- **`position: absolute` (on `.child`)**:  
    This allows `.child` to be positioned relative to its closest **positioned ancestor** (in this case, `.parent`). It enables the use of `top`, `left`, and other offset properties.
    

---

### 2. **100vh (Viewport Height)**:

- **`height: 100vh` (on `.parent`)**:  
    This makes the `.parent` element's height span **100% of the viewport height**.
    - `1vh` equals 1% of the height of the browser's visible area (viewport).
    - `100vh` ensures that `.parent` always covers the full height of the screen, even if the content inside is smaller.

---

### 3. **50% Offsets**:

- **`top: 50%` and `left: 50%` (on `.child`)**:  
    These place the **top-left corner** of the `.child` element at the center of the `.parent`.
    - `top: 50%`: Moves the `.child` element down to 50% of `.parent`'s height.
    - `left: 50%`: Moves the `.child` element to 50% of `.parent`'s width.

---

### 4. **Transform for Centering**:

- **`transform: translate(-50%, -50%)` (on `.child`)**:  
    By default, `top: 50%` and `left: 50%` place the **top-left corner** of `.child` at the center.  
    To center the entire `.child` element, we use `transform: translate(-50%, -50%)` to adjust its position:
    - `translate(-50%, -50%)` moves the element **50% of its own width to the left** and **50% of its own height upward**.
    - This ensures that the element's center aligns with the center of `.parent`.

---

### Putting It All Together:

1. **`.parent` with `position: relative; height: 100vh;`** ensures that the parent spans the full height of the screen and provides a reference point for positioning `.child`.
2. **`.child` with `position: absolute; top: 50%; left: 50%;`** moves its top-left corner to the center of `.parent`.
3. **`transform: translate(-50%, -50%)`** shifts the element so that its center, not its corner, aligns with the parent’s center.

---

### Visualizing:

Imagine `.child` as a small box inside a large box (`.parent`):

- `top: 50%; left: 50%`: Moves the top-left corner of the small box to the middle of the large box.
- `translate(-50%, -50%)`: Adjusts the small box so that its own center (not the corner) is in the middle.

This combination is a commonly used technique for precise centering of elements in CSS.

