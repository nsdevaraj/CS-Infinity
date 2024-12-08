

### **5. Create a Circular Image**

**Question:** Create a circular profile image from a square one.  
**Answer:**

```css
.image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  border: 2px solid gray;
}
```



Here’s the HTML code to create a circular profile image using the provided CSS:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Circular Image</title>
    <style>
        .image {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            overflow: hidden;
            border: 2px solid gray;
        }
        .image img {
            width: 100%;
            height: 100%;
            object-fit: cover; /* Ensures the image covers the entire area without distortion */
        }
    </style>
</head>
<body>
    <div class="image">
        <img src="https://via.placeholder.com/150" alt="Profile Image">
    </div>
</body>
</html>
```

### Key Details:

1. **`.image` class**:
    
    - `width` and `height` set to 100px to create a square container.
    - `border-radius: 50%` makes the container circular by rounding the edges.
    - `overflow: hidden` ensures that any part of the image outside the circular container is hidden.
    - `border: 2px solid gray` adds a subtle border around the image.
2. **`img` inside `.image`**:
    
    - The `img` tag is styled to fill the container completely using `width: 100%` and `height: 100%`.
    - `object-fit: cover` ensures that the image maintains its aspect ratio while filling the container, cropping where necessary, without stretching.

This will display a circular profile image from a square image, with the border and proper sizing.

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Circular Image</title>
        <style>
            .image {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                overflow: hidden;
            }
            .image img {
                width: 100%;
                height: 100%;
                object-fit: cover; /* Ensures the image covers the entire area without distortion */
            }
        </style>
    </head>
    <body>
        <div class="image">
            <img src="https://via.placeholder.com/150" alt="Profile Image" />
        </div>
    </body>
</html>

```