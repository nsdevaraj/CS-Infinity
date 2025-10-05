

### **1. Mapped Types + Utility Types (e.g., `Partial`, `Pick`, `Omit`, custom)**

**Why it's powerful:**

-   Helps manage **edit vs. create** forms, where fields are optional or restricted.
-   Great for **reusing types** across API layers and UI components.

**Example:**

```ts
type Listing = {
  id: string;
  title: string;
  description: string;
  isPublished: boolean;
};

// For edit form
type EditableListing = Partial<Omit<Listing, 'id'>>;

```

**Catchy KT Title:** _“Shape-shifting Types: Building Dynamic Forms with TypeScript Magic”_

----------

### **2. Generics with Constraints**

**Why it’s useful:**

-   You often write functions/components that work with various types of listings.
-   Ensures **reusability + type safety**.

**Example:**

```ts
function getTitle<T extends { title: string }>(item: T): string {
  return item.title;
}

```

**Catchy KT Title:** _“The Power of Reusable Type-Safe Functions with Generics”_

----------

### **3. `infer` with Conditional Types (Advanced)**

**Why it's mind-blowing:**

-   Enables type **transformation and inference** in deeply nested objects.
-   Can auto-generate things like filter input types from listing types.

**Example:**

```ts
type Listing = { title: string; details: { views: number } };

type Inner<T> = T extends { details: infer D } ? D : never; // { views: number }

```

**Catchy KT Title:** _“Infer the Unseen: TypeScript’s Secret Weapon for Type Wizards”_

----------

### **4. Template Literal Types (for key composition, path building)**

**Why it’s relevant:**

-   Helpful when you have structured fields like `meta.title`, `meta.description`.
-   Use for **dynamic filtering**, **sorting**, or **query key** building.

**Example:**

```ts
type ListingKeys = 'title' | 'description';
type SortKeys = `sort_by_${ListingKeys}`; // 'sort_by_title' | 'sort_by_description'

```

**Catchy KT Title:** _“TypeScript DSL: Writing Business Rules with Template Literal Types”_

----------

### **Recommended for KT (based on impact + ease of demo):**

-   **Beginner/Mid-level team?** → Start with **Mapped Types + Utility Types**
-   **Advanced/Architect team?** → Go for **Conditional + Infer Types**