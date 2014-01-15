from subprocess import *

def newDir(params=[]):
	if not params:
		print("Enter a name for the directory.")
		return False

	command = ["mkdir"]
	paramsBash = command+params
	p = call(paramsBash)
	return True