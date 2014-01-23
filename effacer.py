from subprocess import *
import os

def clear(path, options=[], entree=None, sortie=PIPE):
	os.system("clear")
	return True