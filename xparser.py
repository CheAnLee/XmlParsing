import utils as lib

S = ['<?', '<', '</', '/>', '>']

def removeSign(data):
	if not data or data is None:
		return None
	ret = ''
	if data[0] == '<':
		if data[1] == '?' or data[1] == '/':
			ret = data[2:]
		else:
			ret = data[1:]
	if data[-1] == '>':
		if data[-2] == '/':
			ret = ret[:-2]
		else:
			ret = ret[:-1]
	if not ret:
		return data
	return ret

def classisfy(data):
	if not data or data is None:
		return
	tokens = data.split()
	if len(tokens) < 0:
		return
	signature = tokens[0]
	if len(tokens) > 1:
		attr = list()
		for t in tokens[1:]:
			# correct mistaken token splited by whatespace
			if '=' in t:
				attr.append(t)
			else:
				attr[-1] = str(attr[-1])+' '+str(t)
		attrL = list()
		for element in attr:
			name = element.split('=')[0]
			value = element.split('=')[1][1:-1]
			attrL.append([name, value])
		return signature, attrL
	return signature, []

def showByLayer(List):
	if not List or List is None:
		return
	layBase = List[0][0]
	tabSize = 4
	for element in List:
		layer, sig, attrL = element
		F = "%"+str((layer-layBase)*tabSize)+"s %s"
		if attrL: print(F % ('-', element))

def parsing(fp):
	if fp is None:
		return None

	ret = list()
	symbol = list()
	layerNum = 0

	lineNum = sum(1 for line in fp)
	fp.seek(0)
	idx = 0
	action = 0
	while idx < lineNum:
		action = 0
		line = fp.readline().strip()
		lib.debugMsg("------------------ %s ------------------------" % idx)
		# Empty line
		if not line or lib.isStartwith(S[0], line):
			idx += 1
			continue
		# End of Attr.
		if lib.isStartwith(S[2], line):
			lib.debugMsg("POP  "+str(line.split()[0]))
			t = symbol.pop()
			if t[1:] not in line.split()[0]:
				lib.debugMsg("Error")
				return None
			action = -1
		# New Attr.
		elif lib.isStartwith(S[1], line):
			if (not lib.isEndwith(S[4], line)) and (not lib.isEndwith(S[3], line)):
				line = line + str(fp.readline().strip())
				idx += 1
			lib.debugMsg("PUSH  " + str(line.split()[0]))
			if lib.isEndwith(S[3], line):
				lib.debugMsg("POP  "+str(line.split()[0]))
			else:
				symbol.append(line.split()[0])
				action = 1
		sig, attrL = classisfy(removeSign(line))
		ret.append([layerNum, sig, attrL])
		idx += 1
		layerNum += action
		lib.debugMsg(symbol)

	if symbol:
		lib.debugMsg("Error")
		return None
	return ret

def filterBySigAndAttr(List, SigL=[], AttrL=[]):
	if List is None or not SigL:
		return None

	ret = list()
	for element in List:
		layer, sig, attrL = element
		if not set([sig]).intersection(set(SigL)):
			continue
		tempAttrList = list()
		for attr in attrL:
			name, val = attr
			if set([name]).intersection(set(AttrL)):
				tempAttrList.append([name, val])
		ret.append([layer, sig, tempAttrList])
	return ret
