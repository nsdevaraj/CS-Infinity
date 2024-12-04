
React has three core phases in its component lifecycle:

1. **Mounting Phase**
    
    - This is when a component is being created and inserted into the DOM for the first time.
    - Key methods/hooks:
        - **Constructor**: Initializes the component state.
        - **`getDerivedStateFromProps`** (Static Method): Allows updating the state based on initial props.
        - **`render`**: Outputs the JSX to be rendered in the DOM.
        - **`componentDidMount`**: Invoked after the component is mounted in the DOM, typically used for API calls or subscriptions.
2. **Updating Phase**
    
    - This phase occurs when the component is being re-rendered due to changes in props, state, or context.
    - Key methods/hooks:
        - **`getDerivedStateFromProps`** (Static Method): Updates state based on prop changes.
        - **`shouldComponentUpdate`**: Determines whether the component should re-render.
        - **`render`**: Renders the updated JSX.
        - **`getSnapshotBeforeUpdate`**: Captures some state (e.g., DOM position) before updates are applied.
        - **`componentDidUpdate`**: Invoked after the updates are reflected in the DOM.
3. **Unmounting Phase**
    
    - This phase occurs when the component is being removed from the DOM.
    - Key method:
        - **`componentWillUnmount`**: Cleanup method used to unsubscribe, cancel timers, or clean resources.

### With React Hooks

In functional components, hooks like `useEffect` replace most of these lifecycle methods:

- **Mounting**: Use `useEffect` with an empty dependency array (`[]`).
- **Updating**: Use `useEffect` with specific dependencies.
- **Unmounting**: Return a cleanup function from `useEffect`.

This functional approach simplifies component lifecycle management in React.
