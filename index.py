from git import Repo
import os

gitUrl = "https://github.com/OpenGenus/cosmos.git"
repoDir = os.path.dirname(os.path.abspath(__file__)) +"/cosmos"

try:
    Repo.clone_from(gitUrl, repoDir)
except Exception as e:
    print(e)