
# 🎯 Web Scraping with Playwright — Deep Dive

### Sections:

1. **Setting Up Playwright and Basic Scraping Concepts**
    
2. **Handling Dynamic Content, Pagination, and Authentication**
    
3. **Advanced Techniques: Stealth, Bypassing Bot Detection, and Scraping at Scale**
    

---

# 📚 Section 1: Setting Up Playwright and Basic Scraping Concepts

## 1. What is Playwright?

[Playwright](https://playwright.dev/) is a Node.js library by Microsoft that allows you to **automate browsers** (Chromium, Firefox, WebKit) via a powerful API.  
Unlike traditional scraping libraries like `requests` or `axios`, Playwright **controls a real browser**, allowing you to scrape **JavaScript-heavy websites** easily.

✅ Works with Single Page Applications (SPAs)  
✅ Supports headless and headful modes  
✅ Allows browser context management (incognito, multiple users, etc.)

---

## 2. Install Playwright

First, set up a project:

```bash
mkdir playwright-scraper
cd playwright-scraper
npm init -y
npm install playwright
```

Optionally, install browsers:

```bash
npx playwright install
```

This downloads Chromium, Firefox, and WebKit browsers.

---

## 3. Your First Scraper

Let’s scrape **example.com** (static page, easy start).

```javascript
// scrape-example.js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true }); // true = no GUI
  const page = await browser.newPage();

  await page.goto('https://example.com');

  const title = await page.title();
  const textContent = await page.textContent('h1');

  console.log({ title, textContent });

  await browser.close();
})();
```

Run it:

```bash
node scrape-example.js
```

You’ll get:

```json
{
  "title": "Example Domain",
  "textContent": "Example Domain"
}
```

---

## 4. Playwright Browser, Context, Page Model

**Key Playwright Concepts** you need to know:

|Concept|Description|Analogy|
|:--|:--|:--|
|`Browser`|Physical browser instance (e.g., Chrome)|The actual Chrome app|
|`Context`|Separate browser profile/session|Different Chrome user profile|
|`Page`|Single tab in the browser|A tab in Chrome|

✅ Multiple contexts allow you to simulate multiple users without launching multiple browsers.

Example:

```javascript
const browser = await chromium.launch();
const context = await browser.newContext();
const page = await context.newPage();
```

---

## 5. Selecting Elements

You can grab elements using CSS selectors (like in the browser console).

Examples:

```javascript
await page.textContent('h1'); // Get text inside <h1>
await page.getAttribute('a', 'href'); // Get href attribute
await page.innerHTML('p'); // Get inner HTML
await page.click('button#submit'); // Click a button
```

You can also use more complex selectors:

```javascript
await page.locator('div.product-item >> text="Add to Cart"').click();
```

---

## 6. Scraping Lists (Multiple Elements)

Scraping multiple items (e.g., list of products):

```javascript
const items = await page.$$eval('ul li', elements =>
  elements.map(el => el.textContent.trim())
);

console.log(items);
```

- `$$eval` evaluates an array of elements.
    
- You map over each and extract text.
    

---

## 7. Saving Data

You usually want to **save the scraped data**:

Example to save as a JSON file:

```javascript
const fs = require('fs');

fs.writeFileSync('output.json', JSON.stringify(items, null, 2));
```

---

## 8. Basic Error Handling

Always wrap your navigation and scraping in try/catch:

```javascript
try {
  await page.goto('https://example.com', { timeout: 10000 });
} catch (err) {
  console.error('Failed to load page:', err);
}
```

- `timeout` ensures you don't hang forever.
    
- Good practice for production scrapers.
    

---

# 🧠 Quick Recap of Section 1

|You learned|Example|
|:--|:--|
|Install Playwright|`npm install playwright`|
|Launch browser, page|`chromium.launch()`, `browser.newPage()`|
|Select elements|`page.textContent()`, `page.$$eval()`|
|Save data|`fs.writeFileSync()`|
|Basic error handling|`try/catch around page.goto()`|

---



# 📚 Section 2: Handling Dynamic Content, Pagination, and Authentication

## 1. Scraping Dynamic Content

Many modern websites **load data dynamically** (via JavaScript).  
With Playwright, **waiting** for elements properly is critical.

Instead of rushing right after `page.goto()`, you wait for **specific elements**:

```javascript
await page.goto('https://example.com/products');

// Wait for products to appear
await page.waitForSelector('.product-card');

// Now scrape
const products = await page.$$eval('.product-card', cards =>
  cards.map(card => ({
    title: card.querySelector('h2').textContent,
    price: card.querySelector('.price').textContent
  }))
);

console.log(products);
```

✅ **Rule**: Always `waitForSelector` before interacting.

---

## 2. Handling Lazy-loaded / Infinite Scroll Pages

Some pages **load more items as you scroll**.

Playwright lets you **scroll** programmatically:

```javascript
// Scroll to bottom multiple times to trigger lazy loading
for (let i = 0; i < 5; i++) {
  await page.evaluate(() => window.scrollBy(0, window.innerHeight));
  await page.waitForTimeout(1000); // wait 1 sec after each scroll
}

// Now scrape loaded content
const items = await page.$$eval('.item', nodes =>
  nodes.map(n => n.innerText.trim())
);

console.log(items);
```

✅ **Tip**: Adjust scrolling times and timeout based on the site behavior.

---

## 3. Dealing with Pagination (Next Button or Page Numbers)

### Method 1: Clicking "Next" button until no more pages

```javascript
let hasNextPage = true;
const results = [];

while (hasNextPage) {
  await page.waitForSelector('.product-card');

  const products = await page.$$eval('.product-card', cards =>
    cards.map(card => ({
      title: card.querySelector('h2').textContent,
      price: card.querySelector('.price').textContent
    }))
  );

  results.push(...products);

  // Check if next button exists and is enabled
  const nextButton = await page.$('button.next');
  if (nextButton) {
    await nextButton.click();
    await page.waitForTimeout(2000); // wait for next page load
  } else {
    hasNextPage = false;
  }
}

console.log(results);
```

---

### Method 2: Scraping through URL Patterns (e.g., `?page=1`, `?page=2`)

If the site uses URL-based pagination, it's even simpler:

```javascript
const results = [];

for (let pageNum = 1; pageNum <= 5; pageNum++) {
  await page.goto(`https://example.com/products?page=${pageNum}`);
  await page.waitForSelector('.product-card');

  const products = await page.$$eval('.product-card', cards =>
    cards.map(card => ({
      title: card.querySelector('h2').textContent,
      price: card.querySelector('.price').textContent
    }))
  );

  results.push(...products);
}

