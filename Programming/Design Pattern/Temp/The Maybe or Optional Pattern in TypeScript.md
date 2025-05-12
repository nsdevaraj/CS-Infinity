
## What Is the Maybe Pattern?

The **Maybe pattern** helps avoid `null` and `undefined` errors by wrapping values in a safe container.


```ts
User {
	Profile? : {
		Name?: string,
	}
}
```

### Traditional Code Example

```ts
if (user && user.profile && user.profile.name) {
  return user.profile.name;
}
return "Anonymous";
```

Or with optional chaining:

```ts
return user?.profile?.name || "Anonymous";
```

### Maybe Pattern Version

```ts
maybe(user)
  .map(u => u.profile)
  .map(p => p.name)
  .getOrElse("Anonymous");
```

This eliminates null checks and improves safety and readability.

---

## Why Use It?

|Problem|Solution|
|---|---|
|Null checks throughout code|Use `Maybe.map()` for safe chaining|
|`undefined is not a function` runtime errors|Value access occurs only when present|
|Complex nested logic for optional values|Code becomes flat and readable|

---

## Example: Implementation

```ts
type Maybe<T> = Just<T> | Nothing;

class Just<T> {
  constructor(private value: T) {}

  map<U>(fn: (val: T) => U): Maybe<U> {
    return new Just(fn(this.value));
  }

  flatMap<U>(fn: (val: T) => Maybe<U>): Maybe<U> {
    return fn(this.value);
  }

  getOrElse(_defaultValue: T): T {
    return this.value;
  }

  orElse(_alternative: () => Maybe<T>): Maybe<T> {
    return this;
  }

  filter(predicate: (val: T) => boolean): Maybe<T> {
    return predicate(this.value) ? this : new Nothing();
  }
}

class Nothing {
  map<U>(_fn: (val: never) => U): Maybe<U> {
    return this;
  }

  flatMap<U>(_fn: (val: never) => Maybe<U>): Maybe<U> {
    return this;
  }

  getOrElse<U>(defaultValue: U): U {
    return defaultValue;
  }

  orElse<T>(alternative: () => Maybe<T>): Maybe<T> {
    return alternative();
  }

  filter(_predicate: (val: never) => boolean): Maybe<never> {
    return this;
  }
}

function maybe<T>(val: T | null | undefined): Maybe<T> {
  return val === null || val === undefined ? new Nothing() : new Just(val);
}

function maybeTry<T>(fn: () => T): Maybe<T> {
  try {
    const result = fn();
    return result === null || result === undefined ? new Nothing() : new Just(result);
  } catch {
    return new Nothing();
  }
}
```




Here's a breakdown of what each method does:


###  `map<U>(fn: (val: T) => U): Maybe<U>`

**Purpose:** Transforms the inner value **if it exists**, wrapping the result back in a `Maybe`.
- Used when you want to **apply a function** to the value (e.g., formatting, math).
- Returns a new `Just(fn(value))` or stays as `Nothing`.


**Example:**

```ts
maybe(5).map(x => x * 2) // => Just(10)
maybe(null).map(x => x * 2) // => Nothing
```


### `flatMap<U>(fn: (val: T) => Maybe<U>): Maybe<U>`

**Purpose:** Like `map`, but for functions that **already return a Maybe** — it avoids nested Maybes (`Maybe<Maybe<U>>`).

- Used for chaining functions that **may also fail or be optional**.


**Example:**

```ts
// A simple function that adds 10 to a number, wrapped in Maybe
function addTen(num: number): Maybe<number> {
  return new Just(num + 10);  // Always returns a Just with num + 10
}

// Using maybe and flatMap
function incrementValue(value: number): Maybe<number> {
  return maybe(value)  // Wrap the value into a Maybe
    .flatMap(num => addTen(num))  // Add 10 using flatMap
    .getOrElse(0);  // If any failure, return 0
}

console.log(incrementValue(5));  // 15
console.log(incrementValue(-3)); // 7
console.log(incrementValue(undefined)); // 0
```


### `getOrElse(_defaultValue: T): T`

**Purpose:** Extracts the value if it exists, or returns a default otherwise.
- Useful at the **end of the chain** when you want a definite value.


**Example:**

```ts
maybe(user.name).getOrElse("Anonymous");
```


### `orElse(_alternative: () => Maybe<T>): Maybe<T>`

**Purpose:** If current `Maybe` is `Nothing`, it tries the fallback by calling `_alternative`.
- **Lazy** fallback — only runs the function if needed.
- Good for **fallback options**, e.g., trying username if name is missing.


**Example:**

```ts
maybe(user.displayname).orElse(() => maybe(user.username));
```



#### getOrElse vs orElse


