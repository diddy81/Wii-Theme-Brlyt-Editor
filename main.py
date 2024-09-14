import wx
import wx.lib.agw.cubecolourdialog as CCD
import chansel, common, homebtn1, setupsel, cmnbtn, sdchansel, channel, misc
import zipfile, os, shutil, webbrowser
from wx.lib.wordwrap import wordwrap
from urllib2 import urlopen



class PageOne(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

class PageTwo(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

class PageThree(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

class PageFour(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

class PageFive(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

class PageSix(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

class PageSeven(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

version = "1.3"

class diddy81(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, None, title="Theme Brlyt Editor %s" %version, size=(520,250))
		
		self.panel = wx.Panel(self)
		nb = wx.Notebook(self.panel)
		
		page1 = PageOne(nb)
		page2 = PageTwo(nb)
		page3 = PageThree(nb)
		page4 = PageFour(nb)
		page5 = PageFive(nb)
		page6 = PageSix(nb)
		page7 = PageSeven(nb)

		nb.AddPage(page1, "Settings")
		nb.AddPage(page2, "Main Menu")
		nb.AddPage(page3, "SD Channel")
		nb.AddPage(page4, "Inside Channel")
		nb.AddPage(page5, "Memory Management")
		nb.AddPage(page6, "Home Button")
		nb.AddPage(page7, "Misc")

		sizer = wx.BoxSizer()
		sizer.Add(nb, 1, wx.EXPAND)
		self.panel.SetSizer(sizer)
		
		self.colourData = None
		colorCubeBtn2 = wx.Button(page2, -1, "Open Color Picker", (220,150), (150,30))
		colorCubeBtn3 = wx.Button(page3, -1, "Open Color Picker", (220,150), (150,30))
		colorCubeBtn4 = wx.Button(page4, -1, "Open Color Picker", (220,150), (150,30))
		colorCubeBtn5 = wx.Button(page5, -1, "Open Color Picker", (220,150), (150,30))
		colorCubeBtn6 = wx.Button(page6, -1, "Open Color Picker", (220,150), (150,30))
		colorCubeBtn7 = wx.Button(page7, -1, "Open Color Picker", (220,150), (150,30))
		colorCubeBtn2.Bind(wx.EVT_BUTTON, self.Cube2)
		colorCubeBtn3.Bind(wx.EVT_BUTTON, self.Cube3)
		colorCubeBtn4.Bind(wx.EVT_BUTTON, self.Cube4)
		colorCubeBtn5.Bind(wx.EVT_BUTTON, self.Cube5)
		colorCubeBtn6.Bind(wx.EVT_BUTTON, self.Cube6)
		colorCubeBtn7.Bind(wx.EVT_BUTTON, self.Cube7)
		
		self.selectedmain = None
		self.selectedsd = None
		self.selectedchannel = None
		self.selectedmem = None
		self.selectedhome = None
		self.selectedmisc = None
		
		pickmain = ['Outer BG Behind Channels', 'Inner BG Behind Channels', 'Bottom Line',
					'Channel Border','Channel Spinner', 'Main Btn Border', 'Clock', 'Text Before Clock', 
					'Date', 'New Message Indicator']
					
		picksd = ['Outer BG Behind Channels', 'Inner BG Behind Channels', 'Bottom Line', 'Channel Border', 
					'Page Number', 'Title Text', 'Main Btn Border',	'Info Dialog Text', 'Info Btn Text', 
					'Info Btn Border', 'Info Btn Colour']
					
		pickchannel = ['Disk Channel Btn BG', 'Disk Channel Btn Colour', 'Disk Channel Btn Border', 'Disk Channel Btn Text',
						'SD Channel Btn BG', 'SD Channel Btn Colour', 'SD Channel Btn Border', 'SD Channel Btn Text']
					
		pickmem = [ 'Back Btn Colour', 'Back Btn Text', 'Main Btn Text', 'Free Blocks Text']
					
		pickhome = ['Dialog Text', 'Dialog Btn Colour', 'Dialog Btn Border', 'Dialog Btn Text', 'Close Btn Colour', 'Close Btn Text']
					
		pickmisc = ['Back & Post Btn Colour in Messageboard', 'Back & Post Btn Border in Messageboard', 'Back & Post Btn Text in Messageboard']
		
							
		self.pickedmain = wx.ComboBox(page2, -1, "", (10, 30), choices = pickmain, style = wx.CB_READONLY)
		self.pickedmain.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		
		self.pickedsd = wx.ComboBox(page3, -1, "", (10, 30), choices = picksd, style = wx.CB_READONLY)
		self.pickedsd.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		
		self.pickedchannel = wx.ComboBox(page4, -1, "", (10, 30), choices = pickchannel, style = wx.CB_READONLY)
		self.pickedchannel.Bind(wx.EVT_COMBOBOX, self.OnSelect)
				
		self.pickedmem = wx.ComboBox(page5, -1, "", (10, 30), choices = pickmem, style = wx.CB_READONLY)
		self.pickedmem.Bind(wx.EVT_COMBOBOX, self.OnSelect)
				
		self.pickedhome = wx.ComboBox(page6, -1, "", (10, 30), choices = pickhome, style = wx.CB_READONLY)
		self.pickedhome.Bind(wx.EVT_COMBOBOX, self.OnSelect)
				
		self.pickedmisc = wx.ComboBox(page7, -1, "", (10, 30), choices = pickmisc, style = wx.CB_READONLY)
		self.pickedmisc.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		
		
		self.spinnerselect = wx.RadioBox(page2, -1, "Choose Spinner Effect", (200, 20),
										choices=["No Spinner", "Fast Spinner",
												 "Slow Spinner"],
										majorDimension=3, style=wx.RA_SPECIFY_ROWS)
										
		self.setspinner()
		self.spinnerselect.Bind(wx.EVT_RADIOBOX, self.getspinner)
		
		self.sdspinnerselect = wx.RadioBox(page3, -1, "Choose Spinner Effect", (200, 20),
										choices=["No Spinner", "Fast Spinner",
												 "Slow Spinner"],
										majorDimension=3, style=wx.RA_SPECIFY_ROWS)
										
		self.setsdspinner()
		self.sdspinnerselect.Bind(wx.EVT_RADIOBOX, self.getsdspinner)
		
		dirDlgBtn = wx.Button(page1, -1, "Set brlyt path", (10, 10))
		dirDlgBtn.Bind(wx.EVT_BUTTON, self.onDir)
		
		wx.StaticText(page1, -1, 'Selected Brlyt Path:', (10, 160))
		self.showpath = wx.StaticText(page1, -1, common.brlytpath(), (110, 160))
		
		zipit=wx.Button(page1, -1, "Create mym", (190,10), (100,25))
		zipit.Bind(wx.EVT_BUTTON, self.makemym)
		self.cb = wx.CheckBox(page1, -1, 'Open mym folder after creation', (190, 40))
		
		self.cusmym = wx.CheckBox(page1, -1, 'Use custom mym name', (190, 60))
		self.cusmym.Bind(wx.EVT_CHECKBOX, self.usecusmym)
		self.cusmym.SetToolTip( wx.ToolTip("Set a mym name otherwise the folder name will be used") )
		self.pickmymname = wx.TextCtrl(page1, -1, '', (190, 80))
		self.pickmymname.Enable(False)
		
		
		close=wx.Button(page1, -1,"Close",(190,115),(100,30))
		self.Bind(wx.EVT_BUTTON, self.closebutton, close)
		
		thememii=wx.Button(page1, -1, "Download Thememii Mod", (10,55), (145,25))
		thememii.Bind(wx.EVT_BUTTON, self.downthememii)
		
		aboutme=wx.Button(page1, -1, "About", (10,100), (100,25))
		aboutme.Bind(wx.EVT_BUTTON, self.disclaimerbtn)
		
		self.checkupdate()
		self.firstboot()
		
	def Cube2(self, event):
			# main menu colour picker
		dlg = CCD.CubeColourDialog(self, self.colourData)
		if dlg.ShowModal() == wx.ID_OK:
			self.colourData = dlg.GetColourData()
			r, g, b, a = dlg.GetRGBAColour()
				
			try:
				if common.brlytpath() == '':
					self.patherror()
					
				elif self.selectedmain == None:
					self.selectionerror()
					
				elif self.selectedmain == 'Main Btn Border':
					cmnbtn.mainbtnborder(r, g, b, a)
					self.onInfo()
					
				elif self.selectedmain == 'New Message Indicator':
					cmnbtn.newmessage(r, g, b, a)
					self.onInfo()
					
				elif self.selectedmain == 'Outer BG Behind Channels':
					chansel.behind_channel_outer(r, g, b, a)
					self.onInfo()
					
				elif self.selectedmain == 'Inner BG Behind Channels':
					chansel.behind_channel_inner(r, g, b, a)
					self.onInfo()
					
				elif self.selectedmain == 'Clock':
					chansel.clock(r, g, b, a)
					self.onInfo()
					
				elif self.selectedmain == 'Text Before Clock':
					chansel.wiimenutext(r, g, b, a)
					self.onInfo()
					
				elif self.selectedmain == 'Date':
					chansel.date(r, g, b, a)
					self.onInfo()
					
				elif self.selectedmain == 'Bottom Line':
					chansel.line(r, g, b, a)
					self.onInfo()
				elif self.selectedmain == 'Channel Border':
					chansel.channelborder(r, g, b, a)
					self.onInfo()
				elif self.selectedmain == 'Channel Spinner':
					chansel.spinner(r, g, b, a)
					self.onInfo()
				
			except:
				self.patherror2()
				
		dlg.Destroy()
			
	def Cube3(self, event):
			# sd channel colour picker
		dlg = CCD.CubeColourDialog(self, self.colourData)
		if dlg.ShowModal() == wx.ID_OK:
			self.colourData = dlg.GetColourData()
			r, g, b, a = dlg.GetRGBAColour()
				
			try:
				if common.brlytpath() == '':
					self.patherror()
					
				elif self.selectedsd == None:
					self.selectionerror()
					
				elif self.selectedsd == 'Outer BG Behind Channels':
					sdchansel.behind_sdchannel_outer(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Inner BG Behind Channels':
					sdchansel.behind_sdchannel_inner(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Bottom Line':
					sdchansel.sdline(r, g, b, a)
					self.onInfo()
				elif self.selectedsd == 'Channel Border':
					sdchansel.sdchannelborder(r, g, b, a)
					self.onInfo()
				elif self.selectedsd == 'Page Number':
					sdchansel.sdpagetext(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Title Text':
					sdchansel.sdtitletext(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Main Btn Border':
					sdchansel.sdmainbtnborder(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Info Dialog Text':
					sdchansel.sdinfodialogtext(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Info Btn Text':
					sdchansel.sdinfobtntext(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Info Btn Border':
					sdchansel.sdinfobtnborder(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Info Btn Colour':
					sdchansel.sdinfobtncolour(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Channel Btn Colour':
					sdchansel.sdchannelbtncolour(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Channel Btn Border':
					sdchansel.sdchannelbtnborder(r, g, b, a)
					self.onInfo()
					
				elif self.selectedsd == 'Channel Btn Text':
					sdchansel.sdchannelbtntext(r, g, b, a)
					self.onInfo()
				
			except:
				self.patherror2()
		dlg.Destroy()
			
	def Cube4(self, event):
			# inside channel colour picker
		dlg = CCD.CubeColourDialog(self, self.colourData)
		if dlg.ShowModal() == wx.ID_OK:
			self.colourData = dlg.GetColourData()
			r, g, b, a = dlg.GetRGBAColour()
				
			try:
				if common.brlytpath() == '':
					self.patherror()
					
				elif self.selectedchannel == None:
					self.selectionerror()
					
				elif self.selectedchannel == 'Disk Channel Btn BG':
					channel.channelbg(r, g, b, a)
					self.onInfo()
					
				elif self.selectedchannel == 'Disk Channel Btn Colour':
					channel.channelbtncolour(r, g, b, a)
					self.onInfo()
					
				elif self.selectedchannel == 'Disk Channel Btn Border':
					channel.channelbtnborder(r, g, b, a)
					self.onInfo()
					
				elif self.selectedchannel == 'Disk Channel Btn Text':
					channel.channelbtntext(r, g, b, a)
					self.onInfo()
					
				elif self.selectedchannel == 'SD Channel Btn BG':
					channel.sdchannelbg(r, g, b, a)
					self.onInfo()
					
				elif self.selectedchannel == 'SD Channel Btn Colour':
					channel.sdchannelbtncolour(r, g, b, a)
					self.onInfo()
					
				elif self.selectedchannel == 'SD Channel Btn Border':
					channel.sdchannelbtnborder(r, g, b, a)
					self.onInfo()
					
				elif self.selectedchannel == 'SD Channel Btn Text':
					channel.sdchannelbtntext(r, g, b, a)
					self.onInfo()
				
			except:
				self.patherror2()
		dlg.Destroy()
			
	def Cube5(self, event):
			# setupsel colour picker
		dlg = CCD.CubeColourDialog(self, self.colourData)
		if dlg.ShowModal() == wx.ID_OK:
			self.colourData = dlg.GetColourData()
			r, g, b, a = dlg.GetRGBAColour()
				
			try:
				if common.brlytpath() == '':
					self.patherror()
					
				elif self.selectedmem == None:
					self.selectionerror()
									
				elif self.selectedmem == 'Back Btn Colour':
					setupsel.setupselbackbtn(r, g, b, a)
					self.onInfo()
				elif self.selectedmem == 'Back Btn Text':
					setupsel.setupselbacktext(r, g, b, a)
					self.onInfo()
				elif self.selectedmem == 'Main Btn Text':
					setupsel.setupseltext(r, g, b, a)
					self.onInfo()
				elif self.selectedmem == 'Free Blocks Text':
					setupsel.freeblocks(r, g, b, a)
					self.onInfo()
				
			except:
				self.patherror2()
		dlg.Destroy()
			
	def Cube6(self, event):
			# homebtn1 colour picker
		dlg = CCD.CubeColourDialog(self, self.colourData)
		if dlg.ShowModal() == wx.ID_OK:
			self.colourData = dlg.GetColourData()
			r, g, b, a = dlg.GetRGBAColour()
				
			try:
				if common.brlytpath() == '':
					self.patherror()
					
				elif self.selectedhome == None:
					self.selectionerror()
									
				elif self.selectedhome == 'Dialog Text':
					homebtn1.homedialogtext(r, g, b, a)
					self.onInfo()
									
				elif self.selectedhome == 'Dialog Btn Colour':
					homebtn1.homedialogbtncolour(r, g, b, a)
					self.onInfo()
									
				elif self.selectedhome == 'Dialog Btn Border':
					homebtn1.homedialogbtnborder(r, g, b, a)
					self.onInfo()
									
				elif self.selectedhome == 'Dialog Btn Text':
					homebtn1.homedialogbtntext(r, g, b, a)
					self.onInfo()
									
				elif self.selectedhome == 'Close Btn Colour':
					homebtn1.homeclosebtncolour(r, g, b, a)
					self.onInfo()
									
				elif self.selectedhome == 'Close Btn Text':
					homebtn1.homeclosebtntext(r, g, b, a)
					self.onInfo()
				
			except:
				self.patherror2()
		dlg.Destroy()
			
	def Cube7(self, event):
			# homebtn1 colour picker
		dlg = CCD.CubeColourDialog(self, self.colourData)
		if dlg.ShowModal() == wx.ID_OK:
			self.colourData = dlg.GetColourData()
			r, g, b, a = dlg.GetRGBAColour()
				
			try:
				if common.brlytpath() == '':
					self.patherror()
					
				elif self.selectedmisc == None:
					self.selectionerror()
									
				elif self.selectedmisc == 'Back & Post Btn Colour in Messageboard':
					misc.backpostbtncolour(r, g, b, a)
					self.onInfo()
									
				elif self.selectedmisc == 'Back & Post Btn Border in Messageboard':
					misc.backpostbtnborder(r, g, b, a)
					self.onInfo()
									
				elif self.selectedmisc == 'Back & Post Btn Text in Messageboard':
					misc.backpostbtntext(r, g, b, a)
					self.onInfo()
				
			except:
				self.patherror2()
		dlg.Destroy()
			
				

	def setspinner(self):
		if not os.path.exists(common.brlytpath() + '/../do_not_delete\spinners'):
			self.spinnerselect.SetSelection(0)
			
		elif not os.path.exists(common.brlytpath() + "\\fastOn.brlan") and not os.path.exists(common.brlytpath() + "\\slowOn.brlan"):
			self.spinnerselect.SetSelection(0)
			
		elif os.path.exists(common.brlytpath() + "\\fastOn.brlan"):
			self.spinnerselect.SetSelection(1)
			
		elif os.path.exists(common.brlytpath() + "\\slowOn.brlan"):
			self.spinnerselect.SetSelection(2)
		
	def getspinner(self, event):
		if  not os.path.exists('data.bin'):
			self.setspinner()
			self.patherror()
		else:			
			try:
				if self.spinnerselect.GetSelection() == 0:
					try:
						os.remove(common.brlytpath() + '\\slowOn.brlan')
						os.remove(common.brlytpath() + '\\slowOff.brlan')
					except:
						os.remove(common.brlytpath() + '\\fastOn.brlan')
						os.remove(common.brlytpath() + '\\fastOff.brlan')
					else:
						pass
				elif self.spinnerselect.GetSelection() == 1:
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\fastOn.brlan", common.brlytpath())
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\fastOff.brlan", common.brlytpath())
					try:
						os.remove(common.brlytpath() + '\\slowOn.brlan')
						os.remove(common.brlytpath() + '\\slowOff.brlan')		
					except:
						pass
				elif self.spinnerselect.GetSelection() == 2:
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\slowOn.brlan", common.brlytpath())
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\slowOff.brlan", common.brlytpath())
					try:
						os.remove(common.brlytpath() + '\\fastOn.brlan')
						os.remove(common.brlytpath() + '\\fastOff.brlan')		
					except:
						pass
			except:
				self.setspinner()
				self.packerror()
							
	def setsdspinner(self):
		if not os.path.exists(common.brlytpath() + '/../do_not_delete\spinners'):
			self.sdspinnerselect.SetSelection(0)
			
		elif not os.path.exists(common.brlytpath() + "\\sdfastOn.brlan") and not os.path.exists(common.brlytpath() + "\\sdslowOn.brlan"):
			self.sdspinnerselect.SetSelection(0)
			
		elif os.path.exists(common.brlytpath() + "\\sdfastOn.brlan"):
			self.sdspinnerselect.SetSelection(1)
			
		elif os.path.exists(common.brlytpath() + "\\sdslowOn.brlan"):
			self.sdspinnerselect.SetSelection(2)
		
	def getsdspinner(self, event):
		if  not os.path.exists('data.bin'):
			self.setsdspinner()
			self.patherror()
		else:
			try:
				if self.sdspinnerselect.GetSelection() == 0:
					try:
						os.remove(common.brlytpath() + '\\sdslowOn.brlan')
						os.remove(common.brlytpath() + '\\sdslowOff.brlan')
					except:
						os.remove(common.brlytpath() + '\\sdfastOn.brlan')
						os.remove(common.brlytpath() + '\\sdfastOff.brlan')
					else:
						pass
				elif self.sdspinnerselect.GetSelection() == 1:
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\fastOn.brlan", common.brlytpath() + '\\sdfastOn.brlan')
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\fastOff.brlan", common.brlytpath() + '\\sdfastOff.brlan')
					try:
						os.remove(common.brlytpath() + '\\sdslowOn.brlan')
						os.remove(common.brlytpath() + '\\sdslowOff.brlan')		
					except:
						pass
				elif self.sdspinnerselect.GetSelection() == 2:
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\slowOn.brlan", common.brlytpath() + '\\sdslowOn.brlan')
					shutil.copy2(common.brlytpath() + "/../do_not_delete\spinners\\slowOff.brlan", common.brlytpath() + '\\sdslowOff.brlan')
					try:
						os.remove(common.brlytpath() + '\\sdfastOn.brlan')
						os.remove(common.brlytpath() + '\\sdfastOff.brlan')		
					except:
						pass
			except:
				self.setsdspinner()
				self.packerror()
				
	def closebutton(self,event):
		self.Destroy()
		
	def makemym(self, event):
		try:
			target_dir = common.brlytpath() + '/..'
			mymname=target_dir.split('\\')
			
			if self.cusmym.GetValue() == True:
				newmym = self.pickmymname.GetValue()
				if newmym[-4:] == '.mym' or newmym[-4:] == '.MYM':
					newmym = newmym[:-4]
			else:
				n=len(mymname)
				newmym = mymname[n-2]
				
			zip = zipfile.ZipFile(target_dir + '/../' + newmym + '.mym', 'w', zipfile.ZIP_DEFLATED)
			rootlen = len(target_dir) + 1
			for base, dirs, files in os.walk(target_dir):
			   for file in files:
				  fn = os.path.join(base, file)
				  zip.write(fn, fn[rootlen:])
							
			mympath = mymname[:-2]
			self.path = os.path.join(*mympath)
			self.mymcreated()
			if self.cb.GetValue() == True:
				webbrowser.open(self.path)
		except:
			self.patherror()
			
	def usecusmym(self, event):
		if self.cusmym.Value==True:
			self.pickmymname.Enable(True)
		else:
			self.pickmymname.Enable(False)
			
	def onDir(self, event):
		dlg = wx.DirDialog(self, "Choose your brlyt directory:", style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			with open("data.bin", "w") as dirpath:
				dirpath.write(dlg.GetPath())
		dlg.Destroy()
		self.setsdspinner()
		self.setspinner()
		self.showpath.SetLabel(common.brlytpath())
		
	def OnSelect(self, event):
		self.selectedmain = self.pickedmain.GetValue()
		self.selectedsd = self.pickedsd.GetValue()
		self.selectedchannel = self.pickedchannel.GetValue()
		self.selectedmem = self.pickedmem.GetValue()
		self.selectedhome = self.pickedhome.GetValue()
		self.selectedmisc = self.pickedmisc.GetValue()
	
	def firstboot(self):
		if not os.path.exists('data.bin'):
			self.disclaimer()
							
	def disclaimerbtn(self, event):
		self.disclaimer()
	
	def disclaimer(self):
		info = wx.AboutDialogInfo()
		info.Name = "Theme Brlyt Editor"
		info.Version = version
		info.Description = wordwrap(
			"This program is designed to be used in conjunction with the Wii Theme Team Base Pack and Thememii MOD \n\n Some functions may work with other theme bases but not all \n\n If you dont have the base pack you can download it from the link below\n\n  First thing you need to do is set your brlyt folder",
			420, wx.ClientDC(self.panel))
		info.WebSite = ("https://www.dropbox.com/s/9j7sbrrxrenz0ij/Wii%20Theme%20Team%20Base%20Pack.rar?dl=1", "Wii Theme Team Base Pack")
		info.Developers = ["Diddy81"]
		# Show the wx.AboutBox
		wx.AboutBox(info)
			
	def downthememii(self, event):
		webbrowser.open('https://www.dropbox.com/s/8654u43ioxjhvmr/Thememii_MOD.rar?dl=1', new=0, autoraise=True)
			
	# start of messages here
	def selectionerror(self):
		self.showMessageDlg("You haven't selected a menu part to change!",
							"Information", wx.OK|wx.ICON_INFORMATION)
								
	def mymcreated(self):		
		self.showMessageDlg("mym has been created at\n" + self.path,
							"Information", wx.OK|wx.ICON_INFORMATION)
							
	def packerror(self):
		self.showMessageDlg("This function only works with the Wii Theme Team Base Pack",
							"Information", wx.OK|wx.ICON_INFORMATION)
							
	def patherror(self):
		self.showMessageDlg("You haven't set a brlyt path!",
							"Information", wx.OK|wx.ICON_INFORMATION)
														
	def patherror2(self):
		self.showMessageDlg("Needed file not found \nPlease check Your brlyt path!",
							"Information", wx.OK|wx.ICON_INFORMATION)
							
	def onInfo(self):
		self.showMessageDlg("The new color infomation has been written!",
							"Information", wx.OK|wx.ICON_INFORMATION)
																					
	def showMessageDlg(self, msg, title, style):
		dlg = wx.MessageDialog(parent=None, message=msg, caption=title, style=style)
		dlg.ShowModal()
		dlg.Destroy()
	
	# i dont know if this program will ever need a update but its worth putting this in anyway
	def checkupdate(self):
		try:
			ur = urlopen("https://pastebin.com/raw/ugrAshDE")
			contents = ur.readline()			
			if contents != version:
				self.newupdate()
		except:
			pass
			
	def newupdate(self):
		dlg = wx.MessageDialog(None, "A update is available for Theme Brlyt Editer\nWould you like to download the update now?\n\nClicking Yes will end this session and open a download link",
							"Update", wx.YES_NO|wx.ICON_EXCLAMATION)
		retCode = dlg.ShowModal()
		if (retCode == wx.ID_YES):
			webbrowser.open('https://www.dropbox.com/s/9oiord3mnnh26xt/Theme%20Brlyt%20Editor.exe?dl=1', new=0, autoraise=True)
			self.Destroy()

if __name__ == "__main__":
	app = wx.App(0)
	diddy81().Show()
	app.MainLoop()