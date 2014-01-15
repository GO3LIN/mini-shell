from subprocess import *

def ls(params=[]):
	command = ["ls"]
	paramsBash = command+params
	p = call(paramsBash)
	return True