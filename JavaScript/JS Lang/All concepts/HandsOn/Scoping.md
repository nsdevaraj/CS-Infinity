
```js
var a = 1;  
function b() {  
   a = 10;  
   return;  
   function a() {}  
}  
b();  
console.log(a);//o:  1
```


```js
function foo(){  
   function bar() {  
     return 3;  
   }  
   return bar();  
   function bar() {  
     return 8;  
   }  
}  
console.log(foo());//o: 8
```


```js


function example () {
  var x = 1
  let y = 2
  const z = 3
  
  // const x = 10
  //: SyntaxError: Identifier 'x' has already been declared
  
  if(true){
    var x = 4
    let y = 5
    
    console.log(x,y,z) //=> 4 5 3
  }
  
  
    console.log(x,y,z) //=> 4 2 3
    
    x = 7
    y = 8
    // z = 9 // TypeError: Assignment to constant variable.
}


example()

```




```js




// both runs on callStack itself, so no difference
for (var i=0;i<3;i++){
    console.log('var', i)
}
for (let i=0;i<3;i++){
    console.log('let',i)
}

// var is func scope, so value increase will reflect and have shadow
for (var i=0;i<3;i++){
    setTimeout(()=>{
        console.log('setVar',i)
    }, 100)
}

// let is block scope, so value don't have shadow
for (let i=0;i<3;i++){
    setTimeout(()=>{
        console.log('setLet',i)
    }, 100)
}

/*
var 0
var 1
var 2
let 0
let 1
let 2
setVar 3
setVar 3
setVar 3
setLet 0
setLet 1
setLet 2
*/


```



```javascript
// Global scope
let globalVar = "I am global";

function checkScope() {
  // Function scope
  let funcVar = "I am in function scope";
  console.log(globalVar);  // Accessible: Output -> I am global
  console.log(funcVar);    // Accessible: Output -> I am in function scope
}
checkScope();
console.log(globalVar);     // Accessible: Output -> I am global
// console.log(funcVar);    // Error: funcVar is not defined
```



```js

var num1 = 20, num2 = 3, name = 'Roadside Coder'

function multiple(){
    // takes from globals
    return num1*num2
}

console.log(multiple()) //=> 60

function getScore(){
    var num1 = 10, num2 = 5

    function add(params) {
        // name takes from global
        // num1 and num2 takes from local
        return `${name} scored ${num1+num2}`
    }
    return add()
}

console.log(getScore())//=> Roadside Coder scored 15


```
