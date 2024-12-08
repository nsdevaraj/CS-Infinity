
### **4. Create an Image Gallery**

**Question:**  
Create an image gallery with thumbnails. Clicking on a thumbnail should display the full image.

**Solution:**

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Image Gallery</title>
        <style>
            .gallery img {
                width: 100px;
                cursor: pointer;
            }
            #mainImage {
                display: block;
                width: 100%;
                max-width: 500px;
                margin: 10px auto;
            }
        </style>
    </head>
    <body>
        <img
            id="mainImage"
            src="https://via.placeholder.com/500"
            alt="Main Image"
        />
        <div class="gallery">
            <img
                src="https://via.placeholder.com/100"
                alt="Image 1"
                onclick="changeImage(this.src)"
            />
            <img
                src="https://via.placeholder.com/100/007BFF/FFFFFF"
                alt="Image 2"
                onclick="changeImage(this.src)"
            />
            <img
                src="https://via.placeholder.com/100/FF0000/FFFFFF"
                alt="Image 3"
                onclick="changeImage(this.src)"
            />
        </div>
        <script>
            function changeImage(src) {
                document.getElementById("mainImage").src = src;
            }
        </script>
    </body>
</html>
```

---


