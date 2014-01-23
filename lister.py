from subprocess import *
import os

def ls(params=[], options=[], entree="stdin", sortie="stdout"):
	command = ["ls"]
	if not params:
		params = [os.getcwd()]	
	paramsBash = command+options+params
	p = Popen(paramsBash, stdout=sortie, stdin=entree)
	p.wait()
	return p