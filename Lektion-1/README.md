# Terminal & Git Essentials

- A quick reference for everyday terminal navigation and Git usage.

# Terminal Navigation

pwd            # Show current directory
ls             # List files
ls -a          # List all files (including hidden)
cd folder/     # Move into a folder
cd ..          # Move up one level
cd ~           # Go to home directory

grep "text" file.txt          # Search for text in a file
grep -i "text" file.txt       # Case-insensitive search
grep -r "text" .              # Recursive search in current directory
ls | grep ".md"               # Filter command output

touch file.txt                # Create empty file
touch index.html style.css    # Create multiple files

git status                    # Show working tree status
git ls-files                  # List tracked files
git ls-files -m               # List modified tracked files
git ls-files --others         # List untracked files

git branch                    # List local branches
git branch -r                 # List remote branches
git checkout branch-name      # Switch branch
git checkout -b new-branch    # Create & switch branch

git log --oneline --graph --all    # Commit history graph
git shortlog -sn                   # Commits per author
git diff --stat                    # File change statistics
git count-objects -vH              # Repository size info
git rev-list --count HEAD          # Total commits on branch