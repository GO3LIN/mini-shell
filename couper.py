from subprocess import *

def couper(params=[], options=[], entree=None, sortie=PIPE):
	if not params:
		print("Parametres manquants")
		return False
	command = ["cut"]
	paramsBash = []
	for i,op in enumerate(options):
		paramsBash.append(options[i])
		paramsBash.append(params[i])
	p = Popen(paramsBash)
	p.wait()
	return p