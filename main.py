import sys
import utils as lib
import xparser as xp

def main():
	Data = list()
	with open(sys.argv[1] ,'r') as fp:
		Data = xp.parsing(fp)

	SigL = ['EntityType', 'Property', 'NavigationProperty', 'Annotation']
	AttrL = ['Name', 'BaseType', 'Type', 'EnumMember']
	
	Data = xp.filterBySigAndAttr(Data, SigL, AttrL)
	if Data:
		for i in Data:
			l, sig, attrs = i
			if attrs:
				print(i)

if __name__ == "__main__":
	main()
