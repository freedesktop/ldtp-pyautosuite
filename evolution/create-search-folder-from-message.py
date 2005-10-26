#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Khasim Shaheed <sshaik@novell.com>
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

# Create Search folder from message subject or sender
import time, re

from ldtp import *
from ldtputils import *

# Section to create search folder from message subject or sender
def create_search_folder (source_folder, message_index, search_condition, search_folder):
	try:
		search_mail_count = 0	
		selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', source_folder)
		time.sleep (2)
		total_messages = getrowcount ('frmEvolution-Mail', 'ttblMessageList')
		selectrowindex ('frmEvolution-Mail', 'ttblMessageList', message_index)
		time.sleep (1)

		if (search_condition == 'Subject'): 
			search_text = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', message_index, 4)
		elif (search_condition == 'Sender'):	
			search_text = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', message_index, 3)
		else:
			log (search_condition + ' condition is not handled by this script', 'cause')
			log ('Create Search folder failed', 'fail')
			return
		
		print 'Counting the number of mails which satisfy the condition...'
		# FIXME: This script does not handle the case where subject contains ':'		
		if (search_condition == 'Subject'):
			sub_strings = [None, None]
			mobj = re.search ('^\[.*?\]', search_text)
			if mobj:
				sub_strings[0] = mobj.group ()
				sub_strings[1] = mobj.string[mobj.end():]	
				sub_strings[1] = re.sub ('^\s|$\s', '', sub_strings[1])
			else:
				sub_strings[1] = search_text
				
			regexp = [None, None]
			if sub_strings[0]:	
				regexp[0] = re.compile (re.escape (sub_strings[0]), re.I)
			regexp[1] = re.compile (re.escape (sub_strings[1]), re.I)	
				
			for i in range (total_messages):
				subject = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', i, 4)
				if regexp[1].search (subject):
					search_mail_count = search_mail_count + 1
					continue
				if regexp[0]:
					if regexp[0].search (subject):
						search_mail_count = search_mail_count + 1
		else:
			mobj = re.search ('.*<', search_text)
			if mobj:	
				substr = mobj.string[mobj.end ():]
				search_string = substr[:(len(substr)-1)]
			else:
				search_string = search_text

			regexp = re.compile (re.escape (search_string))
			for i in range (total_messages):
				sender = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', i, 3)
				if regexp.search (sender):
					search_mail_count = search_mail_count + 1

		print '...done'
		selectmenuitem ('frmEvolution-Mail', 'mnuMessage;mnuSearchFolderfrom' + search_condition)
		if waittillguiexist ('dlgNewSearchFolder') == 0:
			log ('Create New Search Folder dialog not opened', 'error')
			raise LdtpExecutionError (0)

		time.sleep (1)
		settextvalue ('dlgNewSearchFolder', 'txtRulename', search_folder)
		click ('dlgNewSearchFolder', 'btnOK')
		if waittillguinotexist ('dlgNewSearchFolder') == 0:
			log ('Create New Search Folder dialog not closed', 'error')
			raise LdtpExecutionError (0)
		
		time.sleep (2)
		if guiexist ('dlgEvolutionError'):
			click ('dlgEvolutionError', 'btnOK')
			click ('dlgNewSearchFolder', 'btnCancel')

			# TODO: The reason for the error should be logged and 
			# Pass/Fail condition has to be changed accordingly
			log ('Creating search mail folder failed', 'cause')
			log ('Creating search mail folder failed', 'fail')
		else:
			if total_messages == getrowcount ('frmEvolution-Mail', 'ttblMessageList'):
				selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', search_folder)
				time.sleep (2)
				if search_mail_count == getrowcount ('frmEvolution-Mail', 'ttblMessageList'):
					log ('Create search folder passed', 'pass')
				else:
					log ('Resulting search folder does not contain all the mails that match the search criteria', 'cause')
					log ('Create search folder failed', 'fail')
			else:
				log ('Some mails are missing from source folder', 'cause')
				log ('Create search folder failed', 'fail')

	except ldtp.error, msg:
		log ('Create search folder failed, ' + str (msg), 'cause')
		log ('Create search folder failed', 'fail')
		if guiexist ('dlgNewSearchFolder'):
			click ('dlgNewSearchFolder', 'btnCancel')
		raise LdtpExecutionError (0)

# Read input from xml file
data_object = LdtpDataFileParser (datafilename)
source_folder = data_object.gettagvalue ('source_folder')
message_index = data_object.gettagvalue ('message_index')
search_condition = data_object.gettagvalue ('search_condition')
search_folder = data_object.gettagvalue ('search_folder')

# Call the function
if source_folder and message_index and search_condition and search_folder:
	create_search_folder (source_folder[0], int (message_index[0]), search_condition[0], search_folder[0])
else:
	if not (source_folder):
		log ('source_folder not provided in data xml file', 'error')
	if not (message_index):
		log ('message_index not provided in data xml file', 'error')
	if not (search_condition):
		log ('search_condition not provided in data xml file', 'error')
	if not (search_folder):
		log ('search_folder not provided in data xml file', 'error')
	log ('create search folder', 'fail')

