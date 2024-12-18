

### **1. useFetch: Fetch Data from an API**

```jsx
import { useState, useEffect } from 'react';

/**
 * Custom hook to fetch data from an API.
 * @param {string} url - The API endpoint.
 * @returns {Object} { data, error, loading }
 */
export function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        if (!response.ok) throw new Error('Failed to fetch data');
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, error, loading };
}

// Example usage
function App() {
  const { data, loading, error } = useFetch('https://jsonplaceholder.typicode.com/posts');

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {data.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

---


to check {

https://stackoverflow.com/questions/71134159/fetching-data-from-the-dog-api-using-axios-and-saving-data-into-a-new-array


https://stackoverflow.com/questions/71134159/fetching-data-from-the-dog-api-using-axios-and-saving-data-into-a-new-array

}