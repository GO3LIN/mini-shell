from subprocess import *
import os

def read(params=[]):
	command = ["cat"]
	if os.path.isfile(params[0]):
		paramsBash = command+params
		p = call(paramsBash)
		print("")
	else:
		print("File not found")
		return False
	return True