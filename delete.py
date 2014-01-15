from subprocess import *
import os

def delete(params=[]):
	if os.path.isdir(params[0]):
		command = ["rmdir"]
	elif os.path.isfile(params[0]):
		command = ["rm"]
	else:
		print("File or directory '"+params[0]+"' not found")
		return False
	paramsBash = command+params
	call(paramsBash)
	return True