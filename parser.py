# Function that parse the parameters to correspond to the shell ones 
# @params: pars: list of parameters in mini-shell logic
# @return: list of parameters in bash logic

import string
import subprocess

def parseParams(commandLine):

	commands = []
	options = {}
	pars = {}
	sorties = {}
	entrees = {}


	commandLines = commandLine.split(" | ")

	for i,commandLine in enumerate(commandLines):
		args = commandLine.split()
		command = args.pop(0)
		commands.append(command)
		pars[command]=[]
		options[command]=[]
		sorties[command]=subprocess.PIPE
		entrees[command]= False

		skip = False
		for n,arg in enumerate(args):
			if not skip:
				if arg == "}":
					sorties[command] = open(args[n+1], "w")
					skipNext = True
				elif arg == "{":
					entrees[command] = open(args[n+1], "r")
					skipNext = True
				elif(list(arg)[0]=="-"):
					options[command].append(arg)
					skipNext = False
				else:
					pars[command].append(arg)
					skipNext = False
			skip = skipNext

	return commands, pars, options, entrees, sorties