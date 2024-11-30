

  
  
• 2011 - FB - dynamic and interactive UIs  
• React library vs other frameworks like Angular, Vue  
• DOM managing vannila js - components based - react maintain things in virtual DOM & update original DOM in efficient manner  
• top component have inner component - similar to DOM tree like hierarchy structure  
*each component build individually and work individually... To make this sync, we make parent children hierarch  
  
  
  
• initial setup - create react app / vite ( faster & smaller bundle size)  
• package json - scripts and dependencies  
• index.html - entry point - main component linkage - link main.tsx in which App component is rendered using react dom create Root...  
• ts for plain util / service code file, tsx for react components  
  
  
• 2 ways of creating components - class and function ( latest, popular, widely adopted)  
• function component name - Pascal Casing, other things Camel case  
• jsx - Javascript XML - seems like writing html in js, but not correct, pure js that creating DOM elements - use [babeljs.io](http://babeljs.io) to see original converted code  
• jsx - give greater dynamicity - check condition and return the this or that or dynamic text content  
  
*tags can have open & close tags, or with sf closing as single tag  
  
• export default - for exporting component  
  
• react takes component tree & builds js datastucture called react DOM - light weight in memory representation - each component is basically virtual dom element & everytime changes happen it check with old virtual dom and new virtual dom & find changed nodes and only refresh that in actual dom- these things done by companion library called react-dom( instead of react dom, we can use react native for mobile & desktop app development)  
  
  
• library vs framework - specific functionality vs set of tools & guideline to build some software - tool vs toolset  
  
  
• jsx - single DOM component return - empty tags <></> or <Fragment > </Fragment >§i.e return one element  
  
*in jsx - we render html element or other components, but not js expression directly... We have to wrap js code in curly braces  
  
  
• css attributes of kebab-case converted into camelCase and just some twitches like class is called className... prop for jsx elements  
  
  
*key attribute for each similar siblings - react to render it efficiently, not use indices since amy change in list changes all indices so rerender all. Siblings  
  
  
*conditional rendering - enables easy way of rendering things conditionally  
  
• common technic - condition && <h1>  
  
• cost vs let - pure func  
  
  
*each html element / onClick ( e) - e is DOM event  
  
- get details like position ( client x and y) , type event ( click or dbclick), target ( from element className)  
  
  
• callback func - don't put braces - onClick = { onClickFun}  
  
  
• prop - parent passing things ( with this help components made reusable ), should not valid to update prop  
• state - current component managing things, valid to update by hook  
  
*any time prop or state change - react rerender  
  
  
*prop - callbackFunc, variables or even child element itself i.e ReactNode  
  
• react dev tools - extension specifically for react  
- see component tree easily  
  
  
  
  
Hooks: - function gives super power things react  
  
Note: use only in top level of functional component, not work inside function or loops etc  
. (expect custom hooks)  
  
  
• useState - handle reactivity data - state variable to maintain component rerenders  
  
getter, setter = ( default)  
  
  
• useEffect - component life cycle things managed in it...  
  
didMount - compount first time rendered  
didUpdate - updated for some reason  
willUnmount - just before unmounted  
  
  
without dependency - rerender on - mount / state  
is updated  
  
empty dependency - rerender on mount  
List of deps ( state or props) - rerender if any of dependencies changes  
  
return callback func in useEffect - call it when unmount  
  
  
• use Context - things shared data without passing as prop - to reduce prop trilling  
  
  
in top level, create Context and put provider in return with values...  
  
In child renderer - get those values from use Content hook or context.consumer  
  
context updates - context using component rerenders  
  
  
useRef - maintain reference of things , but not rerenders like state variables  
  
Most usecase - grab html element from DOM  
  
  
  
useReducer : like state, but while directly updating given value, it goes to reducer function amd update states  
  
[ state, dispatch] = ( updateFunc, default)  
  
updateFunc ( state, argsPassWhileCalling)  
  
  
Usage : when logics are complex  
  
  
useMemo - cache results of function call - optimise computation for improving Performances  
, so only use for expensive operations - memoize return values..  
  
cost getCount = useMemo ( () => do something, [deps])  
  
  
  
useCallback - memoize entire func ( not only return value)  
  
Creating a func in parent and passing to children as callback, when parent are-renderer, child passing func recreated and which makes rerenders os child, which prevented by this...  
  
To be continued :...  
  
  
  
  
Extra :  
  
Swallow copy vs deep copy  
100 concepts in js  
  
  
  
[https://www.linkedin.com/posts/rajatgajbhiye_dont-overwhelm-to-learn-reactjs-reactjs-activity-7201076470310436865-zGHb?utm_source=share&utm_medium=member_android](https://www.linkedin.com/posts/rajatgajbhiye_dont-overwhelm-to-learn-reactjs-reactjs-activity-7201076470310436865-zGHb?utm_source=share&utm_medium=member_android)

