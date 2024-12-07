

To create **curved borders** (rounded corners) in a `div` (or any other HTML element) using CSS, you use the `border-radius` property. This property allows you to set rounded corners for an element, which can be applied to all corners or individually to each corner.

### Basic Syntax:

```css
div {
  border-radius: [value];
}
```

### Value of `border-radius`:

- You can specify a **length** (e.g., `10px`, `2em`, `50%`) or a **percentage** (e.g., `50%`).
- **`px` or `em`** creates a fixed pixel or relative radius.
- **`%`** makes the radius relative to the size of the element, and can be used to create perfect circles.

### Example 1: **Uniform Curved Corners**

This will round all four corners equally.

```css
div {
  width: 200px;
  height: 100px;
  background-color: #3498db;
  border-radius: 15px; /* Applies rounded corners with a radius of 15px */
}
```

This will create a `div` with all four corners rounded by 15px.

### Example 2: **Elliptical (Non-Uniform) Curves**

You can use different values for the horizontal and vertical radius to create elliptical corners.

```css
div {
  width: 200px;
  height: 100px;
  background-color: #3498db;
  border-radius: 30px 15px; /* Horizontal radius of 30px and vertical radius of 15px */
}
```

- **`border-radius: 30px 15px;`** means the top-left and bottom-right corners will have a horizontal radius of `30px` and a vertical radius of `15px`.

### Example 3: **Curved Only Specific Corners**

You can also round individual corners by specifying four values for the `border-radius` property.

#### Syntax for individual corners:

```css
border-radius: [top-left] [top-right] [bottom-right] [bottom-left];
```

#### Example 4: **Different Radius for Each Corner**

```css
div {
  width: 200px;
  height: 100px;
  background-color: #3498db;
  border-radius: 20px 40px 60px 80px; /* Different radius for each corner */
}
```

- **`20px`** for top-left corner.
- **`40px`** for top-right corner.
- **`60px`** for bottom-right corner.
- **`80px`** for bottom-left corner.

### Example 5: **Creating a Circle**

If you make the width and height equal and set `border-radius` to 50%, you'll get a circle.

```css
div {
  width: 100px;
  height: 100px;
  background-color: #3498db;
  border-radius: 50%; /* Turns the square div into a circle */
}
```

This will turn the `div` into a **circle** because the `border-radius` is 50% of the width and height.

### Example 6: **Creating a Capsule (Ellipse)**

If you set a high `border-radius` on a rectangular element with equal width and height, you can create a capsule shape.

```css
div {
  width: 300px;
  height: 50px;
  background-color: #3498db;
  border-radius: 25px; /* Curves the corners to make it look like a capsule */
}
```

This will create a **capsule shape** with rounded ends.

---

### Conclusion

- **Uniform Rounded Corners**: `border-radius: 15px;`
- **Elliptical Corners**: `border-radius: 30px 15px;`
- **Different Radius for Each Corner**: `border-radius: 20px 40px 60px 80px;`
- **Perfect Circle**: `border-radius: 50%;` (with equal width and height)

By adjusting the `border-radius`, you can create various curved border effects for any element, from subtle rounded corners to full circles or capsules.