from subprocess import *

def newDir(params=[], options=[], entree=None, sortie=PIPE):
	if not params:
		print("Enter a name for the directory.")
		return False

	command = ["mkdir"]
	paramsBash = command+options+params
	p = Popen(paramsBash, stdin=entree, stdout=sortie)
	p.wait()
	return p