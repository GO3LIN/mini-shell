import os

def go(path):
	if os.path.isdir(path[0]):
		os.chdir(path[0])
	else:
		print("Path not found")
		return False
	return True