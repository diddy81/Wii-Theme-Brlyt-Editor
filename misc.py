import common

def backpostbtnborder(r, g, b, a):
	offset = [0x13E9, 0x1449, 0x14A9, 0x20D1, 0x2131, 0x2191]
	with open(common.brlytpath() + "\\my_IplTop_e.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def backpostbtncolour(r, g, b, a):
	offset = [0x1509, 0x1569, 0x15C9, 0x19CD, 0x1A2D, 0x1A8D]
	with open(common.brlytpath() + "\\my_IplTop_e.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)

def backpostbtntext(r, g, b, a):
	offset = [0x1629, 0x1AED]
	with open(common.brlytpath() + "\\my_IplTop_e.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)