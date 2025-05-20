
ts-reset : - lib to fix common ts issues

https://www.totaltypescript.com/ts-reset



-  `.json` (in fetch) and `JSON.parse` both return `any`
- 🤦 `.filter(Boolean)` doesn't behave how you expect
- 😡 `array.includes` often breaks on readonly arrays




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
```




ts-reset fix truth1 problem







referred {

https://youtu.be/C_v0fcGEGbA?si=fNnwRcqyXoIguJAh


}


