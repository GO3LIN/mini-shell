# Python librairies imports
import os
import string

# My imports 
from lister import *
from go import *
from newDir import *
from newFile import *
from delete import *
from read import *
from newFifo import *
from parser import *

os.system("clear")

while True:
    currentDir = os.getcwd() # The current dir
    commandLine = input(currentDir+": ") # The command line
    lineExploded = commandLine.split(" ") # Command line splitted by the delimiter : <space>
    command = lineExploded.pop(0) # Extract the first element in command and delete it
    params = parseParams(lineExploded) # Function that translate miniShell params to bash params

    # Commands dictionnary { "commandName": funcToExecute }
    commandsDic = {
    "list" : ls ,
    "go" : go,
    "newDir" : newDir,
    "newFile" : newFile,
    "del": delete,
    "read": read,
    "newFifo": newFifo,
    "help": help
    }

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


    if(command == "bye"):
        break

    def help():
        print(helpDic)


    if command not in commandsDic:
        print("Command not found. Type help for the commands list")
    else:
        if not params:
            commandsDic[command]()
        else:
            commandsDic[command](params)