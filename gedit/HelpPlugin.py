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
from string import *
def testHelpPlugin():
	try:
		log('Testing Help','info')	
       	 	selectmenuitem('*gedit','mnuHelp;mnuContents')
		time.sleep(15)
		#check for the manual window
		if guiexist('*geditManual*')==1:
			log('Manual window appears','info')
		else:
		        log('Manual does not appear','error')
        	        raise LdtpExecutionError(0)
		selectmenuitem('*gedit','mnuHelp;mnuAbout')
		time.sleep(10)
		#check for the About window
		if guiexist('dlgAboutgedit')==1:
			click('dlgAboutgedit','btnCredits')
			time.sleep(5)
			if guiexist('dlgCredits')==1:
				log('Test Help About Success','info')
				click('dlgCredits','btnClose')
			else:
				log('Credits Dialog does not appear','error')
				raise LdtpExecutionError(0)
			click('dlgAboutgedit','btnClose')
		else:
			log('About Gedit Dialog does not appear','error')
			raise LdtpExecutionError(0)
   	except:
       		log('Test Help Failed','error')
       	        raise LdtpExecutionError(0)
       		return
   	log('Test Help  Success','info')

		
try:
	log('Test Help Plugin','teststart')	
	launchapp('gedit',1)
	waittillguiexist('*gedit')
	testHelpPlugin()
except:
	log('Test Help Plugin Failed','error')
	raise LdtpExecutionError(0)
if guiexist('*gedit'):
	selectmenuitem('*gedit','mnuFile;mnuQuit')
	time.sleep(5)
	if guiexist('dlgQuestion')==1:
		click('dlgQuestion','btnClosewithoutSaving')
log('Test Help lugin','testend')
