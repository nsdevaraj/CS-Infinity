

# Different Ways to Apply CSS in React Components

Styling React components is a crucial part of building scalable and maintainable apps. React supports multiple approaches for applying CSS — each with trade-offs around scope, performance, maintainability, and developer experience.

This article explores the **prominent CSS strategies** for React with crisp explanations and depth.

---

## 1. **Global CSS / Plain CSS Files**

### What?

- Traditional `.css` files imported globally once (e.g., in `index.js` or `App.js`).
    
- Styles apply globally to matching selectors.
    

### Usage

```js
// index.js
import './styles.css';
```

### Pros

- Simple to set up.
    
- Familiar to all web developers.
    
- Easy to apply resets, typography, utility classes.
    

### Cons

- No style encapsulation → risk of conflicts.
    
- Difficult to maintain in large apps.
    
- No dynamic or scoped styles.
    

### Best for

- Small apps or legacy projects.
    
- Global resets and base styles.
    

---

## 2. **CSS Modules**

### What?

- CSS files with `.module.css` extension.
    
- Classes are locally scoped and hashed automatically by the build tool.
    
- Imported as JS objects.
    

### Usage

```css
/* Button.module.css */
.button {
  background: blue;
  color: white;
}
```

```tsx
import styles from './Button.module.css';

<button className={styles.button}>Click me</button>
```

### Pros

- Scoped styles: no global leakage.
    
- Familiar CSS syntax.
    
- Supported out-of-the-box by tools like Vite, CRA, Next.js.
    
- Easy to maintain per-component styles.
    

### Cons

- Limited dynamic styling (requires conditional className logic).
    
- Still need separate CSS files.
    

### Best for

- Medium to large apps needing scoped CSS without heavy tooling.
    
- Teams familiar with CSS wanting isolation.
    

---

## 3. **CSS-in-JS (Styled Components, Emotion, etc.)**

### What?

- Write CSS inside JavaScript, often as tagged template literals or objects.
    
- Styles scoped automatically to components.
    
- Enables dynamic styling via props and theme access.
    

### Example (styled-components)

```tsx
import styled from 'styled-components';

const Button = styled.button`
  background: ${props => (props.primary ? 'blue' : 'gray')};
  color: white;
  padding: 8px 16px;
`;

<Button primary>Click me</Button>
```

### Pros

- Full dynamic styling with JS logic.
    
- Scoped and encapsulated styles.
    
- Theming support.
    
- Removes the need to switch between CSS and JS files.
    

### Cons

- Adds runtime overhead (styles generated at runtime).
    
- Requires additional dependencies.
    
- Can bloat bundle size if misused.
    

### Best for

- Apps requiring highly dynamic styles.
    
- Teams wanting co-location of styles and logic.
    
- Theming-heavy applications.
    

---

## 4. **Inline Styles**

### What?

- Styles passed directly as a JavaScript object to the `style` prop.
    

### Usage

```tsx
<button style={{ backgroundColor: 'blue', color: 'white' }}>Click</button>
```

### Pros

- Simple for quick one-off styles.
    
- No external CSS or dependencies.
    
- Dynamic and computed styles easy to apply.
    

### Cons

- No support for pseudo-classes (`:hover`) or media queries.
    
- Not reusable or scalable.
    
- Often harder to maintain.
    

### Best for

- Tiny style overrides or quick prototyping.
    
- Dynamic styling that cannot be done in CSS easily.
    

---

## 5. **Sass / SCSS with Modules**

### What?

- Sass is a CSS preprocessor adding variables, nesting, mixins, functions.
    
- Can be combined with CSS Modules (`.module.scss`).
    

### Usage

```scss
// Button.module.scss
$primary-color: blue;

.button {
  background: $primary-color;
  color: white;
}
```

```tsx
import styles from './Button.module.scss';

<button className={styles.button}>Click me</button>
```

### Pros

- Powerful CSS syntax extensions.
    
- Scoped styles with modules.
    
- Well supported in build tools.
    

### Cons

- Requires build tooling.
    
- Larger learning curve.
    

### Best for

- Large projects needing advanced CSS features.
    
- Teams with Sass experience.
    

---

## 6. **Utility-First CSS (Tailwind CSS)**

### What?

- Use pre-defined utility classes directly in JSX.
    
- No writing custom CSS for common styles.
    

### Usage

```tsx
<button className="bg-blue-500 text-white px-4 py-2 rounded">Click me</button>
```

### Pros

- Rapid development with consistent styles.
    
- No CSS files needed.
    
- Highly customizable via config.
    

### Cons

- Verbose class lists in JSX.
    
- Learning curve for utility class names.
    
- Can lead to mixing styles with markup.
    

### Best for

- Teams favoring fast prototyping.
    
- Design systems standardizing on utilities.
    
- Projects with strict design tokens.
    

---

## 7. **CSS Variables with Global / Scoped Styles**

### What?

- Use native CSS variables (`--var-name`) defined globally or per component.
    
- Can combine with any CSS approach.
    

### Usage

```css
:root {
  --primary-color: blue;
}

.button {
  background: var(--primary-color);
  color: white;
}
```

### Pros

- Dynamic theming possible.
    
- Supported natively in browsers.
    
- Works well with CSS Modules or global CSS.
    

### Cons

- Requires CSS knowledge.
    
- Limited by browser support in legacy environments.
    

### Best for

- Theming and design token implementations.
    
- Mixed CSS architectures.
    

---

## Summary Table

|Method|Scoped?|Dynamic Styles|Tooling Needed|Best For|
|---|---|---|---|---|
|Global CSS|No|Limited|No|Small apps, resets|
|CSS Modules|Yes|Moderate|Build tool|Component scoped styles|
|CSS-in-JS|Yes|Full|Yes|Dynamic, theme-heavy apps|
|Inline Styles|No|Full|No|Quick prototyping, overrides|
|Sass/SCSS Modules|Yes|Moderate|Build tool|Large apps with advanced CSS|
|Utility-first (Tailwind)|No|Moderate|Yes|Rapid development, design systems|
|CSS Variables|Scoped if combined|Yes|No|Theming, tokens, hybrid approaches|

---

## Final Tips

- For **enterprise apps**, prefer **CSS Modules**, **CSS-in-JS**, or **Sass Modules** for scalability and maintainability.
    
- Use **utility-first CSS** for rapid prototyping or if your team embraces that style.
    
- Reserve **inline styles** for small dynamic tweaks.
    
- Always organize styles close to components for better modularity.
    
- Leverage theming and design tokens with CSS variables or CSS-in-JS for consistent UI.
    

---
