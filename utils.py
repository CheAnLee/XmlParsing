"""
	Python Library
	Che-An Li

"""

def debugMsg(msg):
	if __debug__: print(msg)

def isStartwith(token, Str):
	if Str[:len(token)] == token:
		return True
	return False

def isEndwith(token, Str):
	if Str[-len(token):] == token:
		return True
	return False
