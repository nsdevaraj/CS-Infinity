

Here’s a concise version of rendering HTML files and using a view engine in Express.js:

---

### Rendering HTML with Express.js

1. **Setup**:
   - To render HTML files, use the `render` method:
     ```javascript
     res.render('index'); // Renders index file
     ```

2. **Directory Structure**:
   - Create a `views` folder to store your HTML files (e.g., `index.html`).

3. **Error Handling**:
   - If you see "no default engine specified," you need to set up a view engine.

4. **Using EJS as a View Engine**:
   - Install EJS:
     ```bash
     npm install ejs
     ```
   - Set EJS as the view engine:
     ```javascript
     app.set('view engine', 'ejs');
     ```

5. **Create EJS Files**:
   - Rename your HTML file to `index.ejs` and add boilerplate content.

6. **Passing Data to Views**:
   - Use the `render` method’s second parameter to pass data:
     ```javascript
     res.render('index', { text: 'World' });
     ```
   - Access it in EJS with:
     ```ejs
     <%= text %> <!-- Outputs: World -->
     ```

7. **Handling Undefined Variables**:
   - Use `locals` to prevent errors when variables are not defined:
     ```ejs
     <%= locals.text || 'Default' %>
     ```

8. **Organizing Routes**:
   - For large applications, use Express routers to manage routes efficiently:
     ```javascript
     const router = express.Router();
     // Define routes here
     app.use('/api', router); // Integrate router into the main app
     ```

### Summary

This setup allows you to render HTML using EJS, pass data to your views, handle potential undefined variables, and maintain a clean code structure with routers in Express.js.


[[Different View Engines]]







