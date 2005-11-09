#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Khasim Shaheed <khasim.shaheed@gmail.com>
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

# Create a mail folder

import time

from ldtp import *
from ldtputils import *

# Section to create a mail folder
def create_mail_folder (parent, folder_name):
	try:
		if parent == 'Search Folders':
			log ('Can not create vFolder using this script', 'cause')
			log ('Can not create vFolder using this script', 'fail')
			return
		else:	
			selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', parent)

		selectmenuitem ('frmEvolution-Mail', 'mnuFolder;mnuNew1')
		if waittillguiexist ('dlgCreatefolder') == 0:
			log ('Create folder dialog not opened', 'error')
			raise LdtpExecutionError (0)
			
		selectrowpartialmatch ('dlgCreatefolder', 'ttblMailFolderTree', parent)
		settextvalue ('dlgCreatefolder', 'txtFoldername', folder_name)
		click ('dlgCreatefolder', 'btnCreate')
		if waittillguinotexist ('dlgCreatefolder') == 0:
			log ('Create folder dialog not closed', 'error')
			raise LdtpExecutionError (0)
		
		time.sleep (2)
		if guiexist ('dlgEvolutionError'):
			click ('dlgEvolutionError', 'btnOK')
			time.sleep (1)
			click ('dlgCreatefolder', 'btnCancel')
			time.sleep (1)

			# TODO: The reason for the error should be logged and 
			# Pass/Fail condition has to be changed accordingly
			log ('Creating mail folder failed', 'cause')
			log ('Creating mail folder failed', 'fail')
		else:
			# TODO: If the folder is created as child of some already existing folder
			# this verification will fail because by default it will be in collapsed state.
			# So first we have to expand the tree and then execute the following steps.
			if doesrowexist ('frmEvolution-Mail', 'ttblMailFolderTree', folder_name):
				log ('Creating a mail folder passed successfully', 'pass')
			else:
				log ('Creating a mail folder failed', 'cause')
				log ('Creating a mail folder failed', 'fail')

	except ldtp.error, msg:
		log ('Creating a mail folder failed, ' + str (msg), 'cause')
		log ('Creating a mail folder failed', 'fail')
		if guiexist ('dlgCreatefolder'):
			click ('dlgCreatefolder', 'btnCancel')
		raise LdtpExecutionError (0)	

# Read input from xml file
data_object = LdtpDataFileParser (datafilename)
parent = data_object.gettagvalue ('parent')
folder_name = data_object.gettagvalue ('folder_name')

# Call the function
if parent and folder_name:
	create_mail_folder (parent[0], folder_name[0])
else:
	if not (parent):
		log ('parent not provided in data xml file', 'error')
	if not (folder_name):
		log ('folder_name not provided in data xml file', 'error')
	log ('Create folder', 'fail')	

