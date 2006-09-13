#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Author:
#     Venkateswaran S <wenkat.s@gmail.com>
#
#  Copyright 2004 Novell, Inc.
#
#  This test script is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Library General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Library General Public License for more details.
#
#  You should have received a copy of the GNU Library General Public
#  License along with this library; if not, write to the
#  Free Software Foundation, Inc., 59 Temple Place - Suite 330,
#  Boston, MA 02111-1307, USA.
#

#To create a folder.
from menu_reorganization import *
#from evoutils.menu_reorganization import *
from contact import *

def selectMailPane():
   """Selects the Mail Pane in Evolution"""
   log ('Open Evolution Mail Pane','teststart')
   setcontext ('Evolution - Mail','Evolution - Mail')
   #code to find the present window and revert back to the Mail Pane
   if guiexist('frmEvolution-Mail')!=1:
        log ('Present Window now Mail pane','info')
        setcontext ('Evolution - Mail','Evolution - Mail')
        if guiexist('frmEvolution-Mail')!=1:
             log ('Present Window now Mail pane','info')
             setcontext ('Evolution - Mail','Evolution - Calendars')
             if guiexist('frmEvolution-Mail')!=1:
                  log ('Present Window now Calendars pane','info')
                  setcontext ('Evolution - Mail','Evolution - Memos')
                  if guiexist('frmEvolution-Mail')!=1:
                       log ('Present Window now Memos pane','info')
                       setcontext ('Evolution - Mail','Evolution - Tasks')
                       log ('Present Window has to be Taskspane','info')
   time.sleep (1)
   try:
       click ('frmEvolution-*','tbtnMail')
       time.sleep(3)
       waittillguiexist ('frmEvolution-*')

   except:
       log ('error selecting Mail pane','error')
       log ('Open Evolution Mail Pane','testend')
       raise LdtpExecutionError(0)

   log ('Open Evolution Mail Pane','testend')


try:
	log('creation of a folder','teststart')
	#selectMailPane()
        selectPanel('Mail')
	data_object = LdtpDataFileParser (datafilename)

	#Extracting imput data from xml file
	Folder_name = data_object.gettagvalue ('folder_name')[0]
	location = data_object.gettagvalue ('location')[0]
	log('User data read','info')	
	selectmenuitem('frmEvolution-*','mnuFile;mnuNew;mnuMailFolder')
	if create_folder(Folder_name, location) == 1:
		log('Folder created','info')
                #log('Folder created','pass')
		#log('creation of a folder','testend')
	else:
		log('Folder not created','error')
                #log('Folder created','fail')
		#log('creation of a folder','testend')
except:
	log('cannot create a folder','error')
	#log('creation of a folder','testend')
	raise LdtpExecutionError(0)
