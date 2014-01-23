from subprocess import *
import os

def read(params=[], options=[], entree=None, sortie=PIPE):
	command = ["cat"]
	if params or entree :
		if params:
			if os.path.isfile(params[0]):
				paramsBash = command+options+params
			else:
				print("File not found")
				return False
		else :
			paramsBash = command+options
		p = Popen(paramsBash, stdin=entree, stdout=sortie)
		p.wait()
		return p
	else:
		return False
