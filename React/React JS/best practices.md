


## Introduction

This document outlines the best practices to ensure consistency, maintainability, and scalability of the project.

----------

## Coding Standards

-   Follow [Airbnb's JavaScript Style Guide](https://github.com/airbnb/javascript).


----------

## Project Structure

-   Place all components in the `/src/components/` directory.
-   Place all assets under the `src/assets` directory.
-   Use `/src/hooks/` for reusable custom hooks.
-   Use `/src/utils/` for placing all reusable utility functions.
-   Use `/src/contexts/` for placing all `useContext` variables.
-   Maintain a shallow directory structure, avoiding more than two nested levels.

### Feature-Based Organization

-   Group files by feature (e.g., `components/product-details`, `components/user-profile`) rather than file type.
-   Use descriptive names for folders and files (e.g., `ProductDetails.js`, `ProductDetails.css`).
-   Keep related files together (e.g., components, styles, and tests in the same folder).

----------

## File Structure

-   Maintain a proper import structure:
    
    1.  Built-in modules (e.g., `react`)
    2.  External (third-party libraries)
    3.  Internal modules (project-specific components, utilities, etc.)
-   Use functional components (prefer arrow functions) that serve a single purpose and remain pure.
    
-   Avoid using `any` type; include strict typing (TypeScript or PropTypes).
    
-   Use the `useReducer` hook if a component exceeds four `useState` hooks or involves complex state management.
    
-   Use shorthand for boolean props:
    
    ```jsx
    // Instead of this:
    <RegistrationForm hasPadding={true} withError={true} />
    
    // Use this:
    <RegistrationForm hasPadding withError />
    
    ```
    

----------

## Naming Conventions

-   Use `PascalCase` for components, interfaces, type aliases, and file names.
-   Use `camelCase` for variables, arrays, objects, and functions.
-   Use `UPPER_CASE_SNAKE_CASE` for constants.

----------

## Component Design

-   **Functional Components**: Use functional components with Hooks (`useState`, `useEffect`) instead of class components.
-   **Single Responsibility**: Each component should do one thing well.
-   **Small, Reusable Components**: Break down large components into smaller ones for reuse and easier testing.
-   **Controlled Components**: Use controlled components for forms where React state manages the form data.
-   **Avoid Prop Drilling**: Use the Context API or state management libraries (e.g., Redux, Zustand) to avoid passing props down multiple levels.

----------

## State Management

-   Lift state up when needed and avoid unnecessary global state.
-   redux for state management, redux toolkit
-   Always update state immutably to avoid side effects.

----------

## Styling

-   Use CSS Modules or styled-components for scoped, maintainable styling. => emotion lib
-   Follow consistent naming conventions for CSS classes (e.g., BEM).
-   Avoid inline styles to prevent performance issues and maintain consistency.

----------

## Performance Optimization

-   Use `React.memo` for functional components to prevent unnecessary re-renders.
-   Use `useCallback` and `useMemo` to memoize functions and expensive calculations.
-   Implement code splitting using dynamic imports to reduce initial load time.
-   Lazy load components with `React.lazy` and `Suspense`.
-   Use virtualization libraries for rendering large datasets.

----------

## Error Handling

-   Implement error boundaries to catch JavaScript errors and display fallback UIs.

----------

## Type Safety

-   Use TypeScript for type safety in large applications.
-   Use PropTypes for smaller projects to enforce type validation for components.

----------

## Testing

-   Write tests for every new feature or bug fix.
-   Aim for at least 90% test coverage.
-   Use tools like Jest and React Testing Library for unit and integration tests.
- Use playwrite for end to end testing..  
-   Use snapshot testing for ensuring consistent rendering of components.

----------

## Accessibility

-   Use semantic HTML elements (e.g., `<header>`, `<nav>`, `<footer>`).
-   Ensure components are navigable via keyboard.
-   Provide alternative text for images and appropriate labels for form elements.

----------

## Version Control

-   Use feature branches, pull requests, and code reviews to maintain a clean codebase.
-   Follow conventional commit messages (e.g., `feat:`, `fix:`, `chore:`).

----------

## Deployment & CI/CD

-   Use CI/CD pipelines for automated testing and deployment (e.g., GitHub Actions, CircleCI).
-   Manage environment variables with `.env` files, configuring different settings for development and production.

----------

## Security

-   Sanitize inputs and escape dynamic content to prevent XSS attacks.
-   Use CSRF tokens for secure backend interactions.

----------

## Documentation

-   Document components and hooks with clear README files, inline comments, and JSDocs.
-   Use Storybook for documenting UI components and their variations.

----------

## Commit Message Convention

-   Use [Conventional Commits](https://www.conventionalcommits.org/) for clarity:
    -   `feat:` for new features.
    -   `fix:` for bug fixes.
    -   `chore:` for non-functional changes.

- precommit hook , husky.. 

External libs:
- lodash - utilities.. 
- time dayjs
- use js Intl wherever needed 
