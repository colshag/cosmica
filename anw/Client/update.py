# ---------------------------------------------------------------------------
# Cosmica - All rights reserved by NeuroJump Trademark 2018
# update.py
# Written by Chris Lewis
# ---------------------------------------------------------------------------
# This will try to update the code from GitHub play-cosmica repo.
# ---------------------------------------------------------------------------
from selfupdate import update

try:
    update(force=True, check_dev=False, message="", username=None, password=None, verbose=True)
except:
    print 'Error updating from play-cosmica repo on GitHub'