


### **26. How can you handle optional chaining in TypeScript?**

#### **Answer:**

```typescript
type User = {
  profile?: {
    address?: {
      city: string;
    };
  };
};

const user: User = {};
const city = user.profile?.address?.city; // undefined
```
