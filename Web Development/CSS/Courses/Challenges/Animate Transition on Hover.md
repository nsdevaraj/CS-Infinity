

put transition for element's property and change that property on hover.. 


```css
.post p .spoiler {
  cursor: pointer;
  background-color: black; 
  transition: background-color 0.5s ease;
}

.post p .spoiler:hover {
  background-color: white; 
}
```



```css
.spoiler {
  background: var(--spoiler-color);
  color: var(--spoiler-color);
  transition: all .5s ease-in;
}

.spoiler:hover {
  background: initial;
  color: initial;
}

```



referred {

https://scrimba.com/css-challenges-c02p/~01

}