console.log(results);
```

✅ **Tip**: Always look for URL parameters first. They are easier and faster than clicking.

---

## 4. Handling Authentication

### 4.1 Basic Auth (username/password popup)

Some sites trigger a basic auth popup.  
Playwright handles this via context options:

```javascript
const context = await browser.newContext({
  httpCredentials: {
    username: 'myUser',
    password: 'myPassword'
  }
});

const page = await context.newPage();
await page.goto('https://protectedsite.com');
```

---

### 4.2 Login Form (email/password fields)

For **regular login pages**, you automate filling forms:

```javascript
await page.goto('https://example.com/login');

// Fill and submit
await page.fill('input[name="email"]', 'your@email.com');
await page.fill('input[name="password"]', 'yourPassword123');
await page.click('button[type="submit"]');

// Wait for post-login page to load
await page.waitForNavigation();

// Now scrape protected content
await page.goto('https://example.com/account');
const userName = await page.textContent('h1.user-name');
console.log('Logged in as:', userName);
```

✅ **Tip**: Save the login session (cookies) to avoid logging in every time (covered in Section 3).

---

## 5. Dealing with Popups, Modals, and Interstitials

Some websites show annoying popups.  
You can **close** them manually:

```javascript
// Check and close if popup appears
const closeButton = await page.$('.popup-close-button');
if (closeButton) {
  await closeButton.click();
  console.log('Closed popup');
}
```

✅ **Tip**: Wrap popup closing code in try/catch. Some pages won't show it every time.

---

# 🧠 Quick Recap of Section 2

|You learned|Example|
|:--|:--|
|Wait for elements dynamically|`page.waitForSelector()`|
|Handle infinite scrolling|`window.scrollBy(0, window.innerHeight)`|
|Scrape paginated sites|Click next or loop URLs|
|Automate login|`page.fill() + page.click()`|
|Handle popups|Check + close|


---

# 📚 Section 3: Advanced Techniques — Stealth, Anti-Bot Bypass, and Scaling

---

## 1. Running Stealth Browsers (Avoid Detection)

Most websites use bot detection techniques:

- Detect **headless browsers** (`navigator.webdriver === true`)
    
- Check **weird screen sizes**
    
- Detect missing browser features (plugins, languages)
    

➡️ Solution: **Use Stealth Mode**.

Install [`playwright-extra`](https://github.com/berstend/puppeteer-extra) and plugins:

```bash
npm install playwright-extra playwright-extra-plugin-stealth
```

Then, use it:

```javascript
const { chromium } = require('playwright-extra');
const StealthPlugin = require('playwright-extra-plugin-stealth')();

