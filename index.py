from git import Repo
import os
from pathlib import Path
import argparse


class Cosmos:
    def __init__(self, repo_url="https://github.com/OpenGenus/cosmos.git"):
        self.git_url = repo_url
        self.directory = "/" + self.git_url.split("/")[-1].split(".")[0]
        self.repo_dir = os.path.dirname(os.path.abspath(__file__)) + self.directory

    def clone_repo(self):
        p = Path(self.directory)
        if p.exists():
            return True
        else:
            try:
                Repo.clone_from(self.git_url, self.repo_dir)
            except Exception as e:
                return False
                print(e)
            return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clone any git repo")
    parser.add_argument(
        "-c",
        "--clone",
        help="Repo to be cloned",
        default="https://github.com/OpenGenus/cosmos.git",
    )
    results = parser.parse_args()
    choice = results.clone
    cloner = Cosmos(choice)
    cloner.clone_repo()
