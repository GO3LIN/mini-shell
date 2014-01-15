from subprocess import *

def newFile(params=[]):
	if not params:
		print("Enter a name for the file.")
		return False
	command = ["touch"]
	paramsBash = command+params
	p = call(paramsBash)
	return True