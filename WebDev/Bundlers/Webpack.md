
#### 1. **Webpack**
   - **Primary Function**: Webpack creates a dependency graph based on your code and dependencies, outputting a single or optimized set of JavaScript bundles.
   - **Getting Started**:
     1. **Entry Point**: Define an entry file (often `index.js`) for Webpack to begin bundling.
     2. **Output Configuration**: Specify the name and location of the bundle file.
     3. **Using npm**: Install dependencies and run `webpack` commands to bundle files.
   - **Configuring Webpack**:
     - Webpack supports configuration files where you can define entry points, output file names, rules for loaders, and plugins.
     - Example:
       ```javascript
       // webpack.config.js
       module.exports = {
         entry: './src/index.js',
         output: {
           filename: 'bundle.js',
           path: __dirname + '/dist',
         },
         module: {
           rules: [
             { test: /\.css$/, use: ['style-loader', 'css-loader'] },
           ],
         },
         plugins: [new HtmlWebpackPlugin({ template: './src/index.html' })],
       };
       ```
   - **Loaders and Plugins**:
     - **Loaders** transform non-JS files (like CSS, SASS) into modules Webpack can bundle.
     - **Plugins** handle advanced tasks, like bundle analysis and optimization.
   - **Development Server**:
     - Webpack Dev Server watches files for changes and serves them locally, enabling fast, iterative development without constant rebuilds.


### Setting Up Webpack: Step-by-Step Guide
#### Step 1: Initialize Project
   ```bash
   npm init -y
   ```
#### Step 2: Install Webpack and Dependencies
   ```bash
   npm install webpack webpack-cli --save-dev
   ```
#### Step 3: Define Entry Point (`src/index.js`)
   - Import dependencies like lodash and test that the setup works by logging output to the console.

#### Step 4: Configure Loaders and Plugins
   - Add loaders to process CSS and SASS files.
   - Use plugins to analyze and optimize the bundle size.

#### Step 5: Build and Serve
   - Run `npm run build` to generate production-ready bundles.
   - Use Webpack Dev Server for development by configuring it in `webpack.config.js`.

### Advanced Webpack Features

1. **Code Splitting**: Enables faster load times by splitting bundles for different routes or pages.
2. **Tree Shaking**: Removes unused code, especially helpful with libraries like lodash.
3. **Plugins**:
   - **Webpack Bundle Analyzer**: Visualize bundle content and optimize based on dependency size.
   - **Hot Module Replacement**: Refreshes modules on changes without reloading the whole page.


