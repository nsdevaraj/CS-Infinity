

Maintaining **sort** and **filter** state in **URL params** is a great practice for building UX-friendly, shareable, and bookmarkable pages—especially in dashboards, listings, or search pages.

Here’s a crisp breakdown of how to **maintain sort & filter state in URL params**:

---

### ✅ Why Do This?

- Users can **share URLs** with the same filtered/sorted view.
- Browser navigation (back/forward) works predictably.
- State is **preserved on reload**.
- Useful for SEO (for public pages).

---

### 🌐 Example URL Format

```
/products?sort=price_asc&category=electronics&rating=4
```

---

### 🧠 Key Concepts

#### 1. **Reading from URL**

Use query params on page load:

```ts
const params = new URLSearchParams(window.location.search);
const sort = params.get('sort');          // e.g. 'price_asc'
const category = params.get('category');  // e.g. 'electronics'
```

#### 2. **Updating URL without reload**

Use `history.pushState` or framework utilities:

- In **React (Next.js / React-Router)**:
    

```ts
import { useRouter } from 'next/router';
const router = useRouter();

const updateQuery = (key: string, value: string) => {
  const newQuery = { ...router.query, [key]: value };
  router.push({ query: newQuery }, undefined, { shallow: true });
};
```

#### 3. **Maintaining UI State**

When user selects sort/filter:

```ts
updateQuery('sort', 'price_desc');
updateQuery('category', 'books');
```

#### 4. **Listening to URL Changes (Optional)**

For syncing state if URL is changed manually or externally:

```ts
useEffect(() => {
  const sort = router.query.sort;
  const category = router.query.category;
  // update local state if needed
}, [router.query]);
```

---

### 🧹 Tips

- Use consistent naming: `sort=price_asc`, not `order=low_to_high`
- Avoid bloating URL — only include active filters
- Debounce filter updates to avoid excessive routing
- Encode complex filters (e.g. ranges, arrays) if needed:

    ```
    ?category=books&price=100-500&tags=tech,science
    ```


---

### 🔁 Decode & Sync on Load

Always sync UI with query params on first load:

```ts
useEffect(() => {
  const params = new URLSearchParams(window.location.search);
  setSort(params.get('sort') ?? 'relevance');
  setCategory(params.get('category') ?? 'all');
}, []);
```

---


---

Here's a **simple TanStack Router v1** implementation for maintaining filter (`gender`) in the **URL params** for a list view:

---

## 🎯 Goal

Implement a people list filtered by gender:

```
/people?gender=male
```

---

## 🛠️ Setup

### 1. **Define the Route with Search Param**

```tsx
// routes/people.tsx
import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/people')({
  component: PeopleList,
  validateSearch: (search) => ({
    gender: search.gender as 'male' | 'female' | undefined,
  }),
});
```

---

### 2. **Component: PeopleList.tsx**

```tsx
import { useSearch, useNavigate } from '@tanstack/react-router';

const allPeople = [
  { id: 1, name: 'Alice', gender: 'female' },
  { id: 2, name: 'Bob', gender: 'male' },
  { id: 3, name: 'Eve', gender: 'female' },
  { id: 4, name: 'John', gender: 'male' },
];

export default function PeopleList() {
  const search = useSearch({ from: '/people' });
  const navigate = useNavigate({ from: '/people' });

  const handleFilterChange = (gender: 'male' | 'female' | undefined) => {
    navigate({ search: (prev) => ({ ...prev, gender }) });
  };

  const filtered = search.gender
    ? allPeople.filter((p) => p.gender === search.gender)
    : allPeople;

  return (
    <div>
      <h2 className="text-xl font-bold">People List</h2>

      <div className="my-4 space-x-2">
        <button onClick={() => handleFilterChange(undefined)}>All</button>
        <button onClick={() => handleFilterChange('male')}>Male</button>
        <button onClick={() => handleFilterChange('female')}>Female</button>
      </div>

      <ul>
        {filtered.map((person) => (
          <li key={person.id}>{person.name} ({person.gender})</li>
        ))}
      </ul>
    </div>
  );
}
```

---

### ✅ Behavior

- URL updates like: `/people?gender=male`
- State stays in sync on back/forward
- Shareable/bookmarkable filters


---

