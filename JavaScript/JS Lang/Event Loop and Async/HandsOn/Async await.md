

```js
async function test() {
  console.log("Start");
  try {
    const result = await Promise.reject("Error!");
    console.log(result);
  } catch (e) {
    console.log("Caught:", e);
  }
  console.log("End");
}

test();

/*=>
Start
Caught: Error!
End
*/
```



```js

async function taskA() {
  console.log("Task A Start");
  await new Promise((resolve) => setTimeout(resolve, 500));
  console.log("Task A End");
}

async function taskB() {
  console.log("Task B Start");
  await taskA();
  console.log("Task B End");
}

async function taskC() {
  console.log("Task C Start");
  taskB(); // Forgot to await!
  console.log("Task C End");
}

taskC();

/*=>
Task C Start
Task B Start
Task A Start
Task C End
Task A End
Task B End
*/

```



```js
async function fetchWithTimeout(id, delay) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id % 2 === 0) resolve(`Data for ID ${id}`);
      else reject(`Error with ID ${id}`);
    }, delay);
  });
}

async function main() {
  try {
    const results = await Promise.all([
      fetchWithTimeout(1, 1000),
      fetchWithTimeout(2, 500),
      fetchWithTimeout(3, 1500),
    ]);
    console.log("All results:", results);
  } catch (error) {
    console.error("Caught error:", error);
  }
}

main();

// => Caught error: Error with ID 1

```

**Promise.all** breaks on the first rejection.



