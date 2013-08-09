import common

def line(r, g, b, a):
	offset = [0xDE5, 0xFB1, 0x111D, 0x1289, 0x13F5]
	with open(common.brlytpath() + "\\my_IplTop_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)

def behind_channel_outer(r, g, b, a):
	offset = [0x23D, 0x2E9, 0x395, 0x441, 0x4ED, 0x599, 0x5F9, 0x659, 0x6B9, 0x719,
			0x779, 0x825, 0x8A5, 0x925, 0x9A5, 0xA25, 0xF05, 0x1071, 0x11DD, 0x1349]
			
	trans = [0x149c]
	if a == 0:
		vis = 0
	else:
		vis = 1
	with open(common.brlytpath() + "\\my_IplTop_a.brlyt", "r+b") as infile:
		for i in offset:
			infile.seek( i, 0) 
			infile.write(chr(r) + chr(0) + chr(g) + chr(0) + chr(b) + chr(0) + chr(a))
		for i in trans:
			infile.seek( i, 0) 
			infile.write(chr(vis))

def behind_channel_inner(r, g, b, a):
	offset = [0x245, 0x2F1, 0x39D, 0x449, 0x4F5, 0x5A1, 0x601, 0x661, 0x6C1, 0x721,
	0x781, 0x82D, 0x8AD, 0x92D, 0x9AD, 0xA2D, 0xF0D, 0x1079, 0x11E5, 0x1351]
	with open(common.brlytpath() + "\\my_IplTop_a.brlyt", "r+b") as infile:
		for i in offset:
			infile.seek( i, 0) 
			infile.write(chr(r) + chr(0) + chr(g) + chr(0) + chr(b) + chr(0) + chr(a))

		
def channelborder(r, g, b, a):
	offset = [0xB05, 0xB5D, 0xC05, 0xC85, 0xD05]
	with open(common.brlytpath() + "\\my_IplTop_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
			
def spinner(r, g, b, a):
	offset = [0x69]
	with open(common.brlytpath() + "\\my_IplTop_d.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def clock(r, g, b, a):
	offset = [0x22D, 0x28D, 0x2ED, 0x34D, 0x3AD, 0x8ED, 0x991]
	with open(common.brlytpath() + "\\my_Clock_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
			
def wiimenutext(r, g, b, a):
	offset = [0x94D]
	with open(common.brlytpath() + "\\my_Clock_a.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
		
def date(r, g, b, a):
	offset = [0x1E1, 0x225, 0x269]
	with open(common.brlytpath() + "\\my_IplTop_c.brlyt", "r+b") as infile:
		common.writeloop(infile, offset, r, g, b, a)
			
