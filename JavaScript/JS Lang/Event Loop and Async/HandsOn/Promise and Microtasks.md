

```js
console.log("Start");

Promise.resolve().then(() => {
  console.log("Promise1");
});

console.log("Middle");

Promise.resolve().then(() => {
  console.log("Promise2");
});

console.log("End");

/*
Start
Middle
End
Promise1
Promise2
*/
```



```js
console.log("begins");

setTimeout(() => {
  console.log("setTimeout 1");
  Promise.resolve().then(() => {
    console.log("promise 1");
  });
}, 0);

new Promise(function (resolve, reject) {
  console.log("promise 2");
  setTimeout(function () {
    console.log("setTimeout 2");
    resolve("resolve 1");
  }, 0);
}).then((res) => {
  console.log("dot then 1");
  setTimeout(() => {
    console.log(res);
  }, 0);
});
/*
begins
promise 2
setTimeout 1
promise 1
setTimeout 2
dot then 1
resolve 1
*/
```





```js
console.log(1);

setTimeout(function () {
  console.log(2);
}, 0);

Promise.resolve()
  .then(function () {
    console.log(3);
  })
  .then(function () {
    console.log(4);
  });
  
  /*
  
  Promise enter into micro task first
  
  1
3
4
2
*/
```



