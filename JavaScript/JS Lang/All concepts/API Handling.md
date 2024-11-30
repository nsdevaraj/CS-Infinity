

### Fetch:

The `fetch` syntax in JavaScript is used to make HTTP requests. Below is the basic structure of using `fetch` with examples:

### **Basic Syntax**

```javascript
fetch(url, options)
  .then(response => {
    // Handle the response object
  })
  .catch(error => {
    // Handle any errors
  });
```

### **Example: GET Request**

```javascript
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // Parse the JSON from the response
  })
  .then(data => {
    console.log(data); // Process the data
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
```

### **Example: POST Request**

```javascript
fetch('https://api.example.com/data', {
  method: 'POST', // HTTP method
  headers: {
    'Content-Type': 'application/json', // Specify the content type
  },
  body: JSON.stringify({
    key1: 'value1',
    key2: 'value2'
  }) // Convert the payload to JSON
})
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
```

### **Explanation**

1. **`fetch(url, options)`**:
    
    - `url`: The URL to send the request.
    - `options`: An optional object specifying the HTTP method, headers, body, etc.
2. **`response.ok`**:
    
    - A boolean value indicating whether the response status is in the range 200–299.
3. **`response.json()`**:
    
    - Converts the response body to JSON. Similarly, you can use `.text()`, `.blob()`, `.arrayBuffer()`, etc., depending on the response format.
4. **Error Handling**:
    
    - The `.catch()` block handles network errors or exceptions thrown during the fetch process.

Let me know if you need further details!


Here are **varied API request scenarios** written in JavaScript using `async/await`. Each is designed to reflect interview-level understanding and clarity.

---

### **1. Basic GET Request**

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

fetchData();
```

---

### **2. POST Request with JSON Payload**

```javascript
async function postData() {
  try {
    const payload = { key1: 'value1', key2: 'value2' };
    const response = await fetch('https://api.example.com/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    console.log('Data posted successfully:', data);
  } catch (error) {
    console.error('Error posting data:', error);
  }
}

postData();
```

---

### **3. PUT Request to Update Data**

```javascript
async function updateData(id) {
  try {
    const payload = { updatedKey: 'newValue' };
    const response = await fetch(`https://api.example.com/data/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    console.log('Data updated successfully:', data);
  } catch (error) {
    console.error('Error updating data:', error);
  }
}

updateData(123);
```

---

### **4. DELETE Request**

```javascript
async function deleteData(id) {
  try {
    const response = await fetch(`https://api.example.com/data/${id}`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    console.log('Data deleted successfully.');
  } catch (error) {
    console.error('Error deleting data:', error);
  }
}

deleteData(123);
```

---

### **5. Handling Timeouts with AbortController**

```javascript
async function fetchDataWithTimeout() {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 5000); // Timeout after 5 seconds

  try {
    const response = await fetch('https://api.example.com/slow-data', {
      signal: controller.signal,
    });

    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    if (error.name === 'AbortError') {
      console.error('Request timed out.');
    } else {
      console.error('Error fetching data:', error);
    }
  } finally {
    clearTimeout(timeout); // Cleanup timeout
  }
}

fetchDataWithTimeout();
```

---

### **6. Sequential Requests**

```javascript
async function fetchSequential() {
  try {
    const userResponse = await fetch('https://api.example.com/user/1');
    const user = await userResponse.json();

    const postsResponse = await fetch(`https://api.example.com/user/1/posts`);
    const posts = await postsResponse.json();

    console.log('User:', user);
    console.log('Posts:', posts);
  } catch (error) {
    console.error('Error in sequential requests:', error);
  }
}

fetchSequential();
```

---

### **7. Parallel Requests**

```javascript
async function fetchParallel() {
  try {
    const [usersResponse, postsResponse] = await Promise.all([
      fetch('https://api.example.com/users'),
      fetch('https://api.example.com/posts'),
    ]);

    if (!usersResponse.ok || !postsResponse.ok) {
      throw new Error('Error in one of the requests.');
    }

    const [users, posts] = await Promise.all([
      usersResponse.json(),
      postsResponse.json(),
    ]);

    console.log('Users:', users);
    console.log('Posts:', posts);
  } catch (error) {
    console.error('Error in parallel requests:', error);
  }
}

fetchParallel();
```

---

### **8. Retry Logic on Failure**

```javascript
async function fetchDataWithRetry(url, retries = 3) {
  let attempt = 0;
  while (attempt < retries) {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (error) {
      attempt++;
      console.error(`Attempt ${attempt} failed: ${error.message}`);
      if (attempt >= retries) throw new Error('Max retries reached.');
    }
  }
}

(async () => {
  try {
    const data = await fetchDataWithRetry('https://api.example.com/data');
    console.log('Data:', data);
  } catch (error) {
    console.error('Final error:', error);
  }
})();
```

---

These scenarios demonstrate **real-world use cases** that interviewers might expect. Let me know if you want to explore other advanced patterns!

