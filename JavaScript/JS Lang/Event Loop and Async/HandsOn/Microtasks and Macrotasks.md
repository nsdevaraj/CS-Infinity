


```js
console.log("Start");

setTimeout(() => {
  console.log("Timeout");
}, 0);

Promise.resolve().then(() => {
  console.log("Promise");
});

console.log("End");

/*=>
Start
End
Promise
Timeout
*/
```


```js
console.log("Start");

setTimeout(() => {
    console.log("This runs after 2 seconds");
}, 2000);

console.log("End");

/*
Start
End
This runs after 2 seconds
*/

```


---


```js
console.log("Start");

setTimeout(() => console.log("Macro Task"), 0); // Macro task queue
Promise.resolve().then(() => console.log("Micro Task")); // Microtask queue

console.log("End");
```

**Execution Order**:

1. `Start` → **(Call Stack)**
2. `End` → **(Call Stack cleared)**
3. `Micro Task` → **(Micro Task Queue)**
4. `Macro Task` → **(Macro Task Queue)**



```js

console.log('Start'); // Synchronous code

setTimeout(() => {
    console.log('Timeout 1'); // Task (macrotask)
}, 0);

Promise.resolve().then(() => {
    console.log('Promise 1'); // Microtask scheduled
});

setTimeout(() => {
    console.log('Timeout 2'); // Task (macrotask)
}, 0);

Promise.resolve().then(() => {
    console.log('Promise 2'); // Microtask scheduled
});

console.log('End'); // Synchronous code


/*=>
// Synchronous code
Start
End
// Microtask scheduled
Promise 1
Promise 2
// Task (macrotask)
Timeout 1
Timeout 2
*/
```



```js

console.log('Start'); // Synchronous code

setTimeout(() => {
    console.log('Timeout 1'); // Task (macrotask)
}, 10);

Promise.resolve().then(() => {
    console.log('Promise 1'); // Microtask scheduled
});

setTimeout(() => {
    console.log('Timeout 2'); // Task (macrotask)
}, 10);

setTimeout(() => {
    console.log('Timeout 3'); // Task (macrotask)
}, 0);

Promise.resolve().then(() => {
    console.log('Promise 2'); // Microtask scheduled
});

console.log('End'); // Synchronous code


/*=>
// Synchronous code
Start
End
// Microtask scheduled
Promise 1
Promise 2
// Task (macrotask)
Timeout 3
Timeout 1
Timeout 2
*/
```

----

```js
const promise1 = new Promise((resolve, reject) => {  
   console.log(1);  
   resolve('success')  
}); 
promise1.then(() => {  
   console.log(3);  
});  
console.log(4);  

/* =>
// sync code
1
4
// micro task
3 ( resolved )
*/

```


```js
const promise1 = new Promise((resolve, reject) => {  
   console.log(1);  
});
promise1.then(() => {  
   console.log(3);  
});
console.log(4);  

/* => 
// sync code
1
4
// no 3  since not resolved!
*/
```


```js


const promise1 = new Promise((resolve, reject) => {  
   console.log(1)  
   resolve('resolve1')  
})
const promise2 = promise1.then(res => {  
   console.log(res)  
})
const promise3 = promise1.then(res => {  
   console.log(res)  
})
console.log('promise1:', promise1);  
console.log('promise2:', promise2);
console.log('promise3:', promise3);

/*  
// sync code
 1  
"promise1:"  [object Promise] { ... } resolved  
"promise2:"  [object Promise] { ... } pending  
"promise2:"  [object Promise] { ... } pending  
// resolved logs
"resolve1"  
"resolve1"  

*/
```

---

```js

const fn = () => (new Promise((resolve, reject) => {  
   console.log(1)  
   resolve('success')  
}));
fn().then(res => {  
   console.log(res)  
});
console.log(2)  
/*  
o:  
1  
2  
"success"  
*/


```



```js

console.log('start')  
setTimeout(() => {  
   console.log('setTimeout')  
})  
Promise.resolve().then(() => {  
   console.log('resolve')  
})  
console.log('end')
/*  
"start"  
"end"  
"resolve"  
"setTimeout"  
*/

```



```js


const promise = new Promise((resolve, reject) => {  
   console.log(1);  
   setTimeout(() => {  
     console.log("timerStart");  
     resolve("success");  
     console.log("timerEnd");  
   }, 0);  
   console.log(2);  
});  
promise.then((res) => {  
   console.log(res);  
});  
console.log(4)  
/*  
// sync code
1
2
4
// macro task
timerStart
timerEnd
// micro task
success
*/

```



```js

const promise = new Promise((resolve, reject) => {  
    console.log(1);  
    setTimeout(() => {  
        console.log("timerStart");  
        reject("failed"); 
        console.log("timerEnd");  
    }, 0);  
    console.log(2);  
});  

promise
    .then((res) => {  
        console.log(res);  
    })
    .catch((err) => {
        console.log(err);  
    });  

console.log(4);

/*
1
2
4
timerStart
timerEnd
failed
*/

```



```js


const promise = new Promise((resolve, reject) => {  
    console.log(1);  
    setTimeout(() => {  
        
        setTimeout(()=>{
          console.log('inside')
        }, 0)
        resolve('success');
        
        console.log("timerStart");  
        reject("failed"); 
        
        console.log("timerEnd");  
    }, 0);  
    console.log(2);  
});  

promise
    .then((res) => {  
        console.log(res);  
    })
    .catch((err) => {
        console.log(err);  
    });  

console.log(4);

/*
1
2
4
timerStart
timerEnd
success
inside
*/

```



