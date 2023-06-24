import git

# Path to the local repository
repo_path = './'

# Word to be added to the text file
word = 'king'

# Commit message
commit_message = 'Added the word "king"'

# File path relative to the repository root
file_path = './who-am-i.txt'

# Absolute path to the text file
abs_file_path = f'{repo_path}/{file_path}'

# Write the word to the text file
with open(abs_file_path, 'a') as file:
    file.write(word)

# Initialize the repository object
repo = git.Repo(repo_path)

# Add the modified file to the repository
repo.index.add([file_path])

# Commit the changes
repo.index.commit(commit_message)

# Push the changes to the remote repository
origin = repo.remote('origin')
origin.push()

