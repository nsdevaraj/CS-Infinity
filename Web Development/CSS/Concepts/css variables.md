
CSS variables, also known as _custom properties_, are a powerful feature in modern CSS that allow you to define reusable values throughout your stylesheet. They follow the syntax of `--variable-name`, and you can use them with the `var()` function. They are particularly useful for theming, dynamic styling, and maintaining consistency in your design.

### Syntax

#### Defining CSS Variables

CSS variables are defined within a `:root` selector or any other selector. The `:root` pseudo-class is typically used because it targets the highest level of the DOM and allows the variable to be globally accessible.

```css
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --font-size: 16px;
}
```

#### Using CSS Variables

To use a CSS variable, you call it with the `var()` function:

```css
body {
  background-color: var(--primary-color);
  color: var(--secondary-color);
  font-size: var(--font-size);
}
```

### Features and Benefits

1. **Reusability**: Define once, reuse multiple times.
2. **Dynamic Updates**: Easily update styles dynamically using JavaScript.
3. **Scoping**: You can define variables within specific selectors for contextual overrides.
4. **Fallback Values**: Provide fallback values in case a variable is not defined.

```css
p {
  color: var(--text-color, black); /* Defaults to black if --text-color is not defined */
}
```

### JavaScript Integration

CSS variables can be accessed and manipulated using JavaScript:

```javascript
// Accessing a variable's value
const root = document.documentElement;
const primaryColor = getComputedStyle(root).getPropertyValue('--primary-color');

// Updating a variable
root.style.setProperty('--primary-color', '#e74c3c');
```

### Real-World Example: Theming

CSS variables are excellent for creating themes:

```css
:root {
  --background-color: white;
  --text-color: black;
}

.dark-theme {
  --background-color: black;
  --text-color: white;
}

body {
  background-color: var(--background-color);
  color: var(--text-color);
}
```

Switching between themes dynamically can be as simple as toggling the `.dark-theme` class on a parent element.

### Browser Support

CSS variables are well-supported in modern browsers, including the latest versions of Chrome, Edge, Firefox, and Safari. They are not supported in Internet Explorer.

If you're working on a modern project, CSS variables are a great choice to enhance your styling workflow.

