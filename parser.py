
# Function that parse the parameters to correspond to the shell ones 
# @params: pars: list of parameters in mini-shell logic
# @return: list of parameters in bash logic

def parseParams(pars):

	parsToBashDic = {
	"}" : ">"
	}

	for n,par in enumerate(pars):
		if par in parsToBashDic:
			pars[n] = parsToBashDic[par]

	return pars