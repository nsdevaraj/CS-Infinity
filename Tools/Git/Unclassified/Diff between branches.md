

To **see the differences between two branches in Git**, use the `git diff` command. Here are the most useful ways to do it:

---

## 🔍 Basic Syntax

```bash
git diff branch1..branch2
```

This shows the changes in `branch2` **that are not in** `branch1`.

---

## 📘 Examples

### 1. Show what’s different in `feature-branch` compared to `main`:

```bash
git diff main..feature-branch
```

> 🔁 This shows what would change if you merged `feature-branch` into `main`.

---

### 2. Compare both ways (symmetric diff):

```bash
git diff branch1...branch2
```

> `...` (triple dots) compares both branches from their **common ancestor**, useful when both branches have diverged.

---

### 3. Just show file names that differ (not full diffs):

```bash
git diff --name-only main..feature-branch
```

---

### 4. See commits that are in `feature-branch` but not in `main`:

```bash
git log main..feature-branch
```

---

### 5. View changes for a specific file:

```bash
git diff main..feature-branch -- path/to/file.js
```

---

## 🧠 Tip: Use a GUI Tool

- VS Code: `gitlens` or built-in Git tools
    
- `gitk`:
    
    ```bash
    gitk main feature-branch
    ```
    

---

