


```js

(function (a) {
  return (function () {
    console.log(a); // Undefined because `var a` shadows the outer `a`, but is hoisted uninitialized
    var a = 23;     // Creates a new local variable in the inner scope
  })();
})(45);
// Output: undefined


```


```js

(function (a) {
  return (function () {
    console.log(a); // Logs the outer `a` (45), since no new `a` is declared in the inner scope
    a = 23;         // Updates the outer `a`
  })();
})(45);
// Output: 45

```



---

```js


const ary = [1, 2, 3];

for (var i = 0; i < ary.length; i++) {
    setTimeout(() => console.log(ary[i], i), 100);
}

/*
undefined 3
undefined 3
undefined 3
*/


// Correct behavior with `var` using an IIFE
for (var j = 0; j < ary.length; j++) {
  ((index) => {
    setTimeout(() => console.log(ary[index]), 100);
  })(j); // Pass the current `i` to the IIFE
}
/*
1
2
3
*/



// Correct behavior with `let`
for (let k = 0; k < ary.length; k++) {
  setTimeout(() => console.log(ary[k]), 100);
}
/*
1
2
3
*/



```

- Use `let` for block-scoped variables in loops to avoid the scoping issues of `var`.
- Alternatively, wrap `var` in an Immediately Invoked Function Expression (IIFE) to preserve the current value in each iteration.


---


```js

let hero = {  
  powerLevel: 99,  
  getPower(){  
    return this.powerLevel;  
  }  
}
let getPower = hero.getPower; 
console.log(getPower()); // undefined  

let hero2 = {powerLevel:42};  
console.log(getPower.apply(hero2)); // 42  
console.log(hero.getPower()); //99

```

Here's a crisp explanation of the behavior:

1. **`let getPower = hero.getPower;`**
    
    - This assigns the `getPower` function to a standalone variable.
    - The `this` inside `getPower` now refers to the global object (`window` in browsers, `undefined` in strict mode) rather than `hero`.
    
    ```javascript
    console.log(getPower()); // undefined
    ```
    
2. **Using `.apply(hero2)`**
    
    - `.apply()` explicitly sets the `this` context for the function.
    - `getPower` is executed with `this` bound to `hero2`, so it accesses `hero2.powerLevel`.
    
    ```javascript
    console.log(getPower.apply(hero2)); // 42
    ```
    
3. **Calling `hero.getPower()`**
    
    - Here, `getPower` is called as a method of `hero`.
    - The `this` inside the function refers to `hero`, so it accesses `hero.powerLevel`.
    
    ```javascript
    console.log(hero.getPower()); // 99
    ```
    

---

### Key Takeaways

- When a method is assigned to a variable (`let getPower = hero.getPower`), it loses its original `this` context.
- To set the correct `this`, use `.call`, `.apply`, or `.bind`.
- Methods retain their `this` context only when called directly on their objects (`hero.getPower()`).



---



```js
let x= {}, y = {name:"Ronny"},z = {name:"John"};  
x[y] = {name:"Vivek"};  
x[z] = {name:"Akki"};  
// console.log(x[y]);  
/*  
oo:  
[object Object] {  
  name: "Akki"  
}  
*/

function runFunc(){  
  console.log("1" + 1);//'11'  
  console.log("A" - 1);// NaN  
  console.log(2 + "-2" + "2");// '2-22'  
  console.log("Hello" - "World" + 78); // NaN  
  console.log("Hello"+ "78");// Hello78  
}  
// runFunc();function func1(){  
  setTimeout(()=>{  
    console.log(x);  
    console.log(y);  
  },300);  var x = 2;  
  let y = 12;  
}  
// func1();  
// oo: 2,12(function(){  
  setTimeout(()=> console.log(1),2000);  
  console.log(2);  
  setTimeout(()=> console.log(3),0);  
  console.log(4);  
})();  
// oo: 2,4,3,1
```


---


```js


function greet(greetStart){
  
  let count = 0
  
  return function(name){
    count += 1
    return `${greetStart} ${name} (${count})`
  }
  
}


const morningGreet = greet("Good Morning")
const eveningGreet = greet("Good Evening")

console.log(morningGreet("Alice")) //=> Good Morning Alice (1)
console.log(morningGreet("Bob")) //=> Good Morning Bob (2)

console.log(eveningGreet("Cany")) //=> Good Morning Bob (2)


```





