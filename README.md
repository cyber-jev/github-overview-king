# Automatic Git Commits Script

This script automates the process of adding and committing changes to a Git repository. It appends a specified word to a text file, adds the modified file to the repository, commits the changes, and then pushes them to the remote repository.

## Prerequisites

- Python environment with the `os` and `git` modules installed.

## Requirements

Before using the script, ensure you have the following prerequisites installed:

- Python: The script is written in Python and requires a working Python installation (Python 3.x recommended).
- GitPython: This script uses the GitPython library to interact with Git repositories. You can install it using the following command:

```bash
pip install GitPython
```



## Usage

1. Ensure that you have the necessary Python environment set up.

2. Modify the script variables according to your preferences:

   - `repo_path`: Path to the local repository (current directory).
   - `word`: Word to be added to the text file.
   - `commit_message`: Commit message for each iteration.
   - `file_path`: File path relative to the repository root.
   - `num_iterations`: Number of iterations for the process.

3. Run the script using the following command:

   ```bash
   python script.py
