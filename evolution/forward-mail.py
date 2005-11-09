#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
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

# Forward a Mail in different styles
import time

from ldtp import *
from evoutils.mail import *
from evoutils.mailpreferences import *

# Declare global variables
global style, sentitems

# Section to forward mail
def forward_mail (source_fldr, mail_index, to, body, subject_new, cc, refimg):
	try:
		# Change the forward style
		change_style ('Forward', style)
		# forward mail section
		selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', sentitems)
		time.sleep (2)
		n_sentitems = getrowcount ('frmEvolution-Mail', 'ttblMessageList')
		selectrowpartialmatch ('frmEvolution-Mail', 'ttblMailFolderTree', source_fldr)
		time.sleep (2)
		if mail_index == -1:
			mail_index = getrowcount ('frmEvolution-Mail', 'ttblMessageList') - 1
		
		selectrowindex ('frmEvolution-Mail', 'ttblMessageList', mail_index)
		subject = getcellvalue ('frmEvolution-Mail', 'ttblMessageList', mail_index, 4)
		click ('frmEvolution-Mail','btnForward')
		time.sleep (2)
		setcontext ('Compose a message', '[Fwd: '+subject+']')
		if waittillguiexist ('frmComposeamessage') == 0:
			log ('Failed to open forward frame', 'error')
			raise LdtpExecutionError(0)

		if populate_mail_header (to, subject_new, body, cc) == 0:
			log ('Failed to populate mail header', 'error')
			raise LdtpExecutionError (0)
		else:
			if subject_new:
				setcontext ('Compose a message', subject_new[0])

			click ('frmComposeamessage', 'btnSend')
			if waittillguinotexist ('frmComposeamessage') == 0:
				log ('Failed to close Compose dialog after sending','error')
				raise LdtpExecutionError(0)
				
			releasecontext ()
			click ('frmEvolution-Mail', 'btnSend/Receive')
			time.sleep (3)
			if verifymailwithimage (sentitems, n_sentitems, refimg) == 1:
				log ('Forward message Success', 'pass')
			else:
				log ('Forward message', 'fail')
	except ldtp.error, msg:
		log ('Forward messsage Failed ' + str (msg), 'cause')
		log ('Forward Mail Failed', 'fail')
		if guiexist ('frmComposeamessage'):
			selectmenuitem ('frmComposeamessage', 'mnuFile;mnuClose')
		raise LdtpExecutionError (0)

# Reading Input from File
data_object = LdtpDataFileParser (datafilename)
to = data_object.gettagvalue ('to')
cc = data_object.gettagvalue ('cc')
style = data_object.gettagvalue ('style')
subject = data_object.gettagvalue ('subject')
source_fldr = data_object.gettagvalue ('source_fldr')
mail_index = data_object.gettagvalue ('mail_index')
body = data_object.gettagvalue ('body')
sentitemsfolder = data_object.gettagvalue ('sentitemsfolder')
refimg = data_object.gettagvalue ('refimg')

# Initialize global variables
if style:
	style = style[0]
else:
	style = 'Attachment'
if sentitemsfolder:
	sentitems = sentitemsfolder[0]
else:
	sentitems = 'Sent Items'

# Call the function
if source_fldr and mail_index:
	forward_mail (source_fldr[0], int (mail_index[0]), to, body, subject, cc, refimg)
else:
	if not (source_fldr):
		log ('source_fldr is not provided in data xml file', 'error')
	if not (mail_index):
		log ('mail_index is not provided in data xml file', 'error')
	log ('forward mail', 'fail')	

