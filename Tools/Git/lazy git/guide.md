



# 🧠 **Lazygit Complete Guide**

**Terminal Git made intuitive – fast, focused, and visual.**

---

## 🚀 **Getting Started**

### Install Lazygit:

https://github.com/jesseduffield/lazygit

### Launch Lazygit:

```bash
cd your-repo/
lazygit
```

---

## 🎛️ **Interface & Panel Navigation**

Lazygit is panel-based. Each panel serves a specific Git function.

|Panel Key|Panel Name|Function|
|---|---|---|
|`1`|Status|Summary of changes, current branch|
|`2`|Files|Staged, unstaged, modified files|
|`3`|Branches|Local/remote branch management|
|`4`|Commits|History of current branch|
|`5`|Stash|Manage stashed changes|
|—|Preview|Shows diffs, logs, etc.|

### Navigation Keys:

- **Switch panels**: `←` / `→` or `1`–`5` or `Tab` or `Shift + Tab`
- **Move within panel**: `↑` / `↓` or `j` / `k`
- Move sections of panel: `[` / `]` 
- **Scroll in preview**: `PgUp` / `PgDn`  or Scroll with mouse
- **Quit Lazygit**: `q`
- Search or Filter on that panel : `?`


### Help menu:

- **Help menu for current panel**: `shift + ?`

### Modes :

- to filter mode: `/` 
- `Esc` to search mode back i.e exit
	- `Enter` to more info for hightlight / hovering item


---

## ✅ **Staging and Committing**

### 1. **Stage Files**

- Navigate to the **Files panel** (`2`)
- Highlight file: `↑` / `↓`
- Stage/unstage:
    - `Space`: single file
    - `a`: all files

* stage specific chunk of file -> `Enter` on hightlight file, `Space` to stage and unstage each line, `Tab` to switch between stage and unstage views

### 2. **Commit**

- After staging:
    - Press `c` → opens commit message editor
    - Type your message
    - Press `Enter` to commit


### 3. **Amend Commit**

- Press `A` in Status panel (if there's a previous commit)


---

## 🍒 **Cherry-picking Commits**

Useful for applying a commit from one branch to another.

### Steps:
	
1. Go to **Commits panel** (`4`)
    
2. Select commit → Press `C` (copies it)
    
3. Switch to **Branches panel** (`3`) → select target branch → press `Space` (checkout)
    
4. Return to **Commits panel** → press `V` (cherry-pick/paste commit)
    

> 💡 You can cherry-pick multiple commits by copying several before switching branches.

---

## 🌿 **Branch Management**

5. Go to **Branches panel** (`3`)
6. Use `↑` / `↓` to highlight a branch
	1. Use  shortcuts as needed

| Action        | Shortcut |
| ------------- | -------- |
| Create branch | `n`      |
| Delete branch | `d`      |
| Checkout      | `Space`  |
| Merge branch  | `M`      |
| Fetch/refresh | `f`      |
| Pull          | `P`      |
| Push          | `p`      |




---

## 📥 **Stashing Changes**

### Stash:

- In **Status panel**, press `s`
### Apply stash:

- Go to **Stash panel** (`5`)
- Highlight stash → press `S`
### Delete stash:

- Highlight → press `d`

---

## 💥 **Undo, Reset & Reword**

|Action|Panel|Shortcut|
|---|---|---|
|Undo last commit|Commits|`g`|
|Reword commit|Commits|`r`|
|Hard reset HEAD|Commits|`x`|
|Soft reset HEAD|Commits|`X`|

Use these in the **Commits panel** (`4`) carefully!



Fixing conflict:

* when conflict arises, it shows view conflict or abort
* space - pick hunk, b - pick all hunch, 
* up/down - go through the hunk
* left/right - go through different conflicts


---

## 🔁 **Merge, Rebase & Conflict Resolution**

### Merge a Branch

- In **Branches panel** (`3`)
    
- Highlight target branch → press `m`
    

### Rebase Onto Another Branch

- In **Branches panel** → highlight base branch
    
- Press `r` → rebase current branch onto selected one
    

### Resolve Merge Conflicts

7. Conflicted files appear in **Files panel**
    
8. Select a file → press `Enter` to open diff
    
9. Choose between:
    
    - `e`: Edit file manually
        
    - Use in-diff options to pick `ours` / `theirs` chunks
        
10. After resolving, stage and commit
    

---

## 🧠 **Advanced Tips**

- **Keybindings menu**: Press `?` in any panel to discover all context-aware shortcuts.
    
- **Log / blame / diff**: Use `l`, `b`, `d` in Commits or Files panel for deeper inspection.
    
- **Custom config**: Lazygit supports config overrides via `~/.config/lazygit/config.yml`
    
- **Git Hooks** and **Aliases**: Fully respected—use in tandem with Lazygit.
    

---

## 📚 Summary: Quick Shortcuts

|Action|Key|
|---|---|
|Stage file|`Space`|
|Stage all|`a`|
|Commit|`c`|
|Amend commit|`A`|
|Cherry-pick copy|`c`|
|Cherry-pick paste|`v`|
|Checkout branch|`Space`|
|New branch|`n`|
|Delete branch|`d`|
|Stash changes|`s`|
|Apply stash|`S`|
|Push|`p`|
|Pull|`P`|
|Help (keybindings)|`?`|
|Quit|`q`|

---

## 📎 Resources

- GitHub: [https://github.com/jesseduffield/lazygit](https://github.com/jesseduffield/lazygit)
    
- Full documentation: `?` inside Lazygit or view GitHub README
    
- FreeCodeCamp Guide: [freecodecamp.org/news/lazygit](https://www.freecodecamp.org/news/how-to-use-lazygit-to-improve-your-git-workflow/)
    

---


referred {

https://youtu.be/Ihg37znaiBo?si=z-OiIGMVpZjJBCot

}

