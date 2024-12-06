
[@setTimeOut, requestAnimationFrame, TaskQueue](https://www.youtube.com/watch?v=cCOL7MC4Pl0)

{

to do: lower content in it
}

 **The Main Thread and the Event Loop:**
    - JavaScript runs in a **single-threaded environment**—no chaotic parallelism editing the DOM.
    - This simplicity avoids race conditions but makes blocking the main thread (like infinite loops) particularly harmful.


```js

docuemnt.body.appendChild(e1)
el.style.display = 'none';

// => seems like display element and then make it none, may be like flash

el.style.display = 'none';
docuemnt.body.appendChild(e1)

// => may be better soln to tackle this race condition.. but really not needed!

```

no race condition - since timing of running code and rendering is all tightly defined and mostly deterministic since Event Loop


Analogy : human is multithreaded, but when sneezing its single threaded like one, not other task done other than sneeze..  likewise we don't make like this in js.. 
all things are done on other threads and once done, come back to main thread...



---

3. **The Browser's Task Queue:**
    - Tasks like `setTimeout`, mouse events, and network callbacks are queued and executed in order.
    - Rendering waits until tasks are complete, meaning visible elements only update after the current task finishes.


event loop => continuous loop, detour (split ) when new callback comes.. 

![[Pasted image 20241202192346.png]]


![[Pasted image 20241202192517.png]]




![[Pasted image 20241202192536.png]]




![[Pasted image 20241202192554.png]]



![[Pasted image 20241202192756.png]]


Render steps => detour => style calc (css apply element) + Layout (render tree with item on page and positioned ) + pixel painting  ( not all 3 everytime, based on update, do certain things.. )

slip => SLP


---

4. **Blocking the Main Thread:**
    - Example: A `while(true)` loop halts everything—rendering, user interactions, animations. ( task took infinite time )
    - Lesson: Avoid sneeze-like coding; don't let your code incapacitate the browser.

![[Pasted image 20241202193212.png]]

this don't flash, since it don't complete all tasks planned before render steps.. Event loop guarantee your task will complete before rendering next steps


rendering happen inbetween tasks.. it do things efficiently, like when no tasks done, no re-render.. if browser tab is not in view i.e not do render steps when user never see , it don't re-render likewise.. like 60times/sec 60Hz sync render that display capable of.. not more render possible then display Hz

---

5. **SetTimeout vs. RequestAnimationFrame:**
    - `setTimeout` is a tool for scheduling tasks but isn't render-friendly. Callbacks can fire too frequently, leading to wasted computation and drift.
    - `requestAnimationFrame` aligns work with screen refresh rates (usually 60Hz), syncing with the browser's rendering pipeline for smooth animations.




```js 
//# infinite loops with task and render cycle.. 

function callBack() {
 moveBoxForwardOnePixel()
 requestAnimationFrame(callBack)
}
callBack()



function callBack() {
 moveBoxForwardOnePixel()
 setTimeOut(callBack, 0)
}
callBack()

// setTimeOut => calls func 3.5 times more than requestAnimationFrame
```


![[Pasted image 20241202193841.png]]

setTime(callback, 0 ) => but browser run with some default delay, when monitored by author, its 4.7ms for each callback time to called .. 



6. **MessageChannel for Microtasks:**
    - An advanced alternative to `setTimeout`. It schedules tasks more precisely but still doesn’t inherently sync with rendering.


![[Pasted image 20241202194424.png]]


---

7. **Optimizing for User Experience:**
    - Use `requestAnimationFrame` for anything involving visual updates to minimize duplicate or wasted effort.
    - Batch work efficiently to ensure smooth interactions.

---

8. **Tasks and Rendering:**  
    Tasks are unpredictable in frame timing, but render steps are carefully synced to the display, maintaining order and efficiency.

---

### Key Takeaway:

JavaScript’s event loop provides a deterministic, reliable framework for executing tasks and handling rendering. Understanding and respecting the nuances—like not overloading the main thread or choosing the right scheduling tools—keeps apps performant and users happy.

---

### **Understanding the Event Loop and Related APIs**

The event loop is at the heart of JavaScript's asynchronous behavior. This comprehensive guide dives into `requestAnimationFrame`, microtasks, and tasks—core concepts for efficient browser rendering and DOM updates.

---

#### **requestAnimationFrame (RAF)**

**Why Use RAF?** `requestAnimationFrame` (RAF) is a browser API tailored for animations. It synchronizes your code execution with the refresh rate of the browser, ensuring smooth animations and avoiding unnecessary computations.

##### **Key Benefits**

- **Batching Work**: RAF helps batch updates, especially useful during animations.
- **Rendering Efficiency**: Executes before CSS calculation and painting, reducing redundant updates.

##### **Gotchas**

1. **Ignoring Intermediate States**:
    
    ```javascript
    element.style.transform = 'translateX(1000px)';
    element.style.transition = 'transform 1s';
    element.style.transform = 'translateX(500px)';
    ```
    
    - Here, the browser only registers the final value (`translateX(500px)`) because it calculates styles after JavaScript execution.
    - Solution: Use **two RAFs** to ensure intermediate states are captured:
        
        ```javascript
        requestAnimationFrame(() => {
            element.style.transform = 'translateX(1000px)';
            requestAnimationFrame(() => {
                element.style.transition = 'transform 1s';
                element.style.transform = 'translateX(500px)';
            });
        });
        ```
        
2. **Forcing Style Calculations**: Using `getComputedStyle` can force earlier style calculations but may negatively impact performance by introducing unnecessary recalculations. Prefer RAF or the Web Animation API when possible.


```js
button.addEventListner('click',()=> {
	box.style.transform = 'translateX(1000px)';
	box.style.transition = 'transform 1s ease-in-out';
	getComputedStyle(box).transform;
	box.style.transform = 'translateX(500px)'
})
```




---

#### **Microtasks and Tasks**

##### **Understanding Microtasks**

Microtasks are lightweight callbacks queued for execution after JavaScript execution completes but before rendering. Common examples:

- **Promises**
- **Mutation Observers**

**Execution Order:** Microtasks are executed until the queue is empty, even if new microtasks are added during execution. This can block rendering if misused.

##### **Tasks**

Tasks are higher-level events, such as user interactions or `setTimeout` callbacks. They are processed one at a time, allowing the browser to manage rendering between tasks.

---

#### **The Event Loop in Action**

1. **RAF's Place in the Event Loop**:
    
    - Most browsers (e.g., Chrome, Firefox) execute RAF before CSS and painting. However, some (e.g., Safari, Edge) may execute it after painting, causing slight delays.
2. **Microtask Behavior**:
    
    - Microtasks execute as soon as the JavaScript stack is empty.
    - When a microtask queues another microtask, it executes immediately after the current one, potentially blocking rendering if abused.

```js

for (let i=0;i < 1000;i++){
	const span = document.createElement('span')
	document.body.appendChild(span);
	span.textContent = 'Hello';
}
```

This cause 2000 events running, which is not preferred.. 


`requestAnimationFrame` (RAF) is a **macrotask** in the event loop.

### Here's when RAF runs in the event loop:

1. **Execution Flow**:
    
    - RAF callbacks are queued in the **macrotask** queue (even though it is related to animation and often seems to behave like microtasks in terms of timing).
    - After the **render phase** (which occurs after the DOM updates), the event loop processes the macrotasks, including `requestAnimationFrame`.
    - RAF runs **before** the next frame is rendered and is executed **right before the browser repaints**.
2. **RAF Timing**:
    
    - RAF callbacks are typically fired just before the next repaint of the browser's rendering engine. This ensures smooth animations by aligning with the display refresh cycle (usually 60Hz, or about every 16.7ms).

### Order in the Event Loop:

- The **macrotasks** (like `setTimeout`, `setInterval`, etc.) are processed first.
- **Microtasks** (like Promises) run immediately after the currently executing script and before the next macrotask, but **RAF callbacks** are treated like macrotasks, so they run after all **microtasks** have completed but before the browser repaints.

### Summary:

RAF is a **macrotask** and runs in the event loop after the **microtasks** and before the next **repaint** of the page.

Promise - its microtask

```js
Promise.resolve().then(()=> console.log('Hey'))
console.log('Yo!')

// => Yo!
// Hey
```

promise callbacks are async (after synchronous code ).. 

```js
function loop(){
	Promise.resolve().then(loop)
}
loop()

// => Infinite loop
```


---


Task Queue - do one by one.. 
Animation Callbacks - complete the current set of items ( not take added items created by exec current items.. )
Microtasks - complete items until it gets empty ( even complete currently adding item by exec current item )


![[Pasted image 20241202201145.png]]


![[Pasted image 20241202201129.png]]




---

#### **Real-World Examples**

1. **Promise and Event Listeners**:
    
    - Adding two listeners to a button:
        
        ```javascript
        button.addEventListener('click', () => {
            Promise.resolve().then(() => console.log('Microtask 1'));
            console.log('Listener 1');
        });
        
        button.addEventListener('click', () => {
            Promise.resolve().then(() => console.log('Microtask 2'));
            console.log('Listener 2');
        });
        ```
        
        **User-initiated click** logs:
        
        ```
        Listener 1
        Microtask 1
        Listener 2
        Microtask 2
        ```
        
        **Programmatic click** via `button.click()`:
        
        ```
        Listener 1
        Listener 2
        Microtask 1
        Microtask 2
        ```
        
        - **Why?** Programmatic clicks don’t empty the JavaScript stack during event dispatch, so microtasks wait.
2. **Preventing Default Behavior with Promises**:
    
    - Using promises to prevent default actions (e.g., hyperlink navigation) works for user clicks but fails for programmatic clicks. This is because microtasks are delayed until the event dispatch completes, missing the prevention phase.


```js

const nextClick = new Promise(resolve => {
	link.addEventListener('click', resolve, {once:true});
})

nextClick.then(event => {
	event.preventDefault()
	// Handle event
})
```

when user clicks the link, prevent default works..



```js

const nextClick = new Promise(resolve => {
	link.addEventListener('click', resolve, {once:true});
})

nextClick.then(event => {
	event.preventDefault()
	// Handle event
})

link.click()

```

js stack never empties, so micro task can't happen, so follow link.. preventDefault not happen now, but do later.. 

![[Pasted image 20241202202408.png]]





---

#### **Tips for Smooth Animations and Efficient Code**

- Use `requestAnimationFrame` for animations to avoid redundant work and jank.
- Avoid overloading the microtask queue with self-referential callbacks.
- For consistent results, remember the subtle differences in event loop behavior between browsers.

---

By understanding these concepts, you can better manage rendering performance, minimize jank, and write robust, predictable JavaScript.

---

**Pro Tip:** The Web Animation API offers a modern, declarative way to handle animations, eliminating many pitfalls. However, its support varies across browsers, so use it judiciously.



----



### Summary : 

### **Mastering JavaScript's Event Loop, requestAnimationFrame, and Microtasks**

The **event loop** is the backbone of JavaScript’s asynchronous behavior. Understanding how tasks, microtasks, and rendering APIs like `requestAnimationFrame` interact can help you write more efficient and smoother code.

---


### **Understanding the Event Loop**

The event loop processes three main queues:

1. **Task Queue**: Handles tasks like `setTimeout`, user events, and network events.
2. **Microtask Queue**: Processes lightweight tasks, e.g., Promise callbacks or Mutation Observers.
3. **Animation Frame Queue**: Processes callbacks queued by `requestAnimationFrame` (RAF), synchronized with browser rendering.

Tasks and microtasks differ:

- **Tasks** run one at a time, interspersed with rendering.
- **Microtasks** run to completion, including newly queued microtasks, before yielding to rendering.

---

### **requestAnimationFrame (RAF)**

`requestAnimationFrame` is optimized for animations. It queues a callback that runs **before rendering**.

#### **Benefits of RAF**

- Ensures smooth animations by syncing with the browser's refresh rate.
- Batches DOM changes efficiently, reducing unnecessary style recalculations.

#### **Code Example: Animation with RAF**

```javascript
function animate(element, start, end) {
    let current = start;
    function step() {
        if (current >= end) return; // Stop condition
        current += 5; // Increment position
        element.style.transform = `translateX(${current}px)`;
        requestAnimationFrame(step); // Schedule next frame
    }
    step();
}

const box = document.querySelector('.box');
animate(box, 0, 500); // Move .box from 0px to 500px
```

---

#### **Common Gotcha: Ignoring Initial States**

The browser batches style updates, so intermediate styles may be ignored:

```javascript
element.style.transform = 'translateX(1000px)';
element.style.transition = 'transform 1s';
element.style.transform = 'translateX(500px)';
```

This code animates from `0px` to `500px` because the browser skips `translateX(1000px)`.

#### **Fix: Use Two RAFs**

```javascript
requestAnimationFrame(() => {
    element.style.transform = 'translateX(1000px)';
    requestAnimationFrame(() => {
        element.style.transition = 'transform 1s';
        element.style.transform = 'translateX(500px)';
    });
});
```

---

### **Microtasks and Their Role**

Microtasks execute after JavaScript execution but before the browser renders. They are often triggered by:

- **Promises**:
    
    ```javascript
    Promise.resolve().then(() => console.log('Microtask'));
    console.log('Synchronous'); // Logs: Synchronous, Microtask
    ```
    
- **Mutation Observers** for DOM changes.

---

#### **Key Behavior: Blocking Rendering**

Microtasks process until the queue is empty, even if new tasks are queued. Misusing this can block rendering:

```javascript
let count = 0;
function blockRendering() {
    Promise.resolve().then(() => {
        console.log(count++);
        blockRendering(); // Recursively queue microtasks
    });
}
blockRendering(); // Freezes the UI
```

---

### **Tasks vs. Microtasks in Event Listeners**

When dealing with event listeners, the execution order of tasks and microtasks matters.

#### **Example: Two Listeners and Microtasks**

```javascript
button.addEventListener('click', () => {
    Promise.resolve().then(() => console.log('Microtask 1'));
    console.log('Listener 1');
});

button.addEventListener('click', () => {
    Promise.resolve().then(() => console.log('Microtask 2'));
    console.log('Listener 2');
});
```

- **User Click** Logs:
    
    ```
    Listener 1
    Microtask 1
    Listener 2
    Microtask 2
    ```


```js
button.addEventListener('click', () => {
    Promise.resolve().then(() => console.log('Microtask 1'));
    console.log('Listener 1');
});

button.addEventListener('click', () => {
    Promise.resolve().then(() => console.log('Microtask 2'));
    console.log('Listener 2');
});

button.click()
```

- **Programmatic Click (`button.click()`)** Logs:
    
    ```
    Listener 1
    Listener 2
    Microtask 1
    Microtask 2
    ```
    

**Why?** Programmatic clicks don’t empty the JavaScript stack during event dispatch, delaying microtask execution.


---

### **Preventing Default Actions with Promises**

Using promises for event handling works with user clicks but fails with programmatic clicks.

#### **Example: `preventDefault` with Promises**

```javascript
link.addEventListener('click', (event) => {
    Promise.resolve().then(() => event.preventDefault());
});
```

- **User Click**: `preventDefault` works.
- **Programmatic Click**: `preventDefault` is too late because the event stack never empties before the link’s default action.

---

### **Key Takeaways**

1. **RAF for Animations**: Schedule animations efficiently and ensure intermediate states are captured with multiple RAF calls.
2. **Microtasks**: Use sparingly; avoid recursive loops that block rendering.
3. **Task vs. Microtask Order**: Be aware of differences between user and programmatic events.
4. **Testing**: Programmatic clicks behave differently; write tests carefully to match real-world behavior.

Mastering the event loop ensures smooth, responsive web applications and prevents subtle bugs. Dive deep into these concepts to optimize your code!


### **Mastering JavaScript's Event Loop, Microtasks, and requestAnimationFrame**

JavaScript's **event loop** powers its asynchronous behavior, handling tasks, microtasks, and rendering. By understanding the interplay of these components, you can create performant and visually smooth web applications.

---

### **The Event Loop: A Quick Overview**

The event loop ensures proper sequencing of tasks in JavaScript. It manages three primary queues:

1. **Task Queue**:
    - Includes `setTimeout`, `setInterval`, and user-initiated events.
    - Executes tasks one at a time.
2. **Microtask Queue**:
    - Contains lightweight tasks like `Promise` callbacks and `MutationObservers`.
    - Executes all microtasks before the browser renders.
3. **Animation Frame Queue**:
    - Handles `requestAnimationFrame` (RAF) callbacks.
    - Runs before the browser's render cycle.

**Key Rule**: Microtasks are processed until the queue is empty before the event loop proceeds to rendering or new tasks.

---

### **Understanding Microtasks**

**Microtasks** provide a way to prioritize lightweight asynchronous operations. Promises are a common source of microtasks.

#### **Execution Order**

```javascript
Promise.resolve().then(() => console.log('Microtask'));
console.log('Synchronous');
```

**Output**:

```
Synchronous
Microtask
```

---

#### **Beware of Blocking Rendering**

Recursive microtasks can block rendering and freeze the UI:

```javascript
function blockRendering() {
    Promise.resolve().then(() => {
        console.log('Still running');
        blockRendering(); // Queues another microtask
    });
}
blockRendering();
```

This keeps the microtask queue full, preventing rendering.

---

### **Tasks vs. Microtasks in Event Listeners**

JavaScript handles event listeners differently depending on whether they are triggered programmatically or by the user.

#### **Example: Listener and Microtasks**

```javascript
button.addEventListener('click', () => {
    Promise.resolve().then(() => console.log('Microtask'));
    console.log('Listener');
});
```

- **User Click**: Microtasks run immediately after listener execution.
- **Programmatic Click (`button.click()`)**: Execution is batched; microtasks process only after all listeners complete.

---

### **requestAnimationFrame: Optimizing Animations**

`requestAnimationFrame` (RAF) schedules a callback before the browser’s next paint. It ensures animations are synchronized with the display's refresh rate, reducing stuttering.

#### **Using RAF**

```javascript
function animate(element, start, end) {
    let current = start;
    function step() {
        if (current >= end) return; // Stop condition
        current += 5; // Increment
        element.style.transform = `translateX(${current}px)`;
        requestAnimationFrame(step); // Schedule next frame
    }
    step();
}
const box = document.querySelector('.box');
animate(box, 0, 500); // Move .box from 0px to 500px
```

---

### **Common Issues with RAF**

#### **Ignored Intermediate States**

Style changes can be skipped by the browser if they happen too quickly:

```javascript
element.style.transform = 'translateX(1000px)';
element.style.transition = 'transform 1s';
element.style.transform = 'translateX(500px)';
```

Here, the browser animates from `0px` to `500px`, ignoring `1000px`.

#### **Fix Using Two RAF Calls**

```javascript
requestAnimationFrame(() => {
    element.style.transform = 'translateX(1000px)';
    requestAnimationFrame(() => {
        element.style.transition = 'transform 1s';
        element.style.transform = 'translateX(500px)';
    });
});
```

This ensures the browser processes intermediate styles correctly.

---

### **Preventing Default Actions with Promises**

Promises may fail to prevent default actions in programmatically triggered events:

```javascript
link.addEventListener('click', (event) => {
    Promise.resolve().then(() => event.preventDefault());
});
```

- **User Click**: `preventDefault` works because the stack empties.
- **Programmatic Click**: The default action happens before the microtask runs.

**Solution**: Use synchronous `preventDefault` for such cases.

---

### **Key Takeaways**

1. **Microtasks**:
    - Run all queued microtasks before rendering.
    - Avoid recursive microtasks to prevent UI blocking.
2. **requestAnimationFrame**:
    - Synchronizes animations with the browser’s refresh rate.
    - Use multiple RAF calls for capturing intermediate states.
3. **Tasks and Microtasks**:
    - Task execution order differs for user vs. programmatic events.
4. **Testing**:
    - Programmatic events may behave differently; test accordingly.

By mastering the nuances of the event loop, microtasks, and `requestAnimationFrame`, you can optimize both performance and user experience in your web applications.


