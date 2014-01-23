from subprocess import *

def newFile(params=[], options=[], entree=None, sortie=PIPE):
	if not params:
		print("Enter a name for the file.")
		return False
	command = ["touch"]
	paramsBash = command+options+params
	p = Popen(paramsBash, stdin=entree, stdout=sortie)
	p.wait()
	return p