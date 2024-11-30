
### **Approach 1: Basic Filtering with `useState`**

```jsx
import React, { useState } from "react";

const SearchFilter = () => {
  const [query, setQuery] = useState("");
  const items = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];

  const filteredItems = items.filter((item) =>
    item.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchFilter;
```

---

### **Approach 2: Optimized with `useMemo`**

```jsx
import React, { useState, useMemo } from "react";

const SearchFilter = () => {
  const [query, setQuery] = useState("");
  const items = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];

  // Memoize filtered items to prevent re-computation
  const filteredItems = useMemo(
    () =>
      items.filter((item) =>
        item.toLowerCase().includes(query.toLowerCase())
      ),
    [query, items]
  );

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchFilter;
```

---

### **Approach 3: Debounced Search with `useEffect`**

```jsx
import React, { useState, useEffect } from "react";

const SearchFilter = () => {
  const [query, setQuery] = useState("");
  const [debouncedQuery, setDebouncedQuery] = useState(query);
  const items = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];

  // Apply debounce to limit updates
  useEffect(() => {
    const handler = setTimeout(() => setDebouncedQuery(query), 300);
    return () => clearTimeout(handler);
  }, [query]);

  const filteredItems = items.filter((item) =>
    item.toLowerCase().includes(debouncedQuery.toLowerCase())
  );

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchFilter;
```

---

### **Approach 4: Search Filter with API Integration**

```jsx
import React, { useState, useEffect } from "react";

const SearchFilter = () => {
  const [query, setQuery] = useState("");
  const [items, setItems] = useState([]);
  const [filteredItems, setFilteredItems] = useState([]);

  // Simulate API call
  useEffect(() => {
    const fetchItems = async () => {
      const response = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];
      setItems(response);
    };
    fetchItems();
  }, []);

  // Filter items when query or items change
  useEffect(() => {
    setFilteredItems(
      items.filter((item) =>
        item.toLowerCase().includes(query.toLowerCase())
      )
    );
  }, [query, items]);

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchFilter;
```

---

### **Approach 5: Controlled Component with Parent State**

```jsx
import React, { useState } from "react";

const SearchBar = ({ query, onQueryChange }) => (
  <input
    type="text"
    value={query}
    onChange={(e) => onQueryChange(e.target.value)}
    placeholder="Search..."
  />
);

const SearchFilter = () => {
  const [query, setQuery] = useState("");
  const items = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];

  const filteredItems = items.filter((item) =>
    item.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div>
      <SearchBar query={query} onQueryChange={setQuery} />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchFilter;
```

---

### **Approach 6: Highlight Matching Text**

```jsx
import React, { useState } from "react";

const SearchFilter = () => {
  const [query, setQuery] = useState("");
  const items = ["Apple", "Banana", "Orange", "Mango", "Pineapple"];

  const filteredItems = items.filter((item) =>
    item.toLowerCase().includes(query.toLowerCase())
  );

  const highlightText = (text) => {
    const parts = text.split(new RegExp(`(${query})`, "gi"));
    return (
      <>
        {parts.map((part, index) =>
          part.toLowerCase() === query.toLowerCase() ? (
            <span key={index} style={{ backgroundColor: "yellow" }}>
              {part}
            </span>
          ) : (
            part
          )
        )}
      </>
    );
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <ul>
        {filteredItems.map((item, index) => (
          <li key={index}>{highlightText(item)}</li>
        ))}
      </ul>
    </div>
  );
};

export default SearchFilter;
```

---
