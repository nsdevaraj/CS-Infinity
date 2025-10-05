

No, **you should not use React Query inside `useEffect`**.  
React Query **_replaces_** your `useEffect + useState + fetch` pattern entirely — it does everything for you.

---

### 🔄 Here's the before & after comparison:

#### ❌ **Old Way (manual state + fetch + effect)**

```tsx
useEffect(() => {
  const loadData = async () => {
    setIsLoading(true);
    const reviews = await fetchReviewData();
    setDataState(reviews);
    setIsLoading(false);
  };

  loadData();
}, []);
```

---

#### ✅ **React Query Way (cleaner and automatic)**

```tsx
import { useQuery } from '@tanstack/react-query';

const customerName = 'kyruus_boston_reach';

const fetchReviewData = async (): Promise<ReviewResponseDto[]> => {
  const baseUrl = import.meta.env.VITE_API_URL; // Vite way
  const res = await fetch(`${baseUrl}/pull-reviews/customer/${customerName}`);
  if (!res.ok) throw new Error('Failed to fetch reviews');
  return res.json();
};

const { data, isLoading, error } = useQuery({
  queryKey: ['reviews', customerName],
  queryFn: fetchReviewData,
});
```

React Query will:

- handle loading
    
- manage error state
    
- refetch if needed
    
- cache results
    
- avoid duplication
    

---

### 💡 Why `useEffect` is not needed

React Query's `useQuery()` **is already a hook** that triggers your fetch when the component mounts.  
So if you write:

```tsx
const { data, isLoading } = useQuery({ queryKey, queryFn });
```

…it already behaves like:

```tsx
useEffect(() => {
  fetchData();
}, []);
```

but better.

---

### ✅ Final Verdict

Don’t mix `useEffect` with React Query.

Instead, **move your `fetchReviewData()` into a queryFn and wrap it with `useQuery()`**.

---