why not this ?
```ts
const name = maybe(user.public_account) 
             .getOrElse(maybe(user.username)) 
             .getOrElse("Anonymous"); 
```



Explanation of `maybe(user.name).getOrElse(maybe(user.username))`:

1. **`maybe(user.name)`**: This creates a `Maybe` instance that wraps `user.name`, which could be `null`, `undefined`, or a valid value.

2. **`.getOrElse(maybe(user.username))`**: Here’s where things go wrong.
    - **`getOrElse`** expects a **default value** (not another `Maybe` instance). This is meant to be a **value**, not an operation that returns a `Maybe`.
    - When you provide `maybe(user.username)`, you are actually passing a `Maybe` inside `getOrElse`, but the method is designed to accept **a plain value** to return when the `Maybe` is empty (`Nothing`). It does not handle nested `Maybe`s in this way.
    
    **`getOrElse()`** does not handle the situation where the fallback is also a `Maybe`. Instead, it expects the **final value** (not a `Maybe`) to return when the first `Maybe` is `Nothing`.


Why It Doesn’t Work:

- **`getOrElse()`** unpacks the value from the `Maybe`. If `maybe(user.name)` is `Nothing`, it would try to use `maybe(user.username)` as the fallback. But since `maybe(user.username)` is already a `Maybe`, you’ll end up with a nested `Maybe`. This is not what `getOrElse` is designed to handle.



### `filter(predicate: (val: T) => boolean): Maybe<T>`

**Purpose:** Keeps the value only if it passes the predicate — otherwise becomes `Nothing`.
- Used to **conditionally reject values** in the chain.


**Example:**

```ts
maybe(age).filter(a => a >= 18) // Only keeps age if 18+
```


---

## How to Use It Elegantly

### Wrapping a Possibly Null Value

```ts
const name = maybe(user.name).getOrElse("Anonymous");
```

### Chaining Transformations

```ts
maybe(user)
  .map(u => u.profile)
  .map(p => p.email)
  .getOrElse("no-email@example.com");
```

### Using Fallbacks with `orElse()`

```ts
maybe(primaryValue)
  .orElse(() => maybe(secondaryValue))
  .getOrElse("default");
```

---

## Key Benefits

- Eliminates null checks
- Improves code readability
- Makes error handling explicit


---

## Optional Chaining vs. Maybe

### Optional Chaining (Good for Simple Cases)

```ts
const name = user?.profile?.name ?? "Anonymous";
```

Advantages:
- Short
- Readable

Limitations:
- Not composable
- Limited to direct property access and fallback


---

## Where Maybe Excels

### 1. Multiple Transformations


#### Single Transformation 

```ts
const shortName = maybe(user)
  .map(u => u.profile)
  .map(p => p.name)
  .map(n => n.toUpperCase())
  .getOrElse("UNKNOWN");
```

Versus optional chaining:

```ts
const shortName = user?.profile?.name?.toUpperCase() ?? "UNKNOWN";
```

Maybe becomes preferable as the chain grows or transformations increase in complexity.


Let’s make the **Multiple Transformations** example more compelling by showing a longer, real-world data chain where each step could potentially fail, and where the transformations go beyond just a single method call.


#### Multiple Transformations

Let’s say we want to extract a user’s **city** from a deeply nested object, normalize it (trim, lowercase), and capitalize it.

##### ✅ With the `Maybe` Monad:

```ts
const city = maybe(user)
  .map(u => u.profile)
  .map(p => p.contactInfo)
  .map(c => c.address)
  .map(a => a.city)
  .map(c => c.trim())
  .map(c => c.toLowerCase())
  .map(c => c[0].toUpperCase() + c.slice(1))
  .getOrElse("Unknown City");
```

Each step is safe, cleanly chained, and transformation logic is declarative.

##### ❓ Optional Chaining Equivalent (less clean):


```ts
const normalizedCity = user?.profile?.contactInfo?.address?.city
  ?.trim()
  ?.toLowerCase()
  ?[0].toUpperCase() + user.profile.contactInfo.address.city.trim().toLowerCase().slice(1) ?? "Unknown City";

```

```ts
const city = user?.profile?.contactInfo?.address?.city
  ?.trim()
  ?.toLowerCase();

const normalizedCity = city
  ? city[0].toUpperCase() + city.slice(1)
  : "Unknown City";
```

While this works, it becomes harder to read and maintain as logic grows — the fallback and transformation steps are disjointed and mixed.

### 💡 Why This Is Better

| With Maybe Monad                                    | With Optional Chaining                                  |
| --------------------------------------------------- | ------------------------------------------------------- |
| Clearly separated steps                             | Logic feels fragmented                                  |
| Easy to extend (add `.filter()`, `.flatMap()` etc.) | More awkward to insert conditional logic                |
| Encourages pure, composable functions               | Can drift toward imperative/defensive style             |
| Safer — any failure short-circuits cleanly          | Risk of `undefined` creeping in with more complex logic |

