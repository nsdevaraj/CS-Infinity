

### **49. Write a function to check if two binary trees are identical.**

#### **Answer:**

```javascript
function areIdenticalTrees(tree1, tree2) {
  if (!tree1 && !tree2) return true;
  if (!tree1 || !tree2 || tree1.value !== tree2.value) return false;
  return areIdenticalTrees(tree1.left, tree2.left) && areIdenticalTrees(tree1.right, tree2.right);
}
```


