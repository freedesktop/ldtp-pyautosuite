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
def testViewToolbarOptions():
	try:
		log('Testing View Toolbar Options','info')	
		if (menucheck('*gedit','mnuView;mnuStatusbar'))==1:
			selectmenuitem('*gedit','mnuView;mnuStatusbar')
		if (menucheck('*gedit','mnuView;mnuToolbar'))==1:
			selectmenuitem('*gedit','mnuView;mnuToolbar')
		time.sleep(3)			
		#check for buttons
		a=getobjectlist('*gedit')
		if 'mnuToolbar'  in  a:
			retval=0
		#check for statusbar
		retval1=verifystatusbarvisible('*gedit','stat0')
		time.sleep(3)
		if (retval1==0 and retval==0):
			log('Test View Toolbar Options Success','info')
		else:
			log('Test View Toolbar Options Failed','error')
			raise LdtpExecutionError(0)
			return
   	except:
       		log('Test View Toolbar Options Failed','error')
       	        raise LdtpExecutionError(0)
       		return
	selectmenuitem('*gedit','mnuView;mnuStatusbar')
	

		
try:
	log('Test View Toolbar Options','teststart')	
	launchapp('gedit',1)
	waittillguiexist('*gedit')
	testViewToolbarOptions()
except:
	log('Test View Toolbar Options Failed','error')
	raise LdtpExecutionError(0)
selectmenuitem('*gedit','mnuFile;mnuQuit')
time.sleep(5)
if guiexist('dlgQuestion')==1:
	click('dlgQuestion','btnClosewithoutSaving')
log('Test View Toolbar Options','testend')
