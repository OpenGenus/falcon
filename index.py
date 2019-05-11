from git import Repo
import os
from pathlib import Path

class Cosmos:
    def clone_repo(self):
        p = Path("./cosmos")
        if p.exists():
            return True
        else:
            gitUrl = "https://github.com/OpenGenus/cosmos.git"
            repoDir = os.path.dirname(os.path.abspath(__file__)) +"/cosmos"

            try:
                Repo.clone_from(gitUrl, repoDir)
            except Exception as e:
                return False
                print(e)
            return True