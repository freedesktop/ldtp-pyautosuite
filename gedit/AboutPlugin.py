#############################################################################
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#	T V Lakshmi Narasimhan <lakshminaras2002@gmail.com>
#
#  Copyright 2004 - 2006 Novell, Inc.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#
#############################################################################


from ldtp import *
from ldtputils import *

def testAboutPlugin():
	try:
		log('Testing About Plugin','info')
		time.sleep(5)
		selectmenuitem('*gedit','mnuEdit;mnuPreferences')
		waittillguiexist('dlggeditPreferences')
		if guiexist('dlggeditPreferences')==1:
			selecttab('dlggeditPreferences','ptl0','Plugins')
			noofrows=getrowcount('dlggeditPreferences','tbl1')
			i=0
			while i<noofrows:
				#select the row by its index
				selectrowindex('dlggeditPreferences', 'tbl1',i)
				#the celltext variable seems redundant
				celltext=getcellvalue ('dlggeditPreferences', 'tbl1', i,1)
				click('dlggeditPreferences','btnAboutPlugin')
				waittillguiexist('dlgAbout*')
				time.sleep(2)
				if guiexist('dlgAbout*')==1:
					log('About dialog Appears','info')
					click('dlgAbout*','btnClose')
					i=i+1
				else:
					log('About Dialog does not appear','error')
					raise LdtpExecutionError(0)
			click('dlggeditPreferences','btnClose')
		else:
			log('Preferences Dialog does not appear','error')
			raise LdtpExecutionError(0)
	except:
		log('Testing About Plugin','error')
		raise LdtpExecutionError(0)
                return
	log('Testing About Plugin Success','info')


try:
	log('Test About Plugin','teststart')
	launchapp('gedit',1)
	waittillguiexist('*gedit')
	testAboutPlugin()

except:
	log('Test About  Plugin Failed','error')
	raise LdtpExecutionError(0)
selectmenuitem('*gedit','mnuFile;mnuQuit')
time.sleep(3)
if guiexist('dlgQuestion')==1:
	click('dlgQuestion','btnClosewithoutSaving')
log('Test About Plugin','testend')

	
