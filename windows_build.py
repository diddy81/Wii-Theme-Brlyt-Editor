from distutils.core import setup
from py2exe.build_exe import py2exe
import os, os.path, shutil, sys

current = '1.0'

dir = 'distrib/windows'

print '[[ Running Theme Brlyt Editor Through py2exe! ]]'
print '>> Destination directory: %s' % dir
sys.argv.append('py2exe')

if os.path.isdir(dir): shutil.rmtree(dir)
os.makedirs(dir)

excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
			'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
			'Tkconstants', 'Tkinter', 'doctest', 'pdb', 'unittest', 'difflib', 'inspect',
			'_ssl', 'pyreadline', 'optparse', 'pickle', 'calendar']    

includes = ['chansel', 'cmnbtn', 'common', 'homebtn1', 'setupsel', 'sdchansel', 'channel', 'misc']

packages = []

dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
				'tk84.dll']
setup(
    name='Theme Brlyt Editor',
    version=current,
    description="Easily edit Theme brlyt files",
    windows=[
        {'script': 'main.py',
		"dest_base": "Theme Brlyt Editor",
		"icon_resources": [(1, "brlyt.ico")]
         }
    ],
    options={'py2exe':{
        'includes': includes,
        'compressed': 1,
        'optimize': 2,
        'excludes': excludes,
		"packages": packages,
		"dll_excludes": dll_excludes,
        'bundle_files': 1,
        'dist_dir': dir
    }}
	,zipfile = None
	)

os.unlink(dir + '/w9xpopen.exe')
