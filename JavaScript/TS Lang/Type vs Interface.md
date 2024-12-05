
#### **Answer:**

- **Interface**:
    - Primarily used for defining object shapes.
    - Supports inheritance via `extends`.
- **Type**:
    - More flexible; can define unions, intersections, primitives, etc.
    - Cannot be extended like interfaces.

```typescript
interface User {
  name: string;
}
type Status = 'active' | 'inactive';
```




Both define object shapes. `interface` is extendable, while `type` is more flexible (can include union types).

### **`type` vs `interface` in TypeScript (Crisp Comparison)**

|**Aspect**|**`type`**|**`interface`**|
|---|---|---|
|**Usage**|Can define primitive types, union types, intersections, and object types.|Primarily used to define object shapes and classes.|
|**Declaration Merging**|Cannot merge declarations.|Supports declaration merging (i.e., multiple interfaces with the same name are merged).|
|**Extending**|Can extend other types using intersections (`&`).|Can extend using `extends` keyword.|
|**Flexibility**|More flexible, supports unions, intersections, mapped types, and conditional types.|More rigid, focuses on object shapes and class definitions.|
|**Class Compatibility**|Cannot be used to declare the shape of a class directly.|Can be used to describe a class’s structure and its methods.|
|**Use Case**|Suitable for complex types like unions, intersections, or when flexibility is needed.|Ideal for defining object shapes, and extending objects or classes.|

### **Example Code:**

#### `type`

```typescript
type Shape = {
  width: number;
  height: number;
};

type ColoredShape = Shape & { color: string }; // Intersection
type Circle = Shape | { radius: number }; // Union
```

#### `interface`

```typescript
interface Shape {
  width: number;
  height: number;
}

interface ColoredShape extends Shape {
  color: string;
}
```

### **Conclusion:**

- Use **`type`** when you need flexibility (e.g., unions, intersections, or mapped types).
- Use **`interface`** when you define the structure of objects or classes and want to take advantage of declaration merging.



