



![[RenderingDiffs.png]]


### Server Rendering  - old way

old websites and old web development works on Server Side Rendering .. Almost no client side things ( just few js for interactivity) , server is the tough and heavy guy to do all works  , need powerful server, but no need powerful client.. any navigation click on page will do full page rerender.. 

### 1. CSR (Client-Side Rendering) - on client
- **Definition**: Renders web pages on the client side using JavaScript.
- **Process**:
  - **Source Code**: All JavaScript, HTML, and CSS are written in files.
  - **Build Phase**: The command `npm run build` prepares the code for production.
  - **Server Phase**: HTML, JavaScript, and CSS are stored separately.
  -  **Client Phase**: An empty HTML page is sent to the client; JavaScript is responsible for rendering content after the page loads.  This JavaScript request CSS file and further JavaScript files needed for rendering. 
- **SEO Impact**: Poor for SEO since the content is generated client-side, leading to empty HTML at first.
-    CSR - is the core React flow... 
-  React and all fontend frameworks came out, followed this.. then due to some drawbacks, other rendering patterns were discovered!
- absolutely no server work, the client do all work from the gotten js file


### 2. SSR (Server-Side Rendering) - on server
- **Definition**: Renders web pages on the server before sending them to the client.
- **Process**:
  - **Source Code**: HTML, JavaScript, and CSS are still prepared in the same way.
  - **Request Handling**: When a client requests a page, the server generates the complete HTML page.
  - **Advantages**: Faster loading for users as content is pre-rendered; better for SEO as search engines can see the full HTML content.
- **Performance**: Utilizes server's higher compute power to render pages quickly. Don't depend on client's machine's power.
- usual approach of Next JS
- more work on server and some work on client ( not no work like old web pages server rendering), server give html, client hookup html with frontend framework using ( hydration phase ) !

### 3. SSG (Static Site Generation) - on build
- **Definition**: Generates static HTML pages at build time. 
- Any CMS like wordpress websites use this SSG, since they are slower on other approches since content are dynamic 
- **Process**:
  - **Build Phase**: During the build, HTML pages are created based on known content.
  -  Generate Each page and store on server, painfully long build time and server storage, any update again we do build and publish, not feasible for frequently changing contents.
  - **Storage**: All pages are stored on the server, ready to be served without additional rendering.
- **Advantages**: Fast delivery of content since static pages don’t require server computation for each request.
- **Use Case**: Ideal for sites with infrequent content updates (e.g., blogs).
- Gatsby known for it, Astro also uses it
- if app has 1k pages, this apporaches create 1k unique html pages on build time, serving them on client request.. no server and client work.. but no dynamic content..

### 4. ISR (Incremental Static Regeneration) - specific update on build
- **Definition**: Combines SSG with the ability to update content dynamically.
- **Process**:
  - **Scheduled Rebuilds**: Pages can be rebuilt at specified intervals.
  - **Advantage**: Fresh content is served without requiring a complete site rebuild.
- **Use Case**: Useful for content that updates occasionally, maintaining performance while keeping information current.
- combines with SSG and SSR - some pgs are SSG and some dynamic pages of SSR.. gives fast build time and have dynamic content pages, so pages not build on buildTime will be build on server on demand by client ( some times it give stale version of page and generate new version for next request or now itself create page and send it.. based on setup ). When user request data, if the data on stale is out of date, then server will regenerate.. so work on server is medium when current stale is out of date or no work , just use cache version of page.. 
- for Ecommer site where no  products change often or CMS systems whose content don't change often

## Comparison of Approaches
- **Build Time**: Important for deciding which method to use based on how often updates are required. - server build time vs client build time
- **Dynamic Content**: Assess how frequently the content changes to choose the right rendering approach. - how often updated
- **SEO Requirements**: Consider the importance of SEO—SSR and ISR are typically better for SEO than CSR. - SEO is valuable for you or not
- **Rendering Time**: Evaluate whether it’s more crucial for the server or client to handle rendering. - build time vs server time vs client time
- **Content Updates**: Determine how often content needs to be refreshed to find the best fit. - how often content update happen

Here's a comparison table highlighting the differences between the different rendering methods:

