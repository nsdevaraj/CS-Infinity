
```js
let length, filledArray;

  

length = 3;
filledArray = Array(length).fill(0);
filledArray; // [0, 0, 0]
console.log('filledArray: ', filledArray);

  

length = 3;
filledArray = Array(length).fill({ value: 0 });
filledArray; // [{ value: 0 }, { value: 0 }, { value: 0 }]
console.log('filledArray: ', filledArray);

  

length = 3;
filledArray = Array.from(Array(length), () => {
return { value: 0 };
});

filledArray; // [{ value: 0 }, { value: 0 }, { value: 0 }]
console.log('filledArray: ', filledArray);

  

length = 3;
const sparseArray = Array(length);
sparseArray; // [empty × 3] i.e [undefined, undefined, undefined]
console.log('sparseArray: ', sparseArray);

  

length = 3;
filledArray = Array(length).map(() => { // map skips empty
return { value: 0 };
});
filledArray; // [empty × 3] i.e [undefined, undefined, undefined]
console.log('filledArray: ', filledArray);

  

length = 3;
filledArray = [...Array(length)].map(() => {
return { value: 0 };
});
filledArray; // [{ value: 0 }, { value: 0 }, { value: 0 }]
console.log('filledArray: ', filledArray);

  

//! [...Array(length)] creates an array with items initialized as undefined
```