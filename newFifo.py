from subprocess import *

def newFifo(params=[], options=[], entree=None, sortie=PIPE):
	command = ["mkfifo"]
	paramsBash = command+params
	
	if not params:
		print("Enter a name for the fifo.")
		return False

	if call(paramsBash) == 0:
		print("Fifo created succesfuly !")
	else:
		print("Fifo error. Maybe the fifo '"+params[0]+"' already exists.")
	return True