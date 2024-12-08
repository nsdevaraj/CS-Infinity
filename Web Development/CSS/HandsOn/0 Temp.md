
---

---

---

### **8. Overlap Two Divs**

**Question:** Position one div overlapping another.  
**Answer:**

```css
.container {
  position: relative;
  width: 300px;
  height: 300px;
  background: lightgray;
}
.overlay {
  position: absolute;
  top: 50px;
  left: 50px;
  width: 200px;
  height: 200px;
  background: rgba(0, 0, 0, 0.5);
}
```

---

### **9. Responsive Text Size**

**Question:** Make text size responsive.  
**Answer:**

```css
.responsive-text {
  font-size: clamp(16px, 2vw, 24px); /* Min 16px, Max 24px */
}
```

---

### **10. Sticky Footer**

**Question:** How do you create a sticky footer?  
**Answer:**

```css
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  margin: 0;
}
.main-content {
  flex: 1;
}
.footer {
  background: lightgray;
  padding: 10px;
  text-align: center;
}
```


