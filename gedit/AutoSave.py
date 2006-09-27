#############################################################################
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#	T V Lakshmi Narasimhan <lakshminaras2002@gmail.com>
#
#  Copyright 2004 - 2006 Novell,  Inc.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License,  or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, 
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not,  write to the
#  Free Software Foundation,  Inc.,  59 Temple Place - Suite 330, 
#  Boston,  MA 02111-1307,  USA.
#
#############################################################################


from ldtp import *
from ldtputils import *
from string import *
def testAutoFileSave (filename, str, noofminutes):
	try:
		log ('Test Auto File Save', 'info')	
		#delays introduced intentionally
		time.sleep (5)
       	 	selectmenuitem ('*gedit', 'mnuEdit;mnuPreferences')
    	        time.sleep (5)
       	        if guiexist ('dlggeditPreferences') == 1:
			selecttab ('dlggeditPreferences',  'ptl0',  'Editor')
			if check ('dlggeditPreferences', 'chkCreateabackupcopyoffilesbeforesaving')==0:
				click ('dlggeditPreferences', 'chkCreateabackupcopyoffilesbeforesaving')
			if check ('dlggeditPreferences', 'chkAutosavefilesevery')==0:
				click ('dlggeditPreferences', 'chkAutosavefilesevery')
			setvalue ('dlggeditPreferences', 'sbtnminutes', '1')
			click ('dlggeditPreferences', 'btnClose')
			#open a file
			selectmenuitem ('*gedit', 'mnuFile;mnuClose')
			selectmenuitem ('*gedit', 'mnuFile;mnuOpenLocation')
                        waittillguiexist ('dlgOpenLocation')
                        if guiexist ('dlgOpenLocation')==1:
                                settextvalue ('dlgOpenLocation', 'cboEnterthelocation (URI)ofthefileyouwouldliketoopen', filename)
                                click ('dlgOpenLocation', 'btnOpen')
                        else:
                                log ('Open Location dialog does not appear', 'error')
                                raise LdtpExecutionError (0)
			appendtext ('*gedit', 'txt0', str)
			#calculate the noofseconds to wait
			noofseconds= (int (noofminutes))*60+10
			time.sleep (noofseconds)
			selectmenuitem ('*gedit', 'mnuFile;mnuClose')
			#check the contents of the file
			if guiexist ('dlgQuestion') == 0:
				fp=open (filename, 'r')
				filecontents=fp.read ()
				if filecontents==str:
					log ('Test Auto File Save Success', 'info')
			else:
				log ('Test Auto File Save Failed', 'error')
				raise LdtpExecutionError (0)
				return
			time.sleep (3)
		else:
		        log ('Preferences dialog does not appear', 'error')
        	        raise LdtpExecutionError (0)
   	except:
       		log ('Test Auto File Save Failed ', 'error')
       	        raise LdtpExecutionError (0)
       		return
   	log ('Test Auto File Save Success', 'info')


try:
	log ('Test  Auto File Save', 'teststart')	
	launchapp ('gedit', 1)
	waittillguiexist ('*gedit')
	#get the data from the data xml
	obj = LdtpDataFileParser (datafilename)
	filename = obj.gettagvalue ('file0')[0]
	text = obj.gettagvalue ('text')[0]
	sampletext=obj.gettagvalue ('sampletext')[0]
	noofminutes=obj.gettagvalue ('noofminutes')[0]
	strlist=rsplit (text, ':')
	#Create the files if they dont exist
	if os.path.exists (os.getcwd () + '/' + filename) == False: 
		 a = open (filename,  'w')
		 i=0
		 length=len (strlist)
		 while i<length:
			 a.write (strlist[i]+'\n')
			 i=i+1
		 a.close ()
	testAutoFileSave (os.getcwd () + '/' + filename, sampletext, noofminutes)
except:
    log ('Test Auto File Save Failed', 'error')
    raise LdtpExecutionError (0)
time.sleep (5)
selectmenuitem ('*gedit', 'mnuFile;mnuQuit')
time.sleep (5)
if guiexist ('dlgQuestion'):
   click ('dlgQuestion', 'btnClosewithoutSaving')
log ('Test Auto File Save', 'testend')

