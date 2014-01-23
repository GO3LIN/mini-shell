from subprocess import *
import os

def fileMsg(params=[], options=[], entree=None, sortie=PIPE):
	command = ["./fm1"]
	p = Popen(command)
	return p