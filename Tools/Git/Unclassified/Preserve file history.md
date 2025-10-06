

To **merge branches in Git** while **preserving full history of all files**, including their commits and authorship, you should use Git’s built-in `merge` command **without squashing or rebasing**.

Here’s a step-by-step guide to do it **correctly and safely**:

---

## ✅ **Standard Git Merge (Preserves File History)**

### 🧭 Scenario

You have two branches:

- `main`
    
- `feature-branch`
    

You want to merge `feature-branch` **into** `main` and keep the full commit history.

---

### 🔧 Commands

```bash
# Step 1: Switch to the target branch (e.g., main)
git checkout main

# Step 2: Ensure it's up to date
git pull origin main

# Step 3: Merge the feature branch into main
git merge feature-branch
```

---

### ✅ This:

- Keeps **full commit history** of all files from both branches.
    
- Preserves **authorship**, timestamps, and diff history.
    
- Results in a **merge commit** (unless it's a fast-forward).
    

---

## 🚫 Avoid These if You Want Full History:

|Method|Why Avoid|
|---|---|
|`git merge --squash`|Combines all commits into one — **history is lost** for the branch being merged|
|`git rebase`|Rewrites commit history — can cause confusion, especially in team settings|
|`git cherry-pick`|Only copies selected commits — **does not preserve branch structure or full history**|

---

## 🧠 Bonus: Checking File History After Merge

You can confirm a file’s history remains intact using:

```bash
git log --follow -- path/to/your/file
```

This will show the full history **across renames and merges**.

---

If your branches have diverged significantly, and there are conflicts, Git will prompt you to resolve them manually during the merge.
