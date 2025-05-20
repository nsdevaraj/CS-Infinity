
private fields

as const

enums 
inter, return, as const

template literal types


type inference
type narrowing

type predicates


any vs unknown

as



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






```ts
  
const ary = [1,2,3,null]

  

const truth = ary.filter(Boolean)
//=> const truth: (number | null)[] 
// still null, even its filtered

console.log(truth)
```



## ✅ **Why Use `as const`?**

### 1. **Defining Discriminated Unions**

```ts
const statuses = ["loading", "success", "error"] as const;

type Status = typeof statuses[number]; 
// type Status = "loading" | "success" | "error"
```

This is a clean and maintainable way to define union types based on a list of strings.



### 3. **Safe Enums (Enum Alternatives)**

Instead of:

```ts
enum Direction {
  Up = "UP",
  Down = "DOWN"
}
```

Use:

```ts
const Direction = {
  Up: "UP",
  Down: "DOWN"
} as const;

type Direction = typeof Direction[keyof typeof Direction]; 
// "UP" | "DOWN"
```

Benefits:

- Works better with tree-shaking
- Avoids runtime overhead of enums
- More readable and JS-friendly


### 2. **Not for Runtime Logic**

Remember: `as const` is **purely a compile-time construct**. It doesn’t affect JavaScript behavior—it only affects how TypeScript infers types.

