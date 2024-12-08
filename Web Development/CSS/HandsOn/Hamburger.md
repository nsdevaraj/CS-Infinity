

### **6. Create a Hamburger Menu**

**Question:** Design a hamburger menu using only CSS.  
**Answer:**

```html
<div class="hamburger">
  <span></span>
  <span></span>
  <span></span>
</div>
<style>
.hamburger {
  display: flex;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
}
.hamburger span {
  width: 30px;
  height: 3px;
  background-color: black;
  transition: all 0.3s;
}
</style>
```




Here is the complete HTML code for the hamburger menu you described:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hamburger Menu</title>
    <style>
        .hamburger {
            display: flex;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
        }
        .hamburger span {
            width: 30px;
            height: 3px;
            background-color: black;
            transition: all 0.3s;
        }
        /* Hamburger menu animation (toggle state) */
        .hamburger.active span:nth-child(1) {
            transform: rotate(45deg);
            position: relative;
            top: 6px;
        }
        .hamburger.active span:nth-child(2) {
            opacity: 0;
        }
        .hamburger.active span:nth-child(3) {
            transform: rotate(-45deg);
            position: relative;
            top: -6px;
        }
    </style>
</head>
<body>
    <div class="hamburger" onclick="this.classList.toggle('active')">
        <span></span>
        <span></span>
        <span></span>
    </div>
</body>
</html>
```

### Key Features:

1. **Hamburger Menu Design**:
    
    - The `.hamburger` div contains three `<span>` elements that represent the lines of the hamburger icon.
    - The `flex-direction: column` stacks the spans vertically with a gap of 5px between them.
2. **CSS Styling**:
    
    - Each `<span>` has a width of `30px`, a height of `3px`, and a black background.
    - The `transition: all 0.3s` allows for smooth animations when the hamburger menu is toggled.
3. **Hamburger Menu Toggle Animation**:
    
    - When the `.hamburger` div is clicked, it adds or removes the `active` class.
    - The first span rotates `45deg` and shifts down, creating the upper part of the "X."
    - The second span fades out by setting its `opacity` to 0.
    - The third span rotates `-45deg` and shifts up, forming the bottom part of the "X."
4. **Toggle Interaction**:
    
    - The `onclick="this.classList.toggle('active')"` JavaScript is a simple toggle that adds/removes the `active` class, triggering the animation.

This solution creates a neat and interactive hamburger menu without using JavaScript for complex toggling logic, just relying on CSS for the visual transformation.


{

to fix easier.. 
}