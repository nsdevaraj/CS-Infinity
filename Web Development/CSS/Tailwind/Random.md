
In Tailwind CSS, you can use the utility class `hidden` to apply `display: none;`. Here's how you would use it:

```html
<div class="hidden">
  This content is hidden.
</div>
```

If you want to control visibility based on screen size, you can use responsive variants. For example:

```html
<div class="hidden md:block">
  This content is hidden on small screens but visible on medium screens and up.
</div>
```

In this example, the content will be hidden on small screens (`hidden`) and displayed as a block on medium screens and larger (`md:block`).




```
<div className="flex flex-wrap gap-6 max-w-[80vw] mx-auto xl:max-w-none">
```


