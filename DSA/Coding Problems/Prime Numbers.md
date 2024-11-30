


Prime number ( a number is prime or not):

 1 - neither prime nor composite, i.e not prime


## Approaches

### Brute force:



```ts
// Time Complexity: O(n)
// Space Complexity: O(1)
const checkPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2; i < n; i++) {
    if (n % i == 0) return false;
  }
  return true;
};
```


### Reducing loops:

```ts
// Space - O(1)
// Time - O(n) - loop will run until val/2 i.e O(n/2)
const checkPrime = (val) => {
  // less than 2 and non 2 even nums
  if (val < 2 || (val !== 2 && val % 2 === 0)) {
    return false;
  }
  // check divisors until half
  for (let i = 2; i <= val / 2; i++) {
    if (val % i === 0) {
      return false;
    }
  }
  return true;
};
```


```ts
// Time - O(sqrt(n)) ->  iterates up to the square root of n in the for loop
// Space - O(1)
function checkPrime(n) {
  if (n <= 1) {
    return false; // 0 and 1 are not prime numbers
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false; // Found a divisor, not prime
    }
  }
  return true; // No divisors found, n is prime
}

```

### Prime number series  

Efficient way : ( when space complexitiy matters & just to find a number is prime or not )



```ts
// Time Complexity: O(sqrt(n)) loop iterates at max of sqrt(n)
// Space Complexity: O(1)
const checkPrime = (n) => {
  if (n <= 1) return false;
  if (n == 2 || n == 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;

  let i = 5;
  // considering upto square root since in among 2 factors
  // one factor must be below square root of that number
  while (i * i <= n) {
    // prime numbers repeat n+6 and n+6+2 ... this order skips %2 and %3
    if (n % i == 0 || n % (i + 2) == 0) return false;
    i += 6;
  }
  return true;
};
```

2, 3 => multiples are =>  2,3,4,6... k=6 means, k-1 is 5 and k+1 = 7... likewise


##### Skipping Non-Prime Candidates:

The condition `if (n % i == 0 || n % (i + 2) == 0) return false;` checks for divisibility by \( i \) (of the form \( 6k - 1 \)) and \( i + 2 \) (of the form \( 6k + 1 \)). This leverages the fact that all prime numbers greater than 3 can be expressed as \( 6k \pm 1 \). By focusing on these two forms, the algorithm effectively skips all even numbers and multiples of 3, optimizing the primality test.


##### Prime Number Form:

All prime numbers greater than 3 can be represented as \( 6k - 1 \) or \( 6k + 1 \) due to how integers distribute around multiples of 6. 

Any integer \( n \) can be expressed as \( 6k + r \), where \( r \) can be \( 0, 1, 2, 3, 4, \) or \( 5 \). Among these:

- **\( r = 0 \)**: \( n \) is a multiple of 6.
- **\( r = 2 \)**: \( n \) is even.
- **\( r = 3 \)**: \( n \) is a multiple of 3.
- **\( r = 4 \)**: \( n \) is even.

These residues (0, 2, 3, and 4) cannot be prime (except for 2 and 3). Thus, the only candidates that can be prime are those in the forms \( 6k - 1 \) (where \( r = 5 \)) and \( 6k + 1 \) (where \( r = 1 \)). This pattern allows for efficient testing of potential primes.




### The Sieve of Eratosthenes

The Sieve of Eratosthenes is known for its excellent time complexity for finding prime numbers.


