# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# update.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This updates COSMICA from the play-cosmica GitHub repo
# ---------------------------------------------------------------------------
import git
import os

if __name__ == '__main__':
	repo = git.Repo(os.getcwd(), search_parent_directories=True)
	# fetch all
	fetch_resp = str(repo.git.fetch("--all"))
	print("Fetched any and all changes with response: {}".format(fetch_resp))
	