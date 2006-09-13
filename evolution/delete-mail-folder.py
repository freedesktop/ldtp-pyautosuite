#!/usr/bin/python
#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
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

# Delete a mail folder

import time, re

from ldtp import *
from ldtputils import *

# Section to delete a mail folder
def delete_mail_folder (folder_to_delete):
	try:
		mobj = re.search ('.*/', folder_to_delete)
		if mobj:
			folder_name = mobj.string[mobj.end ():]
		else:	
			folder_name = folder_to_delete
	
		selectrow ('frmEvolution-*', 'ttblMailFolderTree', folder_name)
		selectmenuitem ('frmEvolution-*', 'mnuFolder;mnuDelete')
		dialog_title = 'Delete \"' + folder_to_delete + '\"?'
		#setcontext ('folder label', dialog_title)
		if waittillguiexist ('dlgDelete*') == 0:
			log ('Delete folder dialog not opened', 'error')
			raise LdtpExecutionError (0)
		
		click ('dlgDelete*', 'btnDelete')
		if waittillguinotexist ('dlgDelete*') == 0:
			log ('Delete folder dialog not closed', 'error')
			raise LdtpExecutionError (0)

		time.sleep (2)
		if guiexist ('dlgEvolutionError'):
			click ('dlgEvolutionError', 'btnOK')
			# TODO: The reason for the error message should be logged
			log ('Not able to delete folder', 'cause')
			# Pass/Fail condition has to be changed in case of system folders
			log ('Delete mail folder', 'fail')
		else:
			if (doesrowexist ('frmEvolution-*', 'ttblMailFolderTree', folder_name)):
				log ('Mail folder not deleted', 'cause')
				log ('Delete mail folder failed', 'fail')
			else:	
				log ('Delete mail folder passed successfully', 'pass')

	except ldtp.error, msg:
		log ('Delete mail folder failed, ' + str (msg), 'cause')
		log ('Delete mail folder failed', 'fail')
		if guiexist ('dlgDeleteFolder'):
			click ('dlgDeleteFolder', 'btnCancel')

# Read input from xml file
data_object = LdtpDataFileParser (datafilename)
folder_to_delete = data_object.gettagvalue ('folder_to_delete')

# Call the function
if folder_to_delete:
	delete_mail_folder (folder_to_delete[0])
else:
	log ('folder_to_delete not provided in data xml file', 'error')
	log ('Delete folder', 'fail')

