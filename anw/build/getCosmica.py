from git import Repo
import os

Repo.clone_from("http://github.com/colshag/play-cosmica.git", 'play-cosmica', quiet=True)
