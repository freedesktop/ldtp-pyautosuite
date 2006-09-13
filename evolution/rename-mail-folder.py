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

# Rename a mail folder

import time

from ldtp import *
from ldtputils import *

# Section to rename a mail folder
def rename_mail_folder (prev_label, new_label):
	try:
		selectrow ('frmEvolution-*', 'ttblMailFolderTree', prev_label)
		selectmenuitem ('frmEvolution-*', 'mnuFolder;mnuRename*')
		if waittillguiexist ('dlgRenameFolder') == 0:
			log ('Rename Folder dialog not opened', 'error')
			raise LdtpExecutionError (0)

		settextvalue ('dlgRenameFolder', 'txt0', new_label)
		click ('dlgRenameFolder', 'btnOK')
		if waittillguinotexist ('dlgRenameFolder') == 0:
			log ('Rename Folder dialog not closed', 'error')
			raise LdtpExecutionError (0)

		time.sleep (2)
		if guiexist ('dlgEvolutionError'):
			click ('dlgEvolutionError', 'btnOK')
			time.sleep (1)
			click ('dlgRenameFolder', 'btnCancel')
			
			# TODO: The reason for the error should be logged and 
			# Pass/Fail condition has to be changed accordingly
			log ('Renaming folder failed', 'cause')
			log ('Renaming folder failed', 'fail')
		else:
			if doesrowexist ('frmEvolution-*', 'ttblMailFolderTree', prev_label):
				log ('Renaming a folder failed, renaming not done properly', 'cause')
				log ('Renaming a folder failed, renaming not done properly', 'fail')
			elif doesrowexist ('frmEvolution-*', 'ttblMailFolderTree', new_label):
				log ('Renaming a folder passed successfully', 'pass')
			else:
				log ('Renaming a folder failed', 'cause')
				log ('Renaming a folder failed', 'fail')

	except ldtp.error, msg:
		log ('Renaming a mail folder failed, ' + str (msg), 'cause')
		log ('Renaming a mail folder failed', 'fail')
		if guiexist ('dlgRenameFolder'):
			click ('dlgRenameFolder', 'btnCancel')
		raise LdtpExecutionError (0)	

# Read input from file
data_object = LdtpDataFileParser (datafilename)
prev_label = data_object.gettagvalue ('prev_label')
new_label = data_object.gettagvalue ('new_label')

# Call the function
if prev_label and new_label:
	rename_mail_folder (prev_label[0], new_label[0])
else:
	if not (prev_label):
		log ('prev_label not provided in data xml file', 'error')
	if not (new_label):
		log ('new_label not provided in data xml file', 'error')
	log ('Delete folder', 'fail')	

