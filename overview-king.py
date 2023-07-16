import os
import git

# Path to the local repository (current directory)
repo_path = os.getcwd()

# Word to be added to the text file
word = ":) "

# Commit message
commit_message = "who am i :)"

# File path relative to the repository root
file_path = "who-am-i.txt"

# Absolute path to the text file
abs_file_path = os.path.join(repo_path, file_path)

# Number of iterations
num_iterations = 20

# Repeat the process specified number of times
for i in range(num_iterations):
    # Write the word to the text file
    with open(abs_file_path, "a") as file:
        file.write(word)

    # Initialize the repository object
    repo = git.Repo(repo_path)

    # Add the modified file to the repository
    repo.index.add([file_path])

    # Commit the changes
    repo.index.commit(commit_message)

    # Push the changes to the remote repository
    origin = repo.remote("origin")
    origin.push()

    # Commit count
    commit_count = "commit" if i + 1 <= 1 else "commits"

    # Display progress
    progress = (i + 1) / num_iterations * 100
    print(f"Progress: {progress:.1f}%  ({i + 1} {commit_count})")

# Finished message
print("Hacking completed. All thanks to cyber-jev")
