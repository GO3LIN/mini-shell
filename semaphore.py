from subprocess import *
import os

def semaf(params=[], options=[], entree=None, sortie=PIPE):
	command = ["./tubesem"]
	p = Popen(command)
	return p