// Add stealth plugin
chromium.use(StealthPlugin());

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  await page.goto('https://bot.sannysoft.com'); // test site
  await page.screenshot({ path: 'test-stealth.png' });

  await browser.close();
})();
```

✅ Now your scraper **mimics a real user** far better.

---

## 2. Rotating User Agents and Viewports

Every scraper should **rotate user agents** to look more real.

Example:

```javascript
const fakeUserAgents = [
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15',
  // Add more
];

const context = await browser.newContext({
  userAgent: fakeUserAgents[Math.floor(Math.random() * fakeUserAgents.length)],
  viewport: { width: 1280, height: 720 }
});

const page = await context.newPage();
```

✅ Pro tip: Also rotate `viewport` size slightly.

---

## 3. Handling Captchas

If the website uses **Captcha** (e.g., reCAPTCHA, hCaptcha):

### 3.1 Manual Solve (Basic)

You can detect it and pause:

```javascript
await page.screenshot({ path: 'captcha.png' });
console.log('Manual captcha detected! Solve it manually...');
await page.pause(); // Open Playwright Inspector
```

You solve it by hand when running in `headful` mode.

---

### 3.2 Automated Solving (Advanced)

You can integrate third-party services:

- [2Captcha](https://2captcha.com/)
    
- [Anti-Captcha](https://anti-captcha.com/)
    

➡️ They solve captchas for you via API.  
But this usually costs **real money**.

---

## 4. Using Proxies to Hide Your IP

Scraping heavily from the same IP will get you **rate-limited** or **banned**.

Use **proxies** (residential, datacenter, rotating):

```javascript
const browser = await chromium.launch({
  proxy: {
    server: 'http://myproxyserver:3128',
    username: 'proxyUser',
    password: 'proxyPass'
  }
});
```

✅ Rotate proxies frequently if scraping large datasets.

---

## 5. Scraping in Parallel (Speeding Things Up)

**Single-threaded** scraping is slow.  
**Multi-page** or **multi-browser** parallel scraping speeds it up drastically.

Example: Open multiple pages simultaneously.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();

  const urls = [
    'https://example.com/page1',
    'https://example.com/page2',
    'https://example.com/page3'
  ];

  const pages = await Promise.all(
    urls.map(url => context.newPage())
  );

  await Promise.all(
    pages.map((page, i) => page.goto(urls[i]))
  );

  const titles = await Promise.all(
    pages.map(page => page.title())
  );

  console.log(titles);

  await browser.close();
})();
```

✅ Rule: **Don’t open 1000 tabs at once** — browsers can crash.  
Limit concurrency, e.g., **5–10 pages at a time**.

(You can use libraries like [p-limit](https://www.npmjs.com/package/p-limit) for better control.)

---

## 6. Session Persistence (Saving Login State)

After logging into a website once, **save the cookies** and **reuse them**.

### Save cookies:

```javascript
await context.storageState({ path: 'auth.json' });
```

### Load cookies next time:

```javascript
const context = await browser.newContext({
  storageState: 'auth.json'
});
```

✅ Now you stay logged in across scraping sessions!

---

## 7. Setting Custom Headers and Other Tweaks

For more realism:

```javascript
await page.setExtraHTTPHeaders({
  'Accept-Language': 'en-US,en;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br'
});
```

✅ Helps mimic a **real browser network request**.

---

# 🧠 Quick Recap of Section 3

|You learned|Example|
|:--|:--|
|Stealth browsing|`playwright-extra` + stealth plugin|
|Rotate user agents, viewport|`newContext({ userAgent })`|
|Solve captchas|Manual or via API|
|Use proxies|`launch({ proxy: { server } })`|
|Scrape in parallel|`Promise.all()` over multiple pages|
|Save sessions|`storageState()`|
|Custom headers|`setExtraHTTPHeaders()`|

---

# 🎯 Full Deep Dive Summary

✅ **Section 1**: Playwright Basics  
✅ **Section 2**: Dynamic Content, Pagination, Login  
✅ **Section 3**: Stealth Mode, Anti-Bot, Scaling

---

# ⚡ Bonus: Suggested Best Practices

- Always **respect robots.txt** if legally required.
    
- Implement **random delays** between actions (`waitForTimeout` random between 500ms-3000ms).
    
- Always **log errors** and handle retries.
    
- **Throttle** your scraping to avoid overloading servers (polite scraping!).
    
- Consider **headful** mode for very bot-sensitive sites.
    

