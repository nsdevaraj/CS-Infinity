
Certainly! Here's a list of common **vanilla DOM manipulation** tasks in JavaScript that often come up in coding interviews, along with concise solutions:

---

### **1. Change Text Content of an Element**

**Question:** Change the text content of an HTML element with a specific `id`.  
**Answer:**

```javascript
document.getElementById('myElement').textContent = 'New Text';
```

---

### **2. Change the Style of an Element**

**Question:** Change the background color of an element with a specific `class`.  
**Answer:**

```javascript
document.querySelector('.myClass').style.backgroundColor = 'blue';
```

---

### **3. Add a New HTML Element**

**Question:** Create a new `div` element and append it to the body.  
**Answer:**

```javascript
let newDiv = document.createElement('div');
newDiv.textContent = 'Hello, World!';
document.body.appendChild(newDiv);
```

---

### **4. Remove an Element**

**Question:** Remove an element from the DOM by `id`.  
**Answer:**

```javascript
let element = document.getElementById('myElement');
element.remove();
```

---

### **5. Add a Class to an Element**

**Question:** Add a class `active` to an element with a specific `id`.  
**Answer:**

```javascript
document.getElementById('myElement').classList.add('active');
```

---

### **6. Remove a Class from an Element**

**Question:** Remove a class `active` from an element with a specific `id`.  
**Answer:**

```javascript
document.getElementById('myElement').classList.remove('active');
```

---

### **7. Toggle a Class on an Element**

**Question:** Toggle the class `active` on an element with a specific `id`.  
**Answer:**

```javascript
document.getElementById('myElement').classList.toggle('active');
```

---

### **8. Change the Value of an Input Field**

**Question:** Change the value of an input element with a specific `id`.  
**Answer:**

```javascript
document.getElementById('myInput').value = 'New Value';
```

---

### **9. Add an Event Listener to an Element**

**Question:** Add a `click` event listener to a button with the `id` of `myButton`.  
**Answer:**

```javascript
document.getElementById('myButton').addEventListener('click', function() {
  alert('Button clicked!');
});
```

---

### **10. Get the Value of a Selected Option in a Dropdown**

**Question:** Get the value of the selected option in a `select` element.  
**Answer:**

```javascript
let selectedValue = document.getElementById('mySelect').value;
console.log(selectedValue);
```

---

### **11. Create and Append Multiple Elements**

**Question:** Create several list items (`li`) and append them to a `ul` element.  
**Answer:**

```javascript
let ul = document.getElementById('myList');
for (let i = 0; i < 5; i++) {
  let li = document.createElement('li');
  li.textContent = `Item ${i + 1}`;
  ul.appendChild(li);
}
```

---

### **12. Set an Attribute on an Element**

**Question:** Set the `href` attribute of an anchor tag (`<a>`) to a new URL.  
**Answer:**

```javascript
document.getElementById('myLink').setAttribute('href', 'https://www.example.com');
```

---

### **13. Get the Attribute of an Element**

**Question:** Get the `href` attribute of an anchor tag (`<a>`).  
**Answer:**

```javascript
let linkHref = document.getElementById('myLink').getAttribute('href');
console.log(linkHref);
```

---

### **14. Change the HTML Content of an Element**

**Question:** Change the inner HTML content of an element with a specific `id`.  
**Answer:**

```javascript
document.getElementById('myElement').innerHTML = '<strong>New HTML Content</strong>';
```

---

### **15. Query Elements by Class Name**

**Question:** Select all elements with a specific class name and change their text content.  
**Answer:**

```javascript
let elements = document.getElementsByClassName('myClass');
for (let element of elements) {
  element.textContent = 'New Text for all elements';
}
```

---

### **16. Scroll to an Element**

**Question:** Scroll smoothly to an element with a specific `id`.  
**Answer:**

```javascript
document.getElementById('myElement').scrollIntoView({ behavior: 'smooth' });
```

---

### **17. Animate an Element (Simple)**

**Question:** Change an element's position using `setInterval` to animate it.  
**Answer:**

```javascript
let elem = document.getElementById('myElement');
let position = 0;
let interval = setInterval(() => {
  position += 5;
  elem.style.left = position + 'px';
  if (position > 200) clearInterval(interval); // stop after moving 200px
}, 10);
```

---

### **18. Clone an Element**

**Question:** Clone an element and append the clone to the body.  
**Answer:**

```javascript
let originalElement = document.getElementById('myElement');
let clonedElement = originalElement.cloneNode(true); // true for deep clone
document.body.appendChild(clonedElement);
```

---

### **19. Get All Elements of a Specific Tag Name**

**Question:** Get all elements with a specific tag name (e.g., `div`) and change their background color.  
**Answer:**

```javascript
let divs = document.getElementsByTagName('div');
for (let div of divs) {
  div.style.backgroundColor = 'lightblue';
}
```

---

### **20. Create a Modal Popup**

**Question:** Create a simple modal that appears when a button is clicked and closes when the "Close" button is clicked.  
**Answer:**

```html
<button id="openModal">Open Modal</button>
<div id="modal" style="display:none;">
  <div class="modal-content">
    <span id="closeModal" style="cursor:pointer;">&times;</span>
    <p>This is a modal!</p>
  </div>
</div>

<script>
  document.getElementById('openModal').addEventListener('click', () => {
    document.getElementById('modal').style.display = 'block';
  });

  document.getElementById('closeModal').addEventListener('click', () => {
    document.getElementById('modal').style.display = 'none';
  });
</script>
```

---

### **21. Set and Get CSS Styles**

**Question:** Set the `font-size` of an element and get its current `font-size`.  
**Answer:**

```javascript
document.getElementById('myElement').style.fontSize = '20px';
let fontSize = window.getComputedStyle(document.getElementById('myElement')).fontSize;
console.log(fontSize);
```

---

These are common **vanilla DOM manipulation** tasks you'll often see in coding interviews. They cover basic operations like changing content, modifying styles, adding/removing elements, handling events, and working with attributes. Let me know if you need further explanations or more examples!