import common

def setupseltext(r, g, b, a):
	offset = [0x279, 0x2BD, 0x481, 0x585, 0x689, 0x78D]
	with open(common.brlytpath() + "\\it_ObjSetUp_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def setupselbacktext(r, g, b, a):
	offset = [0x559]
	with open(common.brlytpath() + "\\it_Button_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
					
def setupselbackbtn(r, g, b, a):
	offset = [0x1F9, 0x259, 0x2B9]
	with open(common.brlytpath() + "\\it_Button_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def freeblocks(r, g, b, a):
	offset = [0x515]
	with open(common.brlytpath() + "\\it_ObjCubeEdit_a.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
	offset2 = [0x52D]
	with open(common.brlytpath() + "\\it_ObjChannelEdit_a.brlyt", "r+b") as infile2:
		common.writebackbtnloop(infile2, offset2, r, g, b, a)