Would you like an even more complex transformation — like extracting and formatting a list or performing fallback lookup from another source?

### 2. Alternative Fallback Paths

```ts
const name = maybe(user.displayname)
  .orElse(() => maybe(user.username))
  .getOrElse("Anonymous");
```

Compared to:

```ts
const name = user?.displayname ?? user?.username ?? "Anonymous";
```

Maybe allows composable, readable fallback logic.

---

### 3. Wrapping Risky Operations

```ts
function tryParse(json: string): Maybe<any> {
  try {
    return maybe(JSON.parse(json));
  } catch {
    return new Nothing();
  }
}

const data = tryParse(rawInput)
  .map(obj => obj.value)
  .getOrElse("default");
```


```ts
const data =  maybeTry(() => JSON.parse(rawInput))
  .map(obj => obj.value)
  .getOrElse("default");

```


This pattern is not achievable with optional chaining alone.

---

## Summary Table: Maybe vs. Optional Chaining

| Use Case                       | Optional Chaining | Maybe Pattern   |
| ------------------------------ | ----------------- | --------------- |
| Simple nested access           | Supported         | Supported       |
| Multiple safe transformations  | Verbose           | Clean           |
| Fallback to alternative values | Imperative        | Composable      |
| Wrapping risky functions       | Not supported     | Fully supported |


---

## Refactoring Examples:

### Refactoring Example: Marketable Location Description

#### Before

```ts
function getProfile(marketableLocation: MarketableLocation) {
  const locationDescription =
    marketableLocation.location_description ||
    marketableLocation.location_description_short;

  if (!locationDescription) {
    return {
      description: '',
    };
  }

  return {
    description: formatDescription(
      locationDescription,
      DescriptionMaximumLength.GOOGLE_BUSINESS_PROFILE,
    ),
  };
}
```

#### After (Using Maybe)

```ts
function getProfile(marketableLocation: MarketableLocation) {
  return maybe(marketableLocation.location_description)
    .orElse(() => maybe(marketableLocation.location_description_short))
    .map(desc =>
      formatDescription(desc, DescriptionMaximumLength.GOOGLE_BUSINESS_PROFILE)
    )
    .map(description => ({ description }))
    .getOrElse({ description: '' });
}
```

---

## Refactoring Example: Phone Number Formatting

#### Before

```ts
export function getPhoneNumberToSyndicate(phoneNumber: string): string {
  try {
    const formattedPhoneNumber = formatPhoneNumber(phoneNumber);
    return formattedPhoneNumber || phoneNumber;
  } catch (error) {
    return phoneNumber;
  }
}
```


```ts
function formatPhoneNumber(inputPhoneNumber: string): string | undefined {
  const phoneNumber = parsePhoneNumberWithError(inputPhoneNumber, {
    extract: false,
    defaultCountry: US_COUNTRY_CODE,
  });

  const isValid = phoneNumber?.isValid() && phoneNumber.country === US_COUNTRY_CODE;
  return isValid ? phoneNumber.format(PHONE_NUMBER_FORMATTING_STANDARD.E164) : undefined;
}
```


#### After (Using Maybe)

```ts
function tryFormatPhoneNumber(raw: string): Maybe<string> {
  return maybeTry(() => parsePhoneNumberWithError(raw, {
    extract: false,
    defaultCountry: US_COUNTRY_CODE,
  }))
    .filter(p => p.isValid() && p.country === US_COUNTRY_CODE)
    .map(p => p.format(PHONE_NUMBER_FORMATTING_STANDARD.E164));
}

export function getPhoneNumberToSyndicate(phoneNumber: string): string {
  return tryFormatPhoneNumber(phoneNumber).getOrElse(phoneNumber);
}
```

---

## Is Maybe a Design Pattern?

The **Maybe pattern** is best described as a **functional programming pattern**, not a classical object-oriented design pattern.

### Comparison

|Aspect|Design Pattern|Functional Pattern (e.g., Maybe)|
|---|---|---|
|Origin|Object-Oriented Programming|Functional Programming|
|Structure|Focused on object relationships|Focused on value transformations|
|Goal|Solve class design issues|Solve control flow and error handling|
|Example|Singleton, Factory, Observer|Maybe, Either, IO, Task|


`Maybe` (a.k.a. `Option`) monad implementation - typically used to **safely handle nullable or optional values** in a functional style — without using a lot of `if` checks or `?.` chains.


The **Maybe** pattern is a **functional programming pattern** (and also a form of a **monad**), used to safely represent optional values.

---