| Feature                        | Old Way (Traditional Server Rendering) | CSR (Client-Side Rendering)             | SSR (Server-Side Rendering)              | SSG (Static Site Generation)            | ISR (Incremental Static Regeneration)    |
|---------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-----------------------------------------|------------------------------------------|
| **Rendering Process**           | HTML is fully rendered on the server and sent to the client. | JavaScript renders the page on the client side after downloading raw data. | Server renders the page for every request, then sends HTML to the client. | Pages are pre-built as static HTML at build time. | Combines SSG with the ability to regenerate static pages on request. |
| **Performance**                 | Slow initial load, fast interactions.  | Fast initial load if cached, otherwise can be slow. | Fast initial load, slower for high traffic. | Extremely fast, served as static files.  | Fast, and pages can be updated without rebuilding the whole site. |
| **Initial Page Load**           | Full page loads with every request.    | Blank page until JavaScript loads and renders content. | Full page HTML delivered on first load.  | Instant delivery as pre-built static pages. | Same as SSG, but with dynamic updates possible. |
| **SEO Friendliness**            | Good for SEO as content is fully rendered. | Poor, content is rendered client-side which affects SEO unless SSR fallback is used. | Excellent for SEO as HTML is rendered server-side. | Excellent for SEO since pages are pre-rendered. | Excellent, similar to SSG, with flexibility to regenerate. |
| **Use Cases**                   | Traditional web applications, forms, etc. | Single Page Applications (SPAs) needing fast, dynamic interactions. | Web apps needing SEO, where data changes per request. | Blogs, marketing sites, documentation, static content. | Dynamic content with static-like performance, e.g., e-commerce. |
| **Interactivity**               | Limited client-side interactivity.     | High interactivity; relies on JavaScript. | Server handles initial page, then client-side interactivity via JavaScript. | Limited interactivity unless JavaScript is added later. | Same as SSG, but can serve updated pages. |
| **Caching**                     | Requires heavy use of caching for better performance. | Can use client-side caching mechanisms, slower for initial render. | Can use server caching, good for repeated requests. | Automatically cached, no need for server-side resources. | Caches pre-rendered pages and regenerates as needed. |
| **Content Updates**             | Requires page reload or AJAX calls.    | Client-side data fetching for updates.  | Dynamic content with every request.      | Content is static, must rebuild site for updates. | Updates can happen during runtime without full rebuild. |
| **Complexity**                  | Simple but may need extra effort for interactivity. | More complex due to heavy reliance on JavaScript. | Medium complexity, combining server rendering with client-side logic. | Simple for static sites, no backend required. | More complex, requires backend and regeneration logic. |

Reffered {
CSR SSR SSG ISR
https://www.youtube.com/watch?v=YkxrbxoqHDw
https://www.youtube.com/watch?v=p02AIAoImzU

}


---


## Every rendering pattern flow

reffered {

10 patthers - quick view - better watching then reading
https://www.youtube.com/watch?v=Dkx5ydvtpCA

}


### 1. **Static Website**
   - Pre-render all web pages as static files.
   - Upload files to a storage bucket and point a domain to them.
   - Frameworks: **Hugo, 11ty, Jekyll**.
   - Great for basic websites without frequent data changes.
   - **Drawback**: Not suitable for websites with dynamic data or interactivity.

### 2. **Multi-Page Applications (MPA)**
   - HTML and data are dynamically generated on the server for each request.
   - Example: **Amazon.com** (new page generated with every link).
   - Frameworks: **Ruby on Rails, Django, Laravel**, CMS like **WordPress**.
   - Good for apps where data changes frequently.
   - **Drawback**: Feels clunky with full-page reloads, especially compared to mobile apps.

### 3. **Single Page Applications (SPA)**
   - All UI rendering happens in the browser via **JavaScript**.
   - Starts with one HTML shell; UI is rendered dynamically with JavaScript.
   - Routes are handled by JavaScript without full page reloads.
   - Frameworks: **AngularJS, React**.
   - **Advantages**: Feels instantaneous, fluid user experience.
   - **Disadvantages**:
     - Large JavaScript bundles, slow initial page load.
     - Poor SEO since search engines have trouble indexing dynamic content.

### 4. **Server-Side Rendering (SSR)**
   - Initial request renders HTML and data on the server, then hydrates to JavaScript on the client-side.
   - Combines benefits of SPA and MPA: dynamic, SEO-friendly, app-like experience.
   - Frameworks: **Next.js, Nuxt, SvelteKit**.
   - **Drawback**: Requires an actual server, which costs money.

### 5. **Static Site Generation (SSG)**
   - Render all HTML in advance (like static websites), but with the ability to hydrate to JavaScript for dynamic interactivity.
   - Part of the **JAMstack** ecosystem.
   - Frameworks: **Next.js, Nuxt, SvelteKit**.
   - **Advantages**: Low-cost static hosting, fast loading times.
   - **Drawback**: Must redeploy the site for any content updates.

### 6. **Incremental Static Regeneration (ISR)**
   - Combines static generation with the ability to rebuild individual pages on the fly.
   - Pages are cached and re-built based on specific rules (e.g., time-based).
   - Framework: **Next.js**.
   - **Advantages**: Handles dynamic data while keeping static-like performance, no full redeployment needed.
   - **Drawback**: More complex setup, often requires specialized hosting like **Vercel**.

### 7. **Partial Hydration**
   - Only hydrates parts of the page (instead of the entire page) to improve performance.
   - Example: Hydrate components at the top of the page first and load other parts later (e.g., lazy loading).
   - Helps reduce the **JavaScript** call stack for complex pages.

### 8. **Islands Architecture**
   - Static HTML for the entire page, with only small interactive "islands" hydrated by JavaScript.
   - Framework: **Astro**.
   - **Advantage**: No JavaScript is shipped to the client if no interactivity is required, even though built with JavaScript frameworks like **React**.

### 9. **Streaming SSR**
   - Renders server-side content concurrently in chunks instead of all at once.
   - Supported by **Next.js 13** with **React server components**.
   - **Advantage**: Faster interactivity, improved user experience.

### 10. **Resumability**
   - Pioneered by the **Qwik** framework.
   - Website and data are serialized into HTML, with JavaScript broken into tiny chunks.
   - **Advantage**: No hydration needed, always delivers static HTML first.
   - JavaScript for interactivity is lazily loaded in the background.




