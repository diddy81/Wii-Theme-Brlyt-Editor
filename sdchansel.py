import common

def sdline(r, g, b, a):
	offset = [0xD39, 0xF05, 0x1071, 0x11DD, 0x1349]
	with open(common.brlytpath() + "\\mn_SdcardMenu_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)

def behind_sdchannel_outer(r, g, b, a):
	offset = [0x23D, 0x2E9, 0x395, 0x441, 0x4ED, 0x599, 0x5F9, 0x659, 0x6B9, 0x719,
			0x779, 0x7F9, 0x879, 0x8F9, 0x979, 0xE59, 0xFC9, 0x1131, 0x129D, 0x13A9]
			
	trans = [0x149c]
	if a == 0:
		vis = 0
	else:
		vis = 1
	with open(common.brlytpath() + "\\mn_SdcardMenu_a.brlyt", "r+b") as infile:
		for i in offset:
			infile.seek( i, 0) 
			infile.write(chr(r) + chr(0) + chr(g) + chr(0) + chr(b) + chr(0) + chr(a))
		for i in trans:
			infile.seek( i, 0) 
			infile.write(chr(vis))

def behind_sdchannel_inner(r, g, b, a):
	offset = [0x245, 0x2F1, 0x39D, 0x449, 0x4F5, 0x5A1, 0x601, 0x661, 0x6C1, 0x721,
	0x781, 0x801, 0x881, 0x901, 0x981, 0xE61, 0xFD1, 0x1139, 0x12A5, 0x13B1]
	with open(common.brlytpath() + "\\mn_SdcardMenu_a.brlyt", "r+b") as infile:
		for i in offset:
			infile.seek( i, 0) 
			infile.write(chr(r) + chr(0) + chr(g) + chr(0) + chr(b) + chr(0) + chr(a))
		
def sdchannelborder(r, g, b, a):
	offset = [0xA59, 0xAD9, 0xB59, 0xBD9, 0xC59]
	with open(common.brlytpath() + "\\mn_SdcardMenu_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def sdpagetext(r, g, b, a):
	offset = [0x85, 0xC9]
	with open(common.brlytpath() + "\\mn_SdcardMenu_Page.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def sdtitletext(r, g, b, a):
	offset = [0x52D]
	with open(common.brlytpath() + "\\mn_SdcardMenu_b.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)

def sdmainbtnborder(r, g, b, a):
	offset = [0x22D, 0x631]
	with open(common.brlytpath() + "\\mn_SdcardMenu_b.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def sdinfodialogtext(r, g, b, a):
	offset = [0x4A9]
	with open(common.brlytpath() + "\\my_DialogWindow_a2.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def sdinfobtntext(r, g, b, a):
	offset = [0x591, 0x6F5]
	with open(common.brlytpath() + "\\my_DialogWindow_a2.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def sdinfobtnborder(r, g, b, a):
	offset = [0xA99, 0xAF9, 0xB59, 0xBB9, 0xC19, 0xC79]
	with open(common.brlytpath() + "\\my_DialogWindow_a2.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
			
def sdinfobtncolour(r, g, b, a):
	offset = [0x5D5, 0x635, 0x695, 0x739, 0x799, 0x7F9]
	with open(common.brlytpath() + "\\my_DialogWindow_a2.brlyt", "r+b") as infile:
		common.writebackbtnloop(infile, offset, r, g, b, a)
		
def spinner(r, g, b, a):
	offset = [0x69]
	with open(common.brlytpath() + "\\my_IplTop_d.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		