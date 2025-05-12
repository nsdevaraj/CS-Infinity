

Sure — here is your content rewritten in a clean, formal Markdown format without emojis or informal elements:

---

# The Maybe Pattern in TypeScript

## What Is the Maybe Pattern?

The **Maybe pattern** is a functional approach to safely handle optional values. It encapsulates the presence (`Just`) or absence (`Nothing`) of a value, avoiding the need for repeated `null` or `undefined` checks.

### Traditional Approach

```ts
if (user && user.profile && user.profile.name) {
  return user.profile.name;
}
return "Anonymous";
```

Or using optional chaining:

```ts
return user?.profile?.name || "Anonymous";
```

### Maybe Pattern Alternative

```ts
maybe(user)
  .map(u => u.profile)
  .map(p => p.name)
  .getOrElse("Anonymous");
```

This avoids explicit null checks and creates a readable, fluent flow.

---

## Why Use the Maybe Pattern?

|Problem|Solution|
|---|---|
|Repetitive null checks|`Maybe.map()` chains safely|
|Runtime errors like `undefined is not a function`|No access occurs unless the value is present|
|Complex fallback and transformation logic|Simplified, declarative structure|

---

## Basic Implementation

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

---

## How to Use It Elegantly

### 1. Wrapping Optional Values

```ts
const name = maybe(user.name).getOrElse("Anonymous");
```

### 2. Safe Chaining of Operations

```ts
maybe(user)
  .map(u => u.profile)
  .map(p => p.email)
  .getOrElse("no-email@example.com");
```

### 3. Declarative Fallbacks

```ts
maybe(primaryValue)
  .orElse(() => maybe(secondaryValue))
  .getOrElse("default");
```

---

## Optional Chaining vs. Maybe

Optional chaining is suitable for simple cases:

```ts
const name = user?.profile?.name ?? "Anonymous";
```

However, it becomes limiting for more complex flows.

### Comparison Table

|Use Case|Optional Chaining|Maybe Pattern|
|---|---|---|
|Simple nested access|Supported|Supported|
|Multiple transformations|Verbose|Clean and composable|
|Alternative values|Imperative|Declarative and chainable|
|Wrapping risky operations|Not supported|Supported via `maybeTry`|

---

## Example: Using Maybe with Fallbacks

### Before

```ts
function getProfile(marketableLocation: MarketableLocation) {
  const locationDescription =
    marketableLocation?.location_description ||
    marketableLocation?.location_description_short;

  if (!locationDescription) {
    return { description: '' };
  }

  return {
    description: formatDescription(
      locationDescription,
      DescriptionMaximumLength.GOOGLE_BUSINESS_PROFILE,
    ),
  };
}
```

### After (Using Maybe)

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

### Benefits

|Feature|Benefit|
|---|---|
|Null safety|No need for manual checks|
|Readability|Clear transformation steps|
|Maintainability|Easier to test and refactor|

---

## Example: Phone Number Formatting

### Before

```ts
export function getPhoneNumberToSyndicate(phoneNumber: string): string {
  try {
    const formattedPhoneNumber = formatPhoneNumber(phoneNumber);
    return formattedPhoneNumber || phoneNumber;
  } catch {
    return phoneNumber;
  }
}
```

### After (Using Maybe)

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

---

Let me know if you would like this content packaged into a PDF or formatted for a slide presentation.