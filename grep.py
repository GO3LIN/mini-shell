from subprocess import *
import os

def grep(params=[], options=[], entree="stdin", sortie="stdout"):
	command = ["grep"]
	if not params:
		params = []	
	paramsBash = command+options+params
	p = Popen(paramsBash, stdout=sortie, stdin=entree)
	p.wait()
	return p