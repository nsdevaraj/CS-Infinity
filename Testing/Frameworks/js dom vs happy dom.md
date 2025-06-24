

### 📦 Overview

|Feature|**JSDOM**|**Happy DOM**|
|---|---|---|
|Maintainer|Maintained by the `jsdom` team (linked to Mozilla)|Community-maintained (fast-growing)|
|Language|Written in JavaScript|Written in TypeScript|
|Usage|Used by **Jest**, **Mocha**, etc.|Used in **Vitest**, some ESM-native tools|
|Performance|Slower|**Faster (~2–10×)**|
|Fidelity|**High spec accuracy**|Good, but not as deep as JSDOM|

---

### ⚙️ Technical Differences

#### ✅ **JSDOM**

- Simulates the browser using the WHATWG DOM and HTML specs
    
- Very close to real browser behavior
    
- Heavier and slower to initialize
    
- Great for testing edge cases and browser quirks
    

#### ✅ **Happy DOM**

- Designed for **speed and ESM-first tools** (like Vitest)
    
- Implements just enough DOM to be useful for most app/unit tests
    
- Fast and lightweight — ideal for headless or large test suites
    
- Slightly less accurate for things like layout, styles, and browser quirks
    

---

### ⚡ Performance Snapshot

|Operation|**JSDOM**|**Happy DOM**|
|---|---|---|
|Initialization Time|~50–300ms|~5–20ms|
|Memory Usage|Higher|Lower|
|Parallel Test Support|Moderate|**Better scaling**|

> 🧪 Real-world: Happy DOM is often **5–10× faster** than JSDOM in large test suites.

---

### 🧪 Feature Comparison

|Capability|**JSDOM**|**Happy DOM**|
|---|---|---|
|HTML parsing/rendering|✅|✅|
|CSS parsing|⚠️ Partial|⚠️ Limited|
|Web APIs (e.g., fetch)|❌ (manual or polyfill)|⚠️ (partial support)|
|`document.createElement`|✅|✅|
|`requestAnimationFrame`|✅|✅|
|Web components / shadow DOM|✅|⚠️ Experimental|
|Speed|🐢 Slower|🐇 **Faster**|

---

### 🤔 When to Use What?

|Scenario|Recommended Tool|
|---|---|
|Realistic browser simulation|**JSDOM**|
|Fast unit/component testing|**Happy DOM**|
|Full React/Vue app tests|JSDOM (more support)|
|Large test suite needing speed|**Happy DOM**|
|DOM-specific edge-case behavior|JSDOM|
|Using **Vitest**|**Happy DOM** is the default and best option|

---

### 🧠 TL;DR

|Category|**JSDOM**|**Happy DOM**|
|---|---|---|
|Accuracy|🏆 Browser-like|✅ Good enough|
|Speed|🐢 Slow|⚡ Very Fast|
|Ecosystem|Well-established|Modern (Vitest-ready)|
|Language|JavaScript (older)|TypeScript (modern)|