prime number seq.. checking - [https://byjus.com/maths/prime-numbers-from-1-to-1000/](https://byjus.com/maths/prime-numbers-from-1-to-1000/)

**Sequence of prime numbers / between ranges**  
Efficient way : ( when space complexity not matters and to find sequence of prime numbers )


```ts
// Time - O(n*log(log(n))
// The Sieve of Eratosthenes algorithm has a time complexity of O(n*log(log(n))) where n is the limit provided.
// This is because the algorithm iterates through all numbers up to the square root of the limit
// and marks multiples of prime numbers as not primes
// Space - O(n) // primes storage upto limit n
function sieveEratosthenes(limit: number): number[] {
  // Create a boolean array "isPrime" and initialize all entries to true
  let isPrime = new Array(limit + 1).fill(true);
  isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime

  // Start with the first prime number, 2
  for (let p = 2; p * p <= limit; p++) {
    // If isPrime[p] is still true, then it is a prime number
    if (isPrime[p]) {
      // Mark all multiples of p as not prime
      for (let i = p * p; i <= limit; i += p) isPrime[i] = false;
    }
  } // Generate and return the list of prime numbers

  let primes = [];
  for (let i = 0; i <= limit; i++) {
    if (isPrime[i]) primes.push(i);
  }
  return primes;
}

let limit = 1000;
let primesUpToLimit = sieveEratosthenes(limit);

console.log(primesUpToLimit);
```


```ts
// Time - O(n*log(log(n))
// Space - O(n) // primes storage upto limit n
function sieveEratosthenesInRange(start: number, end: number): number[] {
  // Create a boolean array "isPrime" and initialize all entries to true
  let isPrime = new Array(end + 1).fill(true);
  isPrime[0] = isPrime[1] = false; // 0 and 1 are not prime

  // Start with the first prime number, 2
  for (let p = 2; p * p <= end; p++) {
    // If isPrime[p] is still true, then it is a prime number
    if (isPrime[p]) {
      // Determine the starting point for marking multiples of p
      // We start marking multiples from p * p to avoid marking smaller multiples
      // We also ensure that the starting point is within the specified range
      let firstMultiple = Math.max(p * p, Math.ceil(start / p) * p);

      // Mark all multiples of p within the specified range as not prime
      for (let i = firstMultiple; i <= end; i += p) isPrime[i] = false;
    }
  }

  // Generate and return the list of prime numbers within the specified range
  let primesInRange = [];
  for (let i = Math.max(2, start); i <= end; i++) {
    if (isPrime[i]) primesInRange.push(i);
  }

  return primesInRange;
}

// Example usage:
let start = 10; // Change the starting point of the range
let end = 50; // Change the ending point of the range
let primesInRange = sieveEratosthenesInRange(start, end);
console.log("Prime numbers between", start, "and", end, "are:", primesInRange);

```


```ts
/*
we consider all as prime and start striking out multiples of each
*/
const checkPrime = (to: number, from: number = 0): boolean => {
  const rangeLen: number = to - from + 1;

  // es6 or later
  // const primes: boolean[] = Array.from({ length: rangeLen - from }, (_, i) => {
  //   const num = i + from;
  //   // Handle special case: mark numbers less than 2 as non-prime
  //   return num >= 2;
  // });

  const primes: boolean[] = [];
  // Loop through the specified range
  for (var i = from; i < rangeLen; i++) {
    var idx = i - from;
    // Handle special case: mark numbers less than 2 as non-prime
    primes[idx] = !(i < 2);
  }

  for (let i = 2; i * i < to + 1; i++) {
    // making all its multiples in the range as false
    // finding firstMultiple, must not below i^2, since we don't need to check them
    const firstMultiple = Math.max(i * i, Math.ceil(from / i) * i);
    for (let j = firstMultiple; j < to + 1; j += i) {
      const ary_idx = j - from;
      primes[ary_idx] = false;
    }
  }

  return primes[rangeLen - from - 1];
};

```



{

try:
can we try steve of eratosthenes with 6k+-1 combinations
}

## Prime regex

Regular expression to check prime numbers:

[https://www.noulakaz.net/2007/03/18/a-regular-expression-to-check-for-prime-numbers/](https://www.noulakaz.net/2007/03/18/a-regular-expression-to-check-for-prime-numbers/)

`/^1?$|^(11+?)\1+$/`

[https://www.youtube.com/watch?v=B9H0TyApBtU](https://www.youtube.com/watch?v=B9H0TyApBtU)

more {  
[https://www.regular-expressions.info/](https://www.regular-expressions.info/)

[https://github.com/tom-lord/regexp-examples](https://github.com/tom-lord/regexp-examples)
  
}

  

However while cute, it is very slow. It tries every possible factorization as a pattern match. When it succeeds, on a string of length n that means that n times it tries to match a string of length n against a specific pattern. This is O(n^2). Try it on primes like 35509, 195341, 526049 and 1030793 and you can observe the slowdown. (Some regular expression engines may employ tricks that speed this up over the naive analysis, but none will be super speedy about it.)




## Extra

##### Tests

```ts

const primeTestCases = [
  {
    name: "Small Prime",
    input: 2,
    expected: true,
    // 2 is the smallest and only even prime number.
  },
  {
    name: "Small Non-Prime 0",
    input: 0,
    expected: false,
    // 0 is not prime as it is not greater than 1.
  },
  {
    name: "Small Non-Prime 1",
    input: 1,
    expected: false,
    // 1 is neither prime nor composite.
  },
  {
    name: "Small Prime 3",
    input: 3,
    expected: true,
    // 3 has no divisors other than 1 and itself.
  },
  {
    name: "Small Prime 5",
    input: 5,
    expected: true,
    // 5 has no divisors other than 1 and itself.
  },
  {
    name: "Small Prime 7",
    input: 7,
    expected: true,
    // 7 has no divisors other than 1 and itself.
  },
  {
    name: "Small Non-Prime 4",
    input: 4,
    expected: false,
    // 4 is divisible by 2.
  },
  {
    name: "Small Prime 17",
    input: 17,
    expected: true,
    // 17 has no divisors other than 1 and itself.
  },
  {
    name: "Small Non-Prime 10",
    input: 10,
    expected: false,
    // 10 is divisible by 2 and 5.
  },
  {
    name: "Large Prime 97",
    input: 97,
    expected: true,
    // 97 has no divisors other than 1 and itself.
  },
  {
    name: "Large Prime 89",
    input: 89,
    expected: true,
    // 89 has no divisors other than 1 and itself.
  },
  {
    name: "Large Prime 101",
    input: 101,
    expected: true,
    // 101 has no divisors other than 1 and itself.
  },
  {
    name: "Small Non-Prime 10 Duplicate",
    input: 10,
    expected: false,
    // 10 is divisible by 2 and 5.
  },
];

function testCheckPrime(func: any) {
  console.log("Testing function:", func.name);

  let allPassed = true; // Flag to track if all test cases passed
  for (const testCase of primeTestCases) {
    const { input, expected, name } = testCase;
    const result = func(input); // Call the function with the input

    // Check if the returned result matches the expected result
    if (result !== expected) {
      console.error(
        `Test case (${name}) failed! Expected ${expected}, got ${result}`,
      );
      allPassed = false; // Set flag to false if any test case fails
      break; // Optional: break after the first failure
    }
  }

  // Print results based on the flag
  if (allPassed) console.log("All test cases passed!");
  else console.log("Some test cases failed.");
}
```


##### More Refs:

{
more :

[https://palak001.medium.com/sieve-of-eratosthenes-b91d3900d72c](https://palak001.medium.com/sieve-of-eratosthenes-b91d3900d72c)

[https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html#segmented-sieve](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html#segmented-sieve)

[https://www.enjoymathematics.com/blog/how-to-find-prime-numbers-in-a-range](https://www.enjoymathematics.com/blog/how-to-find-prime-numbers-in-a-range)

[https://www.geeksforgeeks.org/sieve-of-eratosthenes/](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

[https://www.geeksforgeeks.org/program-to-find-prime-numbers-between-given-interval/](https://www.geeksforgeeks.org/program-to-find-prime-numbers-between-given-interval/)


}



