
Scope and Variable ...


|**Aspect**|**Global Scope**|**Local Scope**|
|---|---|---|
|**Definition**|The scope accessible throughout the entire code.|The scope confined to a specific function, block, or context.|
|**Declared Variables**|Variables declared with `var`, `let`, or `const` at the top level.|Variables declared inside a function or block.|
|**Examples**|`javascript<br>var globalVar = "I am global";<br>console.log(globalVar);<br>`|`javascript<br>function example() {<br> let localVar = "I am local";<br> console.log(localVar);<br>}<br>example();<br>console.log(localVar); // Error`|
|**Scope Chain Access**|Accessible from any part of the program.|Accessible only within the function or block it is defined in.|
|**Lifetime**|Exists as long as the script runs.|Exists only while the function or block is running.|
|**Shadowing**|Can be shadowed by local variables if a local variable shares the same name.|Overrides global variables if it shares the same name.|
|**Interaction with `window`**|Global variables (`var`) are attached to the global `window` object in browsers.|Local variables are not attached to `window`.|

---

### Key Points:

1. **Global Scope**: Variables are accessible anywhere in the code after their definition.
2. **Local Scope**: Variables are only accessible within their own function, block, or context.
3. **Shadowing**: A local variable can hide a global variable if they share the same name.
4. `let` and `const` are block-scoped, which means their scope is limited to the nearest enclosing block.




```js

let variable = "I am global"; // Global variable

function shadowingExample() {
  // console.log( variable); // ReferenceError: Cannot access 'variable' before initialization
  let variable;
  console.log(variable); // undefined
  variable = "I am local"; 
  console.log(variable); // "I am local"
}

shadowingExample();
console.log(variable); // "I am global"


```



### **Shadowing 

**Shadowing** occurs when a **local variable** (inside a function or block) has the **same name** as a **global variable**, and within its scope, the local variable takes precedence over the global one.

---

### **Example**

```javascript

let x = 10

function example(){
  let x = 20
  console.log(x) //=> 20
  if(true){
    let x = 30
    console.log(x) //=> 30
  }
  console.log(x) //=> 20
}

example()
console.log(x) //=> 10

```

### **Why it Matters?**

Shadowing prevents accidental usage of a global variable by creating a local context-specific version. However, it can lead to bugs if not used carefully.