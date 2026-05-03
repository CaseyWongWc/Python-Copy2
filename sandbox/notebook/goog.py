with open("test123.py", "w") as file:
# out: This is a test file.
    file.write('print("This is a test file.")\n')
    # val: 30
    for thing in range(0,5):
        print(thing)
        # out: 0
        # out: 1
        # out: 2
        # out: 3
        # out: 4
import test123
with bash:
    git status
    # out: On branch main
    # out: Your branch is up to date with 'origin/main'.
    # out: 
    # out: Changes not staged for commit:
    # out:   (use "git add <file>..." to update what will be committed)
    # out:   (use "git restore <file>..." to discard changes in working directory)
    # out: 	modified:   ../notebook/goog.py
    # out: 
    # out: no changes added to commit (use "git add" and/or "git commit -a")
    bash push_replit.sh
    # out: 📦 Staging all changes...
    # out: 🔄 Syncing with remote (rebase)...
    # out: ⚠️  Conflict detected — accepting local version of conflicted files...
    # out: 🚀 Pushing to origin/main...
    # out: ✅ Done! Code is live on GitHub/Replit.
    # err: error: cannot pull with rebase: You have unstaged changes.
    # err: error: Please commit or stash them.
    # err: fatal: no rebase in progress
    # err: Everything up-to-date
    .git add
    # err: /bin/sh: 1: .git: not found
    # !err: exit code 127


    
