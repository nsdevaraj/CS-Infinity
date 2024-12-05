

Listen to scroll events:

```javascript
useEffect(() => {
  const handleScroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      loadMoreData();
    }
  };
  window.addEventListener('scroll', handleScroll);
  return () => window.removeEventListener('scroll', handleScroll);
}, []);
```




### **1. Infinite Scrolling in Vanilla JavaScript**

#### **Steps**

1. Use the `IntersectionObserver` API to detect when a target element (e.g., a loader) is visible.
2. Load more data when the observer detects the loader in the viewport.

#### **Code Example**

```html
<div id="data-container"></div>
<div id="loader">Loading...</div>
<script>
  const dataContainer = document.getElementById("data-container");
  const loader = document.getElementById("loader");

  let currentPage = 1;

  // Function to fetch and append data
  const fetchData = () => {
    for (let i = 1; i <= 10; i++) {
      const item = document.createElement("div");
      item.textContent = `Item ${i + (currentPage - 1) * 10}`;
      dataContainer.appendChild(item);
    }
    currentPage++;
  };

  // IntersectionObserver callback
  const handleObserver = (entries) => {
    const target = entries[0];
    if (target.isIntersecting) {
      fetchData();
    }
  };

  const observer = new IntersectionObserver(handleObserver, { root: null, threshold: 1.0 });
  observer.observe(loader);

  // Initial fetch
  fetchData();
</script>
```

---

### **2. Infinite Scrolling in React**

#### **Steps**

1. Track the scroll position using an event listener or `IntersectionObserver`.
2. Update the state with new data when reaching the bottom of the list.

#### **Code Example**

```jsx
import React, { useState, useEffect, useRef } from "react";

const InfiniteScroll = () => {
  const [data, setData] = useState([]);
  const [page, setPage] = useState(1);
  const loaderRef = useRef(null);

  // Fetch data function
  const fetchData = () => {
    const newData = Array.from({ length: 10 }, (_, i) => `Item ${i + (page - 1) * 10}`);
    setData((prev) => [...prev, ...newData]);
  };

  useEffect(() => {
    fetchData();
  }, [page]);

  // IntersectionObserver logic
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          setPage((prevPage) => prevPage + 1);
        }
      },
      { threshold: 1.0 }
    );

    if (loaderRef.current) {
      observer.observe(loaderRef.current);
    }

    return () => {
      if (loaderRef.current) {
        observer.unobserve(loaderRef.current);
      }
    };
  }, []);

  return (
    <div>
      {data.map((item, index) => (
        <div key={index}>{item}</div>
      ))}
      <div ref={loaderRef} style={{ height: "50px", textAlign: "center" }}>
        Loading...
      </div>
    </div>
  );
};

export default InfiniteScroll;
```

---

### **Key Points**

1. **Vanilla JS**:
    
    - Use `IntersectionObserver` to efficiently track element visibility.
    - Avoid unnecessary scroll event listeners.
2. **React**:
    
    - Manage data using `useState` and fetch more items on state update.
    - Use `IntersectionObserver` with `useRef` for React's functional components.
3. Both approaches avoid heavy computations and ensure smooth scrolling.