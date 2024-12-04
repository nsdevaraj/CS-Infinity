


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


