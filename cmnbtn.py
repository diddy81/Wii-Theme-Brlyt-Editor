import common

def mainbtnborder(r, g, b, a):
	offset = [0x2535, 0x2595, 0x2655, 0x26B5, 0x2715, 0x2835, 0x2895, 0x29F9]
	with open(common.brlytpath() + "\\my_IplTop_e.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)

def newmessage(r, g, b, a):
	offset = [0x2E1E]
	with open(common.brlytpath() + "\\my_IplTop_e.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)