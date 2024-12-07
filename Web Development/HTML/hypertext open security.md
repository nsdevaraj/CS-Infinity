

**How do you create a hyperlink that opens in a new tab?**


    Copy code
    
    `<a href="https://example.com" target="_blank" rel="noopener noreferrer">Example</a>`
    
- **Explanation:** `target="_blank"` opens the link in a new tab, and `rel="noopener noreferrer"` prevents security risks.


When you use the `target="_blank"` attribute in an anchor (`<a>`) tag to open a link in a new tab or window, it introduces certain **security vulnerabilities** that can be exploited by malicious websites. The `rel="noopener noreferrer"` attribute is used to mitigate these risks.

### Security Risks:

1. **Window Object Access (via `window.opener`)**:
    
    - When you open a link with `target="_blank"`, the newly opened page (in the new tab) can access the original page's `window` object via `window.opener`.
    - This means that the page opened in the new tab can modify or interact with the content of the page that opened it. This is a potential **cross-site scripting (XSS)** vulnerability. For example, the opened page could run JavaScript code that manipulates the original page, leading to unauthorized actions like **redirecting the user to a malicious site** or **stealing sensitive information** from the original page.
    
    **Example of the risk:**
    
    ```javascript
    // Code in the newly opened page
    window.opener.location.href = "https://malicious-site.com"; // Redirects the original page
    ```
    
2. **Leakage of Referrer Information (via `referrer` header)**:
    
    - When you open a link in a new tab with `target="_blank"`, the referring page's URL (the page where the user clicked the link) is sent to the newly opened page as part of the `Referer` HTTP header.
    - If the original page contains sensitive or private information in the URL (e.g., a session token in the query string), this information can be exposed to the destination page.
    
    **Example:**
    
    - A URL like `https://example.com/dashboard?session=12345` could expose the session token in the referrer header when opening a link to another website, allowing the new site to capture this information.

### How `rel="noopener noreferrer"` Mitigates These Risks:

- **`rel="noopener"`**: Prevents the new page from accessing the `window.opener` object, which removes the ability of the newly opened page to modify the original page. It ensures that the two pages are **isolated** and can't interfere with each other.
    
- **`rel="noreferrer"`**: Prevents the browser from sending the referring page's URL (the original page's URL) to the newly opened page in the `Referer` header. This helps protect sensitive data that might be included in the URL.
    

### Example of Safe Usage:

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Visit Example</a>
```

- **`target="_blank"`** opens the link in a new tab.
- **`rel="noopener noreferrer"`** mitigates security vulnerabilities by:
    - **`noopener`** preventing the new tab from manipulating the original page.
    - **`noreferrer`** preventing the referrer information from being sent to the destination.

### Conclusion:

Using `rel="noopener noreferrer"` is a **best practice** whenever you use `target="_blank"` to ensure the security and privacy of the user, especially when linking to external websites.

