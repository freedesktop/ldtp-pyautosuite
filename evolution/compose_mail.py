#
#  Linux Desktop Testing Project http://ldtp.freedesktop.org
#
#  Authors:
#     Khasim Shaheed <khasim.shaheed@gmail.com>
#
#  Copyright 2004 Novell, Inc.
#
#  This library is free software; you can redistribute it and/or
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

# Compose a new mail through File menu
from evoutils.mail import *
from evoutils.composemail import *
from evoutils.mailpreferences import *
from contact import *

# Section to compose a new mail through File menu
def compose_mail (to, subject, body, cc, bcc, attachment, sentitemsfolder, refimg):
	try:
		if sentitemsfolder:
			sent_folder = sentitemsfolder[0]
		else:
			sent_folder = 'Sent'

		selectrowpartialmatch ('frmEvolution-*', 'ttblMailFolderTree', sent_folder)
		time.sleep (2)
		waittillguiexist ('frmEvolution-'+sent_folder+'*')
		sent_mail_count = getrowcount ('frmEvolution-*', 'ttblMessageList')
		compose (to, subject, body, cc,bcc, attachment)
		sendmail (subject)
		click ('frmEvolution-*', 'btnSend/Receive')
		waittillguinotexist ('dlgSend&ReceiveMail')
		if verifymailwithimage (sent_folder, sent_mail_count, refimg) == 1:
			log ('Compose new message', 'pass')
		else:
			log ('Compose new message', 'fail')

		## check if To and CC are empty with only BCC field having values
		if len (to)==0 and len (cc)==0:
			sub=getcellvalue ('frmEvolution-*','ttblMessageList',sent_mail_count,4)
			if body[0].startswith (sub)==1:
				log ('Message without To and cc contains first line of message as subject','pass')
			else:
				log ('Message without To and cc contains first line of message as subject','fail')

		## check if attachment is received properly
# selectitem () not implemented properly in LDTP. uncomment following lines whe resolved
# 		if len (attachment)>0:
# 			setcontext ('Readonlyframe', subject)
# 			selectmenuitem ('frmEvolution-Mail', 'mnuMessage;mnuOpeninNewWindow')
# 			time.sleep (1)
# 			if waittillguiexist ('frmReadonly') == 0:
# 				log ('Readonlyframe failed to open', 'cause')
# 				raise LdtpExecutionError (0)
			
# 			activatewin (subject)
# 			time.sleep (1)
# 			try:
# 				for x in attachment[0]:
# 					selectitem ('frmReadonly','paneAttachmentBar',x)
#                               releasecontext()
# 			except:
# 				log ('attachments not received properly','error')
# 				raise LdtpExecutionError (0)

	except ldtp.error, msg:
		log ('Compose new message failed ' + str (msg), 'cause')
		log ('Compose message failed', 'fail')
		raise LdtpExecutionError (0)
	
compose_mail (['prashmohan@gmail.com'],'test mail','This is the body of the test email','prashmohan@gmail.com','',[],'Sent','')
