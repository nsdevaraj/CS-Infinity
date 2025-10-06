



```bash
sudo git pull origin main
```

---

### ⚠️ Additional Notes:

1. **Avoid using `sudo` with git unless absolutely necessary**  
    Git rarely needs elevated privileges. Running it with `sudo` can cause **permissions issues** in your local repo (e.g., files being owned by root). Try without `sudo` first:
    
    ```bash
    git pull origin main
    ```
    
2. **If you’re prompted for a password**, and you're using HTTPS instead of SSH, Git is likely asking for your GitHub/GitLab credentials.  
    Consider switching to **SSH** for better authentication (no need to type password every time):
    
    - [GitHub SSH setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
        
3. **If it still fails after correcting the typo**, check that:
    
    - You have the correct remote set up:
        
        ```bash
        git remote -v
        ```
        
        You should see something like:
        
        ```
        origin  git@github.com:your-user/repo.git (fetch)
        origin  git@github.com:your-user/repo.git (push)
        ```
        
    - If `origin` is missing, you can re-add it:
        
        ```bash
        git remote add origin git@github.com:your-user/repo.git
        ```
        

---

### ✅ Final (Recommended) Command:

```bash
git pull origin main
```



--

Got it! Here’s a **crisp, generic workflow** to:

- Merge a feature (or any) branch into main
    
- Delete local branch
    
- Delete remote branch (if exists)
    

---

# 🔥 Generic Git Workflow: Merge + Delete Branch

---

### 1. **Fetch latest from remote**

```bash
git fetch origin
```

---

### 2. **Checkout target branch (e.g., main)**

```bash
git checkout main
```

---

### 3. **Merge source branch into target**

```bash
git merge branch-name
```

- This preserves **full commit history**
    
- Resolve conflicts if any
    

---

### 4. **Push merged changes to remote**

```bash
git push origin main
```

---

### 5. **Delete local branch**

```bash
git branch -d branch-name
```

- Use `-D` to force delete if needed
    

---

### 6. **Delete remote branch**

```bash
git push origin --delete branch-name
```

- If you get `remote ref does not exist`, the remote branch might have been already deleted or never existed
    

---

### 7. **Clean up stale remote-tracking branches (optional)**

```bash
git fetch -p
```

---

# 📋 Summary Table

|Step|Command|Notes|
|---|---|---|
|Fetch latest branches|`git fetch origin`|Sync remote branch info|
|Switch to target branch|`git checkout main`|Usually main or develop|
|Merge source branch|`git merge branch-name`|Preserves history|
|Push merged changes|`git push origin main`|Update remote target branch|
|Delete local branch|`git branch -d branch-name`|Safe delete (merged only)|
|Force delete local branch|`git branch -D branch-name`|Use if branch not merged|
|Delete remote branch|`git push origin --delete branch-name`|Remove from remote repo|
|Prune remote branches|`git fetch -p`|Remove deleted remote refs|

---

# ⚠️ Notes:

- Avoid using `sudo` for Git commands unless you have permission issues.
    
- Always double-check branch names before deleting.
    
- If remote branch delete gives error, check with:
    
    ```bash
    git branch -r
    ```
    
- Merge commits preserve the full commit history of merged branches.
    

---

