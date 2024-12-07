

```js
const a = function(){  
  console.log(this);
  const b = {  
    func1: function(){  
      console.log(this);  
    }  
  }
  const c = {  
    func2: ()=>{  
      console.log(this);  
    }
  }
  
  b.func1();  
  c.func2();  
}

a();// ouput : window,b,window
```



```js

const b = {  
    name:"Vivek",  
    f: function(){  
      var self = this;  
      console.log(this.name);  
      (function(){  
        console.log(this.name);  
        console.log(self.name);  
      })();  
    }  
  }  
  b.f();  
// oo: vivek, undefined, vivek

```