```js
const timer1 = setTimeout(() => {  
   console.log('timer1');
   const timer3 = setTimeout(() => {  
     console.log('timer3')  
   }, 0)
}, 0)
const timer2 = setTimeout(() => {  
   console.log('timer2')  
}, 0)
console.log('start')  
/*  
o:  
"start"  
"timer1"  
"timer2"  
"timer3"  
*/
```




```js
console.log("Start");

setTimeout(() => {
  console.log("Timeout 1");
}, 0);

Promise.resolve()
  .then(() => {
    console.log("Promise 1");
    return Promise.resolve();
  })
  .then(() => {
    console.log("Promise 2");
  });

setTimeout(() => {
  console.log("Timeout 2");
}, 0);

console.log("End");

/*=>
Start
End
Promise 1
Promise 2
Timeout 1
Timeout 2
*/

```



```js
setTimeout(() => console.log("Macrotask 1"), 0);

Promise.resolve()
  .then(() => {
    console.log("Microtask 1");
    return Promise.resolve();
  })
  .then(() => {
    console.log("Microtask 2");
  });

setTimeout(() => console.log("Macrotask 2"), 0);

Promise.resolve()
  .then(() => console.log("Microtask 3"));

console.log("Sync Task");

/*=>
Sync Task
Microtask 1
Microtask 3
Microtask 2
Macrotask 1
Macrotask 2
*/

```





Here are some **hands-on code questions** with their explanations related to **microtasks**, **macrotasks**, and the **event loop** in JavaScript:

---

### 1. **Question: What will be the output of this code?**

```javascript
console.log("Start");

setTimeout(() => console.log("Macrotask 1"), 0);

Promise.resolve().then(() => console.log("Microtask 1"));

setTimeout(() => console.log("Macrotask 2"), 0);

Promise.resolve().then(() => console.log("Microtask 2"));

console.log("End");
```

#### **Answer**:

**Output**:

```
Start
End
Microtask 1
Microtask 2
Macrotask 1
Macrotask 2
```

- **Explanation**:
    - **Synchronous code** runs first (`Start`, `End`).
    - **Microtasks** (`Promise` callbacks) run next, before any **macrotasks**.
    - **Macrotasks** (`setTimeout`) are executed after microtasks.

---

### 2. **Question: What will be the output of this code?**

```javascript
console.log("Start");

setTimeout(() => {
  console.log("Macrotask 1");
  Promise.resolve().then(() => console.log("Microtask 1"));
}, 0);

Promise.resolve().then(() => console.log("Microtask 2"));

console.log("End");
```

#### **Answer**:

**Output**:

```
Start
End
Microtask 2
Macrotask 1
Microtask 1
```

- **Explanation**:
    - **Synchronous code** runs first (`Start`, `End`).
    - The first **microtask** (`Promise`) is executed before the **macrotask**.
    - The **macrotask** (`setTimeout`) is executed after the microtasks, and it queues another **microtask** inside it.

---

### 3. **Question: What will be the output of this code?**

```javascript
console.log("Start");

setTimeout(() => {
  console.log("Macrotask 1");
  setTimeout(() => console.log("Macrotask 2"), 0);
}, 0);

Promise.resolve().then(() => console.log("Microtask 1"));

console.log("End");
```

#### **Answer**:

**Output**:

```
Start
End
Microtask 1
Macrotask 1
Macrotask 2
```

- **Explanation**:
    - **Synchronous code** (`Start`, `End`) runs first.
    - The **microtask** runs before the **macrotask**.
    - **Macrotask 1** is executed, and then **Macrotask 2** is queued, which is processed after `Macrotask 1`.

---

### 4. **Question: What will be the output of this code?**

```javascript
console.log("Start");

setTimeout(() => {
  console.log("Macrotask 1");
  Promise.resolve().then(() => console.log("Microtask 1"));
}, 0);

Promise.resolve().then(() => console.log("Microtask 2"))
  .then(() => console.log("Microtask 3"));

console.log("End");
```

#### **Answer**:

**Output**:

```
Start
End
Microtask 2
Microtask 3
Macrotask 1
Microtask 1
```

- **Explanation**:
    - **Synchronous code** (`Start`, `End`) runs first.
    - **Microtasks 2 and 3** are processed before **Macrotask 1**.
    - **Macrotask 1** runs, and then the **microtask 1** inside it is executed last.

---

### 5. **Question: How does the event loop process this code?**

```javascript
setTimeout(() => console.log("Timeout 1"), 0);

setImmediate(() => console.log("Immediate 1"));

Promise.resolve().then(() => console.log("Promise 1"));
```

#### **Answer** (Node.js-specific):

**Output**:

```
Promise 1
Immediate 1
Timeout 1
```

- **Explanation**:
    - **Promises** are **microtasks** and execute first.
    - **setImmediate** is a **macrotask** that runs after **microtasks** in Node.js.
    - **setTimeout** (even with 0 ms delay) is processed after `setImmediate`.

---

### Key Points to Remember:

- **Microtasks** (Promises, `queueMicrotask`, `MutationObserver`) have **higher priority** and execute before **macrotasks** (like `setTimeout`, `setInterval`).
- The **event loop** processes **all microtasks** before moving to the next macrotask.

