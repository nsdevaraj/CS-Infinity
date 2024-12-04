
```js
console.log("A");

setTimeout(() => {
  console.log("B");
}, 0);

console.log("C");

setTimeout(() => {
  console.log("D");
}, 0);

console.log("E");

/*=>
A
C
E
B
D

*/
```


```js

function asyncOperation(msg, delay, callback) {
  setTimeout(() => {
    console.log(msg);
    callback();
  }, delay);
}

console.log("Start");

asyncOperation("Step 1", 1000, () => {
  asyncOperation("Step 2", 500, () => {
    asyncOperation("Step 3", 200, () => {
      console.log("Done");
    });
  });
});

console.log("End");


/*
Start
End
Step 1
Step 2
Step 3
Done

*/
```