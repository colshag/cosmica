#!/usr/bin/env python3

import inspect
import git
import os

__version__ = "0.1.0"
__author__ = "Broderick Carlin (beeedy)"
__email__= "broderick.carlin@gmail.com"
__license__= "MIT"

global_verbosity = False


def __print(verbose, msg):
	'''
	This is a simple utility function used to help assist in 
	adding debug messages throughout the code. Print messages
	are formated as such:
	<name of calling function>:<line #> :: <msg>
	'''
	if not verbose and not global_verbosity:
		return

	stack = inspect.stack()
	calling_func = stack[1][3]
	line = stack[1][2]
	msg.replace("\n", "\n           ".format(calling_func, line))
	print("{}():{} :: {}".format(calling_func, line, msg))

def __get_calling_file(verbose=False):
	'''
	This function will go through the python call stack and find
	the script that originally called into this file. Returns a 
	tuple where the first element is a string that is the folder
	containing the calling script, and the second element is the
	name of the file name of the calling script. If a file can not
	be found for some reason a LookupError is raised to indicate
	that an external script could not be found.
	'''
	stack = inspect.stack()
	this_file = stack[0][1]
	complete_path = os.path.normpath(this_file)
	return os.path.split(complete_path)
	#for i in range(1, len(stack)):
		#if stack[i][1] != this_file:
			##complete_path = os.path.normpath(os.getcwd() + "/" + stack[i][1])
			#complete_path = os.path.normpath(stack[i][1])
			#__print(verbose, "Module was called from: {}".format(complete_path))
			#return os.path.split(complete_path)

	#__print(verbose, "Module was not called by an external script.")
	#raise LookupError("Module was not called by an external script.")

def __find_repo(verbose=False):
	'''
	This function will go figure out if the calling python script
	is inside a git repo, and if so, return a string that is the 
	location of the base of the git repo. If the script is not, a 
	LookupError is raised to indicate it could not find the repo
	'''
	file_path, file_name = __get_calling_file()
	# walk up the file tree looking for a valid git repo, stop when we hit the base
	while True:
		#if os.path.samefile(os.path.normpath(file_path), os.path.normpath("/")):
		if __samefile(os.path.normpath(file_path), os.path.normpath("/")):
			__print(verbose, "Calling script is not in a valid git repo")
			raise LookupError("Calling script is not in a valid git repo")

		try:
			git.Repo(file_path)
			__print(verbose, "Found root of repo located at: {}".format(os.path.normpath(file_path)))
			return os.path.normpath(file_path)
		except git.exc.InvalidGitRepositoryError:
			file_path = os.path.normpath(file_path + "/..")

def __samefile(file1, file2):
	"""required for python 2.7 - Chris Lewis"""
	try:
		return os.stat(os.path.normpath(file1)) == os.stat(os.path.normpath(file2))
	except:
		return False

def __find_current_branch(repo, verbose=False):
	'''
	Simple function that returns the name of the current branch. 
	If for some reason the function fails to find the current branch
	an IOError is raised to indicate something has gone wrong. 
	'''
	assert type(repo) is git.repo.base.Repo, "Passed in repo needs to be of type 'git.repo.base.Repo'"
	branches = str(repo.git.branch()).splitlines()
	for branch in branches:
		# asterix represents current branch, search for it
		if branch[0] == "*":
			__print(verbose, "Found current branch to be: {}".format(branch[2:]))
			return branch[2:]
	__print(verbose, "Failed to find current branch")
	raise  IOError("Failed to find current branch")

def __is_dev_env(directory, suppress_errors=False, verbose=False):
	'''
	This function will return 'True' if the git repo is setup to 
	be a selfupdate development environment. This indicates that 
	functions that perform destructive file manipulation will be 
	limited in scope as to not cause the script to complicate 
	development efforts when using the selfupdate library. A 
	selfupdate development environment is configured by placeing
	an empty file in the root directory of the repo simply named
	'.devenv'. This file must also be included in the .gitignore
	or a EnvironmentError will be raised. This is to avoid the 
	propogation of the development environment file to the main 
	repo and any other local repositories that would then pull 
	this file down and turn themselves into development 
	environments. This error can be suppressed by setting the 
	argument 'suppress_errors' to 'True' when calling is_dev_env().
	Suppressing this error can cause remote repos that rely on 
	selfupdate to no longer update succesfully without direct
	user input. You have been warned! 
	'''
	directory = os.path.normpath(directory)
	# see if the .devenv file even exists
	if os.path.isfile(directory + "/.devenv"):
		# it exists, so make sure a .gitignore exists and it includes .devenv
		if os.path.isfile(directory + "/.gitignore"):
			with open(directory + "/.gitignore", 'r') as gitignore:
				for line in gitignore.readlines():
					if ".devenv" in line:
						__print(verbose, "Found valid development environment")
						return True
		#raise error here
		__print(verbose, "'.devenv' found but not included in '.gitignore'.")
		if not suppress_errors:
			raise EnvironmentError("'.devenv' found but not included in '.gitignore'.")
	else:
		__print(verbose, "No '.devenv' file found in the root directory of the repo")

	return False

