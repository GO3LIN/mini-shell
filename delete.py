from subprocess import *
import os

def delete(params=[], options=[], entree=None, sortie=PIPE):
	if os.path.isdir(params[0]):
		command = ["rmdir"]
	elif os.path.isfile(params[0]):
		command = ["rm"]
	else:
		print("File or directory '"+params[0]+"' not found")
		return False
	paramsBash = command+options+params
	p = Popen(paramsBash, stdin=entree, stdout=sortie)
	p.wait()
	return p