




```js


const fun1 = () => {
  setTimeout(function() {
    console.log('1')
  }, 3000);
}

const fun2 = () => {
  setTimeout(function() {
    console.log('2')
  }, 2000);
}

const fun3 = () => {
  setTimeout(function() {
    console.log('3')
  }, 1000);
}


fun1()
fun2()
fun3()

/*
3
2
1
*/
```



make this synchronous:


To run `fun1`, `fun2`, and `fun3` synchronously (ensuring they execute in sequence: `fun1` completes, then `fun2`, and finally `fun3`), you can use various methods in JavaScript. Here are some options:

---

### 1. **Using Promises and `async/await`**

```javascript
const fun1 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('1');
      resolve();
    }, 3000);
  });
};

const fun2 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('2');
      resolve();
    }, 2000);
  });
};

const fun3 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('3');
      resolve();
    }, 1000);
  });
};

const runSynchronously = async () => {
  await fun1();
  await fun2();
  await fun3();
};

runSynchronously();
```

---

### 2. **Using Nested Callbacks**

```javascript
const fun1 = (callback) => {
  setTimeout(function () {
    console.log('1');
    callback();
  }, 3000);
};

const fun2 = (callback) => {
  setTimeout(function () {
    console.log('2');
    callback();
  }, 2000);
};

const fun3 = (callback) => {
  setTimeout(function () {
    console.log('3');
    callback();
  }, 1000);
};

fun1(() => {
  fun2(() => {
    fun3(() => {
      console.log('All done');
    });
  });
});
```

---

### 3. **Using Promise Chaining**

```javascript
const fun1 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('1');
      resolve();
    }, 3000);
  });
};

const fun2 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('2');
      resolve();
    }, 2000);
  });
};

const fun3 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('3');
      resolve();
    }, 1000);
  });
};

fun1()
  .then(() => fun2())
  .then(() => fun3())
  .then(() => console.log('All done'));
```

---

### 4. **Using Generators**

```javascript
function* generator() {
  yield new Promise((resolve) => {
    setTimeout(() => {
      console.log('1');
      resolve();
    }, 3000);
  });

  yield new Promise((resolve) => {
    setTimeout(() => {
      console.log('2');
      resolve();
    }, 2000);
  });

  yield new Promise((resolve) => {
    setTimeout(() => {
      console.log('3');
      resolve();
    }, 1000);
  });
}

const runGenerator = async (gen) => {
  for (let promise of gen()) {
    await promise;
  }
};

runGenerator(generator);
```

---

### 5. **Using a Sequential `setTimeout`**

```javascript
const fun1 = (callback) => {
  setTimeout(function () {
    console.log('1');
    callback();
  }, 3000);
};

const fun2 = (callback) => {
  setTimeout(function () {
    console.log('2');
    callback();
  }, 2000);
};

const fun3 = (callback) => {
  setTimeout(function () {
    console.log('3');
    callback();
  }, 1000);
};

const runSynchronously = () => {
  fun1(() => {
    fun2(() => {
      fun3(() => {
        console.log('All done');
      });
    });
  });
};

runSynchronously();
```

---

### 6. **Using `setTimeout` with Delays Calculated Cumulatively**

```javascript
const fun1 = () => {
  setTimeout(function () {
    console.log('1');
  }, 3000);
};

const fun2 = () => {
  setTimeout(function () {
    console.log('2');
  }, 3000 + 2000);
};

const fun3 = () => {
  setTimeout(function () {
    console.log('3');
  }, 3000 + 2000 + 1000);
};

fun1();
fun2();
fun3();
```

While this works, it is less flexible and not recommended for complex scenarios.

---

Among these, **`async/await`** and **Promise chaining** are the most commonly used approaches for maintaining readability and scalability.



The code you've provided is a **callback hell** example where each function depends on the completion of the previous function. This creates a nested structure that's hard to manage, especially as more asynchronous calls are added. It works, but it’s difficult to maintain and prone to errors.

### Fixing the issue

