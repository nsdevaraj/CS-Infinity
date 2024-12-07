

```js

function parent() {  
   var hoisted = "I'm a variable";  
   function hoisted() {  
     return "I'm a function";  
   }  
   return hoisted();  
}  
console.log(parent());
// o: TypeError: hoisted is not a function

```


```js


function parent() {  
   var hoisted = "I'm a variable";  
    hoisted = () =>  {  
     return "I'm a function";  
   }  
   return hoisted();  
}  
console.log(parent());
// o: I'm a function



```



```js


console.log(foo());  
function foo() {  
   var bar = function() { return 3;  };  
   return bar();  
   var bar = function() {  
     return 8;  
   };  
}  

// o: 3


```


```js

var myVar = 'foo';  
(function()  
  {  
   console.log('Original value was: ' + myVar);  
   var myVar = 'bar';  
   console.log('New value is: ' + myVar);  
})(); 
/*  
o:  
"Original value was: undefined"  
"New value is: bar"  
*/

```




```js
var x = 23;
(function(){  
  var x = 43;  
  (function random(){  
    x++;  
    console.log(x);  
    var x = 21;  
  })();  
})();  
//=> NaN


var x = 23;
(function(){  
  var x = 43;  
  (function random(){  
    x++;  
    console.log(x);  
  })();  
})();  
//=> 44

```



