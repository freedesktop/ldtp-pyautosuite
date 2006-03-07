#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Authors:
#     Nagashree <mnagashree@novell.com>
#     Premkumar <jpremkumar@novell.com>
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

# Copying an existing Mail
import time

from ldtp import *
from evoutils.mail import *

# Section to select and copy mail
def copy_mail (from_fldr, to_fldr, mail_index):
	try:
		selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', to_fldr)
		time.sleep (2)
		row_before = getrowcount('frmEvolution-*', 'ttblMessages')
		selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', from_fldr)
		time.sleep (2)
		rowcount = getrowcount('frmEvolution-*', 'ttblMessages') 
		if rowcount > 0:
			if mail_index == -1:
				mail_index = rowcount-1
				
			selectrowindex ('frmEvolution-*', 'ttblMessages', mail_index)
			time.sleep (1)
			selectmenuitem ('frmEvolution-*', 'mnuMessage;mnuCopytoFolder')
			if waittillguiexist ('dlgSelectfolder') == 0:
				log ('Select folder dialog not opened', 'error')
				raise LdtpExecutionError (0)

			selectrowpartialmatch ('dlgSelectfolder','ttblMailFolderTree', to_fldr )
			time.sleep (1)
			click ('dlgSelectfolder', 'btnCopy')
			time.sleep (1)
			if waittillguinotexist ('dlgSelectfolder') == 0:
				log ('Select folder dialog not closed', 'error')
				raise LdtpExecutionError (0)
			else:
				# TODO: Copying a duplicate message has to be handled 
				selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', to_fldr)
				time.sleep (2)
				row_after = getrowcount('frmEvolution-*', 'ttblMessages')
				selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', from_fldr)
				time.sleep (2)
				rowcount_after_copy = getrowcount('frmEvolution-*', 'ttblMessages')
				if row_after == (row_before+1) and rowcount == rowcount_after_copy:
					log ('Copying a mail passed successfully','pass') 
				else:
					log ('Row count does not match after copying', 'cause')
					log ('Copying a mail failed', 'fail')
		else:
			log ('From folder empty!', 'Warning')
			log ('Did not move any mails to other folder', 'Pass')
	except ldtp.error,msg:
		log ('Copying mail between folders failed ' + str(msg), 'cause')
		log ('Copying mail failed','fail')
		raise LdtpExecutionError (0)
			
# Read input from file
data_object = LdtpDataFileParser (datafilename)
from_fldr = data_object.gettagvalue ('from_fldr')
to_fldr = data_object.gettagvalue ('to_fldr')
mail_index = data_object.gettagvalue ('mail_index')

# Call the function
if from_fldr and to_fldr and mail_index:
	copy_mail (from_fldr[0], to_fldr[0], int (mail_index[0]))
else:
	if not(from_fldr): 
		log ('from_fldr is not provided in data xml file', 'error')
	if not(to_fldr):	
		log ('to_fldr is not provided in data xml file', 'error')
	if not(mail_index):	
		log ('mail_index is not provided in data xml file', 'error')
	log ('Copy mail', 'fail')	

