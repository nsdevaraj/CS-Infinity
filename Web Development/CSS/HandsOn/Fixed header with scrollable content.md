

### **4. Create a Fixed Header with Content Scrollable**

**Question:** Create a fixed header with a scrollable content area.  
**Answer:**

```css
body {
  margin: 0;
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.header {
  background: teal;
  color: white;
  padding: 10px;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1;
}
.content {
  margin-top: 50px; /* Header height */
  overflow-y: auto;
  height: calc(100vh - 50px);
  padding: 20px;
}
```


---

Here’s the complete HTML with the CSS for creating a fixed header and a scrollable content area:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fixed Header with Scrollable Content</title>
    <style>
        body {
            margin: 0;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        .header {
            background: teal;
            color: white;
            padding: 10px;
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1;
            text-align: center;
            font-size: 18px;
        }
        .content {
            margin-top: 50px; /* Header height */
            overflow-y: auto;
            height: calc(100vh - 50px);
            padding: 20px;
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <div class="header">
        Fixed Header
    </div>
    <div class="content">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.</p>
        <p>Maecenas non felis bibendum, ultricies ligula eu, vehicula lacus. Nulla facilisi. Ut luctus nulla ac dolor laoreet, non pellentesque mauris interdum.</p>
        <p>Integer imperdiet interdum eros, a malesuada odio cursus at. Sed nec dui nec arcu consectetur vehicula non a odio. Cras consequat sapien in pharetra venenatis.</p>
        <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum et ligula in nunc bibendum fringilla a eu lectus.</p>
        <p>Mauris ultrices eros in cursus turpis massa tincidunt dui ut ornare lectus. Sed euismod nisi porta lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor id eu.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet est a erat ornare hendrerit. Duis vel nibh at velit scelerisque suscipit.</p>
        <p>Scroll down to see more content...</p>
        <p>Additional content for testing scrolling behavior...</p>
        <p>Another paragraph to fill the space...</p>
        <p>Keep scrolling for more!</p>
    </div>
</body>
</html>
```

### Key Features:

1. **Fixed Header**:
    
    - `.header` is fixed at the top using `position: fixed` and spans the full width of the viewport with `width: 100%`.
    - `z-index: 1` ensures the header stays above the scrollable content.
2. **Scrollable Content**:
    
    - `.content` has `overflow-y: auto`, enabling vertical scrolling if the content exceeds the height of its container.
    - `height: calc(100vh - 50px)` ensures the content area fills the remaining space below the header (`50px` is the height of the header).
3. **Responsive Design**:
    
    - The layout dynamically adapts to the viewport height (`100vh`), making it suitable for both desktop and mobile views.

This layout is commonly used for webpages or apps with a fixed navigation bar or header.



```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Fixed Header with Scrollable Content</title>
        <style>
            body {
                /* to stop double scrolls  */
                margin: 0;
                display: flex;
                flex-direction: column;
                height: 100vh;
            }
            .header {
                background: teal;

                width: 100%;
                height: 30px;
                position: fixed;
                top: 0;
            }
            .content {
                margin-top: 30px;
                overflow-y: auto;
                height: calc(100vh - 30px);
            }
        </style>
    </head>
    <body>
        <div class="header">Fixed Header</div>
        <div class="content">
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus
                lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod
                malesuada.
            </p>
            <p>
                Maecenas non felis bibendum, ultricies ligula eu, vehicula
                lacus. Nulla facilisi. Ut luctus nulla ac dolor laoreet, non
                pellentesque mauris interdum.
            </p>
            <p>
                Integer imperdiet interdum eros, a malesuada odio cursus at. Sed
                nec dui nec arcu consectetur vehicula non a odio. Cras consequat
                sapien in pharetra venenatis.
            </p>
            <p>
                Pellentesque habitant morbi tristique senectus et netus et
                malesuada fames ac turpis egestas. Vestibulum et ligula in nunc
                bibendum fringilla a eu lectus.
            </p>
            <p>
                Mauris ultrices eros in cursus turpis massa tincidunt dui ut
                ornare lectus. Sed euismod nisi porta lorem mollis aliquam ut
                porttitor leo a diam sollicitudin tempor id eu.
            </p>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
                sit amet est a erat ornare hendrerit. Duis vel nibh at velit
                scelerisque suscipit.
            </p>
            <p>Scroll down to see more content...</p>
            <p>Additional content for testing scrolling behavior...</p>
            <p>Another paragraph to fill the space...</p>
            <p>Keep scrolling for more!</p>
        </div>
    </body>
</html>

```