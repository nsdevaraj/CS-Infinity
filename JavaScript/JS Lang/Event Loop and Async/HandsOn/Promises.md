



```js


const timer1 = setTimeout(() => {  
   console.log('timer1');  
   const promise1 = Promise.resolve().then(() => {  
     console.log('promise1')  
   })  
}, 0)  
const timer2 = setTimeout(() => {  
   console.log('timer2')  
}, 0)  
console.log('start')
/*  
o:
start  
timer 1  
p1  
t2  
*/

```




```js

const promise1 = Promise.resolve().then(() => {  
   console.log('promise1');
   const timer2 = setTimeout(() => {  
     console.log('timer2')  
   }, 0)  
});
const timer1 = setTimeout(() => {  
   console.log('timer1')  
   const promise2 = Promise.resolve().then(() => {  
     console.log('promise2')  
   })  
}, 0)
console.log('start');  
/*  
o:  
s  
p1  
t1  
p2  
t2  
*/
```




```js


const promise1 = new Promise((resolve, reject) => {  
   const timer1 = setTimeout(() => {  
     resolve('success')  
   }, 1000)  
})  
const promise2 = promise1.then(() => {  })
console.log('promise1', promise1)  
console.log('promise2', promise2)
const timer2 = setTimeout(() => {  
   console.log('promise1', promise1);  
   console.log('promise2', promise2);  
}, 2000)
/*  
promise1 Promise { <pending> }
promise2 Promise { <pending> }
promise1 Promise { 'success' }
promise2 Promise { undefined }
*/

```




```js


const promise1 = new Promise((resolve, reject) => {  
   const timer1 = setTimeout(() => {  
     resolve('success')  
   }, 1000)  
})  
const promise2 = promise1.then(() => {  
  throw new Error('error!!!')  
})

console.log('promise1', promise1)  
console.log('promise2', promise2)
const timer2 = setTimeout(() => {  
   console.log('promise1', promise1);  
   console.log('promise2', promise2);  
}, 2000)

/*  
promise1 Promise { <pending> }
promise2 Promise { <pending> }

/index.js:7
  throw new Error('error!!!')  
        ^

Error: error!!!
    at /index.js:7:9

*/

```






```js

const promise1 = new Promise((resolve, reject) => {  
    const timer1 = setTimeout(() => {  
        resolve('success');  
    }, 1000);  
});  

const promise2 = promise1.then(() => {  
    throw new Error('error!!!');  
});

console.log('Initial states:');  
console.log('promise1', promise1);  // Logs: pending
console.log('promise2', promise2);  // Logs: pending

const timer2 = setTimeout(() => {  
    console.log('After timeout:');  
    console.log('promise1', promise1);  // Logs: resolved with "success"
    console.log('promise2', promise2);  // Logs: rejected with "Error: error!!!"
}, 2000);


/*
Initial states:
promise1 Promise { <pending> }
promise2 Promise { <pending> }

After timeout:
promise1 Promise { 'success' }
promise2 Promise { <rejected> Error: error!!! }

*/



/*
Initial states:
promise1 Promise { <pending> }
promise2 Promise { <pending> }
ERROR!
/tmp/XrNSn3ctgX/main.js:9
    throw new Error('error!!!');  
          ^

Error: error!!!
    at /tmp/XrNSn3ctgX/main.js:9:11

Node.js v18.20.5

=== Code Exited With Errors ===
*/
```



```js

const promise1 = new Promise((resolve, reject) => {  
    const timer1 = setTimeout(() => {  
        resolve('success');  
    }, 1000);  
});  

const promise2 = promise1
    .then(() => {  
        throw new Error('error!!!');  
    })
    .catch((error) => {  
        console.log('Handled error in promise2:', error.message);  
    });  

console.log('Initial states:');  
console.log('promise1', promise1);  // Logs: pending
console.log('promise2', promise2);  // Logs: pending

const timer2 = setTimeout(() => {  
    console.log('After timeout:');  
    console.log('promise1', promise1);  // Logs: resolved with "success"
    console.log('promise2', promise2);  // Logs: resolved to undefined because the catch handled the error
}, 2000);

/*
Initial states:
promise1 Promise { <pending> }
promise2 Promise { <pending> }
Handled error in promise2: error!!!
After timeout:
promise1 Promise { 'success' }
promise2 Promise { undefined }
*/
```



```js
Promise.resolve()
  .then(() => {
    throw new Error("Oops!");
  })
  .catch((error) => {
    console.log("Caught:", error.message);
  })
  .then(() => {
    console.log("Recovered");
  });

/*=>
Caught: Oops!
Recovered
*/
```


```js
Promise.all([
  Promise.resolve(1),
  Promise.resolve(2),
  Promise.resolve(3),
])
  .then((results) => {
    console.log(results);
  })
  .catch((error) => {
    console.log("Caught:", error);
  });

//=> [ 1, 2, 3 ]
```


```js
Promise.all([
  Promise.resolve(1),
  Promise.reject("Error!"),
  Promise.resolve(2),
])
  .then((results) => {
    console.log(results);
  })
  .catch((error) => {
    console.log("Caught:", error);
  });

// => Caught: Error!
```


```js
Promise.race([
  new Promise((resolve) => setTimeout(() => resolve("Fast"), 100)),
  new Promise((resolve) => setTimeout(() => resolve("Slow"), 500)),
]).then((result) => {
  console.log(result);
});

//=> Fast
```



```js
async function fetchData() {
  const data = await Promise.all([
    Promise.resolve(1),
    Promise.resolve(2),
    Promise.resolve(3),
  ]);
  console.log(data);
}

fetchData();

//=> [ 1, 2, 3 ]
```




