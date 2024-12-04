

- Use **props** to pass data between components.
- Define props like custom attributes in the parent component.
- Access props in the child component as properties of the `props` object.
- You can pass various data types (strings, numbers, arrays, objects, functions) as props.



### Passing Data with Props in React

1. **What are Props?**: Props (short for properties) allow you to pass data from one component to another. They act like custom attributes for components.

2. **Creating a Prop**: To pass data, define a prop on the component you want to send data to and assign it a value.

3. **Using Props**: Inside the receiving component, access the props through the component's parameters.

4. **Data Types**: You can pass various data types as props, including strings, numbers, arrays, objects, and even functions.

### Example

#### Parent Component

```jsx
import React from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  const userName = "Alice";
  const userAge = 30;

  return (
    <div>
      <ChildComponent name={userName} age={userAge} />
    </div>
  );
};

export default ParentComponent;
```

#### Child Component

```jsx
import React from 'react';

const ChildComponent = (props) => {
  return (
    <div>
      <h1>Name: {props.name}</h1>   {/* Accessing props */}
      <p>Age: {props.age}</p>
    </div>
  );
};

export default ChildComponent;
```




• prop - parent passing things ( with this help components made reusable ), should not valid to update prop  
• state - current component managing things, valid to update by hook  
  
*any time prop or state change - react rerender  
  
  
*prop - callbackFunc, variables or even child element itself i.e ReactNode  
  \
  


