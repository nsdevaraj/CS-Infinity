

Here’s a **detailed yet crisp explanation** of **media queries** in CSS:

### What Are Media Queries?
**Media queries** in CSS allow you to apply different styles to elements based on the **characteristics of the device or viewport** (such as width, height, resolution, etc.). They are a powerful tool for creating **responsive designs** that adjust to different screen sizes and devices.

---

### Basic Syntax

```css
@media (condition) {
  /* CSS rules */
}
```

- **@media:** The keyword used to define a media query.
- **(condition):** The condition that must be met (e.g., screen width).
- **CSS rules:** The styles applied when the condition is true.

---

### Key Media Query Features

1. **Media Type**
   - Specifies the type of media device, like screen, print, or speech.
   - **Common Media Types:**
     - `screen`: For displays (computers, phones, tablets).
     - `print`: For printed documents.
     - `speech`: For screen readers.
   
   **Example:**
   ```css
   @media screen {
     /* Styles for screens */
   }
   ```

2. **Media Features**
   - **Width and Height** (of viewport or device)
     - `width`, `height`: The viewport width or height.
     - `min-width`, `max-width`: Set conditions for the minimum or maximum width.
     - `min-height`, `max-height`: Set conditions for the minimum or maximum height.
   
     **Example:**
     ```css
     @media (min-width: 768px) {
       /* Styles for devices wider than 768px */
     }
     ```

   - **Resolution**
     - `resolution`: Specifies the resolution of the display, useful for devices with high DPI (dots per inch) screens.
     - **Commonly used for retina displays:**
     ```css
     @media (min-resolution: 192dpi) {
       /* Styles for high-resolution screens */
     }
     ```

   - **Orientation**
     - `orientation`: Checks whether the device is in **portrait** or **landscape** mode.
     - **Common Use Case:** Styling layouts differently based on device rotation.
     ```css
     @media (orientation: landscape) {
       /* Styles for landscape orientation */
     }
     ```

   - **Aspect Ratio**
     - `aspect-ratio`: Allows styling based on the ratio between width and height of the viewport.
     ```css
     @media (aspect-ratio: 16/9) {
       /* Styles for devices with 16:9 aspect ratio */
     }
     ```

---

### Common Use Cases

1. **Mobile-First Design (Mobile-First Approach)**
   - Styles are defined for small screens first, and then you use media queries to adjust for larger screens (progressively enhancing the design).
   - **Example:**
   ```css
   /* Base styles for mobile devices */
   .container {
     padding: 10px;
   }

   /* For tablets and larger screens */
   @media (min-width: 768px) {
     .container {
       padding: 20px;
     }
   }
   ```

2. **Tablet and Desktop Layout Adjustments**
   - Use `min-width` to define styles for larger screens.
   - **Example:**
   ```css
   /* Base styles for mobile devices */
   .navbar {
     display: block;
   }

   /* For larger screens (tablets and desktops) */
   @media (min-width: 768px) {
     .navbar {
       display: flex;
     }
   }
   ```

3. **Responsive Typography**
   - Adjust font sizes based on screen width.
   - **Example:**
   ```css
   h1 {
     font-size: 2rem; /* Default for small screens */
   }

   @media (min-width: 768px) {
     h1 {
       font-size: 3rem; /* For larger screens */
     }
   }
   ```

---

### Combining Multiple Conditions

You can combine multiple conditions in a media query using **logical operators**:
- `and`: Combines multiple conditions (all must be true).
- `or` (comma `,`): Either condition can be true.
- `not`: Inverts the condition.

**Examples:**

1. **`and`**
   ```css
   @media (min-width: 768px) and (max-width: 1024px) {
     /* Styles for tablets */
   }
   ```

2. **`or`**
   ```css
   @media (max-width: 768px), (max-height: 600px) {
     /* Styles for smaller screens or shorter heights */
   }
   ```

3. **`not`**
   ```css
   @media not all and (max-width: 768px) {
     /* Styles that apply when the screen is larger than 768px */
   }
   ```

---

### Best Practices

1. **Mobile-First Approach**
   - Start by defining base styles for small screens, then progressively add styles for larger screens using `min-width`.
   
2. **Avoid Overuse**
   - Avoid creating too many media queries for every small change, as it can become complex and harder to maintain.

3. **Use Logical Combinations**
   - Combine multiple conditions (`and`, `or`, `not`) for better control and flexibility.

4. **Use `min-width` for Width Queries**
   - For responsiveness, always use `min-width` to ensure your design works across a range of devices.

---

### Example: Responsive Design

```css
/* Base styles for mobile devices */
.container {
  font-size: 14px;
  padding: 20px;
}

header {
  display: block;
}

footer {
  font-size: 12px;
}

/* Tablet and larger screens (min-width: 768px) */
@media (min-width: 768px) {
  .container {
    font-size: 16px;
    padding: 30px;
  }

  header {
    display: flex;
    justify-content: space-between;
  }

  footer {
    font-size: 14px;
  }
}

/* Desktop and larger screens (min-width: 1024px) */
@media (min-width: 1024px) {
  .container {
    font-size: 18px;
    padding: 40px;
  }

  header {
    display: flex;
    justify-content: space-between;
    padding: 20px;
  }

  footer {
    font-size: 16px;
  }
}
```

---

### Summary
Media queries are essential for **responsive web design**. They allow you to apply specific styles based on conditions like screen width, height, device type, resolution, orientation, and more. The most common approach is mobile-first design, where you start with styles for mobile devices and progressively enhance the design for larger screens. By combining multiple conditions with logical operators, media queries become a powerful tool for creating adaptive and flexible layouts.

