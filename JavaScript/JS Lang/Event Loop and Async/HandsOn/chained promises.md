
```js
Promise.resolve(1)
  .then((res) => {
    console.log(res);
    return 2;
  })
  .then((res) => {
    console.log(res);
    return Promise.resolve(3);
  })
  .then((res) => {
    console.log(res);
  });


/* =>
1
2
3

*/
```



```js
const p1 = new Promise((resolve) => setTimeout(() => resolve("One"), 1000));
const p2 = new Promise((resolve) => setTimeout(() => resolve("Two"), 2000));
const p3 = new Promise((_, reject) => setTimeout(() => reject("Three"), 1500));

Promise.allSettled([p1, p2, p3])
  .then((results) => {
    results.forEach((result, index) => {
      console.log(`Promise ${index + 1}:`, result);
    });
  })
  .catch(() => {
    console.log("This will never run with Promise.allSettled");
  });

/*
Promise 1: { status: 'fulfilled', value: 'One' }
Promise 2: { status: 'fulfilled', value: 'Two' }
Promise 3: { status: 'rejected', reason: 'Three' }
*/
```



**Promise.allSettled**, which resolves regardless of individual promise status.




```js
async function fetchData(id) {
  if (id === 3) throw new Error("Invalid ID!");
  return `Data for ID: ${id}`;
}

async function process() {
  try {
    const results = await Promise.all([
      fetchData(1),
      fetchData(2),
      fetchData(3), // This will throw an error
    ]);
    console.log(results);
  } catch (error) {
    console.error("Error:", error.message);
  } finally {
    console.log("Process completed");
  }
}

process();

/*

Error: Invalid ID!
Process completed
*/
```

**Promise.all** breaks on the first rejection.



```js
Promise.resolve("Start")
  .then((msg) => {
    console.log(msg);
    throw new Error("Something went wrong");
  })
  .then(() => {
    console.log("This will not run");
  })
  .catch((error) => {
    console.error("Caught error:", error.message);
    return "Recovered";
  })
  .then((msg) => {
    console.log("After recovery:", msg);
  })
  .finally(() => {
    console.log("Cleanup actions");
  });

/* => 
Start
Caught error: Something went wrong
After recovery: Recovered
Cleanup actions
*/

```


```js
Promise.race([
  new Promise((resolve) => setTimeout(() => resolve("Fastest"), 500)),
  new Promise((_, reject) => setTimeout(() => reject("Rejected First"), 300)),
  new Promise((resolve) => setTimeout(() => resolve("Slowest"), 1000)),
])
  .then((result) => {
    console.log("Race resolved with:", result);
  })
  .catch((error) => {
    console.error("Race rejected with:", error);
  });

//=> Race rejected with: Rejected First
```



`Promise.race` resolves or rejects based on the first settled promise.



