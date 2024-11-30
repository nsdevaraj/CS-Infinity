
### Event Bubbling and Delegation in JavaScript

**Event Bubbling** and **Event Delegation** are techniques for handling events in the DOM.

#### 1. **Event Bubbling**
Event Bubbling is a concept in JavaScript where an event triggered on a child element propagates (or "bubbles up") through its parent elements in the DOM.

**Example**: Suppose you click on a `<button>` inside a `<div>`. The click event starts on the `<button>` but then bubbles up to its parent `<div>`, and then to the `<body>`, all the way up to the root of the document.

```html
<div id="parent">
  <button id="child">Click Me!</button>
</div>

<script>
  // Attach an event listener to the child element
  document.getElementById('child').addEventListener('click', (event) => {
    alert('Button clicked!');
  });

  // Attach an event listener to the parent element
  document.getElementById('parent').addEventListener('click', (event) => {
    alert('Div clicked!');
  });
</script>
```

In this example:
- Clicking the button will alert both `"Button clicked!"` and `"Div clicked!"` because the event bubbles up from the button to the div.

#### 2. **Event Delegation**
Event Delegation is a technique where you attach a single event listener to a parent element to manage events for all of its children. This is useful for handling events on dynamically added elements or when there are multiple child elements with similar behavior.

**Example**: Using event delegation to handle clicks on multiple buttons within a `<div>`.

```html
<div id="parent">
  <button class="child">Button 1</button>
  <button class="child">Button 2</button>
  <button class="child">Button 3</button>
</div>

<script>
  // Add a single event listener on the parent element
  document.getElementById('parent').addEventListener('click', (event) => {
    // Check if the clicked element has the class 'child'
    if (event.target.classList.contains('child')) {
      alert(event.target.innerText + ' clicked!');
    }
  });
</script>
```

In this example:
- Instead of adding a `click` event listener to each button, we add one listener to the parent `<div>`. When any button is clicked, the event listener on the `<div>` handles it by checking if the `event.target` (clicked element) has the class `"child"` and then performs an action. This reduces code and improves performance when handling multiple elements.

### Key Takeaways
- **Event Bubbling** allows events to propagate up from a child to its parents.
- **Event Delegation** leverages bubbling to attach a single event listener to a parent element, which manages events for all specified child elements.

