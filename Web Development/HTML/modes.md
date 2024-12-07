
### Modes

In HTML, **Standard Mode** and **Quirks Mode** are two different rendering modes that browsers use to display web pages. These modes are determined based on how a document is structured and the presence (or absence) of certain elements, particularly the **DOCTYPE declaration**. 

### 1. **Standard Mode**

- **Definition**: Standard Mode is the default rendering mode in modern browsers, where the page is rendered according to the current web standards (W3C specifications).
- **DOCTYPE**: A proper **DOCTYPE** declaration (e.g., `<!DOCTYPE html>`) at the beginning of the document triggers Standard Mode.
- **Rendering**: The page is rendered based on modern CSS and JavaScript behavior, and the layout follows the latest web standards.

### 2. **Quirks Mode**

- **Definition**: Quirks Mode is a backward compatibility mode used by browsers to render older web pages that were designed before modern web standards were established.
- **DOCTYPE**: If there is no DOCTYPE declaration or an incorrect one, the browser assumes the page was designed before standards were enforced and switches to Quirks Mode.
- **Rendering**: The page is rendered in a way that mimics older browser behavior, including non-standard interpretations of CSS, box model differences, and other quirks that existed in older browsers.

---

### **Comparison Table: Standard Mode vs. Quirks Mode**

|Feature|**Standard Mode**|**Quirks Mode**|
|---|---|---|
|**DOCTYPE**|Requires a proper DOCTYPE (e.g., `<!DOCTYPE html>`)|No DOCTYPE or an incomplete/incorrect DOCTYPE|
|**CSS Box Model**|Follows modern CSS box model (width includes padding and border)|Uses old box model (width doesn't include padding and border)|
|**Layout Behavior**|Strict adherence to modern web standards (flexbox, grid, etc.)|Older layout practices, inconsistent behavior|
|**JavaScript**|Modern JavaScript behaviors and methods|Older JavaScript methods and quirks (e.g., `alert` sizing)|
|**Rendering Engine**|Modern rendering engine (e.g., Blink, Gecko)|Old rendering engine behavior, mimicking legacy browsers|
|**Compatibility**|Best for modern websites|Used for legacy websites that need backward compatibility|
|**Flexibility**|Fully supports modern features like Flexbox, Grid, etc.|Limited support for modern features (may break layouts)|
|**HTML Interpretation**|Strict HTML5 syntax is followed|Tolerates older or invalid HTML markup (e.g., unclosed tags)|
|**Viewport Handling**|Fully supports responsive design and meta viewport|May not respect responsive design, inconsistent viewport scaling|

---

### How to Avoid Quirks Mode:

- **Always use a proper DOCTYPE** (e.g., `<!DOCTYPE html>`) at the beginning of your HTML document.
- Avoid old-style DOCTYPEs that are associated with legacy browsers (e.g., `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd>`).

### Summary:

- **Standard Mode** is preferred for modern web development and ensures that your website follows current web standards.
- **Quirks Mode** is generally avoided unless you're working with older content or websites that need to be rendered in legacy browser conditions.


### **Examples of Differences in Rendering**

1. **Box Model Calculation**:
   - In **Standards Mode**, padding and border are added to the content width.
   - In **Quirks Mode**, the browser may calculate width differently, including padding and border within the width, similar to the IE5 box model.

2. **CSS Positioning and Floating**:
   - **Standards Mode** handles positioning and floats based on precise CSS standards.
   - **Quirks Mode** may display elements inaccurately, with shifts or gaps.