def __get_file_conflicts(repo, verbose=False):
	'''
	Simple function that takes in pointer to the repo
	and returns a list of files that have conflicts with
	the remote repo.
	'''
	assert type(repo) is git.repo.base.Repo, "Passed in repo needs to be of type 'git.repo.base.Repo'"
	diff = str(repo.git.diff("--name-only", "--diff-filter=U")).splitlines
	if len(diff) == 0:
		__print(verbose, "No diff conflicts found")
	else:
		msg = "Found {} conflicts in files:".format(len(diff))
		for conflict in diff:
			msg += "\n  {}".format(conflict)
		__print(verbose, msg)
	return diff

def __get_file_diffs(repo, verbose=False):
	'''
	Simple function that takes in a pointer to the repo
	and returns a list of files that contain changes 
	between the remote and local repo.
	'''
	assert type(repo) is git.repo.base.Repo, "Passed in repo needs to be of type 'git.repo.base.Repo'"
	diff = str(repo.git.diff("--name-only")).splitlines
	if len(diff) == 0:
		__print(verbose, "No diff found")
	else:
		msg = "Found {} diffs in files:".format(len(diff))
		for conflict in diff:
			msg += "\n  {}".format(conflict)
		__print(verbose, msg)
	return diff

def pull(force=False, check_dev=True, verbose=False):
	'''
	This function will attempt to pull any remote changes down to 
	the repository that the calling script is contained in. If 
	there are any file conflicts the pull will fail and the function
	will return. This function is *safe* and does not perform 
	destructive actions on the repo it is being called on. This 
	function returns a tuple containing 2 fields. The first is a
	boolean value that indicates if the pull was successful or not. 
	The second field contains a list of the files that were effected
	by the pull. If the pull was successful, this is the files that 
	were updated by the pull action. If the pull was unsuccesful, 
	this list contains the files that have conflicts and stopped the
	pull. All files listed in the case of a success or failure are 
	referanced relative to the base of the repository. This function 
	attempts to capture git errors but it is entirely possible that 
	it does not handle a git error correctly in which case it will be 
	raised again to be potentially handled higher up. 
	'''
	repo_path = __find_repo()
	repo = git.Repo(repo_path)
	if not force:
		try:
			resp = str(repo.git.pull()).splitlines()
			if resp[0] == "Already up-to-date.":
				__print(verbose, "Repository is already up to date.")
				return (False, [])

			files = [a.split("|")[0][1:-1] for a in resp[2:-1]]
			__print(verbose, "Files that were updated:" + "\n  ".join(files))
			return (True, files)

		except git.exc.GitCommandError as err:
			err_list = str(err).splitlines()

			# this is a poor and rudamentary way to tell if there was a specific error TODO: fix
			if err_list[3] == "  stderr: 'error: Your local changes to the following files would be overwritten by merge:":
				files = [a[1:] for a in err_list[4:-2]]
				__print("Pull failed. Files with conflicts:" + "\n  ".join(files))
				return (False, files)
			# we got an error we didn't expect, pass it back up
			raise

		return (True, [])
	else:
		if check_dev and __is_dev_env(repo_path):
			__print(verbose, "Detected development environment. Aborting hard pull")
			return (False, [])
		repo_path = __find_repo()
		repo = git.Repo(repo_path)
		branch = __find_current_branch(repo)

		# record the diff, these will all replaced
		##diffs = __get_file_diffs(repo)

		##if len(diffs) == 0:
			##return (False, [])

		# fetch all
		fetch_resp = str(repo.git.fetch("--all"))
		__print(verbose, "Fetched any and all changes with response: {}".format(fetch_resp))
		# reset
		reset_resp = str(repo.git.reset("--hard", "origin/{}".format(branch)))
		__print(verbose, "Completed hard pull with response: {}".format(reset_resp))
		# clean
		clean_resp = str(repo.git.clean("-f"))
		__print(verbose, "Completed clean with response: {}".format(clean_resp))
		##return (True, diffs)
		return (True, [])

def update(force=False, check_dev=True, message="python selfupdate", username=None, password=None, verbose=False):
	'''
	The single function that can be called to automagically
	update the repo in which the calling file is located.
	The 'force' paramter will cause the module to force do a
	pull. This is a destructive action that can
	cause loss of local data. 'check_dev' when set to True 
	will not allow any destructive action to take place IFF 
	the calling script is in a selfupdate dev environment. 
	'''
	if force:
		pull(force=force, check_dev=check_dev, verbose=verbose)
		__print(verbose, "Pulled any possible remote changes")
	else:
		pull(force=force, check_dev=check_dev, verbose=verbose)
		__print(verbose, "Pulled any possible remote changes")


if __name__ == '__main__':
	try:
		update(force=True, check_dev=False, message="", username=None, password=None, verbose=True)
	except:
		print 'Error updating from play-cosmica repo on GitHub'