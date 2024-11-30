

1. **React Components**: Every React component is a JavaScript function that returns markup.

2. **JSX vs. HTML**: React components return JSX (JavaScript XML) instead of HTML. JSX is essentially JavaScript in disguise.

3. **JSX is Optional**: While JSX is commonly used, you can also create user interfaces using `React.createElement`, though this can be cumbersome.

4. **Attribute Naming**: In JSX, HTML attributes are written in camelCase. For example:
   - `class` becomes `className`
   - `for` becomes `htmlFor`

5. **Dynamic Values**: Unlike static HTML, JSX allows the use of dynamic JavaScript values (put by curly braces), enhancing interactivity and responsiveness in user interfaces.


### Using Curly Braces in JSX

1. **Displaying Data**: You can display data (like strings and numbers) in your JSX using curly braces `{}`.

2. **Dynamic Attributes**: Curly braces allow you to make attributes dynamic. You can embed JavaScript expressions directly.

3. **Styling with Objects**: You can apply styles to React elements using a JavaScript object inside curly braces.

### Example

```jsx
import React from 'react';

const MyComponent = () => {
  const name = "Alice";
  const age = 30;
  const style = { color: 'blue', fontSize: '20px' };

  return (
    <div>
      <h1>Hello, {name}!</h1>           {/* Displaying a string */}
      <p>You are {age} years old.</p>    {/* Displaying a number */}
      <p style={style}>Styled Text</p>   {/* Styling with a JavaScript object */}
    </div>
  );
};

export default MyComponent;
```
