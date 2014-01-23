from subprocess import *
import os

def help(path="", options=[], entree=None, sortie=PIPE):
	# Help dictionnary { "commandName": "Description"}
	helpDic = {
	"list" : "List the content of current directory",
	"go" : "Go to a directory Usage : go <path>",
	"newDir" : "Creates a directory with the name given in parameter into the current Dir",
	"newFile" : "Creates a file with the name given in parameter into the current dir",
	"del" : "Delete a file or directory given in parameter",
	"read" : "Reads the file given in parameter into stdout",
	"newFifo" : "Creates a fifo with the name given in parameter",
	"bye" : "Exit mini-shell"
	}

	for c,d in enumerate(helpDic):
		print(d, "->", helpDic[d])
	return True