The issue you're facing isn't so much a functional one (it works fine, it's just nested too deeply), but more about readability and managing asynchronous code. To fix this and make the code more maintainable, we can use **Promises** or **`async/await`** to handle asynchronous code in a cleaner way.

Here’s how you can refactor the code using **Promises** and **`async/await`**.

### 1. **Using Promises:**

We'll wrap each function in a `Promise` to make the asynchronous calls easier to handle in sequence.

```javascript
const fun1 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('1');
      resolve();
    }, 3000);
  });
}

const fun2 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('2');
      resolve();
    }, 2000);
  });
}

const fun3 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('3');
      resolve();
    }, 1000);
  });
}

const runFunc = async () => {
  await fun1();
  await fun2();
  await fun3();
}

runFunc();
```

#### Explanation:

- `fun1`, `fun2`, and `fun3` now return `Promises`. When the asynchronous operation is done (after the `setTimeout`), we call `resolve()`, which signals that the function has completed.
- `runFunc` is marked as `async` so we can use `await` inside it.
- `await` ensures that each function runs in sequence, i.e., `fun1` completes before `fun2` starts, and `fun2` completes before `fun3` starts.

### 2. **Using `async/await` with `Promise.all` (for parallel execution)**

If you want to run these functions **in parallel** (not in sequence), you can do so with `Promise.all`:

```javascript
const fun1 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('1');
      resolve();
    }, 3000);
  });
}

const fun2 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('2');
      resolve();
    }, 2000);
  });
}

const fun3 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('3');
      resolve();
    }, 1000);
  });
}

const runFunc = async () => {
  await Promise.all([fun1(), fun2(), fun3()]);
}

runFunc(); //=> 3,2,1
```

#### Explanation:

- `Promise.all` allows you to execute multiple promises concurrently. All three functions (`fun1`, `fun2`, and `fun3`) will be executed at the same time, and the program will wait for all of them to finish before continuing.

### When to use `async/await` vs. `Promise.all`:

- **Use `async/await`** if you need the functions to run **in sequence** (one after the other).
- **Use `Promise.all`** if you want the functions to run **in parallel** (at the same time), and you only need to wait for all of them to complete.

In your case, it seems like you want to run them in sequence, so the first solution with `async/await` is probably the best.

### Summary:

By wrapping the asynchronous operations in `Promises` and using `async/await`, the code becomes cleaner, more readable, and easier to maintain.


----


### callback helling

```js
const fun1 = (callback) => {
  setTimeout(function() {
    console.log('1')
    callback()
  }, 300);
}

const fun2 = (callback) => {
  setTimeout(function() {
    console.log('2')
    callback()
  }, 200);
}

const fun3 = () => {
  setTimeout(function() {
    console.log('3')
  }, 100);
}



const runFunc = () => {
  fun1(()=> {
    fun2(()=> {
      fun3()
    })
  })
}

runFunc() //=> 1, 2,3 

```


### then chaining

```js



const fun1 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('1')
      resolve()
    }, 300);
  })
}


const fun2 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('2')
      resolve()
    }, 200);
  })
}

const fun3 = () => {
  return new Promise((resolve) => {
    setTimeout(function() {
      console.log('3')
      resolve()
    }, 100);
  })
}

const runFunc = () => {
  fun1()
  .then(()=>fun2())
  .then(()=>fun3())
}

runFunc() //=> 1, 2, 3

```

### promise reduce

```js
const fun1 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('1');
      resolve();
    }, 300);
  });
};

const fun2 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('2');
      resolve();
    }, 200);
  });
};

const fun3 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('3');
      resolve();
    }, 100);
  });
};

const runFunc = () => {
  const functions = [fun1, fun2, fun3];
  functions
    .reduce((prevPromise, currentFunction) => {
      return prevPromise.then(() => currentFunction());
    }, Promise.resolve())
    .then(() => console.log('All done!'));
};

runFunc();
/*
1
2
3
All done!
*/

```

### async await 

```js

const fun1 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('1');
      resolve();
    }, 300);
  });
};

const fun2 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('2');
      resolve();
    }, 200);
  });
};

const fun3 = () => {
  return new Promise((resolve) => {
    setTimeout(function () {
      console.log('3');
      resolve();
    }, 100);
  });
};

const runFunc = async () => {
  await fun1()
  await fun2()
  await fun3()
};

runFunc();
/*
1
2
3
*/

```










