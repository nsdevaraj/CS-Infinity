
Web storage provides mechanisms to store data in the browser for client-side applications. It includes **Session Storage**, **Local Storage**, **Cookies**, and **Cache Storage**, among other implementations. Here’s a breakdown:

---

### 1. **Session Storage**

- **Description**: Stores data for the duration of the page session. The data is cleared when the page session ends (e.g., when the browser tab is closed).
- **Use Cases**: Temporary data like form inputs or UI state that needs to persist across page reloads but not across tabs or sessions.
- **API Example**:
    
    ```javascript
    // Set an item
    sessionStorage.setItem('key', 'value');
    
    // Get an item
    const value = sessionStorage.getItem('key');
    
    // Remove an item
    sessionStorage.removeItem('key');
    
    // Clear all
    sessionStorage.clear();
    ```
    

---

### 2. **Local Storage**

- **Description**: Stores data with no expiration time. Data persists even after the browser is closed and reopened.
- **Use Cases**: Persisting user preferences, themes, or data that does not require high security.
- **API Example**:
    
    ```javascript
    // Set an item
    localStorage.setItem('key', 'value');
    
    // Get an item
    const value = localStorage.getItem('key');
    
    // Remove an item
    localStorage.removeItem('key');
    
    // Clear all
    localStorage.clear();
    ```
    

---

### 3. **Cookies**

- **Description**: Small data files stored on the client side, often sent with each HTTP request to the server. They support expiration times and can be scoped to specific domains or paths.
- **Use Cases**: Authentication tokens, session identifiers, tracking user activity.
- **API Example**:
    
    ```javascript
    // Set a cookie
    document.cookie = "key=value; path=/; expires=Fri, 31 Dec 2024 23:59:59 GMT";
    
    // Get cookies
    const cookies = document.cookie; // Returns a string like "key=value; key2=value2"
    
    // Delete a cookie
    document.cookie = "key=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT";
    ```
    

---

### 4. **IndexedDB**

- **Description**: A low-level API for client-side storage of structured data, including large binary files.
- **Use Cases**: Complex applications requiring structured queries or offline-first apps (e.g., Progressive Web Apps).
- **API Example**:
    
    ```javascript
    const request = indexedDB.open("MyDatabase", 1);
    
    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      db.createObjectStore("MyStore", { keyPath: "id" });
    };
    
    request.onsuccess = (event) => {
      const db = event.target.result;
      const transaction = db.transaction("MyStore", "readwrite");
      const store = transaction.objectStore("MyStore");
      store.add({ id: 1, name: "John Doe" });
    };
    ```
    

---

### 5. **Cache Storage (Service Workers)**

- **Description**: API designed for caching network requests and responses for offline access or performance optimization.
- **Use Cases**: Caching assets in Progressive Web Apps (PWAs), enabling offline access to resources.
- **API Example**:
    
    ```javascript
    // Open a cache
    caches.open("my-cache").then((cache) => {
      // Add to cache
      cache.add("/index.html");
    
      // Match cache
      cache.match("/index.html").then((response) => {
        if (response) {
          console.log("Cache hit:", response);
        } else {
          console.log("Cache miss");
        }
      });
    });
    ```
    

---

### 6. **Session Tokens in Memory**

- **Description**: Data stored temporarily in JavaScript variables (not persistent).
- **Use Cases**: Sensitive data like session tokens that should not be stored in persistent storage.
- **Example**:
    
    ```javascript
    const sessionToken = "abc123";
    ```
    

---

### Comparison Table:

|Feature|Session Storage|Local Storage|Cookies|IndexedDB|Cache Storage|
|---|---|---|---|---|---|
|**Lifetime**|Until tab closes|Persistent|Configurable|Persistent|Persistent|
|**Storage Limit**|~5MB|~5MB|~4KB|Varies (~50MB+)|Large (per origin)|
|**Accessible by JS**|Yes|Yes|Yes|Yes|No|
|**Sent with HTTP**|No|No|Yes|No|No|
|**Use Cases**|Temp state|User preferences|Authentication|Complex data storage|Caching assets|

---

### Choosing the Right Storage:

- **Session Storage**: Short-lived, tab-specific data.
- **Local Storage**: Persistent, non-sensitive data.
- **Cookies**: Data shared with the server.
- **IndexedDB**: Large and structured data.
- **Cache Storage**: Offline assets for performance.

Let me know if you'd like detailed implementation examples for any specific storage mechanism!




Session, Cookie, JWT, Token, SSO, and OAuth 2.0 Explained in One Diagram  
  
When you login to a website, your identity needs to be managed. Here is how different solutions work:  
  
- Session - The server stores your identity and gives the browser a session ID cookie. This allows the server to track login state. But cookies don't work well across devices.  
  
- Token - Your identity is encoded into a token sent to the browser. The browser sends this token on future requests for authentication. No server session storage is required. But tokens need encryption/decryption.  
  
- JWT - JSON Web Tokens standardize identity tokens using digital signatures for trust. The signature is contained in the token so no server session is needed.  
  
- SSO - Single Sign On uses a central authentication service. This allows a single login to work across multiple sites.  
  
- OAuth2 - Allows limited access to your data on one site by another site, without giving away passwords.  
  
- QR Code - Encodes a random token into a QR code for mobile login. Scanning the code logs you in without typing a password.  
  
Over to you: QR code logins are gaining popularity. Do you know how it works?


![[Pasted image 20241202064400.png]]


