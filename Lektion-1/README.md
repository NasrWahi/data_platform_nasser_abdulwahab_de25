# Terminal & Git Essentials

A quick reference for everyday terminal navigation and Git usage.

## Terminal Navigation

```bash
pwd                    # Show current directory
ls                     # List files
ls -a                  # List all files (including hidden)
cd folder/             # Move into a folder
cd ..                  # Move up one level
cd ~                   # Go to home directory

grep "text" file.txt   # Search for text in a file
grep -i "text" file.txt # Case-insensitive search
grep -r "text" .       # Recursive search in current directory
ls | grep ".md"        # Filter command output

touch file.txt         # Create empty file
touch index.html style.css # Create multiple files