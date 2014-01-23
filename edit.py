from subprocess import *
import os

def edit(params=[], options=[], entree=None, sortie=PIPE):
	if not params:
		print("Enter a name for the file.")
		return False
	if os.path.isfile(params[0]):
		command = ["nano"]
		paramsBash = command+options+params
		p = Popen(paramsBash)
		p.wait()
		return p
	else:
		print("Fichier "+params[0]+" introuvable")
		return False