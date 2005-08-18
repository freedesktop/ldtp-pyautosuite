#!/usr/bin/python
#
#  Linux Desktop Testing Project http://www.gnomebangalore.org/ldtp
#
#  Author:
#     Bhargavi  <kbhargavi_83@yahoo.co.in>
#     Premkumar <jpremkumar@novell.com>
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

# To Reply a Mail using args supplied by a text file

#To reply mail
def reply_mail (source_fldr, mail_index, body, cc=''):
	try:
		time.sleep (3)
		selectmenuitem('evolution','mnuView;mnuWindow;mnuMail')
		time.sleep (15)

		selectrowpartialmatch ('evolution', 'ttblMailFolderTree', source_fldr)
		time.sleep (3)
		if mail_index == -1:
			mail_index = getrowcount ('evolution', 'ttblMessageList') - 1
		selectrowindex ('evolution', 'ttblMessageList', mail_index)
		subject = getcellvalue ('evolution', 'ttblMessageList', mail_index, 4)
		click ('evolution', 'btnReply')
		time.sleep (3)
		if subject.startswith ('Re:') == False:
			setcontext ('Compose a message', 'Re: '+subject)
		else:
			setcontext ('Compose a message', subject)
		time.sleep (5)
		if guiexist ('Composeamessage') == 0:
			log ('Failed to open reply frame', 'error')
			raise LdtpExecutionError (0)
		else:
			new_context = 'Re: '+subject
			if cc!='' and setandverify ('Composeamessage', 'txtCc', cc) == 0:
				log ('Failed to insert into Cc field', 'error')
				raise LdtpExecutionError (0)
			else:
				if setandverify ('Composeamessage', 'txt6', body) == 0:
					log ('Failed to insert body text', 'error')
					raise LdtpExecutionError (0)
				else:
					click ('Composeamessage', 'btnSend')
					time.sleep (5)
					if guiexist ('Composeamessage') == 1:
						log ('Failed to close Compose dialog after sending', 'error')
						raise LdtpExecutionError (0)
					else:
						click ('evolution', 'btnSend/Receive')
						time.sleep (3)
						log ('Reply-message-Success', 'pass')
	except error:
		releasecontext ()
		print 'Reply messsage Failed'
		log('Reply-Mail-Failed','fail')

#Trying to read from the file
file = open('reply-mail.dat', 'r')
argmts = file.readlines ()
Bodytxt_Mail = argmts[0].strip ()
Cc_mailid = argmts[1].strip ()
source_fldr = argmts[2].strip ()
mail_index = argmts[3].strip ()

if source_fldr == '$':
	source_fldr = 'Inbox'
if mail_index == '$':
	mail_index = -1

# Call the function

log('Reply and Verification of Mail','teststart')
log('Reply Mail', 'teststart')
reply_mail (source_fldr, mail_index, Bodytxt_Mail, Cc_mailid)
log('Reply Mail','testend')
log('Reply Mail - Verification', 'teststart')
verifymailwithimage ('Sent Items', -1,'replymail_refimg.png')
log('Reply Mail - Verification', 'testend')
log('ReplyandVerificationofMail', 'testend')
