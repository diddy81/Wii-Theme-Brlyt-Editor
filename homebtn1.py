import common

def homedialogtext(r, g, b, a):
	offset = [0x2E51]
	with open(common.brlytpath() + "\\th_HomeBtn_d.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def homedialogbtncolour(r, g, b, a):
	offset = [0x2E95, 0x2EF5, 0x2F55, 0x2FB5, 0x3015, 0x3075]
	with open(common.brlytpath() + "\\th_HomeBtn_d.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
		
def homedialogbtnborder(r, g, b, a):
	offset = [0x3315, 0x3375, 0x33D5, 0x3435, 0x3495, 0x34F5]
	with open(common.brlytpath() + "\\th_HomeBtn_d.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def homedialogbtntext(r, g, b, a):
	offset = [0x2791, 0x27F1]
	with open(common.brlytpath() + "\\th_HomeBtn_d.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def homeclosebtncolour(r, g, b, a):
	offset = [0x35F9, 0x3659, 0x36B9]
	with open(common.brlytpath() + "\\th_HomeBtn_d.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
		
def homeclosebtntext(r, g, b, a):
	offset = [0x2551]
	with open(common.brlytpath() + "\\th_HomeBtn_d.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)