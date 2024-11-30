
- A React component can only return **one parent element**.
- To avoid adding unnecessary DOM elements, use **React Fragments** (`<React.Fragment>` or shorthand `<>...</>`) to group multiple elements together without extra markup.



1. **Single Return**: In JavaScript, functions can only return one value. Similarly, a React component must return one parent element.

2. **Error on Multiple Returns**: If you try to return multiple sibling elements without a parent, you’ll get an error.

3. **Using a Wrapper**: You could wrap elements in a `<div>`, but this adds an unnecessary element to the DOM.

4. **React Fragments**: Instead, you can use a React Fragment to group multiple elements without adding extra nodes to the DOM.

### Example

```jsx
import React from 'react';

const MyComponent = () => {
  return (
    <React.Fragment>
      <h1>Hello, World!</h1>
      <p>This is a paragraph.</p>
    </React.Fragment>
  );
};

// Alternatively, you can use the shorthand syntax:
const MyComponentShorthand = () => {
  return (
    <>
      <h1>Hello, World!</h1>
      <p>This is a paragraph.</p>
    </>
  );
};

export default MyComponent;
```

