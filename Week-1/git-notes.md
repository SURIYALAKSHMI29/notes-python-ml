# **BASIC COMMANDS**

- **git clone** – used to clone an existing remote repo in local device  
- **git add** – used to link existing local repo to remote  
- **git add** – stage modified files in local repo  
- **git diff** – compares the working dir and staged area  
- **git diff --staged** or **git diff --cached** – compares staged area and HEAD  
- **git diff** – compares working dir and HEAD (both staged and unstaged)  
- **git commit** – creates snapshot of the current state (like checkpoint), records time, commit msg, who committed that and HEAD moves to this commit  
- **git status** – shows modified, staged, untracked files name  

---

### **HEAD**

- A pointer, indicates your current working location in the repository (points to latest commit on that branch).  

---

### **Branches**

- **git branch** – list all the branches  
- **git branch branchName** – creates new branch  
- **git branch -d branchName** – deletes a branch (-D → force deletion)  
- **git branch -m branchName** – renames a branch  
- **git checkout branchName** or **git switch branchName (new)** – switches branch  

---

### **Stash**

- **git stash** – saves the current local unsaved or uncommitted changes  
  - used when local and remote are not same, so that we can pull after stashing  
- **git stash pop** – used to reapply the uncommitted changes after pulling  

---

### **Pull / Push**

- **git pull** – pull changes from remote to local (**git fetch + git merge**)  
- **git push** – push changes from local to remote  

---

### **Fetch**

- **git fetch** – get updates from remote repo, doesn’t modify the working local dir  
  - Reviewing changes before merging  

---

### **Merge / Rebase**

- **git merge branchName** – merges the changes in branchName into current working branch  
  - Doesn’t change commit history, just includes a new merge commit  
  - Just makes references to the commits  
- **git rebase branchName** – used to replay  
  - Modifies commit history (linear commit history)  
  - Goes back to common commit of specified branch and current branch (like rollback), then reapplies the current branch commits on top of it  
  - Copies the commits again  

---

### **Cherry-pick**

- **git cherry-pick commit-hashCode** – apply specific commit from another branch  
  - Use case: when fixing specific bugs in all branches or versions  

---

### **Logs**

- **git log** – return commit history  
- **git reflog** – reference log; return history of all commits and actions (stash, rebase, ..)  

---

### **Reset / Revert**

- **git reset** – moves the HEAD pointer, modifies the commit history  
- **git reset --soft HEAD~1** – rollback to prev state before commit, soft → just undo a commit, doesn’t undo the changes made in local repo  
- **git reset --hard HEAD~1** – rollback to prev state, force rollback, no changes will be present  
- **git revert** – undoes the last commit, by making a new revert commit; preserving commit history  

---

### **Tags**

- **git tag** – list all tags  
- **git tag tagName** – bookmarking; create references to specific commit  
- **git tag -a tagName -m msg** – annotates tag; saves metadata (commit msg, time, author)  

---

### **Deleting a Branch**

- **git branch -d branchName** – deleting a branch locally  
- **git push origin --delete branchName** – deleting a remote branch  

---

# **CONCEPTS**

### **Repository**

- Local repo, Remote repo  
- Local repo: `.git` folder, has local commit history and snapshots  
  - **Staging area** – a temporary space where changes are prepared before committing  
- Remote repo: lives on a server  

---

### **Branch**

- Used to work separately, isolate works  

---

### **Remote Repo**

- Repo hosted on server  
- `git remote add <name> <remote-URL>`  
- Multiple remote repos like origin(main), backup, ..  
- Can have different branches or same  

**Tracking Branches**  

Each remote has its remote-tracking branches in your local `.git` folder:  

Example after adding remotes:  

`refs/remotes/origin/master

refs/remotes/origin/feature-1

refs/remotes/backup/master

refs/remotes/backup/feature-1`


- `refs/remotes/<remote>/<branch>` is how Git keeps track of what the remote repo looks like  
- These are read-only in local repo — you cannot commit to them directly  

---

### **Deleting Repo**

1. Local: deleted → Remote: still exists → Fetch: recreates local reference if needed  
2. Remote: deleted → Local: still exists → Push: recreates branch on remote  

---

### **PR / MR**

- **PR** – Pull Request; term used in GitHub  
- **MR** – Merge Request; term used in GitLab  
- **Working**: when we need approval or opinion from others (collaborators), MR is made to merge a branch with main  
  - Useful when we don’t have direct access, and need confirmation before merging  

---

### **Merges**

- **Fast forward merge**: No new merge commit is created  
  - Happens when the target branch has no new commits since the branch was created. Git simply moves the target branch pointer forward to include the changes  
- **Squashed merge**: Combines all commits from a branch into a single commit on the target branch  
  - Maintains the code changes in order, but history is simplified  

**Case:** What happens when you try to merge branch source into branch target, but target is ahead?  

- Example: src = feature1, target = main  
- “Target is ahead” → main already has all commits that feature1 has (and maybe more)  
- In that case, no new merge commit is created  

---

### **Git vs GitHub / GitLab**

- **Git** – version control system  
  - A tool installed on the local computer to track changes in the code  
  - Commits are stored in `.git` locally  
- **GitHub / GitLab** – a cloud platform that hosts Git repositories online  
  - Provides web interface and APIs for managing repositories  
