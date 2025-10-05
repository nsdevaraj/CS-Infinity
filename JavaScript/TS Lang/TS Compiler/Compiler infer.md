

```ts
const ary1 = [1, 2, 3, null];

const truth1 = ary1.filter(Boolean);  // const truth1: (number | null)[]
console.log(truth1);

const truth2 = ary1.filter(item => item !== null); // const truth2: number[]
console.log(truth2);
```



Note: works from TS 5.5 version => ary.filter(item => item !== null)


```ts
const ary1 = [1,2,3,null]


const truth1 = ary1.filter(Boolean)
//=> const truth1: (number | null)[] 
// still null, even its filtered

console.log(truth1)


// works from ts 5.5 version
const truth2 = ary1.filter(item => item !== null)
// const truth2: number[]

console.log(truth2)


const ary2 = [1,2,3,null, undefined]

const truth3 = ary2.filter(item => item !== null)
// const truth3: (number | undefined)[]

const truth4 = ary2.filter(item => item !== null && item !== undefined)
// const truth4: number[]

const truth5 = ary2.filter(item => item != null)
// const truth5: number[]

const truth6 = ary2.filter(item => !!item)
// const truth6: (number | null | undefined)[]

const truth7 = ary1.filter(item => item !== null && item !== undefined)
// const truth7: number[]
```



 **TypeScript believes _you_, sometimes too much.**
 
 but gradually it believes it much enough!
 

```ts
const ary1 = [1, 2, 3, null];

const truth1 = ary1.filter(Boolean);  // const truth1: (number | null)[]
console.log(truth1);

const truth2 = ary1.filter(item => item !== null); // const truth2: number[]
console.log(truth2);

const filterNull1 = (ary: (number | null) []) => ary.filter(item => item!==null)


const truth3 = filterNull1(ary1);
// const truth3: number[]


const filterNull2 = (ary: (number | null) []) => ary.filter(item => typeof item !== 'object')

const truth4 = filterNull2(ary1);
// const truth4: number[]


const filterNumbers1 = (ary: (number | null)[]) => 
  ary.filter(item => typeof item === 'number');

const truth5 = filterNumbers1(ary1)
// const truth5: number[]

const filterNumbers2 = (ary: (number | null)[]) : (number | null)[] => 
  ary.filter(item => typeof item === 'number');

// inference overrides developer 
const truth6 = filterNumbers1(ary1)
// const truth5: number[]



```



so ts infering things sometime wider, but no ambiguity


TypeScript assumes you **know what you’re doing** with a named variable — but plays it safe with inline objects.

Zod not only validates your object at runtime, it also gives you **full type safety**, closing the gap between what’s actually in the data and what TypeScript _assumes_.


