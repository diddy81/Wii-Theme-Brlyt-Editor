import common


def channelbg(r, g, b, a):
	offset = [0xA55]
	with open(common.brlytpath() + "\\my_ChTop_a.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
		
def channelbtncolour(r, g, b, a):
	offset = [0x2F1, 0x351, 0x3B1, 0x455, 0x4B5, 0x515]
	with open(common.brlytpath() + "\\my_ChTop_a.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
		
def channelbtnborder(r, g, b, a):
	offset = [0x815, 0x875, 0x8D5, 0x935, 0x995, 0x9F5]
	with open(common.brlytpath() + "\\my_ChTop_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def channelbtntext(r, g, b, a):
	offset = [0x2AD, 0x411]
	with open(common.brlytpath() + "\\my_ChTop_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def sdchannelbg(r, g, b, a):
	offset = [0x14E1]
	with open(common.brlytpath() + "\\mn_SdcardMenuBanner_bc.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
		
def sdchannelbtncolour(r, g, b, a):
	offset = [0xD7D, 0xDDD, 0xE3D, 0xEE1, 0xF41, 0xFA1]
	with open(common.brlytpath() + "\\mn_SdcardMenuBanner_bc.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
		
def sdchannelbtnborder(r, g, b, a):
	offset = [0x12A1, 0x1301, 0x1361, 0x13C1, 0x1421, 0x1481]
	with open(common.brlytpath() + "\\mn_SdcardMenuBanner_bc.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def sdchannelbtntext(r, g, b, a):
	offset = [0xD39, 0xE9D]
	with open(common.brlytpath() + "\\mn_SdcardMenuBanner_bc.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)