
def writeloop(infile, offset, red, green, blue, alpha):
		for i in offset:
			infile.seek( i, 0) 
			infile.write(chr(red) + chr(0) + chr(green) + chr(0) + chr(blue) + chr(0) + chr(0) + chr(0)
			+ chr(red) + chr(0) + chr(green) + chr(0) + chr(blue) + chr(0) + chr(alpha))
			
def writebackbtnloop(infile, offset, red, green, blue, alpha):
		for i in offset:
			infile.seek( i, 0) 
			infile.write(chr(0) + chr(0) + chr(0) + chr(0) + chr(0) + chr(0) + chr(0) + chr(0)
			+ chr(red) + chr(0) + chr(green) + chr(0) + chr(blue) + chr(0) + chr(alpha))

def brlytpath():
	try:
		with open('data.bin', "r") as pathfile:
			lines = pathfile.readline()
			return lines
	except:
		lines = ''
		return lines
	
	