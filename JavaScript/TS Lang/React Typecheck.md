


### **20. How do you type-check a React component with TypeScript?**

#### **Answer:**

```typescript
import React from "react";

type Props = {
  name: string;
};

const MyComponent: React.FC<Props> = ({ name }) => <div>Hello, {name}</div>;

export default MyComponent;
```
