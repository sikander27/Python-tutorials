import os
import git
from datetime import datetime

# Path to the folder containing all GitHub repositories
GITHUB_FOLDER_PATH = '/Users/sikanderkhan/Documents/Github/personal-repos'

# Default commit message
COMMIT_MESSAGE = f"Auto-commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def commit_and_push(repo_path, commit_message):
    try:
        repo = git.Repo(repo_path)
        if repo.is_dirty(untracked_files=True):
            repo.git.add(A=True)
            repo.index.commit(commit_message)
            origin = repo.remote(name='origin')
            origin.push()
            print(f"Changes committed and pushed for repository: {repo_path}")
        else:
            print(f"No changes to commit for repository: {repo_path}")
    except Exception as e:
        print(f"An error occurred while processing repository {repo_path}: {e}")

def main():
    for root, dirs, files in os.walk(GITHUB_FOLDER_PATH):
        for dir_name in dirs:
            repo_path = os.path.join(root, dir_name)
            if os.path.isdir(os.path.join(repo_path, '.git')):
                commit_and_push(repo_path, COMMIT_MESSAGE)

if __name__ == "__main__":
    main()

