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

# Search for mail based on one of the following search conditions
# a) Subject or Sender contains 
# b) Subject contains
# c) Sender contains
#

import time, re

from ldtp import *
from ldtputils import *

# Section to perform search for mail based on above search condition
def search (search_type, search_folder, search_text):
	try:
		selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', search_folder)
		time.sleep (2)
		search_mail_count = 0
		total_mail_count = getrowcount ('frmEvolution-Mail', 'ttblMessageList')
		
		print 'Counting the number of mails which satisfy the condition...'
		regexp = re.compile (re.escape (search_text), re.I)

		if (search_type == 'Subject or Sender contains'):
			for i in range (total_mail_count):
				subject = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', i, 4)
				sender = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', i, 3)
				if (regexp.search (subject) or regexp.search (sender)):
					search_mail_count = search_mail_count + 1
		elif (search_type == 'Subject contains'):			
			for i in range (total_mail_count):
				subject = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', i, 4)
				if (regexp.search (subject)): 
					search_mail_count = search_mail_count + 1
		elif (search_type == 'Sender contains'):	
			for i in range (total_mail_count):
				sender = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', i, 3)
				if (regexp.search (sender)):
					search_mail_count = search_mail_count + 1
		else:
			log ('This type of search is not handled by this script', 'cause')
			log ('This type of search is not handled by this script', 'fail')
			return
		
		print '...done'
		comboselect ('frmEvolution-Mail', 'cboSearchType', search_type)
		settextvalue ('frmEvolution-Mail', 'txtSearchTextEntry', search_text)
		click ('frmEvolution-Mail', 'btnFindNow')
		time.sleep (2)
		filter_mail_count = getrowcount ('frmEvolution-Mail', 'ttblMessageList')
		click ('frmEvolution-Mail', 'btnClear')
		time.sleep (2)

		if search_mail_count == filter_mail_count:
			log ('Search based on ' + search_type + ' passed', 'pass')
		else:
			log ('Search based on ' + search_type + ' failed', 'cause')
			log ('Search based on ' + search_type + ' failed', 'fail')
			
	except ldtp.error, msg:
		log ('Search based on ' + search_type + ' failed '+ str (msg), 'cause')
		log ('Search based on ' + search_type + ' failed', 'fail')
		raise LdtpExecutionError (0)
			
# Read input from file
data_object = LdtpDataFileParser (datafilename)
search_type = data_object.gettagvalue ('search_type')
search_folder = data_object.gettagvalue ('search_folder')
search_text = data_object.gettagvalue ('search_text')

# Call the function
if search_type and search_folder and search_text:
	search (search_type[0], search_folder[0], search_text[0])
else:
	if not (search_type):
		log ('search_type is not provided in data xml file', 'error')
	if not (search_folder):
		log ('search_folder is not provided in data xml file', 'error')
	if not (search_text):
		log ('search_text is not provided in data xml file', 'error')
	log ('search mail', 'fail')

