

To delete a Git branch, you can do it either **locally** or **remotely**, depending on where the branch exists.

---

## 🧹 **Delete a Local Branch**

### ✅ Syntax:

```bash
git branch -d branch-name
```

### 🧨 Force delete (if not merged):

```bash
git branch -D branch-name
```

### ⚠️ Notes:

- `-d` (safe): Deletes only if branch is fully merged into current branch.
    
- `-D` (force): Deletes even if not merged (⚠️ use with caution).
    

---

## 🌐 **Delete a Remote Branch**

### ✅ Syntax:

```bash
git push origin --delete branch-name
```

> 🔁 This tells the remote (e.g. GitHub) to remove the branch.

---

## 📘 Examples

### Delete local branch `feature/login`:

```bash
git branch -d feature/login
```

### Force delete local branch:

```bash
git branch -D feature/login
```

### Delete the same branch from remote:

```bash
git push origin --delete feature/login
```

---

### 🔍 List branches:

```bash
git branch          # local branches
git branch -r       # remote branches
git branch -a       # all (local + remote)
```

Let me know if you want to delete multiple branches at once, or clean up stale remote-tracking branches!



To **delete a branch both locally and remotely**, follow these two steps:

---

## ✅ 1. Delete the Local Branch

```bash
git branch -d branch-name
```

- Use `-d` to delete **only if the branch is merged**.
    
- Use `-D` to force delete **even if unmerged**.
    

🔧 Example:

```bash
git branch -d feature/login
```

or (force delete):

```bash
git branch -D feature/login
```

---

## ✅ 2. Delete the Remote Branch

```bash
git push origin --delete branch-name
```

🔧 Example:

```bash
git push origin --delete feature/login
```

---

### 📌 Summary

|Task|Command|
|---|---|
|Delete local branch|`git branch -d branch-name`|
|Force delete local|`git branch -D branch-name`|
|Delete remote branch|`git push origin --delete branch-name`|

---

### ✅ Optional: Clean up stale remote branches

After deleting remote branches, clean up local tracking references:

```bash
git fetch -p
```

> `-p` stands for “prune” — it removes deleted remote branches from your local metadata.

---

Let me know if you're working in a team setting or using GitHub UI — you can also delete remote branches from the GitHub web interface.


