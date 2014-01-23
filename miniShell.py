from imports import *

os.system("clear")
print("##############################")
print("# Mini-shell v0.9 ")
print("# Version Python requise 3.x, version installée :")
os.system("python3.3 -V")

while True:
    currentDir = os.getcwd() # The current dir
    commandLine = input(currentDir+": ") # The command line
    #command = lineExploded.pop(0) # Extract the first element in command and delete it
    commands, params, options, entrees, sorties = parseParams(commandLine)
    process = []

    # Commands dictionnary { "commandName": funcToExecute }
    commandsDic = {
    "lister" : ls ,
    "go" : go,
    "newDir" : newDir,
    "newFile" : newFile,
    "supprimer": delete,
    "lire": read,
    "creerFifo": newFifo,
    "help": help,
    "reg": grep,
    "semafo": semaf,
    "messageFile": fileMsg,
    "edit": edit,
    "eff": clear
    }

    


    if(commands[0] == "bye"):
        os.system("exit")

    for i,command in enumerate(commands):

        if command not in commandsDic:
            print("Command not found. Type help for the commands list")
        else:
            if i>0:
                if not entrees[command]:
                    entrees[command] = process[i-1].stdout
            process.append(commandsDic[command](params[command], options[command], entree=entrees[command], sortie=sorties[command]))

    if process :
        if len(process)<2:
            if type(process[0]) is not bool:
                output = process[0].communicate()[0]
            else:
                output = False
        else:
            output = process[-1].communicate()[0]

        if type(output) is bytes:
            print(output.decode("utf-8"))